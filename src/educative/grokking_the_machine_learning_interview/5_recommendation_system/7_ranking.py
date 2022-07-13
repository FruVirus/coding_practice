"""
Main Takeaways
~~~~~~~~~~~~~~

The task at hand is to predict the probability of different engagement actions for a
given Tweet. So, essentially, your models are going to predict the probability of likes,
comments and retweets, i.e., P(click), P(comments) and P(retweet). Looking at the
training data, we know that this is a classification problem where we want to minimize
the classification error or maximize area under the curve (AUC).

Some questions to consider are: Which model will work best for this task? How should you
set up these models? Should you set up completely different models for each task?

Initially, a simple model that makes sense to train is a logistic regression model with
regularization, to predict engagement using dense features. A key advantage of using
logistic regression is that it is reasonably fast to train. This enables you to test new
features fairly quickly to see if they make an impact on the AUC or validation error.
Also, it’s extremely easy to understand the model. You can see from the feature weights
which features have turned out to be more important than others.

A major limitation of the linear model is that it assumes linearity exists between the
input features and prediction. Therefore, you have to manually model feature
interactions. Other models like tree-based and neural networks are able to learn these
feature interactions and utilize them effectively for predictions.

Another key question is whether you want to train a single classifier for overall
engagement or separate ones for each engagement action based on production needs. In a
single classifier case, you can train a logistic regression model for predicting the
overall engagement on a Tweet. Tweets with any form of engagement will be considered as
positive training examples for this approach. Another approach is to train separate
logistic regression models to predict P(like), P(comments) and P(retweet). These models
will utilize the same features. However, the assignments of labels to the training
examples will differ. Tweets with likes, comments, or retweets will be considered
positive examples for the overall engagement predictor model. Only Tweets with likes
will be considered as positive examples for the “Like” predictor model. Similarly, only
Tweets with comments will be considered as positive examples for the “Comment” predictor
model and only Tweets with retweets will be considered as positive examples for the
“Retweet” predictor model.

Another modeling option that should be able to outperform logistic regression with dense
features is additive tree-based models, e.g., Boosted Decision Trees and Random Forest.
Trees are inherently able to utilize non-linear relations between features that aren’t
readily available to logistic regression. Tree-based models also don’t require a large
amount of data as they are able to generalize well quickly. So, a few million examples
should be good enough to give us an optimized model.

There are various hyperparameters that you might want to play around to get to an
optimized model, including

    - Number of trees
    - Maximum depth
    - Minimum samples needed for split
    - Maximum features sampled for a split

Approach 1

A simple approach is to train a single model to predict the overall engagement.

Approach 2

You could have specialized predictors to predict different kinds of engagement. For
example, you can have a like predictor, a comment predictor and a reshare predictor.
Once again these models will utilize the same features. However, the assignments of
labels to the training examples will differ depending on the model’s objective.

Approach 3

One way to utilize the overall engagement data among each individual predictor of
P(like), P(comment) and P(retweet) is to build one common predictor, i.e., P(engagement)
and share its output as input into all of your predictors. To take this approach a notch
further, you can use the output of each tree in the “overall engagement predictor”
ensemble as features in the individual predictors. This allows for even better learning
as the individual model will be able to learn from the output of each individual tree.

Training a deep learning model as well as evaluating the model at feed generation time
can make deep learning computationally very expensive. So, you may want to fall back to
the multi-layer approach; i.e., having a simpler model for stage one ranking and use
complex stage two model to obtain the most relevant Tweets ranked at the top of the
user’s Twitter feed.

One way is to train separate neural nets for each of the P(like), P(comment) and
P(retweet). However, for a very large scale data set, training separate deep neural
networks (NNs) can be slow and take a very long time (ten’s of hours to days).

Predicting P(like), P(comment) and P (retweet) are similar tasks. When predicting
similar tasks, you can use multitask learning. Hence, you can train a neural network
with shared layers (for shared knowledge) appended with specialized layers for each
task’s prediction. The weights of the shared layers are common to the three tasks.
Whereas in the task-specific layer, the network learns information specific to the
tasks. The loss function for this model will be the sum of individual losses for all the
tasks. The model will then optimize for this joint loss leading to regularization and
joint learning. This will also allow us to share all the engagement data across each
learning task. This approach should be able to perform at least as effective as training
separate networks for each task. It should be able to outperform in most cases as we use
the shared data and use it across each predictor. Also, one key advantage of using
shared layers is that models would be much faster to train than training completely
separate deep neural networks for each task.

One way to outperform the “single model technique approach” is to use multiple models to
utilize the power of different techniques by stacking models on top of each other. The
setup includes training tree-based models and neural networks to generate features that
you will utilize in a linear model (logistic regression). The main advantage of doing
this is that you can utilize online learning, meaning we can continue to update the
model with every user action on the live site. You can also use sparse features in our
linear model while getting the power of all non-linear relations and functions through
features generated by tree-based models and neural networks.

For trees, you can generate features by using the triggering of leaf nodes, e.g., given
two trees with four leaf nodes, each will result in eight features that can be used in
logistic regression. Each leaf node in the random forest will result in a boolean
feature that will be active based on whether the leaf node is triggered or not.

Similarly, for neutral networks, rather than predicting the probability of events, you
can just plug-in the output of the last hidden layer as features into the logistic
regression models.

To summarize, this stacking model setup will still give us all the learning power of
deep neural networks and tree-based models along with the flexibility of training
logistic regressions model, while keeping it almost real-time refreshed with online
learning.

Given that features like tweet_id and user_id are extremely sparse, training and
evaluation of the model must be done in a distributed environment because the data won’t
fit on one machine.

Ranking
=======

The task at hand is to predict the probability of different engagement actions for a
given Tweet. So, essentially, your models are going to predict the probability of likes,
comments and retweets, i.e., P(click), P(comments) and P(retweet). Looking at the
training data, we know that this is a classification problem where we want to minimize
the classification error or maximize area under the curve (AUC).

Modeling options
----------------

Some questions to consider are: Which model will work best for this task? How should you
set up these models? Should you set up completely different models for each task? Let’s
go over the modeling options and try to answer these questions. We will also discuss the
pros and cons of every approach.

Logistic regression
-------------------

Initially, a simple model that makes sense to train is a logistic regression model with
regularization, to predict engagement using the dense features that we discussed in the
feature engineering lesson.

A key advantage of using logistic regression is that it is reasonably fast to train.
This enables you to test new features fairly quickly to see if they make an impact on
the AUC or validation error. Also, it’s extremely easy to understand the model. You can
see from the feature weights which features have turned out to be more important than
others.

A major limitation of the linear model is that it assumes linearity exists between the
input features and prediction. Therefore, you have to manually model feature
interactions. For example, if you believe that the day of the week before a major
holiday will have a major impact on your engagement prediction, you will have to create
this feature in your training data manually. Other models like tree-based and neural
networks are able to learn these feature interactions and utilize them effectively for
predictions.

Another key question is whether you want to train a single classifier for overall
engagement or separate ones for each engagement action based on production needs. In a
single classifier case, you can train a logistic regression model for predicting the
overall engagement on a Tweet. Tweets with any form of engagement will be considered as
positive training examples for this approach.

Another approach is to train separate logistic regression models to predict P(like),
P(comments) and P(retweet). These models will utilize the same features. However, the
assignments of labels to the training examples will differ. Tweets with likes, comments,
or retweets will be considered positive examples for the overall engagement predictor
model. Only Tweets with likes will be considered as positive examples for the “Like”
predictor model. Similarly, only Tweets with comments will be considered as positive
examples for the “Comment” predictor model and only Tweets with retweets will be
considered as positive examples for the “Retweet” predictor model.

MART
----

Another modeling option that should be able to outperform logistic regression with dense
features is additive tree-based models, e.g., Boosted Decision Trees and Random Forest.
Trees are inherently able to utilize non-linear relations between features that aren’t
readily available to logistic regression.

Tree-based models also don’t require a large amount of data as they are able to
generalize well quickly. So, a few million examples should be good enough to give us an
optimized model.

There are various hyperparameters that you might want to play around to get to an
optimized model, including

    - Number of trees

    - Maximum depth

    - Minimum samples needed for split

    - Maximum features sampled for a split

To choose the best predictor, you should do hyperparameter tuning and select the
hyperparameter that minimizes the test error.

Approach 1

A simple approach is to train a single model to predict the overall engagement.

Approach 2

You could have specialized predictors to predict different kinds of engagement. For
example, you can have a like predictor, a comment predictor and a reshare predictor.
Once again these models will utilize the same features. However, the assignments of
labels to the training examples will differ depending on the model’s objective.

Approach 3

Consider a scenario, where a person reshares a Tweet but does not click the like button.
Even though the user didn’t actually click on the like button, retweeting generally
implies that the user likes the Tweet. The positive training example for the retweet
model may prove useful for the like model as well. Hence, you can reuse all positive
training examples across every model.

One way to utilize the overall engagement data among each individual predictor of
P(like), P(comment) and P(retweet) is to build one common predictor, i.e., P(engagement)
and share its output as input into all of your predictors.

To take approach three a notch further, you can use the output of each tree in the
“overall engagement predictor” ensemble as features in the individual predictors. This
allows for even better learning as the individual model will be able to learn from the
output of each individual tree.

Deep learning
-------------

With advancements in computational power and the amount of training data you can gather
from hundreds of million users, deep learning can be very powerful in predicting user
engagement for a given Tweet and showing the user a highly personalized feed.

Having said that, training the model as well as evaluating the model at feed generation
time can make this approach computationally very expensive. So, you may want to fall
back to the multi-layer approach, which we discussed in the search ranking chapter,
i.e., having a simpler model for stage one ranking and use complex stage two model to
obtain the most relevant Tweets ranked at the top of the user’s Twitter feed.

Like with the tree-based approach, there are quite a few hyperparameters that you should
tune for deep learning to find the most optimized model that minimizes the test set
error. They are:

    - Learning rate

    - Number of hidden layers

    - Batch size

    - Number of epochs

    - Dropout rate for regularizing model and avoiding overfitting

Separate neutral networks
-------------------------

One way is to train separate neural nets for each of the P(like), P(comment) and
P(retweet). However, for a very large scale data set, training separate deep neural
networks (NNs) can be slow and take a very long time (ten’s of hours to days).

Multi-task neural networks
--------------------------

Likes, comments, and retweets are all different forms of engagement on a Tweet.
Therefore, predicting P(like), P(comment) and P (retweet) are similar tasks. When
predicting similar tasks, you can use multitask learning. Referring back to the scenario
in approach 3 of MART, if you want to predict the probability of a like, it would
certainly be helpful for the model to know that this Tweet has been retweeted (knowledge
sharing). Hence, you can train a neural network with shared layers (for shared
knowledge) appended with specialized layers for each task’s prediction. The weights of
the shared layers are common to the three tasks. Whereas in the task-specific layer, the
network learns information specific to the tasks. The loss function for this model will
be the sum of individual losses for all the tasks:

total_loss = like_loss + comment_loss + retweet_loss

The model will then optimize for this joint loss leading to regularization and joint
learning.

Given the training time is slow for neural networks, training one model (shared layers)
would make the overall training time much faster. Moreover, this will also allow us to
share all the engagement data across each learning task.

This approach should be able to perform at least as effective as training separate
networks for each task. It should be able to outperform in most cases as we use the
shared data and use it across each predictor. Also, one key advantage of using shared
layers is that models would be much faster to train than training completely separate
deep neural networks for each task.

Stacking models and online learning
-----------------------------------

One way to outperform the “single model technique approach” is to use multiple models to
utilize the power of different techniques by stacking models on top of each other. Let’s
go over one such stacking setup that should work out very well for the feed problem.

The setup includes training tree-based models and neural networks to generate features
that you will utilize in a linear model (logistic regression). The main advantage of
doing this is that you can utilize online learning, meaning we can continue to update
the model with every user action on the live site. You can also use sparse features in
our linear model while getting the power of all non-linear relations and functions
through features generated by tree-based models and neural networks.

For trees, you can generate features by using the triggering of leaf nodes, e.g., given
two trees with four leaf nodes, each will result in eight features that can be used in
logistic regression. Each leaf node in the random forest will result in a boolean
feature that will be active based on whether the leaf node is triggered or not.

Similarly, for neutral networks, rather than predicting the probability of events, you
can just plug-in the output of the last hidden layer as features into the logistic
regression models.

To summarize, this stacking model setup will still give us all the learning power of
deep neural networks and tree-based models along with the flexibility of training
logistic regressions model, while keeping it almost real-time refreshed with online
learning.

Logistic regression can be easily used for changing the model online, based on real-time
user interactions that happen with the tweets. This helps the model to re-learn the
weight of all tree leaves as well.

Another advantage of using real-time online learning with logistic regression is that
you can also utilize sparse features to learn the interaction, e.g., features like
user_id and tweet_id can be used to memorize the interaction with each individual user
and Tweet.

Given that features like tweet_id and user_id are extremely sparse, training and
evaluation of the model must be done in a distributed environment because the data won’t
fit on one machine.
"""
