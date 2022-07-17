"""
Training Data Generation
========================

Training data generation through online user engagement
-------------------------------------------------------

When we show an ad to the user, they can engage with it or ignore it. Positive examples
result from users engaging with ads, e.g., clicking or adding an item to their cart.
Negative examples result from users ignoring the ads or providing negative feedback on
the ad. Advertisers will usually specify which actions to consider as positive vs.
negative.

Suppose the advertiser specifies “click” to be counted as a positive action on the ad.
In this scenario, a user-click on an ad is considered as a positive training example,
and a user ignoring the ad is considered as a negative example.

Suppose the ad refers to an online shopping platform and the advertiser specifies the
action “add to cart” to be counted as positive user engagement. Here, if the user clicks
to view the ad and does not add items to the cart, it is counted as a negative training
example.

Balancing positive and negative training examples
-------------------------------------------------

Users’ engagement with an ad can be fairly low based on the platform e.g. in case of a
feed system where people generally browse content and engage with minimal content, it
can be as low as 2 - 3%. In order to balance the ratio of positive and negative training
samples, we can randomly down sample the negative examples so that we have a similar
number of positive and negative examples.

Model recalibration
-------------------

Negative downsampling can accelerate training while enabling us to learn from both
positive and negative examples. However, our predicted model output will now be in the
downsampling space. For instance, consider that if our engagement rate is 5% and we
select only 10% negative samples, our average predicted engagement rate will be near
33%. Auction uses this predicted rate to determine order and pricing; therefore it’s
critical that we recalibrate our score before sending them to auction. The recalibration
can be done using:

q = p / (p + (1 - p) / w

Here,

q is the re-calibrated prediction score,
p is the prediction in downsampling space,
w is the negative downsampling rate.

Train test split
----------------

We need to be mindful of the fact that user engagement patterns may differ throughout
the week. Hence we will use a week’s engagement to capture all patterns during training
data generation.

Random splitting would result in utilizing future data for prediction given our data has
a time dimension, i.e., we can utilize engagement on historical ads to predict future ad
engagement. Hence we will train the model on data from the one-time interval and
validate it on the data from its succeeding time interval.
"""
