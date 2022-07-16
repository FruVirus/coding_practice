"""
Architectural Components
========================

Tweet selection
---------------

This component performs the first step in generating a user’s feed, i.e., it fetches a
pool of Tweets from the user’s network (the followees), since their last login. This
pool of Tweets is then forwarded to the ranker component.

Ranker
------

The ranker component will receive the pool of selected Tweets and predict their
probability of engagement. The Tweets will then be ranked according to their predicted
engagement probabilities for display on user A’s feed. We can:

    1. Train a single model to predict the overall engagement on the tweet.

    2. Train separate models. Each model can focus on predicting the occurrence
probability of a certain user action for the tweet. There will be a separate predictor
for like, comment, time spent, share, hide, and report. The results of these models can
be merged, each having a different weight/importance, to generate a rank score. The
Tweets will then be ranked according to this score.

Separately predicting each user action allows us to have greater control over the
importance we want to give to each action when calculating the rank of the Tweet. We can
tweak the weights to display Tweets in such a manner that would align with our current
business objectives, i.e., give certain user actions higher/lower weight according to
the business needs.

Training data generation
------------------------

Each user engagement action on the Twitter feed will generate positive and negative
training examples for the user engagement prediction models.
"""
