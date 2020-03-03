import numpy as np

X = np.array(([3], [1], [2]))
Y = np.array(([1], [2], [3]))
theta = 0.5
h = X * theta
m = len(Y)


def costfunction(x, y, thetas):
    sumarry = []
    for x, y in zip(X, Y):
        sumvalue = (1 / (2 * m)) * np.math.pow(((x * thetas) - y), 2)
        sumarry.append(sumvalue)
    return sumarry


print(costfunction(X, Y, theta))
