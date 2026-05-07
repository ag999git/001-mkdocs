



# Script Writing Questions and Answers – Python Basics II



**1. Write a Python script to demonstrate that integers are immutable objects. Your script should display the value and memory ID of an integer before and after modification.**

```python
# Demonstrates immutability of integers in Python

# Create an integer object
x = 10

# Print value and memory ID before modification
print("Before modification:")
print("Value of x:", x)
print("ID of x:", id(x))

# Modify the integer
# Since integers are immutable, Python creates a NEW object
x = x + 5

# Print value and memory ID after modification
print("\nAfter modification:")
print("Value of x:", x)
print("ID of x:", id(x))

# The ID changes because integers cannot be modified in-place

```

----------

**2. Write a Python script that demonstrates implicit type conversion during mixed arithmetic between an integer and a float.**

```python
# Demonstrates implicit type conversion in Python

# Integer variable
num1 = 5

# Float variable
num2 = 2.5

# Python automatically converts integer to float
result = num1 + num2

# Print result and type
print("Result:", result)
print("Type of result:", type(result))

# Since float is a wider type than int,
# Python converts 5 to 5.0 automatically

```

----------

**3. Write a Python script to show floating-point precision problems using 0.1 and 0.2. Also compare the values safely using the math module.**

```python
# Import math module
import math

# Floating-point addition
result = 0.1 + 0.2

# Print actual result
print("0.1 + 0.2 =", result)

# Direct comparison may fail
print("Direct comparison:", result == 0.3)

# Safe comparison using math.isclose()
print("Using math.isclose():", math.isclose(result, 0.3))

# Floating-point numbers are stored in binary internally,
# therefore some decimal numbers cannot be represented exactly

```

----------

**4. Write a Python script to create complex numbers using different methods and display their real part, imaginary part, conjugate, and magnitude.**

```python
# Method 1: Direct creation
z1 = 3 + 4j

# Method 2: Using complex() function
z2 = complex(5, 6)

# Method 3: Imaginary-only number
z3 = 7j

# Display details of z1
print("Complex number:", z1)
print("Real part:", z1.real)
print("Imaginary part:", z1.imag)
print("Conjugate:", z1.conjugate())
print("Magnitude:", abs(z1))

# Display additional complex numbers
print("\nSecond complex number:", z2)
print("Third complex number:", z3)

# abs() calculates the magnitude using:
# sqrt(real^2 + imaginary^2)

```

----------

**5. Write a Python script that demonstrates valid and invalid Boolean values and naming conventions for Boolean variables.**

```python
# Boolean values in Python
is_logged_in = True
has_permission = False
can_upload = True

# Print Boolean values
print(is_logged_in)
print(has_permission)
print(can_upload)

# Print types
print(type(is_logged_in))

# Python Boolean values must start with capital letters
# true and false are invalid unless separately defined

# Boolean naming convention usually uses prefixes like:
# is_, has_, can_, should_

```

----------

**6. Write a Python script to demonstrate indexing, slicing, concatenation, and repetition operations on strings.**

```python
# Create a string
message = "Python Basics"

# Indexing
print("First character:", message[0])
print("Last character:", message[-1])

# Slicing
print("Slice [0:6]:", message[0:6])

# Concatenation
new_message = message + " Part 2"
print("Concatenated string:", new_message)

# Repetition
print("Repeated string:")
print(message * 3)

# Strings are sequences,
# therefore indexing and slicing are supported

```

----------

**7. Write a Python script to demonstrate that strings are immutable objects.**

```python
# Create a string
text = "hello"

# Print original ID
print("Original string:", text)
print("Original ID:", id(text))

# Modify string
# Python creates a NEW string object
text = text + " world"

# Print modified string and ID
print("\nModified string:", text)
print("Modified ID:", id(text))

# Different IDs show that strings are immutable

```

----------

**8. Write a Python script that creates a list of mixed data types and performs indexing, slicing, appending, removing, and membership testing.**

