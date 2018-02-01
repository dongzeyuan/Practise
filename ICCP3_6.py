# coding=UTF-8
# 列表中存有5名同学的名字，输入同学的名字，如果在列表中找到则输出“找到此人”
# 否则输出“查无此人”

name_list = ['张三','李四','王五','赵六','钱七']

check_name = input('请输入查找人姓名： ')

if check_name in name_list:
    print('找到此人')
else:
    print('查无此人')