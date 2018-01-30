# coding=UTF-8
# 举一个生活中的例子，用分支语句来设计程序
# 比如去餐馆点餐，有西红柿鸡蛋拌面，红烧牛肉拌面，过油肉拌面，新疆大盘鸡，炒拉条子
# 收银员需要根据我们的点餐来收钱

print("欢迎来到拌面馆，请问您想吃点什么？")

order_list = input('<<<: ')

if order_list == '西红柿鸡蛋拌面':
    price = 10
    print('共计{0}元'.format(price))
elif  order_list == '红烧牛肉拌面':
    price = 15
    print('共计{0}元'.format(price))
elif  order_list == '过油肉拌面':
    price = 20
    print('共计{0}元'.format(price))
elif  order_list == '新疆大盘鸡':
    price = 30
    print('共计{0}元'.format(price))
elif  order_list == '炒拉条子':
    price = 12
    print('共计{0}元'.format(price))
else:
    print("输入错误")