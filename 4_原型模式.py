import copy
 
class 原型:
    def __init__(self):
        self._objects = {}
 
    def 设置参考对象(self, name, obj):
        self._objects[name] = obj
 
    def 取消参考对象(self, name):
        del self._objects[name]
 
    def clone(self, name, **attr):
        """Clone a registered object and update inner attributes dictionary"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj
 
 
def main():
    class 正品:
        def __str__(self):
            return "我是正品"
 
    _正品 = 正品()
    _原型 = 原型()
    _原型.设置参考对象('正品', _正品)

    #以正品为原型，增加几项黑科技
    仿品 = _原型.clone('正品', 黑科技1="黑科技1", 黑科技2="黑科技2", 黑科技3="黑科技3")
 
    print(_正品)
    print(仿品.黑科技1, 仿品.黑科技2, 仿品.黑科技3)
 
 
if __name__ == '__main__':
    main()