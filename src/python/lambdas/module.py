# pylint: disable=C0114, E1121, R0204

# Python Lambda #

x = lambda a: a + 10
print(x(5))
x = lambda a, b: a * b  # type: ignore
print(x(5, 6))  # type: ignore
x = lambda a, b, c: a + b + c  # type: ignore
print(x(5, 6, 2))  # type: ignore


def myfunc(n):
    print(666, n)
    return lambda a: a * n


mydoubler = myfunc(2)
print(mydoubler(11))
mytripler = myfunc(3)
print(mytripler(11))
myotherdoubler = lambda a: a * 2  # type: ignore
print(myotherdoubler(11))
print()
