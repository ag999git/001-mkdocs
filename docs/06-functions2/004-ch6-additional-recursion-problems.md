### Additional Problems on recursion

### 1. Recursive Function to Compute $a^b$

Another useful example of recursion is computing the value of:  $a^{b}$, where $a$ (base) and $b$ (exponent) are non-negative integers.


For example:

$2^5 = 2 × 2 × 2 × 2 × 2 = 32$

<div align="left">
 
$$
a^b = \begin{cases} 
1 & \text{if } b = 0 \\ 
a \times a^{(b-1)} & \text{if } b > 0 
\end{cases}
$$

</div>


Key Components of the Recursive Algorithm

| Component | Description |
| --- | --- |
| Base case | When b=0b = 0b=0, return 1 |
| Recursive case | Multiply a by the result of ab−1a^{b-1}ab−1 |
| Progress toward base case | The exponent decreases by 1 in each call |


```python

# Recursive function to compute a^b (base raised to exponent)
# The exponent is reduced by 1 in every recursive call
# until the base case (exponent = 0) is reached.

def power_recursive(base, exponent):
    
    # Returns base raised to the power exponent using recursion.
    
    # ---------- BASE CASE ----------
    # Any number raised to the power 0 is equal to 1
    if exponent == 0:
        print("Reached base case: exponent = 0 → returning 1")
        return 1

    # ---------- RECURSIVE CASE ----------
    # Reduce the exponent and call the function again
    print(f"Computing {base}^{exponent} → calling {base}^{exponent - 1}")

    # Recursive call with smaller exponent
    partial_result = power_recursive(base, exponent - 1)

    # Multiply base with result returned from recursion
    result = base * partial_result

    # Show the computation during the return phase
    print(f"Returning: {base}^{exponent} = {base} × {partial_result} = {result}")

    return result

# Test cases
# Each tuple contains (base, exponent)

test_cases = [
    (2, 5),   # 2^5 = 32
    (3, 4),   # 3^4 = 81
    (5, 0),   # 5^0 = 1
    (7, 1),   # 7^1 = 7
    (4, 3)    # 4^3 = 64
]

# Run the recursive function on each test case in the list and print the results
for base, exponent in test_cases:

    print("\n----------------------------------")
    print(f"Computing {base}^{exponent}")

    result = power_recursive(base, exponent)

    print(f"Final Result: {base}^{exponent} = {result}")

```


### 2. Using Recursion to Check Whether a String Is a Palindrome

A palindrome is a word, phrase, or sequence of characters that reads the same forward and backward.

Examples:
```python
madam
level
racecar

```

Each of these strings remains the same when the characters are reversed.

Idea Behind the Recursive Solution

A string is a palindrome if:

The first character and last character are the same.

The remaining middle portion of the string is also a palindrome.

For example:

```python
madam
Step-by-step comparison:

m   ada   m
↑         ↑
match
Now check the inner string:

ada
Again:

a  d  a
↑     ↑
match
Now check:
d
A single character is always a palindrome.

```

**Recursive Logic**

  

| Condition | Result |
| --- | --- |
| Length ≤ 1 | Palindrome (base case) |
| First ≠ Last | Not a palindrome |
| First = Last | Recursively check the inner substring |


Thus the recursion continues until the string becomes empty or one character long.

##### Recursive Python Implementation

```python


# Recursive function to check whether a string is a palindrome
# A palindrome reads the same forward and backward.

def is_palindrome(text):

    # Returns True if 'text' is a palindrome, otherwise False.

    # ---------- BASE CASE ----------
    # If the string has length 0 or 1,
    # it is automatically a palindrome
    if len(text) <= 1:
        return True

    # ---------- MISMATCH CHECK ----------
    # Compare the first and last characters
    if text[0] != text[-1]:
        return False   # characters differ → not a palindrome

    # ---------- RECURSIVE CASE ----------
    # Remove first and last characters
    # and test the remaining substring
    inner_text = text[1:-1]

    return is_palindrome(inner_text)



# Testing the palindrome function.

print(is_palindrome("level"))            # True
print(is_palindrome("madam"))            # True
print(is_palindrome("racecar"))          # True
print(is_palindrome("python"))           # False
print(is_palindrome("neveroddoreven"))   # True
print(is_palindrome(""))                 # True (empty string)
print(is_palindrome("a"))                # True (single character)

```


