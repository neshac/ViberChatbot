#!/usr/bin/python

from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import VideoMessage
from viberbot.api.messages.text_message import TextMessage
import logging

from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest


logger = logging.getLogger(__name__)

viber = Api(BotConfiguration(
    name='PythonSampleBot',
    avatar='https://internet.example.net/viber/avatar.png',
    auth_token='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
))

viber.set_webhook('https://viberbot.example.net/flask/incoming') 
