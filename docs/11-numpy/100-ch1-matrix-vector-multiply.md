


# Project: Matrix–Vector Multiplication as Transformations


## Objective

To explore how matrix–vector multiplication:

-   transforms vectors
-   performs scaling, reflection, rotation
-   is used in data science and ML

----------

## PART A — RESEARCH QUESTIONS

### Conceptual

1.  What is a vector in NumPy?
2.  What happens when a matrix multiplies a vector?
3.  Why is matrix multiplication called a “transformation”?
4.  What is a diagonal matrix and how does it affect a vector?
5.  How do matrices represent:
    -   scaling
    -   reflection
    -   rotation

## Part B — Task

Write a script that:

1.  Defines a vector
2.  Applies:
    -   scaling
    -   non-uniform scaling
    -   reflection
    -   rotation
3.  Prints results clearly
4.  Explains transformation

----------

### HINTS

-   Use `@` operator
-   Use small vectors (2D)
-   Compare input vs output

----------

## Solution (Explanation)


## What is happening when we multiply?
Suppose we have 2D Matrix **M** of dimensions say **m x n**.
and we have vector **x** of dimension **n x 1**.
Note; 
-    Multiplication between **M** and **x** is only possible if the number of columns in **M** is equal to number of rows in **x**. 
-   Also note that when we do $$y=Mx$$ , then y will have dimensions m x 1.
- So multiplying a matrix of dimensions **m x n** to a vector of dimensions **n x 1** will result in a new vector y of dimensions **m x 1**.
- Note that matrix to vector multiplication will not only change the individual contents in each position but also change the dimensions of a vector.
- So, each matrix: (1) changes the vector (2) produces a new vector
- This change of a vector by a matrix is called **Transformation**.

----------

## Types of Transformations

Having understood what a transformation is , we can consider the **various types of transformations** which can be done to a vector by a matrix

  

| Type | Matrix Form | Effect |
| --- | --- | --- |
| Scaling | Diagonal | Stretch/shrink |
| Reflection | Special matrices | Flip direction |
| Rotation | Trigonometric | Rotate vector |

Consider the common transformations which can be done by a 2 x 2 matrix.
They are shown in the table below:-

  

| Operation | Matrix | Effect |
| --- | --- | --- |
| Uniform scaling | `[[k,0],[0,k]]` | Stretch equally |
| Non-uniform | `[[a,0],[0,b]]` | Stretch differently |
| Reflection X | `[[1,0],[0,-1]]` | Flip vertically |
| Reflection Y | `[[-1,0],[0,1]]` | Flip horizontally |
| Rotation | `[[cosθ,-sinθ],[sinθ,cosθ]]` | Rotate |



## Script

The following script shows all the above mentioned transformations on a 2D Matrix


```python

# Matrix-Vector Transformations in NumPy

import numpy as np

# <----------One ------------->
# Step 1: Define vector
x = np.array([1, 2])
print("Original vector:", x)  # Output: [1 2]

# <----------Two ------------->
# Step 2: Uniform scaling. 
# The matrix M1 is a diagonal matrix with the scaling factor (3) on the diagonal, 
# which means it will scale the x and y components of the vector by 3 when we perform the matrix multiplication.
M1 = np.array([[3, 0],
                [0, 3]])

y1 = M1 @ x
print("\nUniform scaling (×3):", y1) # [3, 6]

# <----------Three ------------->
# Step 3: Non-uniform scaling. 
# The matrix M2 is a diagonal matrix with different scaling factors on the diagonal, 
# which means it will scale the x component by 3 and the y component by 5 when we perform the matrix multiplication.
M2 = np.array([[3, 0],
                [0, 5]])

y2 = M2 @ x
print("\nNon-uniform scaling:", y2) # [3, 10]

# <----------Four ------------->
# Step 4: Reflection about X-axis. 
# The matrix M3 will invert the y component of the vector, effectively reflecting it across the X-axis.
M3 = np.array([[1, 0],
                [0, -1]])

y3 = M3 @ x
print("\nReflection about X-axis:", y3) # [1, -2]

# <----------Five ------------->
# Step 5: Reflection about Y-axis
# The matrix M4 will invert the x component of the vector, effectively reflecting it across the Y-axis.
M4 = np.array([[-1, 0],
                [0, 1]])

y4 = M4 @ x
print("\nReflection about Y-axis:", y4) # [-1, 2]

# <----------Six ------------->
# Step 6: Rotation (90 degrees). 
# The matrix M5 will rotate the vector by 90 degrees counterclockwise.

theta = np.pi / 2

M5 = np.array([[np.cos(theta), -np.sin(theta)],
                [np.sin(theta),  np.cos(theta)]])

y5 = M5 @ x
print("\nRotation (90°):", y5) # approx [-2, 1]


# Interpretation:
# Each matrix changes the vector
# → This is called transformation

```

## The following Figures show the transformation of a 2D vector by a 2 x 2 matrix



### Uniform scaling. 

![Unifrom Scaling](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch11-uniform-scaling-matrix-vector.png)

### Non-Uniform scaling

![Non-Uniform scaling](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch11-non-uniform-scaling-matrix-vector.png)

### Reflection on X-axis

![Reflection on X axis[(https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch11-reflection-x-axis-matrix-vector.png)

### Reflection on Y-axis

![Reflection on Y-axis](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch11-reflection-y-axis-matrix-vector.png)


### Rotation by 90 degrees

![Rotation by 90 degrees](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch11-rotation-90-matrix-vector.png)
















