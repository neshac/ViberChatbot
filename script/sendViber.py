#!/usr/bin/env python

import sys, requests

PATH="https://viberbot.example.net:8080/send"
PASSWORD="secret_password"

TEXT=sys.argv[1]
RECIP=[]
for i in range(2,len(sys.argv)):
  RECIP.append(sys.argv[i])

#print(PATH,PASSWORD,RECIP,TEXT)
requests.post(PATH, json={"password":PASSWORD,"recipients":RECIP,"text":TEXT})
