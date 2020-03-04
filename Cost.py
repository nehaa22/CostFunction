import numpy as np

X = [1, 2, 3]
Y = [1, 2.5, 3.5]
hypothesis = [0.5, 1.0, 1.5]

mvalue = len(X)
limit = (1 / (2 * mvalue))
values = []


def x_multiply_theta(x, theta):
    assumed = []
    for terms in range(mvalue):
        assumed.append(x[terms] * theta)
    return assumed


def cost_function(m, x, y):
    summation = 0
    for term in range(m):
        cost = np.math.pow((x[term] - y[term]), 2)
        summation += cost
    return summation / limit


for i in range(len(hypothesis)):
    hypothesis_values = x_multiply_theta(X, hypothesis[i])
    value = cost_function(mvalue, hypothesis_values, Y)
    values.append(value)

    print(hypothesis[i], ",", value)
print("Best fit for data :", min(values))
