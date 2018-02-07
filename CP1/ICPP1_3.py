# coding=UTF-8
# 输入两个点，建立起直线方程 y=kx+b，输入第三个点，求点到直线的距离
import math

x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

k = (y1 - y2) / (x1 - x2)

b = (x1 * y1 - x2 * y1) / (x1 - x2)

print('y = {0}x + {1}'.format(k, b))

x3 = float(input('x3 = '))
y3 = float(input('y3 = '))

distance = abs(k * x3 - y3 + b) / math.sqrt(k**2 + 1)

print('The distance is {0}'.format(distance))
