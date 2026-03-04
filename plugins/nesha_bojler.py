from viberbot.api.messages.text_message import TextMessage
from viberbot.api.messages import KeyboardMessage
import requests 



BOJLER_ON={
        "Columns": 6,
        "Rows": 1,
        "BgColor": "#008000",
#       "BgMedia": "https://internet.example.net/b92.png",
#       "BgMediaType": "picture",
#       "BgLoop": True,
        "ActionType": "reply",
        "ActionBody": "bojler 0",
        "ReplyType": "message",
        "Text": "<font color=\"#FFFFFF\"><b>Ukljucen - iskljuci bojler</b></font>",
        "Silent": True
}
BOJLER_OFF={
        "Columns": 6,
        "Rows": 1,
        "BgColor": "#FF0000",
#       "BgMedia": "https://internet.example.net/b92.png",
#       "BgMediaType": "picture",
#       "BgLoop": True,
        "ActionType": "reply",
        "ActionBody": "bojler 1",
        "ReplyType": "message",
        "Text": "<font color=\"#FFFFFF\"><b>Iskljucen - ukljuci bojler</b></font>",
        "Silent": True
}
AUTO_ON={
        "Columns": 6,
        "Rows": 1,
        "BgColor": "#008000",
#       "BgMedia": "https://internet.example.net/b92.png",
#       "BgMediaType": "picture",
#       "BgLoop": True,
        "ActionType": "reply",
        "ActionBody": "bojler a0",
        "ReplyType": "message",
        "Text": "<font color=\"#FFFFFF\"><b>Ukljucena - iskljuci automatiku</b></font>",
        "Silent": True
}
AUTO_OFF={
        "Columns": 6,
        "Rows": 1,
        "BgColor": "#FF0000",
#       "BgMedia": "https://internet.example.net/b92.png",
#       "BgMediaType": "picture",
#       "BgLoop": True,
        "ActionType": "reply",
        "ActionBody": "bojler a1",
        "ReplyType": "message",
        "Text": "<font color=\"#FFFFFF\"><b>Iskljucena - ukljuci automatiku</b></font>",
        "Silent": True
}
KRAJ={

        "Columns": 6,
        "Rows": 1,
        "BgColor": "#00BFFF",
#       "BgMedia": "https://internet.example.net/b92.png",
#       "BgMediaType": "picture",
        "BgLoop": True,
        "ActionType": "reply",
        "ActionBody": "bojler kraj",
        "ReplyType": "message",
        "Text": "<font color=\"#FFFFFF\"><b>KRAJ</b></font>",
        "Silent": True
}

Buttons=[]

def bojler(action):
    del Buttons[:]
    if action == 'on' or action=='1':
       r = requests.post("http://nesha:secret_password@example.net/bojler/index.php", data={'hid': 1, 'status': 1, 'auto': int(requests.get('http://example.net/wemos/auto.txt').text[0])})
    elif action == 'of' or action=='0':
       r = requests.post("http://nesha:secret_password@example.net/bojler/index.php", data={'hid': 1, 'status': 0, 'auto': int(requests.get('http://example.net/wemos/auto.txt').text[0])})
    elif action == 'a1':
       r = requests.post("http://nesha:secret_password@example.net/bojler/index.php", data={'hid': 1, 'auto': 1, 'status': int(requests.get('http://example.net/wemos/one.txt').text[0])})
    elif action == 'a0':
       r = requests.post("http://nesha:secret_password@example.net/bojler/index.php", data={'hid': 1, 'auto': 0, 'status': int(requests.get('http://example.net/wemos/one.txt').text[0])})
    ret='Bojler je '
    if requests.get('http://example.net/wemos/one.txt').text[0]=='0':
       ret += 'OFF'
       Buttons.append(BOJLER_OFF)
    else:
       ret+='ON'
       Buttons.append(BOJLER_ON)
    ret += '\nAutomatika je '
    if requests.get('http://example.net/wemos/auto.txt').text[0]=='0':
       ret += 'OFF'
       Buttons.append(AUTO_OFF)
    else:
       ret += 'ON'
       Buttons.append(AUTO_ON)
    Buttons.append(KRAJ)
    ret += '\nNa dugme (hardwerski) je '
    ret += 'OFF' if requests.get('http://nesha:secret_password@example.net/bojler/older.php').text[0]=='0' else 'ON'
    if action == 'kraj':
       ret += '\n\nNapisati poruku u formatu "bojler 1" (ili "bojler on") za ukljucivanje odnosno "bojler 0" (ili bojler off) \
       za iskljucivanje bojlera, odnosno "bojler a1" za ukljucivanje i "bojler a0" za iskljucivanje automatike'
    return ret

#https://developers.viber.com/docs/tools/keyboards/
def rep(text):
    if text.lower()[0:6] == 'bojler':
        #yield TextMessage(text=bojler(text.lower()[7:9]))
        tekst=bojler(text.lower()[7:9])
        SAMPLE_KEYBOARD = {
          "Type": "keyboard",
          "Buttons": Buttons
        }
        if text.lower()[7:11] != "kraj":
           yield KeyboardMessage(tracking_data='tracking_data', keyboard=SAMPLE_KEYBOARD)
        else:
           yield TextMessage(text=tekst)
        yield 'stop_'
