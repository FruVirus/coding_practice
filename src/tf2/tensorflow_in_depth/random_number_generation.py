# pylint: disable=C0114, E1123, E1120, E0102, W0223, R0901, W0703, W0613, R0204
# pylint: disable=E1129, C0102, W0603

# Third Party Library
import tensorflow as tf

physical_devices = tf.config.list_physical_devices("CPU")
tf.config.experimental.set_virtual_device_configuration(
    physical_devices[0],
    [
        tf.config.experimental.VirtualDeviceConfiguration(),
        tf.config.experimental.VirtualDeviceConfiguration(),
        tf.config.experimental.VirtualDeviceConfiguration(),
    ],
)

# The tf.random.Generator class #

g1 = tf.random.Generator.from_seed(1)
print(g1.normal(shape=[2, 3]))
g2 = tf.random.get_global_generator()
print(g2.normal(shape=[2, 3]))

g1 = tf.random.Generator.from_seed(1, alg="philox")
print(g1.normal(shape=[2, 3]))

g = tf.random.Generator.from_non_deterministic_state()
print(g.normal(shape=[2, 3]))

g = tf.random.Generator.from_seed(1)
print(g.normal([]))
print(g.normal([]))
g.reset_from_seed(1)
print(g.normal([]))

# Creating independent random-number streams
g = tf.random.Generator.from_seed(1)
print(g.normal([]))
new_gs = g.split(3)
for new_g in new_gs:
    print(new_g.normal([]))
print(g.normal([]))

with tf.device("cpu"):
    g = tf.random.get_global_generator().split(1)[0]
    print(g.normal([]))

# Interaction with tf.function
g = tf.random.Generator.from_seed(1)


@tf.function
def foo():
    return g.normal([])


print(foo())

g = None


@tf.function  # type: ignore
def foo():
    global g
    if g is None:
        g = tf.random.Generator.from_seed(1)
    return g.normal([])


print(foo())
print(foo())

num_traces = 0


@tf.function  # type: ignore
def foo(g):
    global num_traces
    num_traces += 1
    return g.normal([])


foo(tf.random.Generator.from_seed(1))
foo(tf.random.Generator.from_seed(2))
print(num_traces)

# Interaction with distribution strategies
g = tf.random.Generator.from_seed(1)
strat = tf.distribute.MirroredStrategy(devices=["cpu:0", "cpu:1"])
with strat.scope():

    def f():
        print(g.normal([]))

    results = strat.run(f)
print()

# Stateless RNGs #

print(tf.random.stateless_normal(shape=[2, 3], seed=[1, 2]))
print(tf.random.stateless_normal(shape=[2, 3], seed=[1, 2]))
