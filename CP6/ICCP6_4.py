# coding=UTF-8
# 编写一个函数，输入三个数，作为三角形的三个边长，计算三角形的面积

import math


def fun1(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print('这三个数能构成三角形')
        l = (a + b + c) / 2
        s = math.sqrt(l * (l - a) * (l - b) * (l - c))
        print('这个三角形的面积是:{0}'.format(s))
    else:
        print('这三个数构不成三角形')


if __name__ == '__main__':
    a = float(input('请输入第一个数： '))
    b = float(input('请输入第一个数： '))
    c = float(input('请输入第一个数： '))
    fun1(a, b, c)
