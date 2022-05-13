# pylint: disable=C0114, E1123, E1120, E0102, W0223, R0901, W0703, W0613, R0204
# pylint: disable=E1129, C0102, W0603

# Third Party Library
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers

# When to use a Sequential model #

model = keras.Sequential(
    [
        layers.Dense(2, activation="relu", name="layer1"),
        layers.Dense(3, activation="relu", name="layer2"),
        layers.Dense(4, name="layer3"),
    ]
)
x = tf.ones((3, 3))
y = model(x)

layer1 = layers.Dense(2, activation="relu", name="layer1")
layer2 = layers.Dense(3, activation="relu", name="layer2")
layer3 = layers.Dense(4, name="layer3")
x = tf.ones((3, 3))
y = layer3(layer2(layer1(x)))

# Creating a Sequential model #

model = keras.Sequential(
    [
        layers.Dense(2, activation="relu"),
        layers.Dense(3, activation="relu"),
        layers.Dense(4),
    ]
)
print(model.layers)

model = keras.Sequential()
model.add(layers.Dense(2, activation="relu"))
model.add(layers.Dense(3, activation="relu"))
model.add(layers.Dense(4))
model.pop()
print(len(model.layers))  # 2

model = keras.Sequential(name="my_sequential")
model.add(layers.Dense(2, activation="relu", name="layer1"))
model.add(layers.Dense(3, activation="relu", name="layer2"))
model.add(layers.Dense(4, name="layer3"))
print()

# Specifying the input shape in advance #

layer = layers.Dense(3)
print(layer.weights)

x = tf.ones((1, 4))
y = layer(x)
print(layer.weights)

model = keras.Sequential(
    [
        layers.Dense(2, activation="relu"),
        layers.Dense(3, activation="relu"),
        layers.Dense(4),
    ]
)
x = tf.ones((1, 4))
y = model(x)
print("Number of weights after calling the model:", len(model.weights))
print(model.summary())

model = keras.Sequential()
model.add(keras.Input(shape=(4,)))
model.add(layers.Dense(2, activation="relu"))
print(model.summary())
print(model.layers)

model = keras.Sequential()
model.add(layers.Dense(2, activation="relu", input_shape=(4,)))
print(model.summary())
print()

# A common debugging workflow: add() + summary() #

model = keras.Sequential()
model.add(keras.Input(shape=(250, 250, 3)))  # 250x250 RGB images
model.add(layers.Conv2D(32, 5, strides=2, activation="relu"))
model.add(layers.Conv2D(32, 3, activation="relu"))
model.add(layers.MaxPooling2D(3))

print(model.summary())

model.add(layers.Conv2D(32, 3, activation="relu"))
model.add(layers.Conv2D(32, 3, activation="relu"))
model.add(layers.MaxPooling2D(3))
model.add(layers.Conv2D(32, 3, activation="relu"))
model.add(layers.Conv2D(32, 3, activation="relu"))
model.add(layers.MaxPooling2D(2))

print(model.summary())

model.add(layers.GlobalMaxPooling2D())

model.add(layers.Dense(10))
print()

# Feature extraction with a Sequential model #

initial_model = keras.Sequential(
    [
        keras.Input(shape=(250, 250, 3)),
        layers.Conv2D(32, 5, strides=2, activation="relu"),
        layers.Conv2D(32, 3, activation="relu"),
        layers.Conv2D(32, 3, activation="relu"),
    ]
)
feature_extractor = keras.Model(
    inputs=initial_model.inputs,
    outputs=[layer.output for layer in initial_model.layers],
)

x = tf.ones((1, 250, 250, 3))
features = feature_extractor(x)

initial_model = keras.Sequential(
    [
        keras.Input(shape=(250, 250, 3)),
        layers.Conv2D(32, 5, strides=2, activation="relu"),
        layers.Conv2D(32, 3, activation="relu", name="my_intermediate_layer"),
        layers.Conv2D(32, 3, activation="relu"),
    ]
)
feature_extractor = keras.Model(
    inputs=initial_model.inputs,
    outputs=initial_model.get_layer(name="my_intermediate_layer").output,
)
x = tf.ones((1, 250, 250, 3))
features = feature_extractor(x)

# Transfer learning with a Sequential model #

model = keras.Sequential(
    [
        keras.Input(shape=(784)),
        layers.Dense(32, activation="relu"),
        layers.Dense(32, activation="relu"),
        layers.Dense(32, activation="relu"),
        layers.Dense(10),
    ]
)

model.load_weights(...)

for layer in model.layers[:-1]:
    layer.trainable = False

model.compile(...)
model.fit(...)

base_model = keras.applications.Xception(
    weights="imagenet", include_top=False, pooling="avg"
)

base_model.trainable = False

model = keras.Sequential(
    [
        base_model,
        layers.Dense(1000),
    ]
)

model.compile(...)
model.fit(...)
