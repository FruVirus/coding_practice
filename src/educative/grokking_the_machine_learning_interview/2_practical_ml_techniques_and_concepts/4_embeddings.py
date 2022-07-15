"""
Embeddings
==========

Embeddings
----------

Embeddings enable the encoding of entities (e.g., words, docs, images, person, ad, etc.)
in a low dimensional vector space such that it captures their semantic information.
Capturing semantic information helps to identify related entities that occur close to
each other in the vector space.

Transfer learning refers to transferring information from one ML task to another.
Embeddings easily enable us to do that for common entities among different tasks. For
example, Twitter can build an embedding for their users based on their organic feed
interactions and then use the embeddings for ads serving. Organic interactions are
generally much greater in volume compared to ads interactions. This allows Twitter to
learn user interests by organic feed interaction, capture it as embedding, and use it to
serve more relevant ads.

Auto-encoders use neural networks consisting of both an encoder and a decoder. They
first learn to compress the raw image pixel data to a small dimension via an encoder
model and then try to de-compress it via a decoder to re-generate the same input image.
The last layer of encoder determines the dimension of the embedding, which should be
sufficiently large to capture enough information about the image so that the decoder can
decode it. The combined encoder and decoder tries to minimize the difference between
original and generated pixels, using backpropagation to train the network. Once we have
trained the model, we only use the encoder (first N network layers) to generate
embeddings for images.

Text embeddings
---------------

Word2Vec

Word2Vec produces word embeddings by using shallow neural networks (having a single
hidden layer) and self-supervised learning from a large corpus of text data. Word2Vec is
self-supervised as it trains a model by predicting words from other words that appear in
the sentence (context).

Context-based embeddings

Contextualized information can result in different meanings of the same word, and
context-based embeddings look at neighboring terms at embedding generation time. This
means that we have to provide contextual information (neighboring terms) to fetch
embeddings for a term.

Two popular architectures used to generate word context-based embedding are:

    1. Embeddings from Language Models (ELMo)

    2. Bidirectional Encoder Representations from Transformers (BERT)

Visual embedding
----------------

Auto-encoders

Auto-encoders use neural networks consisting of both an encoder and a decoder. They
first learn to compress the raw image pixel data to a small dimension via an encoder
model and then try to de-compress it via a decoder to re-generate the same input image.
The last layer of encoder determines the dimension of the embedding, which should be
sufficiently large to capture enough information about the image so that the decoder can
decode it. Once we have trained the model, we only use the encoder (first N network
layers) to generate embeddings for images.

Visual supervised learning tasks

Visual supervised learning tasks such as image classification or object detection, are
generally set up as convolution layers, pooling layers, and fully connected network
layers, followed by final classification (softmax) layers. The penultimate layer before
softmax captures all image information in a vector such that it can be used to classify
the image correctly. So, we can use the penultimate layer value of a pre-trained model
as our image embedding.

Learning embeddings for a particular learning task
--------------------------------------------------

The advantage of this embedding is a specialized one for the given prediction task. One
important assumption here is that we have enough training data to be able to learn such
representation during model training. Another consideration is that training time for
learning the embedding as part of the task will be much higher compared to utilizing a
pre-trained embedding.

Network/Relationship-based embedding
------------------------------------

Most of the systems have multiple entities, and these entities interact with each other.
both queries and users that interact with web results. We can think of these
interactions as relationships in a graph or resulting in interaction pairs. For the
above example, these pairs would look like:

    1. (User, Pin) for Pinterest

    2. (User, Video) for YouTube

    3. (User, Tweet) for Twitter

    4. (Query, Webpage) for Search

    5. (Searcher, Webpage) for Search

In all the above scenarios, the retrieval and ranking of results for a particular user
(or query) are mostly about predicting how close they are. Therefore, having an
embedding model that projects these documents in the same embedding space can vastly
help in the retrieval and ranking tasks of recommendation, search, feed-based, and many
other ML systems.

We can generate embeddings for both the above-discussed pairs of entities in the same
space by creating a two-tower neural network model that tries to encode each item using
their raw features. The model optimizes the inner product loss such that positive pairs
from entity interactions have a higher score and random pairs have a lower score. Let’s
say the selected pairs of entities (from a graph or based on interactions) belong to set
A. We then select random pairs for negative examples.
"""
