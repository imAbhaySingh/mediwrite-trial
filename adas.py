import mysql.connector as sc
import pywhatkit
import datetime
from flask import Flask, request
from flask_cors import CORS, cross_origin

current_time=datetime.datetime.now()
hour=current_time.hour
minute=current_time.minute

def sendMessage(__aadhNr,__cause): #NOTE: __aadhNr is a float 
    mycon=sc.connect(host="localhost",user="root",passwd="root",database="mediwrite")

    c=mycon.cursor()
    c.execute("select aadhaar from aadhaar;")
    e=c.fetchall()
    d=list(e)
    print(d)

    c.execute("select address from aadhaar;")
    add=c.fetchall()
    addlist=list(add)

    c.execute("select mobno from aadhaar;")
    mob=c.fetchall()
    moblist=list(mob)
    
    c.execute("select name from aadhaar;")
    name=c.fetchall()
    namelist=list(name)

    a=__aadhNr
    b="("+str(a)+","+")"
    
    for i in range(3):
        if b == str(d[i]):
            addvar=addlist[i]
            namevar=namelist[i]
            print(addlist[i])
            for j in range(3):
                if addlist[j]==addvar:
                    mobvar=moblist[j]
                    print(moblist[j])
                    pywhatkit.sendwhatmsg(f"+91{mobvar[0]}" , f"Your relative {namevar[0]} has been admitted to the hospital due to {__cause}",hour,minute+3)
                else:
                    break
        else:
            break
sendMessage(aadharNr,cause)
