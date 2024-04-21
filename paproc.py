import matplotlib.pyplot as plt
import numpy as np

def fern(n_points=50000):
    x = np.zeros(n_points)
    y = np.zeros(n_points)

    for i in range(1, n_points):
        r = np.random.rand()
        if r <= 0.01:
            x[i], y[i] = 0, 0.16*y[i-1]
        elif r <= 0.86:
            x[i] = 0.85*x[i-1] + 0.04*y[i-1]
            y[i] = -0.04*x[i-1] + 0.85*y[i-1] + 1.6
        elif r <= 0.93:
            x[i] = 0.2*x[i-1] - 0.26*y[i-1]
            y[i] = 0.23*x[i-1] + 0.22*y[i-1] + 1.6
        else:
            x[i] = -0.15*x[i-1] + 0.28*y[i-1]
            y[i] = 0.26*x[i-1] + 0.24*y[i-1] + 0.44

    return x, y

x, y = fern()

plt.figure(figsize=(8, 10))
plt.scatter(x, y, s=1, color='green')
plt.axis('off')
plt.show()
