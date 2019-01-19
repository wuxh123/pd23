#!/usr/bin/python
#coding:utf8
'''
Flyweight
'''
 
import weakref 
 
 
class Card(object):
    _CardPool = weakref.WeakValueDictionary()
 
    def __new__(cls, value, suit):        
        obj = Card._CardPool.get(value + suit, None)        
        if not obj:            
            obj = object.__new__(cls)            
            Card._CardPool[value + suit] = obj            
            obj.value, obj.suit = value, suit         
        return obj
 
    # def __init__(self, value, suit):        
    #     self.value, self.suit = value, suit     
 
    def __repr__(self):        
        return "<Card: %s%s>" % (self.value, self.suit)     
 
 
if __name__ == '__main__':
    # comment __new__ and uncomment __init__ to see the difference
    c1 = Card('9', 'h')
    c2 = Card('9', 'h')
    print(c1, c2)
    print(c1 == c2)
    print(id(c1), id(c2))