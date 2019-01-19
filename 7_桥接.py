#!/usr/bin/python
#coding:utf8
'''
Bridge
'''
 
 
#作图工具
class 圆规(object):
    def draw_circle(self, x, y, radius):
        print('画一个圆 at {}:{} radius {}'.format(x, y, radius))
 
 
#作图工具
class 硬币(object):
    def draw_circle(self, x, y, radius):
        print('画一个圆 at {}:{}  {}'.format(x, y, radius))
 
 
# Refined Abstraction
class CircleShape(object):
    def __init__(self, x, y, radius, 画圆):
        self._x = x
        self._y = y
        self._radius = radius
        self.画圆 = 画圆
 
    # 调用该方法，使用不同的工具
    def draw(self):
        self.画圆.draw_circle(self._x, self._y, self._radius)
 
    # high-level i.e. Abstraction specific
    def scale(self, pct):
        self._radius *= pct
 
 
def main():
    shapes = (
        CircleShape(1, 2, 3, 圆规()),
        CircleShape(5, 7, 11, 硬币())
    )
 
    for shape in shapes:
        shape.scale(2.5)
        shape.draw()
 
 
if __name__ == '__main__':
    main()