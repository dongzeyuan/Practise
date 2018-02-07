# coding=UTF-8
# 输入一个小数，对第n+1位小数进行四舍五入，保留n位小数


def fun1(a, b):
    x = int(a * 10**b)
    y = float(x / (10**b))
    z = float(a - y)
    if z >= float(5 * (10 ** (-(b+1)))):
        x += 1
    return (x / (10**(b)))


if __name__ == '__main__':

    a = float(input('Please enter a float number: '))
    b = int(input('Please enter a number: '))

    print(fun1(a, b))
