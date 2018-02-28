# coding=UTF-8
# 设计一个类代表花，其中含2个对象属性，2个方法。
# 建立2个花的对象并使用


class Flower(object):
    petal_number = 4
    petal_color = 'Red'

    def __init__(self, name):
        self.name = name
        print('This is a ', self.name)

    def attack(self):
        print('The flower {0} take out a bullet'.format(self.name))


f1 = Flower('Lily')
f2 = Flower('Rose')

f1.attack()
f2.attack()

print(f1.petal_number)
print(f2.petal_color)
