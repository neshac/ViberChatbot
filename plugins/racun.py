from viberbot.api.messages.text_message import TextMessage

def rep(text):
    if text.lower()[0:3] == 'rac':
        yield TextMessage(text="265000000007000000 John Smith")
        yield TextMessage(text="205900100000000000 Lola Smith")
        yield TextMessage(text="265000000030000000 Ivanho Vlah")
        yield TextMessage(text="200000003000000000 Rada Toms")
        yield 'stop_'
