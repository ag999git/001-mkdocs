

## Project: (Using `np.stack`)

### **Project/Research Question**

> **"In Machine Learning, we often need to combine multiple independent 2D datasets (like images or classroom records) into a single 3D structure without losing the identity of the original groups. Investigate the `np.stack()` function in NumPy. Explain how it differs from traditional joining methods like `vstack` and `hstack`. Demonstrate, through a Python script, how to create a 3D 'Data Cube' from 2D sources, and discuss the architectural implications of stacking along different axes (Axis 0 vs. Axis 1)."**

----------

## Answer & Technical Note: Understanding `np.stack()`

### 1. The Core Concept

Standard joining functions (`concatenate`, `vstack`, `hstack`) work **within existing dimensions**. If you have two 2D arrays, they stay 2D.

`np.stack()`, however, is a **Dimensional Upgrader**. It takes a sequence of arrays of the same shape and joins them along a **new axis**.

-   If you stack two 1D vectors, you get a 2D matrix.
    
-   If you stack two 2D matrices, you get a 3D tensor.
    

**Analogy:**

-   **`vstack`**: Taping two pages together to make one giant, long page.
    
-   **`stack`**: Putting one page on top of the other to start a book. You now have a "Page Number" dimension that didn't exist before.
    

### **2. Common Use Cases (Advance- can ignore)**

-   **Image Batching (AI):** Combining 32 individual images (each 28x28 pixels) into a single "Batch" array of shape $(32, 28, 28)$ for a Neural Network.
    
-   **Time-Series Data:** Stacking daily sales reports (2D) into a monthly report (3D).
    
-   **Multi-Sensor Data:** Stacking data from "Sensor A" and "Sensor B" while keeping their readings separate but aligned.
    

### 3. Comparative Table: `vstack` vs. `hstack` vs. `stack`

  

| Feature | np.vstack | np.hstack | np.stack |
| --- | --- | --- | --- |
| Dimension Change | Stays same (e.g., 2D) | Stays same (e.g., 2D) | Increases (e.g., 2D → 3D) |
| Logic | Adds more Rows | Adds more Columns | Adds a New Axis |
| Analogy | A longer list | A wider table | A stack of papers |
| Requirement | Columns must match | Rows must match | Shapes must be identical |


### 4. The "Do's and Don'ts" & Common Errors

#### DOs:

-   Use `np.stack` when you want to keep the original arrays as distinct "sub-entities" (e.g., `stacked[0]` is Class A, `stacked[1]` is Class B).
    
-   Ensure all input arrays have the **exact same shape**.
    

#### DON'Ts:

-   Don't use `stack` if you just want to append data to an existing list (use `vstack` or `concatenate` for that).
    
-   Don't forget to check the `axis` parameter. Stacking on `axis=0` vs `axis=1` produces very different 3D structures.
    

#### Common Errors:

-   **`ValueError: all input arrays must have the same shape`**: This happens if Array A is $(3, 4)$ and Array B is $(3, 5)$. Unlike `hstack`, `stack` is strictly symmetrical.
    
-   **`IndexError`**: Trying to access `axis=2` on a 2D array stack.
    

----------

### **5. Simple script explaining the concepts

```python

import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

# 1. Stacking arrays vertically (row-wise)
result = np.stack((a, b), axis=0)  # Stacks a and b vertically (row-wise)
print(result.shape)  # Output: (2, 3)
print(result)
# Output: 
# [[1 2 3]
#  [4 5 6]]
# Two arrays became 2 rows

# 2. Stacking arrays horizontally (column-wise)
result2 = np.stack((a, b), axis=1)  # Stacks a and b horizontally (column-wise)
print(result2.shape)  # Output: (3, 2)  
print(result2)
# Output:
# [[1 4]
#  [2 5]
#  [3 6]]
# Two arrays became 2 columns


```


----------

### 4. Understanding `axis`. This is the essential part.

----------

### Rule

`axis` = where the **new** dimension is inserted

----------

### Example: `axis = 0`

```python

# When using:
np.stack((a, b), axis=0)

# Result:
#  [[1 2 3]  
 # [4 5 6]]

# Shape: (2, 3)
# New axis added at position 0 → arrays become rows


```

----------

## Example: `axis = 1`

```python

np.stack((a, b), axis=1)

# Result:

#  [[1 4]  
#   [2 5]  
#   [3 6]]

# Shape: 
(3, 2)
# Now arrays become columns

```
----------

### Visual Intuition

### `axis = 0 → stack vertically`

a → [1 2 3]  
b → [4 5 6]  
  
