"""
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

The first key requirement to be able to achieve the quick selection objective is to have
the ads stored in a system that is fast and enables complex selection criteria. This is
where building an in-memory index to store the ads will be massively helpful. Index
allows us to fetch ads quickly based on different targeting and relevance information
from the user. We will index ads on all possible indexing terms that can be used for
selection e.g. targeted terms, city, state, country, region, age etc.

In a search-based system, the selection query in this case will look like:

    (term = "machine learning")
            and
    (age = "\*" or age contains "25")
            and
    (gender = "\*" or gender = "male")
            and
            ...
            and
    (has_budget = True)

In a feed-based system, the selection query would look like:

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
