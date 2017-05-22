#-*- coding: utf-8 -*-

import test
import speech

speech = speech.SpeechRecognition()
test = test.Test()

for i in range(10):
    file = '0' + str(i)
    print("file : ", file)
    speech.recognition(file)

while(True):

    file = input("input : ")

    if file=='q' or file=='Q':
        break

    speech.recognition(file)

    # basicGraph = speech.getBasicGraph(file)
    #
    # # 정규화(-100~100)
    # normalizeGraph = speech.normalization(basicGraph)
    #
    # # 누적 그래프의 기울기 리스트
    # slopeGraph = speech.getGraphAccumulateSlopeList(normalizeGraph)
    #
    # # 실제 소리부분 그래프 추출
    # calculateGraph = speech.findRealGraph(normalizeGraph, slopeGraph)
    #
    # # speech.printGraph(calculateGraph, title=file)
    #
    # test.test1(0, calculateGraph)
    # test.test2(0, calculateGraph)
    # test.test3(0, calculateGraph, speech.getArea(calculateGraph))
    # test.test4(0, calculateGraph)
    # test.test5(0, calculateGraph)
    # test.test6(0, calculateGraph)