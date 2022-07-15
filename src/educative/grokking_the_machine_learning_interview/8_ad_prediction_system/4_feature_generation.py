"""
Main Takeaways
~~~~~~~~~~~~~~

The main actors that t will play a key role in our feature engineering process are:

    1. Ad
    2. Advertiser
    3. User
    4. Context. Context refers to the engagement history, user interests, current
location, time and date, etc.

Features for the model
----------------------

The features would fall into the following categories:

    1, Ad specific features
    2. Advertiser specific features
    3. User specific features
    4. Context specific features
    5. User-ad cross features
    6. User-advertiser cross features

Ad specific features
--------------------

    - ad_id
    - ad_content_raw_terms
    - historical_engagement_rate
        - ad_engagement_history_last_24_hrs
        - ad_engagement_history_last_7_days
    - ad_impression
    - ad_negative_engagement_rate
    - ad_embedding
    - ad_age
    - ad_bid

Advertiser specific features
----------------------------

    - advertiser_domain
    - historical_engagement_rate
    - region_wise_engagement

User specific features
----------------------

    - user_previous_search_terms
    - user_search_terms
    - age
    - gender
    - language
    - embedding_last_k_ads
    - engagement_content_type
    - engagement_days
    - platform_time_spent
    - region

Context specific features
-------------------------

    - current_region
    - time
    - device
        - screen_size

User-ad cross features
----------------------

    - embedding_similarity
    - region_wise_engagement
    - user_ad_category_histogram
    - user_ad_subcategory_histogram
    - user_gender_ad_histogram
    - user_age_ad_histogram

User-advertiser cross features
------------------------------

    - embedding_similarity
    - user_gender_advertiser_histogram
    - user_age_advertiser_histogram

Key consideration for historical engagement features
----------------------------------------------------

There are two ways to pass historical data that is partitioned on a specific key (such
as day, age, gender, etc.) as features to our models.

The first approach is to give the histogram data along with the key value to the model
for learning. For example, in the case of daily historical engagement rate, we will give
the model a histogram of seven-day user engagement from Sunday to Monday, which looks
like [0.4, 0.2, 0.21, 0.25, 0.27, 0.38, 0.42]. In addition, we will pass the current day
as a feature as well, e.g., if the day is Sunday the feature value of day will be 1, and
for Saturday the feature value will be 7. So, the model will see eight features in
total: seven more raw features for each day historical engagement rate and one feature
for the current day of the week.

The second approach for giving this historical information to our model is to create a
single feature that gives the current day engagement rate as a value, e.g., the feature
value on Sunday will be 0.4, and on Friday it will be 0.38 for the above data.

It would be better to create features for learning by using both the first and second
approaches. The models that are able to learn feature interactions effectively (such as
neural networks or decision trees) can learn the current day engagement rate by the
features described in the first approach. They might also be able to learn more
interesting patterns such as understanding weekend data interactions, previous day
interactions, etc. However, it’s better to provide the full histogram data for the model
to learn new interactions for us. But, for linear models providing the current day
engagement data as we did in the second approach is critical because they can’t learn
these interactions on their own.

Feature Engineering
===================

Features are the backbone of any learning system. Let’s think about the main actors or
dimensions that will play a key role in our feature engineering process.

    1. Ad

    2. Advertiser

    3. User

    4. Context. Context refers to the engagement history, user interests, current
location, time and date, etc.

Features for the model
----------------------

Now it’s time to generate features based on these actors. The features would fall into
the following categories:

    1, Ad specific features

    2. Advertiser specific features

    3. User specific features

    4. Context specific features

    5. User-ad cross features

    6. User-advertiser cross features

Ad specific features
--------------------

    - ad_id

    A unique id is assigned to each ad and can be used as a sparse feature. Utilizing
ad_id as a sparse feature allows the model to memorize historical engagement for each
ad, and it can also be used in interesting cross features for memorization (such as
ad_id * user interests). Additionally, we can also generate embeddings during training
time for the ad using its id.

    - ad_content_raw_terms

    Ad terms can also be very useful sparse features. They can tell us a lot about the
ad, e.g., a good model can learn from the text’s content to identify what the ad is
about, such as politics or sports. Raw terms allow the models (especially NN models) to
learn such behavior from given raw terms.

    - historical_engagement_rate

    This feature specifies the rate of user engagement with the ad. Here we will measure
engagement in different windows such as different times of the day or days of the week.
For instance, we can have the following features:

        - ad_engagement_history_last_24_hrs

        Since ads are short-lived, recent engagement is important. This feature captures
the most recent engagement with the ad.

        - ad_engagement_history_last_7_days

    This captures the activity on the ad on each day of the week. For example, an ad can
get more engagement on weekends rather than on weekdays. This feature can tell the model
that a particular ad is performing well. This prior engagement data can help predict
future engagement behavior.

    - ad_impression

    This feature records the number of times an ad is viewed. This is helpful since we
can train the model on the engagement rate as a feature when we have a reasonable number
of ad impressions. We can select the cut-off point until which we want to consider the
impressions. For example, we can say that if a particular ad has twenty impressions, we
can measure the historical engagement rate.

    - ad_negative_engagement_rate

    This feature keeps a record of negative engagement (hide, report) with the ad.

    - ad_embedding

    We can generate embedding for an ad given all the data that we know about it e.g. ad
terms and engagement data. This embedding is then a dense representation of the ad that
can be used in modeling. Ad embedding can also be used to detect the ad’s category,
e.g., it can tell if the ad belongs to sports, etc.

    - ad_age

    This feature specifies how old the ad is.

    - ad_bid

    We can record the bid for the ad specified by the advertiser.

Advertiser specific features
----------------------------

    - advertiser_domain

    This is a sparse feature that keeps a record of the domain name for an advertiser.
This can be used in the same way for memorization and embedding generation as discussed
for ad_id.

    - historical_engagement_rate

    This feature specifies the ratio of user engagement with ads posted by a particular
advertiser.

    - region_wise_engagement

    The system should learn to show ads specific to a region from the histogram of
engagement based on region. From an advertiser’s perspective, the ad posted by an
advertiser can be restricted to a specific region based on the ad content.

    For example, an American football ad posted by the advertiser will be most relevant
to people living in the United States. This relevance can be predicted using the given
histogram of engagement between the users and the ad.

User specific features
----------------------

    - user_previous_search_terms

    This sparse feature specifies what users have searched in the past. This helps in
recommending ads based on past user preferences.

    - user_search_terms

    This sparse feature keeps a record of the user’s search query terms.

    - age

    This feature records the age of the user. It allows the model to learn the kind of
ad that is appropriate according to different age groups.

    - gender

    The model learns about gender-based preferences.

    - language

    This feature records the language of the user.

    - embedding_last_k_ads

    The model will learn about the interest of the user using the history of the user’s
activity on the last k ads that were shown. We can make one embedding by combining
embedding vectors of the last k ads that the user engaged with.

    - engagement_content_type

    This takes into account the content of the ad that the user engages with. Here, we
can track which type of ad a user plays around with, such as a video or an image ad.

    - engagement_days

    This feature captures the user activity on each day of the week. For example, the
user might be more active on weekends rather than on weekdays.

    - platform_time_spent

    This feature captures how long the user has been on the platform. This can be useful
because we can show a different ad set to the user every hour to maximize their
engagement with the ad.

    - region

    This feature records the country of the user. Users from different geographical
regions have different content preferences. This feature can help the model learn
regional preferences and tune the recommendations accordingly.

Context specific features
-------------------------

    - current_region

    This feature keeps track of the geographical location of the user. Note that the
context may change if the user travels to other parts of the world. The system should
learn the context of the user and show ads accordingly.

    - time

    This feature will show ads subject to time of the day. The user would be able to see
a different set of ads appear throughout the day.

    - device

    It can be beneficial to observe the device a person is using to view content on. A
potential observation could be that a user tends to watch content for shorter bursts on
their mobile. However, they usually choose to watch on their laptop when they have more
free time, so they watch for longer periods consecutively.

        - screen_size

        The size of the screen is an important feature because if the users are using a
device with a small screen size, there is a possibility that ads are actually never seen
by the users. This is because they don’t scroll far down enough to bring the ads
in-view.

User-ad cross features
----------------------

    - embedding_similarity

    Here, we can generate vectors for the user’s interest and the ad’s content. We can
generate embedding vectors for ads based on their content and for the user based on
their interactions with the ad. A dot product between these vectors can be calculated to
measure their similarity. A high score would equate to a highly relevant ad for the
user.

    For example, the ad is about tennis and the user is not interested in tennis.
Therefore, this feature will have a low similarity score.

    - region_wise_engagement

    An ad engagement radius can be another important feature. For example, the ad-user
histogram below shows that an American Football ad is mostly viewed by people living in
America.

    - user_ad_category_histogram

    This feature observes user engagement on an ad category using a histogram plot
showing user engagement on an ad category.

    - user_ad_subcategory_histogram

    This feature observes user engagement on an ad subcategory using a histogram plot
that shows user engagement on an ad subcategory.

    - user_gender_ad_histogram

    Some ads can be more appealing to a specific gender. This similarity can be
calculated by making a histogram plot showing user engagement gender-wise on an ad.

    - user_age_ad_histogram

    An ad_age histogram can be used to predict user age-wise engagement.

User-advertiser cross features
------------------------------

    - embedding_similarity

    We can project the advertisement and user in the same embedding space to see how
close they are. From the embedding similarity score, we can figure out the type of ads
the advertiser shows, and whether the user clicks on those types of ads.

    - user_gender_advertiser_histogram

    This feature observes gender-wise user engagement on an ad posted by an advertiser
using a histogram plot. For example, the advertiser’s ad for male clothing might be more
engaging for men than women.

    - user_age_advertiser_histogram

    This feature observes age-wise user engagement on an ad posted by an advertiser
using a histogram plot. For example, a young audience might demonstrate a greater
inclination towards the advertiser’s ad on pop music.

Key consideration for historical engagement features
----------------------------------------------------

There are two ways to pass historical data that is partitioned on a specific key (such
as day, age, gender, etc.) as features to our models.

The first approach is to give the histogram data along with the key value to the model
for learning. For example, in the case of daily historical engagement rate, we will give
the model a histogram of seven-day user engagement from Sunday to Monday, which looks
like [0.4, 0.2, 0.21, 0.25, 0.27, 0.38, 0.42]. In addition, we will pass the current day
as a feature as well, e.g., if the day is Sunday the feature value of day will be 1, and
for Saturday the feature value will be 7. So, the model will see eight features in
total: seven more raw features for each day historical engagement rate and one feature
for the current day of the week.

The second approach for giving this historical information to our model is to create a
single feature that gives the current day engagement rate as a value, e.g., the feature
value on Sunday will be 0.4, and on Friday it will be 0.38 for the above data.

It would be better to create features for learning by using both the first and second
approaches. The models that are able to learn feature interactions effectively (such as
neural networks or decision trees) can learn the current day engagement rate by the
features described in the first approach. They might also be able to learn more
interesting patterns such as understanding weekend data interactions, previous day
interactions, etc. However, it’s better to provide the full histogram data for the model
to learn new interactions for us. But, for linear models providing the current day
engagement data as we did in the second approach is critical because they can’t learn
these interactions on their own.
"""
