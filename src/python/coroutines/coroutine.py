"""
Overview
========

Functions are also known as a subroutines, procedures, sub-processes, etc. A function is
a sequence of instructions packed as a unit to perform a certain task. When the logic of
a complex function is divided into several self-contained steps that are themselves
functions, then these functions are called helper functions or subroutines.

Subroutines in Python are called by the main function which is responsible for
coordinating the use of these subroutines. Subroutines have a single entry point.

Coroutines are generalizations of subroutines. They are used for cooperative
multitasking where a process voluntarily yields (gives away) control periodically or
when idle in order to enable multiple applications to be run simultaneously. The
differences between coroutines and subroutines are:

1. Unlike subroutines, coroutines have many entry points for suspending and resuming
execution. Coroutine can suspend its execution and transfer control to other coroutine
and can resume again execution from the point it left off.

2. Unlike subroutines, there is no main function to call coroutines in a particular
order and coordinate the results. Coroutines are cooperative, which means they link
together to form a pipeline. One coroutine may consume input data and send it to another
that processes it. Finally, there may be a coroutine to display the result.

In Python, coroutines are similar to generators but with few extra methods and slight
changes in how we use yield statements. Generators produce data for iteration while
coroutines can also consume data.

Execution of Coroutines
-----------------------

The execution of the coroutine is similar to the generator. When we call coroutine
nothing happens, it runs only in response to the next() and send() methods. This can be
seen in the example(s) below, as only after calling the __next__() method, does our
coroutine start executing. After this call, execution advances to the first yield
expression, and now execution pauses and waits for the value to be sent to the coro
object. After a value is sent, then the coroutine continues its execution from the last
point at which it suspended itself. In other words, in a coroutine, both next() and
send() methods can continue/suspend the execution of the coroutine.

Closing a Coroutine
-------------------

Coroutine might run indefinitely. To close a coroutine, we use the close() method. When
a coroutine is closed it generates a GeneratorExit exception which can be caught in the
usual way. After closing the coroutine, if we try to send values, it will raise the
StopIteration exception.

Chaining Coroutines for Creating Pipelines
------------------------------------------

Coroutines can be used to set pipes. We can chain together coroutines and push data
through the pipe using send() method. A pipe needs:

1. An initial source (producer) that derives the whole pipeline. The producer is
usually not a coroutine, it’s just a simple method.

2. A sink, which is the endpoint of the pipe. A sink might collect all data and
display it.

Coroutines vs. Threads
----------------------

In the case of threads, it’s an operating system (or run time environment) that switches
between threads according to the scheduler. While in the case of coroutines, it’s the
programmer and programming language which decides when to switch coroutines. Coroutines
work cooperatively multitask by suspending and resuming at set points by the programmer.
"""


def print_name(prefix):
    print("Searching prefix: {}".format(prefix))
    try:
        while True:
            name = yield
            if prefix in name:
                print(name)
    except GeneratorExit:
        print("Closing coroutine!!")


corou = print_name("Dear")
corou.__next__()
corou.send("Fru")
corou.send("Dear Fru")
corou.close()
print()


def producer(sentence, next_coroutine):
    """Producer which splits strings and feeds it to pattern_filter coroutine.

    NB: This coroutine closes pattern_file() when it is done producing tokens since this
    means that there are no more patterns to be filtered.
    """

    print("Producing tokens for: {}".format(sentence))
    tokens = sentence.split(" ")
    for token in tokens:
        next_coroutine.send(token)
    print("Done with producing tokens!")
    print("Closing pattern_filter() coroutine!")
    next_coroutine.close()


def pattern_filter(pattern="ing", next_coroutine=None):
    """Search for a pattern in the received token and if the pattern is matched, then
    send it to print_token() coroutine for printing.

    NB: This coroutine is closed by producer().
    """

    print("Searching for pattern: {}".format(pattern))
    try:
        while True:
            token = yield
            if pattern in token:
                next_coroutine.send(token)
    except GeneratorExit:
        print("Done with pattern filtering!")
        print("Closing print_token() coroutine!")
        next_coroutine.close()


def print_token():
    """Act as a sink and simply print the received tokens.

    NB: This coroutine is closed by the program simply exiting().
    """

    print("I'm a sink. I'll print tokens!")
    try:
        while True:
            token = yield
            print(token)
    except GeneratorExit:
        print("Done with printing!")


sentence = "Bob is running behind a fast moving car."
pt = print_token()
pt.__next__()
pf = pattern_filter(next_coroutine=pt)
pf.__next__()
producer(sentence, pf)
