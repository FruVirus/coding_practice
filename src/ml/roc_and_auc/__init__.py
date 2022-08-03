"""
ROC and AUC
===========

Classifying samples with logistic regression
--------------------------------------------

When we do logistic regression, we have to set a threshold to classify a sample as
either positive or negative. Depending on the threshold, we get different values for our
confusion matrix.

Creating confusion matrices for different thresholds
----------------------------------------------------

A confusion matrix has actual labels for its columns and predicted labels for its rows.

The threshold for classification can be set to anything between 0 and 1. How do we test
which threshold is the best?

For starters, we don't need to test every single option. Some thresholds result in the
exact same confusion matrix. Even if we did create a confusion matrix for every single
distinct threshold, it would result in a lot of confusion matrices.

ROC is an alternative to tons of confusion matrices
---------------------------------------------------

Instead of being overwhelmed with confusion matrices, Receiver Operator Characteristic
(ROC) graphs provide a simple way to summarize all of the information.

The ROC graph summarizes all of the confusion matrices that each threshold produced.

ROC graphs plot Sensitivity (True Positive Rate) vs. (1 - Specificity)
(False Positive Rate).

Sensitivity tells you what proportion of positive samples were correctly classified.

The False Positive Rate is the proportion of negative samples that were incorrectly
classified.

A point at (1, 1) means that we classified all samples as positive, even the ones that
are actually negative. This corresponds to a threshold of 0.

The diagonal line from (0, 0) to (1, 1) shows where the number of correctly classified
positive samples is the same as the number of correctly classified negative samples.

A point at (0, 0) means that we classified all samples as negative, even the ones that
are actually positive. This corresponds to a threshold of 1.

Connecting all the points gives us the ROC graph.

AUC to compare different models
-------------------------------

The Area Under the Curve (AUC) is the area under the ROC graph. The AUC makes it easy to
compare one ROC curve to another. Higher AUC suggests a better model.

False Positive Rate vs Precision
--------------------------------

We can also replace FPR with Precision.

Precision is the proportion of positive results that were correctly classified.

If there were lots of negative samples, then Precision might be more useful that FPR.
This is because Precision does not include True Negatives in its calculation, and is not
affected by the imbalance.

Summary of concepts
-------------------

1. ROC curves make it easy to identify the best threshold for making a decision.

2. The AUC can help you decide which categorization method is better overall.
"""
