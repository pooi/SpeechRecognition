#-*- coding: utf-8 -*-

import test
import speech
import numpy as np

speech = speech.SpeechRecognition()
test = test.Test()

while(True):
    path = input("input : ")

    if path == 'q' or path == 'Q':
        break

    basicGraph = speech.getBasicGraph(path)

    basicGraph = speech.changeAmplitude(basicGraph, 3)

    # 정규화
    normalizeGraph = speech.normalization(basicGraph)

    # 누적 그래프의 기울기 리스트
    slopeGraph = speech.getGraphAccumulateSlopeList(normalizeGraph)

    # 실제 소리부분 그래프 추출
    calculateGraph = speech.findRealGraph(normalizeGraph, slopeGraph)

    speech.getCircle(calculateGraph)

    # speech.recognition(path)

# for j in range(10):
#     file = '0' + str(j)
#
#     basicGraph = speech.getBasicGraph(file)
#
#     # 진폭 변경
#     basicGraph = speech.changeAmplitude(basicGraph)
#
#     # 고속 푸리에 변환
#     # lf = abs(np.fft.rfft(sig))/len(sig)
#     # printSpectrumGraph(lf, title=file)
#
#     # 정규화(-100~100)
#     normalizeGraph = speech.normalization(basicGraph)
#
#     # 누적 그래프의 기울기 리스트
#     slopeGraph = speech.getGraphAccumulateSlopeList(normalizeGraph)
#
#     # 실제 소리부분 그래프 추출
#     calculateGraph = speech.findRealGraph(normalizeGraph, slopeGraph)
#     # test.test1(j, calculateGraph)
#     # test.test2(j, calculateGraph)
#     # test.test3(j, calculateGraph, speech.getArea(calculateGraph))
#     # test.test4(j, calculateGraph)
#     # test.test5(j, calculateGraph)
#     # test.test6(j, calculateGraph)
#     # print("-"*30)
#
#
#     #speech.printGraph(calculateGraph, title=file, isSaveImg=True)
#
#     # print(file, " : ", end='')
#     # print(round(getArea(calculateGraph), 2))
#
#     # t = len(calculateGraph)*200;
#     # print(j, " | area percentage : ", round(sum/t*100,2))
#
#
#     # imgTitle = '0' + str(j) + '_b'
#     # printGraph(calculateGraph, title=imgTitle, isSaveImg=False)
#
#     # lf = abs(np.fft.rfft(calculateGraph))/len(calculateGraph)
#     # lf = abs(np.fft.rfft(calculateGraph))
#     # list = lf.tolist()
#     # fMax = 0.0
#     # for i in range(len(list)):
#     #     if fMax < list[i]:
#     #         fMax = list[i]
#     #
#     # for i in range(len(list)):
#     #     list[i] = list[i] * 10 / fMax
#     #printGraph(lf, title='fft')
#
#
#     # imgTitle = '0' + str(j) + '_s'
#     # speech.printGraph(list3, title=imgTitle)
#     #speech.printGraph(list, title=imgTitle, isSaveImg=False)
#     # speech.printSpectrumGraph(list, title=imgTitle, isSaveImg=False)

