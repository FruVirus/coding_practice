"""
Training Data Generation
========================

Training data generation through online user engagement
-------------------------------------------------------

If you are training a single model to predict user engagement, then all the Tweets that
received user engagement would be labeled as positive training examples. Similarly, the
Tweets that only have impressions would be labeled as negative training examples.

Impression: If a Tweet is displayed on a user’s Twitter feed, it counts as an
impression. It is not necessary that the user reads it or engages with it, scrolling
past it also counts as an impression.

You can train different models, each to predict the probability of occurrence of
different user actions on a tweet. When you generate data for the “Like” prediction
model, all Tweets that the user has liked would be positive examples, and all the Tweets
that they did not like would be negative examples.

Balancing positive and negative training examples
-------------------------------------------------

In the feed-based system scenario, on average, a user engages with as little as
approximately 5% of the Tweets that they view per day. Therefore, in order to balance
the ratio of positive and negative training samples, you can randomly downsample:

    - negative examples to five million samples

    - positive examples to five million samples

Now, you would have a total of ten million training examples per day; five million of
which are positive and five million are negative.

If a model is well-calibrated, the distribution of its predicted probability is similar
to the distribution of probability observed in the training data. However, as we have
changed the sampling of training data, our model output scores will not be
well-calibrated. For example, for a tweet that got only 5% engagement, the model might
predict 50% engagement. This would happen because the model is trained on data that has
an equal quantity of negative and positive samples. So the model would think that it is
as likely for a tweet to get engagement as it is to be ignored. However, we know from
the training that this is not the case. Given that the model’s scores are only going to
be used to rank Tweets among themselves, poor model calibration doesn’t matter much in
this scenario.

Train test split
----------------

You need to be mindful of the fact that the user engagement patterns may differ
throughout the week. Hence, you will use a week’s engagement to capture all the patterns
during training data generation.

Random splitting defeats the purpose of training the model on an entire week’s data.
Also, the data has a time dimension, i.e., we know the engagement on previous Tweets,
and we want to predict the engagement on future Tweets ahead of time. Therefore, you
will train the model on data from one time interval and validate it on the data with the
succeeding time interval.
"""
