import speech_recognition as sr
from playsound import playsound
import os
import keyboard
from gtts import gTTS
class SpeechToText:
    r = sr.Recognizer()
    __audio = ""
    def __init__(self):
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source)
            audio = self.r.listen(source)
            self.__audio=audio             
    def voice_to_text(self):
        try:
            text = str(self.r.recognize_google(self.__audio,language='vi-VN'))
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            print('You Pressed Enter to say!')
            while True:  
                try: 
                    if keyboard.is_pressed('Enter'):
                        break
                except:
                    break 
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition")
            print('You Pressed Enter to say!')
            while True:  
                try: 
                    if keyboard.is_pressed('Enter'):
                        break 
                except:
                    break 
        except sr.WaitTimeoutError:
            print("Waiting time too long")
            print('You Pressed Enter to say!')
            while True:  
                try: 
                    if keyboard.is_pressed('Enter'):
                        break 
                except:
                    break 