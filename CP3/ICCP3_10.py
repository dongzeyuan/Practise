# coding=UTF-8
# 在键盘输入年份和月份，输出该月的天数


def is_leapyear(year, month):
    c = year % 400
    d = year % 4
    e = year % 100
    days31 = (1, 3, 5, 7, 8, 10, 12)
    days30 = (4, 6, 9, 11)

    if c == 0:
        print('This year {0} is a leap year'.format(year))
        if month in days31:
            print('This month {0} is 31 days'.format(month))
        elif month in days30:
            print('This month {0} is 30 days'.format(month))
        else:
            print('This month {0} is 29 days'.format(month))
    elif d == 0 and e != 0:
        print('This year {0} is a leap year'.format(year))
        if month in days31:
            print('This month {0} is 31 days'.format(month))
        elif month in days30:
            print('This month {0} is 30 days'.format(month))
        else:
            print('This month {0} is 29 days'.format(month))
    else:
        print('This year {0} isn\'t a leap year'.format(year))
        if month in days31:
            print('This month {0} is 31 days'.format(month))
        elif month in days30:
            print('This month {0} is 30 days'.format(month))
        else:
            print('This month {0} is 28 days'.format(month))


if __name__ == '__main__':
    year = int(input('Please enter the year: '))
    month = int(input('Please enter the month: '))
    is_leapyear(year, month)
