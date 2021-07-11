# NewFriend

This is a Slackbot that can be trained on your Slack history to emulate your friends and coworkers to great amusement for all. 

## How does it work?
It trains a Markov chain and produces conversations based on those in your workspace.
It uses the https://github.com/jsvine/markovify library as core Markov chain functionality.

## How do I do it?
You need to be an administrator of your Slack workspace to use NewFriend.

### Install
First, clone this repo and install:
```bash
git clone https://github.com/perciplex/new-friend.git
cd new-friend
pip install .
```

### Train
To train, you'll need download the conversation history for your Slack workspace. You can do this by following the instructions here:
https://slack.com/help/articles/201658943-Export-your-workspace-data

Extract the resulting zip file into a directory. It should contain (among other things) a sub-directory for each channel and a `user.json` containing data about each user. If there's anyone humorless in your workspace, you should delete their entry from `users.json` to prevent their _replacement_ from speaking.

To train the Markov model run
```bash
python3 -m new_friend train --data <export_data_path> --out model.p
```

### Test
Test the model with 
```bash
python -m new_friend run --model model.p --dry-run
```

### Setup the bot
To run the model you need create a Slack app and add a bot token with the following scopes:
* `chat:write` -- write messages in chats
* `chat:write.customize` -- write messages with a custom name and icon (an `app` badge will appear to distinguish from real users)
* `chat:write.public` -- write messages in any channel

For info on how to create a Slack app with bot permissions, check here:
https://slack.com/help/articles/115005265703-Create-a-bot-for-your-workspace


### Run
Grab the Bot User OAuth Token and press go:
```bash
python3 -m new_friend run --model model.p --channel <channel> --token <bot_user_oauth_token>
```

We recommend posting directly to `#general` without testing it or warning anyone.