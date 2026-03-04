from viberbot.api.messages.text_message import TextMessage

def rep(text):
    if text.lower()[0:3] == 'rac':
        yield TextMessage(text="265000000007062771 Nebojsa Milovanovic")
        yield TextMessage(text="205900101845340022 Tanja Milovanovic")
        yield TextMessage(text="265000000036422343 Ivana Vlahovic")
        yield TextMessage(text="200000003781387785 Radmila Tomovic")
        yield 'stop_'
