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
    if text.lower()[0:4] == 'prij':
        filename1=str(time.time())
        filename2=filename1
        filename1+='pa.jpg'
        filename2+='pb.jpg'
        stop=False
        if sendcam('http://10.5.13.55/cgi-bin/image.jpg?display_mode=simple\&rotate=180', filename1) == 0:
            stop=True
            yield  PictureMessage(media="https://example.net/images/"+filename1 , text="B92 Prijavnica")
        if sendcam('http://admin:camera_password@10.5.13.62/cgi-bin/image.jpg?display_mode=simple\&rotate=180', filename2) == 0:
            stop=True
            yield PictureMessage(media="https://example.net/images/"+filename2 , text="Prva Prijavnica")      
        if stop:
            yield 'stop_'
