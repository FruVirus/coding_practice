"""
Metrics
=======

Types of metrics
----------------

If a model performs well in an offline test but not in the online test, we need to think
about where we went wrong. For instance, we need to consider whether our data was biased
or whether we split the data appropriately for train and test.

Driving online metrics in the right direction is the ultimate goal of the recommendation
system.

Online metrics
--------------

Engagement rate

The success of the recommendation system is directly proportional to the number of
recommendations that the user engages with. So, the engagement rate
(sessions with clicks / total number of sessions) can help us measure it. However, the
user might click on a recommended movie but does not find it interesting enough to
complete watching it. Therefore, only measuring the engagement rate with the
recommendations provides an incomplete picture.

Videos watched

To take into account the unsuccessful clicks on the movie/show recommendations, we can
also consider the average number of videos that the user has watched. We should only
count videos that the user has spent at least a significant time watching (e.g., more
than two minutes).

However, this metric can be problematic when it comes to the user starting to watch
movie/series recommendations but not finding them interesting enough to finish them. So
just measuring the average number of videos watched might miss out on overall user
satisfaction with the recommended content.

Session watch time

Session watch time measures the overall time a user spends watching content based on
recommendations in a session. The key measurement aspect here is that the user is able
to find a meaningful recommendation in a session such that they spend significant time
watching it.

Offline metrics
---------------

The purpose of building an offline measurement set is to be able to evaluate our new
models quickly. Offline metrics should be able to tell us whether new models will
improve the quality of the recommendations or not.

Can we build an ideal set of documents that will allow us to measure recommendation set
quality? One way of doing this could be to look at the movies/series that the user has
completely watched and see if your recommendation system gets it right using historical
data. Once we have the set of movies/series that we can confidently say should be on the
user’s recommendation list, we can use the following offline metrics to measure the
quality of your recommendation system.

mAP @ N

One such metric is the Mean Average Precision (mAP @ N), where N is the length of the
recommendation list.

P = number of relevant recommendations / total number of recommendations

We can observe that precision alone does not reward the early placement of relevant
items on the list. However, if we calculate the precision of the subset of
recommendations up until each position, k (k = 1 to N), on the list and take their
weighted average, we will achieve our goal. Let’s see how.

Assume the following:

    1. The system recommended N = 5 movies.

    2. The user watched three movies from this recommendation list and ignored the other
two.

    3. Among all the possible movies that the system could have recommended (available
on the Netflix platform), only m = 10 are actually relevant to the user (historical
data).

We would then calculate the precision at each value of k.

Now to calculate the average precision (AP), we have the following formula:

AP @ N = (1 / m) * sum(P(k) * rel(k)), where rel(k) tells us whether that kth item is
relevant (1) or not (0).

Here, we see that P(k) only contributes to AP if the recommendation at position k is
relevant. Also, observe the “placement legalization” by AP by the following scores of
three different recommendation lists:

User interaction with recommendation	Precision @ k	AP @ 3
[1 0 0]	                                [1/1 1/2 1/3]	(1/10) * (1/1) = 0.1
[0 1 0]	                                [0/1 1/2 1/3]	(1/10) * (1/2) = 0.05
[0 0 1]	                                [0/1 0/2 1/3]	(1/10) * (1/3) = 0.03

Note that a true positive (1), down the recommendation list, leads to low a mAP compared
to the one that is high up in the list. This is important because we want the best
recommendations to be at the start of the recommendation set.

Lastly, the “mean” in mAP means that we will calculate the AP with respect to each
user’s ratings and take their mean. So, mAP computes the metric for a large set of users
to see how the system performs overall on a large set of users.

mAR @ N

Another metric that rewards the previously mentioned points is called Mean Average
Recall (mAR @ N). It works similar to mAP @ N. The difference lies in the use of recall
instead of precision.

R = number of relevant recommendations / total number of all possible relevant items

We will use the same recommendation list as used in the mAP @ K example, where N = 5 and
m = 10. Let’s calculate the recall of recommendation subsets up to each position, k.

The average recall (AR) will then be calculated as follows:

AR @ N = (1 / m) * sum(R(k) * rel(k)), where rel(k) tells us whether that kth item is
relevant (1) or not (0).

Lastly, the “mean” in mAR means that we will calculate AR with respect to each user’s
ratings and then take their mean.

So, mAR at a high-level, measures how many of the top recommendations (based on
historical data) we are able to get in the recommendation set.

F1 score

If you want to give equal importance to precision and recall, you need to look for a
score that conveys the balance between precision and recall.

mAP @ N focuses on how relevant the top recommendations are, whereas mAR @ N shows how
well the recommender recalls all the items with positive feedback, especially in its top
recommendations. You want to consider both of these metrics for the recommender. Hence,
you arrive at the final metric “F1 score”.

F1 score = (2 * mAR * mAP) / (mAR + mAP)

So, the F1 score based on mAP and mAR will be a fairly good offline way to measure the
quality of your models.

Offline metric for optimizing ratings
-------------------------------------

We established above that we optimize the system for implicit feedback data. However,
what if the interviewer says that you have to optimize the recommendation system for
getting the ratings (explicit feedback) right. Here, it makes sense to use root mean
squared error (RMSE) to minimize the error in rating prediction.

RMSE = sqrt((1 / N) * sum(y_hat_i - y_i) ^ 2)

y_hat_i is the recommendation system’s predicted rating for the movie, and y_i is the
ground truth rating actually given by the user. The difference between these two values
is the error. The average of this error is taken across N movies.
"""
