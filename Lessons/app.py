'''
import math
x = 1
y = 2
unit_price = 3
print("Hello World")

students_count = 1000
rating = 4.99
is_published = True

'''

'''
# strings in python:
course_name = "Python Programming"
print(len(course_name))
print(course_name[0])
print(course_name[-1])
print(course_name[0:3])
print(course_name[0:])
print(course_name[:3])
print(course_name[:])

'''

# course = "python programming"
# print(course.upper())  # UPPER CASE
# print(course.lower())  # lower case
# print(course.title())  # Title
# print(course.strip())  # removes white spaces
# print(course.lstrip())  # removes white spaces from the left
# print(course.rstrip())  # removes white spaces from the right
# print(course.find("Pro"))
# print(course.replace("p", "j"))
# print("pro" in course)
# print("swift" not in course)

# Standard Arithmetic Operators:
# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)
# print(10 // 3)
# print(10 % 3)
# print(10 ** 3)

# Rounding Numbers

# print(round(2.9))
# print(abs(-2.9))


# maths module

# print(math.ceil(2.2))

# x = input("x: ")
# y = int(x) + 1
# print(f"x: {x}, y: {y}")

# int(x)
# float(x)
# bool(x)
# str(x)

# Falsy values
# ""
# 0
# None

# print(bool("False"))

# comparison operators:
# 10 > 3
# 10 >= 3
# 10 < 20
# 10 <= 20
# 10 == 10
# 10 == "10"
# 10 != "10"
# "bag" > "apple"
# "bag" == "bag"

# temperature = 25
# if temperature > 30:
#     print("It's warm")
#     print("Drink water")
# elif temperature > 20:
#     print("It's nice")
# else:
#     print("It's cold")
# print("Done")


# Ternary operator:
# age = 17
# if age >= 18:
#     print("Eligible")
# else:
#     print("Not eligible")

########
# age = 22
# message = "Eligible" if age >= 18 else "Not eligible"
# print(message)

###########
# Logical Operators:
# and
# or
# not

# examples:
# high_income = False
# good_credit = True
# student = False

# if (high_income or good_credit) and not student:
#     print("Eligible")
# else:
#     print("Not eligible")

###########
# This is called chaining comparison operators
# age should be between 18 and 65
# age = 22
# if 18 <= age < 65:  # This expression is the sme as this "age >= 18 and age < 65".
#     print("Eligible")

# We use loop to create repetition
# for number in range(3):
#     print("Attempt", number + 1, (number + 1) * ".")

# OR
# for number in range(1, 4):
#     print("Attempt", number, number * ".")

# for number in range(1, 10, 2):
#     print("Attempt", number, number * ".")


# successful = True
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break


# successful = False
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 times and failed")

# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")
# print(type(5))
# print(type(range(5)))

# # Iterable
# for x in "Python":
#     print(x)

# number = 100
# while number > 0:
#     print(number)
#     number //= 2


# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)


# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break

# count = 0
# for x in range(1, 10):
#     if x % 2 == 0:
#         count += 1
#         print(x)
# print(f"We have {count} even numbers")


'''
# FUNCTIONS:
# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome aboard")


# greet("Iheanyi", "Okwara")

'''

'''
def greet(name):
    print(f"Hi {name}")


greet("Iheanyi")

'''


# Types of functions:
'''
# In programming we have two types of functions
# 1 - function that performs a task
# 2 = function that returns a value

# def get_greeting(name):
#     return f"Hi {name}"


# message = get_greeting("Iheanyi")
# file = open("content.txt", "w")
# file.write(message)

'''


# Keyword arguements:

'''
def increment(number, by):
    return number + by


result = increment(2, 1)
print(result)

# OR


def increment(number, by):
    return number + by


print(increment(2, by=1))

'''


# Default arguement:
'''
def increment(number, by=1):
    return number + by


print(increment(2))


# OR


def increment(number, by=1):
    return number + by


print(increment(2, 5))

'''

# xargs
'''

def multiply(*numbers):
    for number in numbers:
        print(number)


multiply(2, 3, 4, 5)

'''
# We use squared brackets[] to create list and parenthesis() to create tuples
# The difference is that we cannot modify tuples (add or remove)

'''
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
'''

# xxargs

'''
def save_user(**user):
    print(user)


save_user(id=1, name="John", age=22)


# Example 2:

def save_user(**user):
    print(user["name"])


save_user(id=1, name="John", age=22)
'''

