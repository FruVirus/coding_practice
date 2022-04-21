# pylint: disable=C0114, E1121, R0204

# Standard Library
import math

# Third Party Library
import numpy as np

# NumPy Tutorial #

# NumPy Getting Started
print(np.__version__)
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print()

# NumpY Creating Arrays
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
a = np.array(42)
print(a, a.ndim)
b = np.array((1, 2, 3, 4, 5))
print(b, b.ndim)
c = np.array([[1, 2, 3], [4, 5, 6]])
print(c, c.ndim)
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(d, d.ndim)
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr, arr.ndim)
print()

# NumPy Array Indexing
arr = np.array([1, 2, 3, 4, 5])
print(arr[0])
print(arr[-1])
print(arr[2] + arr[3])
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0, 1])
print(arr[1, 4])
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, -1])
print(arr[1][-1])
print()

# NumPy Array Slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:])
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2])
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])
print(arr[1][1:4])
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2])
# This will FAIL because arr[0:2] creates another array with only 2 elements.
# print(arr[0:2][2])
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])
print()

# NumPy Data Types
arr = np.array([1, 2, 3, 4])
print(arr.dtype)
arr = np.array(["apple", "banana", "cherry"])
print(arr.dtype)
arr = np.array([1, 2, 3, 4], dtype="S")
print(arr)
print(arr.dtype)
# This will FAIL because "a" is not an integer string and cannot be converted to an
# integer.
# arr = np.array(['a', '2', '3'], dtype='i')
arr = np.array([1.1, 2.1, 3.1])
print(arr, arr.dtype)
newarr = arr.astype("i")
print(newarr, newarr.dtype)
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)
print(newarr, newarr.dtype)
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr, newarr.dtype)
print()

# NumPy Array Copy vs. View
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31
print(arr)
print(x)
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(arr.base)
print(x.base)
print(y.base)
print()

# NumPy Array Shape
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr, arr.shape)
print()

# NumPy Array Reshape
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(arr, arr.base)
print(newarr, newarr.base)
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr, newarr.shape, newarr.base)
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr, newarr.shape)
print()

# NumPy Array Iterating
arr = np.array([1, 2, 3])
for x in arr:
    print(x)
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    print(x)
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    for y in x:
        print(y)
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    print(x)
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    for y in x:
        for z in y:
            print(z)
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
    print(x)
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=["buffered"], op_dtypes=["S"]):
    print(x)
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
    print(x)
arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
    print(idx, x)
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
    print(idx, x)
print()

# NumPy Array Join
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr, arr.base)
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=0)
print(arr, arr.shape, arr.base)
arr = np.concatenate((arr1, arr2), axis=1)
print(arr, arr.shape, arr.base)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=0)
print(arr, arr.base)
arr = np.stack((arr1, arr2), axis=1)
print(arr)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print(arr, arr.base)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))
print(arr, arr.base)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))
print(arr, arr.shape, arr.base)
print()

# NumPy Array Split
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr, newarr[0].base, newarr[1].base, newarr[2].base)
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(newarr)
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)
arr = np.array(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
)
newarr = np.array_split(arr, 3, axis=1)
print(newarr, newarr[0].base)
arr = np.array(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
)
newarr = np.hsplit(arr, 3)
print(newarr, newarr[0].base)
print()

# NumPy Array Search
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr % 2 == 0)
print(x)
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side="right")
print(x)
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)
print()

# NumPy Array Sort
arr = np.array([3, 2, 0, 1])
newarr = np.sort(arr)
print(newarr, newarr.base)
arr = np.array(["banana", "cherry", "apple"])
print(np.sort(arr))
arr = np.array([True, False, True])
print(np.sort(arr))
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr, axis=0))
print(np.sort(arr, axis=1))
print(np.sort(arr))
print()

# NumPy Array Filter
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)
arr = np.array([41, 42, 43, 44])
filter_arr = []
for element in arr:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
print()

# NumPy Random #

# Random Intro
x = np.random.randint(100)
print(x)
x = np.random.rand()
print(x)
x = np.random.randint(100, size=5)
print(x)
x = np.random.randint(100, size=(3, 5))
print(x)
x = np.random.rand(5)
print(x)
x = np.random.rand(3, 5)
print(x)
x = np.random.choice([3, 5, 7, 9])
print(x)
x = np.random.choice([3, 5, 7, 9], size=(3, 5))
print(x)
print()

# Data Distribution
x = np.random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x)
x = np.random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x)
print()

# Random Permutation
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print(arr)
arr = np.array([1, 2, 3, 4, 5])
newarr = np.random.permutation(arr)
print(newarr, newarr.base)
print()

# Seaborn Module
# sns.distplot([0, 1, 2, 3, 4, 5])
# plt.show()
# sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
# plt.show()

# Normal Distribution
x = np.random.normal(size=(2, 3))
print(x)
x = np.random.normal(loc=1, scale=2, size=(2, 3))
print(x)
print()

# Binomial Distribution
x = np.random.binomial(n=10, p=0.5, size=10)
print(x)
print()

