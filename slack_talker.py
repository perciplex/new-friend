import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import json
import numpy as np
from pathlib import Path

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

TOKEN = os.getenv("SLACK_TOKEN")


class SlackTalker:
    def __init__(self, channel_id):
        self.client = WebClient(token=TOKEN)
        self.channel_id = channel_id

        path = Path("data") / "fpff_slack" / "users.json"
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
            # Call the chat.postMessage method using the WebClient
            result = self.client.chat_postMessage(
                channel=self.channel_id,
                text=text,
                username=self.users.get(user_id).get("profile").get("display_name")
                or self.users.get(user_id).get("profile").get("real_name"),
                icon_url=self.users.get(user_id).get("profile").get("image_72"),
            )

        except SlackApiError as e:
            print(f"Error posting message: {e}")