# numpy: 평균 제곱 오차(MSE)
import numpy as np


def mse(y, t):
    return np.sum((y - t) ** 2) / t.size


t = np.array([1, 2, 3, 4])
y1 = np.array([0.5, 1, 1.5, 2])

print(f"(t, y1): {t, y1}")
print("MSE(t, y1)=", mse(t, y1))

y2 = np.array([0.5, 1.5, 2.5, 3.5])
print("MSE(t, y2)=", mse(t, y2))
