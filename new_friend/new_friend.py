from .bot import ConversationBot
import random
import time
from .slack_talker import SlackTalker
import logging
from pathlib import Path

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)
log = logging.getLogger()

DEFAULT_MODELS_PATH = Path(__file__).parent.parent / "models"
DEFAULT_MODEL_FILE = "model.p"


def run(channel=None, model_path=None, train=False, token=None):
    bot = ConversationBot()

    if train:
        log.warning(f"Training enabled. Ignoring model path.")
        bot.train()
    else:
        if not model_path:
            model_path = DEFAULT_MODEL_FILE
            log.warning(f"No model file specified. Using default {DEFAULT_MODEL_FILE}")
        bot.load(DEFAULT_MODELS_PATH / model_path)

    talker = SlackTalker(channel, token)

    while True:
        for user_id, message in bot.get_conversation():
            talker.say(user_id, message)
            time.sleep(random.randint(1, 4))
        time.sleep(random.randint(1000, 5000))


def train(output_path=None):
    if not output_path:
        output_path = DEFAULT_MODELS_PATH/DEFAULT_MODEL_FILE

    bot = ConversationBot()
    bot.train()
    bot.save(output_path)