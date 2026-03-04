from viberbot.api.messages.text_message import TextMessage
#python3
#import subprocess as sp
#python2
import commands as sp

ip_hosts={
    "gateway.example.net",
    "tequila.example.net",
    "mail.example.net",
    "udba.example.net",
    "ftp.example.net",
    "internet.example.net",
    "backup.nb.example.net",
    "sisoje.nb.example.net",
    "stream.example.net",
    "web.example.net",
    "oracle.nb.example.net",
    "videopirat.example.net"
}

def ipcheck(host):
    status,result = sp.getstatusoutput("ping -c1 -w2 " + str(host))
    return status

def ping(host):
    rep=''
    if ipcheck(host) == 0:
        rep+="UP - System " + str(host) + "\n"
    else:
        rep+="(!)(Q)OOPS DOWN - System " + str(host) + " (surprised)\n"
    return rep
	

def rep(text):
    rep=''		
    if text.lower()[0:4] == 'ping':
        for host in ip_hosts:
            rep+=ping(host)

        yield TextMessage(text=rep)
        yield 'stop_'
