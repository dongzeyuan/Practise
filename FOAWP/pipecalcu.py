import math


class Pipe():
    def __init__(self, length, od, thickness):
        self.length = length
        self.od = od
        self.thickness = thickness

    def weight(self):
        self.squ_od = math.pi*(self.od/2)**2
        self.squ_id = math.pi*((self.od-self.thickness*2)/2)**2
        self.squ = self.squ_od-self.squ_id
        self.wei = self.squ*self.length*7850/1000000000
        print('{0} mm 长的 管子 {1} 重量为 {2} kg'.format(
            self.length, (self.od, self.thickness), self.wei))


if __name__ == '__main__':
    length = float(input('请输入长度，单位 mm：'))
    od = float(input('请输入外径，单位 mm：'))
    thickness = float(input('请输入壁厚，单位 mm：'))

    pipe = Pipe(length, od, thickness)
    pipe.weight()
