"""
Main Takeaways
~~~~~~~~~~~~~~

Problem statement
-----------------

The interviewer has asked you to build a system to show the most relevant ads to users.

Let’s set up the machine learning problem:

    “Predict the probability of engagement of an ad for a given user and context
(query, device, etc.)”

Visualizing the problem
-----------------------

Google’s search network allows advertisers to show their business advertisements to
users who are actively looking for products or services that the advertiser provides.

Unlike Google, Facebook ads are mostly shown on users’ news feed based on users’
interests.

Amazon.com also shows ads, generally in their search result page based on query context
as shown in the picture.

Interview questions
-------------------

The interviewer can ask the following questions about this problem, narrowing the scope
of the question each time.

    - How would you build an ML system to predict the probability of engagement for Ads?
    - How would you build an Ads relevance system for a search engine?
    - How would you build an Ads relevance system for a social network?

Note that the context can be different depending on the type of application in which we
are displaying the advertisement.

There are two categories of applications:

Search engine: Here, the query will be part of the context along with the searcher. The
system will display ads based on the search query issued by the searcher.

Social media platforms: Here, we do not have a query, but the user information (such as
location, demographics, and interests hierarchy) will be part of the context and used to
select ads. The system will automatically detect user interest based on the user’s
historical interactions (using machine learning algorithms) and display ads accordingly.

Most components will be the same for the above two discussed platforms with the main
difference being the context that is used to select and predict ad engagement.

Problem Statement
=================

Problem statement
-----------------

The interviewer has asked you to build a system to show the most relevant ads to users.

Visualizing the problem
-----------------------

There are two well-known advertising platforms Google and Facebook, that run
advertisements paid for by businesses.

Have you ever wondered how Google and Facebook drive new (or existing) customers who are
searching for the product or service that you provide to your website using
advertisements?

When you type a search query in a google.com search bar, ads appear in the search
results.

Google’s search network allows advertisers to show their business advertisements to
users who are actively looking for products or services that the advertiser provides.

Within the Search Network, Google matches a keyword that is relevant to a product or
business advertiser, so that when a user issues a query, it triggers an ad that shows up
on the search page for a user to click on.

Unlike Google, Facebook ads are mostly shown on users’ news feed based on users’
interests.

Amazon.com also shows ads, generally in their search result page based on query context
as shown in the picture.

Interview questions
-------------------

The interviewer can ask the following questions about this problem, narrowing the scope
of the question each time.

    - How would you build an ML system to predict the probability of engagement for Ads?

    - How would you build an Ads relevance system for a search engine?

    - How would you build an Ads relevance system for a social network?

Note that the context can be different depending on the type of application in which we
are displaying the advertisement.

There are two categories of applications:

Search engine: Here, the query will be part of the context along with the searcher. The
system will display ads based on the search query issued by the searcher.

Social media platforms: Here, we do not have a query, but the user information (such as
location, demographics, and interests hierarchy) will be part of the context and used to
select ads. The system will automatically detect user interest based on the user’s
historical interactions (using machine learning algorithms) and display ads accordingly.

Most components will be the same for the above two discussed platforms with the main
difference being the context that is used to select and predict ad engagement.

Let’s set up the machine learning problem:

    “Predict the probability of engagement of an ad for a given user and context
(query, device, etc.)”
"""
