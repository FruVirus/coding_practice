"""
Decision trees are highly sensitive to the training data. Different training data
produces different trees, which results in high variance in the predictions (i.e.,
decision tree models might fail to generalize).

A random forest is a collection of multiple, random decision trees and is less sensitive
to the training data.

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

Best practice is to use either sqrt() or log() of the total number of features for the
number of features in the subsets.
"""
