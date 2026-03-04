from viberbot.api.messages.text_message import TextMessage

def rep(text):
    if text.lower()[0:4] == 'jmbg':
        rep= "0609972710029 Nebojsa Milovanovic\n"
        rep+="3101977738514 Tanja Milovanovic\n"
        rep+="1405008710124 Aleksa Milovanovic\n"
        rep+="2008012715283 Senka Milovanovic"
        yield TextMessage(text=rep)
        yield 'stop_'
