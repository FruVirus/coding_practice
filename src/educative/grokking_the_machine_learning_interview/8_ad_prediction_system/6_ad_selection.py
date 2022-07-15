"""
Main Takeaways
~~~~~~~~~~~~~~

The main goal of the ads selection component is to narrow down the set of ads that are
relevant for a given query.

In a search-based system, the ads selection component is responsible for retrieving the
top relevant ads from the ads database (built using all the active ads in the system)
according to the user and query context.

In a feed-based system, the ads selection component will select the top k relevant ads
based more on user interests than search terms.

It would make sense to structure the ad selection process in the following three phases:

    - Phase 1: Quick selection of ads for the given query and user context according to
selection criteria
    - Phase 2: Rank these selected ads based on a simple and fast algorithm to trim ads.
    - Phase 3: Apply the machine learning model on the trimmed ads to select the top
ones.

Phase 1: Selection of ads
-------------------------

The first key requirement to be able to achieve the quick selection objective is to have
the ads stored in a system that is fast and enables complex selection criteria. This is
where building an in-memory index to store the ads will be massively helpful. Index
allows us to fetch ads quickly based on different targeting and relevance information
from the user. We will index ads on all possible indexing terms that can be used for
selection e.g. targeted terms, city, state, country, region, age etc.

Let’s take an example of a search ads system to explain this concept further. Let’s say
that a male user, aged twenty-five, and located in San Francisco, California is
searching stuff related to machine learning. He types in a query “machine learning”. In
this case, we would want to select all potential ads that we can show to the user, i.e.,
the ads targeting criteria matches the user’s profile.

The selection query in this case will look like:

    (term = "machine learning")
            and
    (age = "\*" or age contains "25")
            and
    (gender = "\*" or gender = "male")
            and
            ...
            and
    (has_budget = True)

In a feed-based system, the selection of ads will base more on user interests rather
than search terms. Let’s assume that the same user is interested in Computer science and
football, and we want to now fetch ads for his feed. The selection query will look like
the following:

    (interest = "Computer Science" or interest = "Football" or interest = "*")
            and
    (age = "\*" or age contains "25")
            and
    (gender = "\*" or gender = "male")
            and
            ...
            and
    (has_budget = True)

Phase 2: Narrow down selection set to top relevant ads
------------------------------------------------------

The eventual ranking of ads is going to be based on (bid * predicted score). We already
know the bid at this point and can use the prior engagement score (CPE) based on the ad,
advertiser, ad type, etc. as our predicted score basd on priors:

Ad Score Based on Prior = Bid * Prior CPE Score

For a new ad or advertiser where the system doesn’t have good prior scores, a slightly
higher score can be given to ads also called score boost. We can use time decay to
reduce it. The ranking might look like the following with a new ad boost of 10% to CPE
score for the first forty-eight hours of ad with time decay.

if ad_age < 48:
    boost = 0.1 * (1 - ad_age / 48)
    ad_score =  bid * (1 + boost) * Prior CPE Score

Phase 3: Ranking of selected ads using a simplistic model
---------------------------------------------------------

As the ranking in phase 2 is super simplistic, we should still select a sizable ads
(e.g., ten thousand) by running a better model as we work towards reducing the ad set.
We can run a simplistic and efficient model on ads selected in phase 2 to further narrow
it down. The top ads from this phase will be passed to our ad prediction stage to run
more complex and accurate models for better user engagement prediction.

We can use either logistic regression or additive trees based models (such as random
forest or boosted decision trees) as they are quite efficient. Neural network-based
models need more capacity and time so they might not be the best choice at this stage.

The target is to select the top k relevant ads from the set given by phase 2. We will
use training data and dense features to train this model to predict engagement scores
better and minimize our log loss error.

At evaluation time, we will get a new predicted engagement score for ranking of ads. Ads
will be sorted based on this prediction CPE as we did in phase 2. However, our predicted
CPE score should be a far better prediction than using historical priors as we did in
phase 2.

How does the system scale?
--------------------------

Note that our index is sharded, i.e., it runs on multiple machines and every machine
selects the top k ads based on the prior score. Each machine then runs a simplistic
logistic regression model built on dense features (there are no sparse features to keep
the model size small) to rank ads.

The number of partitions (shards) depends on the size of the index. A large index
results in more partitions as compared to a smaller index. Also, the system load
measured in queries per second (QPS) decides how many times the partition is replicated.

Consider a scenario where the size of the index is 1 tera-byte and memory of a single
shard is 250 giga-bytes. The index data gets distributed in four partitions. Each
partition selects ads that satisfy the selection criteria. Then, we use the prior score
of the selected ads and select top five-hundred ads based on that score. To further
narrow down the ad set, we run logistic regression which returns the top 50 ads. The top
fifty ranked ads from each of the four partitions (200 ads in total) are fed to the ad
prediction component.

Note that for each level we are selecting top “k” ads. The selection of the number “k”
for each level is very arbitrary. It is based on experimentation and system available
load/capacity.

Ad Selection
============

The main goal of the ads selection component is to narrow down the set of ads that are
relevant for a given query. In a search-based system, the ads selection component is
responsible for retrieving the top relevant ads from the ads database (built using all
the active ads in the system) according to the user and query context. In a feed-based
system, the ads selection component will select the top k relevant ads based more on
user interests than search terms.

Based on our discussions about the funnel-based approach for modeling, it would make
sense to structure the ad selection process in the following three phases:

    - Phase 1: Quick selection of ads for the given query and user context according to
selection criteria

    - Phase 2: Rank these selected ads based on a simple and fast algorithm to trim ads.

    - Phase 3: Apply the machine learning model on the trimmed ads to select the top
ones.

Phase 1: Selection of ads
-------------------------

Advertising platforms can have hundreds of millions of active ads. Our main motivation
in this phase is to quickly reduce this space from millions of ads to one ad that can be
shown to the current user in the given context (e.g. for a user searching “machine
learning” on a mobile device).

The first key requirement to be able to achieve the quick selection objective is to have
the ads stored in a system that is fast and enables complex selection criteria. This is
where building an in-memory index to store the ads will be massively helpful. Index
allows us to fetch ads quickly based on different targeting and relevance information
from the user. This is similar to our Search system discussion, where we had to
similarly select documents quickly at the selection time to narrow our focus to relevant
documents. We will index ads on all possible indexing terms that can be used for
selection e.g. targeted terms, city, state, country, region, age etc.

Let’s take an example of a search ads system to explain this concept further. Let’s say
that a male user, aged twenty-five, and located in San Francisco, California is
searching stuff related to machine learning. He types in a query “machine learning”. In
this case, we would want to select all potential ads that we can show to the user, i.e.,
the ads targeting criteria matches the user’s profile.

The selection query in this case will look like:

    (term = "machine learning")
            and
    (age = "\*" or age contains "25")
            and
    (gender = "\*" or gender = "male")
            and
            ...
            and
    (has_budget = True)

In a feed-based system, the selection of ads will base more on user interests rather
than search terms. Let’s assume that the same user is interested in Computer science and
football, and we want to now fetch ads for his feed. The selection query will look like
the following:

    (interest = "Computer Science" or interest = "Football" or interest = "*")
            and
    (age = "\*" or age contains "25")
            and
    (gender = "\*" or gender = "male")
            and
            ...
            and
    (has_budget = True)

So, the above selection criteria in phase 1 will reduce our space set from all active
ads to ads that are targeted for the current user.

Phase 2: Narrow down selection set to top relevant ads
------------------------------------------------------

The number of ads selected in phase 1 can be quite large depending on the query and the
user, e.g., we can have millions of ads targeted for a sports fan. So, running a complex
ML model to predict engagement on all these selected ads will be slow and expensive. At
this point, it makes sense to narrow down the space using a simplistic approach before
we start running complex models.

The eventual ranking of ads is going to be based on (bid * predicted score). We already
know the bid at this point and can use the prior engagement score (CPE) based on the ad,
advertiser, ad type, etc. as our predicted score:

Ad Score = Bid * Prior CPE Score

For a new ad or advertiser where the system doesn’t have good prior scores, a slightly
higher score can be given to ads also called score boost. We can use time decay to
reduce it. The ranking might look like the following with a new ad boost of 10% to CPE
score for the first forty-eight hours of ad with time decay.

if ad_age < 48:
    boost = 0.1 * (1 - ad_age / 48)
    ad_score =  bid * (1 + boost) * CPE

Based on these prior scores, we can narrow down ads from our large selected set to the
top k ads. In phase 3, we will use a much stronger predictor than prior scores on the
top selected ads from phase 2.

Phase 3: Ranking of selected ads using a simplistic model
---------------------------------------------------------

As the ranking in phase 2 is super simplistic, we should still select a sizable ads
(e.g., ten thousand) by running a better model as we work towards reducing the ad set.
We can run a simplistic and efficient model on ads selected in phase 2 to further narrow
it down. The top ads from this phase will be passed to our ad prediction stage to run
more complex and accurate models for better user engagement prediction.

We can use either logistic regression or additive trees based models (such as random
forest or boosted decision trees) as they are quite efficient. Neural network-based
models need more capacity and time so they might not be the best choice at this stage.

The target is to select the top k relevant ads from the set given by phase 2. We will
use training data and dense features to train this model to predict engagement scores
better and minimize our log loss error.

At evaluation time, we will get a new predicted engagement score for ranking of ads. Ads
will be sorted based on this prediction CPE, which is the (bid * CPE) score, as we did
in phase 2. However, our predicted CPE score should be a far better prediction than
using historical priors as we did in phase 2.

As we progress down the funnel, the complexity of the models increases, and the number
of results decrease. Within the ad selection component, we adopt the same funnel based
approach. First, we select ads in phase 1, then rank them based on prior scores in phase
2. Finally, we rank them using an efficient model in phase 3 to come up with the top ads
that we want to send to the ad prediction stage.

How does the system scale?
--------------------------

Note that our index is sharded, i.e., it runs on multiple machines and every machine
selects the top k ads based on the prior score. Each machine then runs a simplistic
logistic regression model built on dense features (there are no sparse features to keep
the model size small) to rank ads.

The number of partitions (shards) depends on the size of the index. A large index
results in more partitions as compared to a smaller index. Also, the system load
measured in queries per second (QPS) decides how many times the partition is replicated.

Consider a scenario where the size of the index is 1 tera-byte and memory of a single
shard is 250 giga-bytes. The index data gets distributed in four partitions. Each
partition selects ads that satisfy the selection criteria. Then, we use the prior score
of the selected ads and select top five-hundred ads based on that score. To further
narrow down the ad set, we run logistic regression which returns the top 50 ads. The top
fifty ranked ads from each of the four partitions (200 ads in total) are fed to the ad
prediction component.

Note that for each level we are selecting top “k” ads. The selection of the number “k”
for each level is very arbitrary. It is based on experimentation and system available
load/capacity.

The ad set returned from the ad selection component is further ranked by the ad
prediction component.
"""
