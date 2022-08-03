"""
Singular Value Decomposition
============================

Singular Value Decomposition, or SVD, is a computational method often employed to
calculate principal components for a dataset. Using SVD to perform PCA is efficient and
numerically robust. Moreover, the intimate relationship between them can guide our
intuition about what PCA actually does and help us gain additional insights into this
technique.

Singular Value Decomposition is a matrix factorization method utilized in many numerical
applications of linear algebra such as PCA. This technique enhances our understanding of
what principal components are and provides a robust computational framework that lets us
compute them accurately for more datasets.

Principal Component Analysis (PCA) is a procedure through which we try to remove the
redundancy present in the Dataset by projecting the given dataset to a different vector
space such that the covariance matrix (of the dataset in new space) is diagonalized.
Such a projection of the dataset is achieved by multiplying the given dataset with a
rotation matrix (which also turns out to be eigen-vectors of the covariance matrix). If
Y represents the transformed vector space and U and X represents rotation matrix and
dataset respectively, then:

Y = U.T * X, given that X has zero mean

In other words, PCA finds a linear projection of data into an orthogonal basis system
that has the minimum redundancy and preserves the variance in the data.

Singular Value Decomposition (SVD) of a given matrix tells us how exactly can we
decompose the matrix, in to its rotation and scaling parts, which gives us a relation in
terms of the covariance matrix as:

X * X.T = V * L^2 * V.T, where V is the eigen-vector of matrix X * X.T and L^2 is a
diagonal matrix containing information about the scaling part.

In other words, SVD is a general technique to decompose any given rectangular matrix
into a matrix of eigenvectors and eigenvalues.
"""
