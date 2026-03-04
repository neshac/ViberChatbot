from viberbot.api.messages.text_message import TextMessage
#python3
#import subprocess as sp
#python2
import commands as sp
import re

def tracer(host,interface,hop):
    return re.search(host,sp.getstatusoutput("traceroute -m "+str(hop)+" -i "+interface+" 8.8.8.8")[1].split('\n')[-1].lower()) 

def walk(octet):
    return sp.getstatusoutput("snmpwalk -c gonzales -v 2c 212.102.128.1 IF-MIB::"+octet)[1].split(' ')[-1]	

def rep(text):
    rep=''		
    if text.lower()[0:4] == 'link':
        telekom_in = walk("ifHCInOctets.11")
        telekom_out= walk("ifHCOutOctets.11")
        akton_in = walk("ifHCInOctets.6")
        akton_out= walk("ifHCOutOctets.6")
        
        if tracer('akton','eth0',2):
           #if (walk("ifHCInOctets.6") > akton_in) and (walk("ifHCOutOctets.6")[1].split(' ')[-1] > akton_out):
           if (walk("ifHCInOctets.6") > akton_in) and (walk("ifHCOutOctets.6") > akton_out):
              rep+="Akton UP"
           else:
              rep+="Akton ruta UP, saobracaj ne radi"
        else:
           rep+="Akton ruta DOWN" 
        rep+="\n"
        
        if tracer('telekom','eth1',4):
           #if (walk("ifHCInOctets.11") > telekom_in) and (walk("ifHCOutOctets.11")[1].split(' ')[-1] > telekom_out):
           if (walk("ifHCInOctets.11") > telekom_in) and (walk("ifHCOutOctets.11") > telekom_out):
              rep+="Telekom UP"
           else:
              rep+="Telekom ruta UP, saobracaj ne radi"
        else:
           rep+="Telekom ruta DOWN" 
        rep+="\n"
        
        yield TextMessage(text=rep)
        yield 'stop_'
