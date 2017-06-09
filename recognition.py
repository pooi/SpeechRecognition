#-*- coding: utf-8 -*-

import test
import speech
import numpy as np
import pygame

speech = speech.SpeechRecognition()
test = test.Test()

while(True):
    path = input("input : ")

    if path == 'q' or path == 'Q':
        break

    fileName = path
    if not fileName.endswith(".wav"):
        fileName = fileName + ".wav"

    pygame.mixer.init()
    pygame.mixer.music.load(fileName)
    pygame.mixer.music.play()

    speech.recognition(path)
    speech.recognition2(path)

    # speech.printTestValue(path)
    # speech.printFFTGraph(path)

    # basicGraph = speech.getBasicGraph(path)
    #
    # basicGraph = speech.changeAmplitude(basicGraph, 3)
    #
    # # 정규화
    # normalizeGraph = speech.normalization(basicGraph)
    #
    # accum = speech.getAccumulateList(normalizeGraph)
    #
    # # 누적 그래프의 기울기 리스트
    # slopeGraph = speech.getGraphAccumulateSlopeList(normalizeGraph)
    #
    # # 실제 소리부분 그래프 추출
    # calculateGraph = speech.findRealGraph(normalizeGraph, slopeGraph)

    # cal = []
    # # 중성까지만 대략적으로 추출
    # for i in range(len(calculateGraph)):
    #     if i < max(2000, len(calculateGraph) / 3):
    #         cal.append(calculateGraph[i])
    #
    # # speech.printGraph(cal)
    #
    # lf = abs(np.fft.rfft(cal))  # / len(calculateGraph)
    # lf = abs(np.fft.rfft(calculateGraph))
    # list = lf.tolist()
    #
    # speech.printGraph(list)

    #
    #
    # lf = abs(np.fft.rfft(calculateGraph))/len(calculateGraph)
    # list = lf.tolist()
    # fMax = 0.0
    # for i in range(len(list)):
    #     if fMax < list[i]:
    #         fMax = list[i]
    #
    # for i in range(len(list)):
    #     list[i] = list[i] * 10 / fMax
    #
    # f = open(path + '.txt', 'w')
    # for i in range(len(list)):
    #     f.write(str(list[i]) + "\n")
    # f.close()





    # speech.getCircle(calculateGraph)

