#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import operator

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

    # def getArea(self, list):
    #     """
    #     4개의 직선의 방적식으로 둘러싸인 영역의 넓이를 구하는 함수
    #     :param list: 파형 그래프
    #     :return: 영역의 넓이 값
    #     """
    #     start = {}  # 시작 x,y 좌표
    #     finish = {}  # 종료 x,y 좌표
    #     max = {}  # 최댓값 x,y 좌표
    #     min = {}  # 최소값 x,y 좌표
    #
    #     start['x'] = 0
    #     start['y'] = list[0]
    #     # start[0] = list[0]
    #     finish['x'] = len(list) - 1
    #     finish['y'] = list[len(list) - 1]
    #     # finish[len(list) - 1] = list[len(list) - 1]
    #
    #     maxValue = 0
    #     minValue = 0
    #
    #     for i in range(len(list)):
    #         s = int(list[i])
    #
    #         if maxValue < s:
    #             max.clear()
    #             max['x'] = i
    #             max['y'] = s
    #             # max[i] = s
    #             maxValue = s
    #
    #         if minValue > s:
    #             min.clear()
    #             min['x'] = i
    #             min['y'] = s
    #             # min[i] = s
    #             minValue = s
    #
    #             # print("x : ", i, ", y : ", sig[i])
    #
    #     # print(start)
    #     # print(finish)
    #     # print(max)
    #     # print(min)
    #
    #     lineLT = self.getLineFunc(start, max)  # find left-top line
    #     lineRT = self.getLineFunc(max, finish)  # find right-top line
    #     lineLB = self.getLineFunc(start, min)  # find left-bottom line
    #     lineRB = self.getLineFunc(min, finish)  # find right-bottom line
    #
    #     # print(lineLT)
    #     # print(lineRT)
    #     # print(lineLB)
    #     # print(lineRB)
    #
    #     # calculate total area
    #     totalArea = 0.0
    #     totalGraph = []
    #
    #     for i in range(len(list)):
    #
    #         line1 = {}
    #         line2 = {}
    #
    #         # find current top line from two top line
    #         topMax = lineLT['max']
    #         if i < topMax:
    #             line1 = lineLT
    #         else:
    #             line1 = lineRT
    #
    #         # find current bottom line from two bottom line
    #         botMax = lineLB['max']
    #         if i < botMax:
    #             line2 = lineLB
    #         else:
    #             line2 = lineRB
    #
    #         topA = line1['a']  # top line 기울기
    #         topB = line1['b']  # top line y절편
    #
    #         botA = line2['a']  # bottom line 기울기
    #         botB = line2['b']  # bottom line y절편
    #
    #         # y = ax + b
    #         topDistance = topA * i + topB
    #         botDistance = botA * i + botB
    #
    #         area = abs(topDistance) + abs(botDistance)
    #
    #         totalArea += area
    #         totalGraph.append(totalArea)  # option
    #
    #     # printGraph(totalGraph, title=file) # option
    #
    #     return totalArea

    def getArea2(self, list):
        """
        4개의 직선의 방적식으로 둘러싸인 영역의 넓이를 구하는 함수
        :param list: 파형 그래프
        :return: 영역의 넓이 값
        """
        start = {}  # 시작 x,y 좌표
        finish = {}  # 종료 x,y 좌표
        max1 = {}  # 최댓값 x,y 좌표
        min1 = {}  # 최소값 x,y 좌표
        max2 = {}  # 최댓값 x,y 좌표
        min2 = {}  # 최소값 x,y 좌표
        max3 = {}  # 최댓값 x,y 좌표
        min3 = {}  # 최소값 x,y 좌표

        start['x'] = 0
        start['y'] = list[0]
        # start[0] = list[0]
        finish['x'] = len(list) - 1
        finish['y'] = list[len(list) - 1]
        # finish[len(list) - 1] = list[len(list) - 1]


        maxValue = 0
        minValue = 0
        for i in range( 0, int(len(list)*1/3) ):
            s = int(list[i])

            if maxValue < s:
                max1.clear()
                max1['x'] = i
                max1['y'] = s
                # max[i] = s
                maxValue = s

            if minValue > s:
                min1.clear()
                min1['x'] = i
                min1['y'] = s
                # min[i] = s
                minValue = s

        maxValue = 0
        minValue = 0
        for i in range( int(len(list)*1/3), int(len(list)*2/3) ):
            s = int(list[i])

            if maxValue < s:
                max2.clear()
                max2['x'] = i
                max2['y'] = s
                # max[i] = s
                maxValue = s

            if minValue > s:
                min2.clear()
                min2['x'] = i
                min2['y'] = s
                # min[i] = s
                minValue = s

        maxValue = 0
        minValue = 0
        for i in range( int(len(list)*2/3), int(len(list)) ):
            s = int(list[i])
            if maxValue < s:
                max3.clear()
                max3['x'] = i
                max3['y'] = s
                # max[i] = s
                maxValue = s

            if minValue > s:
                min3.clear()
                min3['x'] = i
                min3['y'] = s
                # min[i] = s
                minValue = s

        lineLT = self.getLineFunc(start, max1)  # find left-top line
        lineCLT = self.getLineFunc(max1, max2)
        lineCRT = self.getLineFunc(max2, max3)
        lineRT = self.getLineFunc(max3, finish)  # find right-top line
        lineLB = self.getLineFunc(start, min1)  # find left-bottom line
        lineCLB = self.getLineFunc(min1, min2)
        lineCRB = self.getLineFunc(min2, min3)
        lineRB = self.getLineFunc(min3, finish)  # find right-bottom line

        # print(lineLT)
        # print(lineRT)
        # print(lineLB)
        # print(lineRB)

        # calculate total area
        totalArea = 0.0
        totalGraph = []
        topGraph = []

        preTopMax = 0
        preBotMax = 0
        checkT = 0
        checkB = 0
        lineT = lineLT
        lineB = lineLB
        for i in range(len(list)-1):


            # find current top line from two top line
            topMax = lineT['max']
            if i < topMax:
                pass
            else:
                preTopMax = topMax
                checkT += 1
                if checkT == 1:
                    lineT = lineCLT
                elif checkT == 2:
                    lineT = lineCRT
                elif checkT == 3:
                    lineT = lineRT

            # find current bottom line from two bottom line
            botMax = lineB['max']
            if i < botMax:
                pass
            else:
                preBotMax = botMax
                checkB += 1
                if checkB == 1:
                    lineB = lineCLB
                elif checkB == 2:
                    lineB = lineCRB
                elif checkB == 3:
                    lineB = lineRB

            topA = lineT['a']  # top line 기울기
            topB = lineT['b']  # top line y절편

            botA = lineB['a']  # bottom line 기울기
            botB = lineB['b']  # bottom line y절편

            # y = ax + b
            topDistance = topA * (i-preTopMax) + topB
            botDistance = botA * (i-preBotMax) + botB

            topGraph.append(topDistance)

            area = abs(topDistance) + abs(botDistance)

            totalArea += area
            totalGraph.append(totalArea)  # option

        # self.printGraph(topGraph) # option

        return totalArea

    def changeAmplitude(self, graph, ratio):
        """
        진폭 수정
        :param graph: 파형 그래프 값
        :return: 진폭이 수정된 파형 그래프 값
        """
        for i in range(len(graph)):
            graph[i] *= ratio

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

    def getAccumulateList(self, graph):
        accumulateGraph = []
        for i in range(len(graph)):
            accumulateGraph.append(abs(graph[i]))

        for i in range(len(accumulateGraph)):
            if i > 0:
                accumulateGraph[i] = accumulateGraph[i] + accumulateGraph[i - 1]

        return accumulateGraph

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

    def getFFTAreaRatio(self, graph):

        lf = abs(np.fft.rfft(graph)) / len(graph)
        # lf = abs(np.fft.rfft(calculateGraph))
        list = lf.tolist()

        area = 0
        area1 = 0
        area2 = 0
        area3 = 0
        area4 = 0
        area5 = 0
        area6 = 0
        area7 = 0

        for i in range(len(list)):
            if 1 < i and i <= 5.5:
                area1 += list[i]
            elif 5.5 < i and i <= 10:
                area2 += list[i]
            elif 10 < i and i <= 55:
                area3 += list[i]
            elif 55 < i and i <= 100:
                area4 += list[i]
            elif 100 < i and i <= 550:
                area5 += list[i]
            elif 550 < i and i <= 1000:
                area6 += list[i]
            elif 1000 < i:
                area7 += list[i]
            area += list[i]

        areaList = {}
        areaList[1] = area1/area * 100
        areaList[2] = area2/area * 100
        areaList[3] = area3/area * 100
        areaList[4] = area4/area * 100
        areaList[5] = area5/area * 100
        areaList[6] = area6/area * 100
        areaList[7] = area7/area * 100

        return areaList

    def twoHalves(self, graph):
        sum = 0
        sum1 = 0
        sum2 = 0
        for i in range(len(graph)):
            if i < len(graph) / 2:
                sum1 += abs(graph[i])
            else:
                sum2 += abs(graph[i])
            sum += abs(graph[i])

        return (sum1/sum*100, sum2/sum*100)

    # def getAreaRatio(self, graph):
    #     area = self.getArea(graph)
    #     total = len(graph) * 200
    #     return area/total*100

    def getAreaRatio2(self, graph):
        area = self.getArea2(graph)
        total = len(graph) * 200
        return area/total*100

    def getBelow25Ratio(self, graph):
        count = 0
        for i in range(len(graph)):
            c = abs(graph[i])
            if c <= 25:
                count += 1
        return count/len(graph)*100

    def getLRBelow10Ratio(self, graph):
        sum = 0
        sum1 = 0
        sum2 = 0
        sum3 = 0
        sum4 = 0
        sum5 = 0
        sum6 = 0
        for i in range(len(graph)):
            c = abs(graph[i])
            if i < len(graph) * 1 / 6:
                sum1 += c
            elif i < len(graph) * 2 / 6:
                sum2 += c
            elif i < len(graph) * 3 / 6:
                sum3 += c
            elif i < len(graph) * 4 / 6:
                sum4 += c
            elif i < len(graph) * 5 / 6:
                sum5 += c
            else:
                sum6 += c
            sum += c

        left = sum1 / sum * 100
        right = sum6 / sum * 100

        return left, right

    def getSixPartRatio(self, graph):
        sum = 0
        sum1 = 0
        sum2 = 0
        sum3 = 0
        sum4 = 0
        sum5 = 0
        sum6 = 0
        for i in range(len(graph)):
            c = abs(graph[i])
            if i < len(graph) * 1 / 6:
                sum1 += c
            elif i < len(graph) * 2 / 6:
                sum2 += c
            elif i < len(graph) * 3 / 6:
                sum3 += c
            elif i < len(graph) * 4 / 6:
                sum4 += c
            elif i < len(graph) * 5 / 6:
                sum5 += c
            else:
                sum6 += c
            sum += c

        list = []
        list.append(round(sum1/sum*100, 2))
        list.append(round(sum2/sum*100, 2))
        list.append(round(sum3/sum*100, 2))
        list.append(round(sum4/sum*100, 2))
        list.append(round(sum5/sum*100, 2))
        list.append(round(sum6/sum*100, 2))

        return list

    def threeQuartersRatio(self, graph):
        sum = 0
        sum1 = 0
        sum2 = 0
        sum3 = 0
        for i in range(len(graph)):
            c = abs(graph[i])
            if i < len(graph) * 1 / 3:
                sum1 += c
            elif i < len(graph) * 2 / 3:
                sum2 += c
            else:
                sum3 += c
            sum += c

        return (sum1/sum*100, sum2/sum*100, sum3/sum*100)

    def getCircle(self, graph):

        sum = 0
        for i in range(len(graph)-1):
            sum = abs(graph[i] - graph[i+1])

        print(sum)

    def printTestValue(self, path):

        basicGraph = self.getBasicGraph(path)

        basicGraph = self.changeAmplitude(basicGraph, 3)

        # 정규화
        normalizeGraph = self.normalization(basicGraph)

        # 누적 그래프의 기울기 리스트
        slopeGraph = self.getGraphAccumulateSlopeList(normalizeGraph)

        # 실제 소리부분 그래프 추출
        graph = self.findRealGraph(normalizeGraph, slopeGraph)

        groupList = self.getFFTAreaRatio(graph)
        below25 = self.getBelow25Ratio(graph)
        first, second, third = self.threeQuartersRatio(graph)
        left, right = self.getLRBelow10Ratio(graph)
        twoLeft, twoRight = self.twoHalves(graph)
        area = self.getAreaRatio2(graph)
        list = self.getSixPartRatio(graph)

        print("푸리에 그룹 비율 : ", groupList)
        print("2등분 sample 비율 : ", twoLeft, ", ", twoRight)
        print("3등분 sample 비율 : ", first, ", ", second, ", ", third)
        print("6등분 sample 비율 : ", list)
        print("25이하 비율 : ", below25)
        print("8각형 영역 넓이 비율 : ", area)


    def recognition(self, path):

        basicGraph = self.getBasicGraph(path)

        basicGraph = self.changeAmplitude(basicGraph, 3)

        # 정규화
        normalizeGraph = self.normalization(basicGraph)

        # 누적 그래프의 기울기 리스트
        slopeGraph = self.getGraphAccumulateSlopeList(normalizeGraph)

        # 실제 소리부분 그래프 추출
        calculateGraph = self.findRealGraph(normalizeGraph, slopeGraph)

        # 푸리에 변환으로 7개 비율 구함
        groupList = self.getFFTAreaRatio(calculateGraph)
        groupList = sorted(groupList.items(), key=operator.itemgetter(1), reverse=True)

        firstIndex = groupList[0][0]
        secondIndex = groupList[1][0]

        # if firstIndex == 5:
        #     if secondIndex == 6:
        #         below25 = self.getBelow25Ratio(calculateGraph)
        #         left, right = self.getLRBelow10Ratio(calculateGraph)
        #         print(path, " : ", left, ", ", right)
        #         first, second, third = self.threeQuartersRatio(calculateGraph)
        #
        #         if first >= 40:
        #             print("8")
        #         elif below25 <= 75:
        #             print("6")
        #         elif left < 10 and right < 10:
        #             print("0")
        #         else:
        #             print("4")
        #     else:
        #         areaRatio = self.getAreaRatio(calculateGraph)
        #         below25 = self.getBelow25Ratio(calculateGraph)
        #         first, second, third = self.threeQuartersRatio(calculateGraph)
        #
        #         if areaRatio >= 85:
        #             print("9")
        #         elif second >= 50:
        #             print("5")
        #         elif below25 <= 75:
        #             print("1")
        #         else:
        #             print("3")
        # else:
        #     left, right = self.twoHalves(calculateGraph)
        #
        #     if left < right:
        #         print("2")
        #     else:
        #         print("7")

        print("예상 숫자 : ", end='')
        if firstIndex == 5:
            if secondIndex == 6:
                below25 = self.getBelow25Ratio(calculateGraph)
                first, second, third = self.threeQuartersRatio(calculateGraph)
                left, right = self.getLRBelow10Ratio(calculateGraph)

                if below25 < 80:
                    print("6")
                else:
                    if first >= 45:
                        print("8")
                    else:
                        if left < 10 and right < 10:
                            print("0")
                        else:
                            print("4")
            else:
                areaRatio = self.getAreaRatio2(calculateGraph)
                below25 = self.getBelow25Ratio(calculateGraph)
                left, right = self.twoHalves(calculateGraph)

                if below25 < 75:
                    if areaRatio < 61:
                        print("1")
                    else:
                        print("9")
                else:
                    if left < right:
                        print("3")
                    else:
                        print("5")
        else:
            left, right = self.twoHalves(calculateGraph)

            if left < right:
                print("2")
            else:
                print("7")


