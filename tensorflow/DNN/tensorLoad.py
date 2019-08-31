import tensorflow as tf
import numpy as np

saver=tf.train.import_meta_graph("modelTest/model.ckpt.meta")

vl = tf.Variable(tf.constant(1.0 , shape=[1]), name='v1')
v2 = tf.Variable(tf.constant(2.0 , shape=[1]) , name='v2')

#saver= tf.train.Saver ()
with tf.Session() as sess:
    saver.restore(sess,"modelTest/model.ckpt")

    print(sess.run(tf.get_default_graph().get_tensor_by_name("add:0")))