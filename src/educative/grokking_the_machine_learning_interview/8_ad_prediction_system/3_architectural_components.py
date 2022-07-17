"""
Architectural Components
========================

Architecture
------------

There will be two main actors involved in our ad prediction system - platform users and
advertiser.

1. Advertiser flow

Advertisers create ads containing their content as well as targeting, i.e., scenarios in
which they want to trigger their ads. A few examples are:

    - Query-based targeting: This method shows ads to the user based on the query terms.
The query terms can be a partial match, full match, expansion, etc.

    - User-based targeting: The ads will be subjective to the user based on a specific
region, demographic, gender, age, etc.

    - Interest-based targeting: This method shows interest-based ads. For example, the
advertiser might like to show sports-related ads to people interested in sports.

    - Set-based targeting: This type shows ads to a set of users selected by the
advertisers. For example, showing an ad to people who were previous buyers or have spent
more than ten minutes on the website.

2. User flow

As the platform user queries the system, it will look for all the potential ads that can
be shown to this user based on different targeting criteria used by the advertiser.

So, the flow of information will have two major steps as described below:

    - Advertisers create ads providing targeting information, and the ads are stored in
the ads index.

    - When a user queries the platform, ads can be selected from the index based on
their information (e.g., demographics, interests, etc.) and run through our ads
prediction system.

Ad selection
------------

The ad selection component will fetch the top k ads based on relevance (subject to the
user context) and bid from the ads index.

Ad prediction
-------------

The ad prediction component will predict user engagement with the ad (the probability
that an action will be taken on the ad if it is shown), given the ad, advertiser, user,
and context. Then, it will rank ads based on relevance score and bid.

Auction
-------

The auction mechanism then determines whether these top K relevant ads are shown to the
user, the order in which they are shown, and the price the advertisers pay if an action
is taken on the ad.

For every ad request, an auction takes place to determine which ads to show. The top
relevant ads selected by the ad prediction system are given as input to Auction. Auction
then looks at total value based on an ad’s bid as well as its relevance score. An ad
with the highest total value is the winner of the auction. The total value depends on
the following factors:

    - Bid: The bid an advertiser places for that ad. In other words, the amount the
advertiser is willing to pay for a given action such as click or purchase.

    - Budget: The advertiser’s budget for an ad

    - User engagement rate: An estimate of user engagement with the ad.

    - Ad quality score: An assessment of the quality of the ad by taking into account
feedback from people viewing or hiding the ad.

The estimated user engagement and ad quality rates combined results in the ad relevance
score. They can be combined based on different weights as selected by the platform,
e.g., if it’s important to keep positive feedback high, the ad quality rate will get a
higher weight.

The rank score is calculated based on predicted ad score (from the ad prediction
component) multiplied by the bid.

Ad rank score = Ad predicted score * bid

Ads with the highest ad rank score wins the auction and are shown to the user. Once an
ad wins the auction, the cost per engagement (CPE) or cost per click (CPC) will depend
on its ad rank score and ad rank score of the ad right below it in rank order, i.e.,

CPE = Ad rank of ad below / Ad rank score + 0.01

A general principle is that the ad will cost the minimal price that still allows it to
win the auction.

Pacing
------

Pacing an ad means evenly spending the ad budget over the selected time period rather
than trying to spend all of it at the start of the campaign.

Remember that whenever the user shows engagement with an ad, the advertiser gets charged
the bid amount of the next ad. If the ad rank score is high, the ad set can spend the
whole budget at the start of a time period (like the start of a new day, as advertisers
generally have daily budgets). This would result in a high cost per click (CPC) when the
ad load (the user engagement rate) is high.

Pacing overcomes this by dynamically changing the bid such that the ad set is evenly
spread out throughout the day and the advertiser gets maximum ROI on their campaign.
This also prevents the overall system from having a significantly high load at the start
of the day, and the budget is spent evenly throughout the campaign.

Training data generation
------------------------

We need to record the action taken on an ad. This component takes user action on the ads
(displayed after the auction) and generates positive and negative training examples for
the ad prediction component.

Funnel model approach
---------------------

For a large scale ads prediction system, it’s important to quickly select an ad for a
user based on either the search query and/or user interests. The scale can be large both
in terms of the number of ads in the system and the number of users on the platform.

To achieve the above objective, it would make sense to use a funnel approach, we
gradually move from a large set of ads to a more precise set for the next step in the
funnel.

As we go down the funnel, the complexity of the models becomes higher and the set of ads
that they run on becomes smaller. It’s also important to note that the initial layers
are mostly responsible for ads selection. On the other hand, ads prediction is
responsible for predicting a well-calibrated engagement and quality score for ads. This
predicted score is going to be utilized in the auction as well.

Let’s go over an example to see how these components will interact for the search
scenario.

    - A thirty-year old male user issues a query “machine learning”.

    - The ads selection component selects all the ads that match the targeting criteria
(user demographics and query) and uses a simple model to predict the ad’s relevance
score.

    - The ads selection component ranks the ads according to r, where
r = bid * relevance and sends the top ads to our ads prediction system.

    - The ads prediction component will go over the selected ads and uses a highly
optimized ML model to predict a precise calibrated score.

    - The ads auction component then runs the auction algorithm based on the bid and
predicted ads score to select the top most relevant ads that are shown to the user.
"""
