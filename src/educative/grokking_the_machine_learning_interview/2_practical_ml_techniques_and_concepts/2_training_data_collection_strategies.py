"""
Training Data Collection Strategies
===================================

Significance of training data
-----------------------------

A machine-learning system consists of three main components. They are the training
algorithm (e.g., neural network, decision trees, etc.), training data, and features. The
training data is of paramount importance. The model learns directly from the data to
create and refine its rules on a given task. Therefore, inadequate, inaccurate, or
irrelevant data will render even the most performant algorithms useless. The quality and
quantity of training data are a big factor in determining how far you can go in our
machine learning optimization task.

Collection techniques
---------------------

User’s interaction with pre-existing system (online)

In some cases, the user’s interaction with the pre-existing system can generate good
quality training data.

For many cases, the early version built for solving relevance or ranking problem is a
rule-based system. With the rule-based system in place, you build an ML system for the
task (which is then iteratively improved). So when you build the ML system, you can
utilize the user’s interaction with the in-place/pre-existing system to generate
training data for model training.

Human labelers (offline)

Here, the consumer of the system can’t generate training data for us. They are not
interacting with the system in a way that would give segmentation labels for the images
captured by the camera. In such a scenario, we need to figure out the person/resource
that can generate labeled training data for us.

Targeted data gathering

Offline training data collection is expensive. So, you need to identify what kind of
training data is more important and then target its collection more. To do this, you
should see where the system is failing, i.e., areas where the system is unable to
predict accurately. Your focus should be to collect training data for these areas.

Three such resources are:

    1. Crowdsourcing. Crowdsourcing can be used to collect training data for relatively
simpler tasks without requiring any special training. However, there are cases, like
when we have privacy concerns, where we cannot utilize crowdsourcing.

    2. Specialized labelers. We can hire specialized/trained labelers who can label data
for us according to the given ML task. One caveat of using specialized labelers is that
training them for a specialized task may be time-consuming and costly. The tasks would
be delayed until enough labelers have received training.

    3. Open-source datasets. Generating training data through manual labelers is an
expensive and time-consuming way to gather data. So, we need to supplement it with
open-source datasets where possible.

Additional creative collection techniques
-----------------------------------------

    - Build the product in a way that it collects data from user. We can tweak the
functionality of our product in a way that it starts generating training data for our
model. Let’s consider an example where people go to explore their interests on
Pinterest. You want to show a personalized selection of pins to the new users to
kickstart their experience. This requires data that would give you a semantic
understanding of the user and the pin. This can be done by tweaking the system in the
following way:

        - Ask users to name the board (collection) to which they save each pin. The name
of the board will help to categorize the pins according to their content.

        - Ask new users to choose their interests in terms of the board names specified
by existing users.

    The first step will help you to build content profiles. Whereas, the second step
will help you build user profiles. The model can utilize these to show pins that would
interest the user, personalizing the experience.

    - Creative manual expansion. We can expand training data using creative ways. Assume
that we are building a system that detects logos in images (object detection) and we
have some images containing the logos we want to detect. We can expand/enhance the
training data by manually placing those logos on a different set of images as well. This
logo placement can be done in different positions and sizes.

    - Data expansion using GANs. When working with systems that use visual data, such as
object detectors or image segmenters, we can use GANs to enhance the training data.

Train, test, & validation splits
--------------------------------

The three parts are as follows:

    1. Training data. It helps in training the ML model (fit model parameters).

    2. Validation data. After training the model, we need to tune its hyperparameters.
This process requires testing the model’s performance on various hyperparameter
combinations to select the best one.

    3. Test data. Now that we have trained and tuned the model, the final step is to
test its performance on data that it has not seen before. In other words, we will be
testing the model’s generalization ability. The outcome of this test will allow us to
make the final choice for model selection.

Points to consider during splitting

    - The size of each split will depend on your particular scenario. The training data
will generally be the largest portion, especially if you are training a model like a
deep neural network that requires a lot of training data.

    - While splitting training data, you need to ensure that you are capturing all kinds
of patterns in each split.

    - Most of the time, we are building models with the intent to forecast the future.
Therefore, you need your splits to reflect this intent as well. For instance, in the
movie recommendation system example, your data has a time dimension, i.e., you know the
users’ interactions with previous movie recommendations, and you want to predict their
interactions with future recommendations ahead of time. Hence, you will train the model
on data from one time interval and validate/test it on the data from its succeeding time
interval.

Quantity of training data
-------------------------

As a general guideline, the quantity of the training data required depends on the
modeling technique you are using. If you are training a simple linear model, like linear
regression, the amount of training data required would be less in comparison to more
complex models. If you are training complex models, such as a neural network, the
magnitude of data required would be much greater.

Gathering a large amount of training data requires time and effort. Moreover, the model
training time and cost also increase as we increase the quantity of training data. To
see the optimal amount of training data, you can plot the model’s performance on the
validation set against the number of training data samples. After a certain quantity of
training data, you can observe that there isn’t any gain in the model’s performance.

Training data filtering
-----------------------

It is essential to filter your training data since the model is going to learn directly
from it. Any discrepancies in the data will affect the learning of the model.

    - Cleaning up data. General guidelines are available for data cleaning such as
handling missing data, outliers, duplicates and dropping out irrelevant features. Apart
from this, you need to analyze the data with regards to the given task to identify
patterns that are not useful.

    - Removing bias. When we are generating training data through online user
engagement, it may become biased.

    - Bootstrapping new items. Sometimes we are dealing with systems in which new items
are added frequently. The new items may not garner a lot of attention, so we need to
boost them to increase their visibility. We can boost them by increasing their relevance
scores a little, thereby artificially increasing their chance of being viewed by a
person.
"""
