"""Gradient Boost

Part 1: Regression Main Ideas
=============================

Gradient Boost compared to AdaBoost
-----------------------------------

If we want to use measurements to Predict Weight, then AdaBoost starts by building a
very short tree, called a Stump, from the Training Data and the amount of say that the
stump has on the final output is based on how well it compensated for those previous
errors. Then AdaBoost builds the next stump based on errors that the previous stump
made. If a stump does a poor job compensating for the previous stump's errors, then its
amount of say is reduced and vice versa. Then AdaBoost builds another stump based on the
errors made by the previous stump and so on until is has made the number of stumps you
asked for, or it has a perfect fit.

In contrast, Gradient Boost starts by making a single leaf, instead of a tree or stump.
This leaf represents an initial guess for the Weights of all the samples. When trying to
Predict a continuous value like Weight, the first guess is the average value. Then
Gradient Boost builds a tree. Like AdaBoost, this tree is based on the errors made by
the previous tree. But unlike AdaBoost, this tree is usually larger than a stump. That
said, Gradient Boost still restricts the size of the tree. In practice, the maximum
number of leaves is usually between 8 and 32.

Thus, like AdaBoost, Gradient Boost builds fixed sized trees based on the previous
tree's errors, but unlike AdaBoost, each tree can be larger than a stump. Also, like
AdaBoost, Gradient Boost scales the trees. However, Gradient Boost scales all trees by
the same amount. Gradient Boost contains to build trees in this fashion until it has
made the number of trees you asked for, or additional trees fail to improve the fit.

Building the first tree to predict weight
-----------------------------------------

Let's see how the most common Gradient Boost configuration would use a Training Data to
Predict Weight.

The first thing we do is calculate the average Weight. This is the first attempt at
predicting everyone's weight.

The next thing we do is build a tree based on the errors from the first tree. The errors
that the previous tree made are the differences between the Observed Weights and the
Predicted Weight. This difference is called a Pseudo Residual. The term Pseudo Residual
is based on Linear Regression---the "Pseudo" part is a reminder that we are doing
Gradient Boost and not Linear Regression.

We build the tree using all the variables (features) from the training data to predict
the (pseudo) residuals. Note that we don't use the variables to predict the Weights
(explained later). By restricting the total number of leaves in a given (decision) tree,
we get fewer leaves than residuals. As a result, leaves can contain multiple residual
values and we simply take the average of the residual values as the value for a given
leaf.

Now we can combine the original leaf (for the first iteration, the original leaf value
is just the average of all the Weights) with the new tree to make a new Prediction of an
individual's Weight from the Training Data.

We start with the initial prediction (i.e., the average weight), then we run the data
down the tree to get the leaf value and add the leaf value to the initial prediction.

New Prediction = Initial Prediction + Leaf Value

Typically, the model will fit the Training Data too well. In other words, we have low
Bias, but probably very high Variance.

Gradient Boost deals with this problem by using a Learning Rate to scale the
contribution from the new tree.

New Prediction = Initial Prediction + Learning Rate * Leaf Value.

The Learning Rate is a value between 0 and 1. Scaling the tree by the Learning Rate
results in a small step in the right direction. Empirical evidence shows that taking
lots of small steps in the right direction results in better Predictions with a Testing
Dataset, i.e., lower Variance.

Building the second tree to predict weight
------------------------------------------

So let's build another tree so that we can take another small step in the right
direction.

Just like before, we calculate the Pseudo Residuals, the difference between the Observed
Weights and our LATEST predictions.

If the new Residuals are smaller than before, then we've taken a small step in the right
direction.

In practice, each tree can be different from previous trees. Just like before, since
multiple samples can end up in each leaf, we just replace the Residuals with their
averages.

Now we combine the new Tree with the previous Tree and the initial Leaf. We scale ALL of
the Trees by the SAME Learning Rate and add everything together.

Now we're ready to make a new Prediction from the Training Data. Just like before, we
start with the initial Prediction, then add the scaled amount from the first Tree and
the scaled amount from the second Tree.

Each time we add a tree to the Prediction, the Residuals get smaller.

Building additional trees to predict weight
-------------------------------------------

We keep making trees until we reach the maximum specified, or adding additional trees
does not significantly reduce the size of the Residuals.

Prediction with Gradient Boost
------------------------------

When we get new measurements, we can Predict Weight by starting with the initial
Prediction and adding the scaled values from all the trees.

Summary of concepts and main ideas
---------------------------------

In summary, when Gradient Boost is used for Regression:

1. We start with a leaf that is the average value of the variable we want to Predict.

2. Then we add a tree based on the Residuals, the difference between the Observed values
and the Predicted values and we scale the tree's contribution to the final Prediction
with a Learning Rate.

3. Then we add another tree based on the new Residuals.

4. And we keep adding trees based on the errors made by the previous tree.

Part 2: Regression Details
==========================

See notes.

Part 3: Classification
======================


"""
