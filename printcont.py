# coding=UTF-8
f = open('Q7_1.txt','r')
while True:
    line=f.readline()
    if line=='':
        break
    print(line)
f.close()