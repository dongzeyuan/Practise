# coding=UTF-8
# 编写一个函数，判断三个数是否能够成一个三角形

import math


def is_tri(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print('这三个数能构成三角形')
    else:
        print('这三个数构不成三角形')


if __name__ == '__main__':
    a = float(input('请输入第一个数： '))
    b = float(input('请输入第一个数： '))
    c = float(input('请输入第一个数： '))
    is_tri(a, b, c)