# Poisson Distribution
x = np.random.poisson(lam=2, size=10)
print(x)
print()

# Uniform Distribution
x = np.random.uniform(size=(2, 3))
print(x)
print()

# Logistic Distribution
x = np.random.logistic(loc=1, scale=2, size=(2, 3))
print(x)
print()

# Multinomial Distribution
x = np.random.multinomial(n=6, pvals=[1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6])
print(x)
print()

# Exponential Distribution
x = np.random.exponential(scale=2, size=(2, 3))
print(x)
print()

# Chi Square Distribution
x = np.random.chisquare(df=2, size=(2, 3))
print(x)
print()

# Rayleigh Distribution
x = np.random.rayleigh(scale=2, size=(2, 3))
print(x)
print()

# Pareto Distribution
x = np.random.pareto(a=2, size=(2, 3))
print(x)
print()

# Zipf Distribution
x = np.random.zipf(a=2, size=(2, 3))
print(x)
print()

# NumPy ufunc #

# ufunc Intro
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)
print(z)
print()


# ufunc Create Function
def myadd(x, y):
    return x + y


myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))
print(type(np.add))
print(type(np.concatenate))

# ufunc Simple Arithmetic
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.add(arr1, arr2)
print(newarr)
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.subtract(arr1, arr2)
print(newarr)
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.multiply(arr1, arr2)
print(newarr)
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])
newarr = np.divide(arr1, arr2)
print(newarr)
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 6, 8, 2, 33])
newarr = np.power(arr1, arr2)
print(newarr)
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr = np.mod(arr1, arr2)
print(newarr)
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr = np.remainder(arr1, arr2)
print(newarr)
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr = np.divmod(arr1, arr2)
print(newarr)
arr = np.array([-1, -2, 1, 2, 3, -4])
newarr = np.absolute(arr)
print(newarr)
print()

# ufunc Rounding Decimals
arr = np.trunc([-3.1666, 3.6667])
print(arr)
arr = np.fix([-3.1666, 3.6667])
print(arr)
arr = np.around(3.1666, 3)
print(arr)
arr = np.floor([-3.1666, 3.6667])
print(arr)
arr = np.ceil([-3.1666, 3.6667])
print(arr)
print()

# ufunc Logs
arr = np.arange(1, 10)
print(np.log2(arr))
arr = np.arange(1, 10)
print(np.log10(arr))
arr = np.arange(1, 10)
print(np.log(arr))
nplog = np.frompyfunc(math.log, 2, 1)
print(nplog(100, 15))
print()

# ufunc Summations
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2])
print(newarr)
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2], axis=0)
print(newarr)
newarr = np.sum([arr1, arr2], axis=1)
print(newarr)
arr = np.array([1, 2, 3])
newarr = np.cumsum(arr)
print(newarr)
print()

# ufunc Products
arr = np.array([1, 2, 3, 4])
x = np.prod(arr)
print(x)
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
x = np.prod([arr1, arr2])
print(x)
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
newarr = np.prod([arr1, arr2], axis=0)
print(newarr)
newarr = np.prod([arr1, arr2], axis=1)
print(newarr)
arr = np.array([5, 6, 7, 8])
newarr = np.cumprod(arr)
print(newarr)
print()

# ufunc Differences
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr)
print(newarr)
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr, n=2)
print(newarr)
print()

# ufunc Finding LCM
num1 = 4
num2 = 6
x = np.lcm(num1, num2)
print(x)
arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr)
print(x)
arr = np.arange(1, 11)
x = np.lcm.reduce(arr)
print(x)
print()

# ufunc Finding GCD
num1 = 6
num2 = 9
x = np.gcd(num1, num2)
print(x)
arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)
print(x)
print()

# ufunc Trigonometric
x = np.sin(np.pi / 2)
print(x)
arr = np.array([np.pi / 2, np.pi / 3, np.pi / 4, np.pi / 5])
x = np.sin(arr)
print(x)
arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)
print(x)
arr = np.array([np.pi / 2, np.pi, 1.5 * np.pi, 2 * np.pi])
x = np.rad2deg(arr)
print(x)
x = np.arcsin(1.0)
print(x)
arr = np.array([1, -1, 0.1])
x = np.arcsin(arr)
print(x)
base = 3
perp = 4
x = np.hypot(base, perp)
print(x)
print()

# ufunc Hyperbolic
x = np.sinh(np.pi / 2)
print(x)
arr = np.array([np.pi / 2, np.pi / 3, np.pi / 4, np.pi / 5])
x = np.cosh(arr)
print(x)
x = np.arcsinh(1.0)
print(x)
arr = np.array([0.1, 0.2, 0.5])
x = np.arctanh(arr)
print(x)
print()

# ufunc Set Operations
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)
print(x)
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.union1d(arr1, arr2)
print(newarr)
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.intersect1d(arr1, arr2, assume_unique=True)
print(newarr)
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
newarr = np.setdiff1d(set1, set2, assume_unique=True)
print(newarr)
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
newarr = np.setxor1d(set1, set2, assume_unique=True)
print(newarr)
