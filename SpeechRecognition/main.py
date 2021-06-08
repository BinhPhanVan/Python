from requests.models import Response
import ChatBox
import SpeechToText
import TextToSpeech
while True:
    question = SpeechToText.__init__()
    print("you said: "+ question)
    if question == "dừng lại":
        break
    Response = ChatBox.__init__(question)
    print("Simi answer: "+ Response)
    TextToSpeech.__init__(Response)
