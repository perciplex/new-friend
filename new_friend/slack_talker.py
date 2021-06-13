import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import json
from pathlib import Path
import logging

log = logging.getLogger()


DEFAULT_DATA_PATH = Path(__file__).parent.parent / "data"
DEFAULT_CHANNEL = "app-test"


WHITELIST = [
    "U1P9EE03G",
    "U1P9FQQRL",
    "U1PMZHL49",
    "U1PPEPJTT",
    "U1PRD7UV6",
    "U1SF4QG4E",
    "U1SFW60F4",
    "U1YUGM7RQ",
    "U1Z8T3Q7J",
    "U29BL3VDW",
    "U2PP3NN3V",
    "U3LA6SYAE",
    "U01065Z0FDF",
    "U016HPSKSTW",
    "U015C5HPPFS",
]

shortid_to_userid = {user_id[-5:]: user_id for user_id in WHITELIST}


class SlackTalker:
    def __init__(self, channel, token=None):
        # if token is not specified, try getting it from env vars
        if token is None:
            token = os.getenv("SLACK_TOKEN")

        if channel is None:
            channel = DEFAULT_CHANNEL

        self.client = WebClient(token=token)
        self.channel = channel

        path = DEFAULT_DATA_PATH / "users.json"
        with open(path, "r") as f:
            self.users = {user.get("id"): user for user in json.load(f)}

    def say(self, user_id, text):
        if len(user_id) == 5:
            user_id = shortid_to_userid.get(user_id)

        if user_id not in WHITELIST:
            return

        if self.users.get(user_id).get("is_bot"):
            return

        try:
            # call the chat.postMessage method using the WebClient
            self.client.chat_postMessage(
                channel=self.channel,
                text=text,
                username=(
                    self.users.get(user_id).get("bot_name") or
                    self.users.get(user_id).get("profile").get("display_name") or 
                    self.users.get(user_id).get("profile").get("real_name")
                    ),
                icon_url=self.users.get(user_id).get("profile").get("image_72"),
            )

<<<<<<< HEAD:new_friend/slack_talker.py
        except SlackApiError:
            log.exception(f"Error posting message: {e}")
=======
        except SlackApiError as e:
            print(f"Error posting message: {e}")
>>>>>>> 7a4b8ce2b817cb4d034c8e2409441bd379ec75fc:slack_talker.py