Result:  
  
[ [1 2 3]  
 [4 5 6] ]

----------

### `axis = 1 → stack sideways`

Result:  
  
[ [1 4]  
 [2 5]  
 [3 6] ]

----------

## Script which implements the stacking of 2 subjects of 2 students in 2 classes

```python

# SCRIPT: Understanding np.stack() with Axis

import numpy as np

#<-----------------ONE---------------->
# STEP 1: Create two classes with marks in 2 subjects (Math, Science)
# Each class has 2 students and 2 subjects, so the shape is (2, 2)
#           Math     Science
# Student 1: 80,     85
# Student 2: 70,     75
#
class_a = np.array([[80, 85],
                    [70, 75]])   # 2 students × 2 subjects
#
class_b = np.array([[95, 90],
                    [60, 65]])
#
print("Shape of one class:", class_a.shape)  # (2,2)

#<-----------------TWO---------------->
# STEP 2: Stack along axis = 0
# Stacking along axis 0 creates a new "depth" dimension at the front
school_axis0 = np.stack((class_a, class_b), axis=0)  # Shape: (2, 2, 2) -> [Class, Student, Subject]
print("\nStack Axis 0 Shape:", school_axis0.shape)  # Result: (2, 2, 2)
# 
print("\nAxis 0 (Class First)")  # Interpretation: [Class, Student, Subject]
print(school_axis0)  # Output:
# [[[80 85]
#   [70 75]]
#  [[95 90]
#   [60 65]]]
#
print("Shape:", school_axis0.shape)  # Output: (2, 2, 2)
#
print("Class A:\n", school_axis0[0])  
# Output: Class A:
# [[80 85]
#  [70 75]]
print("Class B:\n", school_axis0[1])
# Output: Class B:
# [[95 90]
#  [60 65]]


# <-----------------THREE---------------->
# STEP 3: Stack along axis = 1
# Stacking along axis 1 creates a new "depth" dimension in the middle
school_axis1 = np.stack((class_a, class_b), axis=1)  # Shape: (2, 2, 2) -> [Student, Class, Subject]
#
print("\nAxis 1 (Student First)")  # Interpretation: [Student, Class, Subject]
print(school_axis1)  # Output:
# [[[80 85] [95 90]]
#  [[70 75] [60 65]]]
#
print("Shape:", school_axis1.shape)  # Output: (2, 2, 2)
#
print("Student 0 from both classes:\n", school_axis1[0])
# Output: Student 0 from both classes:
# [[80 85]
#  [95 90]]
print("Student 1 from both classes:\n", school_axis1[1])
# Output: Student 1 from both classes:
# [[70 75]
#  [60 65]]


# <-----------------FOUR---------------->
# STEP 4: Stack along last axis (axis=-1)
# Stacking along the last axis creates a new "depth" dimension at the end
# Shape: (2, 2, 2) -> [Student, Subject, Class]
school_last = np.stack((class_a, class_b), axis=-1)  
#
print("\nAxis -1 (Subject comparison)")  # Interpretation: [Student, Subject, Class]
print(school_last)  # Output:
# [[[80 95]
#   [85 90]]
#  [[70 60]
#   [75 65]]]
#
print("Shape:", school_last.shape)  # Output: (2, 2, 2)
#
print("Student 0, Subject 0 comparison:\n", school_last[0,0])
# Output: Student 0, Subject 0 comparison:
# [80 95]
print("Student 0, Subject 1 comparison:\n", school_last[0,1])
# Output: Student 0, Subject 1 comparison:
# [85 90]
print("Student 1, Subject 0 comparison:\n", school_last[1,0])
# Output: Student 1, Subject 0 comparison:
# [70 60]
print("Student 1, Subject 1 comparison:\n", school_last[1,1])
# Output: Student 1, Subject 1 comparison:
# [75 65]


```


## Flowchart
#### The following flowchart visualizes the above script and shows the 3 possible ways in which np.stack() was used

![Diagram](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch11-np-stack.png)




### 5. Do Arrays Need Same Shape?

### YES — They must have the same shape

----------

### Why?

Because `np.stack()` does **not stretch or broadcast** arrays.

It simply places them along a new axis.

Think: You are placing identical-sized blocks on top of each other

----------

### Example (Error)

```python
a  =  np.array([1,2,3])  
b  =  np.array([4,5])  
  
np.stack((a,b))  # Error

# Error: ValueError: all input arrays must have the same shape

```

----------

### Reason for error

a → length 3  
b → length 2  

Cannot align element-by-element











