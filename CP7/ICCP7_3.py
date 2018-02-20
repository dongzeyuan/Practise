# coding=UTF-8
# 先建立一个文本文件，然后变成把文件中的大写字母替换为小写字母

f = open('123.txt', 'r+')
while True:
    lines = f.readline()
    print(lines)
    low_lines = lines.lower()
# '\t'+变量名这种方式要记住
    f.write('\n'+low_lines)
    if lines == '':
        break
f.close()



    