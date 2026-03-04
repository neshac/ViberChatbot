from viberbot.api.messages.text_message import TextMessage
import requests 


def bojler(action):
    if action == 'on' or action=='1':
       r = requests.post("http://nesha:secret_password@nesha.net/bojler/index.php", data={'hid': 1, 'status': 1, 'auto': int(requests.get('http://nesha.net/wemos/auto.txt').text[0])})
    elif action == 'of' or action=='0':
       r = requests.post("http://nesha:secret_password@nesha.net/bojler/index.php", data={'hid': 1, 'status': 0, 'auto': int(requests.get('http://nesha.net/wemos/auto.txt').text[0])})
    elif action == 'a1':
       r = requests.post("http://nesha:secret_password@nesha.net/bojler/index.php", data={'hid': 1, 'auto': 1, 'status': int(requests.get('http://nesha.net/wemos/one.txt').text[0])})
    elif action == 'a0':
       r = requests.post("http://nesha:secret_password@nesha.net/bojler/index.php", data={'hid': 1, 'auto': 0, 'status': int(requests.get('http://nesha.net/wemos/one.txt').text[0])})
    ret='Bojler je '
    ret += 'OFF' if requests.get('http://nesha.net/wemos/one.txt').text[0]=='0' else 'ON'
    ret += '\nAutomatika je '
    ret += 'OFF' if requests.get('http://nesha.net/wemos/auto.txt').text[0]=='0' else 'ON'
    ret += '\nNa dugme (hardwerski) je '
    ret += 'OFF' if requests.get('http://nesha:secret_password@nesha.net/bojler/older.php').text[0]=='0' else 'ON'
    ret += '\n\nNapisati poruku u formatu "bojler 1" (ili "bojler on") za ukljucivanje odnosno "bojler 0" (ili bojler off) \
    za iskljucivanje bojlera, odnosno "bojler a1" za ukljucivanje i "bojler a0" za iskljucivanje automatike'
    return ret


def rep(text):
    if text.lower()[0:6] == 'lerboj':
        yield TextMessage(text=bojler(text.lower()[7:9]))
        yield 'stop_'
