



# Research Project

## Project Title: Row Vectors vs Column Vectors in NumPy and Linear Algebra: Concepts, Comparisons, and Transformations



## Research/ Project Question

Study the concept of **row vectors and column vectors** in NumPy and linear algebra.  
Explain their structure, differences, and practical use cases in data science, machine learning, and mathematical transformations.

Your study should include:

1.  Definition and structure of row vectors and column vectors.
2.  Comparison between:
    -   Python lists
    -   NumPy 1D arrays
    -   Row vectors
    -   Column vectors
3.  Explanation of why many mathematical transformations use **column vectors**.
4.  Demonstration of matrix multiplication involving:
    -   Matrix × Column vector
5.  Implementation of geometric transformations such as:
    -   Rotation of a point in a 2D system
    -   Scaling transformation
6.  Use NumPy scripts to demonstrate the concepts.
7.  Include tables, diagrams, and explanations.

Finally, conclude when it is preferable to use row vectors and when column vectors are more appropriate.

----------

# Answer 


## 1. Introduction

Vectors are fundamental objects in mathematics, data science, and machine learning. In NumPy, vectors can be represented in different forms depending on how the data is structured.

The two main forms are:

-   Row vector
-   Column vector

Although both store the same values, their **orientation affects mathematical operations**, especially matrix multiplication and transformations.

----------

## 2. Row Vector

A row vector is a horizontal arrangement of values.

Example:

`[ 3  5  7 ]`

Shape in NumPy:

`(1, 3)`

Example code:

```python

# This code demonstrates how to create a row vector using NumPy and reshape it to have a specific shape.
# A row vector is a 1D array that has only one row and multiple columns.
# NumPy library is used for creating and manipulating arrays in Python. 
# The reshape method is used to change the shape of the array without changing its data. 
# In this case, we are reshaping a 1D array into a 2D array with 1 row and 3 columns.

import numpy as np  

# Create a row vector (1D array) with values 3, 5, and 7, and reshape it to have 1 row and 3 columns.
# The reshape(1, 3) method is used to change the shape of the array to a 2D array with 1 row and 3 columns.
row_vector = np.array([3,5,7]).reshape(1,3)  

print(row_vector)  # Output: [[3 5 7]]
print("Shape:", row_vector.shape)  # Output: (1, 3) - This indicates that the array has 1 row and 3 columns.


```


## 3. Column Vector

A column vector is a vertical arrangement of values.

Example:

```python
[3  
 5  
 7]
```
Shape:

`(3,1)`

Example:


```python

# This code demonstrates how to create a column vector using NumPy and check its shape.
# A column vector is a 2D array that has multiple rows and only one column.
# NumPy library is used for creating and manipulating arrays in Python. 
# The reshape method is used to change the shape of the array without changing its data.

import numpy as np

# Create a column vector (2D array) with values 3, 5, and 7, and 
# reshape it to have 3 rows and 1 column.
column_vector = np.array([3,5,7]).reshape(3,1)

print(column_vector) # Output: [[3]
#                    #          [5]
#                    #          [7]]
                    
print("Shape:", column_vector.shape)  
# Output: (3, 1) - This indicates that the array has 3 rows and 1 column.

```

**Interpretation: Three values stacked vertically.**


## Comparison Table (Row Vector | Column Vector) 

  

| Feature | Row Vector | Column Vector |
| --- | --- | --- |
| Shape | (1,n) | (n,1) |
| Orientation | Horizontal | Vertical |
| Common use | Represent one data record | Used in matrix transformations |
| Machine learning | Prediction input | Model computations |
| Linear algebra | Less common | Standard representation |



## 5. Comparison with Python Lists


  

| Feature | Python List | NumPy Row Vector | NumPy Column Vector |
| --- | --- | --- | --- |
| Structure | Flexible | Structured | Structured |
| Shape | Not defined | Defined | Defined |
| Matrix math | Not supported | Supported | Supported |
| Performance | Slower | Fast | Fast |



## 6. Why Column Vectors Are Used in Transformations

In linear algebra, transformations such as:

rotation
scaling
projection
translation

are defined using:

`Matrix × Column Vector`

Mathematically:

`y = Mx`

Where

`M = transformation matrix`

`x = column vector`


## 7. Example: Rotation by 90 Degrees

Suppose we have a point: `(2,1)`

We represent it as a column vector.

Rotation matrix for 90°:

```python

[ 0  -1 ]
[ 1   0 ]
```

## 8 Script for rotation bt 90 Degrees

```python

# Rotation Transformation Example

import numpy as np

# 1. Create Original point
# We create a column vector (2D array) for the point (2, 1) and 
# reshape it to have 2 rows and 1 column.
point = np.array([2,1]).reshape(2,1)  # Original point as a column vector (2D array)

print("Original Point:")
print(point)

# 2. Create Rotation matrix (90 degrees)
# We create a 2x2 rotation matrix for a 90-degree rotation.
# The rotation matrix for a 90-degree counterclockwise rotation in 2D is:
# [ 0 -1]
# [ 1  0]
# because it transforms the point (x, y) to (-y, x), which corresponds 
# to a 90-degree rotation.
rotation_matrix = np.array([
    [0, -1],
    [1,  0]
])

print("\nRotation Matrix:")
print(rotation_matrix)

# 3. Perform Transformation
# M x P = New Point rotated by 90 degrees
# [ 0 -1][2]   = [ 0*2 + (-1)*1] = [-1]
# [ 1  0][1]   = [ 1*2 +  0*1] = [ 2]

rotated_point = rotation_matrix @ point  # The @ operator is used for matrix multiplication in Python. It multiplies the rotation matrix by the point vector to get the new coordinates of the point after rotation.

print("\nRotated Point:") 
print(rotated_point)
# Output: [[-1]
#          [ 2]]

```

### The following figure shows how the vector gets rotated

![2D diagram](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch11-final-vector-rotation.png)


## 9. Example: Scaling Transformation

Scaling increases or decreases size.

## Example: Scaling Transformation

Scaling increases or decreases size.

Scaling matrix:

In general  if:-

-    $$s_x = scaling  factor$$  on  X-axis 


-    $$s_y = scaling factor$$ on Y-axis 

The scaling matrix is a **diagonal matrix**


$$
S = \begin{bmatrix} s_x & 0 \\\\ 0 & s_y \end{bmatrix}
$$



```python
[2 0]  
[0 3]
```
This means:

x scaled by 2  
y scaled by 3

Example script:


Scaling matrix:

```python
[2 0]  
[0 3]
```
This means:

x scaled by 2  
y scaled by 3

## Example script:

```python

import numpy as np
# Scaling Transformation

# 1. Create Original point
point = np.array([3,4]).reshape(2,1)

# 2. Create Scaling matrix
scaling_matrix = np.array([
    [2,0],
    [0,3]
])

# 3. Perform Transformation
scaled_point = scaling_matrix @ point  # The @ operator is used for matrix multiplication in Python. It multiplies the scaling matrix by the point vector to get the new coordinates of the point after scaling.

print("Scaled Point:")
print(scaled_point)  # Output: [[ 6]
#                    #          [12]]


```


## Figure showing scaling in 2D

![Figure showing scaling](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch11-scaling-matrix.png)





















