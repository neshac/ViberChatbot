from viberbot.api.messages import PictureMessage
import urllib
import re

def rep(text):
    if text.lower()[0:4] == 'radi':
        yield PictureMessage(media="https://redata.jrc.ec.europa.eu/chart/timeseries/daily/RS0005" , text="Vinca")
        yield PictureMessage(media="https://redata.jrc.ec.europa.eu/chart/timeseries/hourly/RS0005" , text="Vinca")
        yield 'stop_'
