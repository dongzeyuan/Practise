# coding=UTF-8
f = open('Q7_1.txt', 'w')
f.write('姓名' + '\t性别' + '\t电话' + '\t\t地址' + '\n')
flag = 1
while flag == 1:
    name = input('请输入姓名： ')
    sex = input('请输入性别：')
    phone = input('请输入电话： ')
    address = input('请输入住址： ')
    s = name + '\t' + sex + '\t' + phone + '\t' + address + '\n'
    f.write(s)
    flag = int(input('是否继续输入1/0 ？'))
f.close
