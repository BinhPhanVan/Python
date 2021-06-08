import speech_recognition as sr
from playsound import playsound
import os
from gtts import gTTS
class TextToSpeech:
    __text=""
    __file="test"
    def __init__(self, text):
        self.__text=text
    def speech_text(self):
        audio = gTTS(self.__text, lang='vi')
        audio.save(self.__file+ ".mp3")
        playsound(self.__file+ ".mp3")
        os.remove(self.__file+ ".mp3")
def __init__(text):
    TextToSpeech1= TextToSpeech(text)
    TextToSpeech1.speech_text()
