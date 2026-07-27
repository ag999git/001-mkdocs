



# Project: Modern Random Number Generation in NumPy

NumPy provides two ways to generate random numbers:  
the older `np.random` functions and the newer  
`np.random.default_rng()` approach.

## Task

## Part A — Conceptual Study

Investigate the following:

1.  What is the difference between:
    -   `np.random.seed()` and
    -   `np.random.default_rng(seed)`
2.  Why does NumPy recommend using `default_rng()` in modern applications?
3.  What problems can arise from using global random state?
4.  Explain the role of randomness in:
    -   simulations
    -   machine learning
    -   data analysis

----------

## Part B — Practical Task

Write a Python program that:

1.  Creates random arrays using both:
    -   old API (`np.random`)
    -   new API (`default_rng()`)
2.  Uses the following distributions:
    -   uniform
    -   normal
    -   integers
3.  Demonstrates:
    -   reproducibility using seeds
    -   independence of generators
4.  Compares outputs and documents observations.

----------

## Expected Outcome

You should be able to explain:

-   Why modern random generators are preferred
-   When reproducibility matters
-   How different distributions behave

----------

## PART 2 — ANSWER)

----------

## ANSWER — THEORY

### 1. Global vs Local Random State

-   `np.random.seed()` sets a **global state**
-   Affects all random operations in the program
-   Can cause unintended interference

Example problem:  Two functions using randomness may affect each other.

----------

## 2. Generator-Based Approach

`np.random.default_rng()` creates an **independent generator**

-   Each generator has its own state
-   Safer for experiments
-   Better for parallel computing

----------

## 3. Why Modern API is Preferred

  

| Feature | Old API | New API |
| --- | --- | --- |
| State | Global | Local |
| Control | Limited | High |
| Reproducibility | Risky | Reliable |
| Parallel use | Poor | Strong |

## 4. Role of Randomness

-   **Simulations** → modeling uncertainty
-   **Machine Learning** → weight initialization
-   **Statistics** → sampling



## Detailed explanation of the difference between the old and new API

## 1. First: What does “same seed” mean?

A **seed** fixes the starting point of a random sequence.

Same seed ⇒ same sequence (always)

This is true for **both old and new API**.

----------

# Example (Both give SAME output)

```python
import  numpy  as  np  
  
np.random.seed(0)  
print(np.random.rand(3))  
  
np.random.seed(0)  
print(np.random.rand(3)) # same output

rng1  =  np.random.default_rng(0)  
rng2  =  np.random.default_rng(0)  
  
print(rng1.random(3))  
print(rng2.random(3)) # same output
```

So far → **no difference**

----------

## 2. Then where is the difference?

The difference is in **How the sequence is managed**

----------

### Old API → Global State (Shared)

There is **one single hidden random generator** in the whole program.

Everyone uses the same generator

----------

### Example (Interference Problem)

```python
import  numpy  as  np  
  
np.random.seed(0)  
  
a  =  np.random.rand(3) # first call  
b  =  np.random.rand(3) # second call  
  
print(a)  
print(b)
```

> **`b` depends on the fact that `a` was already generated**

----------

#### Important Insight

If you change code order:
```python
np.random.seed(0)  
  
b  =  np.random.rand(3)  
a  =  np.random.rand(3)
```

> **Now values of `a` and `b` change**

----------

### That’s the problem:

> **Old API = shared global sequence → order matters → bugs possible**

----------

## New API → Independent Generators

Each `rng` is its own **separate random machine**

----------

### Example (No Interference)

```python
rng1  =  np.random.default_rng(0)  
rng2  =  np.random.default_rng(0)  

a  =  rng1.random(3)  
b  =  rng2.random(3)  
  
print(a)  
print(b)
```

> **Same output (same seed)**

----------

Now continue:
```python
a_next  =  rng1.random(3)  
b_next  =  rng2.random(3)  
  
print(a_next)  
print(b_next)
```

> **Still same**

----------

### Key Insight

Each generator runs its **own independent sequence**











