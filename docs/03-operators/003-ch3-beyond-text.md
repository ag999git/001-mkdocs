


#### 1\. Matrix Multiplication Operator (@) 
Operator (@) was introduced in Python 3.5 and later. It is useful for matrix and vector multiplications especially in NumPy. Study Matrix Multiplication Operator (`@`)

The following script explains how Matrix Multiplication Operator (`@`) works

```python

# Note: The @ operator is only available in Python 3.5 and later versions.
# For matrix operations, it's often more efficient to use NumPy arrays instead of nested lists.
# In this example, we used NumPy to create matrices and perform multiplication, which is optimized for performance.
# The @ operator is a convenient way to express matrix multiplication in a clear and concise manner.
# Always ensure that the dimensions of the matrices or vectors are compatible for multiplication when using the @ operator.
# For matrix multiplication, the number of columns in the first matrix must equal the number of rows in the second matrix.
# For matrix-vector multiplication, the number of columns in the matrix must equal the number of elements in the vector.    


# This script demonstrates the use of the @ operator for matrix multiplication
# in Python. The @ operator is used to perform matrix multiplication between two    
# matrices (2D lists) or between a matrix and a vector (1D list).
# ============================================================= 
import numpy as np
# Example 1: Matrix-Matrix Multiplication
A = np.array([[1, 2], [3, 4]])  
B = np.array([[5, 6], [7, 8]])
C = A @ B  # Matrix multiplication of A and B   
print("Matrix A:\n", A)
print("Matrix B:\n", B)     
print("Result of A @ B:\n", C)  # Should output the product of A and B  
# Example 2: Matrix-Vector Multiplication
M = np.array([[1, 2], [3, 4]]) 
v = np.array([5, 6])
result = M @ v  # Matrix multiplication of M and v 
print("Matrix M:\n", M)
print("Vector v:\n", v) 
print("Result of M @ v:\n", result)  # Should output the product of M and v

```

#### 2. There are also set operators in Python. Python supports the following set operators:- (1) |   union (2) &   intersection (3) -   difference (4) ^   symmetric difference. Study these set operators in Python

```python

"""
Set Operators
Sets support:

|   union
&   intersection
-   difference
^   symmetric difference

"""

# Example 1: Union
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a | set_b
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5}

# Example 2: Intersection
intersection_set = set_a & set_b
print("Intersection:", intersection_set)  # Output: {3}

# Example 3: Difference
difference_set = set_a - set_b  
print("Difference (A - B):", difference_set)  # Output: {1, 2}

# Example 4: Symmetric Difference   
symmetric_diff_set = set_a ^ set_b
print("Symmetric Difference:", symmetric_diff_set)  # Output: {1, 2, 4, 5}


```








