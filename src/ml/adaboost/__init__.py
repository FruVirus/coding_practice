"""AdaBoost, Clearly Explained

The three main ideas behind AdaBoost
------------------------------------

In a Random Forest, each time you make a tree, you make a full sized tree. Some trees
might be bigger than others, but there is no predetermined maximum depth.

In contrast, in a Forest of Trees made with AdaBoost, the trees are usually just a node
and two leaves. A tree with just one node and two leaves is called a stump. Thus,
AdaBoost really just makes a Forest of Stumps rather than trees. Stumps are not great
at making accurate classifications. A full sized Decision Tree would take advantage of
all variables (features) in the dataset to make a decision but a Stump can only use one
variable to make a decision. Thus, Stumps are technically "weak learners". However,
that's the way AdaBoost likes it, and it's one of the reasons why they are so commonly
combined.

In a Random Forest, each tree has an equal vote on the final classification. In
contrast, in a Forest of Stumps made with AdaBoost, some stumps get more say in the
final classification than others.

In a Random Forest, each decision tree is made independently of the others. In contrast,
in a Forest of Stumps made with AdaBoost, order is important. The errors that the first
stump makes influence how the second stump is made, and so on.

Review of the three main ideas
------------------------------

To review, the three ideas behind AdaBoost are:

1. AdaBoost combines a lot of "weak learners" to make classifications. The weak learners
are almost always stumps.

2. Some stumps get more say in the classification than others.

3. Each stump is made by taking the previous stump's mistakes into account.

Building a stump with the GINI index
------------------------------------

We create a Forest of Stumps with AdaBoost to predict if a patient has heart disease. We
will make these predictions based on a patient's Chest Pain and Blocked Artery status
and their Weight.

The first thing we do is give each sample a weight that indicates how important it is to
be correctly classified. At the start, all samples get the same weight (i.e., 1 / n,
where n is the number of samples) and that makes the samples all equally important.
However, after we make the first stump, these weights will change in order to guide how
the next stump is created.

Now we need to make the first stump in the forest. This is done by finding the variable,
Chest Pain, Blocked Arteries or Patient Weight, that does the best job classifying the
samples. For the first iteration, we can ignore the sample weights because they are all
the same.

We start by seeing how well Chest Pain classifies the samples. Of the 5 samples with
Chest Pain, 3 were correctly classified as having Heart Disease and 2 were incorrectly
classified. Of the 3 samples without Chest Pain, 2 were correctly classified as not
having Heart Disease and 1 was incorrectly classified. We do the same thing for Blocked
Arteries and Patient Weight.

Determining the Amount of Say for a stump
-----------------------------------------

Now we calculate the Gini Index for the three stumps. Since the Gini index for Patient
Weight is the lowest, it will be the first stump in the forest. Now we need to determine
how much say this stump will have in the final classification.

Remember that some stumps get more say in the final classification than others. We
determine how much say a stump has in the final classification based on how well it
classified the samples.

The Total Error for a stump is the sum of the sample weights associated with the
INCORRECTLY classified samples. Because all of the sample weights add up to 1, the Total
Error will always be between 0, for a perfect stump, and 1, for a horrible stump. We
use the Total Error to determine the Amount of Say this stump has in the final
classification with the following formula:

Amount of Say = 0.5 * log((1 - Total Error) / Total Error)

The Amount of Say curve looks like a sigmoid curve rotated CW by 90 degrees.

When a stump does a good job, and the Total Error is small, then the Amount of Say is a
relatively large, positive value.

When a stump is no better at classification than flipping a coin, then Total Error = 0.5
and the Amount of Say is 0.

And when a stump does a terrible job and the Total Error is close to 1, then the Amount
of Say will be a large negative value. In other words, the negative Amount of Say will
turn classification into the opposite category.

Updating sample weights
-----------------------

Now we need to learn how to modify the weights so that the next stump will take the
errors that the current stump made into account.

Let's go back to the first stump that we made. When we created this stump, all of the
Sample Weights were the same and that meant we did not emphasize the importance of
correctly classifying any particular sample.

However, if a current stump incorrectly classifies a sample, then we will emphasize the
need for the next stump to correctly classify it by increasing its Sample Weight and
decreasing all of the other Sample Weights (so that all Sample Weights still sum to 1).

For the INCORRECTLY classified sample(s), we need to INCREASE the Sample Weight(s). The
new sample weight is:

New Sample Weight = Sample Weight * exp(Amount of Say)

When the Amount of Say is relatively large (i.e., the last stump did a good job
classifying samples), then we will scale the previous Sample Weight with a large number.
This means that the New Sample Weight will be much larger than the old one.

And when the Amount of Say is relatively low (i.e., the last stump did not do a very
good job classifying samples), then the previous Sample Weight is scaled by a relatively
small number. This means that the New Sample Weight will only be a little larger than
the old one.

Now we need to DECREASE the Sample Weights for all of the CORRECTLY classified samples.
The new sample weight is:

New Sample Weight = Sample Weight * exp(-Amount of Say)

When the Amount of Say is relatively large, then we scale the Sample Weight by a value
very close to 0. This will make the New Sample Weight very small.

If the Amount of Say for the last stump is relatively small, then we will scale the
Sample Weight by a value to close 1. This means that the New Sample Weight will be just
a little smaller than the old one.

In summary:

For INCORRECTLY classified samples, we want to INCREASE sample weights for the next
stump. If the current stump was a good classifier, then the new sample weight will be
much larger so that its weighted Gini index will be larger and vice versa. If a sample
weight is larger, then its weighted Gini index will also be larger, which means that a
particular variable will be less likely to be the root of the new stump.

For CORRECTLY classified samples, we want to DECREASE sample weights for the next stump.
If the current stump was a good classifier, then the new sample weight will be much
smaller so that its weighted Gini index will be smaller and vice versa. If a sample
weight is smaller, than its weighted Gini index will also be smaller, which means that a
particular variable will be more likely to be the root of the new stump.

Normalizing the sample weights
------------------------------

After updating all the Sample Weights, we normalize them so that they add up to 1 (i.e.,
divide the new sample weights by the sum of the new sample weights).

Using the normalized weights to make the second stump
-----------------------------------------------------

Now we can use the normalized New Sample Weights to make the second stump in the
forest.

In theory, we could use the Sample Weights to calculate Weighted Gini Indexes to
determine which variable should split the next stump. The Weighted Gini Index would put
more emphasis on correctly classifying the misclassified example(s), since those
examples have the largest Sample Weights.

Alternatively, instead of using a Weighted Gini Index, we can make a new collection of
samples that contains duplicate copies of the samples with the largest Sample Weights.
The new collection of samples should have the same total number of samples as the
original collection.

We give all the new samples equal Sample Weights just like before. However, that doesn't
mean the next stump will not emphasize the need to correctly classify the previously
incorrectly classified samples. Because the incorrectly classified samples are more
likely to appear multiple times in the new collection, they will be treated as a block,
creating a large penalty of being misclassified by the next stump.

Using stumps to make classifications
------------------------------------

Now we need to talk about how a forest of stumps created by AdaBoost makes
classifications.

Imagine we have a group of stumps that classify a patient as Has Heart Disease and
another group of stumps that classify a patient as Does Not Have Heart Disease. We sum
up the Amounts of Say from each group. The group with the largest Amount of Say is the
classification.

Review of the three main ideas behind AdaBoost
----------------------------------------------

To review, the three ideas behind AdaBoost are:

1. AdaBoost combines a lot of "weak learners" to make classifications. The weak learners
are almost always stumps.

2. Some stumps get more say in the classification than others.

3. Each stump is made by taking the previous stump's mistakes into account.
"""
