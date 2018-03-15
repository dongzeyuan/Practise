# 比如，有一列数据，1.2.3.4.5.6.7.8.9.10，
# 现在，我想把所有大于5的数据修改为4


def flit():
    list1 = [1,2,3,4,5,6,7,8,9,10]
    for i in range(0,len(list1)):
        if list1[i] > 5:
            list1[i] = 4
            i += 1
        else:
            i += 1

    print(list1)

if __name__ == '__main__':
    flit()