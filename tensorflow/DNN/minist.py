from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import cv2

mnist = input_data.read_data_sets("./", one_hot=True)
labels = np.load("rusult.npy")
count=0
dataSet = np.zeros(shape = mnist.test.images.shape,dtype=np.uint8)
dataSet[np.where(mnist.test.images >= 0.5)] = 255
dataSet[np.where(mnist.test.images < 0.5)] = 0

npWight=np.load("weight.npz")

weight1=npWight["w1"]
weight2=npWight["w2"]
for i in range(0, 10000):
    imgdata = mnist.test.images[i].copy()
    lay1 = np.matmul(imgdata,weight1)
    laySig=lay1/(1+np.exp(-lay1))
    lay2 = np.matmul(laySig, weight2)

    labelCount=np.argmax(lay2)

    if np.where(mnist.test.labels[i] == 1)[0][0]==labelCount:
        continue
    data = np.reshape(dataSet[i], (28, 28))
    data = cv2.cvtColor(data, cv2.COLOR_GRAY2BGR)
    data = cv2.resize(data, (280, 280))
    # data = cv2.putText(data, str(np.where(mnist.train.labels[i] == 1)[0][0]), (5, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,                  (0, 255, 255), 2)
    data = cv2.putText(data, str(labelCount), (5, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2)
    count = count+1
    print (count)
    cv2.imshow("123", data)
    if cv2.waitKey(100) == 27:
        break
