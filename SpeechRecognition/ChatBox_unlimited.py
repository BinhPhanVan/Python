import requests
import sys
from requests.api import request 
from TextToSpeech import TextToSpeech
from SpeechToText import SpeechToText
import requests
url = "https://api.simsimi.net/"
class ChatBox_unlimited:   
    __question = ""
    __reply = ""
    def __init__(self):
        self.__question = ""
        self.__reply = "" 
    def Chat(self):
        url_question = "v1/?text="+self.__question+"&lang=vi_VN"
        r = requests.get(url+url_question)
        if r.status_code==200:
            return r.json()["success"]
    def ChatBox_with_api(self):
        while True:
            print("Please say!")
            self.__question = str(SpeechToText().voice_to_text())
            if self.__question == "stop":
                print("stop conservation")
                break
            else:
                if self.__question=="None":
                    continue
                else:

                    print("you said: " + str(self.__question))
            self.__reply = str(self.Chat())
            print("Simi answer: "+ self.__reply)
            TextToSpeech(self.__reply).speech_text()
