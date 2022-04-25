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
    4. yield from

send() is used to send a value to a generator that just yielded. When a generator yields
a value, it suspends its execution until the next next() or send() call. A for-loop will
automatically execute subsequent next() calls for us. However, if you explicitly execute
a send() call inside a for-loop, then the send() will also restart the suspended
generator function and continue its execution (until it hits another yield statement).

throw() raises an exception at the point where the generator was paused, and returns the
next value yielded by the generator. It raises StopIteration if the generator exits
without yielding another value. The generator has to catch the passed-in exception,
otherwise the exception will be propagated to the caller.

close() allows you to stop a generator. This can be especially handy when controlling an
infinite sequence generator. The advantage of using close() is that it raises
StopIteration, an exception used to signal the end of a finite iterator.

The yield from <expr> statement can be used inside the body of a generator. <expr> has
to be an expression evaluating to an iterable, from which an iterator will be extracted.
The iterator is run to exhaustion, i.e. until it encounters a StopIteration exception.
This iterator yields and receives values to or from the caller of the generator, i.e.
the one which contains the yield from statement. The benefit of a yield from statement
can be seen as a way to split a generator into multiple generators. Furthermore, the
sub-generator is allowed to execute a return statement with a value, and that value
becomes the value of the yield from expression.
"""


# SEND
def gen():
    yield 1
    x = yield 42
    print(x)  # None, 100
    yield 2


# Create generator object and store it in variable "c".
c = gen()

# Go to yield 1 line, return the value 1, and suspend execution.
print(next(c))  # 1

# Send a value of 100 to generator but it isn't saved by the yield 1 line. send() then
# restarts the generator execution on yield 42 line. Generator returns value 42 and
# suspends execution.
print(c.send(100))  # 42

# Calling next() continues execution of generator from x = yield 42 line but since we're
# using next() instead of send(), we did not provide a value for x. Thus, x inside the
# generator function is None. Generator continues to yield 2 line, returns the value 2,
# and suspends execution.
print(next(c))  # 2
print()

# Create generator object and store it in variable "c".
c = gen()

# Go to yield 1 line, return the value 1, and suspend execution.
print(next(c))  # 1

# Go to yield 42 line, return the value 42, and suspend execution.
print(next(c))  # 42

# Send a value of 100 to generator. This time, the value is saved into the variable x
# since this was the point at which the generator previously stopped its execution.
# Generator then continues its execution by printing x and then returning the value 2
# (after which it suspends its execution again).
print(c.send(100))  # 2
print()


# gen2() will execute as expected.
def gen2():
    z = yield 1
    x = yield 42
    print(x, z)  # 666 100
    yield 2


c = gen2()
print(next(c))  # 1
print(c.send(100))  # 42
print(c.send(666))  # 2
print()

# NB: We have to send a default value of None if we use send() without calling next()
# first. next() and send(None) are equivalent.
c = gen2()
print(c.send(None))  # 1
print(c.send(100))  # 42
print(c.send(666))  # 2
print()


def count_send(firstval=0, step=1):
    counter = firstval
    while True:
        new_counter_val = yield counter
        if new_counter_val is None:
            counter += step
        else:
            counter = new_counter_val


# The next() call belows returns 2.1 as the value since that is what the generator was
# initialized with.
counter = count_send(2.1, 0.3)
print(next(counter))  # 2.1

# The send() call assigns new_counter_val inside the generator function the value of
# 100.5 AND continues to execute the generator function until the next yield statement.
# Since new_counter_val = 100.5 != None, this yields 100.5 as the next value.
print(counter.send(100.5))  # 100.5
print()

# Inside the for-loop, each call to next() will invoke the generator and increment the
# counter inside the generator since next() sends None to the generator (and thus,
# new_counter_val is also None inside the generator).
for i in range(10):
    new_value = next(counter)
    print(i, f"{new_value:2.2f}", end="\n")
print()


# THROW
def count_throw(firstval=0, step=1):
    counter = firstval
    while True:
        try:
            new_counter_val = yield counter
            if new_counter_val is None:
                counter += step
            else:
                counter = new_counter_val
        except Exception:  # pylint: disable=W0703
            yield firstval, step, counter


# The next() calls in the for-loop will increment counter by 1 each time since next()
# does not send anything to the generator.
c = count_throw()
for i in range(6):
    print(next(c))

# By throwing an Exception below, we will enter the except block inside count_throw()
# and continue to do whatever is stated there---in this case, we yield some information
# regarding the state of the generator. Note that this does not kill the generator or
# the calling process at all!
#
# NB: The error that we pass to throw() must match a catched exception inside the
# generator function---otherwise, we would just error out in the usual sense. If we
# wanted a blanket throw, then we could specify "except Exception: " inside the
# generator function, which would allow us to throw any kind of errors.
print(c.throw(IndexError))

# When we call next() again in the for-loop below, we start back with 5 (NOT 6) since
# the previous throw did not have logic to increment the variable counter inside the
# generator function. We could, of course, add additional logic inside the except block
# to increment the counter before yield the state of the generator.
for i in range(3):
    print(next(c))
print()


# CLOSE
def count_close(firstval=0, step=1):
    counter = firstval
    while True:
        try:
            new_counter_val = yield counter
            if new_counter_val is None:
                counter += step
            else:
                counter = new_counter_val
        except Exception:  # pylint: disable=W0703
            yield firstval, step, counter


c = count_close()
for i in range(6):
    print(next(c))
    # if i == 4:
    #     c.close()
print()


# YIELD FROM
def cities():
    for city in ["Berlin", "Hamburg", "Munich", "Freiburg"]:
        yield city


def squares():
    for number in range(10):
        yield number ** 2


def generator_all_in_one():
    for city in cities():
        yield city
    for number in squares():
        yield number


def generator_splitted():
    yield from cities()
    yield from squares()


lst1 = [generator_all_in_one()]
lst2 = [generator_splitted()]
print(lst1)
print(lst2)
print(lst1 == lst2)
print()
for i in lst1:
    for j in i:  # type: ignore
        print(j)
print()
for i in lst2:
    for j in i:  # type: ignore
        print(j)
print()


# subgenerator() has both a yield and a return statement. The yield 1 value gets passed
# to the RHS of the yield from statement in delegating_generator() and gets printed
# first by the for-loop. The return 42 value gets passed to the LHS of the yield from
# statement in delegating_generator() (i.e., it gets assigned to x) and gets printed
# second by delegating_generator().
def subgenerator():
    yield 1
    return 42


def delegating_generator():
    x = yield from subgenerator()
    print(x)  # 42


for x in delegating_generator():
    print(x)  # 1
print()


# RECURSIVE GENERATORS
def permutations(items):
    print("items: ", items)
    n = len(items)
    if n == 0:
        yield []
    else:
        for i in range(n):
            print(
                "Index %s, Permuting: %s with %s"
                % (i, items[i], items[:i] + items[i + 1 :])
            )

            # NB: The list concatenation send to permutations below skip the i-th
            # letter. Thus, each new permutation is around the i-th letter.
            for cc in permutations(items[:i] + items[i + 1 :]):
                print("cc: ", cc)
                print("yielding: ", [items[i]] + cc)
                yield [items[i]] + cc


for p in permutations(["r", "e", "d"]):
    print("Permutation: ", "".join(p), "\n")
# for p in permutations(list("game")):
#     print(''.join(p) + ", ", end="")
print()
print()


# GENERATOR OF GENERATORS
def firstn(generator, n):
    g = generator()
    for _ in range(n):
        yield next(g)  # pylint: disable=R1708


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


print(list(firstn(fibonacci, 10)))
print()
