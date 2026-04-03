


### Part 2 — Advanced Concepts of Generators

This section presumes a basic understanding of the idea of `yield`.

----------

#### 1. What Happens When a Generator Finishes?

When a generator finishes producing values, Python raises a special exception called: 

`StopIteration`

This is **not an error in your program**.

It simply signals that **no more values remain**.

#### Example Demonstrating StopIteration.

The following diagram shows how StopIteration works in generator functions.

![StopIteration Diagram](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch6-generators-stopiteration.png)


The following script shos the use of StopIteration for generator functions.

```python

# Demonstration of a simple generator and StopIteration

# 1. This generator function has multiple yield statements and print statements to show the flow of execution.
def simple_generator():
    """Generator with three yield statements."""

    print("Generator started")

    yield "yielding 1"     # First value returned
    print("Resuming after first yield")

    yield "yielding 2"     # Second value returned
    print("Resuming after second yield")

    yield "yielding 3"     # Third value returned
    print("Generator is about to finish")

# 2. Creating the generator object
gen = simple_generator()   # Function does NOT execute yet
print("Generator object created\n")


# 3. Manually retrieving values using next()
print("First next() call:")
print(next(gen))   # Generator starts executing
print("Second next() call:")
print(next(gen))
print("Third next() call:")
print(next(gen))

# 4. Generator is now exhausted
# Calling next() again raises StopIteration
print("Fourth next() call:")

try:
    print(next(gen))
except StopIteration:
    print("StopIteration raised → No more values left in generator!")

# 5. Using a generator inside a for-loop
print("Using generator in a for-loop:")

for value in simple_generator():
    print(value)

print("In a for-loop, StopIteration happens internally and is NOT shown.")


```


#### 2. How a for-loop Handles Generators

A `for` loop internally does something like this:

1.  Call `next()`
    
2.  Use the value
    
3.  Repeat
    
4.  Stop when `StopIteration` occurs
    

But the **exception is hidden from the user**.

Example:

```python
for  value  in  simple_generator():  
  print(value)
```


----------

#### 3. Fibonacci Generator

Generators are perfect for sequences like Fibonacci numbers.

```python

# Fibonacci generator

def fibonacci_generator():
    a, b = 0, 1  # Initialize the first two Fibonacci numbers

    while True:  # Loop indefinitely to generate Fibonacci numbers
        yield a
        a, b = b, a + b


fib = fibonacci_generator()

for _ in range(10):  # _ is a common convention for a variable that is not used
    print(next(fib))

```

#### 4. Generator Example — Prime Numbers


```python

# Generator for prime numbers greater than a given number

def is_prime(num):  # Helper function to check if a number is prime

    if num <= 1:  # 0 and 1 are not prime numbers
        return False

    for i in range(2, int(num**0.5) + 1):  # Check divisibility from 2 to sqrt(num)
        if num % i == 0:  # If num is divisible by any number in this range, it's not prime
            return False

    return True


def next_prime_generator(start):
    num = start + 1

    while True:  # Loop indefinitely to find the next prime number
        if is_prime(num):
            yield num  # Yield the prime number and pause until the next value is requested

        num += 1


prime_gen = next_prime_generator(100)  # Create a generator that will produce prime numbers greater than 100

# Get the first 10 prime numbers greater than 100. 
# Use _ as a throwaway variable since we don't need the loop index
for _ in range(10):  
    print(next(prime_gen))

```


#### 5. Advantages of Generators

The following table shows the advantages of using generators:-

| Advantage | Explanation |
| --- | --- |
| Memory efficient | values generated only when needed |
| Faster for large sequences | avoids building large lists |
| Maintains state automatically | variables preserved between yields |
| Works naturally with loops | integrates with Python iteration |














