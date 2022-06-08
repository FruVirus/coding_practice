"""Linear classifier."""

# pylint: disable=E1120, W1114

# Third Party Library
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

# Generate data
num_samples_per_class = 1000
negative_samples = np.random.multivariate_normal(
    mean=[0, 3],
    cov=[[1, 0.5], [0.5, 1]],
    size=num_samples_per_class,
)
positive_samples = np.random.multivariate_normal(
    mean=[3, 0],
    cov=[[1, 0.5], [0.5, 1]],
    size=num_samples_per_class,
)

inputs = np.vstack((negative_samples, positive_samples)).astype(np.float32)
targets = np.vstack(
    (
        np.zeros((num_samples_per_class, 1), dtype="float32"),
        np.ones((num_samples_per_class, 1), dtype="float32"),
    )
)

# Plot data
# plt.scatter(inputs[:, 0], inputs[:, 1], c=targets[:, 0])
# plt.show()

# Create the linear classifier variables
input_dim = 2
output_dim = 1
W = tf.Variable(initial_value=tf.random.uniform(shape=(input_dim, output_dim)))
b = tf.Variable(initial_value=tf.zeros(shape=(output_dim,)))


# Define the forward pass
def model(inputs):
    return tf.matmul(inputs, W) + b


# Define the loss function.
def square_loss(targets, predictions):
    per_sample_losses = tf.square(targets - predictions)
    return tf.reduce_mean(per_sample_losses)


# Define the training step
def training_step(inputs, targets, lr=0.1):
    with tf.GradientTape() as tape:
        predictions = model(inputs)
        loss = square_loss(predictions, targets)
    grads = tape.gradient(loss, [W, b])
    W.assign_sub((grads[0] * lr))
    b.assign_sub((grads[1] * lr))
    return loss


# Define the training loop
for step in range(40):
    loss = training_step(inputs, targets)
    print(f"Loss at step {step}: {loss: .4f}")


# Run prediction
predictions = model(inputs)
x = np.linspace(-1, 4, 100)
y = (-W[0] * x + (0.5 - b)) / W[1]
plt.plot(x, y, "-r")
plt.scatter(inputs[:, 0], inputs[:, 1], c=predictions[:, 0] > 0.5)
plt.show()
