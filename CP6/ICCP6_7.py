# coding=UTF-8
# 编写一个函数，接受传入的字符串，统计大写字母的个数，小写字母的个数，数字的个数
# 其他字符的个数，并以元组的方式返回这些数，然后调用该函数
def fun1(str1):
    upper_str = 0
    lower_str = 0
    number_str = 0
    other_str = 0
    for i in str('ABCDEFGHIJKLMNOPQLSTUVWXYZ'):
        for j in str1:
            if i == j:
                upper_str += 1

    for i in str('abcdefghijklmnopqlstuvwxyz'):
        for j in str1:
            if i == j:
                lower_str += 1

    for i in str('0123456789'):
        for j in str1:
            if i == j:
                number_str += 1
    other_str = len(str1) - upper_str - lower_str - number_str
    return tuple([upper_str, lower_str, number_str, other_str])

if __name__ == '__main__':
    str1 = str(input('请输入一串字符串： '))
    print(fun1(str1))

