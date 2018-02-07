# coding=UTF-8
# 求一元二次方程的实数根，系数a,b,c由键盘输入
import math


def qiu_gen(a, b, c):
    delta = (b**2 - 4 * a * c)
    if delta < 0:
        print("此方程无实数根")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("此方程的实数根为：x1 = {0}，x2 = {1}".format(x1, x2))

if __name__ == '__main__':
    a = float(input('Please enter a: '))
    b = float(input('Please enter b: '))
    c = float(input('Please enter c: '))
    qiu_gen(a, b, c)
