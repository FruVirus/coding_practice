# pylint: disable=C0114, E1123, E1120, E0102, W0223, R0901, W0703

# Third Party Library
import tensorflow as tf

tf.debugging.set_log_device_placement(True)

# Create a variable #

my_tensor = tf.constant([[1.0, 2.0], [3.0, 4.0]])
my_variable = tf.Variable(my_tensor)
bool_variable = tf.Variable([False, False, False, True])
complex_variable = tf.Variable([5 + 4j, 6 + 1j])
print("Shape: ", my_variable.shape)
print("DType: ", my_variable.dtype)
print("As NumPy: ", my_variable.numpy())
print("A variable:", my_variable)
print("\nViewed as a tensor:", tf.convert_to_tensor(my_variable))
print("\nIndex of highest value:", tf.math.argmax(my_variable))
print("\nCopying and reshaping: ", tf.reshape(my_variable, [1, 4]))
a = tf.Variable([2.0, 3.0])
a.assign([1, 2])
try:
    a.assign([1.0, 2.0, 3.0])
except Exception as e:
    print(f"{type(e).__name__}: {e}")
a = tf.Variable([2.0, 3.0])
b = tf.Variable(a)
a.assign([5, 6])
print(a.numpy())
print(b.numpy())
print(a.assign_add([2, 3]).numpy())
print(a.assign_sub([7, 9]).numpy())
print()

# Lifecycles, naming, and watching #

a = tf.Variable(my_tensor, name="Mark")
b = tf.Variable(my_tensor + 1, name="Mark")
print(a == b)
step_counter = tf.Variable(1, trainable=False)
print()

# Placing variables and tensors #

print(666666666666666666666666)

with tf.device("CPU:0"):
    a = tf.Variable([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    c = tf.matmul(a, b)

print(c)

with tf.device("CPU:0"):
    a = tf.Variable([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    b = tf.Variable([[1.0, 2.0, 3.0]])
with tf.device("GPU:0"):
    k = a * b

print(k)
