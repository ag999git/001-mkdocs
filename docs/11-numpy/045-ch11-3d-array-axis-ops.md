


# Project: Understanding 3D Arrays and Axis Operations in NumPy

----------

## Objective

To understand:

-   Structure of 3D arrays
-   Meaning of axes (0, 1, 2)
-   How `sum(axis=...)` works
-   How multi-dimensional data is reduced

----------

## PART A — CONCEPTUAL STUDY

## Study Questions

1.  What is the shape of a 3D array?
2.  What do the three indices represent?
3.  What does each axis correspond to?
4.  What does it mean to “collapse an axis”?

----------

# Visualizing a 3D Array

Given a 3D array:
```
arr  =  np.array([  
 [[1,2],[3,4]],  
 [[5,6],[7,8]]  
])
```
### Its Shape = (2, 2, 2)

----------

## There are various ways in which it can be represented/ visualized
 ### Representation 1: Visualizing it as 2 layers
```
Layer 0:  
[[1 2]  
 [3 4]]  
  
Layer 1:  
[[5 6]  
 [7 8]]
```
----------

### Representation 2: Indexed View
**Here we view each item by its index of form `arr[i, j, k]`**
```
arr[0,0,0] = 1   arr[0,0,1] = 2  
arr[0,1,0] = 3   arr[0,1,1] = 4  
  
arr[1,0,0] = 5   arr[1,0,1] = 6  
arr[1,1,0] = 7   arr[1,1,1] = 8
```
----------

### Representation 3: Coordinates

***Here we view each item in the array as `(i, j, k) → value`** 
  ```
(0,0,0) → 1  
(1,1,1) → 8
```
----------

## Part B: Task

Write a script that:

1.  Creates the 3D array
2.  Displays it in multiple forms
3.  Computes:
    -   `sum(axis=0)`
    -   `sum(axis=1)`
    -   `sum(axis=2)`
4.  Explains each result

----------

### HINTS

-   Use loops to print layers
-   Print shapes after each operation
-   Compare results carefully

----------

## Script


```python

# 3D Array Axis Exploration

import numpy as np

# Step 1: Create array. Visualize as 2 layers of 2x2 matrices.
arr = np.array([
    [   # Layer 0
        [1, 2],
        [3, 4]
    ],
    [   # Layer 1
        [5, 6],
        [7, 8]
    ]
])

print("Array shape:", arr.shape)  # (2, 2, 2) → 2 layers, each with 2 rows and 2 columns
print("Array:->\n", arr)
# Output:
# Array:->
# [[[1 2]
#   [3 4]]
#
#  [[5 6]
#   [7 8]]]

# Step 2: Visualize layers. Each layer is a 2x2 matrix. We can access them using arr[0] and arr[1].
for i in range(arr.shape[0]):
    print(f"\nLayer-> {i}:\n", arr[i])

# Output:
# Layer-> 0:
# [[1 2]
#  [3 4]]
# Layer-> 1:
# [[5 6]
#  [7 8]]

# Step 3: axis = 0 (across layers). For each position (i,j), sum across layers:
sum0 = arr.sum(axis=0)
print("\nSum axis=0:\n", sum0)
# Output:
# [[ 6  8]
#  [10 12]]
# Explanation:
# axis=0 → combine layers. For each position (i,j), sum across layers:
# sum0[0,0] = arr[0,0,0] + arr[1,0,0] = 1 + 5 = 6
# sum0[0,1] = arr[0,0,1] + arr[1,0,1] = 2 + 6 = 8
# sum0[1,0] = arr[0,1,0] + arr[1,1,0] = 3 + 7 = 10
# sum0[1,1] = arr[0,1,1] + arr[1,1,1] = 4 + 8 = 12  

# Step 4: axis = 1 (across rows). For each layer and column, sum across rows:
# For layer 0, column 0: sum1[0,0] = arr[0,0,0] + arr[0,1,0] = 1 + 3 = 4
# For layer 0, column 1: sum1[0,1] = arr[0,0,1] + arr[0,1,1] = 2 + 4 = 6
# For layer 1, column 0: sum1[1,0] = arr[1,0,0] + arr[1,1,0] = 5 + 7 = 12
# For layer 1, column 1: sum1[1,1] = arr[1,0,1] + arr[1,1,1] = 6 + 8 = 14
sum1 = arr.sum(axis=1)
print("\nSum axis=1:\n", sum1)
# Output:
# [[ 4  6]
#  [12 14]]


# Step 5: axis = 2 (across columns). For each layer and row, sum across columns:
# For layer 0, row 0: sum2[0,0] = arr[0,0,0] + arr[0,0,1] = 1 + 2 = 3
# For layer 0, row 1: sum2[0,1] = arr[0,1,0] + arr[0,1,1] = 3 + 4 = 7
# For layer 1, row 0: sum2[1,0] = arr[1,0,0] + arr[1,0,1] = 5 + 6 = 11
# For layer 1, row 1: sum2[1,1] = arr[1,1,0] + arr[1,1,1] = 7 + 8 = 15
sum2 = arr.sum(axis=2)
print("\nSum axis=2:\n", sum2)
# Output:
# [[ 3  7]
#  [11 15]]

# Overall Conclusion:
# axis=0 → combine layers
# axis=1 → combine rows
# axis=2 → combine columns


```














