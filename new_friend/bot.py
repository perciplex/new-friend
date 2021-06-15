from .markov import Chain, SEND
import json
import pickle
import gzip
import logging

log = logging.getLogger()

IDLE_TIME_THRESHOLD_SECONDS = 3600


class ConversationBot:
    def __init__(self):
        pass

    def read_files(data_path, max_files):
        """Generator for decoded json."""
        for i, path in enumerate(data_path.glob("**/*.json")):
            if max_files and i > max_files:
                return
            try:
                with open(path, "r", encoding="utf8") as f:
                    yield json.load(f)
            except Exception:
                log.warning(f"Failed to read data file {path}.")

    def save(self, path):
        """Dump the model as a JSON object, for loading later."""
        log.info(f"Saving model to {path.absolute()}.")
        pickle.dump((self.model, self.users), gzip.open(path, "wb"))

    def load(self, path):
        """Dump the model as a JSON object, for loading later."""
        log.info(f"Reading model from {path.absolute()}.")
        self.model, self.users = pickle.load(gzip.open(path, "rb"))

    def get_conversation(self):
        """Generator for messages in a new conversation."""
        current_user = None
        conversation = self.model.walk()
        sentence = []
        for word, user in conversation:
            if current_user and word == SEND:
                yield user, " ".join(sentence)
                sentence = []
            else:
                sentence.append(word)
            current_user = user

    def train(self, data_path, max_files=None):
        """Use the json files to train the Markov model."""
        conversation_list = []
        current_conversation = []
        last_time = 0

        users_path = data_path / "users.json"
        with open(users_path, "r") as f:
            self.users = {user.get("id"): user for user in json.load(f)}

        for file in ConversationBot.read_files(data_path, max_files):
            for msg in file:
                user = msg.get("user")
                text = msg.get("text")
                time = msg.get("ts")

                # check that we have a valid message
                if (not user) or (not text) or (not time):
                    continue
                time = float(time)

                # if enough time has passed, save the old conversation and start a new one
                gap_time = time - last_time
                if (gap_time > IDLE_TIME_THRESHOLD_SECONDS) or (gap_time < 0):
                    if current_conversation:
                        conversation_list.append(current_conversation)
                    current_conversation = []
                last_time = time

                text_words = text.split(" ")
                text_words = [word for word in text_words if word]

                if len(text_words) == 0:
                    continue

                text_words.append("___SEND__")
                text_words_userified = [(w, user) for w in text_words]

                current_conversation += text_words_userified

        self.model = Chain(conversation_list, 2)