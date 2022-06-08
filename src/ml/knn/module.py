"""K-Nearest Neighbor Classification & Regression in Python

Classification
--------------

We pick a value of k. Then, given a new data point, we classify the new data point based
on the classifications of its k nearest neighbors.

Regression
----------

We pick a value of k. Then, given a new data point (i.e., a new x value), we find the k
nearest points (i.e., the k nearest x values) around the new point and average the y
values for those k nearest points as the predicted y value for the new point.

Picking Values for K
--------------------

Low values for k can be noisy and subject to the effects of outliers. High values of k
smooth over things, but you don't want k to be so large that a category with only a few
samples in it will always be out voted by other categories.
"""

# pylint: disable=W0632

# Standard Library
from collections import Counter

# Third Party Library
import numpy as np

from matplotlib import pyplot as plt
from pandas import DataFrame
from sklearn.datasets import make_blobs, make_regression

# Generate classification data
X_train, Y_train = make_blobs(
    n_samples=300, centers=2, n_features=2, cluster_std=6, random_state=11
)
print(X_train.shape)
print(Y_train.shape)
print()

# Plot the data
df = DataFrame(dict(x=X_train[:, 0], y=X_train[:, 1], label=Y_train))
colors = {0: "blue", 1: "orange"}
fig, ax = plt.subplots(figsize=(8, 8))
grouped = df.groupby("label")
for key, group in grouped:
    group.plot(ax=ax, kind="scatter", x="x", y="y", label=key, color=colors[key])
plt.xlabel("X_1")
plt.ylabel("X_2")
# plt.show()


# Feature scaling
def normalize(X):
    x1_min, x1_max = min(X_train[:, 0]), max(X_train[:, 0])
    x2_min, x2_max = min(X_train[:, 1]), max(X_train[:, 1])
    f1 = lambda x: (x - x1_min) / (x1_max - x1_min)
    f2 = lambda x: (x - x2_min) / (x2_max - x2_min)
    X[:, 0], X[:, 1] = f1(X[:, 0]), f2(X[:, 1])
    return X


X = normalize(X_train)
print(X[0:5])
print()


# Heart of KNN
def find_neighbors(k, X_tr, new_point):
    neighbor_arr = []
    for i, x in enumerate(X_tr):
        dist = np.sqrt(sum(np.square(x - new_point)))
        neighbor_arr.append([i, dist])
    neighbor_arr = sorted(neighbor_arr, key=lambda x: x[1])
    return neighbor_arr[0:k]


# Classification with KNN
def classifier(neighbor_arr):
    class_arr = [Y_train[i[0]] for i in neighbor_arr]
    return Counter(class_arr).most_common(1)[0][0]


new_points = np.array([[-10, -10], [0, 10], [-15, 10], [5, -2]])
new_points = normalize(new_points)
knn = find_neighbors(4, X, new_points[1])
print(knn)
print(classifier(knn))
print()

# Generate regression data
X_train, Y_train = make_regression(
    n_samples=300, n_features=2, n_informative=2, noise=5, bias=30, random_state=200
)
print(X_train.shape)
print(Y_train.shape)
print()

# Feature scaling
X = normalize(X_train)
print(X[0:5])
print()


# Regression with KNN
def regressor(neighbor_arr):
    y_arr = [Y_train[i[0]] for i in neighbor_arr]
    return np.mean(y_arr)


new_points = np.array([[-1, 1], [0, 2], [-3, -2], [3, -3]])
new_points = normalize(new_points)
knn = find_neighbors(3, X_train, new_points[1])
print(knn)
print(regressor(knn))
