"""Best practices for the real world

13.1 Getting the most out of your models
========================================

13.1.1 Hyperparameter optimization
----------------------------------

You need to search the architecture space and find the best-performing architectures
empirically.

The process of optimzing hyperparameters typicalls looks like:

1. Choose a set of hyperparameters (automatically).
2. Build the corresponding model.
3. Fit it to your training data, and measure performance on the validation data.
4. Choose the next set of hyperparameters to try (automatically).
5. Repeat.
6. Eventually, measure performance on your test data.

Updating hyperparameters presents unique challenges:

- The hyperparameter space is typically made up of discrete decisions and thus isn't
continuous or differentiable.
- Computing the feedback signal of this optimization process can be extremely expensive.
- The feedback signal may be noisy: If a training runs performs better, is that because
of a better model configuration or because we got lucky with the initial weight values?

The Art Of Crafting The Right Search Space

Doing hyperparameter tuning is not a replacement for being familiar with model
architecture best practices.

The good news is that by leveraging hyperparameter tuning, the configuration decisions
you have to make graduate from micro-decisions to higher-level architecture decisions.
And while micro-decisions are specific to a certain model and a certain dataset,
higher-level decisions genearlize better across different tasks and datasets.

13.1.2 Model ensembling
-----------------------

Ensembling consists of pooling together the predictions of a set of different models to
produce better predictions.

Ensembling relies on the assumption that different well-performing models trained
independently are likely to be good for different reasons: each model looks at slightly
different aspects of the data to make its predictions, getting part of the "truth" but
not all of it.

The easiest way to pool the predictions of a set of classifiers is to average their
predictions at inference time. However, this will only work if the classifiers are more
or less equally good. If one of them is significantly worse than the others, the final
predictions may not be as good as the best classifier of the group.

A smarter way to ensemble classifiers is to do a weighted average, where the weights are
learned on the validation data---typically, the better classifiers are given a higher
weight, and the worse classifiers are given a lower weight.

The key to making ensembling work is the diversity of the set of classifiers. In machine
learning terms, if all of your models are biased in the same way, your ensemble will
retain this same bias. If your models are biased in different ways, the biases will
cancel each other out, and the ensemble will be more robust and more accurate.

For this reason, you should ensemble models that are as good as possible while being as
different as possible. This typically means using very different architectures or even
different brands of machine learning approaches. One thing that is largely not worth
doing is ensembling the same network trained several times independently, from different
random initializations. If the only difference between your models is their random
initialization and the order in which they were exposed to the training data, then your
ensemble will be low-diversity and will provide only a tiny improvement over any single
model.

The point of ensembling isn't how good your best model is; it's about the diversity of
your set of candidate models.

13.2 Scaling-up model training
==============================

13.2.1 Speeding up training on GPU with mixed precision
-------------------------------------------------------

Understanding Floating-Point Precision

Single precision is enough to run the forward and backwards pass of a model without
losing any information---particularly when it comes to small gradient updates. However,
half-precision wouldn't work for gradient descent.

Mixed precision uses float-16 computations in places where precision isn't an issue and
float-32 values in other places to maintain numerical stability.

Typically, most of the forward pass of the model will be done in float-16 (with the
exception of numerically unstable operations like softmax), while the weights of the
model will be stored and updated in float-32.
"""
