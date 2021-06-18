import cv2
import numpy as np
import keyboard
class ConvertImage:
    __image_org= cv2.imread("resource/image.PNG")
    def GrayConvert(self):
        grayValue = 0.0722 * self.__image_org[:, :, 0] + 0.7152 * self.__image_org[:, :, 1] \
                  + 0.2126 * self.__image_org[:, :, 2]
        gray_img = grayValue.astype(np.uint8)
        return gray_img
    def BWConvert(self,index):
        Black_White = np.where(self.GrayConvert() >= index, self.GrayConvert(), 0)
        Black_White = np.where(Black_White < index, Black_White, 255)
        return Black_White
    def Show(self):
        cv2.namedWindow("TrackBars")
        cv2.resizeWindow("TrackBars", 300, 300)
        cv2.createTrackbar("BWConvert", "TrackBars", 120, 255, empty)
        cv2.imshow("OriginImage", self.__image_org)
        cv2.imshow("GrayImage", self.GrayConvert())
        while True:
            value = cv2.getTrackbarPos("BWConvert", "TrackBars")
            cv2.imshow("BlackWhiteImage", self.BWConvert(value))
            cv2.waitKey(1)
            if cv2.waitKey(1) & 0xFF == 13:
                cv2.destroyAllWindows()
                break
def empty(a):
    pass