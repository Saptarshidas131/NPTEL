# to recognize speech from an audio  file and search on google
# audio must be of .wav format
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 08:47:17 2020

@author: saptarshi
"""
import speech_recognition as sr
AUDIO_FILE = ("audio.wav")
# use audio file as source

r = sr.Recognizer() # initialise the recogniser

with sr.AudioFile(AUDIO_FILe) as source:
    audio = r.record(source)
# reads the audio file

try:
    print ("audio file contains " + r.recognize_google(audio))
except sr.UnknownValueError:
     print ("Google Speech Recognition coluld not understand audio")
except sr.RequestError:
    print ("couldn't get the results from Google Speech Recognition")