import process
import os
import processinsert
choose = raw_input("what you want to do ")
choose = int(choose)
if choose==1:
    print process.find()
elif choose==2:
    processinsert.insert()
elif choose==3:
    flag = process.find()
    if(flag):
        processinsert.delete()