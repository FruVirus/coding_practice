"""
Training Data Generation
========================

Generating training examples
----------------------------

Autonomous driving systems have to be extremely robust with no margin of error. This
requires training each component model with all the possible scenarios that can happen
in real life.

Human-labeled data
------------------

First, you will have to gather driving images and hire people to label the images in a
pixel-wise manner.

Open source datasets
--------------------

There are quite a few open-source datasets available with segmented driving
videos/images.

These two methods are effective in generating manually labeled data. In most cases, your
training data distribution will match with what you observe in the real-world scene
images. However, you may not have enough data for all the conditions that you would like
your model to make predictions for such as snow, rain, and night. For a self-autonomous
vehicle to be perfect, your segmenter should work well for all the possible weather
conditions, as well as cover a variety of obstacle images in the road.

It is an important area to think about how you can give your model training data for all
conditions. One option is to manually label a lot of examples for each scenario. The
second option is to use powerful data augmentation techniques to generate new training
examples given your human-labeled data, especially for conditions that are missing in
your training set.

Training data enhancement through GANs
--------------------------------------

The segmenter can play its role in creating a reliable system by being able to
accurately segment the driving scene in any condition that the vehicle experiences.

The target includes two parts:

    1. Generating new training images

    2. Ensuring generated images have different conditions (e.g., weather and lighting
conditions).

For the first part, you can utilize GANs. They are deep learning models used for
generation of new content. However, for the second part, i.e., to generate a different
variation of the original segmented image, a simple GAN would not work. You would have
to use conditional generative adversarial networks (cGANs) instead.

If you train a GAN on a set of driving images, you do not have any control over the
generator’s output, i.e., it would just generate driving images similar to the images
present in the training dataset. However, that is not particularly useful in your case.

Therefore, we want to perform image-to-image translation (a kind of data augmentation)
to enhance our training data, i.e., you want to map features from an input image to an
output image. For instance, you want to learn to map driving images with one weather
condition to another weather condition, or you may want to convert day time driving
images to night time images and vice versa. This can be done with a cGAN which is a deep
neural network that extends the concept of GAN.

For image translation, your training data should consist of paired images. For example,
image pairs could be of the same road during day and night. They could also be of the
same road during winter and summer.

In cGAN, you give the source image that you want to translate to the generator, along
with an additional input (target image as a condition). This will guide the generator’s
output image to be of the same place but with a different weather/light condition.

You will also feed the source image to the discriminator so that apart from its usual
task of discriminating between real and generated images, it will also see if the given
image is a plausible translation of the source image.

You see that the cGAN loss function differs from the GAN loss function as the
discriminator’s probability D(x) or D(G(z)) is now conditioned on y.

Once you have trained the cGAN for the image translation task, you can now feed it the
driving images you manually collected through the generator model to enhance the
training data.

Targeted data gathering
-----------------------

Your aim is to gather training data specifically on the areas where you fail while
testing the system. It will help to further enhance the training data.

After this, you can also apply data augmentation on the newly gathered training examples
to further improve your model’s performance.

It is worth mentioning that most of the deep vision architectures are not inherently
designed to preserve sensitivity for different scales, sizes and rotations of the
objects/images. The pooling operation in these networks is only able to capture the
translational variance of the labeled objects/images. Hence, it is critical to cover
the variation in scale and rotation of your training images and keep the testing image
size similar to the image size in your training dataset.
"""
