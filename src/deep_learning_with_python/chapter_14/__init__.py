"""Conclusions

14.1 Key concepts in review
===========================

14.1.5 The universal machine learning workflow
----------------------------------------------

1. Define the problem.
2. Identify a way to reliably measure success on your goal.
3. Prepare the validation process that you'll use to evaluate your models.
4. Vectorize the data by turning it into vectors and preprocessing it in a way that
makes it more easily approachable by a neural network.
5. Develop a first model that beats a trivial common-sense baseline, thus demonstrating
that machine learning can work on your problem.
6. Gradually refine your model architecture by tuning hyperparameters and adding
regularization. Remember that you should get your data to overfit to the training data
and only then begin to add regularization or downsize your model.
7. Deploy your model in production. Keep monitoring its performance on real-world data,
and use your findings to refine the next iteration of the model.

14.1.6 Key network architectures
--------------------------------

A network architecture encodes assumptions about the structure of the data: a hypothesis
space within which the search for a good model will proceed. Whether a given
architecture will work on a given problem depends entirely on the match between the
structure of the data and the assumptions of the network architecture.

- Vector data---Densely connected models.
- Image data---2D convnets.
- Sequence data---RNNs for timeseries or Transformers for discrete sequences. 1D
convnets can also be used for translation-invariant, continuous sequence data.
- Video data---Either 3D convnets, or a combination of a frame-level 2D convnet for
feature extraction followed by a sequence-processing model.
- Volumetric data---3D convnets.

Densely Connected Networks

A densely connected network is a stack of Dense layers meant to process vector data.
Such networks assume no specific structure in the input features: they're called densely
connected because the units of a Dense layer are connected to every other unit. The
layer attempts to map relationships between any two input features; this is unlike 2D
convolution layer, for instance, which only looks at local relationships.

Densely connected networks are most commonly used for categorical data. They're also
used as the final classification or regression stage of most networks.

To perform binary classification, end your stack of layers with a Dense layer with a
single unit and a sigmoid activation, and use binary cross entropy as the loss. Your
target should be either 0 or 1.

To perform single-label classification (i.e., multi-class classification), end your
stack of layers with a Dense layer with a number of units equal to the number of
classes, and a softmax activation, and use categorical cross entropy as the loss.

To perform multi-label classification, end your stack of layers with a Dense layer with
a number of units equal to the number of classes, and a sigmoid activation, and use
binary cross entropy as the loss.

To perform regression toward a vector of continuous values, end your stack of layers
with a Dense layer with a number of units equal to the number of values you're trying to
predict (often a single one), and no activation, and use MSE loss.

Convnets

Convolution layers look at spatially local patterns by applying the same geometric
transformation to different spatial locations in an input tensor. This results in
representations that are translation invariant, making convolution layers highly data
efficient and modular.

Convnets consists of stacks of convolution and max-pooling layers. The max-pooling
layers keep feature maps to a reasonable size as the number of features grows, and to
allow subsequent convolution layers to "see" a greater spatial extent of the inputs.
Convnets are often ended with either a Flatten operation or a global pooling layer,
turning spatial feature maps into vectors, followed by Dense layers to achieve
classification or regression.

When building a very deep convnet, it's common to add batch normalization layers as well
as residual connections---two architecture patterns that help gradient information flow
smoothly through the network.

RNNs

RNNs work by processing sequences of inputs one timestep at a time, and maintaining a
state throughout. They should be used preferentially over 1D convnets in the case of
sequences where patterns of interest aren't invariant by temporal translation (e.g.,
timeseries data where the recent past is more important than the distant past).

Transformers

A Transformer looks at a set of vectors and leverages neural attention to transform each
vector into a representation that is aware of the context provided by the other vectors
in the set. When the set in question is an ordered sequence, you can also leverage
positional encoding to create Transformers that can take into account both global
context and word order.

Transformers can be used for any set-processing or sequence-processing task, but they
excel especially at sequence-to-sequence learning.
"""
