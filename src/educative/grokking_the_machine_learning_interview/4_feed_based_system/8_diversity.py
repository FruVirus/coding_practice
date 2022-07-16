"""
Diversity
=========

Why do you need diverse Tweets?
-------------------------------

Consider a scenario where the sorted list of Tweets has five consecutive posts by the
same author. No, your ranking model hasn’t gone bonkers! It has rightfully placed these
tweets at the top because:

    - The logged-in user and the Tweet’s author have frequently interacted with each
other’s Tweets

    - The logged-in user and the Tweet’s author have a lot in common like hashtags
followed and common followees

    - The author is very influential, and their Tweets generally gain a lot of traction

Diversity in Tweets’ authors
----------------------------

However, no matter how good of a friend the author is or how interesting their Tweets
might be, user A would eventually get bored of seeing Tweets from the same author
repeatedly. Hence, you need to introduce diversity with regards to the Tweets’ author.

Diversity in tweets’ content
----------------------------

Another scenario where we might need to introduce diversity is the Tweet’s content. For
instance, if your sorted list of Tweets has four consecutive tweets that have videos in
them, the user might feel that their feed has too many videos.

Introducing the repetition penalty
----------------------------------

One way to introduce a repetition penalty could be to add a negative weight to the
Tweet’s score upon repetition. For instance, whenever you see the author being repeated,
you add a negative weight of -0.1 to the Tweet’s score.

Another way to achieve the same effect is to bring the Tweet with repetition three steps
down in the sorted list. For instance, when you observe that two consecutive Tweets have
media content in them, you bring the latter down by three steps.
"""
