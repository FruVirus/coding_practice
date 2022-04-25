# pylint: disable=C0114, E1121, R0204
# type: ignore

# Standard Library
import re

# Python RegEx #

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)
print()
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
print()
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)
print()
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())
print()
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
print()
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
print()
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
print()
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
print()
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
print()
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)
print(x.span())
print(x.string)
print(x.group())
print()
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
print(x.string)
print(x.group())
print()
