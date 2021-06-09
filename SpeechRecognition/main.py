from requests.models import Response
import ChatBox_limited
import ChatBox_unlimited
import SpeechToText
import TextToSpeech
import keyboard
def ChatBox_with_api():
    while True:
        question = SpeechToText.__init__()
        if question == "stop":
            print("stop conservation")
            break
        else:
            print("you said: "+ question)
        Response = ChatBox_limited.__init__(question)
        print("Simi answer: "+ Response)
        TextToSpeech.__init__(Response)
ChatBox_with_api()