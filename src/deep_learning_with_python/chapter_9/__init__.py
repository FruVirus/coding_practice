"""Advanced deep learning for computer vision

9.2 An image segmentation example
=================================

Image segmentation with deep learning is about using a model to assign a class to each
pixel in an image, thus segmenting the image into different zones.

There are two different flavors of image segmentation that you should know about:

- Semantic segmentation, where each pixel is independently classified into a semantic
category, like "cat." If there are two cats in the image, the corresponding pixels are
all mapped to the same generic "cat" category.

- Instance segmentation, which seeks not only to classify image pixels by category, but
also to parse out individual object instances. In an image with two cats in it, instance
segmentation would treat "cat 1" and "cat 2" as two separate classes of pixels.

A segmentation mask is the image-segmentation equivalent of a label: it's an image the
same size as the input image, with a single color channel where each integer value
corresponds to the class of the corresponding pixel in the input image.

In segmentation, we typically use downsample by adding strides to every other
convolution layer instead of using max pooling. We do this because, in the case of image
segmentation, we care a lot about the spatial location of information in the image,
since we need to produce per-pixel target masks as output of the model. When you do
2 x 2 max pooling, you are completely destroying location information within each
pooling window: you return one scalar value per window, with zero knowledge of which of
the four locations in the windows the value came from. So while max pooling layers
perform well for classification tasks, they would hurt us quite a bit for a segmentation
task. Meanwhile, strided convolutions do a better job at downsampling feature maps while
retaining location information.

9.3 Modern convnet architecture patterns
========================================

A good model architecture is one that reduces the size of the search space or otherwise
makes it easier to converge to a good point of the search space. Model architecture is
all about making the problem simpler for gradient descent to solve.

9.3.1 Modularity, hierarchy, and reuse
--------------------------------------

The MHR formula is that you structure your amorphous soup of complexity into modules,
organize the modules into a hierarchy, and start reusing the same modules in multiple
places as appropriate. It underlies system architecture across pretty much every domain.

Deep learning model architecture is primarily about making clever use of the MHR
principle. All popular convnet architectures are not only structured into layers,
they're structured into repeated groups of layers (called "blocks" or "modules").

Most convnets often feature pyramid-like structures (feature hierarchies). The number of
filters grows with layer depth, while the size of the feature maps shrinks accordingly.

Deeper hierarchies are intrinsically good because they encourage feature reuse, and
therefore abstraction. In general, a deep stack of narrow layers performs better than a
shollow stack of large layers. However, there's a limit to how deep you can stack
layers, due to the problem of vanishing gradients. This leads us to our first essential
model architecture pattern: residual connections.

9.3.2 Residual connections
--------------------------

Residual connections helps ease the vanishing gradient problem in deep models by forcing
each layer in the model architecture to be nondestructive---to retain a noiseless
version of the information contained in the previous input. The easiest way to implement
this is to use a residual connection; i.e., just add the input of a layer or block of
layers back to its output. The residual connection acts as an information shortcut
around destructive or noisy blocks (such as blocks that contain relu activations or
dropout layers), enabling error gradient information from early layers to propagate
noiselessly through a deep network.

Adding the input back to the output of a block implies that the output should have the
same shape as the input. However, this is not the case if your block includes
convolutional layers with an increased number of filters, or a max pooling layer. In
such cases, use a 1 x 1 conv layer with no activation to linearly project the residual
to the desired output depth and strided convolution to match any downsampling caused by
a max pooling layer.

9.3.3 Batch normalization
-------------------------

Data normalization may be of interest after every transformation operated by the
network: even if the data entering a Dense of Conv2D network has a 0 mean and unit
variance, there's no reason to expect apriori that this will be the case for the data
coming out.

Batch normalization is a type of layer that can adaptively normalize data even as the
mean and variance change over time during training. During training, it uses the mean
and variance of the current batch of data to normalize samples, and during inference
(when a big enough batch of representative data may not be available), it uses an
exponential moving average of the batch-wise mean and variance of the data seen during
training.

The BatchNormalization layer can be used after any layer---Dense, Conv2D, etc. Because
the batch normalization step will take care of centering the layer's output on zero, the
bias vector is no longer needed when using BatchNormalization layers, and the layer can
be created without it.

You can place the BatchNormalization layer after a layer that uses an activation or
after the layer output and before its activation. It is recommended to use batch
normalization after the layer output and before its activation. The intuitive reason for
this approach is that batch normalization will center your inputs on zero, while your
RELU activation uses zero as a pivot for keeping or dropping activated channels: doing
normalization before the activation maximizes the utilization of the RELU.

When fine-tuning a model that includes BatchNormalization layers, it is recommended to
leave those layer frozen. Otherwise, they will keep updating their internal mean and
variance, which can interfere with the very small updates applied to the surrounding
layers.

9.3.4 Depthwise separable convolutions
--------------------------------------

A depthwise separable convolution layer performs a spatial convolution on each channel
of its input, independently, before mixing output channels via a pointwise convolution
(i.e., a 1 x 1 convolution). It serves as a drop-in replacement for Conv2D layers that
will make the model smaller (fewer trainable weight parameters) and leaner (fewer
floating-point operations) and cause it to perform a few percentage points better on its
task.

This is equivalent to separating the learning of spatial features and the learning of
channel-wise features. In much the same way that convolution relies on the assumption
that the patterns in images are not tied to specific locations, depthwise separable
convolution relies on the assumption that spatial locations in intermediate activations
are highly correlated, but different channels are highly independent. Because this
assumption is generally true for the image representations learned by deep neural
networks, it serves as a useful prior that helps the model make more efficient use of
its training data.

Depthwise separable convolutions requires significantly fewer parameters and involves
fewer computations compared to regular convolution, while having comparable
representational power. It results in smaller models that converge faster and are less
prone to overfitting. These advantages become especially important when you're training
small models from scratch on limited data.

Take an input image of size 12 x 12 x 3. If we convolve this with a 5 x 5 x 256 x 3
kernel, we get a 8 x 8 x 256 output feature map. Since there are 256 5 x 5 x 3 kernels
that move 8 x 8 times in the input image, there are a total of 256 x 3 x 5 x 5 x 8 x 8 =
1,228,800 multiplication operations.

Take an input image of size 12 x 12 x 3. If we convolve this with a 5 x 5 x 1 x 3
kernel, we get a 8 x 8 x 3 output feature map. If we then convolve the 8 x 8 x 3 output
feature map with a 1 x 1 x 256 kernel, we get a 8 x 8 x 256 output feature map. Here, we
have 3 5 x 5 x 1 kernel that move 8 x 8 times, for a total of 3 x 5 x 5 x 8 x 8 = 4,800
multiplications. Then, we have 256 1 x 1 x 3 kernels that move 8 x 8 times, for a total
of 256 x 1 x 1 x 3 x 8 x 8 = 49,152 multiplications. The total is 53,952 multiplication
operations.

The main difference is this: in the normal convolution, we are transforming the input
image 256 times and each transformation uses 5 x 5 x 3 x 8 x 8 = 4,800 multiplications.
In the depthwise separable convolution, we only transform the image once---in the
depthwise convolution. Then, we take the transformed image and simply elongate it to
256 channels.

9.3.5 Putting it together: A mini Xception-like model
-----------------------------------------------------

Here are the convnet principlies you've learned so far:

- Your model should be organized into repeated blocks of layers, usually made of
multiple convolution layers and a max pooling layer

- The number of filters in your layers should increase as the size of the spatial
feature maps decreases

- Deep and narrow is better than broad and shallow

- Introducing residual connections around blocks of layers helps you train deeper
networks

- It can be beneficial to introduce batch normalization layers after your convolution
layers

It can be beneficial to replace Conv2D layers with SeparableConv2D layers, which are
more parameter-efficient

NB: The assumption that underlies separable convolution, "feature channels are largely
independent," does not hold for RGB images since the color channels are actually highly
corrleated in natural images. As such, the first layer in a convnet model should just be
a regular Conv2D layer.

9.4 Interpreting what convnets learn
====================================

A wide array of techniques have been developed for visualizing and interpreting convnet
representations:

- Visualizing intermediate convnet outputs (intermediate activations)---Useful for
understanding how successive convnet layers transform their input, and for getting a
first idea of the meaning of individual convnet filters.

- Visualizing convnet filters---Useful for understanding precisely what visual pattern
or concept each filter in a convnet is receptive to

- Visualizing heatmaps of class activation in an image---Useful for understanding which
parts of an image were identified as belonging to a given class, thus allowing you to
localize objects in images

9.4.1 Visualizing intermediate activations
------------------------------------------

Visualizing intermediate activations consists of displaying the values returned by
various convolution and pooling layers in a model, given a certain input (the output of
a layer is often called its activation, the output of the activation function). This
gives a view into how an input is decomposed into the different filters learned by the
network. We want to visualize feature maps with three dimensions: width, height, and
depth (channels). Each channel encodes relatively independent features, so the proper
way to visualize these feature maps is by independently plotting the contents of every
channel as a 2D image.

There are a few things to note:

- The first layer acts as a collection of various edge detectors. At that stage, the
activations retain almost all of the information present in the initial picture.

- As you go deeper, the activations become increasingly abstract and less visually
interpretable. They being to encode higher-level concepts. Deeper representations carry
increasingly less information about the visual contents of the image, and increasingly
more information related to the class of the image.

- The sparsity of the activations increases with the depth of the layer: in the first
layer, almost all filters are activated by the input image, but in the following layers,
more and more filters are blank. This means the pattern encoded by the filter isn't
found in the input image.

9.4.2 Visualizing convnet filters
---------------------------------

Another easy way to inspect the filters learned by convnets is to display the visual
pattern that each filter is meant to respond to. This can be done with gradient ascent
in input space: applying gradient descent to the value of the input image of a convnet
so as to maximize the response of a specific filter, starting from a blank input image.
The resulting input image will be one that the chosen filter is maximally responsive to.

The process is simple: we'll build a loss function that maximizes the value of a given
filter in a given convolution layer, and then we'll use SGD to adjust the values of the
input image so as to maximize this activation value. We can simply use the mean of the
activation values for the filter as the "loss" that we want to maximize.

These filter visualizations tell you a lot about how convnet layers see the world: each
layer in a convnet learns a collection of filters such that their inputs can be
expressed as a combination of the filters. This is similar to how the Fourier transform
decomposes signals onto a bank of cosine functions. THe filters in these convnet filter
banks get increasingly complex and refined as you go deeper in the model:

- The filters from the first layers in the model encode simple directional edges and
colors (or colored edges, in some cases)

- The filters from layers a bit further up the stack encode simple textures made from
combinations of edges and colors

- The filters in higher layers begin to resemble textures found in natural images:
feathers, eyes, leaves, and so on.

9.4.3 Visualizing heatmaps of class activation
----------------------------------------------

Visualizing heatmaps of class activations is useful for understanding which parts of a
given image led a convnet to its final classification decision. It is helpful for
"debugging" the decision process of a convnet, particularly in the case of a
classification mistake. It can also allow you to locate specific objects in an image.

This general category of techniques is called class activation map (CAM) visualization,
and it consists of producing heatmaps of class activation over inputs images. A class
activation heatmap is a 2D grid of scores associated with a specific output class,
computed for every location in any input image, indicating how important each location
is w.r.t the class under consideration. For instance, given an image fed into a
dogs-versus-cats convnet, CAM visualization would allow you to generate a heatmap for
the class "cat," indicating how cat-like different parts of the image are, and also a
heatmap for the class "dog," indicating how dog-like parts of the image are.

Grad-CAM consists of taking the output feature map of a convolution layer, given an
input image, and weighing every channel in that feature map by the gradient of the class
w.r.t. the channel. Intuitively, one way to understand this trick is to imagine that
you're weighting a spatial map of "how intensely the input image activates different
channels" by "how important each channel is with regard to the class," resulting in a
spatial map of "how intensely the input image activates the class." In other words, we
want to calculate how changing the input image changes the class prediction by
calculating how changing the input image changes the channels of the convnet feature
maps and how change the channels of the convnet feature maps change the class
prediction.

First, we create a model that maps the input image to the activations of the last
convolutional layer in the model. We use the activations of the last convolutional layer
since the last convolutional layer contains the feature maps that are ultimately used
for classification.

Second, we create a model that maps the activations of the last convolutional layer to
the final class predictions. This is just reapplying the classifier on top of the last
convolutional layer output.

Then, we compute the gradient of the top predicted class (or any class we care about)
for our input image w.r.t the activations of the last convolution layer.

Finally, we apply pooling and importance weighting to the gradient tensor to obtain our
heatmap of class activation.
"""
