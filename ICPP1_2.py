# coding=UTF-8

# 如何能一次性输出坐标值呢？？？
import math
# 目前这种输入坐标的方式好麻烦，怎么能一次性输入一个点的坐标呢？
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

distance = float(math.sqrt((x1 - x2)**2 + (y1 - y2)**2))

print('The distance is {0}'.format(distance))
