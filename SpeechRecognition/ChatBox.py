import requests
import sys
from requests.api import request
import requests
url = "https://api.simsimi.net/"
class ChatBox:   
    __question = ""
    def __init__(self, question):
        self.__question = question
    def Chat(self):
        url_question = "v1/?text="+self.__question+"&lang=vi_VN"
        r = requests.get(url+url_question)
        data = r.json()
        return (data["success"])
def __init__(question):
    ChatBox1 = ChatBox(question)
    return ChatBox1.Chat()