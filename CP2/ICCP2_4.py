# coding=UTF-8
# 通过键盘输入若干数据（键输入回车结束）建立一个字典，然后用程序读其键和值，并分别存入两个列表中

key_list = []
value_list = []
dict_ori = {}
a = 1
while int(a):
    key = input('请输入键： ')
    # 键输入回车结束
    if key == '':
        break
    else:
        val = input('请输入值： ')
        dict_ori[key] = val

print("字典初始化完成")
print(dict_ori)

for key in dict_ori.keys():
    key_list.append(key)
    value_list.append(dict_ori[key])

print(key_list)
print(value_list)
