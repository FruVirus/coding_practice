# pylint: disable=C0114, E1123, E1120, E0102, W0223, R0901, W0703, W0613, R0204

# Third Party Library
import numpy as np
import tensorflow as tf

# Extract tensor slices #

t1 = tf.constant([0, 1, 2, 3, 4, 5, 6, 7])

print(tf.slice(t1, begin=[1], size=[3]))
print(t1[1:4])
print(t1[-3:])

t2 = tf.constant(
    [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]
)

print(t2[:-1, 1:3])

t3 = tf.constant(
    [[[1, 3, 5, 7], [9, 11, 13, 15]], [[17, 19, 21, 23], [25, 27, 29, 31]]]
)
print(t3.shape)
print(tf.slice(t3, begin=[1, 1, 0], size=[1, 1, 2]))

print(tf.gather(t1, indices=[0, 3, 6]))

alphabet = tf.constant(list("abcdefghijklmnopqrstuvwxyz"))
print(tf.gather(alphabet, indices=[2, 0, 19, 18]))

t4 = tf.constant([[0, 5], [1, 6], [2, 7], [3, 8], [4, 9]])
print(tf.gather_nd(t4, indices=[[2], [3], [0]]))

t5 = np.reshape(np.arange(18), [2, 3, 3])
print(t5)
print(tf.gather_nd(t5, indices=[[0, 0, 0], [1, 2, 1]]))
print(tf.gather_nd(t5, indices=[[[0, 0], [0, 2]], [[1, 0], [1, 2]]]))
print(tf.gather_nd(t5, indices=[[0, 0], [0, 2], [1, 0], [1, 2]]))
print()

# Insert data into tensors #

t6 = tf.constant([10])
indices = tf.constant([[1], [3], [5], [7], [9]])
data = tf.constant([2, 4, 6, 8, 10])
print(tf.scatter_nd(indices=indices, updates=data, shape=t6))

new_indices = tf.constant([[0, 2], [2, 1], [3, 3]])
t7 = tf.gather_nd(t2, indices=new_indices)
print(t7)

t8 = tf.scatter_nd(indices=new_indices, updates=t7, shape=tf.constant([4, 5]))
print(t8)

t9 = tf.SparseTensor(
    indices=[[0, 2], [2, 1], [3, 3]], values=[2, 11, 18], dense_shape=[4, 5]
)
print(t9)

t11 = tf.constant([[2, 7, 0], [9, 0, 1], [0, 3, 8]])
t12 = tf.tensor_scatter_nd_add(t11, indices=[[0, 2], [1, 1], [2, 0]], updates=[6, 5, 4])
print(t12)

t13 = tf.tensor_scatter_nd_sub(
    t11,
    indices=[[0, 0], [0, 1], [1, 0], [1, 1], [1, 2], [2, 1], [2, 2]],
    updates=[1, 7, 9, -1, 1, 3, 7],
)
print(t13)

t14 = tf.constant([[-2, -7, 0], [-9, 0, 1], [0, -3, -8]])
t15 = tf.tensor_scatter_nd_min(
    t14, indices=[[0, 2], [1, 1], [2, 0]], updates=[-6, -5, -4]
)
print(t15)

t16 = tf.tensor_scatter_nd_max(t14, indices=[[0, 2], [1, 1], [2, 0]], updates=[6, 5, 4])
print(t16)
