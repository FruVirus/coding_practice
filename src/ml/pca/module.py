"""Principal Component Analysis in Python

PCA is a dimensionality reduction technique. Given two features, x_1 and x_2, we want to
find a single line that effectively describes both features at once. We then map our old
features onto this new line to get a new single feature representation of the data. The
same can be done with three features, where we map them onto a plane. The goal of PCA is
to reduce the average of all the distances of every feature to the projection line. This
is the projection error.

In Linear Regression we are trying to maintain a relationship between a value on the
x-axis, and the value it would predict on the y-axis. In other words, the x-axis is used
to predict values on the y-axis. This is why we use the vertical distance to measure
error - because that tells us how far off our prediction is for the true value. In PCA,
no such relationship exists, so we minimize the perpendicular distances (i.e., the
shortest orthogonal distances) between the data and the line.

0. Perform feature scaling and mean normalization on the data points.

1. Calculate the average values for x_1 and x_2. With the average values, we know the
center of the data points.

2. Shift the data so that the center is on top of the origin (0, 0). Shifting the data
does not change how the data points are positioned relative to each other.

3. Now that the data is centered on the origin, we can try to fit a line to it. We start
by drawing a random line that goes through the origin. Then we rotate the line until it
fits the data as well as it can, given that it has to go through the origin.

To quantify how good a line fits the data, PCA projects the data onto the line and then
it can either measure the distances from the data to the line and try to find the line
that minimizes those distances OR it can try to find the line that maximizes the
distances from the projected points to the origin. PCA finds the best fitting line by
maximizing the sum of the squared distances from the projected points to the origin
since it's an easier calculation.

The line with the largest sum of squared distances from the projected points to the
origin is called Principal Component 1 (PC1). If the slope of PC1 is 0.25, then this
means that for every 4 units we increase x_1 by, x_2 increases by 1. This means the data
is mostly spread out along the x_1 axis and only a little bit spread out along the x_2
axis. Thus, x_1 is more important in terms of describing the data.

PCA using SVD scales the hypotenuse so that its length is 1 and scales the other sides
accordingly. However, the ratio of x_1 to x_2 remains the same. This unit vector for PC1
is called the singluar vector or the eigenvector for PC1. The sum of squared distances
for PC1 is called the eigenvalue for PC1 and the square root of the eigenvalue for PC1
is called the singular value for PC1.

For PC2, it is simply the line through the origin that is perpendicular to PC1 since we
are working with 2D data.

Once you have all of the PCs figured out, you can use the eigenvalues to determine the
proportion of variation that each PC accounts for. The sum of squared distances divided
by (n - 1) is the variation for each PC. You can then take the highest variance PCs as
the main variables (e.g., to use for plotting). Differences along PC1 are more important
than differences along PC2, etc. Thus, if data points separated by the same distances
along PC1 and PC2, the data points along PC1 are more different from each other than the
data points along PC2.

In theory, there is one PC for each variable. In practice, the number of PCs is either
the number of variables or the number of samples, whichever is smaller.

Advice on Applying PCA
----------------------

The most common use of PCA is to speed up supervised learning, compressing data, and to
visualize high dimensional data. A bad use of PCA is to prevent overfitting. It might
work but it is not recommended since it does not consider the values of our results, y.
Instead, use regularization to prevent overfitting.

Note that we should define the PCA reduction only on the training set and not on the
validation or test sets. You can apply the PCA mapping on the validation/test set after
it is defined on the training set.

Misc.
-----

We can also view PCA as an unsupervised learning algorithm that learns a representation
of data. PCA learns a representation that has lower dimensionality than the original
input. It also learns a representation whose elements have no linear correlation with
each other. However, to achieve full independence, a representation learning algorithm
must also remove the nonlinear relationships between variables.

PCA learns an orthogonal, linear transformation of the data that projects an input x to
a representation z. PCA preserves as much of the information in the data possible as
measured by least-squares reconstruction error.

The ability of PCA to transform data into a representation where the elements are
mutually uncorrelated is a very important property of PCA. It is a simple example of a
representation that attempts to disentangle the unknown factors of variation underlying
the data. In the case of PCA, this disentangling takes the form of finding a rotation of
the input space (described by a weight matrix, W) that aligns the principal axes of
variance with the basis of the new representation space associated with z.
"""

# Standard Library
import random

# Third Party Library
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn import preprocessing
from sklearn.decomposition import PCA

# Generate data
genes = ["gene" + str(i) for i in range(1, 101)]
wt = ["wt" + str(i) for i in range(1, 6)]
ko = ["ko" + str(i) for i in range(1, 6)]
data = pd.DataFrame(columns=[*wt, *ko], index=genes)
for gene in data.index:
    data.loc[gene, "wt1":"wt5"] = np.random.poisson(  # type: ignore
        lam=random.randrange(10, 1000), size=5
    )
    data.loc[gene, "ko1":"ko5"] = np.random.poisson(  # type: ignore
        lam=random.randrange(10, 1000), size=5
    )
print(data.head())
print(data.shape)
print()

# Feature scaling and data normalization
scaled_data = preprocessing.scale(data.T)

# Perform PCA
pca = PCA()  # create a PCA object
pca.fit(scaled_data)  # do the math
pca_data = pca.transform(scaled_data)  # get PCA coordinates for scaled_data

# Scree and PCA plot
per_var = np.round(pca.explained_variance_ratio_ * 100, decimals=1)
labels = ["PC" + str(i) for i in range(1, len(per_var) + 1)]

plt.bar(x=range(1, len(per_var) + 1), height=per_var, tick_label=labels)
plt.ylabel("Percentage of Explained Variance")
plt.xlabel("Principal Component")
plt.title("Scree Plot")
plt.show()

pca_df = pd.DataFrame(pca_data, index=[*wt, *ko], columns=labels)
plt.scatter(pca_df.PC1, pca_df.PC2)
plt.title("My PCA Graph")
plt.xlabel("PC1 - {0}%".format(per_var[0]))
plt.ylabel("PC2 - {0}%".format(per_var[1]))
for sample in pca_df.index:
    plt.annotate(sample, (pca_df.PC1.loc[sample], pca_df.PC2.loc[sample]))
plt.show()

# Determine which genes had the biggest influence on PC1
# First, get the loading scores.
loading_scores = pd.Series(pca.components_[0], index=genes)

# Now sort the loading scores based on their magnitude.
sorted_loading_scores = loading_scores.abs().sort_values(ascending=False)

# Get the names of the top 10 genes.
top_10_genes = sorted_loading_scores[0:10].index.values

print(loading_scores[top_10_genes])
