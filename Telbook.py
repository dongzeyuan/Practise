# coding=UTF-8

# 下面这个是原型中的通讯录输入模块

f = open('Telbook.csv', 'w')
f.write('姓名' + '\t性别' + '\t电话' + '\t\t地址' + '\n')
flag = 1
while flag == 1:
    name = input('请输入姓名：')
    sex = input('请输入性别：')
    phone = input('请输入电话：')
    address = input('请输入住址：')
    s = name + '\t' + sex + '\t' + phone + '\t' + address + '\n'
    f.write(s)
    flag = input('是否继续输入y/n ？')
    if flag == 'y':
        flag = 1
    else:
        flag = 0
f.close