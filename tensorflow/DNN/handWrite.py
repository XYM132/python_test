import numpy as np
import cv2
from ministTrain import mnist_eval
isPress = False


def detect(img):
    cv2.imshow("28",img)
    imgdata = np.zeros(shape=img.shape, dtype=np.uint8)
    imgdata[np.where(img >= 0.5)] = 1
    #imgdata[np.where(img < 0.5)] = 0

    imgdata = np.reshape(imgdata,(1, 784))

    lay1 = np.matmul(imgdata, weight1)
    laySig = lay1 / (1 + np.exp(-lay1))
    lay2 = np.matmul(laySig, weight2)


    return np.argmax(lay2)

def draw(event, x, y, flags, param):
    global img
    global isPress
    if event == cv2.EVENT_LBUTTONDOWN:
        isPress = True
        img = np.zeros(shape=[280, 280], dtype=np.uint8)
    elif event == cv2.EVENT_LBUTTONUP:
        isPress = False
        result = detect(cv2.resize(img, (28, 28)))
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        img = cv2.putText(img, str(result), (5, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2)
    if isPress:
        cv2.circle(img, (x, y), 6, (255, 255, 255), -1)
        print("hand_write")


if __name__ == '__main__':

    npWight = np.load("weight.npz")
    weight1 = npWight["w1"]
    weight2 = npWight["w2"]

    img = np.zeros(shape=[280, 280], dtype=np.uint8)
    cv2.namedWindow("hand_write")
    cv2.setMouseCallback("hand_write", draw, img)

    cv2.imshow("hand_write", img)
    while True:
        cv2.imshow("hand_write", img)
        if cv2.waitKey(10) == 27:
            break
