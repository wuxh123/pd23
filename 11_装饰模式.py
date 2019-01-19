
#!/usr/bin/python
#coding:utf8
'''
装饰器
'''
 
class 店铺(object):
    def 笔(self):
        print("笔原价 10元")
        return 10
 
    def 格尺(self):
        print("格尺原价 20元")
        return 20
 
 #装饰模式 双十一
class 双11_店铺(object):
    def __init__(self, decoratee):
        self._decoratee = decoratee
 
    def 笔(self):
        print("对笔的售价通过装饰模式进行修改。")
        price=self._decoratee.笔()
        print("8.5折，价格",price*0.85)
 
    def __getattr__(self, name):
        return getattr(self._decoratee, name)

#装饰模式 双12.. 
u = 店铺()
v = 双11_店铺(u)
v.笔()
v.格尺()