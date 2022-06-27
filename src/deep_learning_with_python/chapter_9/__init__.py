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
"""
