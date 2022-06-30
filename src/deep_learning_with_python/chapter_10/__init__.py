"""Deep learning for timeseries

10.1 Different kinds of timeseries tasks
========================================

A timeseries can be any data obtained via measurements at regular intervals. Working
with timeseries involves understanding the dynamics of a system---its periodic cycles,
how it trends over time, its regular regime, and its sudden spikes.

The most common timeseries-related task is forecasting: predicting what will happen next
in a series. There's a wide range of other things you can do with timeseries:

- Classification---Assign one or more categorical labels to a timeseries. For example,
given the timeseries of the activity of a visitor on a website, classify whether the
visitor is a bot or a human.

- Event detection---Identify the occurrence of a specific expected event within a
continuous data stream (e.g. hot word detection).

- Anomaly detection---Detect anything unusual happening within a continuous datastream.
Anomaly detection is typically done via unsupervised learning, because you often don't
know what kind of anomaly you're looking for, so you can't train on specific anomaly
examples.

10.2 A temperature-forecasting example
======================================

Always look for periodicity in your data

Periodicity over multiple timescales is an important and very common property of
timeseries data. When exploring your data, make sure to look for these patterns.

When working with timeseries data, it's important to use validation and test data that
is more recent than the training data, because you're trying to predict the future given
the past, not the reverse, and your validation/test splits should reflect that.

10.3 Understanding recurrent neural networks
============================================

A major characteristic of neural networks such as densely connected networks and
convnets, is that they have no memory. Each input shown to them is processed
independently, with no state kept between inputs. With such networks, in order to
process a sequence or a temporal series of data points, you have to show the entire
sequence to the network at once: turn it into a single data point. Such networks are
called feedforward networks.

A recurrent neural network (RNN) processes sequences by iterating through the sequence
elements and maintaining a state that contains information relative to what it has seen
so far. In effect, an RNN is a type of neural network that has an internal loop.

The state of the RNN is reset between processing two different, independent sequences
(such as two samples in a batch), so you still consider one sequence to be a single data
point: a single input to the network. What changes is that this data point is no longer
processed in a single step; rather, the network internally loops over sequence elements.
Note that an RNN batch sample has shape (timesteps, input_features) so that the RNN
internally loops over timesteps for each batch sample. Since each batch sample is
different, the state is reset to 0 for each batch sample at the beginning of the RNN's
internal loop.

Note: Each timestep t in the output tensor contains information about timesteps 0 to t
in the input sequence---about the entire past. For this reason, in many cases, you don't
need the full sequence of outputs; you just need the last output at time t, because it
already contains information about the entire sequence.

10.4 Advanced use of recurrent neural networks
==============================================

10.4.1 Using recurrent dropout to fight overfitting
---------------------------------------------------

Applying dropout layers before a recurrent layer hinders learning rather than helping
with regularization. The proper way to use dropout with a recurrent network is to use
the same dropout mask (the same pattern of dropped units) at every timestep. What's
more, in order to regularize the representations formed by the recurrent gates of layers
such as GRU and LSTM, a temporally constant dropout mask should be applied to the inner
recurrent activations of the layer (a recurrent dropout mask). Using the same dropout
mask at every timestep allows the network to properly propagate its learning error
through time; a temporally random dropout mask would disrupt this error signal and be
harmful to the learning process.

In other words, an RNN cell has a dropout parameter for the linear transformation of its
inputs and a recurrent dropout parameter for the linear transformation of its recurrent
(i.e., hidden state).

10.4.2 Stacking recurrent layers
--------------------------------

Increasing network capacity is typically done by increasing the number of units in the
layers or adding more layers.

10.4.3 Using bidirectional RNNs
-------------------------------

RNNs are notably order-dependent: they process the timesteps of their input sequences in
order, and shuffling or reversing the timesteps can completely change the
representations the RNNs extracts from the sequence. A bidirectional RNN exploits the
order sensitivity of RNNs: it uses two regular RNNs, each of which processes the input
sequence in one direction (chronologically and antichronologically), and then merges
their representations. By processing a sequence both ways, a bidirectional RNN can catch
patterns that may be overlooked by a unidirectional RNN.

Bidirectional RNNs are a great fit for text data, or any other kind of data where order
matters, yet where *which order* you use doesn't matter.
"""
