"""XGBoost

Part 1: Regression
==================

The initial prediction
----------------------

The very first step in fitting XGBoost to the Training Data is to make an initial
prediction. This prediction can be anything, but by default it is 0.5, regardless of
whether you are using XGBoost for Regression or Classification.

The Residuals are the differences between the Observed and Predicted values.

Building an XGBoost Tree for regression
---------------------------------------

Just like Gradient Boost, XGBoost fits a Regression Tree to the residuals.

However, unlike Gradient Boost, which typically uses regular, off-the-shel, Regresssion
Trees, XGBoost uses a unique Regression Tree.

Note: There are many ways to build XGBoost Trees.

Each tree starts out as a single leaf and all of the Residuals go to the leaf.

Calculating Similarity Scores
-----------------------------

Now we calculate a Quality Score, or Similarity Score, for the Residuals.

Similarity Score = (Sum of Residuals) ^ 2 / (Number of Residuals + lambda)

lambda is a Regularization parameter.

Note: Because we do not square the Residuals before we add them together in the
numerator, negative and positive Residuals can cancel each other out.

Now the question is whether or not we can do a better job clustering similar Residuals
if we split them into two groups.

We continuously split observations into two groups based on their average values. And we
calculate new Similarity Scores for the split observations.

When we have calculated Similarity Scores for the root and the two leaf nodes, we see
that when the Residuals in a node are very different, they tend to cancel each other out
and the Similarity Score for the node is relatively small.

In contrast, when the Residuals are similar, or there is just one Residual in a node,
they do not cancel out and the Similarity Score is relatively large.

The minimum number of Residuals in each leaf is determined by calculating something
called Cover. Cover is defined as the denominator of the Similarity Score without the
lambda. For Regression, Cover is the Number of Residuals. By default, the minimum value
for Cover is 1. Thus, by default, when we use XGBoost for Regression, we can have as few
as 1 Residual per leaf. In other words, the default minimum value for Cover has no
effect on how we grow the tree for Regression.

Calculating Gain to evaluate different thresholds
-------------------------------------------------

Now we need to quantify how much better the leaves cluster similar Residuals than the
root.

We do this by calculating the Gain of splitting the Residuals into two groups.

Gain = Sum of Leaf Similarity Scores - Parent Similarity Score

Once we have calculated the Gain for a certain threshold, we can compare it to the Gains
calculate for other thresholds. To do this, we select another threshold (i.e., another
value of the variable we are using) and build a simple tree that divides the
observations using the new threshold.

Higher Gains implies that a given tree is better at splitting the Residuals into
clusters of similar values.

We use the threshold that gave us the largest Gain as the first branch in the XGBoost
tree. We then keep splitting the leaves of the tree and calculating the split that gives
us the highest Gain.

Pruning an XGBoost tree
-----------------------

Now we need to Prune the XGBoost tree. We Prune an XGBoost Tree based on its Gain
values.

We start by picking a number, gamma, referred to as the Tree Complexity Parameter. We
then calculate the difference between the Gain associated with the lowest branch in the
tree and the value for gamma. If the difference is negative, we will remove the branch;
otherwise, we keep the branch.

Note: We do not remove parent branches if the leaf branches are not removed.

Values for lambda > 0 reduce the sensitivity of the tree to individual observations by
pruning and combining them with other observations.

Building an XGBoost Tree with regularization
--------------------------------------------

Remember, lambda is a Regularization Parameter, which means that it is intended to
reduce the prediction's sensitivity to individual observations.

When lambda > 0, the Similarity Scores are smaller and the amount of decrease is
inversely proportional to the Number of Residuals in the node. In other words, leaves
with fewer number of Residuals experience the largest decrease in Similarity Scores.

When lambda > 0, the Gains for each node also decreases. This means that it is easier to
prune leaves when lambda > 0 since the values for Gain are smaller.

Note: setting gamma = 0 does not turn off pruning since Gain can be negative by itself.

Calculating output values for an XGBoost Tree
---------------------------------------------

The Output Value equation is:

Output Value = Sum of Residuals / (Number of Residuals + lambda)

When lambda > 0, it will reduce the amount that a single observation adds to the overall
prediction. Thus, lambda, the Regularization Parameter, will reduce the prediction's
sensitivity to an individual observation.

Making predictions with XGBoost
-------------------------------

After we build our first XGBoost tree, we can make new Predictions.

Just like Gradient Boost, XGBoost makes new predictions by starting with the initial
Prediction (e.g., 0.5) and adding the output of the XGBoost Tree scaled by a Learning
Rate, eta (e.g., 0.3).

Now we build another XGBoost tree based on the latest Residuals and make new predictions
that give us even smaller Residuals, and so on. We keep building trees until the
Residuals are super small, or we have reached the maximum number of trees.

Summary of concepts and main ideas
----------------------------------

In summary, when building XGBoost Trees for Regression:

1. We calculate Similarity Scores

2. We calculate Gain to determine how to split the data

3. And we prune the tree by calculating the differences between Gain values and
user-defined Tree Complexity Parameter, gamma. If gamma is negative, we prune the node;
otherwise, we do not prune.

4. Then we calculate the Output Values for the remaining leaves.

5. Lastly, lambda is a Regularization Parameter and when lambda > 0, it results in more
pruning, by shrinking the Similarity Scores, and it results in smaller Output Values for
the leaves.

Part 2: Classification
======================

The very first step in fitting XGBoost to the Training Data is to make an initial
prediction. This prediction can be anything, but by default it is 0.5 regardless of
whether you are using XGBoost for Regression or Classification.

The Residuals, the differences between the Observed and Predicted values, show us how
good the initial prediction is.

Just like we did for Regression, we fit an XGBoost Tree to the Residuals.

However, since we are using XGBoost for Classification, we have a different formula for
the Similarity Scores:

Similarity Score = (Sum of Residuals) ^ 2 /
                   (Sum of (Previous Probability * (1 - Previous Probability)) + lambda)

Just like for Regression, each tree starts out as a single leaf and all of the Residuals
go to the leaf.

Now we need to decide if we can do a better job clustering similar Residuals if we split
them into two groups.

We continuously split observations into two groups based on their average values. And we
calculate new Similarity Scores for the split observations.

If we are building the first tree, the previous probability refers to the prediction
from the initial leaf (i.e., 0.5).

After we have calculated the Similarity Scores for all the leaf nodes, we calculate the
Gain just like we did for Regression. And we pick the optimal threshold as the one that
maximizes the Gain.

For Classification, Cover is the
Sum of (Previous Probability * (1 - Previous Probability)). Thus, Cover depends on the
previously predicted probability of each Residual in a leaf.

We prune the tree by calculating the difference between the Gain associated with the
lowest branch and a number we pick for gamma.

For Classification, the Output Value for a leaf is:

Output Value = (Sum of Residuals) /
               (Sum of (Previous Probability * (1 - Previous Probability)) + lambda)

After building the first tree, we can make new Predictions. Just like other boosting
methods, XGBoost for Classification makes new predictions by starting with the initial
prediction. However, we need to convert this initial probability to a log(odds) value
using the formula:

log(p / (1 - p)) = log(odds)

In other words, Output = log(odds).

Now we add the log(odds) of the initial prediction to the output of the Tree, scaled by
a Learning Rate, eta. To convert a log(odds) into a probability, we plug the log(odds)
into the Logistic Function.

We keep building trees until the Residuals are super small, or we have reached the
maximum number of trees.

In summary, when building XGBoost Trees for Classification:

1. We calculate Similarity Scores

2. We calculate Gain to determine how to split the data

3. And we prune the tree by calculating the difference between Gain values and a
user-defined Tree Complexity Parameter, gamma. If gamma is negative, we prune the node;
otherwise, we do not prune.

4. Then we calculate the Output Values for the leaves.

5. Lastly, lambda is a Regularization Parameter and when lambda > 0, it results in more
pruning, by shrinking the Similarity Scores and smaller Output Values for the leaves.

Part 3: Mathematical Details
============================

See notes.
"""
