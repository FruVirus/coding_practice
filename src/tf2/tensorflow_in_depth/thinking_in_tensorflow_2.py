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


class DynamicRNN(tf.keras.Model):
    def __init__(self, rnn_cell):
        super().__init__(self)
        self.cell = rnn_cell

    @tf.function(
        input_signature=[tf.TensorSpec(dtype=tf.float32, shape=[None, None, 3])]
    )
    def call(self, input_data):
        input_data = tf.transpose(input_data, [1, 0, 2])
        timesteps = tf.shape(input_data)[0]
        batch_size = tf.shape(input_data)[1]
        outputs = tf.TensorArray(tf.float32, timesteps)
        state = self.cell.get_initial_state(batch_size=batch_size, dtype=tf.float32)
        for i in tf.range(timesteps):
            output, state = self.cell(input_data[i], state)
            outputs = outputs.write(i, output)
        return tf.transpose(outputs.stack(), [1, 0, 2]), state


lstm_cell = tf.keras.layers.LSTMCell(units=13)
my_rnn = DynamicRNN(lstm_cell)
outputs, state = my_rnn(tf.random.normal(shape=[10, 20, 3]))
print(outputs.shape)

# New-style metrics and losses
cce = tf.keras.losses.CategoricalCrossentropy(from_logits=True)
print(cce([[1, 0]], [[-1.0, 3.0]]).numpy())

loss_metric = tf.keras.metrics.Mean(name="train_loss")
accuracy_metric = tf.keras.metrics.SparseCategoricalAccuracy(name="train_accuracy")


@tf.function  # type: ignore
def train_step(inputs, labels):
    with tf.GradientTape() as tape:
        predictions = model(inputs, training=True)
        regularization_loss = tf.math.add_n(model.losses)
        pred_loss = loss_fn(labels, predictions)
        total_loss = pred_loss + regularization_loss

    gradients = tape.gradient(total_loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))

    loss_metric.update_state(total_loss)
    accuracy_metric.update_state(labels, predictions)


for epoch in range(NUM_EPOCHS):
    loss_metric.reset_states()
    accuracy_metric.reset_states()

    for inputs, labels in train_data:
        train_step(inputs, labels)

    mean_loss = loss_metric.result()
    mean_accuracy = accuracy_metric.result()

    print("Epoch: ", epoch)
    print("  loss:     {:.3f}".format(mean_loss))
    print("  accuracy: {:.3f}".format(mean_accuracy))

# Debugging


@tf.function
def f(x):
    if x > 0:
        # Standard Library
        import pdb

        pdb.set_trace()
        x = x + 1
    return x


tf.config.run_functions_eagerly(True)
f(tf.constant(1))


class CustomModel(tf.keras.models.Model):
    @tf.function
    def call(self, input_data):
        if tf.reduce_mean(input_data) > 0:
            return input_data
        # Standard Library
        import pdb

        pdb.set_trace()
        return input_data // 2


tf.config.run_functions_eagerly(True)
model = CustomModel()
model(tf.constant([-2, -4]))
