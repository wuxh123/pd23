#!/usr/bin/python
#coding:utf8
'''
Proxy
'''
 
import time
 
class 经理:
    def work(self):
        print("Sales Manager working...")
 
    def talk(self):
        print("Sales Manager ready to talk")
 
 #秘书是代理类
class 秘书:
    def __init__(self):
        self.busy = 'No'
        self.sales = None
 
    def work(self):
        print("Proxy checking for Sales Manager availability")
        if self.busy == 'No':
            self.sales = 经理()
            time.sleep(2)
            self.sales.talk()
        else:
            time.sleep(2)
            print("Sales Manager is busy")
 
 
if __name__ == '__main__':
    p = 秘书()
    p.work()
    p.busy = 'Yes'
    p.work()