```python
# Create a mixed list
my_list = [10, "apple", 3.5, True]

# Print list
print("Original list:", my_list)

# Indexing
print("First item:", my_list[0])

# Slicing
print("Slice [1:3]:", my_list[1:3])

# Append new item
my_list.append("Python")
print("After append:", my_list)

# Remove an item
my_list.remove(True)
print("After remove:", my_list)

# Membership test
print("Is 'apple' present?", "apple" in my_list)

# Lists are mutable and can store mixed data types

```

----------

**9. Write a Python script that demonstrates mutability of lists using the id() function.**

```python
# Create a list
numbers = [1, 2, 3]

# Print original ID
print("Before append:")
print(numbers)
print("ID:", id(numbers))

# Modify list in-place
numbers.append(4)

# Print modified list and ID
print("\nAfter append:")
print(numbers)
print("ID:", id(numbers))

# ID remains same because list is mutable

```

----------

**10. Write a Python script to demonstrate tuple creation, indexing, slicing, and tuple unpacking.**

```python
# Create a tuple
student = ("Alice", 21, "Physics")

# Indexing
print("Name:", student[0])

# Slicing
print("Slice [1:3]:", student[1:3])

# Tuple unpacking
name, age, subject = student

# Print unpacked values
print("\nUnpacked values:")
print(name)
print(age)
print(subject)

# Tuples are immutable sequences

```

----------

**11. Write a Python script that demonstrates the difference between a single-item tuple and a normal string inside parentheses.**

```python
# Single-item tuple
single_tuple = ("apple",)

# String inside parentheses
not_tuple = ("apple")

# Print values and types
print(single_tuple)
print(type(single_tuple))

print(not_tuple)
print(type(not_tuple))

# The comma is what actually creates the tuple

```

----------

**12. Write a Python script to create a dictionary of student details and perform adding, updating, deleting, and safe retrieval operations.**

```python
# Create dictionary
student = {
    "name": "Alice",
    "age": 20,
    "course": "Maths"
}

# Print original dictionary
print("Original dictionary:")
print(student)

# Add new key-value pair
student["year"] = 2026

# Update existing value
student["name"] = "Bob"

# Delete a key-value pair
del student["course"]

# Safe retrieval using get()
print("\nCourse:", student.get("course"))

# Final dictionary
print("\nUpdated dictionary:")
print(student)

# Dictionaries are mutable containers

```

----------

**13. Write a Python script that demonstrates dictionary methods such as keys(), values(), and items().**

```python
# Create dictionary
employee = {
    "id": 101,
    "name": "John",
    "department": "HR"
}

# Display keys
print("Keys:")
print(employee.keys())

# Display values
print("\nValues:")
print(employee.values())

# Display items
print("\nItems:")
print(employee.items())

# items() returns key-value pairs as tuples

```

----------

**14. Write a Python script to create sets from a string and a list. Show that duplicate values are automatically removed.**

```python
# Create set from string
char_set = set("programming")

# Create set from list
number_set = set([1, 2, 2, 3, 4, 4, 5])

# Print sets
print("Character set:")
print(char_set)

print("\nNumber set:")
print(number_set)

# Sets automatically remove duplicate values

```

----------

**15. Write a Python script that demonstrates union, intersection, and difference operations on sets.**

```python
# Create two sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union
print("Union:")
print(A.union(B))

# Intersection
print("\nIntersection:")
print(A.intersection(B))

# Difference
print("\nDifference A-B:")
print(A.difference(B))

# Sets are useful for mathematical operations

```

----------

**16. Write a Python script that demonstrates why lists cannot be added to a set. Use comments to explain the error.**

```python
# Lists are mutable objects
my_list = [1, 2, 3]

# The following line would produce a TypeError
# because lists are mutable and therefore unhashable

# invalid_set = {my_list}

print("Lists cannot be added to sets because they are mutable.")
print("Set elements must be immutable and hashable.")

```

----------

**17. Write a Python script to demonstrate the use of None as a placeholder value.**

