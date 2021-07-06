import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
myColors = [0,0,0,0,0,0]

def FindColor(image, colors):
    imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    for color in colors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        cv2.imshow("IMG", mask)
while True:

    success, img = cap.read()
    FindColor(img,myColors)
    cv2.imshow("Camera", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# nhận biết khuôn mặt bằng ảnh

# img = cv2.imread(path)
# img = cv2.resize(img,(400,450))
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# faces = front_cascade.detectMultiScale(gray, 1.3, 6)
# for (x, y, w, h) in faces:
#    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 155), 3)
# print(faces)
# nhận biết khuôn mặt bằng camera


# while (True):
#    vid = cv2.VideoCapture(0)
#    ret, frame = vid.read()
#    cv2.imshow('frame1', frame)
#    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#    faces = front_cascade.detectMultiScale(gray, 1.3, 6)
#    for (x, y, w, h) in faces:
#       cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0 , 255), 2)
#       cv2.imshow('frame1', frame)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#       break
   #    number = number +1
   #    cv2.imwrite("dataSet/User." + id + '.' + str(number) + ".jpg", gray[y:y + h, x:x + w] )
   #    print("write finished "+ " image "+ id+'.'+str(number)+".jpg")
   # if number>20:
   #    break
# vid.release()
# cv2.waitKey(0)
# cv2.destroyAllWindows()