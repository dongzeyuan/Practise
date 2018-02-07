# coding=UTF-8
# 如果年份能被400整除，则为闰年，如果能被4整除，不能被100整除，也为闰年
# 编程判断输入的年份是否为闰年


def is_leapyear(year):
    c = year % 400
    d = year % 4
    e = year % 100
    if c == 0:
        print('This year {0} is a leap year'.format(year))
    elif d == 0 and e != 0:
        print('This year {0} is a leap year'.format(year))
    else:
        print('This year {0} isn\'t a leap year'.format(year))


if __name__ == '__main__':
    year = int(input('Please enter the year: '))
    is_leapyear(year)
