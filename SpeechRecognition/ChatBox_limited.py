import requests
import sys
from requests.api import request
import requests
import json
url = "https://wsapi.simsimi.com/190410/talk"
class ChatBox:   
    __question = ""
    def __init__(self, question):
        self.__question = question
    def Chat(self):
        payload ="{\n\t\"utext\": \""+self.__question+"\", \n\t\"lang\": \"vi\" \n}"
        payload=payload.encode("utf-8")
        headers = {
            'Content-Type': "application/json",
            'x-api-key':r"e2wqSRg0i7ppJPD8aGVLvD6EIsy6J-BzeXyxPCcf"
        }
        response = requests.request("POST", url, data = payload, headers=headers)
        if(response.status_code=="200"):
            response = json.loads(response.text)
            return ( response["atext"])
def __init__(question):
    ChatBox1 = ChatBox(question)
    return ChatBox1.Chat()
