# coding=UTF-8
# 通过键盘输入若干数据（到0停止，不包含0）建立一个元组

data_list = []
a = 1
while a:
    x = int(input("请输入数字： "))
    data_list.append(x)
    a = x
data_list.pop()
# 利用tuple函数，将列表转换成元组
i = tuple(data_list)

print(i)
