#!/usr/bin/python
#coding:utf8
'''
Abstract Factory
'''
 
import random
 
class 汽车工厂:
   
    def __init__(self, 实际工厂=None):
        """pet_factory is our abstract factory.
        We can set it at will."""
 
        self.抽象工厂 = 实际工厂
 
    def 工厂生产(self):
        """Creates and shows a pet using the
        abstract factory"""
 
        self.工厂 = self.抽象工厂.GET_工厂()
        self.工厂.生产()
 
 
# 产品
class 轿车:
    def 发动机(self):
        print("汽油发动机")
 
    def 轮胎(self):
        print("半径50毫米")

    def 生产(self):
        print("生产轿车")
        self.发动机()
        self.轮胎()

#产品
class 卡车:
    def 发动机(self):
        print("柴油发动机")
 
    def 轮胎(self):        
        print("半径1米")
    
    def 生产(self):
        print("生产卡车")
        self.发动机()
        self.轮胎() 
 
# Factory classes 
class 轿车工厂:
    def GET_工厂(self):
        return 轿车()
 
    def __str__(self):
        return "轿车"
 
 
class 卡车工厂:
    def GET_工厂(self):
        return 卡车()
 
    def __str__(self):
        return "卡车"
 
 
# 随机取得工厂
def 抽象汽车工厂():
    """Let's be dynamic!"""
    return random.choice([轿车工厂, 卡车工厂])()
 
 
# 生产汽车在不同的工厂
if __name__ == "__main__":
    工厂 = 汽车工厂()
    for i in range(3):
        工厂.抽象工厂 = 抽象汽车工厂()
        工厂.工厂生产()
        print("=" * 20)