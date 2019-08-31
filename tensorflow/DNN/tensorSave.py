import tensorflow as tf
import numpy as np

vl = tf.Variable(tf.constant(1.0 , shape=[1]), name='v1')
v2 = tf.Variable(tf.constant(2.0 , shape=[1]) , name='v2')
result = vl + v2
saver = tf.train.Saver()
with tf.Session() as sess :
    sess.run(tf.global_variables_initializer())
    print(sess.run(result))
    saver.save(sess,"modelTest/model.ckpt")