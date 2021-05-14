import markov
import json
from pathlib import Path
from datetime import datetime, timedelta


def get_all_data():
    """lookup all json files and load them all into a dictionary and return it"""
    p = Path("data/fpff_slack")
    data = {}
    for path in p.glob("**/*.json"):
        # print(path)
        try:
            with open(path, "r") as f:
                data[path] = json.load(f)
        except:
            print(path)

    return data


def keep_string(input_str: str) -> bool:
    if "https:" in input_str:
        return False
    else:
        return True


def train_conversation_sentence_bot():

    data = get_all_data()

    conversation_list = []
    current_conversation = []
    IDLE_TIME_THRESHOLD_SECONDS = 3600
    last_time = 0
    word_to_stylized_words_and_counts = {}
    for k, msgs in data.items():
        for msg in msgs:
            user = msg.get("user")
            text = msg.get("text")
            time = msg.get("ts")
            if user is None or text is None or time is None:
                continue
            time = float(time)

            gap_time = time - last_time
            if (gap_time > IDLE_TIME_THRESHOLD_SECONDS) or (gap_time < 0):
                if current_conversation:
                    conversation_list.append(current_conversation)
                current_conversation = []

            last_time = time

            text_words = text.split(" ")
            text_words = [w for w in text_words if keep_string(w)]

            if len(text_words) == 0:
                continue

            text_words.append("___SEND__")
            text_words_userified = [w + user[-5:] for w in text_words]

            current_conversation += text_words_userified

    text_model = markov.Chain(conversation_list, 2)

    return text_model