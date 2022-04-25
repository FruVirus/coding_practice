# pylint: disable=C0114, E1121, R0204
def square(number):
    return number ** 2


numbers = [1, 2, 3, 4, 5]
squared = map(square, numbers)
print(list(squared))
str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]
int_nums = map(int, str_nums)
print(list(int_nums))
numbers = [-2, -1, 0, 1, 2]
abs_values = list(map(abs, numbers))
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
