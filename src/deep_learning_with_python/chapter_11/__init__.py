"""Deep learning for text

11.2 Preparing text data
========================

Deep learning models can only process numeric tensors: they can't take raw text as
input. Vectorizing text is the process of transforming text into numeric tensors.

- First, you standardize the text to make it easier to process, such as by converting it
to lowercase or removing punctuation.

- You split the text into units (called tokens), such as characters, words, or groups of
words. This is called tokenization.

- You convert each such token into a numerical vector. This will usually involve first
indexing all tokens present in the data.

11.2.1 Text standardization
---------------------------

Text standardization is a basic form of feature engineering that aims to erase encoding
differences that you don't want your model to have to deal with.

One of the simplest and most widespread standardization schemes is "convert to lowercase
and remove punctuation characters." Another common transformation is to convert special
characters to a standard form. Lastly, a much more advanced standardization pattern that
is more rarely used in a machine learning context is stemming: converting variations of
a term into a single shared representation.

With these standardization techniques, your model will require less training data and
will generalize better. Standardization may also erase some amount of information, so
always keep in context in mind (e.g., "?" might be an important token for Q & A tasks).

11.2.2 Text splitting (tokenization)
------------------------------------

Once your text is standardized, you need to break it up into units to be vectorized
(tokens), a step called tokenization.

- Word-level tokenization---Where tokens are space-separated (or punctuation-separated)
substrings. A variant of this is to further split words into subwords.

- N-gram tokenization---Where tokens are groups of N consecutive words. N-grams are a
way to artificially inject a small amount of local word order information into the
model.

- Character-level tokenization---Where each character has its own token. In practice,
this scheme is only used in specialized contexts, like text generation or speech
recognition.

There are two kinds of text-processing models: those that care about word order, called
sequence models, and those that treat input words as a set, discarding their original
order, called bag-of-words models. If you're building a sequence model, you'll use
word-level tokenization, and if you're building a bag-of-words model, you'll use N-gram
tokenization.

Understanding N-grams and bag-of-words

Because bag-of-words isn't an order-preserving tokenization method (the tokens generated
are understood as a set, not a sequence, and the general structure of the sentences is
lost), it tends to be used in shallow language-processing models rather than in deep
learning models. Extracting N-grams is a form of feature engineering, and deep learning
sequence models do away with this manual approach, replacing it with hierarchical
feature learning.

11.2.3 Vocabulary indexing
--------------------------

Once your text is split into tokens, you need to encode each token into a numerical
representation. In practice, you'd build an index of all terms found in the training
data (the "vocabulary"), and assign a unique integer to each entry in the vocabulary.

You then convert that integer into a vector encoding that can be processed by a neural
network, like a one-hot vector or a matrix of random weights.

Any text dataset tends to feature an extremely large number of unique terms, most of
which only show up once or twice---indexing those rare terms would result in an
excessively large feature space, where most features would have almost no information
content. Thus, it's common to restrict the vocabulary to only the top 20k or 30k most
common words found in the training data.

You should use an OOV index---a catch-all for any token that wasn't in the index. When
decoding a sequence of integers back into words, you'll replace the OOV index with
something like "UNK".

The index 0 is typically reserved for the mask token. You'd use the mask token to pad
sequence data: because data batches need to be contiguous, all sequences in a batch of
sequence data must have the same length, so shorter sequences should be padded to the
length of the longest sequence.

11.3 Two approaches for representing groups of words: Sets and sequences
========================================================================

Individual words are categorical features (values from a predefined set)---they should
be encoded as dimensions in a feature space, or as category vectors (i.e., word
vectors). A much more problematic question is how to encode the way words are woven into
sentences: word order.

Unlike the steps of a timeseries, words in a sentence don't have a natural, canonical
order. Different languages order similar words in very different ways. Even within a
given language, you can typically say the same thing in different ways by reshuffling
the words a bit. Order is clearly important, but its relationship to meaning isn't
straightforward.

The simplest thing you could do is just discard order and treat text as an unordered set
of words---this gives you bag-of-words models. You could also decide that words should
be processed strictly in the order in which they appear, like steps in a timeseries. A
hybrid approach is also possible: the Transformer architecture is technically
order-agnostic, yet it injects word-position information into the representations it
processes, which enables it to simultaneously look at different parts of a sentence
(unlike RNNs) while still being order-aware.

11.3.2 Processing words as a set: The bag-of-words approach
-----------------------------------------------------------

The simplest way to encode a piece of text for processing by a machine learning model is
to discard order and treat it as a set of tokens. You could either look at individual
words (unigrams) or try to recover some local order information by looking at groups of
consecutive tokens (N-grams).

Single Words (Unigrams) With Binary Encoding

With binary encoding (multi-hot), you'd encode a text as a vector with as many
dimensions are there are words in your vocabulary---with 0's almost everywhere and some
1's for dimensions that encode words present in the text.

Bigrams With Binary Encoding

Since even atomic concepts can be expressed via multiple words (e.g., "United States"),
you will usually end up re-injecting local order information into your bag-of-words
representation by looking at N-grams rather than single words.

Bigrams With TF-IDF Encoding

You can also add a bit more information by counting how many times each word or N-gram
occurs; i.e., by taking the histogram of the words over the text.

You could also normalize away uninformative words by using TF-IDF weighting.

11.3.3 Processing words as a sequence: The sequence model approach
------------------------------------------------------------------

To implement a sequence model, you'd start by representing your input samples as
sequences of integer indices (one integer standing for one word). Then, you'd map each
integer to a vector to obtain vector sequences. Finally, you'd feed these sequences of
vectors into a stack of layers.

A First Practical Example

The simples way to convert our integer sequences to vector sequences is to one-hot
encode the integers (each dimension would represent one possible term in the
vocabulary).

Understanding Word Embeddings

Crucially, when you encode something via one-hot encoding, you're making a
feature-engineering decision. You're injecting into your model a fundamental assumption
about the structure of your feature space. That assumption is that the different tokens
you're encoding are all independent from each other: indeed, one-hot vectors are all
orthogonal to one another. Words form a structured space: they share information with
each other. Words that are interchangeable should not be orthogonal.

The geometric relationship between two word vectors should reflect the semantic
relationship between these words. Words that mean different things should lie far away
from each other, whereas related words should be closer.

Word embeddings are vector representations of words that achieve exasctly this: they map
human language into a structured geometric space.

Whereas the vectors obtained through one-hot encoding are binary, sparse, and very
high-dimensional (the same dimensionality as the number of words in the vocabulary),
word embeddings are low-dimensional floating-point vectors (i.e., dense vectors). Word
embeddings are learned from data and pack more information into far fewer dimensions.

Besides being dense representations, word embeddings are also structured
representations, and their structure is learned from data. Similar words get embedded in
close locations, and further, specific directions in the embedding space are meaningful.

There are two ways to obtain word embeddings:

- Learn word embeddings jointly in the main task you care about. In this setup, you
start with random word vectors and then learn word vectors in the same way you learn the
weights of a neural network.

- Load into your model word embeddings that were precomputed using a different machine
learning task than the one you're trying to solve. These are called pretrained word
embeddings.

Learning Word Embeddings With the Embedding Layer

What makes a good word-embedding space depends heavily on your task because the
importance of certain semantic relationships varies from task to task. It's thus
reasonable to learn a new embedding space with every new task.

Understanding Padding And Masking

One thing that's slightly hurting model performance is that our input sequences are full
of zeros. Long sentences are truncated and short sentences are padded with zeros at the
end so that they can be concatenated together with other sequences to form contiguous
batches.

The RNN that looks at the tokens in their natural order will spend its last iterations
seeing only vectors that encode padding---possibly for several hundreds of iterations
if the original sentence was short. The information stored in the internal state of the
RNN will gradually fade out as it gets exposed to these meaningless inputs.

We can tell the RNN to skip these iterations by using masking to skip over iterations
where the mask value is 0.

Using Pretrained Word Embeddings

Sometimes you have so little training data available that you can't use your data alone
to learn an appropriate task-specific embedding of your vocabulary. In such cases,
instead of learning word embeddings jointly with the problem you want to solve, you can
load embedding vectors from a precomputed embedding space that you know is highly
structured and exhibits useful properties---one that captures generic aspects of
language structure.

11.4 The Transformer architecture
=================================

11.4.1 Understanding self-attention
-----------------------------------

Not all information seen by a model is equally important to the task at hand, so models
should "pay more attention" to some features and "pay less attention" to other features.

- Max pooling in convnets performs an "all or nothing" form of attention: keep the most
important feature and discard the rest.

- TF-IDF normalization performs a continuous form of attention whereby relevant tokens
are boosted while irrelevant tokens get faded out.

All forms of attention start out by computing importance scores for a set of features,
with higher scores for more relevant features and lower scores for less relevant ones.
These scores can be used to inform the next representation of the input.

Crucially, this kind of attention mechanism can be used for more than just highlighting
or erasing certain features. It can be used to make features context-aware. In an
embedding space, a single word has a fixed position---a fixed set of relationships with
every other word in the space. But that's not quite how langauge works: the meaning of a
word is usually context-specific.

A smart embedding space would provide a different vector representation for a word
embedding depending on the other words surrounding it. That's where self-attention comes
in. The purpose of self-attention is to modulate the representation of a token by using
the representations of related tokens in the sequence. This produces context-aware token
representations.

Step 1 is to compute relevancy scores between a token and every other token in the
input. These are our "attention scores." We're simply going to use the dot product
between two token vectors as measure of the strength of their relationship.

Step 2 is to compute the sum of all token vectors in the input, weighted by our
relevancy scores. Words closely related to the token will contribute more to the sum,
while irrelevant tokens will contriubte almost nothing. The resulting vector is our new
representation for the token: a representation that incorporates the surrounding
context.

Generalized Self-Attention: The Query-Key-Value Model

Conceptually, you've got a reference sequence that describes something you're looking
for: the query. You've got a body of knowledge that you're trying to extract information
from: the values. Each value is assigned a key that describes the value in a format that
can be readily compared to a query. You simply match the query to the keys. Then you
return a weighted sum of values.

11.4.2 Multi-head attention
---------------------------

The "multi-head" moniker refers to the fact that the output space of the self-attention
layer gets factored into a set of independent subspaces, learned separately: the initial
query, key, and value are sent through three independent sets of dense projections,
resulting in three separate vectors. Each vector is processed via neural attention, and
the three outputs are concatenated back together into a single output sequence. Each
such subspace is called a "head."

The presence of the laernable dense projections enables the layer to actually learn
something, as opposed to being a purely stateless transformation that would require
additional layers before or after it to be useful. In addition, having independent heads
helps the layer learn different groups of features for each token, where features within
one group are correlated with each other but are mostly independent from features in a
different group.

This is similar in principle to what makes depthwise separable convolutions work: in a
depthwise separable convolution, the output space of the convolution is factored into
many subspaces (one per input channel) that get learned independently.

11.4.3 The Transformer encoder
------------------------------

While Batch Normalization collections information from many samples (thus, creating
interactions between samples in a batch) to obtain accurate statistics for the feature
means and variances, Layer Normalization pools data within each sequence separately,
which is more appropriate for sequence data.

Self-attention is a set-processing mechanism, focused on the relationships between pairs
of sequence elements---it's blind to whether these elements occur at the beginning, at
the end, or in the middle of a sequence.

Using Positional Encoding To Re-Inject Order Information

The idea behind positional encoding is very simple: to give the model access to
word-order information, we're going tp add the word's position in the sentence to each
word embedding. Our input word embeddings will have two components: the usual word
vector, which represents the word independently of any specific context, and a position
vector, which represents the position of the word in the current sentence.

11.4.4 When to use sequence models over bag-of-words models
-----------------------------------------------------------

A small stack of Dense layers on top of a bag-of-bigrams remains a perfectly valid and
relevant approach in many cases.

When approaching a new text-classification task, you should pay close attention to the
ratio between the number of samples in your training data and the mean number of words
per sample. If that ration is less than 1500, then the bag-of-bigrams model will perform
better. Otherwise, you should go with a sequence model. In other words, sequence models
work best when lots of training data is available and when each sample is relatively
short.

This intuitively makes sense: the input of a sequence model represents a richer and more
complex space, and thus it takes more data to map out that space; meanwhile, a plain set
of terms is a space so simple that you can train a logistic regression. In addition, the
shorter a sample is, the less the model can afford to discard any of the information it
contains---in particular, word order becomes more important, and discarding it can
create ambiguity. With a longer sample, word statistics would become more reliable and
the topic or sentiment would be more apparent from the word histogram alone.

11.5 Beyond text classification: Sequence-to-sequence learning
==============================================================

A sequence-to-sequence model takes a sequence as input and translates it into a
different sequence.

The general template behind sequence-to-sequence models is as follows:

During training:
    - An encoder model turns the source sequence into an intermediate representation.
    - A decoder is trained to predict the next token i in the sequence by looking at
both previous tokens and the encoded source sequence.

During inference, we don't have access to the target sequence---we're trying to predict
it from scratch. We'll have to generate one token at a time:
    1. We obtain the encoded source sequence from the encoder.
    2. The decoder starts by looking at the encoded source sequence as well as an
initial "seed" token, and uses them to predict the first real token in the sequence.
    3. The predicted sequence so far is fed back into the decoder, which generates the
next token, and so on, until it generates a stop token.

11.5.2 Sequence-to-sequence learning with RNNs
----------------------------------------------

You would first use an RNN (the encoder) to turn the entire source sequence into a
single vector (or set of vectors). This could be the last output of the RNN or its final
internal state vectors. Then you would use this vector (or vectors) as the initial state
of another RNN (the decoder), which would look at elements 0, ..., N in the target
sequence, and try to predict step N + 1 in the target sequence. This means we only use
information from the past to predict the future.

The RNN approach to sequence-to-sequence learning has a few fundamental limitations:

- The source sequence representation has to be held entirely in the encoder state
vector(s), which puts significant limitations on the size and complexity of the
sentences you can translate.

- RNNs have trouble dealing with very long sequences, since they tend to progressively
forget about the past.

11.5.3 Sequence-to-sequence learning with Transformer
-----------------------------------------------------

Neural attention enables Transformer models to successfully process sequences that are
considerably longer and more complex than those RNNs can handle.

Unlike RNNs, the Transformer encoder keeps the encoded representation in a sequence
format: it's a sequence of context-aware embedding vectors.

The Transformer Decoder

Unlike an RNN, which looks at its input one step at a time, the Transformer Decoder is
order-agnostic: it looks at the entire target sequence at once. Thus, we use causal
masking for the Decoder.
"""
