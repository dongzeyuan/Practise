# coding=UTF-8
# 编程计算下列表达式的值：
# (1) S=1+(1+sqrt2)+(1+sqrt2+sqrt3)+....+(1+sqrt2+sqrt3+...+sqrtn)
# 参考值，当n=20时，S=534.188884
# (2)S=1+1/（1*2）+1/（1*2*3）+。。。+1/（1*2*3*4*...*50），参考值S=7.718282
# (3)S=1+X+X^2/2!+X^3/3!+******+X^N/N!
# (4)利用一下公示求pi的近似值，指导最后一项的绝对值小于等于10e-6为止
# pi/4 ~ 1-1/3+1/5-1/7+......

import math


def s_1(n):
    a = 1.0
    s = 0.0
    while n > 0:
        s += math.sqrt(n) * a
        n -= 1
        a += 1
    print('S1 = {0}'.format(round(s, 6)))


def s_2():
    s = 0
    n = 1
    while n <= 50:
        s += 1 / (math.factorial(n))
        n += 1
    print('S2 = {0}'.format(round(s, 6)))


def s_3(n3, x):
    s = 1
    n = 1
    while n <= n3:
        s += (x**n) / (math.factorial(n))
        n += 1
    print('S3 = {0}'.format(round(s, 6)))

def s_4():
    s = 0
    n = 1
    while 1/(2*n-1) > 10**(-6):
        s += 1/(2*n-1)
        s = (-s)
        n += 1
    print('PI = {0}'.format(round(4*s, 6)))


if __name__ == '__main__':
    n1 = int(input('Please enter n1 = :'))
    n3 = int(input('Please enter n3 = :'))
    x = float(input('Please enter x = :'))
    s_1(n1)
    s_2()
    s_3(n3, x)
    s_4()