#### Optional Improvement (Often Done in Real Programs)

Real programs often ignore spaces and case differences.

Example:
```python
"Never Odd Or Even"
```

To handle this, we convert the string to lowercase and remove spaces before checking.

Example preprocessing:

`text = text.lower().replace(" ", "")`



### 3. Recursive Function to Find GCD (Greatest Common Divisor)

The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both numbers exactly.

For example: find $GCD(48, 18)$

Note that the common divisors of 48 and 18 are: $1, 2, 3, 6$
But the largest of these is 6.
So $GCD(48, 18) = 6$

##### Euclid’s Algorithm

It is one of the most efficient methods to compute the GCD is Euclid’s Algorithm.

The algorithm is based on the mathematical identity: $gcd(a,b)=gcd(b,amodb)$

where a mod b is the remainder when a is divided by b.

The recursion continues until the remainder becomes 0.

At that point: $gcd(a,0)=a$

This becomes the base case of the recursion.

Example

```python

Find GCD(48,18)

gcd(48,18)
= gcd(18, 48 % 18)
= gcd(18,12)

= gcd(12, 18 % 12)
= gcd(12,6)

= gcd(6, 12 % 6)
= gcd(6,0)

GCD = 6

```

Recursive Python Implementation


```python

# Recursive function to compute the nth Fibonacci number

def fibonacci_recursive(n):
    # Returns the nth Fibonacci number using recursion.
    # There are 2 base cases: Fibonacci(0) = 0 and Fibonacci(1) = 1

    # -------- Base Case 1 --------
    # If n = 0, return 
    if n == 0:
        return 0

    # -------- Base Case 2 --------
    # If n = 1, return 1 
    elif n == 1:
        return 1

    # -------- Recursive Case --------
    # Compute the sum of the previous two Fibonacci numbers
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Test calls

print(f"Fibonacci(5)  → {fibonacci_recursive(5)}")   # 5
print(f"Fibonacci(6)  → {fibonacci_recursive(6)}")   # 8
print(f"Fibonacci(7)  → {fibonacci_recursive(7)}")   # 13
print(f"Fibonacci(10) → {fibonacci_recursive(10)}")  # 55


```

The following diagram shows the flow of execution 

Below is a diagram that illustrates Euclid’s Algorithm for computing GCD using recursion.

The diagram shows the execution for: $gcd(48,18)$ . It has numbered blocks so students can follow the algorithm step-by-step.


![GCD](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch-6-functions2-gcd-recursion.png)


The following table explains each block in the flow chart:-

  

  

| Block No. | Block Description | What Happens in This Step | Example |
| --- | --- | --- | --- |
| 1 | Start | Begin the algorithm with two numbers a and b whose GCD we want to find. | gcd(48, 18) |
| 2 | Check if b = 0 | This is the base condition. If b = 0, the algorithm stops. | Check if 18 = 0 |
| 3 | Compute remainder | Calculate the remainder when a is divided by b using the modulo operator %. | 48 % 18 = 12 |
| 4 | Recursive call | Replace a with b and b with the remainder and call the function again. | gcd(18, 12) |
| 5 | Repeat process | Continue repeating the same steps until b becomes 0. | gcd(12, 6) → gcd(6, 0) |
| 6 | Return result | When b = 0, the value of a is the GCD. | gcd(6, 0) = 6 |


### 4. Recursive function to implement Tower of Hanoi

The recursion solution to the Tower of Hanoi is given in details in the book.

Some additional points are mentioned here

#### Below is the complete table of Tower of Hanoi states for 5 disks.

Conventions used:

Source = A

Auxiliary = B

Destination = C

Lists show disks largest → smallest (left → right).

