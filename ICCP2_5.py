# coding=UTF-8
# 通过键盘输入一串字符，输出其中不同的字符以及他们各自的个数,例如输入adafdsfds，输出：
# a，2


data_list = []
dict_ori = {}
a = 1
while a:
    x = (input("请输入字符串： "))
    if x == '':
        break
    else:
        data_list = x

for i in data_list:
    dict_ori[i] = data_list.count(i)

print(dict_ori)
for key in dict_ori.keys():
    print('{0} : {1}'.format(key, dict_ori[key]))