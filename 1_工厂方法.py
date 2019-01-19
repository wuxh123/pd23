#!/usr/bin/python
#coding:utf8
'''
工厂方法
'''
 
class 中国车:
    def __init__(self):
        print("在中国开车")
 
    def 驾驶(self):
        print("我方向盘在左边")
 
 
class 日本车:
    def __init__(self):
        print("在日本开车")
    def 驾驶(self):
        print("我方向盘在右边")
 
 
def get_localizer(language="中国车"):
    """The factory method"""
    languages = dict(在中国=中国车, 在日本=日本车)
    return languages[language]()
 
# 通过一个接口，可以分别得到中国人或者英国人实例
e, g = get_localizer("在中国"), get_localizer("在日本")

# 你好
e.驾驶()
g.驾驶()