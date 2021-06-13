from bot import ConversationBot

c = ConversationBot()
c.train()

for sentence in c.get_conversation():
    print(sentence)

c.save("model.p")

c2 = ConversationBot()
c2.load("model.p")

for sentence in c2.get_conversation():
    print(sentence)