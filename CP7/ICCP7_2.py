# coding=UTF-8
# 对例7-13进行试验，调用函数FileCopy(tar_File,res_File)时，
# 给形参传入一个新文件名，分析代码运行的流程


def FileCopy(tar_File, res_File):
    try:
        f = open(tar_File, 'a')
        f2 = open(tar_File, 'a')
    except:
        print('打开文件异常')
        return -1
    s = f.read()
    f2.write(s)
    f.close()
    f2.close()
    return 0


if __name__ == '__main__':

# 传递参数时，用字符串传递文件名
    FileCopy('123.txt', '321.txt')
