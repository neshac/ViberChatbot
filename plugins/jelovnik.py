from viberbot.api.messages import PictureMessage
import urllib
import re

def rep(text):
    if text.lower()[0:4] == 'jelo':
        yield PictureMessage(media="https://example.net/images/jelovnik.jpg" , text="Jelovnik NBGD Lido")
        yield 'stop_'
