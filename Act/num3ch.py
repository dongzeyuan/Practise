# 构造词典
num_ch_dict = {'0': '零', '1': '壹', '2': '贰', '3': '叁',
               '4': '肆', '5': '伍', '6': '陆', '7': '柒', '8': '捌', '9': '玖'}

# 用户输入的数字被转换成字符串
num = str(input('Please enter the number >:'))
# 将用户输入的数字按照字符串形式打印出来
print(num)
# 给i赋初值0，对应num字符串中的第一个数字字符
i = 0
# 判定当 i 小于 num字符串长度时执行后续
if i <= len(num):
    # j作为num字符串中的元素
    for j in num:
        # 如果num[i]在词典中
        if num[i] in num_ch_dict:
            # 打印对应的键值（key-value，键-键值）
            print("{0}".format(num_ch_dict[num[i]]), end="")
            # i自增
            i += 1
        # 如果num[i]不在词典中，就是遇到'.'符号了
        else:
            # i自增，跳过'.'符号
            i += 1
