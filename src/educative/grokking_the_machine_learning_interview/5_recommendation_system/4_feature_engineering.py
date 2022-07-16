"""
Feature Engineering
===================

To start the feature engineering process, we will first identify the main actors in the
movie/show recommendation process:

    1. Logged-in user

    2. Movie/show

    3. Context (e.g., season, time, etc.)

User-based features
-------------------

    - age

    - gender

    - language

    - country

    - average_session_time

    - last_genre_watched

    - user_actor_histogram

    - user_genre_histogram

    - user_language_histogram

Context-based features
----------------------

    - season_of_the_year

    - upcoming_holiday

    - days_to_upcoming_holiday

    - time_of_day

    - day_of_week

    - device

Media-based features
--------------------

    - public-platform-rating

    - revenue

    - time_passed_since_release_date

    - time_on_platform

    - media_watch_history

        - media_watch_history_last_12_hrs

        - media_watch_history_last_24_hrs

    - genre

    - movie_duration

    - content_set_time_period

    - content_tags

    - show_season_number

    - country_of_origin

    - release_country

    - release_year

    - release_type

    - maturity_rating

Media-user cross features
-------------------------

In order to learn the users’ preferences, representing their historical interactions
with media as features is very important. For instance, if a user watches a lot of
Christopher Nolan movies, that would give us a lot of information about what kind of
movies the user likes.

User-genre historical interaction features

    - user_genre_historical_interaction_3months

    - user_genre_historical_interaction_1year

    - user_and_movie_embedding_similarity

    - user_actor

    - user_director

    - user_language_match

    - user_age_match

    - movie_id

    - title_of_media

    - synopsis

    - original_title

    - distributor

    - creator

    - original_language

    - director

    - first_release_year

    - music_composer

    - actors
"""
