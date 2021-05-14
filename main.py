import markov
import mm_utils
import random
import time
import slack_talker

model = markov.Chain.from_json("model.json")

talker = slack_talker.SlackTalker("app-test")
for _ in range(10):
    conversation = model.walk()
    message = []
    for word in conversation:
        user_id_short = word[-5:]
        text = word[:-5]
        if text == "___SEND__":
            print(user_id_short, " ".join(message))
            talker.say(user_id_short, " ".join(message))
            time.sleep(random.randint(1, 2))
            message = []
            continue
        message.append(text)
    time.sleep(random.randint(10, 15))