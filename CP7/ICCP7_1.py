# coding=UTF-8
# 把字符串'abc123@#$中国人民'存入文件，查看文件长度（字节数）

f = open('ICCP7_1.txt', 'w')
f.write('abc123@#$中国人民')
f.seek(0, 2)
length = f.tell()
f.close()
print('文件长度是{0}字节'.format(length))

