from viberbot.api.messages import PictureMessage
import time
#python3
#import subprocess as sp
#python2
import commands as sp

def sendcam(source, filename):
    status,result = sp.getstatusoutput("/usr/local/bin/scripts/campic " + source + " " + filename)
    return status

def rep(text):
    if text.lower()[0:4] == 'dust':
        filename=str(time.time())+'.jpg'
        if sendcam('http://gateway.nb.example.net/mrtg/nesha-dust-day.png', filename) == 0:
            yield  PictureMessage(media="https://example.net/images/"+filename , text="Dust")
            yield 'stop_'
