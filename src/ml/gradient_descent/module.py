"""How to Implement Gradient Descent

Gradient descent is an iterative algorithm that is used to find a local minimum of a
differentiable function.

In Machine Learning, gradient descent is used to minimize a cost function and to find
the corresponding optimal parameters of a model.

A cost function is a function to measure the deviation of our model's prediction from
the ground truth.

Gradient descent works by picking a learning rate, alpha, simultaneously updating the
model parameters, and iterating until a negligible change occurs for the cost function.

Gradient descent moves a point in the negative direction of the slope (tangent) of the
function at that point. By iteratively doing this process, gradient descent will find a
local minimum.

Stochastic Gradient Descent
---------------------------

A recurring problem in machine learning is thta large training sets are necessary for
good generalization, but large training sets are also more computationally expensive.

The cost function used by a machine learning algorithm often decomposes as a sum over
training examples of some per-example loss function. The computational cost of gradient
descent is then O(m), where m is the number of training examples. As the training set
size grows to billions of examples, the time to take a single gradient step becomes
prohibitively large.

The insight of SGD is that the gradient is an expectation. The expectation may be
approximately estimated using a small set of samples. Specifically, one each step of the
algorithm, we can sample a mini-batch of examples drawn uniformly from the training set.
Crucially, the mini-batch size is held fixed as the training set size m grows. Thus, we
may fit a training set with billions of examples using updates computed on only a
hundred examples.

For a fixed model size, the cost per SGD update does not depend on the training set size
m. In practice, we often use a larger model as the training set size increases, but we
are not foreced to do so. The number of updates required to reach convergence usually
increases with training set size. However, as m approaches infinity, the model will
eventually converge to its best possible test error before SGD has sampled every example
in the training set. Increasing m further will not extend the amount of training time
needed to reach the model's best possible test error.
"""

# f(w) = 3 * w_0 ** 2 + 4 * w_1 ** 2 - 5 * w_0 + 7


def f(w):
    return 3 * w[0] ** 2 + 4 * w[1] ** 2 - 5 * w[0] + 7


def grad(w):
    g = [0] * 2
    g[0] = 6 * w[0] - 5
    g[1] = 8 * w[1]
    return g


def gradient_descent(w_prev, w_new, lr):
    print(w_prev)
    print(f(w_prev))
    while True:
        w_prev = w_new
        w_0 = w_prev[0] - lr * grad(w_prev)[0]
        w_1 = w_prev[1] - lr * grad(w_prev)[1]
        w_new = [w_0, w_1]  # simultaneous update
        print(w_new)
        print(f(w_new))
        if (w_new[0] - w_prev[0]) ** 2 + (w_new[1] - w_prev[1]) ** 2 < pow(10, -6):
            break


gradient_descent([5, 10], [5, 10], 0.03)
