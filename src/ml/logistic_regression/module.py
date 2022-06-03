"""Logistic Regression in Python

Logistic regression is used to solve classification problems. A non-linear function
(i.e., the sigmoid or logistic function) is introduced on top of the linear function in
order to convert the outputs of the linear function in to the range [0, 1] so that we
can interpret its outputs as probabilities.

The cost function cannot be the same as that used for linear regression since the
logistic function will cause the hypothesis function to have many local minima (i.e., it
will not be a convex function).
"""

# pylint: disable=W0632

# Third Party Library
import numpy as np

from matplotlib import pyplot as plt
from pandas import DataFrame
from sklearn.datasets import make_blobs

# Creating fake data
X, Y = make_blobs(
    n_samples=200, centers=2, n_features=2, cluster_std=5, random_state=11
)
m = 200
print(X.shape)
print(Y.shape)
print()

# Visualizing the data
df = DataFrame(dict(x=X[:, 0], y=X[:, 1], label=Y))
colors = {0: "blue", 1: "orange"}
fig, ax = plt.subplots()
grouped = df.groupby("label")
for key, group in grouped:
    group.plot(ax=ax, kind="scatter", x="x", y="y", label=key, color=colors[key])
plt.xlabel("X_0")
plt.ylabel("X_1")
# plt.show()


# Logistic model
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def h(w, X):
    z = np.array(w[0] + w[1] * np.array(X[:, 0]) + w[2] * np.array(X[:, 1]))
    return sigmoid(z)


# Cost function - Binary Cross Entropy
def cost(w, X, Y, reg=1):
    y_pred = h(w, X)
    return -sum(Y * np.log(y_pred) + (1 - Y) * np.log(1 - y_pred)) / m + (
        0.5 * reg / m
    ) * np.sum(np.array(w) ** 2)


# Gradient descent
def grad(w, X, Y):
    y_pred = h(w, X)
    g = [0] * 3
    g[0] = sum(y_pred - Y) / m
    g[1] = sum((y_pred - Y) * X[:, 0]) / m
    g[2] = sum((y_pred - Y) * X[:, 1]) / m
    return g


def descent(w_prev, w_new, lr, reg=1):
    print(w_prev)
    print(cost(w_prev, X, Y))
    for _ in range(100):
        w_prev = w_new
        grads = grad(w_prev, X, Y)
        w0 = w_prev[0] - lr * grads[0]
        w1 = w_prev[1] - lr * grads[1] - lr * reg * w_prev[1] / m
        w2 = w_prev[2] - lr * grads[2] - lr * reg * w_prev[2] / m
        w_new = [w0, w1, w2]
        print(w_new)
        print(cost(w_new, X, Y))
        if (w_new[0] - w_prev[0]) ** 2 + (w_new[1] - w_prev[1]) ** 2 + (
            w_new[2] - w_prev[2]
        ) ** 2 < pow(10, -6):
            return w_new
    return w_new


# Training the model
w = [1, 1, 1]
w = descent(w, w, 0.0099)
print(w)


# Visualizing the result
def graph(formula, x_range):
    x = np.array(x_range)
    y = formula(x)
    plt.plot(x, y)


def my_formula(x):
    """The equation is w[0] + w[1] * x[0] + w[2] * x[1]. However, for the sake of
    plotting, we take x1 as the y-axis and x0 as the x-axis. The equation for a line in
    2D is ax + by + c = 0 --> y = (-c - ax) / b. In this case, a = w[1], b = w[2], and
    c = w[0].
    """

    return (-w[0] - w[1] * x) / w[2]


df = DataFrame(dict(x=X[:, 0], y=X[:, 1], label=Y))
colors = {0: "blue", 1: "orange"}
fig, ax = plt.subplots()
grouped = df.groupby("label")
for key, group in grouped:
    group.plot(ax=ax, kind="scatter", x="x", y="y", label=key, color=colors[key])
graph(my_formula, range(-20, 15))
plt.xlabel("X_0")
plt.ylabel("X_1")
plt.show()
