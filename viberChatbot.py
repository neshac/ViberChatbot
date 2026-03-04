# by Nebojsa Milovanovic 2019
# nesha@nesha.net

from flask import Flask, render_template, request, send_file, Response, Blueprint
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import PictureMessage
from viberbot.api.messages import VideoMessage
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest
import time
import logging
import urllib
import re
import json
import requests 
import hashlib
import os
#python3
#import subprocess as sp
#python2
import commands as sp
from os.path import dirname, join, isdir, abspath, basename
from glob import glob
#import __builtin__

NESHA='xxxxxxxxxxxxxxxxxxxxxx=='
USER2='xxxxxxxxxxxxxxxxxxxxxx=='
USER3='xxxxxxxxxxxxxxxxxxxxxx=='
USER4='xxxxxxxxxxxxxxxxxxxxxx=='
USER5='xxxxxxxxxxxxxxxxxxxxxx=='

ADMINS=[NESHA]

MAX_LOGS=50


access={
    "log":[NESHA]
}


#logger = logging.getLogger(__name__)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

#app = Flask(__name__)
uzbunkoBot = Blueprint('uzbunkoBot', __name__)
viber = Api(BotConfiguration(
    name='Uzbunko',
    avatar='https://example.net/viber/avatar.png',
    auth_token='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
))


messages_tokens=set()
logs=[]

def my_import(name):
    m = __import__(name)
    for n in name.split(".")[1:]:
       m = getattr(m, n)
    return m

def retlogs():
    ret=''
    for i in logs:
       ret+=i[2]+' - '+i[0]+' '+i[1]+'\n'
    return ret

def reply(name,text,id):
    rep=''
    udir='u'+hashlib.md5(id.encode()).hexdigest()
    pwd = dirname("uzbunko/users/"+udir+"/")
    #logger.debug("________________DEBUG__PWD______________: {0}".format(basename(pwd)))
    #try:       
    for x in glob(join(pwd, '*.py')):
       if not basename(x).startswith('__'):
          #logger.debug("________________DEBUG________________: {0}".format(basename(x)))
          stop=False
          try:
             if text.lower()[0:4] == 'help' or text.lower()[0:4] == 'info':
                rep += re.split(r"[^a-zA-Z0-9]*",basename(x)[:-3])[-1]+'\n'
             else:      
                #m = my_import(x.replace('/','.')[:-3])
                #m = my_import('plugins.'+basename(x)[:-3])
                if os.path.islink(x):
                   #m = my_import(os.readlink(x).replace('../../..','',1).replace('/','.')[:-3])
                   m = my_import(os.readlink(x).replace('../../',x.split('/')[0]+'/').replace('/','.')[:-3])
                   for r in m.rep(text):
                      if stop and r=='stop_':
                         return
                      else:
                         stop=True
                         yield r
          except Exception as e:
             logger.warn("_______PLUGIN__EXCEPTION________: {0}".format(e))
             rep=''
    #except Exception as e:
    # logger.warn("__EXCEPTION__: {0}".format(e))
    # rep=''       
    if id in access['log'] and (text.lower()[0:3] == 'log'):
       rep=retlogs()
    if not rep:
       rep = 'Cao '+ name +'. Napisao/la si: '+text    
    yield TextMessage(text=rep)
    return

@uzbunkoBot.route('/incoming', methods=['POST'])
def incoming():
    logger.debug("received request. post data: {0}".format(request.get_data()))
    # every viber message is signed, you can verify the signature using this method
    if not viber.verify_signature(request.get_data(), request.headers.get('X-Viber-Content-Signature')):
        return Response(status=403)

    # this library supplies a simple way to receive a request object
    viber_request = viber.parse_request(request.get_data())

    # avoid receive duplicate message
    if hasattr(viber_request, 'message_token' ) and (viber_request.message_token in messages_tokens):
        logger.warn("avoid receiving duplicate message for message_token: " + str(viber_request.message_token))
    else:
        if isinstance(viber_request, ViberMessageRequest):
            #message = viber_request.message   
            # lets back
            try:
                if viber_request.sender.id not in ADMINS:
                    logs.append([time.strftime("%Y.%m.%d %H:%M:%S"),viber_request.sender.name.split(' ')[0],viber_request.message.text])
                    if len(logs)>=MAX_LOGS:
                        logs.pop(0)
            except:
                logger.warn("Cannot append in logs") 
            for rep in reply(viber_request.sender.name,viber_request.message.text,viber_request.sender.id):        
                viber.send_messages(viber_request.sender.id, [rep])
        elif isinstance(viber_request, ViberSubscribedRequest):
            viber.send_messages(viber_request.get_user.id, [
                TextMessage(text="Uspesno ste se prijavili!")
            ])
        elif isinstance(viber_request, ViberFailedRequest):
            logger.warn("client failed receiving message. failure: {0}".format(viber_request))
        if hasattr(viber_request, 'message_token' ):    
            messages_tokens.add(viber_request.message_token)

    return Response(status=200)

def set_webhook(viber_bot):
    viber_bot.set_webhook('https://viberbot.example.net:8080/incoming')
    #viber_bot.set_webhook('https://viberbot.example.net/flask/incoming')
    logging.info("Web hook has been set")

@uzbunkoBot.route('/send', methods=['POST'])
def send():
    #send viber text message with:
    #requests.post("https://SERVER:PORT/send", json={"password":"password","recipients":["NESHA"],"text":"Sample text"})
    req=request.get_json(force=True)
    if req.get('password')=='secret_password' and req.get('recipients') and req.get('text'):
        for i in req.get('recipients'):
            if globals().get(i):
                viber.send_messages(globals().get(i), [
                    TextMessage(text=req.get('text'))
                ])
        return Response(status=200)
    else:
        return Response(status=403)

#@uzbunkoBot.route('/images/image.jpg')
#def image():
#   return uzbunkoBot.send_static_file('/images/image.jpg')
#   #return render_template('/images/image.jpg')
   
#set_webhook(viber)   
#if __name__ == "__main__":
#    context = ('server.crt', 'server.key')
#    app.run(host='admin.b92.net', port=8080, debug=True, ssl_context=context)
#    #app.run(debug = True)
 