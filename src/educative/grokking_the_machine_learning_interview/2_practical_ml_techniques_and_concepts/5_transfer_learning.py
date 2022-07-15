"""
Transfer Learning
=================

What is transfer learning?
--------------------------

Transfer learning is the task of using a pre-trained model and applying it to a new
task, i.e., transferring the knowledge learned from one task to another. This is useful
because the model doesn’t have to learn from scratch and can achieve higher accuracy in
less time as compared to models that don’t use transfer learning.

Motivation
----------

1. Growth in the ML community and knowledge sharing.

2. Common sub-problems.

3. Limited supervised learning data and training resources.

Techniques for transfer learning utilization
--------------------------------------------

The transfer learning technique can be utilized in the following ways:

    - Extract features from useful layers. Keep the initial layers of the pre-trained
model and remove the final layers. Add the new layer to the remaining chunk and train
them for final classification.

    - Fine-tuning. Change or tune the existing parameters in a pre-trained network,
i.e., optimizing the model parameters during training for the supervised prediction
task. A key question with fine-tuning the model is to see how many layers can we freeze
and how many final layers we want to fine-tune.

Transfer learning technique can be utilized in one or both of the above ways depending
on the following two factors:

    1. Size of our supervised training dataset. How much labeled data do we possess to
optimize the model? Do we have 100k examples, 1 million examples, 10 million examples?

    Training data is limited: In case of a limited amount of specialized training data,
we can either go with the approach of freezing all the layers and using the pre-trained
model for feature generation or fine-tuning only the final layers.

    Training data is plenty: If we have a significant amount of training data (e.g. one
million+ examples), we have the choice to play around with multiple ideas. We can start
with just freezing the model, fine-tuning only final layers, or we can retrain the whole
model to adjust weights for our specialized task.

    2. Similarity of prediction tasks. The similarity of learning tasks can also guide
us on whether we can simply use the model as it is or need to fine-tune the model for
our new prediction task.

Applications
------------

Computer vision problems

The convolutional filters in a trained convolutional neural network (CNN) are arranged
in a kind of hierarchy. The filters in the first layer often detect edges or blocks of
color. The second layer’s filters can detect features like shapes. All of them are very
general features that are useful in analyzing any image in any dataset. The filters in
the last layers are more specific.

Natural language processing (NLP)

In many of NLP learning tasks such as language understanding, speech recognition, entity
recognition, language generation, semantic understanding, etc. as well as other problems
that are based on search, one major need is to represent our text terms in a way that
they capture the semantic meaning.

For this, we need to generate the dense representation of textual terms. A few of the
popular term representation models that use a self-supervised learning approach, trained
on massive datasets are Word2Vec, BERT, and ELMO. The term representation based on these
models capture their semantic meanings. Hence, we can transfer knowledge from this
learned task in many of the NLP tasks.
"""
