"""
Feature Engineering
===================

The main actors that will play a key role in our feature engineering process are:

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
"""
