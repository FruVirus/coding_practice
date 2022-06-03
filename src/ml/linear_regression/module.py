"""Linear Regression in Python

Linear regression is fitting a curve to the given data by expressing the output variable
by a linear combination of inputs and weights.

If we have overfitted from our hypothesis function, we can reduce the weight that some
terms in our function carry by increasing their cost. Regularization helps with
overfitting by keeping all features but reducing the magnitude of the model parameters.
Regularization works well when we have a lot of slightly useful features.

In order for the cost function to get close to 0, we will have to reduce the values of
model parameters to near zero. Lambda, the regularization parameter, determines how much
the costs of the model parameters are inflated. If lambda is too large, it may smooth
out the function too much and cause underfitting.
"""

# pylint: disable=W0632

# Third Party Library
import numpy as np

from matplotlib import pyplot as plt
from sklearn.datasets import make_regression

# Generating fake data
X, y = make_regression(
    n_samples=200, n_features=1, n_informative=1, noise=6, bias=30, random_state=200
)
print(X.shape)
print(y.shape)
print()
m = 200

# Visualizing the data
plt.scatter(X, y, c="red", alpha=0.5, marker="o")
plt.xlabel("X")
plt.ylabel("Y")
# plt.show()


# Linear model
def h(X, w):
    return w[1] * np.array(X[:, 0]) + w[0]


# Cost function
def cost(w, X, y, reg=1):
    return (0.5 / m) * (
        np.sum(np.square(h(X, w) - np.array(y))) + reg * np.sum(np.array(w) ** 2)
    )


# Gradient descent
def grad(w, X, y):
    g = [0] * 2
    g[0] = np.sum(h(X, w) - np.array(y)) / m
    g[1] = np.sum((h(X, w) - np.array(y)) * np.array(X[:, 0])) / m
    return g


def descent(w_prev, w_new, lr, reg=1):
    print(w_prev)
    print(cost(w_prev, X, y))
    for _ in range(500):
        w_prev = w_new
        grads = grad(w_prev, X, y)
        w0 = w_prev[0] - lr * grads[0]
        w1 = w_prev[1] - lr * grads[1] - lr * reg * w_prev[1] / m
        w_new = [w0, w1]
        print(w_new)
        print(cost(w_new, X, y))
        if (w_new[0] - w_prev[0]) ** 2 + (w_new[1] - w_prev[1]) ** 2 <= pow(10, -6):
            return w_new
    return w_new


# Training the model
w = [0, -1]
w = descent(w, w, 0.1)
print(w)


# Visualizing the result
def graph(formula, x_range):
    x = np.array(x_range)
    y = formula(x)
    plt.plot(x, y)


def my_formula(x):
    return w[0] + w[1] * x


plt.scatter(X, y, c="red", alpha=0.5, marker="o")
graph(my_formula, range(-5, 5))
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
