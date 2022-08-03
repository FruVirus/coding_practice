"""
Mean Reciprocal Rank (MRR)
==========================

MRR is a measure to evaluate systems that return a ranked list of answers to queries.

For a single query, the reciprocal rank is 1 / rank, where rank is the position of the
highest-ranked answer (1, 2, 3, ..., N for N answers returned in a query). If no correct
answer was returned in the query, then the reciprocal rank is 0.

For multiple queries Q, the MRR is the mean of the Q reciprocal ranks.

MRR = (1 / Q) * sum(1 / rank_i)

45

Imagine you have some kind of query, and your retrieval system has returned you a ranked
list of the top-20 items it thinks most relevant to your query. Now also imagine that
there is a ground-truth to this, that in truth we can say for each of those 20 that
"yes" it is a relevant answer or "no" it isn't.

Mean reciprocal rank (MRR) gives you a general measure of quality in these situations,
but MRR only cares about the single highest-ranked relevant item. If your system returns
a relevant item in the third-highest spot, that's what MRR cares about. It doesn't care
if the other relevant items (assuming there are any) are ranked number 4 or number 20.

Therefore, MRR is appropriate to judge a system where either (a) there's only one
relevant result, or (b) in your use-case you only really care about the highest-ranked
one. This might be true in some web-search scenarios, for example, where the user just
wants to find one thing to click on, they don't need any more. (Though is that typically
true, or would you be more happy with a web search that returned ten pretty good
answers, and you could make your own judgment about which of those to click on...?)

Mean average precision (MAP) considers whether all of the relevant items tend to get
ranked highly. So in the top-20 example, it doesn't only care if there's a relevant
answer up at number 3, it also cares whether all the "yes" items in that list are
bunched up towards the top.

When there is only one relevant answer in your dataset, the MRR and the MAP are exactly
equivalent under the standard definition of MAP.

Example 1

Query: "Capital of California"
Ranked results: "Portland", "Sacramento", "Los Angeles"
Ranked results (binary relevance): [0, 1, 0]
Number of correct answers possible: 1

Reciprocal Rank: 1/2

Precision at 1: 0/1
Precision at 2: 1/2
Precision at 3: 1/3
Average precision = (1/m) ∗ 1/2 = 1/1 ∗ 1/2 = 0.5

As you can see, the average precision for a query with exactly one correct answer is
equal to the reciprocal rank of the correct result. It follows that the MRR of a
collection of such queries will be equal to its MAP. However, as illustrated by the
following example, things diverge if there are more than one correct answer:

Example 2

Query: "Cities in California"
Ranked results: "Portland", "Sacramento", "Los Angeles"
Ranked results (binary relevance): [0, 1, 1]
Number of correct answers possible: 2

Reciprocal Rank: 1/2

Precision at 1: 0/1
Precision at 2: 1/2
Precision at 3: 2/3
Average precision = (1 / m) ∗ [1 / 2 + 2 / 3] = 1 / 2 ∗ [1 / 2 + 2 / 3] = 0.38.

As such, the choice of MRR vs MAP in this case depends entirely on whether or not you
want the rankings after the first correct hit to influence.
"""
