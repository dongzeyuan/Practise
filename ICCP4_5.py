# coding=UTF-8
# 求1-100的所有素数，并统计素数的个数

def is_prime(x, y):
    primenumber = []
    if x == 1:
        x += 1
    for i in range(x, y):
        n = 0
        for j in range(1,i+1):
            if i % j == 0:
                n += 1
        if n == 2:
            primenumber.append(i)
    print('在{0}到{1}的区间内的素数为:{2}'.format(x, y, primenumber))

if __name__ == '__main__':
    x = int(input('请输入素数区间下限x: '))
    y = int(input('请输入素数区间上限y: '))
    is_prime(x, y)


            