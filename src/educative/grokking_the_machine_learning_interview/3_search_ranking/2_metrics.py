"""
Metrics
=======

Machine learning models learn directly from the data, and no human intuition is encoded
into the model. Hence, selecting the wrong metric results in the model becoming
optimized for a completely wrong criterion.

There are two types of metrics to evaluate the success of a search query:

    1. Online metrics

    2. Offline metrics

We refer to metrics that are computed as part of user interaction in a live system as
Online metrics. Meanwhile, offline metrics use offline data to measure the quality of
your search engine and don’t rely on getting direct feedback from the users of the
system.

Online metrics
--------------

In an online setting, you can base the success of a search session on user actions. On a
per-query level, you can define success as the user action of clicking on a result.

Click-through rate

A simple click-based metric is click-through rate. The click-through rate measures the
ratio of clicks to impressions.

CTR = Number of clicks / Number of impressions

An impression means a view. For example, when a search engine result page loads and the
user has seen the result, you will consider that as an impression. A click on that
result is your success.

Successful session rate

One problem with the click-through rate could be that unsuccessful clicks will also be
counted towards search success. For example, this might include short clicks where the
searcher only looked at the resultant document and clicked back immediately. You could
solve this issue by filtering your data to only successful clicks, i.e., to only
consider clicks that have a long dwell time.

Dwell time is the length of time a searcher spends viewing a webpage after they’ve
clicked a link on a search engine result page (SERP).

Therefore, successful sessions can be defined as the ones that have a click with a
ten-second or longer dwell time.

Session success rate = Number of successful sessions / Number of total sessions

Caveat

Another aspect to consider is zero-click searches. Zero-click searches occur when a SERP
may answer the searcher’s query right at the top such that the searcher doesn’t need any
further clicks to complete the search. The searcher has found what they were looking for
without a single click!. The click-through rate would not work in this case (but your
definition of a successful session should definitely include it). We can fix this using
the time to success.

Time to success

Until now, we have been considering a single query-based search session. However, it may
span over several queries. For example, the searcher initially queries: “italian food”.
They find that the results are not what they are looking for and make a more specific
query: “italian restaurants”. Also, at times, the searcher might have to go over
multiple results to find the one that they are looking for.

Ideally, you want the searcher to go to the result that answers their question in the
minimal number of queries and as high on the results page as possible. So, time to
success is an important metric to track and measure search engine success.

For scenarios like this, a low number of queries per session means that your system was
good at guessing what the searcher actually wanted despite their poorly worded query.
So, in this case, we should consider a low number of queries per session in your
definition of a successful search session.

Offline metrics
---------------

The offline methods to measure a successful search session makes use of trained human
raters. They are asked to rate the relevance of the query results objectively, keeping
in view well-defined guidelines. These ratings are then aggregated across a query sample
to serve as the ground truth. Ground truth refers to the actual output that is desired
of the system. In this case, it is the ranking or rating information provided by the
human raters.

Normalized Discounted Cumulative Gain (NDCG)

NDCG is an improvement on cumulative gain (CG).

The cumulative gain (CG) for the search engine’s result ranking is computed by simply
adding each document’s relevance rating provided by the human rater.

CG_p = sum(rel_i) for i = 1 to p, where p is the position of the result on the SERP and
rel_i is the relevance rating of document i

In contrast to cumulative gain, discounted cumulative gain (DCG) allows us to penalize
the search engine’s ranking if highly relevant documents (as per ground truth) appear
lower in the result list.

DCG discounts are based on the position of the document in human-rated data. The
intuition behind it is that the search engine will not be of much use if it doesn’t show
the most relevant documents at the top of search result pages.

DCG_p = sum(rel_i / log(i + 1)) for i = 1 to p, where rel_i is the relevance rating of a
document, i is the position of the document, and p is the number of positions.

However, DCG can’t be used to compare the search engine’s performance across different
queries on an absolute scale. The is because the length of the result list varies from
query to query. So, the DCG for a query with a longer result list may be higher due to
its length instead of its quality. To remedy this, you need to move towards NDCG.

NDCG normalizes the DCG in the 0 to 1 score range by dividing the DCG by the max DCG or
the IDCG (ideal discounted cumulative gain) of the query. IDCG is the DCG of an ideal
ordering of the search engine’s result list.

NDCG_p = DCG_p / IDCG_p, where IDCG_p is the ideal discounted cumulative gain

An NDCG value near one indicates good performance by the search engine. Whereas, a value
near 0, indicates poor performance.

In order to compute IDCG, you find an ideal ordering of the search engine’s result list.
This is done by rearranging the search engine’s results based on the ranking provided by
the human raters. For example, if a human rated D_3 higher than D_2, then the
calculation of IDCG would switch the positions of D_2 and D_3.

To compute NDCG for the overall query set with N queries, we take the mean of the
respective NDCGs of all the N queries, and that’s the overall relevance as per human
ratings of the ranking system.

NDCG = sum(NDCG_i) / N for i = 1 to N

Caveat
------

NDCG does not penalize irrelevant search results. In our case, it didn’t penalize D_4,
which had zero relevance according to the human rater. Another result set may not
include D_4, but it would still have the same NDCG score. As a remedy, the human rater
could assign a negative relevance score to that document.
"""
