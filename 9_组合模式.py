#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
组合模式(Composite Pattern):将对象组合成成树形结构以表示“部分-整体”的层次结构,组合模式使得用户对单个对象和组合对象的使用具有一致性.
"""

# 抽象一个组织类
class 抽象结构(object):

    def __init__(self, name):
        self.name = name

    def add(self,comp):
        pass

    def remove(self,comp):
        pass

    def display(self, depth):
        pass

# 叶子节点
class 部门(抽象结构):

    def add(self,comp):
        print('不能添加下级节点')

    def remove(self,comp):
        print('不能删除下级节点')

    def display(self, depth):
        strtemp = ''
        for i in range(depth):
            strtemp += strtemp+'-'
        print(strtemp+self.name)


# 枝节点
class 公司(抽象结构):

    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self,comp):
        self.children.append(comp)

    def remove(self,comp):
        self.children.remove(comp)

    def display(self, depth):
        strtemp = ''
        for i in range(depth):
            strtemp += strtemp+'-'
        print(strtemp+self.name)
        for comp in self.children:
            comp.display(depth+2)

if __name__ == "__main__":
    #生成树根
    root = 公司("总公司")
    #根上长出2个叶子
    root.add(部门('部门 A'))
    root.add(部门('部门 B'))

    #根上长出树枝Composite X
    comp = 公司("子公司 X")
    comp.add(部门('部门 XA'))
    comp.add(部门('部门 XB'))
    root.add(comp)

    #根上长出树枝Composite X
    comp2 = 公司("子公司 XY")
    #Composite X长出2个叶子
    comp2.add(部门('子公司部门 XYA'))
    comp2.add(部门('子公司部门 XYB'))
    root.add(comp2)
    # 根上又长出2个叶子,C和D,D没张昊,掉了
    root.add(部门('总公司部门 C'))
    leaf = 部门("总公司部门 D")
    root.add(leaf)
    root.remove(leaf)
    #展示组织
    root.display(1)