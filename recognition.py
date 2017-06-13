#-*- coding: utf-8 -*-

# This program is based on Python 3.
# The following libraries are required.
# [numpy] pip install numpy (pip3 install numpy)
# [matplotlib] pip install matplotlib (pip3 install matplotlib)
# [pygame] pip install pygame (pip3 install pygame) (option)

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

    ## Play sound (option)
    fileName = path
    if not fileName.endswith(".wav"):
        fileName = fileName + ".wav"

    pygame.mixer.init()
    pygame.mixer.music.load(fileName)
    pygame.mixer.music.play()

    speech.recognition(path)
