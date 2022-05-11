# pylint: disable=C0114, E1123, E1120, E0102, W0223, R0901, W0703, W0613, R0204

# Third Party Library
import tensorflow as tf

# Defining models and layers in TensorFlow #


class SimpleModule(tf.Module):
    def __init__(self, name=None):
        super().__init__(name=name)
        self.a_variable = tf.Variable(5.0, name="train_me")
        self.non_trainable_variable = tf.Variable(
            5.0, trainable=False, name="do_not_train_me"
        )

    def __call__(self, x):
        return self.a_variable * x + self.non_trainable_variable


simple_module = SimpleModule(name="simple")
simple_module(tf.constant(5.0))
print("trainable variables:", simple_module.trainable_variables)
print("all variables:", simple_module.variables)


class Dense(tf.Module):
    def __init__(self, in_features, out_features, name=None):
        super().__init__(name=name)
        self.w = tf.Variable(tf.random.normal([in_features, out_features]), name="w")
        self.b = tf.Variable(tf.zeros([out_features]), name="b")

    def __call__(self, x):
        y = tf.matmul(x, self.w) + self.b
        return tf.nn.relu(y)


class SequentialModule(tf.Module):
    def __init__(self, name=None):
        super().__init__(name=name)
        self.dense_1 = Dense(in_features=3, out_features=3)
        self.dense_2 = Dense(in_features=3, out_features=2)

    def __call__(self, x):
        x = self.dense_1(x)
        return self.dense_2(x)


my_model = SequentialModule(name="the_model")
print("Model results:", my_model(tf.constant([[2.0, 2.0, 2.0]])))
print("Submodules:", my_model.submodules)
for var in my_model.variables:
    print(var, "\n")
print()

# Waiting to create variables


class FlexibleDenseModule(tf.Module):
    def __init__(self, out_features, name=None):
        super().__init__(name=name)
        self.is_built = False
        self.out_features = out_features

    def __call__(self, x):
        if not self.is_built:
            self.w = tf.Variable(
                tf.random.normal([x.shape[-1], self.out_features]), name="w"
            )
            self.b = tf.Variable(tf.zeros([self.out_features]), name="b")
            self.is_built = True
        y = tf.matmul(x, self.w) + self.b
        return tf.nn.relu(y)


class MySequentialModule(tf.Module):
    def __init__(self, name=None):
        super().__init__(name=name)
        self.dense_1 = FlexibleDenseModule(out_features=3)
        self.dense_2 = FlexibleDenseModule(out_features=2)

    def __call__(self, x):
        x = self.dense_1(x)
        return self.dense_2(x)


my_model = MySequentialModule(name="the_model")
print("Model results:", my_model(tf.constant([[2.0, 2.0, 2.0]])))
print()

# Keras models and layers #


# Keras layers
class MyDense(tf.keras.layers.Layer):
    def __init__(self, in_features, out_features, **kwargs):
        super().__init__(**kwargs)
        self.w = tf.Variable(tf.random.normal([in_features, out_features]), name="w")
        self.b = tf.Variable(tf.zeros([out_features]), name="b")

    def call(self, x):
        y = tf.matmul(x, self.w) + self.b
        return tf.nn.relu(y)


simple_layer = MyDense(name="simple", in_features=3, out_features=3)
print(simple_layer([[2.0, 2.0, 2.0]]))


# The build step
class FlexibleDense(tf.keras.layers.Layer):
    def __init__(self, out_features, **kwargs):
        super().__init__(**kwargs)
        self.out_features = out_features

    def build(self, input_shape):
        self.w = tf.Variable(
            tf.random.normal([input_shape[-1], self.out_features]), name="w"
        )
        self.b = tf.Variable(tf.zeros([self.out_features]), name="b")

    def call(self, inputs):
        return tf.matmul(inputs, self.w) + self.b


flexible_dense = FlexibleDense(out_features=3)
print("Model results:", flexible_dense(tf.constant([[2.0, 2.0, 2.0], [3.0, 3.0, 3.0]])))
try:
    print("Model results:", flexible_dense(tf.constant([[2.0, 2.0, 2.0, 2.0]])))
except tf.errors.InvalidArgumentError as e:
    print("Failed:", e)


# Keras models
class MySequentialModel(tf.keras.Model):
    def __init__(self, name=None, **kwargs):
        super().__init__(**kwargs)
        self.dense_1 = FlexibleDense(out_features=3)
        self.dense_2 = FlexibleDense(out_features=2)

    def call(self, x):
        x = self.dense_1(x)
        return self.dense_2(x)


my_sequential_model = MySequentialModel(name="the_model")
print("Model results:", my_sequential_model(tf.constant([[2.0, 2.0, 2.0]])))

inputs = tf.keras.Input(
    shape=[
        3,
    ]
)
x = FlexibleDense(3)(inputs)
x = FlexibleDense(2)(x)
my_functional_model = tf.keras.Model(inputs=inputs, outputs=x)
my_functional_model.summary()
print(my_functional_model(tf.constant([[2.0, 2.0, 2.0]])))
