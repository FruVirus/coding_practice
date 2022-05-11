# pylint: disable=C0114, E1123, E1120, E0102, W0223, R0901, W0703, W0613, R0204
# pylint: disable=E1129, C0102, W0603

# Third Party Library
import tensorflow as tf
import tensorflow_datasets as tfds

# Recommendations for idiomatic TensorFlow 2 #

# Combine tf.data.Datasets and tf.function
datasets, info = tfds.load(name="mnist", with_info=True, as_supervised=True)
mnist_train, mnist_test = datasets["train"], datasets["test"]

BUFFER_SIZE = 10  # Use a much larger value for real code
BATCH_SIZE = 64
NUM_EPOCHS = 5


def scale(image, label):
    image = tf.cast(image, tf.float32)
    image /= 255
    return image, label


train_data = mnist_train.map(scale).shuffle(BUFFER_SIZE).batch(BATCH_SIZE)
test_data = mnist_test.map(scale).batch(BATCH_SIZE)

STEPS_PER_EPOCH = 5

train_data = train_data.take(STEPS_PER_EPOCH)
test_data = test_data.take(STEPS_PER_EPOCH)

image_batch, label_batch = next(iter(train_data))

# Use Keras training loops
model = tf.keras.Sequential(
    [
        tf.keras.layers.Conv2D(
            32,
            3,
            activation="relu",
            kernel_regularizer=tf.keras.regularizers.l2(0.02),
            input_shape=(28, 28, 1),
        ),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dropout(0.1),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dense(10),
    ]
)

model.compile(
    optimizer="adam",
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=["accuracy"],
)

model.fit(train_data, epochs=NUM_EPOCHS)
loss, acc = model.evaluate(test_data)

print("Loss {}, Accuracy {}".format(loss, acc))
print()

# Customize training and write your own loop
model = tf.keras.Sequential(
    [
        tf.keras.layers.Conv2D(
            32,
            3,
            activation="relu",
            kernel_regularizer=tf.keras.regularizers.l2(0.02),
            input_shape=(28, 28, 1),
        ),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dropout(0.1),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dense(10),
    ]
)

optimizer = tf.keras.optimizers.Adam(0.001)
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)


@tf.function
def train_step(inputs, labels):
    with tf.GradientTape() as tape:
        predictions = model(inputs, training=True)
        regularization_loss = tf.math.add_n(model.losses)
        pred_loss = loss_fn(labels, predictions)
        total_loss = pred_loss + regularization_loss

    gradients = tape.gradient(total_loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))


for epoch in range(NUM_EPOCHS):
    for inputs, labels in train_data:
        train_step(inputs, labels)
    print("Finished epoch", epoch)
print()

# Take advantage of tf.function with Python control flow

# New-style metrics and losses

# Debugging
