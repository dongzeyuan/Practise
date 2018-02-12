# coding=UTF-8
# 编写一个函数，计算传入的远足的最大值，最小值和平均值，并以列表的方式范围，调用该函数


def fun1(tuple1):
    list1 = list(tuple1)
    listmin = sorted(list1)
    listmax = sorted(list1, reverse=True)
    equal = sum(list1) / len(list1)
    return_list = [listmin[0], listmax[0], equal]
    print(return_list)
    pass



if __name__ == '__main__':
    list1 = list()
    while True:
        i = float(input('请输入元组中的元素： '))
        list1.append(i)
        n = (input('元组是否输入完毕(Y/N): '))
        if n == 'N':
            continue
        else:
            break
    tuple1 = tuple(list1)
    fun1(tuple1)