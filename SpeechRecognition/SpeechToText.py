import speech_recognition as sr
from playsound import playsound
import os
from gtts import gTTS
class SpeechToText:
    r = sr.Recognizer()
    __audio = ""
    def __init__(self):
        with sr.Microphone() as source:
            print("Bạn hãy nói gì đó!")
            audio = self.r.listen(source)
            self.__audio=audio
    def voice_to_text(self):
        try:
            text = self.r.recognize_google(self.__audio,language='vi-VN')
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition")
def __init__():
    SpeechToText1= SpeechToText()
    return SpeechToText1.voice_to_text()