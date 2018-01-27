# coding=UTF-8
# 输入一个十进制数，输出该数的二进制数，八进制数，和十六进制数

i = int(input('Plaese enter a number <: '))

o2 = bin(i)
o8 = oct(i)
o16 = hex(i)

print(o2,o8,o16)