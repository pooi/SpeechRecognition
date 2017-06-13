#-*- coding: utf-8 -*-

import test
import speech

speech = speech.SpeechRecognition()
test = test.Test()

for i in range(10):
    file = '0' + str(i)
    print("File : ", file, ".wav")
    # speech.printTestValue(file)
    # speech.printFFTGraph(file)
    speech.recognition(file)