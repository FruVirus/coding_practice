# pylint: disable=C0114, E1123, E1120, E0102, W0223, R0901

# Third Party Library
import matplotlib
import tensorflow as tf

from matplotlib import pyplot as plt

matplotlib.rcParams["figure.figsize"] = [9, 6]

# Tensors #

x = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
print(x)
print(x.shape)
print(x.dtype)
print(x + x)
print(5 * x)
print(x @ tf.transpose(x))
print(tf.concat([x, x, x], axis=0))
print(tf.nn.softmax(x, axis=-1))
print(tf.reduce_sum(x))
if tf.config.list_physical_devices("GPU"):
    print("TensorFlow **IS** using the GPU")
else:
    print("TensorFlow **IS NOT** using the GPU")
print()

# Variables #

var = tf.Variable([0.0, 0.0, 0.0])
var.assign([1, 2, 3])
print(var)
var.assign_add([1, 1, 1])
print(var)
print()

# Automatic differentiation #

x = tf.Variable(1.0)


def f(x):
    y = x ** 2 + 2 * x - 5
    return y


print(f(x))
with tf.GradientTape() as tape:
    y = f(x)
g_x = tape.gradient(y, x)
print(g_x)
print()

# Graphs and tf.function #


@tf.function
def my_func(x):
    print("Tracing.\n")
    return tf.reduce_sum(x)


x = tf.constant([1, 2, 3])
my_func(x)
x = tf.constant([10, 9, 8])
my_func(x)
x = tf.constant([10.0, 9.1, 8.2], dtype=tf.float32)
my_func(x)
print()

# Modules, layers, and models #


class MyModule(tf.Module):
    def __init__(self, value):
        self.weight = tf.Variable(value)

    @tf.function
    def multiply(self, x):
        return x * self.weight


mod = MyModule(3)
mod.multiply(tf.constant([1, 2, 3]))
save_path = "./saved"
tf.saved_model.save(mod, save_path)
reloaded = tf.saved_model.load(save_path)
print(reloaded.multiply(tf.constant([1, 2, 3])))
print()

# Training loops #

x = tf.linspace(-2, 2, 201)
x = tf.cast(x, tf.float32)


def f(x):  # type: ignore
    y = x ** 2 + 2 * x - 5
    return y


y = f(x) + tf.random.normal(shape=[201])

plt.plot(x.numpy(), y.numpy(), ".", label="Data")
plt.plot(x, f(x), label="Ground truth")
plt.legend()
# plt.show()


class Model(tf.keras.Model):
    def __init__(self, units):
        super().__init__()
        self.dense1 = tf.keras.layers.Dense(
            units=units,
            activation=tf.nn.relu,
            kernel_initializer=tf.random.normal,
            bias_initializer=tf.random.normal,
        )
        self.dense2 = tf.keras.layers.Dense(1)

    def call(self, x, training=True):
        # For Keras layers/models, implement `call` instead of `__call__`.
        x = x[:, tf.newaxis]
        x = self.dense1(x)
        x = self.dense2(x)
        return tf.squeeze(x, axis=1)


model = Model(64)
plt.plot(x.numpy(), y.numpy(), ".", label="data")
plt.plot(x, f(x), label="Ground truth")
plt.plot(x, model(x), label="Untrained predictions")
plt.title("Before training")
plt.legend()

variables = model.variables
optimizer = tf.optimizers.SGD(learning_rate=0.01)
for step in range(1000):
    with tf.GradientTape() as tape:
        prediction = model(x)
        error = (y - prediction) ** 2
        mean_error = tf.reduce_mean(error)
    gradient = tape.gradient(mean_error, variables)
    optimizer.apply_gradients(zip(gradient, variables))
    if step % 100 == 0:
        print(f"Mean squared error: {mean_error.numpy():0.3f}")

plt.plot(x.numpy(), y.numpy(), ".", label="data")
plt.plot(x, f(x), label="Ground truth")
plt.plot(x, model(x), label="Trained predictions")
plt.title("After training")
plt.legend()

new_model = Model(64)
new_model.compile(
    loss=tf.keras.losses.MSE, optimizer=tf.optimizers.SGD(learning_rate=0.01)
)

history = new_model.fit(x, y, epochs=100, batch_size=32, verbose=0)

model.save("./my_model")
plt.plot(history.history["loss"])
plt.xlabel("Epoch")
plt.ylim([0, max(plt.ylim())])
plt.ylabel("Loss [Mean Squared Error]")
plt.title("Keras training progress")
