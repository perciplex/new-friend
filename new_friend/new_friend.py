from .bot import ConversationBot
import random
import time
from .slack_talker import SlackTalker
import logging
from pathlib import Path

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)
log = logging.getLogger()


def run(channel=None, model_path=None, token=None):
    bot = ConversationBot()

    if not model_path:
        raise Exception("Model path not specified.")
    model_path = Path(model_path)

    talker = SlackTalker(channel, bot.users, token)

    while True:
        for user_id, message in bot.get_conversation():
            talker.say(user_id, message)
            time.sleep(random.randint(1, 4))
        next_convo_sleep_seconds = random.randint(1000, 5000)
        log.info(f"Next convo in {next_convo_sleep_seconds} seconds. Sleeping.")
        time.sleep(next_convo_sleep_seconds)


def train(output_path=None, data_path=None):
    if not output_path:
        output_path = "model.p"
    output_path = Path(output_path)

    if not data_path:
        raise Exception("Data path not specified.")
    data_path = Path(data_path)

    bot = ConversationBot()
    bot.train(data_path)
    bot.save(output_path)