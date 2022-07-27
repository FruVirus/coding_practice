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
totality of the input. With max-pooling, the 3 x 3 windows in the third layer will
contain information coming from 18 x 18 windows in the initial input instead.

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

A common and highly effective approach to deep learning on small image datasets is to
use a pretained model. A pretrained model is a model that was previously trained on a
large dataset. If this original dataset is large enough and general enough, the spatial
hierarchy of features learned by the pretrained model can effectively act as a generic
model of the visual world, and hence, its features can prove useful for many different
computer vision problems, even though these new problems may involve completely
different classes than those of the original task.

There are two ways to use a pretrained model: feature extraction and fine-tuning.

8.3.1 Feature extraction with a pretrained model

Feature extraction consists of using the representations learned by a previously trained
model to extract interesting features from new samples. These features are then run
through a new classifier, which is trained from scratch.

The series of pooling and convolution layers is called the convolutional base of the
model. In the case of convnets, feature extraction consists of taking the convolutional
base of a previously trained network, running the new data through it, and training a
new classifier on top of the output.

Why only reuse the convolutional base? Could we reuse the densely connected classifier
as well? In general, doing so should be avoided. The reason is that the representations
learned by the convolutional base are likely to be more generic and, therefore, more
reusable: the feature maps of a convnet are presence maps of generic concepts over a
picture, which are likely to be useful regardless of the computer vision problem at
hand. But the representations learned by the classifier will necessarily be specific to
the set of classes on which the model was trained---they will only contain information
about the presence probability of this or that class in the entire picture.
Additionally, representations found in densely connected layers no longer contain any
information about where objects are located in the input image; these layers get rid of
the notion of space, whereas the object location is still described by convolutional
feature maps. For problems where object location matters, densely connected features are
largely useless.

The level of generality of the representations extracted by specific convolution layers
depends on the depth of the layer in the model. Layers that come earlier in the model
extract local, highly generic feature maps, whereas layers that are higher up extract
more abstract concepts. So if your new dataset differs a lot from the dataset on which
the original model was trained, you may be better off using only the first few layers of
the model to do feature extraction, rather than using the entire convolutional base.

There are two ways we can proceed with feature extraction:

1. Run the convolutional base over our dataset, record its output to a NumPy array on
disk, and then use this data as input to a standalone, densely connected classifier.
This solution is fast and cheap to run, because it only requires running the
convolutional base once for every input image, and the convolutional base is by far the
most expensive part of the pipeline. But for the same reason, this technique won't allow
us to use data augmentation (since we are not feeding the augmented images through the
convolutional base).

2. Extend the convolutional base model by adding Dense layers on top, and run the whole
thing from end to end on the input data. This will allow us to use data augmentation,
because every input image goes through the convolutional base every time it's seen by
the model. But for the same reason, this technique is far more expensive than the first.

Fast Feature Extraction Without Data Augmentation

We extract features as NumPy arrays by calling the predict() method of the convolutional
base model on our training, validation, and test datasets. These features are then fed
into our classifier and trained from scratch.

Since this technique doesn't use data augmentation, we tend to rapidly overfit with
small image datasets.

Feature Extraction Together with Data Augmentation

In order to do this, we will first freeze the convolutional base so that we prevent
their weights from being updated during training. If we don't do this, the
representations that were previously learned by the convolutional base will be modified
during training. Because the Dense layers on top are randomly initialized, very large
weight updates would be propagated through the network, effectively destroying the
previously learned representations.

Now we can create a new model that chains together:

1. A data augmentation stage
2. Our frozen convolutional base
3. A dense classifier

8.3.2 Fine-tuning a pretrained model
------------------------------------

Another widely-used technique for model reuse is fine-tuning. Fine-tuning consists of
unfreezing a few of the top layers of a frozen model base used for feature extraction,
and jointly training both the newly added part of the model and these top layers. This
is called fine-tuning because it slightly adjusts the more abstract representations of
the model being reused in order to make them more relevant for the problem at hand.

It's only possible to fine-tune the top layers of the convolutional base once the
classifier on top has already been trained. If the classifier isn't already trained, the
error signal propagating through the network during fine-tuning will be too large, and
the representations previously learned by the layers being fine-tuned will be destroyed.
Thus, the steps for fine-tuning a network are as follows:

1. Add the custom network on top of an already-trained base network.
2. Freeze the base network.
3. Train the part we added.
4. Unfreeze some layers in the base network (except for Batch Normalization layers).
5. Jointly train both the unfrozen layers and the part we added.

Note that steps 1 - 3 correspond to feature extraction steps.

We could fine-tune the entire convolutional base. However, you need to consider the
following:

- Earlier layers in the convolutional base encode more generic, reusable features,
whereas layers higher up encode more specialized features. It's more useful to fine-tune
the more specialized features, because these are the ones that need to be repurposed on
your new problem. There would be fast-decreasing returns in fine-tuning the lower
layers.

- The more parameters you're training, the more you're at risk of overfitting on small
datasets.

When fine-tuning, we also want to use a much lower learning rate. The reason is that we
want to limit the magnitude of the modifications we make to the representations of the
layers we're fine-tuning. Updates that are too large may harm these representations.

In general, fine-tuning can lead to better performance gains than feature extraction.
"""
