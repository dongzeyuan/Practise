import pylab


def getData(fileName):
    '''读取一个文件汇总的数据，返回包含距离和质量的列表'''
    dataFile = open(fileName, 'r')
    distances = []
    masses = []
    dataFile.readline()  # ignore header
    for line in dataFile:
        d, m = line.split(' ')
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return (masses, distances)


def plotData(inputFile):
    masses, distances = getData(inputFile)
    distances = pylab.array(distances)
    masses = pylab.array(masses)
    forces = masses*9.81
    pylab.plot(forces, distances, 'bo',
               label = 'Measured displacements')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('|Force| (Newtons)')
    pylab.ylabel('Distances (meters)')
    pylab.show()

if __name__ == '__main__':
    plotData('E:\Python\Practise\ITC\springData.txt')
