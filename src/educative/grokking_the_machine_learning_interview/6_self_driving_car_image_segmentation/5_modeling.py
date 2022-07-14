"""
Main Takeaways
~~~~~~~~~~~~~~

In modeling discussion, we will discuss two key aspects.

    1. SOTA Segmentation Models: What are the state-of-the-art segmentation models and
their architectures?
    2. Transfer Learning: How can you use these models to train a better segmenter for
the self-driving car data?

SOTA segmentation models
------------------------

FCN

Fully convolutional networks (FCNs) are one of the top-performing networks for semantic
segmentation tasks.

A typical FCN operates by fine-tuning an image classification CNN and applying
pixel-wise training. It first compresses the information using multiple layers of
convolutions and pooling. Then, it up-samples these feature maps to predict each pixel’s
class from this compressed information.

The convolutional layers at the end (instead of the fully connected layers) also allow
for dynamic input size. The output pixel-wise classification tends to be coarse, so you
make use of skip connections to achieve good edges. The initial layers capture the edge
information through the deepness of the network. You use that information during our
upsampling to get more refined segmentation.

U-Net

U-Net is commonly used for semantic segmentation-based vision applications. It is built
upon the FCN architecture with some modifications. The overall architecture can be
divided into two halves. The first half down-samples the convolutional features through
the pooling operation. The second half up-samples the feature maps to generate the
output segmentation maps. The upsampling process makes use of skip connections to
concatenate high-resolution features from the downsampling portion. This allows for
accurate upsampling.

In the downsampling portion, the network gains increasing information about what objects
are present but loses information about where objects are present.

In the upsampling portion, skip connections allows the network to create high resolution
segmented outputs. High resolution features are concatenated for accuate upsampling.

Mask R-CNN

Mask R-CNN architecture is constructed by using a convolutional backbone of a powerful
CNN classifier (e.g. ResNet) followed by a Feature Pyramid Network (FPN). FPN extracts
feature maps from the input image at different scales, which are fed to the Region
Proposal Network (RPN). RPN applies a convolutional neural network over the feature maps
in a sliding-window fashion to predict region proposals as bounding boxes that will
contain class objects. These proposals are fed to the RoI Align layer that extracts the
corresponding ROIs (regions of interest) from the feature maps to align them with the
input image properly. The ROI pooled outputs are fixed-size feature maps that are fed to
parallel heads of the Mask R-CNN.

To reduce the computational cost, Mask R-CNN has three parallel heads to perform

    1. Classification
    2. Localization
    3. Segmentation

The output layer of the classifier returns a discrete probability distribution of each
object class. Localisation is performed by the regressor whose output layer generates
the four bounding-box coordinates. The third arm consists of an FCN that generates the
binary masks of the predicted objects.

Transfer learning
-----------------

Assume that, from the above-mentioned SOTA models, you want to utilise a pre-trained FCN
(on ImageNet dataset) for performing segmentation for your self-driving vehicle. Let’s
see three different approaches where you can apply transfer learning.

Retraining topmost layer

This approach makes the most sense when the driving images data is limited and/or you
believe that the current learned layers capture the information that you need for making
a prediction. In this case, you need to update the final pixel-wise prediction layer in
the pre-trained FCN (i.e., replace the classes in ImageNet trained model with classes in
driving image set) and retrain the final layer through an optimizer while freezing the
remaining layers in the FCN.

Retraining top few layers

This approach makes the most sense when you have a decent amount of driving images data.
Also, shallow layers generally don’t need training because they are capturing the basic
image features, e.g., edges, which don’t need retraining. You can experiment with how
many upsampling layers you need to retrain by looking at the IoU metric to see if
retraining any further improves the performance of the segmentation model.

Retraining entire model

As the size of your dataset increase, you can consider retraining even more layers or
retraining the entire model. Once again, you can use the IoU metric to evaluate the
optimal number of layers whose retraining can increase model performance.

Generally, retraining the entire network is laborious and time-consuming. It is usually
done only if the dataset under consideration has completely different characteristics
from the one on which the network was pre-trained.

On top of choosing or designing the optimal DNN architecture, one can also be creative
in adding some extra features in the network to handle the data bias and variance
issues. For instance, adding a regularizer (e.g., L1/L2) after a DNN architecture,
making a hyper-parameter sweep for fine-tuning and experimenting with different
optimizers (e.g., Adam and SGD) during training can further enhance the performance of
the model.

Modeling
========

In modeling discussion, we will discuss two key aspects.

    1. SOTA Segmentation Models: What are the state-of-the-art segmentation models and
their architectures?

    2. Transfer Learning: How can you use these models to train a better segmenter for
the self-driving car data?

SOTA segmentation models
------------------------

Machine learning in general and deep learning, in particular, have progressed a lot in
the domain of computer vision-based applications during the last decade. The models
enlisted in this section are the most commonly used deep neural networks that provide
state-of-the-art (SOTA) results for object detection and segmentation tasks. These tasks
form the basis for the self-driving car use case.

FCN

Fully convolutional networks (FCNs) are one of the top-performing networks for semantic
segmentation tasks.

A typical FCN operates by fine-tuning an image classification CNN and applying
pixel-wise training. It first compresses the information using multiple layers of
convolutions and pooling. Then, it up-samples these feature maps to predict each pixel’s
class from this compressed information.

The convolutional layers at the end (instead of the fully connected layers) also allow
for dynamic input size. The output pixel-wise classification tends to be coarse, so you
make use of skip connections to achieve good edges. The initial layers capture the edge
information through the deepness of the network. You use that information during our
upsampling to get more refined segmentation.

U-Net

U-Net is commonly used for semantic segmentation-based vision applications. It is built
upon the FCN architecture with some modifications. The architectural changes add a
powerful feature in the network to require less training examples. The overall
architecture can be divided into two halves. The first half down-samples the
convolutional features through the pooling operation. The second half up-samples the
feature maps to generate the output segmentation maps. The upsampling process makes use
of skip connections to concatenate high-resolution features from the downsampling
portion. This allows for accurate upsampling.

In the downsampling portion, the network gains increasing information about what objects
are present but loses information about where objects are present.

In the upsampling portion, skip connections allows the network to create high resolution
segmented outputs. High resolution features are concatenated for accuate upsampling.

Mask R-CNN

Mask R-CNN is a powerful deep neural network that is widely used for many real-world
instance segmentation applications. It combines the best of both the worlds: Faster
R-CNN for object detection and localization and FCN for pixel-wise instance segmentation
of objects.

Mask R-CNN architecture is constructed by using a convolutional backbone of a powerful
CNN classifier (e.g. ResNet) followed by a Feature Pyramid Network (FPN). FPN extracts
feature maps from the input image at different scales, which are fed to the Region
Proposal Network (RPN). RPN applies a convolutional neural network over the feature maps
in a sliding-window fashion to predict region proposals as bounding boxes that will
contain class objects. These proposals are fed to the RoI Align layer that extracts the
corresponding ROIs (regions of interest) from the feature maps to align them with the
input image properly. The ROI pooled outputs are fixed-size feature maps that are fed to
parallel heads of the Mask R-CNN.

To reduce the computational cost, Mask R-CNN has three parallel heads to perform

    1. Classification

    2. Localization

    3. Segmentation

The output layer of the classifier returns a discrete probability distribution of each
object class. Localisation is performed by the regressor whose output layer generates
the four bounding-box coordinates. The third arm consists of an FCN that generates the
binary masks of the predicted objects.

Transfer learning
-----------------

Let’s answer the question of how to utilize the discussed SOTA segmentation models to
build one for the self-driving car.

Transfer learning is a widely used technique in the field of deep learning: utilizing
pre-trained powerful deep neural networks (DNNs) for weak or small datasets. When you
kickstart a deep learning project with a small ground-truth (human-annotated) training
data, it is often challenging to scale the performance of your model on a standard-sized
large training dataset. Since increasing the size of human-annotated data can be
time-consuming, transfer learning helps take advantage of a powerful deep neural network
that is pre-trained on a different but large human-annotated dataset that is similar in
nature to the dataset in hand.

We use transfer learning to build upon learned knowledge from one dataset to improve
learning in the dataset.

In a trained model, the low-level feature detectors are fine-tuned to filter
high-frequency visual information (edges), which are mostly common in natural images.
For example, you can transfer the learned edge detectors of a model trained to detect
cats to detect dogs. For more similar objects/images, this similarity can also be
correlated in high-level feature detectors. In this regard, freezing the layers of a
trained deep neural network in transfer learning helps take advantage of the learned
feature detectors from a large and rather similar natural imaging dataset.

Assume that, from the above-mentioned SOTA models, you want to utilise a pre-trained FCN
(on ImageNet dataset) for performing segmentation for your self-driving vehicle. Let’s
see three different approaches where you can apply transfer learning.

Retraining topmost layer

This approach makes the most sense when the driving images data is limited and/or you
believe that the current learned layers capture the information that you need for making
a prediction.

You can take advantage of the large features’ bank in the ImageNet FCN and re-train it
for your smaller driving images dataset. In this case, you need to update the final
pixel-wise prediction layer in the pre-trained FCN (i.e., replace the classes in
ImageNet trained model with classes in driving image set) and retrain the final layer
through an optimizer while freezing the remaining layers in the FCN.

Retraining top few layers

This approach makes the most sense when you have a decent amount of driving images data.
Also, shallow layers generally don’t need training because they are capturing the basic
image features, e.g., edges, which don’t need retraining.

Similarly, in cases where you have a medium-sized driving images dataset available, you
can also try retraining some deeper upsampling layers to improve the accuracy of your
segmenter.

You can experiment with how many upsampling layers you need to retrain by looking at the
IoU metric to see if retraining any further improves the performance of the segmentation
model.

Retraining entire model

As the size of your dataset increase, you can consider retraining even more layers or
retraining the entire model. Once again, you can use the IoU metric to evaluate the
optimal number of layers whose retraining can increase model performance.

Generally, retraining the entire network is laborious and time-consuming. It is usually
done only if the dataset under consideration has completely different characteristics
from the one on which the network was pre-trained.

On top of choosing or designing the optimal DNN architecture, one can also be creative
in adding some extra features in the network to handle the data bias and variance
issues. For instance, adding a regularizer (e.g., L1/L2) after a DNN architecture,
making a hyper-parameter sweep for fine-tuning and experimenting with different
optimizers (e.g., Adam and SGD) during training can further enhance the performance of
the model.
"""
