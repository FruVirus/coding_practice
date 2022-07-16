"""
Filtering Results
=================

You may still have to filter out results that might seem relevant for the query but are
inappropriate to show.

Result set after ranking
------------------------

The result set might contain results that:

    - are offensive

    - cause misinformation

    - are trying to spread hatred

    - are not appropriate for children

    - are inconsiderate towards a particular group

These results are inappropriate despite having good user engagement.

ML problem
----------

From a machine learning point of view, we would want to have a specialized model that
removes inappropriate results from our ranked result set. We would need training data,
features, and a trained classifier for filtering these results.

Training data
-------------

Human raters

Human raters can identify content that needs to be filtered. We can collect data from
raters about the above-mentioned cases of misinformation, hatred, etc. and from their
feedback, we can train a classifier that predicts the probability that a particular
document is inappropriate to show on SERP.

Online user feedback

Good websites provide users with the option to report a result in case it is
inappropriate. Therefore, another way to generate data is through this kind of online
user feedback.

Features
--------

We can use the same features for this model that we have used for training our ranker,
e.g., document word embeddings or raw terms can help us identify the type of content on
the document.

There are maybe a few particular features that we might want to add specifically for our
filtering model. For example, website historical report rate, sexually explicit terms
used, domain name, website description, images used on the website, etc.

Building a classifier
---------------------

Once you have built the training data with the right features, you can utilize
classification algorithms like logistic regression, MART, or a Deep neural network to
classify a result as inappropriate.

Similar to the discussion in the ranking section, your choice of the modelling algorithm
will depend on:

    - how much data you have

    - capacity requirements

    - experiments to see how much gain in reducing bad content do we see with that
modelling technique
"""
