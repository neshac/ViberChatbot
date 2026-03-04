from viberbot.api.messages.text_message import TextMessage
import requests 
from lxml import html

def servertemp():
    try:
       response=requests.get('http://10.5.13.13/export.csv')
       if response.status_code != 200:
           raise
       temp = html.fromstring(response.text).text.split(',')[7]
       return "Serverska soba\n(termometer){}C".format(temp)
    except:
       return "Ne radi senzor u serverskoj sobi"

def rep(text):
    if text.lower()[0:4] == 'temp' or text.lower()[0:5] == 'stemp':
        yield TextMessage(text=servertemp())
        yield 'stop_'
