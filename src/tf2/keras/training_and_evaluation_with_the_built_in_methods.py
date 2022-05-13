# pylint: disable=C0114, E1123, E1120, E0102, W0223, R0901, W0703, W0613, R0204
# pylint: disable=E1129, C0102, W0603

# Third Party Library
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers

# Introduction #

# API overview: a first end-to-end example #

# The compile() method: specifying a loss, metrics, and an optimizer #

# Many built-in optimizers, losses, and metrics are available

# Custom losses

# Custom metrics

# Handling losses and metrics that don't fit the standard signature

# Automatically setting apart a validation holdout set

# Training & evaluation from tf.data Datasets #

# Using a validation dataset

# Other input formats supported #

# Using a keras.utils.Sequence object as input #

# Using sample weighting and class weighting #

# Class weights

# Sample weights

# Passing data to multi-input, multi-output models #

# Using callbacks #

# Many built-in callbacks are available

# Writing your own callback

# Checkpointing models #

# Using learning rate schedules #

# Passing a schedule to an optimizer

# Using callbacks to implement a dynamic learning rate schedule

# Visualizing loss and metrics during training #

# Using the TensorBoard callback
