from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import numpy as np
import cv2



reader = tf.train.NewCheckpointReader("model/model1.ckpt")

all=reader.get_variable_to_shape_map()

for val in all:
    print(val,all[val])

w1=reader.get_tensor("Variable/ExponentialMovingAverage")
w2=reader.get_tensor("Variable_2/ExponentialMovingAverage")

np.savez("weight",w1=w1,w2=w2)