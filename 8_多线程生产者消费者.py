#!/usr/bin/python
#coding:utf8
import threading
import time

list1=[]

def read():
    print("begin read")
    while(True):
        print("read..")
        if (len(list1)>0):
            val=list1.pop(0)
            print(val)
            time.sleep(0.01)
            if (val>=1000):
                break

def put():
    print("begin put")
    i=0
    while(i <= 1000):
        print("begin append",i)
        list1.append(i)  
        time.sleep(0.01)  
        i=i+1    


if __name__=="__main__":
    threads=[]
    t1=threading.Thread(target=put)
    t2=threading.Thread(target=read)
    threads.append(t1)
    threads.append(t2)
    for t in threads:
        t.start()
    for t in threads:
        t.join()