```python
# Placeholder variable
temperature = None

# Print initial value
print("Initial temperature:", temperature)

# Check whether value is assigned
if temperature is None:
    print("Temperature value has not been assigned yet.")

# Later assign a value
temperature = 28

# Print updated value
print("Updated temperature:", temperature)

# None represents absence of meaningful value

```

----------

**18. Write a Python script to demonstrate that functions without a return statement automatically return None.**

```python
# Define a function without return statement
def greet():
    print("Hello student")

# Call function and store result
result = greet()

# Print returned value
print("Returned value:", result)

# Python automatically returns None
# when a function does not explicitly return a value

```

----------

**19. Write a Python script that compares None with False, 0, and an empty string.**

```python
# Compare None with False
print(None == False)

# Compare None with zero
print(None == 0)

# Compare None with empty string
print(None == "")

# None is different from all these values
# It represents absence of value

```

----------

**20. Write a Python script that demonstrates explicit type conversion using int(), float(), and str().**

```python
# String to integer conversion
x = "12"
print(int(x) + 5)

# Integer to float conversion
num = 10
print(float(num))

# Integer to string conversion
age = 25
print("Age is " + str(age))

# Explicit casting is done manually by programmer

```

----------

**21. Write a Python script that demonstrates narrowing and widening type conversions.**

```python
# Widening conversion
# Integer converted to float
x = 10
wide_value = float(x)

print("Widening conversion:")
print(wide_value)

# Narrowing conversion
# Float converted to integer
pi_value = 3.14159
narrow_value = int(pi_value)

print("\nNarrowing conversion:")
print(narrow_value)

# Narrowing may lose information
# because decimal part is removed

```

----------

**22. Write a Python script that demonstrates conversion of numbers into hexadecimal and octal representations.**

```python
# Integer value
number = 64

# Convert to hexadecimal
print("Hexadecimal:", hex(number))

# Convert to octal
print("Octal:", oct(number))

# hex() and oct() return strings
# representing the number in different bases

```

----------

**23. Write a Python script that accepts age input from the user and converts it into an integer before using it in arithmetic.**

```python
# Take input from user
age = input("Enter your age: ")

# Convert string input into integer
age = int(age)

# Perform arithmetic
print("Next year your age will be:", age + 1)

# input() always returns a string,
# therefore conversion is necessary

```

----------

**24. Write a Python script that demonstrates truthy and falsy values in Python using bool().**

```python
# Numbers
print(bool(0))
print(bool(10))

# Strings
print(bool(""))
print(bool("Python"))

# Lists
print(bool([]))
print(bool([1, 2]))

# Dictionaries
print(bool({}))
print(bool({"a": 1}))

# None
print(bool(None))

# Empty containers are falsy
# Non-empty containers are truthy

```

----------

**25. Write a Python script that checks whether a list is empty using the Pythonic approach.**

```python
# Create a list
items = [10, 20, 30]

# Pythonic way to check emptiness
if items:
    print("List contains items")
else:
    print("List is empty")

# Empty lists evaluate to False
# Non-empty lists evaluate to True

```

----------

**26. Write a Python script to demonstrate good and bad practices for Boolean comparisons.**

```python
# Boolean variable
is_active = True

# Non-Pythonic approach
if is_active == True:
    print("Using explicit comparison")

# Better Pythonic approach
if is_active:
    print("Using direct truth-value testing")

# Pythonic code is shorter and more readable

```

----------

**27. Write a Python script that imports the math module and uses its attributes and methods.**

```python
# Import math module
import math

# Access module attribute
print("Value of pi:", math.pi)

# Access module method
print("Square root of 49:", math.sqrt(49))

# Dot operator is used to access
# module attributes and methods

```

----------

**28. Write a Python script that imports only sqrt and pi from the math module and uses them directly.**

```python
# Import specific items from math module
from math import sqrt, pi

# Use imported items directly
print("Square root:", sqrt(64))
print("Pi value:", pi)

# No module prefix is required
# because specific items were imported

```

----------

**29. Write a Python script that demonstrates module aliasing using the math module.**

