import os
import redisfind
import mongodbfind
import time
import datetime

def insert():
    user = raw_input('what is your username ')
    password = raw_input('what is your password ')
    user = int(user)
    #user = 5
    #password = '1234'
    user = int(user)
    print 'Process (%s) start...' % os.getpid()
    pid = os.fork()
    if pid==0:
        redisfind.resultcache(user,password)
    else:
        mongodbfind.inseruser(user,password)

def delete():
    user = raw_input('what username you want delete ')
    user = int(user)

    pid = os.fork()
    if pid==0:
        redisfind.deleteuser(user)
    else :
        mongodbfind.deleteuser(user)