import random


class Location(object):
    def __init__(self, x, y):
        '''x和y是数值型'''
        self.x, self.y = x, y

    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        ox, oy = other.x, other.y
        xDist, yDist = self.x - ox, self.y - oy
        return (xDist**2 + yDist**2)**0.5

    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'


class Field(object):
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc

    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        self.drunks[drunk] = currentLocation.move(xDist, yDist)

    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]


class Drunk(object):
    def __init__(self, name=None):

        self.name = name

    def __str__(self):
        if self != None:
            return self.name
        return 'Anonymous'


class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(stepChoices)
        return random.choice(stepChoices)


def walk(f, d, numSteps):
    '''假设f是一个Field对象，d是f中的一个Drunk对象，numSteps是正整数，
    将d移动numSteps次，返回这次游走最终位置与开始位置之间的距离'''
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))


def simWalks(numSteps, numTrials, dClass):
    '''假设numSteps是非负整数，numTrials是正整数，
    dClass是Drunk的一个子类，
    模拟numTrials次游走，每次游走numSteps步。
    返回一个列表，表示每次模拟的最终距离'''
    Homer = dClass()
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(round(walk(f, Homer, numSteps), 1))
    return distances


def drunkTest(walkLengths, numTrials, dClass):
    '''假设walklengths是非负整数序列，
    numTrials是正整数，dClass是Drunk的一个子类，
    对于walkLengths中的每个步数，运行numTrials次simWalks函数，并输出结果'''
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print(dClass.__name__, 'random walk of', numSteps, 'steps')
        print('Mean = ', round(sum(distances) / len(distances), 4))
        print('Max = ', max(distances), 'Min = ', min(distances))


if __name__ == '__main__':
    drunkTest((10,100,1000,10000),100,UsualDrunk)