#!/usr/bin/python
#coding:utf8
'''
Adapter
'''
 
import os
 
 
class 狗(object):
    def __init__(self):
        self.name = "狗"
 
    def 狗叫(self):
        return "狗叫!"
 
 
class 猫(object):
    def __init__(self):
        self.name = "猫"
 
    def 猫叫(self):
        return "猫叫!"
 
 
class 人(object):
    def __init__(self):
        self.name = "人"
 
    def 人喊(self):
        return "'人喊'"
 
 
class 车(object):
    def __init__(self):
        self.name = "车"
 
    def 鸣笛(self, octane_level):
        return "鸣笛%s" % ("!" * octane_level)
 
'''
    pyton 特有的适配器的写法, 如果是java需要添加 adapter接口

'''
class 适配器(object):
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)
 

    def __getattr__(self, attr):
        return getattr(self.obj, attr)
 
 
def main():
    '''
    适配为统一接口
    '''
    objects = []
    dog = 狗()
    objects.append(适配器(dog, dict(噪音=dog.狗叫)))
    cat = 猫()
    objects.append(适配器(cat, dict(噪音=cat.猫叫)))
    human = 人()
    objects.append(适配器(human, dict(噪音=human.人喊)))
    car = 车()
    car_noise = lambda: car.鸣笛(3)
    objects.append(适配器(car, dict(噪音=car_noise)))
 
    '''
    统统都是噪音
    '''
    for obj in objects:
        print("A", obj.name, "goes", obj.噪音())
 
if __name__ == "__main__":
    main()