import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

def printSpectrumGraph(list, title='title'):
    plt.figure(1)
    b = plt.subplot(211)
    b.set_xscale('log')
    b.set_xlabel('frequency [Hz]')
    b.set_ylabel('|amplitude|')
    plt.title(title)
    plt.plot(list, linewidth=1)
    plt.show()

def printGraph(list, title='Signal Wave...'):
    plt.figure(1)
    plt.title(title)
    plt.plot(list, linewidth=1)
    plt.show()


def printWaveGraph(spf, signal):
    if spf.getnchannels() == 2:
        print("Just mono files")
        sys.exit(0)

    printGraph(signal)

    # plt.figure(1)
    # plt.title('Signal Wave...')
    # plt.plot(signal, linewidth=1)
    # plt.show()

def getLineFunc(location1, location2):

    line = {}

    x1 = location1['x']
    y1 = location1['y']
    x2 = location2['x']
    y2 = location2['y']

    a = (y2 - y1) / (x2 - x1)
    b = y1 - ((y2 - y1) / (x2 - x1))

    line['a'] = a
    line['b'] = b
    line['min'] = x1
    line['max'] = x2

    return line


def getArea(list):
    start = {}
    finish = {}
    max = {}
    min = {}

    start['x'] = 0
    start['y'] = list[0]
    # start[0] = list[0]
    finish['x'] = len(list)-1
    finish['y'] = list[len(list)-1]
    # finish[len(list) - 1] = list[len(list) - 1]

    maxValue = 0
    minValue = 0

    for i in range(len(list)):
        s = int(list[i])

        if maxValue < s:
            max.clear()
            max['x'] = i
            max['y'] = s
            # max[i] = s
            maxValue = s

        if minValue > s:
            min.clear()
            min['x'] = i
            min['y'] = s
            # min[i] = s
            minValue = s

            # print("x : ", i, ", y : ", sig[i])

    #print(start)
    #print(finish)
    #print(max)
    #print(min)

    lineLT = getLineFunc(start, max)
    lineRT = getLineFunc(max, finish)
    lineLB = getLineFunc(start, min)
    lineRB = getLineFunc(min, finish)

    #print(lineLT)
    #print(lineRT)
    #print(lineLB)
    #print(lineRB)

    totalArea = 0.0
    totalGraph = []

    for i in range(len(list)):

        line1 = {}
        line2 = {}

        # find current top line
        topMax = lineLT['max']
        if i < topMax:
            line1 = lineLT
        else:
            line1 = lineRT

        # find current bottom line
        botMax = lineLB['max']
        if i < botMax:
            line2 = lineLB
        else:
            line2 = lineRB

        topA = line1['a']
        topB = line1['b']

        botA = line2['a']
        botB = line2['b']

        topDistance = topA * i + topB
        botDistance = botA * i + botB

        area = abs(topDistance) + abs(botDistance)

        totalArea += area
        totalGraph.append(totalArea)

    #printGraph(totalGraph, title=file)

    return totalArea


for j in range(10):
    file = '0' + str(j)

    if not file.endswith(".wav"):
        file = file + ".wav"

    spf = wave.open(file, 'r')

    signal = spf.readframes(-1)
    signal = np.fromstring(signal, 'Int16')

    sig = signal.tolist()
    # print(file, " : ", end='')
    # print(round(getArea(sig), 2))

    # 진폭 변경
    for i in range(len(sig)):
        sig[i] *= 1
    #
    # lf = abs(np.fft.rfft(sig))/len(sig)
    # printSpectrumGraph(lf, title=file)

    # 정규화(-100~100)
    max = 0
    min = 0
    for i in range(len(sig)):
        s = sig[i]
        if max < s:
            max = s

        if min > s:
            min = s

    num = 10
    max = abs(max)
    min = abs(min)
    sig2 = []
    for i in range(len(sig)):
        if sig[i] >= 0:
            s = sig[i] * num / max
        else:
            s = -(abs(sig[i]) * num / min)

        sig2.append(s)

    print(file, " : ", end='')
    print(round(getArea(sig2), 2))
    printGraph(sig2, title=file)


