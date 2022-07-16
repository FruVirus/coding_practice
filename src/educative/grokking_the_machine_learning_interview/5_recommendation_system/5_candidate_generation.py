"""
Candidate Generation
====================

The purpose of candidate generation is to select the top k (let's say one-thousand)
movies that you would want to consider showing as recommendations to the end-user from a
corpus of more than a million available movies.

Candidate generation techniques
-------------------------------

The candidate generation techniques are as follows:

    1. Collaborative filtering

    2. Content-based filtering

    3. Embedding-based similarity

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

So, you will compute the similarity (e.g. cosine similarity) of other users with user i
and then select the top k similar users/nearest neighbours (KNN(u_i)). Then, user i’s
feedback for an unseen movie j (f_{ij} can be predicted by taking the weighted average
of feedback that the top k similar users gave to movie j. Here the feedback by the
nearest neighbour is weighted by their similarity with user i.

The unseen movies with good predicted feedback will be chosen as candidates for user i’s
recommendations.

It is evident that this process will be computationally expensive with the increase in
numbers of users and movies. The sparsity of this matrix also poses a problem when a
movie has not been rated by any user or a new user has not watched many movies.

We are also looking at the user-based approach of collaborative filtering (CF) where you
are identifying similar users. There is another approach known as the item-based
approach where we look at the similarity of the items (movies/shows) for generating
candidates. First, you calculate media similarity based on similar feedback from users.
Then the media most similar to that already watched by user A will be selected as
candidates for user A’s recommendation.

The user-based approach is often harder to scale as user preference tends to change over
time. Items, in contrast, don’t change so the item-based approach can usually be
computed offline and served without frequent re-training.

Method 2: Matrix factorization

As explained above, you need to represent the user-media interaction matrix in a way
that is scalable and handles sparsity. Here, matrix factorization helps us by factoring
this matrix into two lower dimensional matrices:

    1. User profile matrix (n x M). Each user in the user profile matrix is represented
by a row, which is a latent vector of M dimensions.

    2. Media profile matrix (M x m). Each movie in the movie profile matrix is
represented by a column, which is a latent vector of M dimensions.

The dimension M is the number of latent factors we’re using to estimate the user-media
feedback matrix. M is much smaller than the actual number of users and number of media.

The representation of users and media in the form of a vector of latent factors aims to
explain the reason behind a user’s particular feedback for a media. Latent vectors can
also be thought of as features of a movie or a user.

User A’s vector has their preferences: 1 for the “comedy” and 0 for “quirkiness”. Movie
B’s vector contains the presence/absence of the two factors in the movie, e.g., 1 and 0.
The dot product of these two vectors will tell how much movie B aligns with the
preferences of the user A; hence, the feedback.

The first step is to create the user profile and movie profile matrices. Then, you can
generate good candidates for movie recommendation by predicting user feedback for unseen
movies. This prediction can be made simply by computing the dot product of the user
vector with the movie vector.

Now, let’s go over the process of how to learn the latent factor matrices for users and
media.

You will initialize the user and movie vectors randomly. For each known/historical
user-movie feedback value f_{ij}, you will predict the movie feedback by taking the dot
product of the corresponding user profile vector u_i and movie profile vector m_j. The
difference between the actual (f_{ij}) and the predicted feedback (u_i.m_j) will be the
error (e_{ij}).

e_{ij} = f_{ij} - u_i.m_j

You will use stochastic gradient descent to update the user and movie latent vectors,
based on the error value. As you continue to optimize the user and movie latent vectors,
you will get a semantic representation of the users and movies, allowing us to find new
recommendations that are closer in that space.

The user profile vector will be made based on the movies that the user has given
feedback on. Similarly, the media/movie profile vector will be made based on its user
feedbacks. By utilizing these user and movie profile vectors, you will generate
candidates for a given user based on their predicted feedback for unseen movies.

Content-based filtering
-----------------------

Content-based filtering allows us to make recommendations to users based on the
characteristics or attributes of the media they have already interacted with.

As such the recommendations tend to be relevant to users’ interest. The characteristics
come from metadata (e.g., genre, movie cast, synopsis, director, etc.) information and
manually assigned media-descriptive-tags (e.g., visually striking, nostalgic, magical
creatures, character development, winter season, quirky indie rom-com set in Oregon,
etc.) by Netflix taggers. The media is represented as a vector of its attributes.

Initially, you have the media’s attributes in raw form. They need to be preprocessed
accordingly to extract features. For instance, you need to remove stop words and convert
attribute values to lowercase to avoid duplication. You also have to join the director’s
first name and last name to identify unique people since there maybe two directors with
the first name Christopher. Similar preprocessing is required for the tags. After this,
you are able to represent the movies as a vector of attributes with elements depicting
the term frequency (TF) (binary representation of attribute’s presence (1) or absence
(0)).

Now, you have the movies represented as vectors containing the TF (term/attribute
frequency) of all the attributes. This is followed by normalizing the term frequencies
by the length of the vectors (sum of non-zero features). Finally, you multiply the
movies’ normalized TF vectors and the IDF vector element-wise to make TF-IDF vectors for
the movies. The Document Frequency would be how many times Christopher Nolan appeared in
all movies in the database.

Given the TF-IDF representation of each movie/show, you have two options for
recommending media to the user:

    1. Similarity with historical interactions. You can recommend movies to the user
similar to those they have interacted (seen) with in the past. This can be achieved by
computing the dot product of movies.

    2. Similarity between media and user profiles. The media’s TF-IDF vectors can be
viewed as their profile. Based on user preferences, which can be seen from its
historical interactions with media, you can build user profiles as well. Now, instead of
using past watches to recommend new ones, you can just compute the similarity between
the user’s profile and media profiles of unseen movies to generate relevant candidates
for user A’s recommendations.

Generate embedding using neural networks/deep learning
------------------------------------------------------

Given the historical feedback (u, m), i.e., user u’s feedback for movie m, you can use
the power of deep learning to generate latent vectors/embeddings to represent both
movies and users. Once you have generated the vectors, you will utilize KNN (k nearest
neighbours) to find the movies that you would want to recommend to the user. This method
is similar to generating latent vectors, that you saw in matrix factorization but is
much more powerful because using NNs allows us to use all the sparse and dense features
in the data to generate user and movie embedding.

Embedding generation

You set up the network as two towers with one tower feeding in media only sparse and
dense features and the other tower feeding in user-only sparse and dense features. The
activation of the first tower’s last layer will form the media’s vector embedding (m).
Similarly, the activation of the second tower’s last layer will form the user’s vector
embedding (u). The combined optimization function at the top aims to minimize the
distance between the dot product of u and m (predicted feedback) and the actual feedback
label.

min(abs(dot(u, m) - label))

Let’s look at the intuition behind this cost function. The actual feedback label will be
positive when the media aligns with user preferences and negative when it does not. To
make the predicted feedback follow the same pattern, the network learns the user and
media embeddings in such a way that their distance will be minimized if the user would
like this media and maximized if the user would not like the media.

The vector representation of the user, which you would get as a result, will be nearest
to the kind of movies that the user would like/watch.

Candidate selection (KNN)

After the user and media vector embeddings have been generated, you will apply KNN and
select candidates for each user.

Techniques’ strengths and weaknesses
------------------------------------

Collaborative filtering can suggest candidates based solely on the historical
interaction of the users. Unlike content-based filtering, it does not require domain
knowledge to create user and media profiles. It may also be able to capture data aspects
that are often elusive and difficult to profile using content-based filtering. However,
collaborative filtering suffers from the cold start problem. It is difficult to find
users similar to a new user in the system because they have less historical interaction.
Also, new media can’t be recommended immediately as no users have given feedback on it.

The neural network technique also suffers from the cold start problem. The embedding
vectors of media and users are updated in the training process of the neural networks.
However, if a movie is new or if a user is new, both would have fewer instances of
feedback received and feedback given, respectively. By extension, this means there is a
lack of sufficient training examples to update their embedding vectors accordingly.
Hence, the cold start problem.

Content-based filtering is superior in such scenarios. It does require some initial
input from the user regarding their preferences to start generating candidates, though.
This input is obtained as a part of the onboarding process, where a new user is asked to
share their preferences. Once we have the initial input, it can create and then match
the user’s profile with media profiles. Moreover, new medias’ profiles can be built
immediately as their description is provided manually.
"""
