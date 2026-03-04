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
    if text.lower()[0:4] == 'gara':
        filename1=str(time.time())
        filename2=filename1
        filename1+='ga.jpg'
        filename2+='gb.jpg'
        stop=False
        if sendcam('http://10.5.13.53/cgi-bin/image.jpg', filename1) == 0:
            stop=True
            yield  PictureMessage(media="https://example.net/images/"+filename1 , text="Garaza") 
        if sendcam('http://10.5.13.71/record/current.jpg', filename2) == 0:
            stop=True
            yield PictureMessage(media="https://example.net/images/"+filename2 , text="Zica")      
        if stop:
            yield 'stop_'
