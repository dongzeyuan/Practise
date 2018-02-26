# coding=UTF-8
# 在程序EXP7_16所处理的文本文件中插入几个汉字，
# 运行时会产生错误，请分析异常产生的原因，并修改程序以解决问题

def FileCopy(tar_files, res_files):
    try:
        f = open(res_files)
        f2 = open(tar_files)
    except:
        print('打开文件异常！')
        return -1
    s = f.read()
    f2.write(s)
    f.close()
    f2.close()
    return 0

if __name__ == '__main__':
    try:
        FileCopy('F7_15_2.txt', 'F7_15.txt')
        f = open('F7_15_2.txt', 'r')
        f2 = open('F7_15_3.txt', 'w+')
    except:
        print('打开文件异常！')
    while True:
        s = f.read(2)
        point = f.tell()
        if len(s) < 2:
            break
        else:
            f2.write(s[0])
            f.seek(point-1)

    f.seek(0)
    s = f.read()
    f2.flush()
    f2.seek(0)
    s2 = f2.read()
    f.close()
    f2.close()
    print(s)
    print('='*len(s))
    print(s2)

