#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

class SpeechRecognition:

    def getBasicGraph(self, fileName):

        if not fileName.endswith(".wav"):
            fileName = fileName + ".wav"

        spf = wave.open(fileName, 'r')

        signal = spf.readframes(-1)
        signal = np.fromstring(signal, 'Int16')

        return signal.tolist()

    def printSpectrumGraph(self, list, title='title', isSaveImg=False):
        plt.figure(1)
        b = plt.subplot(111)
        b.set_xscale('log')
        b.set_xlabel('frequency [Hz]')
        b.set_ylabel('|amplitude|')
        plt.title(title)
        plt.plot(list, linewidth=1)
        if isSaveImg:
            plt.savefig(title + '.png')
        plt.show()

    def printGraph(self, list, title='Signal Wave...', isSaveImg=False):
        """
        Draw graph
        :param list: graph items
        :param title: screen title
        :return: void
        """
        plt.figure(1)
        plt.title(title)
        plt.plot(list, linewidth=1)
        if isSaveImg:
            plt.savefig(title + '.png')
        plt.show()

    def printWaveGraph(self, spf, signal):
        if spf.getnchannels() == 2:
            print("Just mono files")
            sys.exit(0)

        self.printGraph(signal)

    def getLineFunc(self, location1, location2):
        """
        두 점을 지나는 직선의 방정식을 구하는 함수
        :param location1: point 1
        :param location2: point 2
        :return: void
        """
        line = {}

        x1 = location1['x']
        y1 = location1['y']
        x2 = location2['x']
        y2 = location2['y']

        a = (y2 - y1) / (x2 - x1)  # 기울기
        b = y1 - ((y2 - y1) / (x2 - x1))  # y절편

        line['a'] = a
        line['b'] = b
        line['min'] = x1  # 범위 (start~finish)
        line['max'] = x2

        return line

    def getArea(self, list):
        """
        4개의 직선의 방적식으로 둘러싸인 영역의 넓이를 구하는 함수
        :param list: 파형 그래프
        :return: 영역의 넓이 값
        """
        start = {}  # 시작 x,y 좌표
        finish = {}  # 종료 x,y 좌표
        max = {}  # 최댓값 x,y 좌표
        min = {}  # 최소값 x,y 좌표

        start['x'] = 0
        start['y'] = list[0]
        # start[0] = list[0]
        finish['x'] = len(list) - 1
        finish['y'] = list[len(list) - 1]
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

        # print(start)
        # print(finish)
        # print(max)
        # print(min)

        lineLT = self.getLineFunc(start, max)  # find left-top line
        lineRT = self.getLineFunc(max, finish)  # find right-top line
        lineLB = self.getLineFunc(start, min)  # find left-bottom line
        lineRB = self.getLineFunc(min, finish)  # find right-bottom line

        # print(lineLT)
        # print(lineRT)
        # print(lineLB)
        # print(lineRB)

        # calculate total area
        totalArea = 0.0
        totalGraph = []

        for i in range(len(list)):

            line1 = {}
            line2 = {}

            # find current top line from two top line
            topMax = lineLT['max']
            if i < topMax:
                line1 = lineLT
            else:
                line1 = lineRT

            # find current bottom line from two bottom line
            botMax = lineLB['max']
            if i < botMax:
                line2 = lineLB
            else:
                line2 = lineRB

            topA = line1['a']  # top line 기울기
            topB = line1['b']  # top line y절편

            botA = line2['a']  # bottom line 기울기
            botB = line2['b']  # bottom line y절편

            # y = ax + b
            topDistance = topA * i + topB
            botDistance = botA * i + botB

            area = abs(topDistance) + abs(botDistance)

            totalArea += area
            totalGraph.append(totalArea)  # option

        # printGraph(totalGraph, title=file) # option

        return totalArea

    def changeAmplitude(self, graph):
        """
        진폭 수정
        :param graph: 파형 그래프 값
        :return: 진폭이 수정된 파형 그래프 값
        """
        for i in range(len(graph)):
            graph[i] *= 1

        return graph

    def normalization(self, graph, value=100):
        """
        파형 그래프의 sample 값들을 원하는 값으로 정규화
        그래프의 최대, 최소값을 찾고
        각 sample을 sample*value/(max or min)으로 정규화
        :param graph: 정규화 시킬 파형 그래프 값
        :param value: 정규화 시킬 값(default : 100)
        :return: 정규화된 파형 그래프 값
        """
        max = 0
        # min = 0
        for i in range(len(graph)):
            s = graph[i]
            if max < abs(s):
                max = abs(s)
                # if max < s:
                #     max = s
                #
                # if min > s:
                #     min = s

        value = abs(value)
        # max = abs(max)
        # min = abs(min)
        normalizeGraph = []
        for i in range(len(graph)):
            if graph[i] >= 0:
                s = graph[i] * value / max
            else:
                s = -(abs(graph[i]) * value / max)

            normalizeGraph.append(s)

        return normalizeGraph

    def getGraphAccumulateSlopeList(self, graph):
        """
        1. 파형 그래프의 값들을 누적시키고
        2. 누적된 값들의 각 기울기를 저장한 배열을 생성
        :param graph: 파형 그래프 값
        :return: 누적 그래프의 각 기울기 값 배열(0~100)
        """
        # 누적 그래프를 구함
        accumulateGraph = []
        for i in range(len(graph)):
            accumulateGraph.append(abs(graph[i]))

        for i in range(len(accumulateGraph)):
            if i > 0:
                accumulateGraph[i] = accumulateGraph[i] + accumulateGraph[i - 1]

        # 누적 그래프의 기울기 리스트
        slopeGraph = []
        slopeGraph.append(0)
        aMax = 0
        for i in range(len(accumulateGraph)):
            if i > 0:
                a = abs((accumulateGraph[i] - accumulateGraph[i - 1]) / (1))
                if a > aMax:
                    aMax = a
                slopeGraph.append(a)

        # 기울기 리스트 정규화
        for i in range(len(slopeGraph)):
            slopeGraph[i] = slopeGraph[i] * 100 / aMax

        return slopeGraph

    def findRealGraph(self, originalGraph, slopeList):
        """
        Original 파형 값과 각 기울기가 저장된 배열을 통해
        실제 소리가 녹음된 영역의 그래프 값을 찾아냄
        :param originalGraph: 실제 소리를 찾아낼 그래프 값
        :param slopeList: 기울기 배열
        :return: 실제 소리가 녹음된 영역의 그래프 값
        """

        THRESHOLD = 5

        startIndex = 0
        finishIndex = len(slopeList) - 1

        while slopeList[startIndex] < THRESHOLD:
            startIndex += 1

        while slopeList[finishIndex] < THRESHOLD:
            finishIndex -= 1

        # print('start : ', startIndex, ' / finish : ', finishIndex)

        calculateGraph = []
        for i in range(startIndex, finishIndex):
            calculateGraph.append(originalGraph[i])

        return calculateGraph