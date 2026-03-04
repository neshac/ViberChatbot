from viberbot.api.messages.text_message import TextMessage
import requests 

def neshatemp():
    try:
       response = requests.get("http://192.168.69.15/temp")
       if response.status_code != 200:
           raise
       line = response.text.split('\n')
       return "Dnevna soba\n(termometer){}C\n(droplet){}%".format(line[0],line[1])
    except:
       return "Ne radi senzor"


def rep(text):
    if text.lower()[0:4] == 'temp':
        yield TextMessage(text=neshatemp())
        yield 'stop_'
