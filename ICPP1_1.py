# int()函数输出括号内整数部分
#输入表示年月日的8位数，输出年，月，日

x = int(input('<<<please enter number: '))

years = int(x / 10000)

months = int((x - 10000 * years) / 100)

days = int(x - 10000 * years - 100 * months)

print('{0}年{1}月{2}日'.format(years, months, days))
