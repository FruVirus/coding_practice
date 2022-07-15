"""
Feature Engineering
===================

An important aspect of the feature generation process is to first think about the main
actors that will play a key role in our feature engineering process.

The four such actors for search are:

    1. Searcher

    2. Query

    3. Document

    4. Context

Searcher-specific features
--------------------------

Assuming that the searcher is logged in, you can tailor the results according to their
age, gender and interests by using this information as features for your model.

Query-specific features
-----------------------

Query historical engagement

For relatively popular queries, historical engagement can be very important. You can use
query’s prior engagement as a feature.

Query intent

The “query intent” feature enables the model to identify the kind of information a
searcher is looking for when they type their query. The model uses this feature to
assign a higher rank to the documents that match the query’s intent. For instance, if a
person queries “pizza places”, the intent here is local. Therefore, the model will give
high rank to the pizza places that are located near the searcher.

Document-specific features
--------------------------

Page rank

The rank of a document can serve as a feature. To estimate the relevance of the document
under consideration, we can look at the number and quality of the documents that link to
it.

Document engagement radius

The document engagement radius can be another important feature. A document on a coffee
shop in Seattle would be more relevant to people living within a ten-mile radius of the
shop. However, a document on the Eiffel Tower might interest people all around the
world. Hence, in case our query has a local intent, we will choose the document with the
local scope of appeal rather than that with a global scope of appeal.

Context-specific features
-------------------------

Time of search

A searcher has queried for restaurants. In this case, a contextual feature can be the
time of the day. This will allow the model to display restaurants that are open at that
hour.

Recent events

The searcher may appreciate any recent events related to the query.

Searcher-document features
--------------------------

Distance

For queries inquiring about nearby locations, we can use the distance between the
searcher and the matching locations as a feature to measure the relevance of the
documents.


Historical engagement

Another interesting feature could be the searcher’s historical engagement with the
result type of the document. For instance, if a person has engaged with video documents
more in the past, it indicates that video documents are generally more relevant for that
person. Historical engagement with a particular website or document can also be an
important signal as the user might be trying to “re-find” the document.

Query-document features
-----------------------

Text Match

One feature can be the text match. Text match can not only be in the title of the
document, but it can also be in the metadata or content of a document.

Unigram or bigram

We can also look at data for each unigram and bigram for text match between the query
and document. For instance, the query: “Seattle tourism guide” will result in three
unigrams:

    1. Seattle

    2. tourism

    3. guide

These unigrams may match different parts of the document, e.g., “Seattle” may match the
document title, while “tourism” may match the document’s content. Similarly, we can
check the match for the bigram and the full trigram, as well. All of these text matches
can result in multiple text-based features used by the model.

Query-document historical engagement

The prior engagement data can be a beneficial feature for determining the best ranking
of the search results.

    - Click rate

    We want to see users’ historical engagement with documents shown in response to a
particular query. The click rates for the documents can help in the ranking process. For
example, we might observe across people’s queries on “Paris tourism” that the click rate
for the “Eiffel tower website” is the highest. So, the model will develop the
understanding that whenever someone queries “Paris tourism”, the document/website on
Eiffel tower is the most engaged with. It can then use this information in the ranking
of documents.

Embeddings

We can use embedding models to represent the query and documents in the form of vectors.
These vectors can provide significant insight into the relationship between the query
and the document.

The embedding model generates vectors in such a manner that if a document is on the same
topic/concept as the query, its vector is similar to the query’s vector. We can use this
characteristic to create a feature called “embedding similarity score”. The similarity
score is calculated between the query vector and each document vector to measure its
relevance for the query. The higher the similarity score, the more relevant a document
is for a query.
"""
