#coding=UTF-8

def yin_shu(n):
    yinshu = []
    for i in range(2, n):
        if n%i == 0:
            yinshu.append(i)
    print(yinshu)

if __name__ == '__main__':
    n = int(input('请输入一个不大于1000的整数n: '))
    yin_shu(n)