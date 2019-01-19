
#!/usr/bin/python
#coding:utf8
'''
Decorator
'''
import time
 
SLEEP = 0.5
 
# Complex Parts
class 打雷:
    def run(self):
        print("###### In 打雷 ######")
        time.sleep(SLEEP)
        print("Setting up")
        time.sleep(SLEEP)
        print("Running test")
        time.sleep(SLEEP)
        print("Tearing down")
        time.sleep(SLEEP)
        print("Test Finished\n")
 
 
class 下雨:
    def run(self):
        print("###### In 下雨 ######")
        time.sleep(SLEEP)
        print("Setting up")
        time.sleep(SLEEP)
        print("Running test")
        time.sleep(SLEEP)
        print("Tearing down")
        time.sleep(SLEEP)
        print("Test Finished\n")
 
 
class 刮风:
    def run(self):
        print("###### In 刮风 ######")
        time.sleep(SLEEP)
        print("Setting up")
        time.sleep(SLEEP)
        print("Running test")
        time.sleep(SLEEP)
        print("Tearing down")
        time.sleep(SLEEP)
        print("Test Finished\n")
 
 
# Facade
class 雨天:
    def __init__(self):
        self.tc1 = 打雷()
        self.tc2 = 下雨()
        self.tc3 = 刮风()
        self.tests = [i for i in (self.tc1, self.tc2, self.tc3)]
 
    def 现象(self):
        [i.run() for i in self.tests]
 
 
# Client
#加入以后阴天现象里又增加了洪水、泥石流 ,我们的调用接口不变
if __name__ == '__main__':
    testrunner = 雨天()
    testrunner.现象()