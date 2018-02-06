# coding=UTF-8
# 6. 给定一个由10个整书值构成的列表，编程删除列表中所有下标为奇数的元素
# 7. 给定一个由10个整数值构成的列表，编程删除列表中所有值为奇数的元素。
# 8. 给定一个由10个整数值构成的列表，编程只对列表中下标为偶数的元素进行升序排序，下标为奇数的元素保持不变


# 第6题函数体开始


def del_odd(list_6):
    #   n = 0
    #   length = len(list_1)
    #   while (2*n-1) <= length:
    #       del list_1[(2*n-1)] 这么写有问题，因为执行完这一句的时候，原列表就已经变了
    # 得从后往前删
    length = len(list_6)
    if length % 2 == 0:
        n = length / 2
    else:
        n = (length + 1) / 2
    while (2 * n - 1) >= 0:
        del list_6[int(2 * n - 1)]  # 这里加int函数，强制将2*N-1转换成int，否则下标为float，会报错
        n -= 1
    print(list_6)
# 第6题函数体结束

# 第7题函数体开始


def del_odd_elem(list_7):
    length = len(list_7)
    while length > 0:
        if list_7[int(length - 1)] % 2 == 0:
            length -= 1
        else:
            del list_7[int(length - 1)]
            length -= 1
    print(list_7)
# 第7题函数体结束

# 第8题函数体开始


def sort_even(list_8):
    list_2 = []
    for i in range(0, len(list_8)):
        if i % 2 == 0:
            list_2.append(list_8[i])
    list_2 = sorted(list_2)
    for i in range(0, len(list_2)):
        list_8[int(2 * i)] = list_2[i]
    print(list_8)
# 第8题函数体结束


if __name__ == '__main__':

    list_test = []
    for i in range(1, 11):
        list_test.append(int(input('请输入第{0}个元素: '.format(i))))
    print(list_test)
# 以下所有函数参数列表中，都要加[:]才能正确输出这是啥原因呢？
# list是典型的可变量，传递这种变量当做参数时，最好传递拷贝
    del_odd(list_test[:])

    del_odd_elem(list_test[:])

    sort_even(list_test[:])
