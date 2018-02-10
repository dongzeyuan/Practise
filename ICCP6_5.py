# coding=UTF-8
# 编写一个函数，计算输入的列表的最大值，最小值和平均值，并以元组的方式返回，调用该函数

def fun1(list1):
    list1.sort()
    pass


if __name__ == '__main__':
    list1 = list()
    while True:
        i = float(input('请输入列表中的元素： '))
        list1.append(i)
        n = (input('列表是否输入完毕(Y/N): '))
        if n == 'N':
            continue
        else:
            break
    fun1(list1[:])