# pylint: disable=C0114, E1123, E1120, E0102, W0223, R0901, W0703

# Third Party Library
import numpy as np
import tensorflow as tf

# Basics #

rank_0_tensor = tf.constant(4)
print(rank_0_tensor)
rank_1_tensor = tf.constant([2.0, 3.0, 4.0])
print(rank_1_tensor)
rank_2_tensor = tf.constant([[1, 2], [3, 4], [5, 6]], dtype=tf.float16)
print(rank_2_tensor)
rank_3_tensor = tf.constant(
    [
        [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]],
        [[10, 11, 12, 13, 14], [15, 16, 17, 18, 19]],
        [[20, 21, 22, 23, 24], [25, 26, 27, 28, 29]],
    ]
)

print(rank_3_tensor)
print(np.array(rank_2_tensor))
print(rank_2_tensor.numpy())
a = tf.constant([[1, 2], [3, 4]])
b = tf.constant([[1, 1], [1, 1]])

print(tf.add(a, b), "\n")
print(tf.multiply(a, b), "\n")
print(tf.matmul(a, b), "\n")
c = tf.constant([[4.0, 5.0], [10.0, 1.0]])

print(tf.reduce_max(c))
print(tf.math.argmax(c))
print(tf.nn.softmax(c))

# About shapes
rank_4_tensor = tf.zeros([3, 2, 4, 5])
print("Type of every element:", rank_4_tensor.dtype)
print("Number of axes:", rank_4_tensor.ndim)
print("Shape of tensor:", rank_4_tensor.shape)
print("Elements along axis 0 of tensor:", rank_4_tensor.shape[0])
print("Elements along the last axis of tensor:", rank_4_tensor.shape[-1])
print("Total number of elements (3*2*4*5): ", tf.size(rank_4_tensor).numpy())
print()

# Indexing #

# Single-axis indexing
rank_1_tensor = tf.constant([0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
print(rank_1_tensor.numpy())
print("First:", rank_1_tensor[0].numpy())
print("Second:", rank_1_tensor[1].numpy())
print("Last:", rank_1_tensor[-1].numpy())

print("Everything:", rank_1_tensor[:].numpy())
print("Before 4:", rank_1_tensor[:4].numpy())
print("From 4 to the end:", rank_1_tensor[4:].numpy())
print("From 2, before 7:", rank_1_tensor[2:7].numpy())
print("Every other item:", rank_1_tensor[::2].numpy())
print("Reversed:", rank_1_tensor[::-1].numpy())

# Multi-axis indexing
print(rank_2_tensor.numpy())
print(rank_2_tensor[1, 1].numpy())
print("Second row:", rank_2_tensor[1, :].numpy())
print("Second column:", rank_2_tensor[:, 1].numpy())
print("Last row:", rank_2_tensor[-1, :].numpy())
print("First item in last column:", rank_2_tensor[0, -1].numpy())
print("Skip the first row:")
print(rank_2_tensor[1:, :].numpy(), "\n")
print(rank_3_tensor[:, :, 4])
print()

# Manipulating Shapes #

x = tf.constant([[1], [2], [3]])
print(x.shape)
print(x.shape.as_list())
reshaped = tf.reshape(x, [1, 3])
print(x.shape)
print(reshaped.shape)
print(rank_3_tensor)
print(tf.reshape(rank_3_tensor, [-1]))
print(tf.reshape(rank_3_tensor, [3 * 2, 5]), "\n")
print(tf.reshape(rank_3_tensor, [3, -1]))
print(tf.reshape(rank_3_tensor, [2, 3, 5]), "\n")
print(tf.reshape(rank_3_tensor, [5, 6]), "\n")
try:
    tf.reshape(rank_3_tensor, [7, -1])
except Exception as e:
    print(f"{type(e).__name__}: {e}")
print()

# More on DTypes #

the_f64_tensor = tf.constant([2.2, 3.3, 4.4], dtype=tf.float64)
the_f16_tensor = tf.cast(the_f64_tensor, dtype=tf.float16)
the_u8_tensor = tf.cast(the_f16_tensor, dtype=tf.uint8)
print(the_u8_tensor)
print()

# Broadcasting #

x = tf.constant([1, 2, 3])
y = tf.constant(2)
z = tf.constant([2, 2, 2])
print(tf.multiply(x, 2))
print(x * y)
print(x * z)
x = tf.reshape(x, [3, 1])
y = tf.range(1, 5)
print(x, "\n")
print(y, "\n")
print(tf.multiply(x, y))
x_stretch = tf.constant([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]])
y_stretch = tf.constant([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
print(x_stretch * y_stretch)
print(tf.broadcast_to(tf.constant([1, 2, 3]), [3, 3]))
print()

# Ragged Tensors #
ragged_list = [[0, 1, 2, 3], [4, 5], [6, 7, 8], [9]]
try:
    tensor = tf.constant(ragged_list)
except Exception as e:
    print(f"{type(e).__name__}: {e}")
ragged_tensor = tf.ragged.constant(ragged_list)
print(ragged_tensor)
print(ragged_tensor.shape)
print()

# String tensors #

scalar_string_tensor = tf.constant("Gray wolf")
print(scalar_string_tensor)
tensor_of_strings = tf.constant(["Gray wolf", "Quick brown fox", "Lazy dog"])
print(tensor_of_strings)
print(tf.constant("🥳👍"))
print(tf.strings.split(scalar_string_tensor, sep=" "))
print(tf.strings.split(tensor_of_strings))
text = tf.constant("1 10 100")
print(tf.strings.to_number(tf.strings.split(text, " ")))
byte_strings = tf.strings.bytes_split(tf.constant("Duck"))
byte_ints = tf.io.decode_raw(tf.constant("Duck"), tf.uint8)
print("Byte strings:", byte_strings)
print("Bytes:", byte_ints)
unicode_bytes = tf.constant("アヒル 🦆")
unicode_char_bytes = tf.strings.unicode_split(unicode_bytes, "UTF-8")
unicode_values = tf.strings.unicode_decode(unicode_bytes, "UTF-8")
print("\nUnicode bytes:", unicode_bytes)
print("\nUnicode chars:", unicode_char_bytes)
print("\nUnicode values:", unicode_values)
print()

# Sparse tensors #

sparse_tensor = tf.sparse.SparseTensor(
    indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4]
)
print(sparse_tensor, "\n")
print(tf.sparse.to_dense(sparse_tensor))
