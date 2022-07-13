"""
Main Takeaways
~~~~~~~~~~~~~~

Candidate Generation
====================

The purpose of candidate generation is to select the top k (let's say one-thousand)
movies that you would want to consider showing as recommendations to the end-user.
Therefore, the task is to select these movies from a corpus of more than a million
available movies.

Candidate generation techniques
-------------------------------

The candidate generation techniques are as follows:

    1. Collaborative filtering

    2. Content-based filtering

    3. Embedding-based similarity

Each method has its own strengths for selecting good candidates, and we will combine all
of them together to generate a complete list before passing it on to the ranker (this
will be explained in the ranking lesson).

Collaborative filtering
-----------------------

In this technique, you find users similar to the active user based on the intersection
of their historical watches. You then collaborate with similar users to generate
candidate media for the active user.

If a user shares a similar taste with a group of users over a subset of movies, they
would probably have similar opinions on other movies compared to the opinion of a
randomly selected person.

There are two methods to perform collaborative filtering:

    1. Nearest neighborhood

    2. Matrix factorization

Method 1: Nearest neighborhood

User A is similar to user B and user C as they have watched the movies Inception and
Interstellar. So, you can say that user A’s nearest neighbours are user B and user C.
You will look at other movies liked by users B and C as candidates for user A’s
recommendations.

Let’s see how this concept is realized. You have a (n x m) matrix of user u_i
(i = 1 to n) and movie m_j (j = 1 to m). Each matrix element represents the feedback
that the user i has given to a movie j. An empty cell means that user i has not watched
movie j. For example a 1 means that the media has been watched/liked, a 0 means that the
media has not been watched/disliked, and an empty cell means that the media has no
impressions yet.

To generate recommendations for user i, you need to predict their feedback for all the
movies they haven’t watched. You will collaborate with users similar to user i for this
process. Their ratings for a movie, not seen by user i, would give us a good idea of how
user i would like it.

So, you will compute the similarity (e.g. cosine similarity) of other users with user i and then select the top k similar users/nearest neighbours (KNN(u_i)
(u
i
​
 )
). Then, user i’s feedback for an unseen movie j (f_{ij}
f
ij
​

) can be predicted by taking the weighted average of feedback that the top k similar users gave to movie j. Here the feedback by the nearest neighbour is weighted by their similarity with user i.

f_{ij}
f
ij
​

 = \frac{\sum\limits_{v\;\in\;KNN(u_i)} Similarity(u_i,u_v)f_{vj}}{k}
k
v∈KNN(u
i
​
 )
∑
​
 Similarity(u
i
​
 ,u
v
​
 )f
vj
​

​


The unseen movies with good predicted feedback will be chosen as candidates for user i’s recommendations.

Collaborative filtering by identifying similar media
It is evident that this process will be computationally expensive with the increase in numbers of users and movies. The sparsity of this matrix also poses a problem when a movie has not been rated by any user or a new user has not watched many movies.
"""
