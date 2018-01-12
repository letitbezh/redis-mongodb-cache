import pymongo
import random
client = pymongo.MongoClient()
db = client.test
item = db.test

#for i in range(0,100000):
#    user = i
#    password = '123456'
#    userdict ={}
#    userdict['user'] = user
#    userdict['password'] = password
#    item.insert(userdict)
def checkpassword(user,nowpassword):
    result = item.find({'user':user},{'_id':0})
    for i in result:
        resultdict = eval(str(i))
        try:
            password = resultdict['password']
        except:
            pass
        if password==nowpassword:
            return 1,resultdict
        else:
            if(str(i)==None):
                return 3,resultdict
            else :
                return 2,resultdict

#checkpassword(1,'123456')
def inseruser(user,nowpassword):
    result = item.update({'user':user},{"$set":{'user':user,'password':nowpassword}})
    return result

def deleteuser(user):
    result = item.delete_one({'user':user})
    print result