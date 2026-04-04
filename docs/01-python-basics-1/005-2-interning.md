


## Interning (Advance concept)

Interning is a memory-optimisation technique where Python reuses certain immutable objects instead of creating new ones every time. Think of it like Python keeping a small cache of commonly used values.

When you create a new variable with one of those values:- Python reuses the same object  
instead of creating a new object in memory. This improves: **(1)** speed, **(2)** memory usage.

Where does interning happen? Python commonly interns:- **(1)** Small integers: Usually from –5 to 256, **(2)** Short strings- (especially identifiers, e.g., `"hello", "user", "abc"`), **(3)** Empty immutable values like empty string `""`, empty tuple `()`, etc.

**Why does Python do this?** Because: **(1)** These values appear very often in programs. **(2)** They never change (immutable). **(3)** Reusing them saves memory and speeds up comparisons.

The following example script shows how interning can affect the use of "`is`" and "`==`".

```python

# Example 1: Small Integer Interning
a = 256
b = 256
print(a is b)  # True -> small integers are interned
print(a == b)  # True -> values are equal

# Example 2: Large integers (not interned by default)
num1 = 10000
num2 = 10000
print(num1 is num2)  # False in some implementations
print(num1 == num2)  # True -> values are equal
# Explanation: 'is' checks for object identity, while '==' checks for value equality.

# Example 3: Interning does NOT affect ==, because the values 
# are compared, not the object locations.
x = 1000000
y = 1000000
print(x is y)  # False in some implementations
print(x == y)  # True -> values are equal

# Example 4: String Interning
str1 = "hello"
str2 = "hello"
print(str1 is str2)  # True -> due to string interning  
print(str1 == str2)  # True -> values are equal

# Example 5: Large strings (not interned by default)
large_str1 = "a" * 1000
large_str2 = "a" * 1000
print(large_str1 is large_str2)  # False in some implementations
print(large_str1 == large_str2)  # True -> values are equal

# Example 6: Lists are not interned
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 is list2)  # False -> different objects in memory
print(list1 == list2)  # True -> values are equal



```












