# -*- coding: utf-8 -*-

import cv2
import numpy as np


# color = np.array([0, 0, 0])
#
#
# def callBack(pos):
#     color[0] = cv2.getTrackbarPos("HH", "img")
#     color[1] = cv2.getTrackbarPos("sH", "img")
#     color[2] = cv2.getTrackbarPos("vH", "img")
#
#     img = np.ones(shape=(200, 200, 3), dtype=np.uint8)
#     img[:, :, 0] = img[:, :, 0] * color[0]
#     img[:, :, 1] = img[:, :, 1] * color[1]
#     img[:, :, 2] = img[:, :, 2] * color[2]
#
#     img = cv2.cvtColor(img,cv2.COLOR_HSV2BGR)
#     cv2.imshow("img1",img)
#
#
# if __name__ == '__main__':
#     cv2.namedWindow("img", 0)
#     cv2.createTrackbar("HH", "img", 0, 180, callBack)
#     cv2.createTrackbar("sH", "img", 0, 255, callBack)
#     cv2.createTrackbar("vH", "img", 0, 255, callBack)
#
#     cv2.waitKey(0)

# rootPath = "img//"
# filePath = rootPath + "stick_2019-08-23_16-53-29.bmp"

isbuttondown = False


def mouse_click(event, x, y, flags, para):
    global isbuttondown
    if event == cv2.EVENT_LBUTTONDOWN:
        isbuttondown = True
    if event == cv2.EVENT_LBUTTONUP:
        isbuttondown = False
    if event == cv2.EVENT_MOUSEMOVE:
        if isbuttondown:
            imgtemp = img.copy()
            cv2.putText(imgtemp, str(hsv[y, x]), (40, 50), 1, 4, (0, 0, 255))
            cv2.imshow(file_Path, imgtemp)


def showImg(filePath):

    global img, hsv,file_Path
    file_Path = filePath
    img = cv2.imdecode(np.fromfile(filePath,dtype=np.uint8),-1)
    # img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    cv2.namedWindow(filePath)
    cv2.setMouseCallback(filePath, mouse_click)
    cv2.imshow(filePath, img)
    cv2.waitKey()

    cv2.destroyAllWindows()