# EXERCISE:

'''
def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(15))
'''
'''
# List:
numbers = list(range(20))
# print(numbers[::2])
print(numbers[::-1])

# Unpacking Lists:
# Ex1
numbers = [1, 2, 3, 4, 4, 4, 4, 4]
first, second, *other = numbers
print(first)
print(other)

# Ex2
numbers = [1, 2, 3, 4, 4, 4, 4, 9]
first, *other, last = numbers
print(first, last)
print(other)
'''

# Looping over Lists:
# Ex1
'''
letters = ["a", "b", "c"]
for letter in letters:
    print(letter)

# Ex2
letters = ["a", "b", "c"]
for letter in enumerate(letters):
    print(letter)
# With enumerate it return a tuple (read-only)

# To get the indexes of the tuple
letters = ["a", "b", "c"]
for letter in enumerate(letters):
    print(letter[0], letter[1])

# If we unpack the above express, we have:
letters = ["a", 'b', "c"]
items = (0, "a")
index, letter = items
for index, letter in enumerate(letters):
    print(index, letter)
'''

# How to add items to a list or remove existing items
'''
letters = ["a", "b", "c"]

# Add (to add at the end use append)
letters.append("d")
# To add at a specific location use insert
letters.insert(0, "-")
# print(letters)

# Remove (to remove at the end of the list use pop method)
letters.pop()
letters.pop(0)  # If you know the index, you can insert it
letters.remove("b")  # if you don't know the index
# Another way to remove an item from a list is to use the del statement
del letters[0:3]
# The difference between the pop method and the del method; with the pop method,
# you can delete only one item, but with the del method, you can delete a range
# of items

# If you want to remove all the objects in a list, use the clear method
letters.clear()
print(letters)
'''

# Finding Items in a list
'''
letters = ["a", "b", "c"]
print(letters.index("a"))  # To find the index of a letter

# You can also use the following to check if a letter is in an item
letters = ["a", "b", "c"]
if "d" in letters:
    print(letters.index("d"))
    
# To return the number of occurences of a given item use: count
letters = ["a", "b", "c"]
print(letters.count("d"))
if "d" in letters:
    print(letters.index("d"))

'''

# Sorting Lists:
'''
numbers = [3, 51, 2, 8, 6]
numbers.sort()  # sort in ascending order
print(numbers)


numbers = [3, 51, 2, 8, 6]
numbers.sort(reverse=True)  # sort in descending order
print(numbers)


numbers = [3, 51, 2, 8, 6]
# This returns a new sorted list, it will not modify the old list
print(sorted(numbers))
print(numbers)


# To change the sort order
numbers = [3, 51, 2, 8, 6]
# This returns a new sorted list, it will not modify the old list
print(sorted(numbers, reverse=True))
print(numbers)
'''


# Sorting a List of tuples with two items:
# Ex1
'''
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]


def sort_item(item):
    return item[1]  # Sort based on price of the item


items.sort(key=sort_item)
print(items)

'''
# Lambda Functions:
'''
# Is a simple one-line anonymous function we can pass to other expressions

# Ex2
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

# items.sort(key=lambda parameters:expression)
items.sort(key=lambda item: item[1])
print(items)  # This returns the same result as the previous Ex1 above
'''

# Map Function:
'''
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

prices = []
for item in items:
    prices.append(item[1])

print(prices)

# OR

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

# x = map(lambda item: item[1], items)
# for item in x:
#     print(item)

# OR

prices = list(map(lambda item: item[1], items))
print(prices)
'''
# Filter Function:
'''
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
'''
# List Comprehensions:
'''
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]
# prices = list(map(lambda item: item[1], items)) # same result with the next line
prices = [item[1] for item in items]  # [expression for item in items]

# filtered = list(filter(lambda item: item[1] >= 10, items)) # same result as the next line
filtered = [item for item in items if item[1] >= 10]
print(filtered)
'''
# Zip Function: used to combine multiple lists
'''
list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip(list1, list2)))

# Ex2
list1 = [10, 20, 30]
list2 = [50, 60, 70]

print(list(zip("abc", list1, list2)))
'''
# Stacks:
# LIFO (Last In - First Out)
'''
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
print("redirect", browsing_session[-1])
if not browsing_session:
    print("disable")
'''
# FIFO (First In - First Out)
'''
from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("empty")
'''