```python
# Import math module with alias
import math as m

# Use alias instead of original name
print("Value of pi:", m.pi)
print("Square root of 81:", m.sqrt(81))

# Aliasing shortens long module names

```

----------

**30. Write a Python script that uses dir() to display all attributes and methods of a module.**

```python
# Import os module
import os

# Display all attributes and methods
print(dir(os))

# dir() returns names available inside module

```

----------

**31. Write a Python script that demonstrates conversion of a list into a tuple and a tuple into a list.**

```python
# Original list
numbers_list = [1, 2, 3]

# Convert list to tuple
numbers_tuple = tuple(numbers_list)

print(numbers_tuple)
print(type(numbers_tuple))

# Convert tuple back to list
new_list = list(numbers_tuple)

print(new_list)
print(type(new_list))

# Conversion functions are useful
# when changing container types

```

----------

**32. Write a Python script that demonstrates conversion of a dictionary into a set.**

```python
# Create dictionary
student = {
    "name": "Alice",
    "age": 20,
    "course": "Physics"
}

# Convert dictionary into set
# Only keys are included
student_set = set(student)

# Print result
print(student_set)

# set(dictionary) converts only keys

```

----------

**33. Write a Python script that demonstrates membership testing using the in operator on strings, lists, dictionaries, and sets.**

```python
# String membership
print("Py" in "Python")

# List membership
print(10 in [5, 10, 15])

# Dictionary membership checks keys
student = {"name": "Alice", "age": 20}
print("name" in student)

# Set membership
print(3 in {1, 2, 3, 4})

# 'in' operator checks existence of element

```

----------

**34. Write a Python script that creates a list of None values using list multiplication.**

```python
# Create list containing None values
placeholder_list = [None] * 5

# Print list
print(placeholder_list)

# Useful when reserving positions
# for future data insertion

```

----------

**35. Write a Python script that demonstrates the difference between list concatenation and string concatenation.**

```python
# String concatenation
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)

# List concatenation
list1 = [1, 2]
list2 = [3, 4]
print(list1 + list2)

# + joins sequences together
# but behaviour depends on data type

```

----------

**36. Write a Python script that demonstrates why Python does not automatically combine strings and integers.**

```python
# Integer variable
age = 20

# The following line would produce TypeError
# because Python does not implicitly
# convert numbers into strings

# print("Age is " + age)

# Correct approach using explicit conversion
print("Age is " + str(age))

# Python prefers explicit type conversion

```

----------

**37. Write a Python script to demonstrate that tuples can contain mutable objects like lists. Modify the internal list and observe the result.**

```python
# Tuple containing a list
my_tuple = (1, 2, [3, 4])

# Print original tuple
print("Original tuple:", my_tuple)

# Modify list inside tuple
my_tuple[2].append(5)

# Print modified tuple
print("Modified tuple:", my_tuple)

# Tuple itself is immutable,
# but mutable objects inside it can change

```

----------

**38. Write a Python script that demonstrates use of sys.builtin_module_names.**

```python
# Import sys module
import sys

# Display built-in module names
print(sys.builtin_module_names)

# Python interpreter contains many built-in modules
# already compiled into the language

```

----------

**39. Write a Python script that demonstrates safe removal of items from a set using discard().**

```python
# Create a set
fruits = {"apple", "banana", "mango"}

# Remove existing item
fruits.discard("banana")

# Attempt to remove missing item
fruits.discard("orange")

# Print final set
print(fruits)

# discard() does not raise error
# if item is absent

```

----------

**40. Write a Python script that demonstrates the use of proper Python naming conventions for variables, constants, classes, and modules.**

```python
# Variable name using snake_case
student_age = 21

# Constant name using UPPER_SNAKE_CASE
MAX_RETRY_LIMIT = 5

# Class name using PascalCase
class StudentProfile:
    pass

# Print values
print(student_age)
print(MAX_RETRY_LIMIT)
print(StudentProfile)

# Python naming conventions improve readability
# and make code more maintainable

```






