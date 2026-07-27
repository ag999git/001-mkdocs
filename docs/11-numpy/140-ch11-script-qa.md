



## 40 script-based exercises 
________________________________________


1. Create a 1D NumPy array containing the numbers from 10 to 49. Then, reverse this array using slicing.

```python
import numpy as np

# Create the array using arange
arr = np.arange(10, 50)

# Reverse the array using the [start:stop:step] slicing syntax with step -1
reversed_arr = arr[::-1]

print("Original:", arr)
print("Reversed:", reversed_arr)

```
2. Create a 3x3 matrix with values ranging from 0 to 8 using `np.reshape`.

```python
import numpy as np

# Create 9 elements and reshape into a 3x3 grid
# Requirement: total elements must match the product of dimensions (3*3=9)
matrix = np.arange(9).reshape(3, 3)

print(matrix)

```
3. Initialize a `5x5` identity matrix and change all the diagonal elements to 5.

```python
import numpy as np

# np.eye creates a square matrix with 1s on the diagonal
identity = np.eye(5)

# Multiply the entire matrix by 5 (Broadcasting a scalar)
# Since only the diagonal has 1s, only they become 5
five_diag = identity * 5

print(five_diag)

```
4. Generate a `10x10` array with random values. Find the minimum and maximum values and their memory addresses.

```python
import numpy as np

# Create random floats in [0, 1)
data = np.random.rand(10, 10)

# Use built-in aggregate functions
min_val = data.min()
max_val = data.max()

print(f"Min: {min_val}, Max: {max_val}")
# The data pointer shows the memory start location
print(f"Memory Address: {data.ctypes.data}")

```
5. Create a `2D` array with 1 on the border and 0 inside.

```python
import numpy as np

# Initialize with ones
x = np.ones((5, 5))

# Use slicing to target the 'interior' (everything except first/last row and col)
# Assign 0 to that sub-view
x[1:-1, 1:-1] = 0

print(x)

```
6. Create an `8x8` matrix and fill it with a checkerboard pattern (0s and 1s) using slicing.

```python
import numpy as np

check = np.zeros((8, 8), dtype=int)

# Every second row starting from index 1, every second column starting from index 0
check[1::2, ::2] = 1

# Every second row starting from index 0, every second column starting from index 1
check[::2, 1::2] = 1

print(check)

```
7. Convert an array of weights `[70.5, 80.2, 65.0]` from kilograms to pounds (1kg = 2.2lb) using vectorization.

```python
import numpy as np

weights_kg = np.array([70.5, 80.2, 65.0])

# Vectorization allows us to multiply the whole array by a scalar without a for-loop
weights_lb = weights_kg * 2.2

print(f"Weights in lbs: {weights_lb}")

```
8. Demonstrate the "View vs Copy" behavior by slicing an array and modifying the slice. Verify the original array.

```python
import numpy as np

original = np.array([1, 2, 3, 4, 5])

# Slicing creates a 'view' (shared memory)
slice_view = original[0:3]
slice_view[0] = 99

print("Modified Original:", original) # Should show 99 at index 0

# To keep original safe, use .copy()
safe_copy = original[0:3].copy()
safe_copy[1] = 88

print("Original after modifying copy:", original) # Should NOT show 88

```
9. Given a `4x4` matrix, extract the inner `2x2` sub-matrix.

```python
import numpy as np

matrix = np.arange(16).reshape(4, 4)

# Slicing rows 1 to 2 (index 1:3) and columns 1 to 2 (index 1:3)
inner = matrix[1:3, 1:3]

print("Full Matrix:\n", matrix)
print("Inner Sub-matrix:\n", inner)

```
10. Normalize a random `5x5` matrix so that all values lie between 0 and 1.

```python
import numpy as np

rand_arr = np.random.rand(5, 5) * 100

# Normalization formula: (x - min) / (max - min)
normalized = (rand_arr - rand_arr.min()) / (rand_arr.max() - rand_arr.min())

print(normalized)

```
11. Create a script to find the common values between two NumPy arrays.

```python
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([3, 4, 5, 6, 7])

# np.intersect1d finds unique common elements
common = np.intersect1d(arr1, arr2)

print("Common elements:", common)

```
12. Generate 50 evenly spaced numbers between 0 and $2π$ and calculate their sine values.

```python
import numpy as np

# linspace is preferred when the number of points is fixed
x = np.linspace(0, 2 * np.pi, 50)

# np.sin is a universal function (ufunc) that works element-wise
y = np.sin(x)

print(y)

```
13. Create a `5x5` matrix and find the sum of each column.

```python
import numpy as np

matrix = np.arange(25).reshape(5, 5)

# Axis 0 refers to the row-wise collapse (summing vertically down columns)
column_sums = matrix.sum(axis=0)

print("Matrix:\n", matrix)
print("Sums of columns:", column_sums)

```
14. Replace all values in a 1D array that are greater than 50 with the value 0 using Boolean Masking.

```python
import numpy as np

arr = np.array([10, 60, 20, 80, 30])

# Step 1: Create the boolean mask
mask = arr > 50

# Step 2: Use mask to index and reassign
arr[mask] = 0

print(arr) # [10, 0, 20, 0, 30]

```
15. Use `np.where` to create an array that marks numbers as "Even" or "Odd" based on an input array.

