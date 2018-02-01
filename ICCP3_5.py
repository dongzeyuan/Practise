# coding=UTF-8
# 编程计算函数的值

x = float(input('请输入X的值： '))

if x < -5:
    y = x + 9
    print(y)
# 用and连接两个判断状态
elif x < 5 and x >= -5:
    y = x**2 + 2 * x + 1
    print(y)
elif x >= 5:
    y = 2 * x - 15
    print(y)
else:
    print('输入错误，请重新输入')