Move 0 = initial state

Move 31 = final solved state

  
    

  

| Move | Disk Moved | Move | A (Source) | B (Aux) | C (Dest) |
| --- | --- | --- | --- | --- | --- |
| 0 | – | Initial | [5,4,3,2,1] | [] | [] |
| 1 | 1 | A→C | [5,4,3,2] | [] | [1] |
| 2 | 2 | A→B | [5,4,3] | [2] | [1] |
| 3 | 1 | C→B | [5,4,3] | [2,1] | [] |
| 4 | 3 | A→C | [5,4] | [2,1] | [3] |
| 5 | 1 | B→A | [5,4,1] | [2] | [3] |
| 6 | 2 | B→C | [5,4,1] | [] | [3,2] |
| 7 | 1 | A→C | [5,4] | [] | [3,2,1] |
| 8 | 4 | A→B | [5] | [4] | [3,2,1] |
| 9 | 1 | C→B | [5] | [4,1] | [3,2] |
| 10 | 2 | C→A | [5,2] | [4,1] | [3] |
| 11 | 1 | B→A | [5,2,1] | [4] | [3] |
| 12 | 3 | C→B | [5,2,1] | [4,3] | [] |
| 13 | 1 | A→C | [5,2] | [4,3] | [1] |
| 14 | 2 | A→B | [5] | [4,3,2] | [1] |
| 15 | 1 | C→B | [5] | [4,3,2,1] | [] |
| 16 | 5 | A→C | [] | [4,3,2,1] | [5] |
| 17 | 1 | B→A | [1] | [4,3,2] | [5] |
| 18 | 2 | B→C | [1] | [4,3] | [5,2] |
| 19 | 1 | A→C | [] | [4,3] | [5,2,1] |
| 20 | 3 | B→A | [3] | [4] | [5,2,1] |
| 21 | 1 | C→B | [3] | [4,1] | [5,2] |
| 22 | 2 | C→A | [3,2] | [4,1] | [5] |
| 23 | 1 | B→A | [3,2,1] | [4] | [5] |
| 24 | 4 | B→C | [3,2,1] | [] | [5,4] |
| 25 | 1 | A→C | [3,2] | [] | [5,4,1] |
| 26 | 2 | A→B | [3] | [2] | [5,4,1] |
| 27 | 1 | C→B | [3] | [2,1] | [5,4] |
| 28 | 3 | A→C | [] | [2,1] | [5,4,3] |
| 29 | 1 | B→A | [1] | [2] | [5,4,3] |
| 30 | 2 | B→C | [1] | [] | [5,4,3,2] |
| 31 | 1 | A→C | [] | [] | [5,4,3,2,1] |

  
Given below is the script which implements the Tower of Hanoi problem

```python

# Tower of Hanoi using three lists representing towers A, B, C. Each list acts
# like a stack. In the list leftmost item is at bottom (Biggest) and rightmost 
# is at top (Smallest). The script also counts and displays move numbers.

def print_towers(towers):
    """Display the current state of all three towers."""
    print(f"A: {towers['A']}   B: {towers['B']}   C: {towers['C']}")
    print("-" * 40)

def move_disk(towers, source, target, move_counter):
    # Move top disk from one tower to another also increment the move counter

    disk = towers[source].pop()     # Remove top disk from source
    towers[target].append(disk)     # Place disk on target

    move_counter[0] += 1            # Increment move count

    print(f"Move {move_counter[0]}: disk from {source} → {target}")
    print_towers(towers)

def hanoi_recursive(n, source, target, auxiliary, towers, move_counter):
    """
    Recursive solution to Tower of Hanoi.

    n         -> number of disks
    source    -> source tower (A/B/C)
    target    -> target tower (A/B/C)
    auxiliary -> auxiliary tower (A/B/C)
    towers    -> dictionary storing the towers
    move_counter -> list used to track number of moves
    """

    # -------- Base Case --------
    if n == 1:
        move_disk(towers, source, target, move_counter)
        return

    # -------- Recursive Case --------

    # Step 1: Move n-1 disks from source → auxiliary
    hanoi_recursive(n - 1, source, auxiliary, target, towers, move_counter)

    # Step 2: Move largest disk from source → target
    move_disk(towers, source, target, move_counter)

    # Step 3: Move n-1 disks from auxiliary → target
    hanoi_recursive(n - 1, auxiliary, target, source, towers, move_counter)

# INITIAL SETUP

num_disks = 3

# Towers represented as a dictionary. Create initial state for tower A with 
# disks from largest on left to smallest on right.
initial_state_A = list(range(num_disks, 0, -1)) 
# Initialize towers with initial_state_A for tower A. Empty lists for B & C
towers = {"A": initial_state_A, "B": [], "C": []}

# Move counter stored in a list so recursion can update it
move_counter = [0]

print("Initial State")
print_towers(towers)

# Solve the puzzle
hanoi_recursive(num_disks, "A", "C", "B", towers, move_counter)

# Display total moves
print(f"Total moves required: {move_counter[0]}")

```

