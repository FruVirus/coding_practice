# pylint: disable=C0114, E1123, E1120, E0102, W0223, R0901, W0703

# Standard Library
import timeit

# Third Party Library
import tensorflow as tf

# Taking advantage of graphs #


def a_regular_function(x, y, b):
    x = tf.matmul(x, y)
    x = x + b
    return x


a_function_that_uses_a_graph = tf.function(a_regular_function)

x1 = tf.constant([[1.0, 2.0]])
y1 = tf.constant([[2.0], [3.0]])
b1 = tf.constant(4.0)
orig_value = a_regular_function(x1, y1, b1).numpy()
tf_function_value = a_function_that_uses_a_graph(x1, y1, b1).numpy()
assert orig_value == tf_function_value


def inner_function(x, y, b):
    x = tf.matmul(x, y)
    x = x + b
    return x


@tf.function
def outer_function(x):
    y = tf.constant([[2.0], [3.0]])
    b = tf.constant(4.0)
    return inner_function(x, y, b)


print(outer_function(tf.constant([[1.0, 2.0]])).numpy())
print()

# Converting Python functions to graphs #


def simple_relu(x):
    if tf.greater(x, 0):
        return x
    return 0


tf_simple_relu = tf.function(simple_relu)
print("First branch, with graph:", tf_simple_relu(tf.constant(1)).numpy())
print("Second branch, with graph:", tf_simple_relu(tf.constant(-1)).numpy())
print(tf.autograph.to_code(simple_relu))
print(tf_simple_relu.get_concrete_function(tf.constant(1)).graph.as_graph_def())
print()

# Polymorphism: one Function, many graphs #


@tf.function
def my_relu(x):
    return tf.maximum(0.0, x)


print(my_relu(tf.constant(5.5)))
print(my_relu([1, -1]))
print(my_relu(tf.constant([3.0, -3.0])))
print(my_relu(tf.constant(-2.5)))
print(my_relu(tf.constant([-1.0, 1.0])))
print(my_relu.pretty_printed_concrete_signatures())
print()

# Using tf.function #

# Graph execution vs. eager execution


@tf.function
def get_MSE(y_true, y_pred):
    sq_diff = tf.pow(y_true - y_pred, 2)
    return tf.reduce_mean(sq_diff)


y_true = tf.random.uniform([5], maxval=10, dtype=tf.int32)
y_pred = tf.random.uniform([5], maxval=10, dtype=tf.int32)
print(y_true)
print(y_pred)
print(get_MSE(y_true, y_pred))
tf.config.run_functions_eagerly(True)
print(get_MSE(y_true, y_pred))
tf.config.run_functions_eagerly(False)
print()

# Non-strict execution


def unused_return_eager(x):
    tf.gather(x, [1])
    return x


try:
    print(unused_return_eager(tf.constant([0.0])))
except tf.errors.InvalidArgumentError as e:
    print(f"{type(e).__name__}: {e}")


@tf.function
def unused_return_graph(x):
    tf.gather(x, [1])
    return x


print(unused_return_graph(tf.constant([0.0])))
print()

# Seeing the speed-up #

x = tf.random.uniform(shape=[10, 10], minval=-1, maxval=2, dtype=tf.dtypes.int32)


def power(x, y):
    result = tf.eye(10, dtype=tf.dtypes.int32)
    for _ in range(y):
        result = tf.matmul(x, result)
    return result


print("Eager execution:", timeit.timeit(lambda: power(x, 100), number=1000))
power_as_graph = tf.function(power)
print("Graph execution:", timeit.timeit(lambda: power_as_graph(x, 100), number=1000))
print()

# When is a Function tracing? #


@tf.function
def a_function_with_python_side_effect(x):
    print("Tracing!")
    return x * x + tf.constant(2)


print(a_function_with_python_side_effect(tf.constant(2)))
print(a_function_with_python_side_effect(tf.constant(3)))
print(a_function_with_python_side_effect(2))
print(a_function_with_python_side_effect(3))
