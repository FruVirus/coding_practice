"""
Decision and Classification Trees
=================================

Basic Decision Tree Concepts
----------------------------

In general, a Decision Tree makes a statement and then makes a decision based on whether
or not the statement is True or False.

When a Decision Tree classifies things into categories, it's called a Classification
Tree.

When a Decision Tree predicts numeric values, it's called a Regression Tree.

A Decision Tree can also mix numeric and binary data in the same tree. In addition,
numeric thresholds for a Decision Tree node can be different for the same data and the
classifications at each leaf can be repeated.

At each node, if the node conditions evaluates to True, we take the left path;
otherwise, we take the right path.

The first node is the Root Node, internal nodes are nodes where decisions are made, and
leaf nodes form the output of the Decision Tree.

Building a tree with Gini impurity
----------------------------------

When starting to build a Decision Tree, you have to make a choice as to which feature
should be the Root Node. If you were to build a Decision Tree by trying out all features
as the Root Node, you will see that some choices for Root Nodes lead to impure leaf
nodes (leaf nodes where there is a mixture of classifications), whereas other choices
can lead to pure leaf nodes (leaf nodes where there is only one classification).

If a tree has fewer impure leaf nodes, then it is considered better than a tree with
more impure leaf nodes.

There are several ways to quantify the impurity of leaf nodes for a given Root Node. The
most popular method is called Gini Impurity; others include Entropy and Information
Gain.

To calculate the Gini Impurity associated with a given Root Node, we start by
calculating the Gini Impurity for the individual leaves.

Gini Impurity for a Leaf = 1 - p("Yes") ^ 2 - p("No") ^ 2

Since leaf nodes will generally contain unequal number of samples, we use the Total Gini
Impurity.

Leaf Weight = Total Number of Leaf Samples / Total Number of Samples Across all Leaves

Total Gini Impurity = Sum(Leaf Weight * Gini Impurity for Leaf)

Numeric and continuous variables
--------------------------------

Calculating the Gini Impurity for numeric data is a bit more involved.

The first thing we do is sort the rows by the numeric value from lowest to highest. Then
we calculate the average value for all adjacent pairs of rows. The average values form
the decision values for each internal node. Lastly, we calculate the Gini Impurity
values for each average age similar to the calculation above.

The feature with the lowest Gini Impurity is chosen as the Root Node. Having chosen the
Root Node, we can define the first split for the Decision Tree.

Adding branches
---------------

Subsequent branches are added by repeating the procedure above for the Root Node. That
is, we consider the rest of the features as internal nodes and pick the internal node
that gives the lowest Gini Impurity. The main difference is that we only consider the
subset of samples that fall into each of the two branches from the Root Node when
building subsequent nodes.

Adding leaves
-------------

Leaf nodes are formed when we make internal nodes with 0 Gini Impurity or we reach a
pre-specified maximum depth for the Decision Tree.

Defining output values
----------------------

Generally speaking, the output of a Leaf Node is whatever category that has the most
values (i.e., the majority value).

Using the tree
--------------

For a new data point, we simply traverse the Decision Tree until we end up at a Leaf
Node. The category assigned by the Leaf Node is our prediction.

How to prevent overfitting
--------------------------

If a Leaf Node has relatively few samples, it's hard to have confidence that it will do
a great job making predictions with unseen data and it is possible that we have overfit
the training data.

In practice, there are two main ways to deal with overfitting. One way is pruning.
Another way is to put limits on how the Decision Tree can grow (e.g., by requiring a
certain number of samples per Leaf Node). We can pick the best value for the number of
samples per Leaf Node using Cross Validation.

We might end up with impure Leaf Nodes, but the hope is that the Decision Tree is better
at generalization overall.

Even when a Leaf Node is impure, we still need an output value to make a
classification. The classification is decided by the majority class in the Leaf Node.

Decision Trees - Feature Selection and Missing Data
===================================================

Feature Selection
-----------------

Decision Trees have the downside of often overfitting to the training data. Requiring
each split to make a large reduction in impurity helps a tree from overfitting.

If the Gini Impurity for an Internal Node is lower without separating the Internal Node
into more nodes, then we make the Internal Node a Leaf Node.

If a feature never gives a reduction in Gini Impurity, we would not use that feature as
an Internal Node in the Decision Tree. This is a type of automatic feature selection.

However, we could have also created a threshold such that the impurity reduction has to
be large enough to make a big difference. As a result, we end up with simpler trees that
are less likely to overfit.

Missing Data
------------

We could either skip over missing data or fill in the missing data with the most common
option for that feature. We could also find another feature that has the highest
correlation with the missing feature column and use that as a guide (e.g., if the
correlated features is "Yes", then the missing feature could also be "Yes").

For numeric data, we could replace missing values with the mean/median or find another
feature column that is correlated with the missing numeric feature and do a linear
regression between the two columns and use the least squares line to predict the missing
value.

Regression Trees
================

Motivation for Regression Trees
-------------------------------

If the relationship between two variables was linear, we could do linear regression to
predict Y given X. However, if the relationship is nonlinear, then linear regression
would not work.

Regression Trees vs. Classification Trees
-----------------------------------------

One option is to use a Regression Tree. In a Regression Tree, each leaf represents a
numeric value. In contrast, Classification Trees typically have True/False or some other
discrete category in their leaf nodes.

The predictions for each leaf node is typically the average of the sample values that
ended up at the leaf node.

Building a Regression Tree with one variable
--------------------------------------------

We pick the first threshold as the average between the first two data points. The
samples are then split between this average. We then calculate the sum of all the
residuals (i.e., the squared difference between the ground-truth and predicted values)
for the first threshold.

We then pick the next two data points, calculate their average value as the split point
and calculate the sum of all the residuals again.

We repeat this process until we have calculated the sum of squared residuals for all of
the remaining thresholds.

The threshold with the lowest sum of squared residuals is chosen as the decision split
for the first node.

In summary, we split the data into two groups by finding the threshold that gave us the
smallest sum of squared residuals.

The process then repeats itself for each branch of the first node.

If a node has only one sample, then it is considered a leaf node. If the sum of squared
residuals is 0 for a node, then it is considered a leaf node.

To prevent overfitting to the training data, we can only split observations when there
are more than some minimum number.

Building a Regression Tree with multiple variables
--------------------------------------------------

For multiple variables, we pick each variable in turn, determine the best threshold for
a particular variable based on the sum of squared residuals, and pick the variable that
gave the lowest sum of squared residuals overall as the node.

Summary of concepts and main ideas
----------------------------------

1. Regression Trees are a type of Decision Tree.

2. In a Regression Tree, each leaf represents a numeric value.

3. We determine how to divide the observations by trying different thresholds and
calculating the sum of squared residuals for each threshold.

4. The threshold with the smallest sum of squared residuals becomes a node.

5. If we have multiple variables, we find the optimal threshold for each one and pick
the candidate with the smallest sum of squared residuals overall.

6. When we have fewer than some minimum number of observations in some node, then that
node becomes a leaf. This helps with overfitting. Otherwise, we repeat the process to
split the remaining observations until we can no longer split the observations into
smaller groups and then we are done.

How to Prune Regression Trees
=============================

Motivating for pruning a tree
-----------------------------

The main idea behind pruning a Regression Tree is to prevent overfitting to the training
data so that the tree will do a better job on unseen data. There are several methods for
pruning Regression Trees. Here, we consider Cost Complexity Pruning (a.k.a. Weakest Link
Pruning).

One way to prevent overfitting a Regression Tree to the training data is to remove some
of the leaf nodes and replace the split with a leaf node that is the average of a larger
number of observations. The new Regression Tree might have larger residuals w.r.t. the
training data but it might do a much better job on unseen data.

Calculating the sum of squared residuals for pruned trees
---------------------------------------------------------

We could keep replacing splits with leaf nodes that is the average of larger and larger
number of observations. In the extreme case, we would just split on the average of all
observations. Cost Complexity Pruning helps us choose which split is the best.



Compared pruned trees with alpha
--------------------------------

Step 1: Use all of the data to build trees with different alphas
----------------------------------------------------------------

Step 2: Use cross validation to compare alphas
----------------------------------------------

Step 3: Select the alpha that, on average, gives the best results
-----------------------------------------------------------------

Step 4: Select the original tree that corresponds to that alpha
---------------------------------------------------------------


"""