# Tuples:
# A tuple is a read-only list. It contains a sequence of objects
# but you cannot modify the object, you cannot add object or remove
# an existing object.
'''
point = (1, 2, 3)
print(type(point))

point = ()  # empty string
print(type(point))

# We can concatinate two tuples
point = (1, 2) + (3, 4)  # point = (1, 2) * 3
print(type(point))
print(point)

# We can convert a list to a tuple
point = tuple([1, 2])
print(point)

# We can pass string to the tuple
point = tuple("Hello World")
print(point)

# We can access individual items using the index
point = (1, 2, 3)
print(point[0])
print(point[0:2])
x, y, z = point
if 10 in point:
    print("exists")
'''

# Swapping Variables:
'''
x = 10
y = 11

z = x
x = y
y = z

print("x", x)
print("y", y)
'''

# In python we can swap a variable using only one line of code
# without a third variable

# Example:
'''
x = 10
y = 11

x, y = y, x
print("x", x)
print("y", y)
'''
# Arrays:
# Use arrays only if you are dealing with a large sequence of numbers
# and you encountered performance problems, for other cases, use list
# and tuples by default.
# To use an array, you need to import it from the array module
'''
from array import array
numbers = array("i", [1, 2, 3])
numbers.append(4)  # To add a number at the end
numbers.insert(2)  # To add a number at a specific index
numbers.pop(2)
numbers.remove(4)
numbers[0]

'''

# Set:
# A set is a number in a list not duplicated

'''
numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
second = {1, 4}
# second.add(5)
# second.remove(5)
# len(second)
print(uniques)

'''

'''
numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}

print(first | second)  # prints a combination numbers in the two sets
print(first & second)  # prints all the numbers in a given set
print(first - second)  # prints the difference of the two sets
# prints numbers in either in first or second set but not both
print(first ^ second)


# Set is an unordered unique items, you cannot have a duplicate, they are not
# in sequence and you cannot access them using an index. Rather, you can say:

if 1 in first:
    print("yes")
'''

# Dictionaries:
# is a collection of key value pairs used to mark a key to a value.

'''
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
print(point["x"])

# We can change the value of x = 10
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
print(point)

# We can set a new value to get 3 key value pairs:
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20
print(point)

# If an item does not exist in the set, we get an error, or none, or 0
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20
if "a" in point:
    print(point["a"])
print(point.get("a", 0))

# We can also delete a point:
del point["x"]
print(point)

# How to look over a dictionary
for key in point:
    print(key, point[key])

# Another way to iterate over a dictionary
for key, value in point.items():
    print(key, value)

'''
# Dictionary Comprehensions:
'''
values = []
for x in range(5):
    values.append(x * 2)
'''
# Generator Expression:
# Here we're creating a list using a list generator expression

'''
values = [x * 2 for x in range(10)]
for x in values:
    print(x)

'''
# This is perfectly fine, but there are times you may be working with a large dataset
# or an infinite set of data, in those situations you have stored those values in a memory.
# However, it takes a lot of memory. Gnerator objects are iterable just like lists.
# Unlike list Generator objects generate a new value in each iteration, they don't store all the values in memory


# How to get size of an object:
'''

from sys import getsizeof
values = (x * 2 for x in range(1000)) 
print("gen:", getsizeof(values))


# Even when you change the range of numbers to say 100000, the generator object remains consistent.
# In contrast, if we use a list comprehension expression here, we will end up with a list of 100000 items.
# For example:


values = [x * 2 for x in range(100000)]
print("list:", getsizeof(values))
'''

# Unpacking Operator:
'''
numbers = [1, 2, 3]
print(numbers)
print(1, 2, 3)
print(*numbers)
'''
# This is the unpacking operator. The application of this is when creating list

# We can unpack any iterables, it doesn't have to be a list only
# For example:
'''
values = list(range(5))
values = [*range(5), *"Hello"]
print(values)
'''
# We can also unpack a string, like *"Hello"

# Furthermore, using this operator, we can combine multiple lists
'''
first = [1, 2]
second = [3]
values = [*first, "a", *second, *"Hello"]
print(values)
'''

# We can also unpack dictionaries but we need to use two asteriks **
'''
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)
'''
# Note that in the result, the value of x is 10 and not 1, this is because
# If you have multiple items with the same key the last value will be used.
# To recap: We can use the unpacking operator to take out individual values in any iterable

