from viberbot.api.messages.text_message import TextMessage
import requests 
from lxml import html

def stopkam():
    try:
       response=requests.get('http://10.0.0.2/vk.php?pass=passrod')
       if response.status_code != 200:
           raise
       return "na 3 min"
    except:
       return "Ne radi"

def rep(text):
    if text.lower()[0:3] == 'ska':
        yield TextMessage(text=stopkam())
        yield 'stop_'