#### Detailed discussion of the script given above.
The following section discusses the above script in detaila

##### 1. Representation of Towers and conventions used in the script

The towers are represented using Python lists.

```python

Example initial state for 3 disks:
A: [3, 2, 1]
B: []
C: []

```

Important conventions used in the script:

  

| List Position | Meaning |
| --- | --- |
| Left side | Bottom of tower |
| Right side | Top of tower |

Thus:

```python

[3, 2, 1]

means

3 (largest disk at bottom)
2
1 (smallest disk at top)
2. The towers Dictionary

```

The three towers are stored in a dictionary:

`towers = {"A": initial_state_A, "B": [], "C": []}`

This allows us to refer to towers by name:
```python

towers["A"]
towers["B"]
towers["C"]

Example state:

A: [3]
B: [2]
C: [1]

```


##### 2. The `print_towers()` Function

Purpose: Displays the current configuration of the towers.

Function definition:

`def print_towers(towers):`


This function helps the reader visualize how disks move after each step.

##### 4. The `move_disk()` Function

Purpose: Moves one disk from a source tower to a target tower.

Function definition:
`move_disk(towers, source, target, move_counter)`

Parameters:

| Parameter | Meaning |
| --- | --- |
| towers | dictionary containing the three towers |
| source | tower from which disk is removed |
| target | tower to which disk is moved |
| move_counter | counts the number of moves |




##### 5. Removing top disk, placing disk on target tower and incrementing move counter
**The following line of script removes disk from top**
`disk = towers[source].pop()  # Remove top disk`

Since lists behave like stacks, `.pop()` removes the top disk.

**The following line in script places the disk on the target tower**

`towers[target].append(disk)  #Place disk on target tower`

**The following line of script increments the counter representing number of moves**
`move_counter[0] += 1`



##### 6. The `move_counter` Variable
`move_counter = [0]`

Why a list instead of a normal integer? Because lists are mutable objects in Python.

When recursion calls functions repeatedly, the list allows all recursive calls to update the same counter.

Thus every move increases the same shared counter.

##### 7. The `hanoi_recursive()` Function

This is the core algorithm.

Function definition:

`hanoi_recursive(n, source, target, auxiliary, towers, move_counter)`

Parameters:
  

| Parameter | Meaning |
| --- | --- |
| n | number of disks to move |
| --- | --- |
| source | tower where disks start |
| --- | --- |
| target | tower where disks must go |
| --- | --- |
| auxiliary | temporary tower used during movement |
| --- | --- |
| towers | dictionary storing towers |
| --- | --- |
| move_counter | counts moves |
| --- | --- |


###### 8. The Base Case

```python

if n == 1:
    move_disk(...)
```

If only one disk remains, simply move it directly from source to target.

Example:

`A → C`

This stops the recursion.

##### 9. The Recursive Case

When more than one disk exists, the algorithm performs three steps.

**Step 1**

Move n−1 disks from source → auxiliary

