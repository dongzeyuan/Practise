import random

def rollDie():
    '''返回一个1-6的随机整数'''
    return random.choice([1,2,3,4,5,6])

def rollN(n):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    print(result)

if __name__ == '__main__':
    rollN(15)