"""
Random Forests Part 1 - Building, Using and Evaluating
======================================================

Motivation for using Random Forests
-----------------------------------

Decision trees are highly sensitive to the training data. Different training data
produces different trees, which results in high variance in the predictions (i.e.,
decision tree models might fail to generalize). In other words, they work great with the
data used to create them, but they are not flexible when it comes to classifying new
examples.

A random forest is a collection of multiple, random decision trees and is less sensitive
to the training data. Random Forests combine the simplicity of decision trees with
flexibility, resulting in a vast improvement in accuracy on unseen data.

In practice, we usually build ~100s of decision trees. Each decision tree randomly
samples from the same training dataset with replacement so that individual data points
can appear multiple times in a given decision tree. This process is known as
bootstrapping.

Next, we train a decision tree on each of the bootstrapped datasets, independently.
However, during this training process, we do not use all the features for each tree.
Instead, we use a random subset of features for each tree. Each tree in this forest
trained in this fashion will be different from one another.

To make a prediction with a new data point, we pass the features of the new data point
through each tree, one by one, and note the prediction from each tree. In the end, we
combine (aggregate) the predictions to make the final prediction (e.g., by majority
voting for classification or average for regression).

Thus, the random forest algorithm consists of bootstrapping and aggregation---commonly
referred to as bagging.

The random forest algorithm uses randomness to create the bootstrapped datasets and to
select the feature subsets. Bootstrapping ensures that we are not using the same data
for every tree. It helps the model to be less sensitive to the original training data.
The random feature selection reduces the correlation between the different decision
trees. If you use all the features, then most of the trees will have the same decision
nodes and they will make similar predictions.

Step 1: Create a bootstrapped dataset
-------------------------------------

Step 1 is to create a "bootstrapped" dataset. To create a bootstrapped dataset that is
the same size as the original, we just randomly select samples from the original
dataset. The important detail is that we are allowed to pick the same sample more than
once.

Step 2: Create a decision tree using a random subset of variables at each step
------------------------------------------------------------------------------

Step 2 is to create a decision tree using the bootstrapped dataset, but only use a
random subset of variables (i.e., columns in the Design Matrix) at each step. In other
words, instead of consider all N variables when determining how to split a node, we only
consider a random subset of the N variables.

For each node, we consider a random subset of the N variables (but we consider the same
number of random subsets). However, the same feature can be reused multiple times. In
other words, every time we select a subset of features to choose from, we choose from
the full list of features, even if we have already used some of those features.

Step 3: Repeat Steps 1 and 2 a bunch of times
---------------------------------------------

Now we go back to Step 1 and repeat. We make a new bootstrapped dataset and build a tree
considering a subset of variables at each step. Ideally, you'd do this ~100s of times.

Using a bootstrapped dataset and only considering a subset of the variables at each step
results in a wide variety of trees. The variety is what makes random forests more
effective than individual decision trees.

Classify a new sample with a Random Forest
------------------------------------------

For a new sample, we run the sample through all the trees that we made and the final
prediction is the majority prediction from all the trees.

Definition of Bagging
---------------------

Bootstrapping the data plus using the aggregate of all models to make a decision is
called "Bagging."

Evaluating a Random Forest
--------------------------

When we create a Bootstrapped dataset, some samples will not be in the Bootstrapped
dataset. Typically, about 1 / 3 of the original data does not end up in the bootstrapped
dataset. This is called the "Out-Of-Bag" dataset.

We can use the Out-Of-Bag dataset to evaluate each decision tree that excluded the
Out-Of-Bag dataset. The majority vote from the random forest is the label for the
Out-Of-Bag sample.

Ultimately, we can measure how accurate our random forest is by the proportion of
Out-Of-Bag samples that were correctly classified by the Random Forest.

The proportion of Out-Of-Bag samples that were incorrectly classified is the
"Out-Of-Bag Error."

Optimizing the Random Forest
----------------------------

Now we can compare the Out-Of-Bad error for a random forest built using only 2 variables
per step to a random forest built using 3 variables per step, and so on. We can test a
bunch of different settings and choose the most accurate random forest as determined by
the Out-Of-Bad Error.

Typically, we start by using the square root of the total number of features and then
try a few settings above or below that value.

Random Forests Part 2: Missing Data and Sample Clustering
=========================================================

Missing Data
------------

Random Forests consider 2 types of missing data:

1. Missing data in the original dataset used to create the random forest.

The general idea for dealing with missing data in the training set is to make an initial
guess that could be bad, then gradually refine the guess until it is (hopefully) a good
guess.

We can look at the correlation between the prediction and the column with the missing
data and choose a value for the missing data that correlates with the other values in
the column. For binary data, we can use the majority value from the other data in the
column. For numeric data, we can use the mean or median value from the other data in the
column.

Now we want to refine these guesses. We do this by first determining which samples are
similar to the one with missing data.

Step 1 is to build a random forest using the data and the data with the initial guess
for the missing values.

Step 2 is to run all of the data through all of the trees.

If the sample with the missing features end up with other samples, then the missing
feature sample is considered as "similar" to those other features. We keep track of
similar samples using a Proximity Matrix.

A Proximity Matrix is an N x N matrix of counts where N is the total number of samples,
where the number of counts corresponds to the total number of times that two samples
were deemed as similar after running the data through all of the trees in the random
forest. After we run the data through the random forest, we divide each proximity value
by the total number of trees.

Next, we use the proximity values for the sample with missing features to make better
guesses for the features.

For binary features:

The weighted frequency for "Yes":

Yes = (# of times "Yes" occurs for the feature / Total number of samples) *
     sum(proximity values for "Yes" samples)

The weighted frequency for "Yes":

No = (# of times "No" occurs for the feature / Total number of samples) *
     sum(proximity values for "No" samples)

If "No" has a higher weighted frequency, then we will assign "No" as the missing feature
for the sample.

For numeric features:

We use proximity values to calculate a weighted average of the missing numeric feature.

Weighted average = Sum(Numeric value for Sample *
                   (Proximity Value for Sample / sum(Proximity Values)))

After we have revised our guesses, we do the whole thing over again. We build a random
forest, run the data through all the trees, recalculate the proximity matrix, and
recalculate the missing values. We do this until the missing feature values converge.

2. Missing data in the new sample that you want to categorize.

Imagine that we had already built a Random Forest with existing data and wanted to
classify a new sample with missing features. We need to make a guess about the value of
the missing feature so that we can run the sample through all the trees in the forest.

Step 1 is to create two copies of the sample, each with a different prediction label
(e.g., Yes and No).

Step 2 is to use the iterative method from above to make a good guess about the missing
values for both copies of the sample.

Step 3 is to run the two samples down the random forest and we see which of the two
copies is correctly labeled by the random forest the most times. The copy that has the
majority prediction wins.

Sample Clustering
-----------------

A proximity value of 1 (after normalization) means that two samples are as close as can
be. 1 - proximity value is then a measure of distance and 1 - proximity matrix is a
distance matrix that we can plot as a heatmap or MDS plot.

The means that no matter what the data are, if we can use it to make a tree, we can draw
a heatmap or MDS plot to show how the samples are related to each other.
"""
