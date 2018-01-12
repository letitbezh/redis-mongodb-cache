import redis
r = redis.Redis(host="127.0.0.1",port=6379)
import pymongo
client = pymongo.MongoClient()
db = client.test
item = db.test

#redis checkpassword
# input user password 
#1 is right 2 is password wrong 3 is empty
def checkpassword(user,nowpassword):
    user = user
    password = r.hget(user,'password')
    if(password==None):
        return 3
    else:
        if(password==nowpassword):
            return 1
        else:
            return 2

def resultcache(user,password):
    a = r.hset(user,'user',user)
    result = r.hset(user,'password',password)
    return result
#for i in range(0,100000):
#    user = i
#    password = '123456'
    #userdict ={}
    #userdict['user'] = user
    #serdict['password'] = password
    #item.insert(userdict)
#    resultcache(user,password)
def deleteuser(user):
    keys = r.hkeys(user)
    print keys
    for i in range(0,len(keys)):
        a = r.hdel(user,keys[i])
        print a