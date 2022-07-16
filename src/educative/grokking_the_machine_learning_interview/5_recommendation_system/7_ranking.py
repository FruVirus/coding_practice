"""
Ranking
=======

Your goal is to rank the content based on the probability of a user watching a media
given a user and a candidate media, i.e., P(watch|(User, Media)).

The ranking model takes the top candidates from multiple sources of candidate
generation. Then, an ensemble of all of these candidates is created, and the candidates
are ranked with respect to the chance of the user watching that video content.

First, we will discuss some approaches using logistic regression or tree ensemble
methods and then a deep learning model with dense and sparse features.

Deep learning should be able to learn through sparse features and outperform simplistic
approach.

Approach 1: Logistic regression or random forest
------------------------------------------------

There are multiple reasons that training a simplistic model might be the way to go. They
are as follows:

    - Training data is limited

    - You have limited training and model evaluation capacity

    - You want model explainability to really understand how the ML model is making its
decision and show that to the end-user

    - You require an initial baseline to see how far you can go in reducing our test set
loss before you try more complex approaches

Approach 2: Deep NN with sparse and dense features
--------------------------------------------------

Another way to model this problem is to set up a deep NN. Some of the factors that were
discussed in Approach 1 are now key requirements for training this deep NN model. They
are as follows:

    - Hundreds of millions of training examples should be available

    - Having the capacity to evaluate these models in terms of capacity and model
interpretability is not that critical.

Since the idea is that you want to predict whether the user will watch the media or not,
you train a deep NN with sparse and dense features for this learning task. Two extremely
powerful sparse features fed into such a network can be videos that the user has
previously watched and the user’s search terms. For these sparse features, you can set
up the network to also learn media and search term embeddings as part of the learning
task. These specialized embeddings for historical watches and search terms can be very
powerful in predicting the next watch idea for a user. They will allow the model to
personalize the recommendation ranking based on the user’s recent interaction with media
content on the platform.

An important aspect here is that both search terms and historical watched content are
list-wise features (i.e., they continue to grow over time). You need to think about how
to feed them in the network given that the size of the layers is fixed. You can use an
approach similar to pooling layers in CNN (convolution neural networks) and simply
average the historical watch id and search text term embeddings before feeding it into
the network.

Network structure
-----------------

You should start with 2-3 hidden layers with a RELU based activation unit and then play
around with the numbers to see how this helps us reduce the test error. Generally,
adding more layers and units helps initially, but its usefulness tapers off quickly. The
computation and time cost would be higher relative to the drop in error rate.

Re-ranking
----------

Re-ranking is done for various reasons, such as bringing diversity to the
recommendations. Consider a scenario where all the top ten recommended movies are
comedy. You might decide to keep only two of each genre in the top ten recommendations.
This way, you would have five different genres for the user in the top recommendations.

If you are also considering past watches for the media recommendations, then re-ranking
can help you. It prevents the recommendation list from being overwhelmed by previous
watches by moving some previously watched media down the list of recommendations.
"""
