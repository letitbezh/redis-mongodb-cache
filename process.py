import os
import redisfind
import mongodbfind
import time
import datetime

def find():
    user = raw_input('what is your username ')
    password = raw_input('what is your password ')
    user = int(user)

    r,w = os.pipe()
    print 'Process (%s) start...' % os.getpid()
    pid = os.fork()
    if pid==0:
        flagredis = 0
    #print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
    
    #flagredis = redisfind.checkpassword(4,'123456')
        print datetime.datetime.now()
        flagredis = redisfind.checkpassword(user,password)
        print 'end redis', datetime.datetime.now()
        if(flagredis==1):
            print "hello redis"
            flagredis = 1
        elif(flagredis==2):
            print "wrong"
        else:
            print "wait mongodb"
        #mongodbcache = {u'password': u'123456', u'user': 2}
        #redisfind.resultcache(mongodbcache['user'],mongodbcache['password'])
            os.close(w)
            r= os.fdopen(r)
            stra = r.read()
            if stra=='None':
                print 'no user'
            else:
                print stra
                mongodbcache = eval(stra)
                redisfind.resultcache(mongodbcache['user'],mongodbcache['password'])
                flagredis = 1
        return flagredis
    else:
    #resultmongodb = mongodbfind.checkpassword(4,'123456')
        print 'start', datetime.datetime.now()
        resultmongodb = mongodbfind.checkpassword(user,password)
        print 'end', datetime.datetime.now()
        print resultmongodb
        if resultmongodb==None:
            print 'no user'
            os.close(r)
            w=os.fdopen(w,'w')
            w.write('None')
        else:
            flagmongodb = resultmongodb[0]
            dictmongodb = eval(str(resultmongodb[1]))
            print dictmongodb
            os.close(r)
            w = os.fdopen(w,'w')
            if(flagmongodb==1):
                print "hello mongodb"
                return 1
            elif(flagmongodb==2):
                print "wrong password"
            else:
                print "no user"
            w.write(str(dictmongodb))
            try:
                w.close()
            except :
                pass 
            print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)
