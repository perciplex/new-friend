import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import json
from pathlib import Path
import logging

log = logging.getLogger()


class SlackTalker:
    def __init__(self, channel, users, token=None, dry_run=False):
        """An object for posting messages to Slack."""
        self.users = users
        self.dry_run = dry_run
        if dry_run:
            return

        # if token is not specified, try getting it from env vars
        if token is None:
            token = os.getenv("SLACK_TOKEN")

        if channel is None:
            raise Exception("Channel not specified.")

        self.client = WebClient(token=token)
        self.channel = channel

    def say(self, user_id, text):
        """Post a message to Slack."""
        if len(text) == 0:
            return

        user = self.users.get(user_id)
        if not user or user.get("is_bot"):
            return

        user_profile = user.get("profile", {})
        user_icon = user_profile.get("image_72")

        username = (
            user.get("new_friend_name")
            or user_profile.get("display_name")
            or user_profile.get("real_name")
        )

        # if a dry run, don't call slack
        if self.dry_run:
            print(f"{username}: {text}")
            return

        # call the chat.postMessage method using the WebClient
        self.client.chat_postMessage(
            channel=self.channel,
            text=text,
            username=username,
            icon_url=user_icon,
        )
