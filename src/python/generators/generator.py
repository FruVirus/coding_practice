"""
Overview
========

Generator functions are a special kind of function that return a lazy iterator. These
are objects that you can loop over like a list. However, unlike lists, lazy iterators do
not store their contents in memory. Generators are created by using generator functions
or generator expressions. Generator expressions are like list comprehensions with the
added benefit that you can create them without building and holding the entire object in
memory before iteration. Generator expressions use parentheses instead of brackets.

List comprehensions return full lists, while generator expressions return generators.
Generators work the same whether they’re built from a function or an expression. Using
an expression just allows you to define simple generators in a single line, with an
assumed yield at the end of each inner iteration. If speed is an issue but memory is
NOT, then LIST comprehensions are better.

When you call a generator function or use a generator expression, you return a special
iterator called a generator. You can assign this generator to a variable in order to use
it. When you call special methods on the generator, such as next(), the code within the
function is executed up to yield.

When the Python yield statement is hit, the program suspends function execution and
returns the yielded value to the caller. In contrast, return stops function execution
completely. When a function is suspended, the state of that function is saved. This
includes any variable bindings local to the generator, the instruction pointer, the
internal stack, and any exception handling. yield is technically an expression, rather
than a statement; i.e., you can assign variables to the result of a yield.

Generators, like all iterators, can be exhausted. Unless your generator is infinite, you
can iterate through it one time only. Once all values have been evaluated, iteration
will stop and the for-loop will exit. If you used next(), then instead you’ll get an
explicit StopIteration exception.

In addition to yield, generator objects can make use of the following methods:
    1, send()
    2. throw()
    3. close()

send() is used to send a value to a generator that just yielded. When a generator yields
a value, it suspends its execution until the next next() or send() call. A for-loop will
automatically execute subsequent next() calls for us. However, if you explicitly execute
a send() call inside a for-loop, then the send() will also restart the suspended
generator function and continue its execution (until it hits another yield statement).
"""


def gen():
    yield 1
    x = yield 42
    print(x)
    yield 2


# Create generator object and store it in variable "c".
c = gen()

# Go to yield 1 line, return the value 1, and suspend execution.
print(next(c))

# Send a value of 100 to generator but it isn't saved by the yield 1 line. send() then
# restarts the generator execution on yield 42 line. Generator returns value 42 and
# suspends execution.
print(c.send(100))

# Calling next() continues execution of generator from x = yield 42 line but since we're
# using next() instead of send(), we did not provide a value for x. Thus, x inside the
# generator function is None. Generator continues to yield 2 line, returns the value 2,
# and suspends execution.
print(next(c))
print()

# Create generator object and store it in variable "c".
c = gen()

# Go to yield 1 line, return the value 1, and suspend execution.
print(next(c))

# Go to yield 42 line, return the value 42, and suspend execution.
print(next(c))

# Send a value of 100 to generator. This time, the value is saved into the variable x
# since this was the point at which the generator previously stopped its execution.
# Generator then continues its execution by printing x and then returning the value 42
# (after which it suspends its execution again).
print(c.send(100))
print()


# gen2() will execute as expected.
def gen2():
    z = yield 1
    x = yield 42
    print(x, z)
    yield 2


c = gen2()
print(next(c))
print(c.send(100))
print(c.send(666))
print()


# NB: We have to send a default value of None if we use send() without calling next()
# first. next() and send(None) are equivalent.
c = gen2()
print(c.send(None))
print(c.send(100))
print(c.send(666))
