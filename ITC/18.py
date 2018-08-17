def getData(fileName):
    '''读取一个文件汇总的数据，返回包含距离和质量的列表'''
    dataFile = open(fileName,'r')
    distances = []
    masses = []
    dataFile.readline()  #ignore header
    for line in dataFile:
        d, m = line.split('')
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return (masses, distances)
