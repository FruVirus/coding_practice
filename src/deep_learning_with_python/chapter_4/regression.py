"""Regression."""

# pylint: disable=E1120, W1114

# Third Party Library
import numpy as np
import tensorflow as tf

from tensorflow import keras

# Loading the Boston housing dataset
(train_data, train_targets), (
    test_data,
    test_targets,
) = tf.keras.datasets.boston_housing.load_data()
print(train_data.shape)
print(train_targets.shape)
print(test_data.shape)
print(test_targets.shape)

# Normalizing the data
mean = train_data.mean(axis=0)
train_data -= mean
std = train_data.std(axis=0)
train_data /= std
test_data -= mean
test_data /= std


# Model definition
def build_model():
    model = keras.Sequential(
        [
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dense(1),
        ]
    )
    model.compile(optimizer="rmsprop", loss="mse", metrics=["mae"])
    return model


# K-fold validation
k = 4
num_val_samples = len(train_data) // k
num_epochs = 500
all_mae_histories = []  # type: ignore
for i in range(k):
    print(f"Processing fold #{i}")
    val_data = train_data[i * num_val_samples : (i + 1) * num_val_samples]
    val_targets = train_targets[i * num_val_samples : (i + 1) * num_val_samples]
    partial_train_data = np.concatenate(
        [train_data[: i * num_val_samples], train_data[(i + 1) * num_val_samples :]],
        axis=0,
    )
    partial_train_targets = np.concatenate(
        [
            train_targets[: i * num_val_samples],
            train_targets[(i + 1) * num_val_samples :],
        ],
        axis=0,
    )
    model = build_model()
    history = model.fit(
        partial_train_data,
        partial_train_targets,
        epochs=num_epochs,
        batch_size=16,
        verbose=0,
    )
    mae_history = history.history["mae"]
    all_mae_histories.append(mae_history)
average_mae_history = [
    np.mean([x[i] for x in all_mae_histories]) for i in range(num_epochs)
]
print(average_mae_history)
