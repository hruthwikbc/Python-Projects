import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import pyaudio

                                              # to play the input text as audio
def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ''

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print('exception:' + str(e))

    return said

speak('Hello')
get_audio()