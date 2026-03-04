from viberbot.api.messages.text_message import TextMessage
import requests 
from lxml import html

def servertemp():
    try:
       response=requests.get('http://10.0.0.2/ups.txt')
       if response.status_code != 200:
           raise
       temp = response.text
       return "UPS\n(termometer){}C".format(temp)
    except:
       return "Ne mogu da ocitam vrednost"

def rep(text):
    if text.lower()[0:3] == 'ups':
        yield TextMessage(text=servertemp())
        yield 'stop_'
