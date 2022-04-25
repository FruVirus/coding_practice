"""
Overview
========

A decorator is a design pattern that we can use to add new functionality to an already
existing object without the need to modify its structure. A decorator should be called
directly before the function that is to be extended. With decorators, you can modify the
functionality of a method, a function, or a class dynamically without directly using
subclasses. This is a good idea when you want to extend the functionality of a function
that you don't want to directly modify. Decorator patterns can be implemented
everywhere, but Python provides more expressive syntax and features for that.

Python allows us to apply more than one decorator to a single function. In order to do
this correctly, make sure that you apply the decorators in the same order that you'd run
them as normal code.

Python decorators can also intercept the arguments that are passed to the decorated
functions. The arguments will in turn be passed to the decorated function at runtime.

General purpose decorators can be applied to any function. These kinds of decorators are
very helpful for debugging purposes, for example. We can define them using the *args and
**kwargs arguments. All positional and keyword arguments are stored in these two
variables, respectively. With args and kwargs, we can pass any number of arguments
during a function call.

Decorators with parameters are similar to normal decorators.
"""

# Standard Library
import functools


def lowercase(func):
    def wrapper():
        func_ret = func()
        return func_ret.lower()

    return wrapper


def split_sentence(func):
    def wrapper():
        func_ret = func()
        return func_ret.split()

    return wrapper


def hello_function():
    return "HELLO WORLD"


decorate = lowercase(hello_function)
print(decorate())
print()


@split_sentence
@lowercase
def hello_function_decorated():
    return "HELLO WORLD"


print(hello_function_decorated())
print()


def my_decorator(func):
    def my_wrapper(argument1, argument2):
        print("The arguments are: {0}, {1}".format(argument1, argument2))
        func(argument1, argument2)

    return my_wrapper


@my_decorator
def names(firstName, secondName):
    print(
        "Your first and second names are {0} and {1} respectively".format(
            firstName, secondName
        )
    )


names("Fru", "Poo")
print()


def my_decorator2(func):
    @functools.wraps(func)
    def my_wrapper(*args, **kwargs):
        print("Positional arguments:", args)
        print("Keyword arguments:", kwargs)
        func(*args, **kwargs)

    return my_wrapper


@my_decorator2
def function_without_arguments():
    print("No arguments")


function_without_arguments()
print()


@my_decorator2
def function_with_arguments(x, y, z, a=None, b=None):
    print(x, y, z, a, b)


function_with_arguments(5, 15, 25, a="Fru", b="Poo")
print(function_with_arguments.__name__)
print()


def coro(func):
    print(111, func)

    def start(*args, **kwargs):
        print(333, args, kwargs)
        cr = func(*args, **kwargs)
        next(cr)
        return cr

    print(222, start)
    return start


@coro
def bare_bones(*args, **kwargs):
    print(444, args, kwargs)
    while True:
        value = yield
        print(value)


cor = bare_bones(1, 2, 3, a=4, b=5)
print(555, cor)
cor.send("Using a decorator!")
print()


def decorator_func(func):
    print("Inside decorator")

    def inner(*args, **kwargs):  # pylint:disable=W0613
        print("Inside inner function")
        print("Decorated the function")
        print("I like ", kwargs["like"], " inside inner function")
        func(**kwargs)

    print("Returning inner function")
    return inner


@decorator_func
def func_to(**kwargs):
    print("Inside actual function")
    print("I like ", kwargs["like"], "inside func")


func_to(like="Fru and Poo")
print()


def func_to2(**kwargs):
    print("Inside actual function")
    print("I like ", kwargs["like"], "inside func")


decorator_func(func_to2)(like="Fru and Poo")
print()


def decorator(*args, **kwargs):  # pylint:disable=W0613
    print("Inside decorator")

    def inner(func):
        print("Inside inner function")
        print("Decorated the function")
        print("I like ", kwargs["like"])
        func()

    print("Returning inner function")
    return inner


@decorator(like="Fru and Poo")
def my_func():
    print("Inside actual function")


print()


def my_func2():
    print("Inside actual function")


decorator(like="Fru and Poo")(my_func2)
print()


def decorator_func2(x, y):
    def inner(func):
        def wrapper(*args, **kwargs):
            print("I like Fru and Poo")
            print("Summation of values - {}".format(x + y))
            func(*args, **kwargs)

        return wrapper

    return inner


def my_func3(*args):
    for ele in args:
        print(ele)


decorator_func2(12, 15)(my_func3)("Fru", "and", "Poo")
print()


@decorator_func2(12, 15)
def my_func4(*args):
    for ele in args:
        print(ele)


my_func4("Fru", "and", "Poo")
print()


def decodecorator(data_type, message1, message2):
    def decorator(func):
        print(message1)

        def wrapper(*args, **kwargs):
            print(message2)
            if all(isinstance(arg, data_type) for arg in args):
                return func(*args, **kwargs)
            return "Invalid Input"

        return wrapper

    return decorator


@decodecorator(str, "Decorator for 'stringjoin'", "stringjoin started ...")
def stringjoin(*args):
    return " ".join(args)


@decodecorator(int, "Decorator for 'summation'\n", "summation started ...")
def summation(*args):
    return sum(args)


print(stringjoin("I ", "like ", "Fru", "and", "Poo"))
print()
print(summation(19, 2, 8, 533, 67, 981, 119))
print()


def stringjoin2(*args):
    return " ".join(args)


def summation2(*args):
    return sum(args)


print(
    decodecorator(str, "Decorator for 'stringjoin'", "stringjoin started...")(
        stringjoin2
    )("I", "like", "Fru", "and", "Poo")
)
print()
print(
    decodecorator(int, "Decorator for 'summation'", "summation started...")(summation2)(
        19, 2, 8, 533, 67, 981, 119
    )
)
print()
