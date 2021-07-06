import cv2
import os
import numpy as np
from person import Person
front_cascade = cv2.CascadeClassifier('Resource/haarcascade_frontalface_default.xml')
path = "Resource/class.jpg"
vid = cv2.VideoCapture(0)
def createFolder(directory):
   try:
      if not os.path.exists(directory):
         os.makedirs(directory) 
   except OSError:
      print("Error: Creating directory. "+directory)

def AddPicture(name):
   i=0
   while (True):
      ret, frame = vid.read()
      cv2.imshow('frame1', frame)
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      faces = front_cascade.detectMultiScale(gray, 1.3, 6)
      for (x, y, w, h) in faces:
         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0 , 255), 2)
         cv2.putText(frame, str(name) ,(x, y-5), cv2.FONT_HERSHEY_PLAIN,1 , (236,	236,	236),2)
         cv2.imshow('frame1', frame)  
      if cv2.waitKey(1) & 0xFF == ord('q'):
         createFolder("dataSet/User/"+name+"/")
         cv2.imwrite("dataSet/User/"+name+"/"+str(i)+".jpg",frame[y:y + h, x:x + w])
         i =i+1
      if i==10:
         vid.release()
         cv2.destroyAllWindows()
         return 
def Show():
   i=0
   while (True):
      ret, frame = vid.read()
      cv2.imshow('frame1', frame)
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      faces = front_cascade.detectMultiScale(gray, 1.3, 6)
      for (x, y, w, h) in faces:
         cv2.rectangle(frame, (x, y), (x + w, y + h), (0,0 , 255), 2)
         cv2.imshow('frame1', frame)  
      if cv2.waitKey(1) & 0xFF == ord('q'):
         vid.release()
         cv2.destroyAllWindows()
         return
if __name__=="__main__":
   while True:
      print("1.Show\n2.Add\n3.Exit")
      number = int(input("Choosen: "))
      if number == 3:
         break
      if number == 1:
         Show()
      if number == 2:
         name = input("Banhaynhapten:")
         AddPicture(name)