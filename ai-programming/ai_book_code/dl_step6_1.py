import numpy as np


def MSE(y, t):
    return np.sum((y - t) ** 2) / t.size


x = np.arange(12)  # [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11]
t = np.arange(12)  # [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11]

# x 절편
w = 0.5  # 초기값
# y 절편
b = 0
lr = 0.001  # 0.01, learning rate = 학습률

loss_list = []
# epoch: 1epoch => 주어진 데이터를 한번 적용해본다.
for epoch in range(200):
    y = w * x + b  # calculate the output
    # dw: 미분 -> w의 변화율
    dW = np.sum((y - t) * x) / (2 * x.size)  # gradients
    print(np.sum((y - t) * x) / (2 * x.size))
    # dB: 미분 -> B의 변화율
    dB = np.sum((y - t)) / (2 * x.size)
    print(dB)

    w = w - lr * dW  # update parameters
    b = b - lr * dB

    y = w * x + b  # calculate the output
    loss = MSE(y, t)
    loss_list.append(loss)
    if not epoch % 10:
        print("epoch={}: w={:>8.4f}. b={:>8.4f}, loss={}".format(epoch, w, b, loss))

print("w={:>.4f}. b={:>.4f}, loss={:>.4f}".format(w, b, loss))

import matplotlib.pyplot as plt

plt.plot(loss_list)
plt.show()
