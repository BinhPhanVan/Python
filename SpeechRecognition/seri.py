import speech_recognition as sr
from playsound import playsound
import os
from gtts import gTTS
def playaudio(audio):
    playsound(audio)
def convert_to_audio(text):
    audio = gTTS(text)
    audio.save("textaudio.mp3")
    playaudio("textaudio.mp3")
    os.remove("textaudio.mp3")
while True:
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("say something!")
        audio = r.listen(source)
        # audio = r.record(source, duration= 3)
    try:
        text = r.recognize_google(audio)
        if text=="stop":
            print("stop conversation")
            break
        print("You said: "+ text)
        convert_to_audio(text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition")
    


    