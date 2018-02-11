# coding=UTF-8
# 编写一个函数，输入三个数，输出最大的数


def largest(a, b, c):
    list1 = list()
    list1.append(a)
    list1.append(b)
    list1.append(c)
    list2 = sorted(list1)
    print('The largest number is {0}'.format(list2[2]))


if __name__ == '__main__':
    a = float(input('Please enter the first number: '))
    b = float(input('Please enter the second number: '))
    c = float(input('Please enter the third number: '))
    largest(a, b, c)
