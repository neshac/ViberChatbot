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
    if text.lower()[0:3] == 'b92':
        filename=str(time.time())+'.jpg'
        if sendcam('http://10.5.17.50/image1.jpg', filename) == 0:
            yield  PictureMessage(media="https://example.net/images/"+filename , text="B92 rezija MultiViewer")
            yield 'stop_'
