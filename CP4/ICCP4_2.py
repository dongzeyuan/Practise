# coding=UTF-8
# 从键盘输入一个整数n，求他所有因子之和（不包括1和本身），规定n不大于1000


def yin_shu(n):
    yinshu = []
    for i in range(2, n+1):
        if n % i == 0:
            yinshu.append(i)
        sum_ys = sum(yinshu)
    print(yinshu)
    print(sum_ys)


if __name__ == '__main__':
    n = int(input('请输入一个不大于1000的整数n: '))
    yin_shu(n)
