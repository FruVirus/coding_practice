"""Multiclass classification."""

# pylint: disable=E1120, W1114

# Third Party Library
import numpy as np
import tensorflow as tf

from tensorflow import keras

# Loading the Reuters dataset
(train_data, train_labels), (
    test_data,
    test_labels,
) = tf.keras.datasets.reuters.load_data(num_words=10000)
print(train_data.shape)
print(train_labels.shape)
print(test_data.shape)
print(test_labels.shape)


# Encoding the integer sequences via multi-hot encoding
def vectorize_sequence(sequences, dimension=10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        for j in sequence:
            results[i, j] = 1
    return results


x_train = vectorize_sequence(train_data)
x_test = vectorize_sequence(test_data)


# Encoding the labels
def to_one_hot(labels, dimension=46):
    results = np.zeros((len(labels), dimension))
    for i, label in enumerate(labels):
        results[i, label] = 1
    return results


y_train = to_one_hot(train_labels)
y_test = to_one_hot(test_labels)

# Model definition
model = keras.Sequential(
    [
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dense(46, activation="softmax"),
    ]
)

# Compiling the model
model.compile(
    optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"]
)

# Setting aside a validation set
x_val = x_train[:1000]
partial_x_train = x_train[1000:]
y_val = y_train[:1000]
partial_y_train = y_train[1000:]

# Training your model
history = model.fit(
    partial_x_train,
    partial_y_train,
    epochs=9,
    batch_size=512,
    validation_data=(x_val, y_val),
)

# Run evaluation
print(model.evaluate(x_test, y_test))

# Run evaluation
predictions = model.predict(x_test)
print(np.argmax(predictions[0]))
