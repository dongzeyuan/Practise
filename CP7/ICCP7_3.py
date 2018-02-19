# coding=UTF-8
# 先建立一个文本文件，然后变成把文件中的大写字母替换为小写字母

f = open('123.txt', w)
while True:
    lines = f.readline()
    up_lines = lines.upper
    