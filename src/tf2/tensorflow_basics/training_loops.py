# pylint: disable=C0114, E1123, E1120, E0102, W0223, R0901, W0703, W0613, R0204

# Third Party Library
import matplotlib.pyplot as plt
import tensorflow as tf

colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]

# Data #

TRUE_W = 3.0
TRUE_B = 2.0
NUM_EXAMPLES = 201

x = tf.linspace(-2, 2, NUM_EXAMPLES)
x = tf.cast(x, tf.float32)


def f(x):
    return x * TRUE_W + TRUE_B


noise = tf.random.normal(shape=[NUM_EXAMPLES])
y = f(x) + noise

plt.plot(x, y, ".")
# plt.show()
print()

# Define the model #


class MyModel(tf.Module):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.w = tf.Variable(5.0)
        self.b = tf.Variable(0.0)

    def __call__(self, x):
        return self.w * x + self.b


model = MyModel()
print("Variables:", model.variables)
assert model(3.0).numpy() == 15.0

# Define a loss function


def loss(target_y, predicted_y):
    return tf.reduce_mean(tf.square(target_y - predicted_y))


plt.plot(x, y, ".", label="Data")
plt.plot(x, f(x), label="Ground truth")
plt.plot(x, model(x), label="Predictions")
plt.legend()
# plt.show()

print("Current loss: %1.6f" % loss(y, model(x)).numpy())

# Define a training loop


def train(model, x, y, learning_rate):
    with tf.GradientTape() as t:
        current_loss = loss(y, model(x))
    dw, db = t.gradient(current_loss, [model.w, model.b])
    model.w.assign_sub(learning_rate * dw)
    model.b.assign_sub(learning_rate * db)


model = MyModel()
weights = []
biases = []
epochs = range(10)


def report(model, loss):
    return f"W = {model.w.numpy():1.2f}, b = {model.b.numpy():1.2f}, loss={loss:2.5f}"


def training_loop(model, x, y):
    for epoch in epochs:
        train(model, x, y, learning_rate=0.1)

        weights.append(model.w.numpy())
        biases.append(model.b.numpy())
        current_loss = loss(y, model(x))

        print(f"Epoch {epoch:2d}:")
        print("    ", report(model, current_loss))


current_loss = loss(y, model(x))

print("Starting:")
print("    ", report(model, current_loss))

training_loop(model, x, y)

plt.plot(epochs, weights, label="Weights", color=colors[0])
plt.plot(epochs, [TRUE_W] * len(epochs), "--", label="True weight", color=colors[0])

plt.plot(epochs, biases, label="bias", color=colors[1])
plt.plot(epochs, [TRUE_B] * len(epochs), "--", label="True bias", color=colors[1])

plt.legend()
# plt.show()

plt.plot(x, y, ".", label="Data")
plt.plot(x, f(x), label="Ground truth")
plt.plot(x, model(x), label="Predictions")
plt.legend()
# plt.show()

print("Current loss: %1.6f" % loss(model(x), y).numpy())
print()

# The same solution, but with Keras #


class MyModelKeras(tf.keras.Model):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.w = tf.Variable(5.0)
        self.b = tf.Variable(0.0)

    def call(self, x):
        return self.w * x + self.b


keras_model = MyModelKeras()
training_loop(keras_model, x, y)

keras_model = MyModelKeras()
keras_model.compile(
    run_eagerly=False,
    optimizer=tf.keras.optimizers.SGD(learning_rate=0.1),
    loss=tf.keras.losses.mean_squared_error,
)
print(x.shape[0])
keras_model.fit(x, y, epochs=10, batch_size=1000)
