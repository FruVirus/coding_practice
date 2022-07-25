"""Fundamentals of machine learning

5.1 Generalization: The goal of machine learning
================================================

The fundamental issue is machine learning is the tension between optimization and
generalization. Optimization refers to the process of adjusting a model to get the best
performance possible on the training data (the learning in machine learning), whereas
generalization refers to how well the trained model performs on data it has never seen
before. The goal of the game is to get good generalization, of course, but you don't
control generalization; you can only fit the model to its training data. If you do that
too well, overfitting kicks in and generalization suffers.

5.1.1 Underfitting and overfitting
----------------------------------

At the beginning of training, optimization and generalization are correlated: the lower
the loss on training data, the lower the loss on test data. While this is happening,
your model is said to be underfit: there is still progress to be made; the network
hasn't yet modeled all relevant patterns in the training data. But after a certain
number of iterations on the training data, generalization stops improving, validation
metrics stall and then begin to degrade: the model is starting to overfit. That is, it's
beginning to learn patterns that are specific to the training data but that are
misleading or irrelevant when it comes to new data.

Overfitting is particularly likely to occur when your data is noisy, if it involves
uncertainty, or if it includes rare features.

Ambiguous Features

Not all data noise comes from inaccuracies---even perfectly clean data and neatly
labeled data can be noisy when the problem involves uncertainty and ambiguity.

Rare Features and Spurious Correlations

Machine learning models trained on datasets that include rare feature values are highly
susceptible to overfitting.

Importantly, a feature value doesn't need to occur only a couple of times to lead to
spurious correlations.

Noisy features inevitably lead to overfitting. As such, in cases where you aren't sure
whether the features you have are informative or distracting, it's common to do
feature selection before training. The typical way to do feature selection is to compute
some usefulness score for each feature available---a measure of how informative the
feature is with respect to the task, such as the mutual information between the feature
and the labels---and only keep features that are above some threshold.

5.1.2 The nature of generalization in deep learning

The nature of generalization in deep learning has rather little to do with deep learning
models themselves, and much to do with the structure of information in the real world.

The Manifold Hypothesis

The subspace of points in a real-world image isn't just a set of points sprinkled at
random in the parent space: it is highly structured.

First, the subspace of valid handwritten digits is continuous: if you take a sample and
modify it a little, it will still be recognizable as the same handwritten digit.
Further, all samples in the valid subspace are connected by smooth paths that run
through the subspace.

The handwritten digits form a manifold within the space of possible 28 x 28 uint8
arrays. A "manifold" is a lower-dimensional subspace of some parent space that is
locally similar to a linear (Euclidean) space.

More generally, the manifold hypothesis posits that all natural data lies on a
low-dimensional manifold within the high-dimensional space where it is encoded.

The manifold hypothesis implies that:

- Machine learning models only have to fit relatively simple, low-dimensional, highly
structured subspaces within their potential input space (latent manifolds).

- Within one of these manifolds, it's always possible to interpolate between two inputs,
that is to say, morph one into another via a continuous path along which all points fall
on the manifold.

The ability to interpolate between samples is the key to understanding generalization in
deep learning.

Interpolation As A Source Of Generalization

If you work with data points that can be interpolated, you can start making sense of
points you[ve never seen before by relating them to other points that lie close on the
manifold. In other words, you can make sense of the totality of the space using only a
sample of the space. YOu can use interpolation to fill in the blanks.

While deep learning achieves generalization via interpolation on a learned approximation
of the data manifold, it would be a mistake to assume that interpolation is all there is
to generalization. Interpolation can only help you make sense of things that are very
close to what you've seen before: it enables local generalization.

Humans are capable of extreme generalization, which is enabled by cognitive mechanisms
other than interpolation: abstraction, symbolic models of the world, reasoning, logic,
common sense, innate priors about the world---what we generally call reason, as opposed
to intuition and pattern recognition.

Why Deep Learning Works

By its very nature, deep learning is about taking a big, complex curve---a manifold---
and incrementally adjusting its parameters until it fits some training data points.

Your data forms a highly structured, low-dimensional manifold within the input space---
that's the manifold hypothesis. And because fitting your model curve to this data
happens gradually and smoothly over time as gradient descent progresses, there will be
an intermediate point during training at which the model roughly approximates the
natural manifold of the data.

Moving along the curve learned by the model at that point will come close to moving
along the actual latent manifold of the data---as such, the model will be capable of
making sense of never-before-seen inputs via interpolation between training inputs.

Besides the trivial fact that they have sufficient representational power, there are a
few properties of deep learning models that make them particularly well-suited to
learning latent manifolds:

- Deep learning models implement a smooth, continuous mapping from their inputs to their
outputs. It has to be smooth and continuous because it must be differentiable. This
smoothness helps approximate latent manifolds, which follow the same properties.

- Deep learning models tend to be structured in a way that mirrors the "shape" of the
information in their training dataa (via architecture priors). More generally, deep
neural networks structure their learned representations in a hierarchical and modular
way, which echos the way natural data is organized.

Training Data Is Paramount

The power to generalize is more a consequence of the natural structure of your data than
a consequence of any property of your model. Data curation and feature engineering are
essential to generalization.

Further, because deep learning is curve fitting, for a model to perform well it needs to
be trained on a dense sampling of its input space. A "dense sampling" in this context
means that the training data should densely cover the entirety of the input data
manifold. This is especially true near decision boundaries. With a sufficiently dense
sampling, it becomes possible to make sense of new inputs by interpolating between past
training inputs without having to use reasoning.

5.2 Evaluating machine learning models
======================================

5.2.1 Training, validation, and test sets
-----------------------------------------

Simple Holdout Validation

This is the simplest evaluation protocol, and it suffers from one flaw: if little data
is available, then your validation and test sets may contain too few samples to be
statistically representative of the data at hand. This is easy to recognize: if
different random shuffling rounds of the data before splitting end up yielding very
different measures of model performance, then you're having this issue.

K-Fold Validation

With this approach, you split your data into K partitions of equal size. For each
partition i, train a model on the remaining K - 1 partitions, and evaluate it on
partition i. Your final score is then the averages of the K scores obtained. This
method is helpful when the performance of your model shows significant variance based on
your train-test split.

Iterated K-Fold Validation With Shuffling

This one is for situations in which you have relatively little data available and you
need to evaluate your model as precisely as possible. It consists of applying K-fold
validation multiple times, shuffling the data every time before splitting it K ways. The
final score is the average of the scores obtained at each run of K-fold validation.

5.2.3 Things to keep in mind about model evaluation
---------------------------------------------------

- Data representativeness---You want both your training and test sets to be
representative of the data at hand. That is, randomly shuffle your data before splitting
it into training and test sets.

- The arrow of time---If you're trying to predict the future given the past, you should
not randomly shuffle your data before splitting it, because doing so will create a
temporal leak: your model will effectively be trained on data from the future.

- Redundancy in your data---Make sure data points in your data do not appear more than
once.

5.3 Improving model fit
=======================

To achieve the perfect fit, you must first overfit.

There are three common problems you'll encounter at this stage:

- Training doesn't get started: your training loss doesn't go down over time.

- Training gets started just fine, but your model doesn't meaningfully generalize: you
can't beat the common-sense baseline you set.

- Training and validation loss both go down over time, and you can beat your baseline,
but you don't seem to be able to overfit, which indicates you're still underfitting.

5.3.1 Tuning key gradient descent parameters
--------------------------------------------

If your training gets stuck, this is always something you can overcome: remember that
you can fit a model to random data.

When this happens, it's always a problem with the configuration of the gradient descent
process: your choice of optimizer, the distribution of initial values in the weights of
your model, your learning rate, or your batch size.

5.3.2 Leveraging better architecture priors
-------------------------------------------

Your model fits, but for some reason your validation metrics aren't improving at all.

It indicates that something is fundamentally wrong with your approach.

First, it may be that the input data you're using simply doesn't contain sufficient
information to predict your targets: the problem as formulated is not solvable.

It may also be that the kind of model you're using is not suited for the problem at
hand. Using a model that makes the right assumptions about the problem is essential to
achieve generalization: you should leverage the right architecture priors.

5.3.3 Increasing model capacity
-------------------------------

If you can't overfit, it's likely a problem with the representational power of your
model: you're going to need a bigger model, one with more capacity.

5.4 Improving generalization
============================

5.4.1 Dataset curation
----------------------

Get more training data, or better training data.

How does one decide whether to gather more data?

First, determine whether the performance on the training set is acceptable. If it is
not, the learning algorithm is not using the training data that is already available, so
there is no reason to gather more data. Instead, try increasing model capacity. Also,
try improving the learning algorithm (e.g., by tuning hyperparameters). If large models
and tuning hyperparameters do not work well, then the problem might be the quality of
the training data.

If the performance on the training set is acceptable, the measure the performance on a
test set. If the performance on the test set is also acceptable, then there is nothing
left to be done.

If the test set performance is much worse than training set performance, then gathering
more data is one of the most effective solutions.

If gather much more data is not feasible, the only other way to improve generalization
error is to improve the learning algorithm itself.

5.4.2 Feature engineering
-------------------------

Feature engineering is the process of using your own knowledge about the data and about
the machine learning algorithm at hand to make the algorithm work better by applying
hardcoded transformations to the data before it goes into the model. The data needs to
be presented to the model in a way that will make the model's job easier.

Make the latent manifold smoother, simpler, better organized.

Modern deep learning still can benefit from feature engineering:

- Good features still allow you to solve problems more elegantly while using fewer
resources.

- Good features let you solve a problem with far less data.

5.4.3 Using early stopping
--------------------------

In deep learning, we always use models that are vastly overparameterized: they have way
more degrees of freedom than the minimum necessary to fit to the latent manifold of the
data. This overparameterization is not an issue, because you never fully fit a deep
learning model. Such a fit wouldn't generalize at all. You will always interrupt
training long before you've reached the minimum possible training loss.

5.4.4 Regularizing your model
-----------------------------

Regularization techniques are a set of best practices that actively impede the model's
ability to fit perfectly to the training data, with the goal of making the model perform
better during validation. This is called "regularizing" the model, because it tends to
make the model simpler, more "regular", its curve smoother, more "generic"; thus it is
less specific to the training set and better able to generalize by more closely
approximating the latent manifold of the data.

Reducing The Network's Size

The simplest way to mitigate overfitting is to reduce the size of the model.

You'll know if your model is too large if it starts overfitting right away (i.e.,
validation loss increases right away) and if its validation loss curve looks choppy with
high variance.

The more capacity the model has, the more quickly it can model the training data
(resulting in a low training loss), but the more susceptible it is to overfitting
(resulting in a large difference between the training and validation loss).

Adding Weight Regularization

A common way to mitigate overfitting is to put constraints on the complexity of a model
by forcing its weights to take only small values, which makes the distribution of
weights more regular. This is called weight regularization, and it's done by adding to
the loss function of the model a cost associated with having lage weights. This cost
comes in two flavors:

- L1 regularization---The cost added is proportional to the absolute value of the weight
coefficients (the L1 norm of the weights).

- L2 regularization---The cost added is proportional to the square of the value of the
weight coefficients (the L2 norm of the weights).

Note that because this penalty is only added at training time, the training loss for the
model will be much higher than the test loss.

Note that weight regularization is more typically used for smaller deep learning models.
Large deep learning models tend to be so overparameterized that imposing constraints on
weight values hasn't much impact on model capacity and generalization. In these cases,
a different regularization technique is preferred: dropout.

Adding Dropout

Dropout, applied to a layer, consists of randomly dropping out (setting to zero) a
number of output features of the layer during training. The dropout rate is the fraction
of the features that are zeroed out; it's usually set between 0.2 and 0.5. At test time,
no units are dropped out; instead, the layer's output values are multiplied by the
dropout rate, to balance for the fact that more units are active than at training time.

Note that this process can be implemented all at once during training time and leaving
the outputs unchanged at test time. In effect, during training, we add dropout to a
layer and then divide the layer's output by the dropout rate.

The core idea behind dropout is that introducing noise (i.e., dropping features) in the
output values of a layer can break up happenstance patterns that aren't significant,
which the model will start memorizing if no noise is present.
"""
