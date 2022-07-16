"""
Feature Engineering
===================

The machine learning model is required to predict user engagement on user A’s Twitter
feed.

Let’s begin by identifying the four main actors in a twitter feed:

    1. The logged-in user

    2. The Tweet

    3. Tweet’s author

    4. The context

Dense features
--------------

User-author features
--------------------

These features are based on the logged-in user and the Tweet’s author. They will capture
the social relationship between the user and the author of the Tweet, which is an
extremely important factor in ranking the author’s Tweets. For example, if a Tweet is
authored by a close friend, family member, or someone that user is highly influenced by,
there is a high chance that the user would want to interact with the Tweet.

User-author historical interactions
    - author_liked_posts_3months

    - author_liked_posts_count_1year

User-author similarity

Another immensely important feature set to predict user engagement focuses on figuring
out how similar the logged-in user and the Tweet’s author are.
    - common_followees

    - topic_similarity

        - followed by the logged-in user and author

        - present in the posts that the logged-in user and author have interacted with
in the past

        - used by the author and logged-in user in their posts

    - tweet_content_embedding_similarity. A user is represented by the content that they
have generated and interacted with in the past. You can utilize all of that content as a
bag-of-words and build an embedding for every user. With an embedding vector for each
user, the dot product between them can be used as a fairly good estimate of
user-to-author similarity.

    - social_embedding_similarity. Another way to capture the similarity between the
user and the author is to generate embeddings based on the social graph rather than
based on the content of Tweets. The basic notion is that people who follow the same or
similar topics or influencers are more likely to engage with each other’s content. A
basic way to train this model is to represent each user with all the other users and
topics (user and topic ids) that they follow in the social graph. Essentially, every
user is represented by bag-of-ids (rather than bag-of-words), and you use that to train
an embedding model. The user-author similarity will then be computed between their
social embeddings and used as a signal.

User-Tweet features
-------------------

The similarity between the user’s interests and the tweet’s topic is also a good
indicator of the relevance of a Tweet.

    - topic_similarity. You can use the hashtags and/or the content of the Tweets that
the user has either Tweeted or interacted with, in the last six months and compute the
TF-IDF similarity with the Tweet itself. This indicates whether the Tweet is based on a
topic that the user is interested in.

    - embedding_similarity. Another option to find the similarity between the user’s
interest and the Tweet’s content is to generate embeddings for the user and the Tweet.
The Tweet’s embedding can be made based on the content and hashtags in it. While the
user’s embedding can be made based on the content and hashtags in the Tweets that they
have written or interacted with.

Author features
---------------

Author’s degree of influence
    - is_verified

    - author_social_rank

    - author_num_followers

    - follower_to_following_ratio

        1. The type of user account

        2.The account’s influence

        3. The quality of the account’s content (Tweets)

Historical trend of interactions on the author’s Tweets
-------------------------------------------------------

Another very important set of features is the interaction history on the author’s
Tweets. If historically, an author’s Tweets garnered a lot of attention, then it is
highly probable that this will happen in the future, too. A high rate of historical
interaction for a user implies that the user posts high-quality content.


    - author_engagement_rate_3months

    - author_topic_engagement_rate_3months

Tweet features
--------------

Features based on Tweet’s content

    - Tweet_length

    - Tweet_recency

    - is_image_video

    - is_URL

        1. Calls for action

        2. Provides valuable information

Features based on Tweet’s interaction

Tweets with a greater volume of interaction have a higher probability of engaging the
user.

    - num_total_interactions

    We can apply a simple time decay model to weight the latest interaction more than
the ones that happened some time ago. Time decay can be used in all features where there
is a decline in the value of a quantity over time. One simple model can be to weight
every interaction (like, comment, and retweet) by 1 / (t + 1), where t is the number of
days from current time.

    Another remedy is to use different time windows to capture the recency of
interactions while looking at their numbers. The interaction in each window can be used
as a feature:

    - interactions_in_last_1_hour

    - interactions_in_last_1_day

Separate features for different engagements

    - likes_in_last_3_days

    - comments_in_last_1_day

    - reshares_in_last_2_hours

    - likes_in_last_3_days_user’s_network_only

    - comments_in_last_1_day_user’s_network_only

    - reshares_in_last_2_hours_user’s_network_only

Context-based features
----------------------

    - day_of_week

    - time_of_day

    - current_user_location

    - season

    - lastest_k_tag_interactions

    - approaching_holiday

Sparse features
---------------

    - unigrams/bigrams of a Tweet. The presence of certain unigrams or bigrams may
increase the probability of engagement for a tweet. For example, during data
visualisation, you may observe that Tweets with the bigram “Order now” have higher user
engagement. The reason behind this might be that such Tweets are useful and informative
for users as they redirect them towards websites where they can purchase things
according to their needs.

    - user_id

    - tweets_id
"""
