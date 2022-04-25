# pylint: disable=C0114, E1121, R0204

# Standard Library
import math

from itertools import starmap


def square(number):
    return number ** 2


numbers = [1, 2, 3, 4, 5]
squared = map(square, numbers)
print(list(squared))
str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]
int_nums = map(int, str_nums)
print(list(int_nums))
numbers = [-2, -1, 0, 1, 2]
abs_values = list(map(abs, numbers))  # type: ignore
print(abs_values)
float_values = list(map(float, numbers))
print(float_values)
words = ["Welcome", "to", "Real", "Python"]
print(list(map(len, words)))
numbers = [1, 2, 3, 4, 5]
squared = map(lambda num: num ** 2, numbers)
print(list(squared))
first_it = [1, 2, 3]
second_it = [4, 5, 6, 7]
print(list(map(pow, first_it, second_it)))
print(list(map(lambda x, y: x - y, [2, 4, 6], [1, 3, 5])))
print(list(map(lambda x, y, z: x + y + z, [2, 4], [1, 3], [7, 8])))
string_it = ["processing", "strings", "with", "map"]
print(list(map(str.capitalize, string_it)))
print(list(map(str.upper, string_it)))
print(list(map(str.lower, string_it)))
with_spaces = ["processing ", "  strings", "with   ", " map   "]
print(list(map(str.strip, with_spaces)))
with_dots = ["processing..", "...strings", "with....", "..map.."]
print(list(map(lambda s: s.strip("."), with_dots)))


def rotate_chr(c):
    rot_by = 3
    c = c.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if c not in alphabet:
        return c
    rotated_pos = ord(c) + rot_by
    if rotated_pos <= ord(alphabet[-1]):
        return chr(rotated_pos)
    return chr(rotated_pos - len(alphabet))


print("".join(map(rotate_chr, "My secret message goes here.")))
numbers = [1, 2, 3, 4]
print(list(map(lambda x: (x ** 2, x ** 3), numbers)))
numbers = [1, 2, 3, 4, 5, 6, 7]
print(list(map(math.factorial, numbers)))


def to_fahrenheit(c):
    return 9 / 5 * c + 32


def to_celsius(f):
    return (f - 32) * 5 / 9


celsius_temps = [100, 40, 80]
print(list(map(to_fahrenheit, celsius_temps)))
fahr_temps = [212, 104, 176]
print(list(map(to_celsius, fahr_temps)))
print(list(map(float, ["12.3", "3.3", "-15.2"])))
print(list(map(int, ["12", "3", "-15"])))


def to_float(number):
    try:
        return float(number.replace(",", "."))
    except ValueError:
        return float("NaN")


print(list(map(to_float, ["12.3", "3,3", "-15.2", "One"])))


def is_positive(num):
    return num >= 0


def sanitized_sqrt(numbers):
    cleaned_iter = map(math.sqrt, filter(is_positive, numbers))
    return list(cleaned_iter)


print(sanitized_sqrt([25, 9, 81, -16, 0]))
print(list(map(pow, (2, 7), (4, 3))))
print(list(starmap(pow, [(2, 7), (4, 3)])))
print(list(map(pow, (2, 4), (7, 3))))
