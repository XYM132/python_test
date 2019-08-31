import numpy as np
from matplotlib import pyplot as plt

data = np.array([0, 10, 20, 10, 0, 10, 20, 30, 5, 0, 10, 20, 10, 0, 10, 20, 30, 5, 0, 10, 20, 10, 0, 10, 20, 30, 5, 0, 10, 20, 10, 0, 10, 20, 30, 5,0, 10, 20, 10, 0, 10, 20, 30, 5, 0, 10, 20, 10, 0, 10, 20, 30, 5, 0, 10, 20, 10, 0, 10, 20, 30, 5, 0, 10, 20, 10, 0, 10, 20, 30, 5])

dataAvg = np.zeros(shape=data.shape, dtype=np.float)
dataMoveAvg = np.zeros(shape=data.shape, dtype=np.float)
dataMoveAvgBia = np.zeros(shape=data.shape, dtype=np.float)
dataMoveAvg[0] = data[0]
dataMoveAvgBia[0] = data[0]
for i in range(0, int(data.shape[0])):
    sum = 0
    for j in range(0, i + 1):
        sum = data[j] + sum
    dataAvg[i] = sum / (i + 1)
    if i > 0:
        dataMoveAvg[i] = 0.8 * dataAvg[i - 1] + 0.2 * data[i]
        dataMoveAvgBia[i] = dataMoveAvg[i]/(1-0.8**(i))

plt.plot(data, color='red')
plt.plot(dataAvg, color=[0.8,0.5,0])
plt.plot(dataMoveAvg, color='blue')
plt.plot(dataMoveAvgBia, color=[0.8,0.5,0.8])
plt.show()
