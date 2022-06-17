"""Linear Discriminant Analysis (LDA)

LDA Main Ideas
--------------

LDA is like PCA in that it reduces dimensions. However, LDA focuses on maximizing the
separability among known categories so that we can make the best decisions. In PCA, we
reduce dimensions and are interested in the categories with the most variation.

LDA with 2 categories and 2 variables
-------------------------------------

For example, we can use LDA to reduce a 2D graph to a 1D graph in such a way that
maximizes the separability of the data points in 1D.

A naive way is to just ignore one dimension (e.g., the Y values) and project the data
into the other dimension (e.g., the X axis). This is bad because it ignores the useful
information that the Y values provide.

LDA provides a better way by:
    1. Using information from both X and Y values to create a new axis
    2. Projecting the data onto this new axis in a way to maximize the separation of the
two categories.

How LDA creates new axes
------------------------

The new axis is created according to two criteria (considered simultaneously):

1. Once the data is projected onto the new axis, we want to maximize the distance
between the means of the two categories.

2. Minimize the variation (the scatter, s ^ 2) within each category.

To consider the two criteria simultaneously, we want to maximize:

(mu_1 - mu_2) ^ 2 / (s_1 ^ 2 + s_2 ^ 2) = d ^ 2 / (s_1 ^ 2 + s_2 ^ 2)

Ideally, we want the numerator to be large and the denominator to be small.

If we only maximized the distance between means, we will end up with a projection with a
lot of overlap in the middle.

However, if we optimize the distance between means the scatter, then we get nice
separation with minimal overlap in the middle. We might end up with closer means, but
less scatter.

LDA with 2 categories and 3 or more variables
---------------------------------------------

The process is the same:
    - Create an axis that maximizes the distance between the means for the two
categories while minimizing the scatter

LDA for 3 categories
--------------------

In this case, two things change (but barely).

The first difference is how you measure the distances among the means. We first find a
point that is central to all of the data. Then we measure the distance between a point
that is central in each category and the main central point.

Now we want to maximize the distance between each category's central point and the main
central point while minimizing the scatter for each category.

To consider the three criteria simultaneously, we want to maximize:

(d_1 ^ 2 + d_2 ^ 2 + d_3 ^ 2) ^ 2 / (s_1 ^ 2 + s_2 ^ 2 + s_3 ^ 2), where the distances
are between each category's central point and the main central point.

The second difference is that LDA creates 2 axes to separate the data. This is because
the 3 central points for each category define a plane (2 points define a line but 3
points define a plane).

Similarities between LDA and PCA
--------------------------------

Both methods rank the new axes in order of importance
    - PC1 accounts for the most variation in the data and so on
    - LD1 accounts for the most variation between the categories and so on

Summary of concepts
-------------------

LDA is like PCA---both try to reduce dimensions
    - PCA looks at variables with the most variation
    - LDA tries to maximize the separation between categories

Misc.
-----

Logistic regression is a simple and powerful linear classification algorithm. It also
has limitations that suggest at the need for alternate linear classification algorithms.

Two-Class Problems. Logistic regression is intended for two-class or binary
classification problems. It can be extended for multi-class classification, but is
rarely used for this purpose.

Unstable With Well Separated Classes. Logistic regression can become unstable when the
classes are well separated.

Unstable With Few Examples. Logistic regression can become unstable when there are few
examples from which to estimate the parameters.

Linear Discriminant Analysis does address each of these points and is the go-to linear
method for multi-class classification problems. Even with binary-classification
problems, it is a good idea to try both logistic regression and linear discriminant
analysis.
"""
