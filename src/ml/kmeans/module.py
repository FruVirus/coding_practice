"""K-means Clustering in Python

The K-means algorithm is used to group data into coherent subsets via the following
iterative procedure:

1. randomly initialize two points in the dataset called the cluster centroids; in
general, have k < m, where m is the number of training examples

2. cluster assignment: assign all examples into one of two groups based on which cluster
centroid the example is closest to

3. move centroid: compute the averages for all the points inside each of the two
cluster centroid groups, then move the cluster centroid points to those averages

4. rerun 2 and 3 until we have found our clusters

K-means can still evenly segment your data into k clusters even for datasets with no
real inner separation or natural structure.

The optimization objective finds all the values in sets C, representing our clusters,
and mu, representing all our centroids, that will minimize the average of the distances
of every training example to its corresponding cluster centroid.

In the cluster assignment step, the goal is to minimize the cost function with C,
holding mu fixed.

In the move centroid step, the goal is to minimize the cost function with mu, holding C
fixed.

With K-means, it is not possible for the cost function to sometimes increase; it should
always decrease (unless it gets stuck in a local optima).

K-means can get stuck in local optima. To decrease the changes of this happening, you
can run the algorithm on many different random initializations and then pick the
clustering that gives the lowest cost.

Choosing k can be quite arbitrary and ambiguous. The cost function should reduce as we
increase the number of clusters an then flatten out --> choose k at the point where the
cost function starts to flatten out --> elbow method. However, fairly often, the curve
is very gradual, so there's no clear elbow.

Another way to choose k is to observe how well K-means performs on a downstream purpose.
That is, you choose k that proves to be most useful for some goal you're trying to
achieve from using these clusters.
"""

# pylint: disable=W0632

# Third Party Library
import numpy as np

from matplotlib import pyplot as plt
from pandas import DataFrame
from sklearn.datasets import make_blobs

# Generate clustering data
X_train, _ = make_blobs(n_samples=500, centers=3, n_features=2, random_state=20)
print(X_train.shape)
print()

# Visualize the data
df = DataFrame(dict(x=X_train[:, 0], y=X_train[:, 1]))
fig, ax = plt.subplots(figsize=(8, 8))
df.plot(ax=ax, kind="scatter", x="x", y="y")
plt.xlabel("X_1")
plt.ylabel("X_2")
# plt.show()


# Helper functions for K-means
def assign_cluster(k, X, cg):
    cluster = [-1] * len(X)
    for i, x in enumerate(X):
        dist_arr = []
        for j in range(k):
            dist_arr.append(dist(x, cg[j]))
        idx = np.argmin(dist_arr)
        cluster[i] = idx
    return np.asarray(cluster)


def compute_centroids(k, X, cluster):
    cg_arr = []
    for i in range(k):
        arr = []
        for j, x in enumerate(X):
            if cluster[j] == i:
                arr.append(x)
        cg_arr.append(np.mean(arr, axis=0))
    return np.asarray(cg_arr)


def dist(a, b):
    return np.sqrt(sum(np.square(a - b)))


def init_centroids(k, X):
    arr = []
    for _ in range(k):
        cx1 = np.random.uniform(min(X[:, 0]), max(X[:, 0]))
        cx2 = np.random.uniform(min(X[:, 1]), max(X[:, 1]))
        arr.append([cx1, cx2])
    return np.asarray(arr)


def measure_change(cg_new, cg_prev):
    res = 0
    for a, b in zip(cg_new, cg_prev):
        res += dist(a, b)
    return res


def show_clusters(X, cluster, cg):
    df = DataFrame(dict(x=X[:, 0], y=X[:, 1], label=cluster))
    colors = {0: "blue", 1: "orange", 2: "green"}
    _, ax = plt.subplots(figsize=(8, 8))
    grouped = df.groupby("label")
    for key, group in grouped:
        group.plot(ax=ax, kind="scatter", x="x", y="y", label=key, color=colors[key])
    ax.scatter(cg[:, 0], cg[:, 1], marker="*", s=150, c="#ff2222")
    plt.xlabel("X_1")
    plt.ylabel("X_2")
    plt.show()


# K-means
def k_means(k, X):
    cg_prev = init_centroids(k, X)
    cluster = [0] * len(X)
    cg_change = 100
    while cg_change > 0.001:
        cluster = assign_cluster(k, X, cg_prev)
        show_clusters(X, cluster, cg_prev)
        cg_new = compute_centroids(k, X, cluster)
        cg_change = measure_change(cg_new, cg_prev)
        cg_prev = cg_new
    return cluster


cluster = k_means(3, X_train)
print(cluster)
