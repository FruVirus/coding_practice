"""
Document Selection
==================

From the one-hundred billion documents on the internet, we want to retrieve the top
one-hundred thousand that are relevant to the searcher’s query by using information
retrieval techniques.

Information retrieval is the science of searching for information in a document. It
focuses on comparing the query text with the document text and determining what is a
good match.

Documents

Document types can be Web-pages, emails, books, news stories, scholarly papers, text
messages, etc. All of the above have a significant amount of textual content.

Inverted Index

Inverted index is an index data structure that stores a mapping from content, such as
words or numbers, to its location in a set of documents. That is, given a set of
documents, where (which document indices) does the term "restaurants" appear?

Document selection process
--------------------------

The searcher’s query does not match with only a single document. The selection criteria
derived from the query may match a lot of documents with a different degree of
relevance.

Selection criteria
------------------

Our document selection criteria would then be as follows:

    Retrieve documents that match term "italian" and (match term "restaurant" or match
    term "food")

We will go into the index and retrieve all the documents based on the above selection
criteria. While we would check whether each of the documents matches the selection
criteria, we would also be assigning them a relevance score alongside. At the end of the
retrieval process, we will have selected relevant documents sorted according to their
relevance score. From these documents, we can then forward the top one-hundred thousand
documents to the ranker.

Relevance scoring scheme
------------------------

One basic scoring scheme is to utilize a simple weighted linear combination of the
factors involved. The weight of each factor depends on its importance in determining the
relevance score. The weight of each factor in determining the score can be selected
manually or using machine learning. Some of these factors are:

    1. Terms match

    2. Document popularity

    3. Query intent match

    4. Personalization match

Terms match

Our query contains multiple terms. We will use the inverse document frequency or IDF
score of each term to weigh the match. The match for important terms in the query weighs
higher.

Document popularity

The document’s popularity score is stored in the index.

Query intent match

The query intent component describes the intent of the query. For our query, the
component may reveal that there is a very strong local intent.

Personalization match

It scores how well a document meets the searcher’s individual requirements based on a
lot of aspects. For instance, the searcher’s age, gender, interests, and location.
"""
