

### 1. `zip()` Function

#### Concept

The `zip()` function combines elements from **two or more iterables** into **tuples**.

Each tuple contains elements taken from the **same position** in the input iterables.

The function **stops when the shortest iterable is exhausted**.

Thus, `zip()` is often used when you want to **iterate over multiple sequences in parallel**.

----------

#### Syntax

`zip(*iterables)`

Where:

-   `iterables` may be lists, tuples, strings, ranges, etc.
    
-   The result is a **zip object (iterator)**.
    

----------

#### Key Properties

  

| Feature | Description |
| --- | --- |
| Works with any iterable | lists, tuples, strings, ranges |
| Returns | iterator object |
| Output format | tuples |
| Stops when | shortest iterable ends |
| Common use | parallel iteration |

Script Demonstrating `zip()`

```python

# Demonstration of the zip() function in Python

# 1. Zipping two lists")

list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']

z = zip(list1, list2)

print("Type of result:", type(z))  # <class 'zip'> - zip() returns an iterator of tuples
# Convert iterator to list to view contents
print("Zipped result:", list(z))  # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

# 2: Zipping sequences of unequal length

a = [10, 20, 30, 40]
b = ['x', 'y']

result = list(zip(a, b))

# Stops when shortest iterable finishes
print(result)  # [(10, 'x'), (20, 'y')]

# 3: Zipping three sequences

names = ["Alice", "Bob", "Charlie"]
ages = [21, 22, 23]
cities = ["Delhi", "Mumbai", "Kolkata"]

combined = list(zip(names, ages, cities))

print(combined)  # [('Alice', 21, 'Delhi'), ('Bob', 22, 'Mumbai'), ('Charlie', 23, 'Kolkata')]

# 4: Iterating with zip

numbers = [1,2,3]
letters = ['A','B','C']

for n, l in zip(numbers, letters):
    print(n, l)

# Output:
# 1 A
# 2 B
# 3 C

# 5: Unzipping sequences

pairs = [(1,'a'), (2,'b'), (3,'c')]

x, y = zip(*pairs)

print("Numbers:", x)  # (1, 2, 3)
print("Letters:", y)  # ('a', 'b', 'c')

# 6: Creating dictionary using zip

keys = ['name','age','city']
values = ['Rahul', 25, 'Delhi']

dictionary = dict(zip(keys, values))
print(dictionary)  # {'name': 'Rahul', 'age': 25, 'city': 'Delhi'}

```


### 2. Lambda Functions

#### Concept

A **lambda function** is a small anonymous function.

Unlike normal functions defined with `def`, lambda functions:

-   have **no name**
    
-   are written in **a single expression**
    

They are commonly used when a **small temporary function** is required.

----------

#### Syntax

`lambda arguments : expression`

Example:

`lambda x : x * x`

----------

#### Key Characteristics
  

  

| Feature | Description |
| --- | --- |
| Anonymous | no function name |
| One expression only | no statements |
| Automatic return | expression result returned |
| Often used with | map(), filter(), sorted() |


```python

# Demonstration of lambda functions

# 1: Normal function
def square(x):
    return x * x

print(square(5))  # 25 

# 2: Lambda equivalent

square_lambda = lambda x: x * x
print(square_lambda(6))  # 36

# 3: Lambda with multiple arguments

add = lambda x, y: x + y
print(add(3, 4))  # 7

# 4: Lambda with three arguments

sum_three = lambda a, b, c: a + b + c
print(sum_three(2,3,4))  # 9

# 5: Lambda inside sorted

students = [("Alice", 23), ("Bob", 21), ("Charlie", 25)]

# Sort by age
sorted_students = sorted(students, key=lambda x: x[1])

print(sorted_students)  # [('Bob', 21), ('Alice', 23), ('Charlie', 25)] 


```

### 3. `map()` Function

#### Concept

The `map()` function applies a **function to every element of an iterable**.

It returns a **map object (iterator)**.

----------

#### Syntax

`map(function, iterable)`

Multiple iterables can also be used:

`map(function, iterable1, iterable2)`

----------

#### Key Properties

  

  

| Feature | Description |
| --- | --- |
| Input | function + iterable |
| Output | map iterator |
| Purpose | transform elements |
| Works with | multiple iterables |


```python

# Demonstration of map() function

# 1: Using map with normal function
def cube(n):
    return n ** 3

numbers = [1,2,3,4,5]

# 2. Using map to apply cube function to each element in numbers
cube_map = map(cube, numbers)
print(list(cube_map))  # [1, 8, 27, 64, 125]

# 3: Using map with lambda function
numbers = [1,2,3,4,5]
cubes = map(lambda x: x**3, numbers)
print(list(cubes))  # [1, 8, 27, 64, 125]

# 4: Using map with two lists
list1 = [1,2,3,4]
list2 = [10,20,30,40]
result = map(lambda x, y: x + y, list1, list2)
print(list(result))  # [11, 22, 33, 44]

# 5: Converting strings to integers
string_numbers = ["10","20","30"]
integers = map(int, string_numbers)
print(list(integers))  # [10, 20, 30]


```


# 4. `filter()` Function

### Concept

The `filter()` function selects elements from an iterable based on a **Boolean condition**.

The filtering function must return **True or False**.

----------

#### Syntax

`filter(function, iterable)`

----------

#### Key Properties

  

| Feature | Description |
| --- | --- |
| Input | function returning Boolean |
| Output | filter iterator |
| Purpose | selection of elements |

#### Script Demonstrating `filter()`

```python

# Demonstration of filter() function

# 1: Filtering even numbers
numbers = list(range(10))
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # [0, 2, 4, 6, 8]

# 2: Filtering positive numbers
data = [-5, -2, 0, 3, 7, -1]
positive_numbers = filter(lambda x: x > 0, data)
print(list(positive_numbers))  # [3, 7]

# 3: Filtering strings longer than 3 characters
words = ["cat", "elephant", "dog", "tiger"]
long_words = filter(lambda x: len(x) > 3, words)
print(list(long_words))  # ['elephant', 'tiger']

# 4: Using filter with normal function
def is_odd(n):
    return n % 2 != 0

numbers = list(range(10))
odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))  # [1, 3, 5, 7, 9]


```




























