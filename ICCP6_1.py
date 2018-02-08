# coding=UTF-8
# 编写一个函数，用户输入一个数，判断是否为素数，然后调用该函数求100以内的素数

import math


def is_prime(x):
    if x == 1:
        return(0)
    elif x == 2:
        return(1)
    elif x == 3:
        return(1)
    elif x >= 5:
        y = int(math.sqrt(x))
        n = 0
        for i in range(2, (y + 1)):
            if x % i == 0:
                n += 1
        if n > 0:
            return(0)
        else:
            return(1)
    else:
        return(0)


if __name__ == '__main__':
    x = int(input('Please enter a number: '))
    if is_prime(x) == 1:
        print('This number is Prime')
    else:
        print('This number is not Prime')

    primelist = []

    m = int(input('请输入素数区间下限x: '))
    n = int(input('请输入素数区间上限y: '))

    for j in range(m, n):
        if is_prime(j) == 1:
            primelist.append(j)
        else:
            continue
    print(primelist)