```python
import numpy as np

numbers = np.array([1, 2, 3, 4, 5, 6])

# np.where(condition, value_if_true, value_if_false)
labels = np.where(numbers % 2 == 0, "Even", "Odd")

print(labels)

```
16. Stack two 2D arrays vertically and then horizontally.

```python
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# vstack adds rows
v = np.vstack((a, b))

# hstack adds columns
h = np.hstack((a, b))

print("Vertical:\n", v)
print("Horizontal:\n", h)

```
17. Calculate the Dot Product of two `3x3` matrices.

```python
import numpy as np

A = np.ones((3, 3)) * 2
B = np.eye(3)

# Use np.dot or the @ operator
dot_product = np.dot(A, B)

print(dot_product)

```
18. Create a `3x3x3` tensor and extract the second "page" (slice along Axis 0).

```python
import numpy as np

tensor = np.arange(27).reshape(3, 3, 3)

# Indexing the first dimension (Axis 0)
second_page = tensor[1, :, :]

print("Full Tensor:\n", tensor)
print("Second Page:\n", second_page)

```
19. Given a 1D array of 12 elements, reshape it into a 3D array of shape `(2, 2, 3)`.

```python
import numpy as np

data = np.arange(12)

# Ensure product 2*2*3 = 12
reshaped = data.reshape(2, 2, 3)

print(reshaped)

```
20. Find the indices of non-zero elements in the array `[1, 2, 0, 0, 4, 0]`.

```python
import numpy as np

arr = np.array([1, 2, 0, 0, 4, 0])

# np.nonzero returns a tuple of arrays (one for each dimension)
indices = np.nonzero(arr)

print(indices)

```
21. Generate a `5x5` identity matrix and add a scalar 10 to it using broadcasting.

```python
import numpy as np

eye_mat = np.eye(5)

# 10 is broadcasted to every element of the 5x5 matrix
result = eye_mat + 10

print(result)

```
22. Multiply a `3x3` matrix by a 1D row vector of length 3 using broadcasting.

```python
import numpy as np

matrix = np.ones((3, 3))
vector = np.array([1, 2, 3])

# Vector is stretched vertically to match the 3 rows of the matrix
result = matrix * vector

print(result)

```
23. Calculate the mean, median, and standard deviation of a dataset of 100 random numbers.

```python
import numpy as np

data = np.random.randn(100)

# Statistical aggregations
mean_val = np.mean(data)
median_val = np.median(data)
std_dev = np.std(data)

print(f"Mean: {mean_val}, Median: {median_val}, Std: {std_dev}")

```
24. Solve the system of linear equations: $3x + y = 9$ and $x + 2y = 8$ using `np.linalg.solve`.

```python
import numpy as np

# Coefficients matrix A
A = np.array([[3, 1], [1, 2]])

# Ordinate/Constants vector B
B = np.array([9, 8])

# Solve for [x, y]
solutions = np.linalg.solve(A, B)

print(f"x = {solutions[0]}, y = {solutions[1]}")

```
25. Compute the Eigenvalues and Eigenvectors of a `2x2` square matrix.

```python
import numpy as np

mat = np.array([[1, 2], [2, 1]])

# linalg.eig returns two values: eigenvalues and the eigenvector matrix
eigenvalues, eigenvectors = np.linalg.eig(mat)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

```
26. Perform a Singular Value Decomposition (SVD) on a `3x2` matrix.

```python
import numpy as np

A = np.array([[1, 2], [3, 4], [5, 6]])

# svd returns U, Sigma (as 1D), and VT (Transpose of V)
U, S, VT = np.linalg.svd(A)

print("U:\n", U)
print("Singular Values (Sigma):", S)
print("V Transpose:\n", VT)

```
27. Create a coordinate grid for the range $x=-1$ to $1$ and $y=-1$ to $1$ using `np.meshgrid`.

```python
import numpy as np

x = np.linspace(-1, 1, 5)
y = np.linspace(-1, 1, 5)

# Meshgrid creates two 2D arrays representing all (x,y) pairs
X, Y = np.meshgrid(x, y)

print("X Grid:\n", X)
print("Y Grid:\n", Y)

```
28. Flatten a 2D matrix into a 1D array using two different methods and explain the difference.

```python
import numpy as np

mat = np.array([[1, 2], [3, 4]])

# .flatten() always returns a copy (safe)
flat_copy = mat.flatten()

# .ravel() returns a view if possible (memory efficient)
flat_view = mat.ravel()

print(flat_copy)

```
29. Calculate the Frobenius Norm of a `3x3` matrix.

```python
import numpy as np

A = np.arange(9).reshape(3, 3)

# ord='fro' specifies the Frobenius norm (sqrt of sum of squares)
norm = np.linalg.norm(A, ord='fro')

print("Frobenius Norm:", norm)

```
30. Create a script to compare the time taken to sum 1 million numbers using a 
python list vs. a NumPy array.

