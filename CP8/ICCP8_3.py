# coding=UTF-8
# 设计一个类代表机动车，设计小车类继承与机动车类

class Auto(object):
    price = 10000
    total_number = 0
    def __init__(self, name):
        self.name = name
        print('{0}的发动机发出了巨大的声音'.format(self.name))
        Auto.total_number += 1
    def engine(self):
        pass

class Car(Auto):
    def __init__(self, name):
        self.name = name

    def engine(self):
        print('total number = {0}'.format(Auto.total_number))


a1 = Auto('Benz')
a2 = Auto('Das Auto')
a3 = Auto('Geely')

b1 = Car('Lotus')
b2 = Car('Range Rover')
# Car 和 Auto 类的 __init__ 函数不一样
Car.engine(1)





    