`hanoi_recursive(n-1, source, auxiliary, target)`

Example: Move disks 1 and 2 from A → B

**Step 2**

Move the largest disk from source → target

`move_disk(...)`

Example: Move disk 3 from A → C

**Step 3**

Move the n−1 disks from auxiliary → target

`hanoi_recursive(n-1, auxiliary, target, source)`

Example: Move disks 1 and 2 from B → C

###### Overall Flow of the Program

```python

Initial state printed
        ↓
hanoi_recursive called
        ↓
Recursive breakdown of problem
        ↓
Each move performed using move_disk()
        ↓
Towers printed after each move
        ↓
Final state reached
        ↓
Total moves displayed
```



### 5. Recursive function to find a number is even or not. (Not very efficient)

We can test a number to be even or odd by recursion also. The steps are as follows:-

 - If number is negative, reverse its sign. 
 - Base condition is when    number is 0 or 1. If 0 it is even, if 1 it is odd.
 - Recursively subtract 2 from the number until it becomes less than 2

> [!TIP]
A number can be tested for **evenness or oddness** using recursion.  
However, this is mainly useful **for learning recursion**, not for efficiency. In practice, Python programmers normally use the **modulus operator (`%`)**.

Idea Behind the Recursive Method. The recursive method is based on the following observations:

  

| Observation | Explanation |
| --- | --- |
| Even numbers differ by 2 | If a number is even, subtracting 2 repeatedly will eventually reach 0 |
| Odd numbers differ by 2 | If a number is odd, subtracting 2 repeatedly will eventually reach 1 |


Thus we use the following rules:

1.  If the number is **negative**, convert it to positive (because even/odd property does not change).  
2.  If the number becomes **0**, it is **even**. _(Base case)_
    
3.  If the number becomes **1**, it is **odd**. _(Base case)_
    
4.  Otherwise subtract **2** and repeat the process recursively.

Recursive Logic

  

  

| Condition | Result |
| --- | --- |
| n = 0 | number is even |
| n = 1 | number is odd |
| n > 1 | check (n − 2) recursively |

```python

# ------------------------------------------------------------
# Recursive function to determine whether a number is even
# ------------------------------------------------------------
# The function repeatedly subtracts 2 from the number
# until it reaches one of the base cases (0 or 1).
# ------------------------------------------------------------

def is_even_recursive(n):
    """
    Returns True if the number is even
    Returns False if the number is odd
    Uses recursion for demonstration purposes.
    """

    # Convert negative numbers to positive
    # (Even/odd property does not change with sign)
    n = abs(n)

    # ---------- Base Cases ----------
    # If n becomes 0, the number is even
    if n == 0:
        return True

    # If n becomes 1, the number is odd
    if n == 1:
        return False

    # ---------- Recursive Case ----------
    # Reduce the problem size by subtracting 2
    return is_even_recursive(n - 2)


# ------------------------------------------------------------
# Example calls
# ------------------------------------------------------------

print("-92 is even?  ", is_even_recursive(-92))   # True  (-92 → 92 → even)
print("17 is even?  ", is_even_recursive(17))    # False (odd)
print("100 is even?  ", is_even_recursive(100))   # True  (even)

```

##### Example Trace: Checking if 7 is Even

The recursive calls proceed as follows:

  

| Step | Function Call |
| --- | --- |
| 1 | is_even_recursive(7) |
| 2 | is_even_recursive(5) |
| 3 | is_even_recursive(3) |
| 4 | is_even_recursive(1) |
| 5 | Base case reached → return False |
  


##### Visual Representation of the Recursion

```python

is_even_recursive(7)
      ↓
is_even_recursive(5)
      ↓
is_even_recursive(3)
      ↓
is_even_recursive(1)
      ↓
Base case → return False

```

##### Why This Method Is Not Efficient

Although recursion works here, it is not efficient for large numbers.

Example:

`is_even_recursive(1,000,000)`

This would require 500,000 recursive calls.

The efficient method is:

`n % 2 == 0`

which completes in one step.























