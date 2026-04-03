

## Conceptual Questions and Answers

### a. Python interprets non-zero values as True

### Answer

In Python, any non-zero number---positive or negative---is treated as
**True** in a Boolean context.

``` python
if -5:
    print("Negative numbers are True")

if 10:
    print("Positive numbers are also True")

if 0:
    print("This will not print because 0 is False")
```

### b. What are nested if-else statements? How can you avoid them?

### Answer

Nested if-else means placing one if-else inside another.

``` python
age = 16
if age >= 13:
    if age < 18:
        print("Teenager")
```

You can avoid nesting using **logical operators**:

``` python
age = 16
if age >= 13 and age < 18:
    print("Teenager")
```

### c. Logical operators can help avoid nested if-else statements. How?

### Answer

Logical operators like `and`, `or`, `not` combine conditions so you
don't need multiple inner if blocks.

Example:

``` python
score = 75
if score >= 50 and score < 90:
    print("Pass but not distinction")
```

### d. Python does not have do--until syntax. How to implement it?

### Answer

Use a `while True` loop with a `break` when condition becomes true.

``` python
while True:
    x = int(input("Enter a number: "))
    if x > 0:
        break
```

### e. What is the use of the pass statement?

### Answer

`pass` is a placeholder used when a statement is required but you don't
want to do anything yet.

``` python
for i in range(5):
    pass  # TODO: implement later
```

### f. Definite vs. Indefinite loops

### Answer

-   **for loop (definite)** → number of iterations is known.
-   **while loop (indefinite)** → number of iterations is unknown in
    advance.

### g. What is an infinite loop?

### Answer

A loop that **never stops** is an infinite loop.

``` python
while True:
    print("This will run forever (use Ctrl+C to stop)")
```

### h. Nested for loops for comparing two collections

### Answer

Used when you want to compare each item of one collection with every
item of another.

``` python
s1 = "cat"
s2 = "hat"
for ch1 in s1:
    for ch2 in s2:
        if ch1 == ch2:
            print(ch1, "matched")
```

### i. When should you use `while` versus `for`?

### Answer

-   Use **for** when number of iterations is known or when iterating
    over a collection.
-   Use **while** when repetition depends on a condition.

### j. `range()` creates arithmetic progressions

### Answer

`range()` generates numbers in a sequence with fixed step.

``` python
for n in range(2, 10, 2):
    print(n)  # 2, 4, 6, 8
```

### Additional Questions

### k. What is short-circuit evaluation?

### Answer

Python stops evaluating once result is known.

``` python
x = 0
if x != 0 and (10/x) > 1:
    print("Won't run")
```

### l. What is the purpose of continue?

### Answer

`continue` skips rest of loop iteration.

``` python
for i in range(5):
    if i == 2:
        continue
    print(i)
```





## Programming Exercises --- Questions and Answers

### a. Write a Python program to test whether a number is between 1000 and 2000.

### Answer

``` python
num = int(input("Enter a number: "))

if 1000 <= num <= 2000:
    print("The number is between 1000 and 2000.")
else:
    print("The number is NOT between 1000 and 2000.")
```

### b. Program to check whether a number is even or odd.

### Answer

``` python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

### c. Compute the sum: 1/2 + 2/3 + 3/4 + ... + n/(n+1)

### Answer

``` python
n = int(input("Enter n: "))

total = 0
for i in range(1, n+1):
    total += i / (i + 1)

print("Sum =", total)
```

### d. Generator for numbers divisible by 3 and 5 between 0 and 100.

### Answer

``` python
def divisible_by_3_and_5():
    for num in range(101):
        if num % 3 == 0 and num % 5 == 0:
            yield num

print(list(divisible_by_3_and_5()))
```

### e. GCD using Euclidean Algorithm.

### Answer

``` python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("GCD =", gcd(x, y))
```

### f. Armstrong numbers between 1 and 1000.

### Answer

``` python
def is_armstrong(num):
    digits = str(num)
    n = len(digits)
    total = sum(int(d)**n for d in digits)
    return total == num

result = []
for i in range(1, 1001):
    if is_armstrong(i):
        result.append(i)

print("Armstrong numbers 1–1000:", result)
```

### g. Hailstone sequence --- iterative and recursive.
The hailstone sequence is (1) Pick a positive integer n as the start. (2) If n is even, divide it by 2 (3) If n is odd, multiply it by 3 and add 1. (4) Continue this process until n is 1.

The number n goes up and down but eventually end at 1. 

Write a python script which takes a random number between 50 and 100 and generate its hailstone sequence. 
Note:- This problem can be solved both by iterative and recursive methods. Write scripts for both. The script should also print the number of items generated. For example
No of items in hailstone series for n = 68 -> 14
Hailstone list for 68 is-> `[34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]`




### Answer

#### Iterative Method

``` python
def hailstone_iterative(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
    sequence.append(1)
    return sequence

import random
n = random.randint(50, 100)
seq = hailstone_iterative(n)
print(f"No. of items for n={n} ->", len(seq))
print("Sequence:", seq)
```

#### Recursive Method

``` python
def hailstone_recursive(n, seq=None):
    if seq is None:
        seq = []
    seq.append(n)
    if n == 1:
        return seq
    if n % 2 == 0:
        return hailstone_recursive(n//2, seq)
    else:
        return hailstone_recursive(3*n + 1, seq)

import random
n = random.randint(50, 100)
seq = hailstone_recursive(n)
print(f"No. of items for n={n} ->", len(seq))
print("Sequence:", seq)
```

### h. Check for Prime

### Answer

``` python
num = int(input("Enter number: "))

is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

print("Prime" if is_prime else "Not Prime")
```

### i. Sum of digits of a number

### Answer

``` python
num = input("Enter number: ")
total = sum(int(d) for d in num)
print("Sum of digits:", total)
```




