"""
Ad Prediction
=============

The ad prediction component has to make predictions for the final set of candidate
selected ads. It needs to be robust and adaptive and should be able to learn from
massive data volume.

Modeling approach
-----------------

Ads are generally short-lived. So, our predictive model is going to be deployed in a
dynamic environment where the ad set is continuously changing over time.

Given this change in an ad set, keeping the model up to date on the latest ads is
important. In other words, model performance will degrade with each passing day if it
isn’t refreshed frequently.

Online learning
---------------

If we have to plot the log loss of the model, we can observe the degradation of
prediction accuracy (increase of log loss) because of the increased delay between the
model training and test set.

One approach to minimize this loss could be refreshing the model more frequently e.g.
training it every day on new data accumulated since the previous day.

However, a more practical and efficient approach would be to keep refreshing the model
with the latest impressions and engagements after regular internals (e.g. 15 mins, 30
mins, etc.). This is generally referred to as online learning or active learning.

In this approach, we train a base model and keep adding new examples on top of it with
every ad impression and engagement. From an infrastructure perspective, we now need a
mechanism that collects the recent ad data and merges it with the current model.

The following figure shows some key components that are critical for enabling online
learning. We need a mechanism that generates the latest training examples via an online
joiner. Our training data generator will take these examples and generate the right
feature set for them. The model trainer will then receive these new examples to refresh
the model using stochastic gradient descent. This forms a tightly closed loop where
changes in the feature distribution or model output can be detected, learned on, and
improved in short successions. Note that the refresh of the model doesn’t have to be
instantaneous, and we can do it in same batches at a certain frequency, e.g., every 30
mins, 60 mins etc.

Model for online learning
-------------------------

One model that easily supports online learning and has the ability to update it using
stochastic gradient descent using mini-batches is logistic regression.

Auto non-linear feature generation
----------------------------------

One potential drawback is that simple logistic regression (generalized linear model)
relies on manual effort to create complex feature crosses and generating non-linear
features. Manually creating such features is cumbersome and will mostly be restricted to
modeling the relationship between two or three features. On the other hand, tree and
neural network-based models are really good at generating complex relationships among
features when optimizing the model.

To overcome this, we can use additive trees and neural networks to find such complex
feature crosses and non-linear feature relationships in data, and then these features
are input to our logistic regression model.

Additive trees

To capture complex feature crosses and non-linear relationships from the given raw
features, additive trees can be extremely handy. We can train a model to predict the
probability of engagement using trees and minimize our loss function.

We can represent an additive tree to generate features by taking into account triggered
leaf nodes, e.g., let’s say that we have one-hundred trees in our ensemble with four
leaf nodes each. This will result in 100 * 4 = 400 leaf nodes in which one-hundred nodes
will trigger for every example. This binary vector itself captures the prediction (or
learning) of our tree ensemble. We can just feed this vector as one input feature to our
logistic regression model.

Neural Network

A deep neural network can be trained on the raw input features to predict our ads
engagement to generate features for our logistic regression model.

The following examples show a network trained with two hidden layers to predict our
engagement rate. Once trained, we can use the activation from the last hidden layer to
feed in as input feature vector to our logistic regression model.

So, let’s combine the above two ideas together:

    - We train additive trees and neural network to predict non-linear complex
relationships among our features. We then use these models to generate features.

    - We use raw features and features generated in the previous step to train a logic
regression model.

The above two steps together solve both of our problems to capture complex non-linear
relationships and also enable us to use online learning to refresh the model frequently
for ads that are fast-changing and dynamic in nature.
"""
