# coding=UTF-8
# 设计一个类代表长方形，其中有1个类属性n能统计用户建立的对象个数


class Square(object):
    population = 0

    def __init__(self, name):
        self.name = name
        print('(Initializing {0} Square)'.format(self.name))
        Square.population += 1

    @classmethod
    def how_many(self):
        print('There are {0} Squares'.format(Square.population))


f1 = Square('Bigger')
f2 = Square('Medium')
f3 = Square('Little')

Square.how_many()
