"""Support Vector Machines

Part 1: Main Ideas
==================

Basic concepts and Maximal Margin Classifiers
---------------------------------------------

The shortest distance between the observations and the threshold is called the margin.
If put we put the threshold halfway between two observations, the distances between the
observations and the threshold are the same and both reflect the margin. When the
threshold is halfway between the two observations, the margin is as large as it can be.
When we use the threshold that gives us the largest margin to make classifications, we
are using a Maximal Margin Classifier.

Maximal Margin Classifiers are super sensitive to outliers in the training data and
thus, have high variance.

Soft Margins (allowing misclassifications)
------------------------------------------

To make a threshold that is not so sensitive to outliers, we must allow
misclassifications. Choosing a threshold that allows misclassifications is an example of
the Bias/Variance Tradeoff that plagues all of machine learning.

When we allow misclassifications, the distance between the observations and the
threshold is called a Soft Margin. To determine the best Soft Margin, we use Cross
Validation to determine how many misclassifications and observations to allow inside of
the Soft Margin to get the best classification.

Soft Margin and Support Vector Classifiers
------------------------------------------

When we use a Soft Margin to determine the location of a threshold, then we are using a
Soft Margin Classifier; i.e., a Support Vector Classifier to classify observations. The
name Support Vector Classifier comes from the fact that the observations on the edge and
within the Soft Margin are called Support Vectors.

When the data are 2D, a Support Vector Classifier is a line. Observations within the
Soft Margin are misclassified and vice versa.

When the data are 3D, a Support Vector Classifier forms a plane, instead of a line and
we classify new observations by determining which side of the plane they are on.

And when the data are in 4 or more dimensions, the Support Vector Classifier is a
hyperplane.

Support Vector Classifiers can handle outliers and, because they allow
misclassifications, they can handle overlapping classifications.

But what if our training data had tons of overlap? Support Vector Classifiers don't
perform well on data with tons of overlap.

Intuition behind Support Vector Machines
----------------------------------------

The main ideas behind Support Vector Machines are:

1. Start with data in a relatively low dimension.

2. Move the data into a higher dimension.

3. Find a Support Vector Classifier that separates the higher dimensional data into two
groups.

The polynomial kernel function
------------------------------

How do we decide how to transform the data?

In order to make the mathematics possible, Support Vector Machines use something called
Kernel Functions to systematically find Support Vector Classifiers in higher dimensions.

The polynomial kernel has a parameter, d, which stands for the degree of the polynomial.

When d = 1, the Polynomial Kernel computes the relationships between each pair of
observations in 1D and these relationships are used to find a Support Vector Classifier.

When d = 2, we get a second dimension based on x^2 and the Polynomial Kernel computes
the 2D relationships between each pair of observations and those relationships are used
to find a Support Vector Classifier.

And so on.

In summary, the Polynomial Kernel systematically increases dimensions by setting d, the
degree of the polynomial and the relationships between each pair of observations are
used to find a Support Vector Classifier. We can find a good value for d with Cross
Validation.

The radial basis function (RBF) kernel
--------------------------------------

The RBF kernel finds Support Vector Classifiers in infinite dimensions. The RBF Kernel
behaves like a Weighted Nearest Neighbor model. The closest observations (i.e., the
nearest neighbors) have a lot of influence on how we classify a new observation and
observations that are further away have relatively little influence on the
classification.

The kernel trick
----------------

Kernel functions only calculate the relationships between every pair of points as if
they are in the higher dimension---they don't actually do the transformation (i.e., they
don't actually transform the data points).

This trick, calculating the high-dimensional relationships without actually transforming
the data to the higher dimension, is called The Kernel Trick. The Kernel Trick reduces
the amount of computation required for SVMs by avoiding the math that transforms the
data from low to high dimensions and it makes calculating the relationships in the
infinite dimensions used by the RBF kernel possible.

Summary of concepts
-------------------

When we have 2 categories, but no obvious linear classifier that separates them in a
nice way, SVMs work by moving the data into a relatively high dimensional space and
finding a relatively high dimensional Support Vector Classifier that can effectively
classify the observations.

Part 2: The Polynomial Kernel
=============================

The Polynomial Kernel is defined as:

(a * b + r) ^ d

a and b refer to two different observations in the dataset. r determines the coefficient
of the polynomial. d sets the degree of the polynomial.

(a * b + 0.5) ^ 2 = (a * b + 0.5) * (a * b + 0.5)
                = (a, a ^ 2, 0.5) dot (a, a ^ 2, 0.5)

The Dot Product gives us the high-dimensional coordinates for the data. The first term
are the x-axis coordinates of a and b. The second terms are the y-axis coordinates of
a and b. The third terms are the z-axis coordinates but we ignore them since they are
the same.

It turns out that all we need to do to calculate the high-dimensional relationships is
to calculate the Dot Product between each pair of points. In other words, since the
kernel is equal to the Dot Product, all we need to do is plug values into the kernel to
get the high-dimensional relationships without actually transforming the data. In some
sense, the relationships are similar to transforming the data to the higher dimension
and calculating the distances between the data points in the higher dimension.

Part 3: The Radial (RBF) Kernel
===============================

The RBF Kernel is defined as:

e ^ (-gamma * (a - b) ^ 2)

a and b refer to two different observations in the dataset. The difference between the
measurements is squared, giving us the squared distances between the two observations.
Thus, the amount of influence one observation has on another is a function of the
squared distance.

gamma, which is determined by Cross Validation, scales the squared distance, and thus,
it scales the influence. Thus, the further two observations are from each other, the
less influence they have on each other.

Just like the Polynomial Kernel, when we plug values into the Radial Kernel, we get the
high-dimensional relationships.

When r = 0, the Polynomial Kernel is (a * b) ^ d = (a ^ d) dot (b ^ d). In other words,
when r = 0, all the Polynomial Kernel does is shift the data down the original axis.
Larger values of d shifts the data further down the axis. So setting r = 0 leaves the
data in the original dimension, regardless of the value of d.

However, we can add a Polynomial Kernel with r = 0 and d = 1 to a Polynomial Kernel with
r = 0 and d = 2 to get:

a * b + a ^ 2 * b ^ 2 = (a, a ^ 2) dot (b, b ^ 2)

This gives us a Dot Product with coordinates for 2D.

If we add another Polynomial Kernel with r = 0 and d = 3, then the Dot Product has
coordinates for 3D, and so on.

If we kept adding polynomials with r = 0 and increasing d until d = infinity, then we
have a Dot Product with coordinates for an infinite number of dimensions and we will
have the RBF kernel.

That means that when we use the RBF Kernel and plug in two points a and b, the value we
get at the end is the relationship between the two points in infinite dimensions.
"""
