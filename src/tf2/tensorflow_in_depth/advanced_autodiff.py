# pylint: disable=C0114, E1123, E1120, E0102, W0223, R0901, W0703, W0613, R0204, E1129

# Third Party Library
import matplotlib as mpl
import matplotlib.pyplot as plt
import tensorflow as tf

mpl.rcParams["figure.figsize"] = (8, 6)

# Controlling gradient recording #

# Stop recording
x = tf.Variable(2.0)
y = tf.Variable(3.0)

with tf.GradientTape() as t:
    x_sq = x * x
    with t.stop_recording():
        y_sq = y * y
    z = x_sq + y_sq

grad = t.gradient(z, {"x": x, "y": y})
print("dz/dx:", grad["x"])
print("dz/dy:", grad["y"])

# Reset/start recording from scratch
x = tf.Variable(2.0)
y = tf.Variable(3.0)
reset = True
with tf.GradientTape() as t:
    y_sq = y * y
    if reset:
        t.reset()
    z = x * x + y_sq

grad = t.gradient(z, {"x": x, "y": y})
print("dz/dx:", grad["x"])
print("dz/dy:", grad["y"])

# Stop gradient flow with precision #
x = tf.Variable(2.0)
y = tf.Variable(3.0)
with tf.GradientTape() as t:
    y_sq = y ** 2
    z = x ** 2 + tf.stop_gradient(y_sq)

grad = t.gradient(z, {"x": x, "y": y})
print("dz/dx:", grad["x"])
print("dz/dy:", grad["y"])
print()

# Custom gradients #


@tf.custom_gradient
def clip_gradients(y):
    def backward(dy):
        return tf.clip_by_norm(dy, 0.5)

    return y, backward


v = tf.Variable(2.0)
with tf.GradientTape() as t:
    output = clip_gradients(v * v)
print(t.gradient(output, v))
print()

# Multiple tapes #

x0 = tf.constant(0.0)
x1 = tf.constant(0.0)
with tf.GradientTape() as tape0, tf.GradientTape() as tape1:
    tape0.watch(x0)
    tape1.watch(x1)

    y0 = tf.math.sin(x0)
    y1 = tf.nn.sigmoid(x1)

    y = y0 + y1
    ys = tf.reduce_sum(y)

print(tape0.gradient(ys, x0).numpy())
print(tape1.gradient(ys, x1).numpy())

# Higher-order gradients
x = tf.Variable(1.0)
with tf.GradientTape() as t2:
    with tf.GradientTape() as t1:
        y = x * x * x
    dy_dx = t1.gradient(y, x)
d2y_dx2 = t2.gradient(dy_dx, x)

print("dy_dx:", dy_dx.numpy())
print("d2y_dx2:", d2y_dx2.numpy())
print()

# Jacobians #

# Scalar source
x = tf.linspace(-10.0, 10.0, 200 + 1)
delta = tf.Variable(0.0)
with tf.GradientTape() as tape:
    y = tf.nn.sigmoid(x + delta)
dy_dx = tape.jacobian(y, delta)
print(y.shape)
print(dy_dx.shape)

plt.plot(x.numpy(), y, label="y")
plt.plot(x.numpy(), dy_dx, label="dy/dx")
plt.legend()
_ = plt.xlabel("x")

# Tensor source
x = tf.random.normal([7, 5])
layer = tf.keras.layers.Dense(10, activation=tf.nn.relu)
with tf.GradientTape(persistent=True) as tape:
    y = layer(x)

print(y.shape)
print(layer.kernel.shape)

j = tape.jacobian(y, layer.kernel)
print(j.shape)

g = tape.gradient(y, layer.kernel)
print("g.shape:", g.shape)

j_sum = tf.reduce_sum(j, axis=[0, 1])
delta = tf.reduce_max(abs(g - j_sum)).numpy()
assert delta < 1e-3
print("delta:", delta)

# Batch Jacobian
x = tf.random.normal([7, 5])

layer1 = tf.keras.layers.Dense(8, activation=tf.nn.elu)
layer2 = tf.keras.layers.Dense(6, activation=tf.nn.elu)

with tf.GradientTape(persistent=True, watch_accessed_variables=False) as tape:
    tape.watch(x)
    y = layer1(x)
    y = layer2(y)

print(y.shape)
j = tape.jacobian(y, x)
print(j.shape)

j_sum = tf.reduce_sum(j, axis=2)
print(j_sum.shape)
j_select = tf.einsum("bxby->bxy", j)
print(j_select.shape)

jb = tape.batch_jacobian(y, x)
print(jb.shape)
error = tf.reduce_max(abs(jb - j_sum))
assert error < 1e-3
print(error.numpy())
