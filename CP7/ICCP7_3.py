# coding=UTF-8
# 先建立一个文本文件，然后变成把文件中的大写字母替换为小写字母

f = open('123.txt', 'w+')
f.write('HLLJSDFOOS')
while True:
    lines = f.readline()
    print(lines)
    low_lines = lines.lower()
    f.write(low_lines)
    if lines == '':
        break
f.close()



    