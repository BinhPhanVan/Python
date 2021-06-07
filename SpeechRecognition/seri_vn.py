import speech_recognition as sr
from playsound import playsound
import os
from gtts import gTTS
def playaudio(audio):
    playsound(audio)
def convert_to_audio(text):
    audio = gTTS(text, lang='vi')
    audio.save("textaudio.mp3")
    playaudio("textaudio.mp3")
    os.remove("textaudio.mp3")
while True:
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Bạn hãy nói gì đó!")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio,language='vi-VN')
        if text =="dừng lại":
            print("Cuộc hội thoại đã dừng lại")
            break
        print("Bạn nói : "+ text)
        convert_to_audio(text)
    except sr.UnknownValueError:
        print("Vui lòng bạn nói lại.........    ")
    except sr.RequestError as e:
        print("Không thể nhận diện giọng nói !!!")
    


    