# tensorflow: 평균 제곱 오차
import numpy as np
import tensorflow as tf


def MSE(y, t):
    return tf.reduce_mean(tf.square(y - t))


t = np.array([1, 2, 3, 4])
y1 = np.array([0.5, 1, 1.5, 2])
print("MSE(t, y1) = ", MSE(t, y1).numpy())

y2 = np.array([0.5, 1.5, 2.5, 3.5])
print("MSE(t, y2) = ", MSE(t, y2).numpy())
