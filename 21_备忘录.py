#!/usr/bin/python
#coding:utf8
'''
Memento
'''
 
import copy
 
def 备忘录(obj, deep=False):
    #深度or普通复制
    state = (copy.copy, copy.deepcopy)[bool(deep)](obj.__dict__)
 
    def Restore():
        obj.__dict__.clear()
        obj.__dict__.update(state)
    return Restore
 
class 业务处理:
    """A transaction guard. This is really just
      syntactic suggar arount a memento closure.
      """
    deep = False
 
    def __init__(self, *targets):
        self.targets = targets
        self.Commit()
 
    def Commit(self):
        #提交之前要备份
        self.states = [备忘录(target, self.deep) for target in self.targets]
 
    def Rollback(self):
        for st in self.states:
            st()
 
class 业务预处理方法(object):
    """Adds transactional semantics to methods. Methods decorated  with
    @transactional will rollback to entry state upon exceptions.
    """
    def __init__(self, method):
        self.method = method
 
    def __get__(self, obj, T):
        print('在为属性赋值前，先存档')
        def transaction(*args, **kwargs):
            state = 备忘录(obj)
            try:
                return self.method(obj, *args, **kwargs)
            except:
                state()
                raise
        return transaction
 
class NumObj(object):
    def __init__(self, value):
        self.value = value
 
    def __repr__(self):
        return '<%s: %r>' % (self.__class__.__name__, self.value)
 
    def Increment(self):
        self.value += 1
 
    @业务预处理方法
    def DoStuff(self):
        print('属性赋值')
        self.value = '1111'  # <- invalid value
        self.Increment()     # <- will fail and rollback
 
if __name__ == '__main__':
    n = NumObj(-1)
    print(n)
    t = 业务处理(n)
    try:
        for i in range(3):
            n.Increment()
            print(n)
        t.Commit()
        print('-- commited')
        for i in range(3):
            n.Increment()
            print(n)
        n.value += 'x'  # will fail
        print(n)
    except:
        t.Rollback()
        print('-- rolled back')
    print(n)
    print('-- now doing stuff ...')
    try:
        n.DoStuff()
    except:
        print('-> doing stuff failed!')
        import traceback
        traceback.print_exc(0)
        pass
    print(n)