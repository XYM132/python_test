import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

inputNode = 784
outputNode = 10

layer1Node = 500
batchSize = 100

learningRateBase = 0.8
learningRateDecay = 0.99

regularizationRate = 0.0001
trainingSteps = 30000
movingAverageDecay = 0.99


def inference(inputTensor, avgClass, weights1, biases1, weights2, biases2):
    if avgClass is None:
        layer1 = tf.nn.relu(tf.matmul(inputTensor, weights1) + biases1)

        return tf.matmul(layer1, weights2) + biases2
    else:
        layer1 = tf.nn.relu(tf.matmul(inputTensor, avgClass.average(weights1)) + avgClass.average(biases1))

        return tf.matmul(layer1, avgClass.average(weights2)) + avgClass.average(biases2)


def train(mnist,isTrain=True):
    x = tf.placeholder(tf.float32, [None, inputNode], name='x-input')
    y_ = tf.placeholder(tf.float32, [None, outputNode], name='y-input')

    weights1 = tf.Variable(tf.truncated_normal([inputNode, layer1Node], stddev=0.1))
    biases1 = tf.Variable(tf.constant(0.1, shape=[layer1Node]))

    weights2 = tf.Variable(tf.truncated_normal([layer1Node, outputNode], stddev=0.1))
    biases2 = tf.Variable(tf.constant(0.1, shape=[outputNode]))

    y = inference(x, None, weights1, biases1, weights2, biases2)

    globalStep = tf.Variable(0, trainable=False)

    variable_averages = tf.train.ExponentialMovingAverage(movingAverageDecay, globalStep)

    variable_averages_op = variable_averages.apply(tf.trainable_variables())

    average_y = inference(x, variable_averages, weights1, biases1, weights2, biases2)

    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.arg_max(y_, 1))

    cross_entropy_mean = tf.reduce_mean(cross_entropy)

    regularizer = tf.contrib.layers.l2_regularizer(regularizationRate)

    regularization = regularizer(weights1) + regularizer(weights2)

    loss = cross_entropy_mean + regularization

    learn_rate = tf.train.exponential_decay(learningRateBase, globalStep, mnist.train.num_examples / batchSize,
                                            learningRateDecay)

    train_step = tf.train.GradientDescentOptimizer(learn_rate).minimize(loss, global_step=globalStep)

    with tf.control_dependencies([train_step, variable_averages_op]):
        train_op = tf.no_op(name='train')

    correct_prediction = tf.equal(tf.arg_max(average_y, 1), tf.arg_max(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    result = tf.arg_max(average_y, 1)

    saver=tf.train.Saver()
    if isTrain:
        with tf.Session() as sess:
            tf.initialize_all_variables().run()

            validate_feed = {x: mnist.validation.images,
                             y_: mnist.validation.labels}

            test_feed = {x: mnist.test.images,
                         y_: mnist.test.labels}

            for i in range(trainingSteps):
                if i % 1000 == 0:
                    validata = sess.run(accuracy, feed_dict=validate_feed)
                    print(i, validata)
                xs, ys = mnist.train.next_batch(batchSize)

                dataSet = np.zeros(shape=xs.shape, dtype=np.uint8)
                dataSet[np.where(xs >= 0.5)] = 1
                dataSet[np.where(xs < 0.5)] = 0

                sess.run(train_op, feed_dict={x: dataSet, y_: ys})

            result, test_acc = sess.run([result, accuracy], feed_dict=test_feed)
            # saver.save(sess,'model/model1.ckpt')
            #np.save("rusult", result)
            print("end", test_acc)

def mnist_eval(data):
    x = tf.placeholder(tf.float32, [None, inputNode], name='x-input')

    weights1 = tf.Variable(tf.truncated_normal([inputNode, layer1Node], stddev=0.1))
    biases1 = tf.Variable(tf.constant(0.1, shape=[layer1Node]))

    weights2 = tf.Variable(tf.truncated_normal([layer1Node, outputNode], stddev=0.1))
    biases2 = tf.Variable(tf.constant(0.1, shape=[outputNode]))

    y = inference(x, None, weights1, biases1, weights2, biases2)

    globalStep = tf.Variable(0, trainable=False)

    variable_averages = tf.train.ExponentialMovingAverage(movingAverageDecay, globalStep)

    variable_averages_op = variable_averages.apply(tf.trainable_variables())

    average_y = inference(x, variable_averages, weights1, biases1, weights2, biases2)

    result = tf.arg_max(average_y, 1)

    saver = tf.train.Saver()
    with tf.Session() as sess:
        saver.restore(sess,"model/model1.ckpt")
        test_feed = {x:np.reshape(data,[1,784])}
        result = sess.run(result, feed_dict=test_feed)
        print("result", result)
        return result[0]

def main():
    mnist = input_data.read_data_sets("./", one_hot=True)
    #train(mnist,False)
    mnist_eval(mnist.test.images[1])


if __name__ == "__main__":
    main()