# EXERCISES:
# Write a program to find the most repeated character in this text:
# sentence = "This is a common interview question"

# Define the sentence
'''
sentence = "This is a common interview question"
# Remove spaces to only consider characters
sentence = sentence.replace("", "")
# create a dictionary to count occurrences of each character
char_count = {}
for char in sentence:
    char = char.lower()  # make it case-insensitive
    char_count[char] = char_count.get(char, 0) + 1

# Find the character with the highest frequency
most_repeated = max(char_count, key=char_count.get)
print(
    f"The most repeated character is '{most_repeated}' with {char_count[most_repeated]} occurrences.")
'''

# ANOTHER APPROACH TO ANSWER THE QUESTION:
'''
from pprint import pprint
sentence = "This is a common interview question"
# Define an empty dictionry
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
char_frequency_sorted = sorted(
    char_frequency.items(), key=lambda kv: kv[1], reverse=True)
print(char_frequency_sorted[0])
'''

# Handling Exceptions:
'''
try:
    age = int(input("Age: "))
except ValueError:
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
print("Execution continues.")
'''


# Handliing Different Exceptions
'''
try:
    age = int(input("Age: "))
    xfactor = 10 / age
except ValueError:
    print("You didn't enter a valid age.")
except ZeroDivisionError:
    print("Age cannot be zero")
else:
    print("No exceptions were thrown.")
    
'''


# For multiple types of exceptions separated by a comma:
'''
try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
'''

# Cleaning up:
# Note: When python executes the code that we have in the try block,
# if any of the statements throws an exception that matches one of the except clauses,
# that except clause is executed and the other except clauses are ignored.

'''
try:
    file = open("app.py")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
finally:
    file.close()

'''

# The finally clause is use to release external resources. It is always executed whether we have
# an except clause or not. This is the perfect place to close files, database connections and
# network connections.

# The With Statement:
# The with statement is used to automatically release external resources
# For example:
'''
try:
    with open("app.py") as file:
        print("File opened.")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")

'''

# We have magic methods - these are methods that start with two underlines __
'''
try:
    with open("app.py") as file:
        print("File opened.")
        file.__exit
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")

'''

# Content Management Protocol - refers to when an object supports these two methods (enter and exit)
# and we can use that object with the With Statement; python will automatically call the exit method
# and there it will release the external resources, amd that is the reason we don't need a finally clause here.


# However, there are times you might be working with multiple external resources, let's say you want to
# read some data from one file and write it to another file:

'''
try:
    with open("app.py") as file, open("another.txt") as target:
        print("File opened.")
        
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")

'''
# Raising Exceptions:

'''

def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
'''

# Cost of Raising Exceptions
# Using the timeit function we can calculate the execution time of some python code
'''
from timeit import timeit
code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""
print("first code=", timeit(code1, number=10000))

'''


# Trying different approach:
'''

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age


xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""
print("first code=", timeit(code1, number=10000))
print("second code=", timeit(code2, number=10000))

'''
# Classes in python:
# A clas is the blueprint for creating new objects
# example:
'''
x = 1
print(type(x))
'''

# An object is an instance of a class
# Example
# Class: Human (defines all the attributes of a human)
# Objects: John, Mary, Jack

# Creating Classes:

'''
class Point:
    def draw(self):
        print("draw")


point = Point()
print(type(point))
print(isinstance(point, Point))
print(isinstance(point, int))
'''

# Constructors:

'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print("draw")


point = Point(1, 2)
print(point.x)
'''

'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
point.draw()
'''

# Class Vs Instance Attributes

'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
point.draw()

another = Point(3, 4)
another.draw()

'''

# Class level attributes are shared across all instances of a class.
# if you change its value, the change is visible across all objects of that type
# For example:

'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


Point.default_color = "Red"  # same applies to "yellow" or any other color of choice

point = Point(1, 2)
print(point.default_color)
print(Point.default_color)
point.draw()

another = Point(3, 4)
print(another.default_color)
another.draw()

'''

# Class Vs Instance Methods:

'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        cls(0, 0)
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point.zero()
point.draw()

'''

# Magic Methods:

# These are methods that have two underscores at the beginning nd end of their names
# They are called automatically by python interpreter depending on the way we use our objects and classes
# Search for "Python 3 magic methods" on the internet, to see a complete list of them.

'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(point)

'''
# Comparing Objects:


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point(10, 20)
other = Point(1, 2)
print(point < other)
