"""
Metrics
=======

The feed-ranking system aims to maximize user engagement.

User actions
------------

The following are some of the actions that the user will perform on their tweet,
categorized as positive and negative actions.

Positive user actions

    - Time spent viewing the tweet

    - Liking a Tweet

    - Retweeting

    - Commenting on a Tweet

Negative user actions

    - Hiding a Tweet

    - Reporting Tweets as inappropriate

Now, you need to look at these different forms of engagements on the feed to see if your
feed ranking system did a good job.

User engagement metrics
-----------------------

User actions on the platform can help generate useful statistics.

Selecting feed optimization metric
----------------------------------

An important thing to understand in selecting a topline is that it’s scientific as well
as a business-driven decision.

The business might want to focus on one aspect of user engagement. For instance, Twitter
can decide that the Twitter community needs to engage more actively in a dialogue. So,
the topline metric would be to focus more on the number of comments on the Tweets. If
the average number of comments per user increases over time, it means that the feed
system is helping the business objective.

Similarly, Twitter might want to shift its focus to overall engagement. Then their
objective will be to increase average overall engagement, i.e., comments, likes, and
retweets. Alternatively, the business may require to optimize for the time spent on the
application. In this case, time spent on Twitter will be the feed system metric.

Negative engagement or counter metric
-------------------------------------

For any system, it’s super important to think about counter metrics along with the key,
topline ones. In a feed system, users may perform multiple negative actions such as
reporting a Tweet as inappropriate, block a user, hide a Tweet, etc. Keeping track of
these negative actions and having a metric such as average negative action per user is
also crucial to measure and track.

Weighted engagement
-------------------

More often than not, all engagement actions are equally important. However, some might
become more important at a particular point in time, based on changing business
objectives. For example, to have an engaged audience, the number of comments might be
more critical rather than just likes. As a result, we might want to have different
weights for each action and then track the overall engagement progress based on that
weighted sum. So, the metric would become a weighted combination of these user actions.
These weights are assigned, keeping in mind the respective importance of different forms
of engagement towards the business objectives.

The user engagements are aggregated across all users’ feeds over a specific period of
time. In the above diagram, two-thousand tweets were viewed in a day on Twitter. There
were a total of seventy likes, eighty comments, twenty retweets, and five reports. The
weighted impact of each of these user engagements is calculated by multiplying their
occurrence aggregate by their weights. In this instance, Twitter is focusing on
increasing “likes” the most. Therefore, “likes” have the highest weight. Note that the
negative user action, i.e., “report”, has a negative weight to cast its negative impact
on the score.

The weighted impacts are then summed up to determine the score. The final step is to
normalize the score with the total number of active users. This way, you obtain the
engagement per active user, making the score comparable. The reason is that the decrease
in score A may just be the effect of less active users (i.e., five-hundred active users
instead of one-hundred active users).
"""
