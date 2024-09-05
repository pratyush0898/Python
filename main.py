# Comments in Python
# This is a single line comment

"""
This
is
a
multi
line
comment
"""

# Functions
def hibox(x, y):
    return x + y

print("Hi, everyone")

# Data Types
none_value = None  # null (nothing)
number = 123  # number (any number)
text = "Hello"  # String (any text)
big_number = 654321  # BigInt (Big numbers)
boolean = True  # Boolean (can be False)
undefined_value = None  # Python does not have a direct undefined type

# Variables
a = "hello"  # best and not globally
b = "hello"  # globally, but can be used in loops
c = "hello"  # same as `a`, but also contains functions, boxes, and objects

# Operators
# Arithmetic Operators
addition = 1 + 2
subtraction = 1 - 2
multiplication = 1 * 2
division = 1 / 2
exponentiation = 1 ** 2

# Comparison Operators
equal = 1 == 2
not_equal = 1 != 2
greater_than = 1 > 2
less_than = 1 < 2
greater_than_or_equal = 1 >= 2
less_than_or_equal = 1 <= 2

# Logical Operators
logical_and = True and False
logical_or = True or False
logical_not = not True

# Function
def hello():
    print("Hello, world")

hello()

# Function can also be written like this
def plus(x, y):
    print(x + y)

plus(16, 4)

# Loops
# For loop
for i in range(1, 10):
    print(i + 1)

# Iterating through dictionary keys
marks = {
    "Pratyush": 80,
    "Rohan": 72,
    "Shiva": 49,
    "Lovish": 64
}

for student in marks:
    print(student)

# Iterating through dictionary values
for mark in marks.values():
    print(mark)

# Iterating through dictionary items
for student, mark in marks.items():
    print(f"marks of {student} is {mark}")

# For loop with string
for char in "Pratyush":
    print(char)

# String operations
my_name = "Pratyush"
print(my_name)

# Length
print(len(my_name))

# Access characters
for i in range(len(my_name)):
    print(my_name[i])

# String interpolation (using f-strings)
print(f"Hi, my name is {my_name}")

# Escape sequence
fruit = 'bana\'na'
print(fruit)

# String properties and methods
name1 = "Pratyush"
print(len(name1))  # prints 8
print(name1.upper())  # prints PRATYUSH
print(name1.lower())  # prints pratyush
print(name1[0:2])  # prints Pr
print(name1.replace("Pratyush", "Kumar"))  # prints Kumar

# Array (list in Python)
numbers = [1, 2, 3, 4]
print(numbers)

# Convert list to string
print(", ".join(map(str, numbers)))  # Replaces , to join numbers with given text

# List operations
print(numbers.pop())  # Will remove and return last item
numbers.append(56)  # Will add new element to end of list
print(numbers)
print(numbers.pop(0))  # Will remove first item from list
numbers.insert(0, 78)  # Will add new element to start of list
print(numbers)

# Concatenate lists
more_numbers = [5, 6, 7, 8]
print(numbers + more_numbers)

# Sorting
words = ['bro', 'wanna', 'zebra', 'jack', 'king']
print(sorted(words))
