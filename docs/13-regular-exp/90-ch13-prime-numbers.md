

## Assignment: Detecting Prime Numbers Using Regular Expressions

### Objective

Use **regular expressions (regex)** to determine whether a given number is **prime**, **without using any arithmetic operations** such as division (`/`, `%`) or loops that test factors.

This assignment is designed to help you understand:

-   Pattern matching beyond simple text search
    
-   Capturing groups and **backreferences**
    
-   **Greedy vs non-greedy** quantifiers
    
-   Creative problem solving with regex
    

----------

### Problem Statement

Write a Python function:

```python
def  is_prime_unary(n: int):
    ...
    ...
``` 

that returns:

-   `True` if `n` is a **prime number**
    
-   `False` otherwise
    

### Restrictions

You **must not**:

-   Use division, modulus, or factorization
    
-   Use libraries for primality testing
    
-   Hardcode prime numbers
    

You **must**:

-   Use the `re` module
    
-   Use **at least one capturing group** and a **backreference**
    
-   Base your solution primarily on a **regular expression**
    

----------

### Conceptual Insight

Prime numbers have **no equal factors other than 1 and themselves**.

If a number **can be broken into equal-sized repeating parts**, it is **not prime**.

----------

### Hints 

#### Hint 1: Change the problem domain

Instead of working with numbers, convert the number into a **string**.

> Example:  
> `5 → "11111"`

This representation is called **unary**.

----------

#### Hint 2: Think in terms of repetition

A **composite number** can be written as:

`(block)(block)(block)...(block)` 

Example:

`9 → "111111111" → "111" + "111" + "111"` 

What regex feature allows you to match _repeated identical patterns_?

----------

#### Hint 3: Use capturing groups

Try capturing a block of `'1'` characters and check whether the **entire string** consists of repeated copies of that block.

Key idea:

`(captured_pattern)\1+` 

----------

#### Hint 4: Handle special cases

What about:

-   `n = 0`
    
-   `n = 1`
    

Are these prime?  
How can regex help detect very short strings?

----------

#### Hint 5: Greedy vs Non-Greedy

If your regex doesn’t work as expected, ask yourself:

-   Is the engine capturing **too much**?
    
-   Would a **non-greedy quantifier (`+?`)** help?
    

Try both and observe the difference.

----------

### Suggested Test Cases

You should test at least:

`0 → False
1 → False
2 → True
3 → True
4 → False
5 → True
6 → False
7 → True
9 → False
11 → True` 

----------

### Deliverables

You should submit:

1.  Python function code
    
2.  The regex pattern used
    
3.  A **written explanation** of:
    
    -   How the regex works
        
    -   Why it detects composite numbers
        
    -   Why primes fail to match

## Solution
#### The following script gives detailed implementation (along with step by step explanation) of the problem

```python
import re

def is_prime_unary(n: int) -> bool:
    """
    Check whether a number is prime using a regular expression
    applied to its unary representation.

    Core idea:
    1. Convert the number n into unary form: n → "111...1"
    2. A composite number can be split into equal repeating blocks.
        Examples:
        4  → "1111" = "11" repeated 2 times. So 4 is not prime
        9  → "111111111" = "111" repeated 3 times. So 9 is not prime
        10 → "1111111111" = "11111" repeated 2 times. So 10 is not prime
        11 → "11111111111" cannot be split this way. So 11 is prime
    3. Prime numbers cannot be split this way (except trivial cases).

    IMPORTANT:
    - This method is for learning REGEX concepts:
        * grouping
        * backreferences
        * greedy vs non-greedy matching
    - It is extremely inefficient for large numbers.
    """

    # The pattern r'^1?$|^(11+?)\1+$' is composed of two main parts separated by the pipe (|) operator.
    # Part 1: ^1?$ 
    # - ^ asserts the start of the string.
    # - 1? matches zero or one occurrence of '1'. ? makes it optional, allowing for both the empty string and a single '1'.
    # - zero '1's corresponds to the number 0 (not prime), and 
    # - one '1' corresponds to the number 1 (not prime).
    # - $ asserts the end of the string
    # So, ^1?$ matches the unary representations of 0 and 1, which are not prime.
    
    # Part 2: ^(11+?)\1+$
    # - ^ asserts the start of the string.
    # - (11+?) captures a block of at least two '1's (the smallest composite factor)
    #   - 11+ matches a sequence of '1's that is at least two characters long (e.g., "11", "111", "1111", etc.)
    #   - The +? makes this match NON-GREEDY, meaning it will capture the smallest possible block of '1's 
    #     that satisfies the condition (e.g., "11" instead of "111" if both are possible).
    # - \1+ repeats the captured block one or more times
    # - $ asserts the end of the string
    # ^(11+?)\1+$     → matches repeated equal blocks:
    #   (11+?)        → capture a block of at least two '1's
    #                   '+' ensures length ≥ 2
    #                   '?' makes it NON-GREEDY (smallest block first)
    #
    #   \1+           → repeat the *same captured block*
    #                   until the end of the string
    # In conclusion, if the string of '1's can be split into equal blocks of at least two '1's, it is not prime.
    non_prime_pattern = r'^1?$|^(11+?)\1+$'

    # Convert the number to unary representation
    # Example: n = 5 → "11111"
    unary = "1" * n

    # Try to match the NON-PRIME pattern
    match = re.match(non_prime_pattern, unary)

    # If there is NO match, the number is prime
    return match is None


# Demonstration
print("is_prime_unary(7) ->", is_prime_unary(7))   # True  (prime)
print("is_prime_unary(9) ->", is_prime_unary(9))   # False (composite)



```













