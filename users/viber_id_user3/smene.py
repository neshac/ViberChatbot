from viberbot.api.messages.text_message import TextMessage
#from flask import url_for
import re
import requests 
import datetime
import EmployeeSchedule

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""

def rep(text):
    if text.lower()[0:3] == 'sme':
        ##url=url_for('emSch.show', _external=True)
        ##s=requests.get(url).text
        #s=EmployeeSchedule.show()
        #tekst=re.sub("<br>",", druga: ",find_between(find_between( s, "<tr bgcolor=\"#ffffff\">", "</tr>" ),"&nbsp;<br>","</td>"))[:-9]
        #if tekst[-1]==' ':
        #  tekst="ceo dan: "+tekst[:-9]
        #else:
        #  tekst="prva: " + tekst
        #yield TextMessage(text=tekst)
        #yield 'stop_'
        #
        date=datetime.datetime.utcnow()
        tekst="danas:\n"+EmployeeSchedule.koradi(date)+"\n\n"
        for i in range(1,7):
           tekst+=EmployeeSchedule.koradi(date+datetime.timedelta(days=i))+"\n"
        yield TextMessage(text=tekst)
        yield 'stop_'