import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import json
from pathlib import Path
import logging

log = logging.getLogger()

DEFAULT_CHANNEL = "app-test"

class SlackTalker:
    def __init__(self, channel, users, token=None):
        # if token is not specified, try getting it from env vars
        if token is None:
            token = os.getenv("SLACK_TOKEN")

        if channel is None:
            channel = DEFAULT_CHANNEL

        self.client = WebClient(token=token)
        self.channel = channel

        self.users = users

    def say(self, user_id, text):

        if self.users.get(user_id).get("is_bot"):
            return

        if len(text) == 0:
            return

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
            
