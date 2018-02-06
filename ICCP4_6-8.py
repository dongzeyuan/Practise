# coding=UTF-8
# 6. 给定一个由10个整书值构成的列表，编程删除列表中所有下标为奇数的元素
# 7. 给定一个由10个整数值构成的列表，编程删除列表中所有值为奇数的元素。
# 8. 给定一个由10个整数值构成的列表，编程只对列表中下标为偶数的元素进行升序排序，下标为奇数的元素保持不变


# 第6题函数体开始
def del_odd(list_1):
    #   n = 0
    #   length = len(list_1)
    #   while (2*n-1) <= length:
    #       del list_1[(2*n-1)] 这么写有问题，因为执行完这一句的时候，原列表就已经变了
    # 得从后往前删
    length = len(list_1)
    if length % 2 == 0:
        n = length / 2
    else:
        n = (length + 1) / 2
    while (2 * n - 1) >= 0:
        del list_1[int(2 * n - 1)]  # 这里加int函数，强制将2*N-1转换成int，否则下标为float，会报错
        n -= 1
    print(list_1)
# 第6题函数体结束

# 第7题函数体开始


def del_odd_elem(list_1):
    length = len(list_1)
    while length >= 0:
        if list_1[int(length - 1)] % 2 == 0:
            length -= 1
        else:
            del list_1[int(length - 1)]
            length -= 1
    print(list_1)
# 第7题函数体结束

# 第8题函数体开始


def sort_even(list_1):
    list_2 = []
    for i in range(0, len(list_1)):
        if i % 2 == 0:
            list_2.append(list_1[i])
    list_2 = sorted(list_2)
    for i in range(0, len(list2)):
        list_1[int(2 * i)] = list_2[i]
    print(list_1)
# 第8题函数体结束


if __name__ == '__main__':
    list_1 = []
    for i in range(1, 11):
        list_1.append(int(input('请输入第{0}个元素'.format(i))))
    del_odd(list_1)
    del_odd_elem(list_1)
    sort_even(list_1)
