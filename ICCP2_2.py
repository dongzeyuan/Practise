# coding=UTF-8
# 通过键盘输入一系列值，输入0则表示输入结束，将这些值（不包含0）建立为一个列表
# 然后再输出该列表的各元素，之后再逆序输出列表


data_list = []
a = 1
while a:
    x = int(input("请输入数字： "))
    data_list.append(x)
    a = x
data_list.pop()
print(data_list)

# 逆序操作，先给定原列表总长，然后循环将其逆序添加入一个新列表

i = len(data_list)
data_list2 = []
while i:
    data_list2.append(data_list[(i - 1)])
    i -= 1
print(data_list2)
