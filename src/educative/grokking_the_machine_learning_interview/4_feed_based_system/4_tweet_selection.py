"""
Tweet Selection
===============

Tweet selection is dynamic in nature. The Tweets selected will continue to change each
time.

New Tweets
----------

Consider the following scenario to see how Tweet selection occurs.

User A logs in to Twitter at 9 am to view their Twitter feed. Now, the Tweet selection
component has to fetch Tweets for display. It fetches the five-hundred newly generated
Tweets by A’s network since the last login at 3 pm yesterday.

New Tweets + unseen Tweets
--------------------------

The new Tweets fetched in the previous step are ranked and displayed on user A’s feed.
They only view the first two-hundred Tweets and log out. The ranked results are also
stored in a cache.

Now, user A logs in again at 10 pm. According to the last scheme, the Tweet selection
component should select all the new Tweets generated between 9 am and 10 pm. However,
this may not be the best idea!

For 9am’s feed, the component previously selected a Tweet made at 8:45 am. Since this
Tweet was recently posted, it did not have much user engagement at that time. Therefore,
it was ranked at the 450th position in the feed. Now, remember that A logged out after
only viewing the first two-hundred Tweets and this Tweet remained unread. Since the
user’s last visit, this unread Tweet gathered a lot of attention in the form of
reshares, likes, and comments. The Tweet selection component should now reconsider this
Tweet’s selection. This time it would be ranked higher, and A will probably view it.

Keeping the above rationale in mind, the Tweet selection component now fetches a mix of
newly generated Tweets along with a portion of unseen Tweets from the cache.

Edge case: User returning after a while
---------------------------------------

Consider a scenario, where user A might log in after two weeks. A lot of Tweets would
have been generated since A’s last login. Therefore, the Tweet selection component will
impose a limit on the Tweet data it will select. The main focus is that the pool of
Tweets keeps on increasing so a limit needs to be imposed on the number of Tweets that
the component will fetch.

Network Tweets + interest / popularity-based Tweets
---------------------------------------------------

There could be Tweets outside of user A’s network that have a high potential of engaging
them. Hence, we arrive at a two-dimensional scheme of selecting network Tweets and
potentially engaging Tweets.

An engaging Tweet could be one that:

    - aligns with user A’s interests

    - is locally/globally trending

    - engages user A’s network

Selecting these Tweets can prove to be very beneficial in two cases:

    1. The user has recently joined the platform and follows only a few others. As such,
their small network is not able to generate a sufficient number of Tweets for the Tweet
selection component (known as the Bootstrap problem).

    2. The user likes a Tweet from a person outside of his network and decides to add
them to their network. This would increase the discoverability on the platform and help
grow the user’s network.
"""
