"""Binary classification."""

# pylint: disable=E1120, W1114

# Third Party Library
import numpy as np
import tensorflow as tf

from tensorflow import keras

# Loading the IMDB dataset
(train_data, train_labels), (test_data, test_labels) = tf.keras.datasets.imdb.load_data(
    num_words=10000
)
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
y_train = np.asarray(train_labels).astype("float32")
y_test = np.asarray(test_labels).astype("float32")

# Model definition
model = keras.Sequential(
    [
        tf.keras.layers.Dense(16, activation="relu"),
        tf.keras.layers.Dense(16, activation="relu"),
        tf.keras.layers.Dense(1, activation="sigmoid"),
    ]
)

# Compiling the model
model.compile(optimizer="rmsprop", loss="binary_crossentropy", metrics=["accuracy"])

# Setting aside a validation set
x_val = x_train[:10000]
partial_x_train = x_train[10000:]
y_val = y_train[:10000]
partial_y_train = y_train[10000:]

# Training your model
history = model.fit(
    partial_x_train,
    partial_y_train,
    epochs=4,
    batch_size=512,
    validation_data=(x_val, y_val),
)

# Run predictions
print(model.predict(x_test))
