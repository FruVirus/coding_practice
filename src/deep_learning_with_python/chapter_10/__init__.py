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
with regularization.
"""
