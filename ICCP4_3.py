# coding=UTF-8
# 变成求斐波那契数列的前20项。第一项和第二项是0、1


def fib(n):
    f1 = 0
    f2 = 1
    fib_n = [0, 1]
    a = 2
    while a < n:
        fib_n.append(fib_n[a-1] + fib_n[a-2])
        a += 1
    print(fib_n)
    print(sum(fib_n))


if __name__ == '__main__':
    n = int(input('请输入一个不大于20的整数n: '))
    fib(n)
