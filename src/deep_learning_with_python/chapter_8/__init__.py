"""Introduction to deep learning for computer vision

8.1 Introduction to convents
============================

8.1.1 The convolution operation
-------------------------------

The fundamental difference between a densely connected layer and a convolution layer is
this: Dense layers learn global patterns in their input feature space (i.e., patterns
involving all pixels), whereas convolution layers learn local patterns (i.e., patterns
found in small windows of the inputs).

This key characteristic gives convnets two interesting properties:

- The patterns they learn are translation-invariant. After learning a certain pattern, a
convnet can recognize it anywhere. A densely connected model would have to learn the
pattern anew if it appeared in a new location. This makes convnets data-efficient when
processing images (because the visual world is fundamentally translation-invariant):
they need fewer training samples to learn representations that have generalization
power.

- They can learn spatial hierarchies of patterns. A first convolution layer will learn
small local patterns such as edges, a second convolution layer will learn larger
patterns made of the features of the first layers, and so on. This allows convnets to
efficiently learn increasingly complex and abstract visual concepts, because the visual
world is fundamentally spatially hierarchical.

Convolutions operate over rank-3 tensors called feature maps, with two spatial axes
(height and width) as well as a depth axis (also called the channels axis). The
convolution operation extracts patches from its input feature map and applies the same
transformation to all of these patches, producing an output feature map. This output
feature map is still a rank-3 tensor: it has a width and a height. Its depth can be
arbitrary, because the output depth is a parameter of the layer, and the different
channels in that depth axis no longer stand for specific colors; rather, they stand for
filters. Filters encode specific aspects of the input data.

Each channel in a feature map is a grid of values called a response map of the filter
over the input, indicating the response of that filter pattern at different locations in
the input.

That is what the term feature map means: every dimension in the depth axis is a feature
(or filter), and the rank-2 tensor outputs are 2D spatial maps of the response of a
particular filter over the input.

Convolutions are defined by two key parameters:

- Size of the patches extracted from the inputs

- Depth of the output feature map

A convolution works by sliding these windows over the 3D input feature map, stopping at
every possible location, and extracting the 3D patch of surrounding features. Each such
3D patch is then transformed into a 1D vector of shape (output_depth,), which is done
via a tensor product with a learned weight matrix, called the convolution kernel---the
same kernel is reused across every patch. All of these vectors (one per patch) are then
spatially reassembled into a 3D output map of shape (height, width, output_depth). Every
spatial location in the output feature map corresponds to the same location in the input
feature map (although the output feature maps are smaller spatially).

Note that the output width and height may differ from the input width and height for two
reasons:

- Border effects, which can be countered by padding the input feature map.

- The use of strides.

Understanding Border Effects and Padding

If you want to get an output feature map with the same spatial dimensions as the input,
you can use padding. Padding consists of adding an appropriate number of rows and
columns on each side of the input feature map so as to make it possible to fit center
convolution windows around every input tile.

Understanding Convolution Strides

The other factor that can influence output size is the notion of strides. The distance
between two successive windows is a parameter of the convolution, called its stride.
It's possible to have strided convolutions: convolutions with a stride higher than 1.

Using a stride of 2 means the width and height of the feature map are downsampled by a
factor of 2 (in addition to any changes induced by border effects). Strided convolutions
are rarely used in classification models, but they come in handy for some types of
models (see Chapter 9).

In classification models, instead of strides, we tend to use the max-pooling operation
to downsample feature maps.

8.1.2 The max-pooling operation
-------------------------------

The role of max-pooling is to aggressively downsample feature maps, much like strided
convolutions.

Max pooling consists of extracting windows from the input feature maps and outputting
the max value of each channel. It's conceptually similar to convolution, except that
instead of transforming local patches via a learned linear transformation (the
convolution kernel), they're transformed via a hardcoded max tensor operation. A big
difference from convolution is that max pooling is usually done with 2 x 2 windows and
stride 2, in order to downsample the feature maps by a factor of 2. On the other hand,
convolution is typically done with 3 x 3 windows and stride 1.

Why downsample feature maps this way? Why not remove the max-pooling layers and keep the
fairly large feature maps al the way up?

Two things:

- It isn't conducive to learning a spatial hierarchy of features. The 3 x 3 windows in
the third layer will only contain information coming from 7 x 7 windows in the initial
input. The high-level patterns learned by the convnet will still be very small with
regard to the initial input, which may not be enough to learn to classify digits (try
recognizing a digit by only looking at it through windows that are 7 x 7 pixels!). We
need the features from the last convolution layer to contain information about the
totality of the input. We max-pooling, the 3 x 3 windows in the third layer will contain
information coming from 18 x 18 windows in the initial input instead.

- The final feature map would have a large number of coefficients without some form of
downsampling before being fed to the Dense layer.

In short, the reason to use downsampling is to reduce the number of feature-map
coefficients to process, as well as to induce spatial-filter hierarchies by making
successive convolution layers look at increasingly large windows of the initial input.

Max pooling tends to work better than other strategies such as average pooling and
strided convolutions. The reason is that features tend to encode the spatial presence of
some pattern or concept over the different tiles of the feature map, and its more
informative to look at the maximal presence of different features than at their average
presence. The most reasonable subsampling strategy is to first produce dense maps of
features (via unstrided convolutions) and then look at the maximal activation of the
features over small patches, rather than looking at sparser windows of the inputs (via
strided convolutions) or averaging input patches, which could cause you to miss or
dilute feature-presence information.

8.2 Training a convnet from scratch on a small dataset
======================================================

The three main strategies are:

1. Training a small model from scratch

2. Doing feature extraction using a pretrained model

3. Fine-tuning a pretrained model

8.2.1 The relevance of deep learning for small-data problems
------------------------------------------------------------

A few hundred examples can potentially suffice if the model is small and well
regularized and the task is simple. Because convnets learn local, translation-invariant
features, they're highly data-efficient on perceptual problems. Training a convnet from
scratch on a very small image dataset will yield reasonable results despite a relative
lack of data, without the need for any custom feature engineering.

8.2.3 Building the model
------------------------

The depth of feature maps progressively increases in the model, whereas the size of the
feature maps decreases. This is a pattern you'll see in almost all convnets.

8.2.4 Data preprocessing
------------------------

A technique specific to computer vision and used almost universally when processing
images with deep learning models is data augmentation.

8.2.5 Using data augmentation
-----------------------------

Overfitting is caused by having too few samples to learn from, rendering you unable to
train a model that can generalize to new data. Data augmentation takes the approach of
generating more training data from existing training samples by augmenting the samples
via a number of random transformations that yield believable-looking images. The goal is
that, at training time, your model will never see the exact same picture twice. This
helps expose the model to more aspects of the data so it can generalize better.

But the inputs it sees are still heavily intercorrelated because they come from a small
number of original images---we can't produce new information; we can only remix existing
information. As such, this may not be enough to completely get rid of overfitting. To
further fight overfitting, we'll also add a Dropout layer (typically right before the
last Dense layer).

8.3 Leveraging a pretrained model
=================================


"""