```python
import numpy as np
import time

size = 1000000
py_list = list(range(size))
np_arr = np.arange(size)

# Time python list
start = time.time()
sum(py_list)
print(f"Python list time: {time.time() - start}")

# Time NumPy array
start = time.time()
np_arr.sum() # Vectorized sum
print(f"NumPy time: {time.time() - start}")

```


## Advanced / Best Practices Exercises

31. Use `np.newaxis` to convert a `1D` array into a column vector.


```python
import numpy as np

arr = np.array([1, 2, 3])

# Increases dimension by adding a new axis at the specified position
col_vector = arr[:, np.newaxis]

print("Shape:", col_vector.shape) # (3, 1)
print(col_vector)

```



32. Use `np.genfromtxt` to load a CSV file (simulated here) while handling missing values.

```python
import numpy as np
import io

# Simulated CSV data with a missing value
csv_data = u"1, 2, 3\n4, , 6"
s = io.StringIO(csv_data)

# filling_values replaces empty spots with a default
data = np.genfromtxt(s, delimiter=",", filling_values=0)

print(data)
```
33. Implement a simple "Rolling Average" using `np.convolve`.

```python
import numpy as np

data = np.array([1, 2, 3, 4, 5, 6, 7, 8])
window_size = 3

# Create a uniform weight window
weights = np.ones(window_size) / window_size

# valid mode ensures the window fits completely within the data
rolling_avg = np.convolve(data, weights, mode='valid')

print(rolling_avg)

```
34. Use Structured Arrays to store a table with different data types (`Name, Age, Grade`).

```python
import numpy as np

# Define the structure: 'U10' for string, 'i4' for int, 'f4' for float
dt = np.dtype([('name', 'U10'), ('age', 'i4'), ('grade', 'f4')])

# Create array with the defined dtype
students = np.array([('Alice', 21, 88.5), ('Bob', 22, 92.0)], dtype=dt)

print(students['name']) # Access specific field

```
35. Use `np.clip` to limit the values in an array between a minimum of 10 and a maximum of 50.

```python
import numpy as np

data = np.array([5, 15, 45, 100, 25])

# Values < 10 become 10, values > 50 become 50
clipped = np.clip(data, 10, 50)

print(clipped)

```
36. Demonstrate Memory Mapping with `np.memmap` for processing files too large for RAM.

```python
import numpy as np

# Create a large file on disk (simulated)
# mode='w+' creates/overwrites file
filename = "large_data.dat"
fp = np.memmap(filename, dtype='float32', mode='w+', shape=(1000, 1000))

# Operations happen on disk, not fully loaded into RAM
fp[:] = np.random.rand(1000, 1000)
fp.flush() # Ensure data is written to disk

print("Data mapped to disk successfully.")

```
37. Find the unique elements and their counts in an array.

```python
import numpy as np

data = np.array([1, 2, 2, 3, 3, 3, 4])

# return_counts=True gives the frequency of each item
values, counts = np.unique(data, return_counts=True)

print(dict(zip(values, counts)))

```
38. Tile an array to repeat a pattern.

```python
import numpy as np

pattern = np.array([1, 2, 3])

# Repeat the pattern 3 times horizontally
tiled = np.tile(pattern, 3)

print(tiled) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

```
39. Use `np.allclose` to check if two arrays are mathematically equal within a small tolerance.

```python
import numpy as np

a = np.array([0.1 + 0.2])
b = np.array([0.3])

# Floating point precision often makes '==' fail
print("Equality:", a == b) 

# allclose is the best practice for comparing floats
print("Close enough:", np.allclose(a, b))

```
40. Create a custom ufunc (Universal Function) using `np.frompyfunc`.

```python
import numpy as np

def my_logic(x):
    return x**2 + 10

# Convert standard Python function to a NumPy ufunc
# 1 input, 1 output
vectorized_logic = np.frompyfunc(my_logic, 1, 1)

data = np.array([1, 2, 3])
print(vectorized_logic(data))
```

## Extra question

41. Problem: Consider the matrix

$$
M = \begin{bmatrix}
-1 & -2 & -2 \\
1 & 2 & 1 \\
-1 & -1 & 0
\end{bmatrix}
$$

and the vectors


$$
v_{1} = \begin{bmatrix}
-1 \\
1 \\
3
\end{bmatrix}
$$

and 

$$
v_{2} = \begin{bmatrix}
-1 \\
1 \\
-2
\end{bmatrix}
$$

Tasks
1. Verify that $v_1$ and $v_2$ are eigenvectors of the matrix $M$
2. Find the corresponding eigenvalues $𝜆_1$ and $𝜆_2$

Confirm your results by explicitly computing: $𝑀v = 𝜆v$.

Solution

For $$v_{1}=[-1,1,3]^{T}$$

$$
\begin{gathered}
M v_1 \\
=\left[\begin{array}{ccc}
-1 & -2 & -2 \\
1 & 2 & 1 \\
-1 & -1 & 0
\end{array}\right]\left[\begin{array}{c}
-1 \\
1 \\
3
\end{array}\right]=\left[\begin{array}{c}
-5 \\
4 \\
0
\end{array}\right]
\end{gathered}
$$



