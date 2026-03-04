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
    if text.lower()[0:2] == 'dj' or text.lower()[0:7] == "parking":
        filename=str(time.time())+'.jpg'
        if sendcam('http://10.5.13.52/cgi-bin/image.jpg', filename) == 0:
            yield  PictureMessage(media="https://example.net/images/"+filename , text="Parking kontejneri")
            yield 'stop_'
