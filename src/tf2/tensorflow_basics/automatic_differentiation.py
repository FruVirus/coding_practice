# pylint: disable=C0114, E1123, E1120, E0102, W0223, R0901, W0703

# Third Party Library
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

# Gradient tapes #

x = tf.Variable(3.0)
with tf.GradientTape() as tape:
    y = x ** 2

dy_dx = tape.gradient(y, x)
print(dy_dx.numpy())
w = tf.Variable(tf.random.normal((3, 2)), name="w")
b = tf.Variable(tf.zeros(2, dtype=tf.float32), name="b")
x = [[1.0, 2.0, 3.0]]
with tf.GradientTape(persistent=True) as tape:
    y = x @ w + b
    loss = tf.reduce_mean(y ** 2)
[dl_dw, dl_db] = tape.gradient(loss, [w, b])
print(w.shape, dl_dw.shape)
print(b.shape, dl_db.shape)
my_vars = {"w": w, "b": b}
grad = tape.gradient(loss, my_vars)
print(grad["b"])
print()

# Gradients with respect to a model #

layer = tf.keras.layers.Dense(2, activation="relu")
x = tf.constant([[1.0, 2.0, 3.0]])
with tf.GradientTape() as tape:
    y = layer(x)
    loss = tf.reduce_mean(y ** 2)
grad = tape.gradient(loss, layer.trainable_variables)
for var, g in zip(layer.trainable_variables, grad):
    print(f"{var.name}, shape: {g.shape}")
print()

# Controlling what the tape watches #

# A trainable variable
x0 = tf.Variable(3.0, name="x0")
# Not trainable
x1 = tf.Variable(3.0, name="x1", trainable=False)
# Not a Variable: A variable + tensor returns a tensor.
x2 = tf.Variable(2.0, name="x2") + 1.0
# Not a variable
x3 = tf.constant(3.0, name="x3")
with tf.GradientTape() as tape:
    y = (x0 ** 2) + (x1 ** 2) + (x2 ** 2)
grad = tape.gradient(y, [x0, x1, x2, x3])
for g in grad:
    print(g)
print([var.name for var in tape.watched_variables()])

x = tf.constant(3.0)
with tf.GradientTape() as tape:
    tape.watch(x)
    y = x ** 2
dy_dx = tape.gradient(y, x)
print(dy_dx.numpy())

x0 = tf.Variable(0.0)
x1 = tf.Variable(10.0)
with tf.GradientTape(watch_accessed_variables=False) as tape:
    tape.watch(x1)
    y0 = tf.math.sin(x0)
    y1 = tf.nn.softplus(x1)
    y = y0 + y1
    ys = tf.reduce_sum(y)
grad = tape.gradient(ys, {"x0": x0, "x1": x1})
print("dy/dx0:", grad["x0"])
print("dy/dx1:", grad["x1"].numpy())
print()

# Intermediate results #

x = tf.constant(3.0)
with tf.GradientTape() as tape:
    tape.watch(x)
    y = x * x
    z = y * y
print(tape.gradient(z, y).numpy())

x = tf.constant([1, 3.0])
with tf.GradientTape(persistent=True) as tape:
    tape.watch(x)
    y = x * x
    z = y * y
print(tape.gradient(z, x).numpy())
print(tape.gradient(y, x).numpy())
del tape
print()

# Gradients of non-scalar target #

x = tf.Variable(2.0)
with tf.GradientTape(persistent=True) as tape:
    y0 = x ** 2
    y1 = 1 / x
print(tape.gradient(y0, x).numpy())
print(tape.gradient(y1, x).numpy())

x = tf.Variable(2.0)
with tf.GradientTape() as tape:
    y0 = x ** 2
    y1 = 1 / x
print(tape.gradient({"y0": y0, "y1": y1}, x).numpy())

x = tf.Variable(2.0)

with tf.GradientTape() as tape:
    y = x * [3.0, 4.0]
print(tape.gradient(y, x).numpy())

x = tf.linspace(-10.0, 10.0, 200 + 1)
with tf.GradientTape() as tape:
    tape.watch(x)
    y = tf.nn.sigmoid(x)
dy_dx = tape.gradient(y, x)
plt.plot(x, y, label="y")
plt.plot(x, dy_dx, label="dy/dx")
plt.legend()
_ = plt.xlabel("x")
print()

# Control flow #

x = tf.constant(1.0)
v0 = tf.Variable(2.0)
v1 = tf.Variable(2.0)
with tf.GradientTape(persistent=True) as tape:
    tape.watch(x)
    if x > 0.0:
        result = v0
    else:
        result = v1 ** 2
dv0, dv1 = tape.gradient(result, [v0, v1])
print(dv0)
print(dv1)
dx = tape.gradient(result, x)
print(dx)
print()

# Getting a gradient of None #

x = tf.Variable(2.0)
y = tf.Variable(3.0)
with tf.GradientTape() as tape:
    z = y * y
print(tape.gradient(z, x))

# 1. Replaced a variable with a tensor
x = tf.Variable(2.0)
for epoch in range(2):
    with tf.GradientTape() as tape:
        y = x + 1
    print(type(x).__name__, ":", tape.gradient(y, x))
    x = x + 1
    # x.assign_add(1)

# 2. Did calculations outside of TensorFlow
x = tf.Variable([[1.0, 2.0], [3.0, 4.0]], dtype=tf.float32)
with tf.GradientTape() as tape:
    x2 = x ** 2
    y = np.mean(x2, axis=0)
    y = tf.reduce_mean(y, axis=0)
print(tape.gradient(y, x))

# 3. Took gradients through an integer or string
x = tf.constant(10)
with tf.GradientTape() as g:
    g.watch(x)
    y = x * x
print(g.gradient(y, x))

# 4. Took gradients through a stateful object
x0 = tf.Variable(3.0)
x1 = tf.Variable(0.0)
with tf.GradientTape(persistent=True) as tape:
    x1.assign_add(x0)
    y = x1 ** 2
print(tape.gradient(y, x0))
print(tape.gradient(y, x1))
print()

# No gradient registered #

image = tf.Variable([[[0.5, 0.0, 0.0]]])
delta = tf.Variable(0.1)
with tf.GradientTape() as tape:
    new_image = tf.image.adjust_contrast(image, delta)
try:
    print(tape.gradient(new_image, [image, delta]))
    assert False  # This should not happen.
except LookupError as e:
    print(f"{type(e).__name__}: {e}")
print()

# Zeros instead of None #

x = tf.Variable([2.0, 2.0])
y = tf.Variable(3.0)
with tf.GradientTape() as tape:
    z = y ** 2
print(tape.gradient(z, x, unconnected_gradients=tf.UnconnectedGradients.ZERO))
