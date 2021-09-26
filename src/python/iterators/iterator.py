"""
Overview
========

An iterator is an object that contains a countable number of values. An iterator is an
object that can be iterated upon, meaning that you can traverse through all the values.
In Python, an iterator is an object that implements the iterator protocol, which
consists of the method __iter__() and __next__().

Iterables are objects that can be iterated over such as lists, tuples, dictionaries,
sets, strings, etc. They are iterable containers from which you can get an iterator from
by using iter(obj).

1. __iter__ method/iter() is called for the initialization of an iterator. This method
must always return the iterator object itself.

2. __next__ method/next() returns the next value for the iterable. When we use a
for-loop to traverse any iterable object, Python uses the iter() method to get an
iterator object, which further uses the next() method to iterate over. This method
raises a StopIteration to signal the end of the iteration and must return the next item
in the sequence.
"""


iterable = "FruPoo"
iterator = iter(iterable)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break


class MyIterator:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.x = 10
        return self

    def __next__(self):
        x = self.x
        if x > self.limit:
            raise StopIteration
        self.x += 1
        return x


for i in MyIterator(15):
    print(i)
