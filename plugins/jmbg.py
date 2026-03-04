from viberbot.api.messages.text_message import TextMessage

def rep(text):
    if text.lower()[0:4] == 'jmbg':
        rep= "0609982710000 John Smith\n"
        rep+="3101987750000 Lola Smith\n"
        rep+="1405028710000 Alex Smith\n"
        rep+="2008032750000 Shadow Milovanovic"
        yield TextMessage(text=rep)
        yield 'stop_'
