# coding=UTF-8
# 通过键盘输入一系列值，输入0则表示输入结束，将这些值（不包含0）建立为一个列表
# 然后再输出该列表的各元素


data_list = []
a = 1
while a:
    x = int(input("请输入数字： "))
    data_list.append(x)
    a = x
data_list.pop()
print(data_list)