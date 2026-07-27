





# BEGINNER LEVEL FUNCTIONS





## 1. `np.array()`

**Signature**

`np.array(object, dtype=None, copy=True, ndmin=0)`

**Parameters**

-   `object` → list, tuple, nested list
-   `dtype` → data type (optional)
-   `copy` → whether to copy data
-   `ndmin` → minimum number of dimensions

**Output**

NumPy ndarray

Example output:

`array([1, 2, 3])`

**Common Usage**

-   Convert Python lists to arrays
-   Creating matrices

**Possible Errors**

`ValueError`: setting an array element with a sequence

Occurs when nested lists have inconsistent lengths.

**Important Notes**

-   Automatically infers datatype
-   Most commonly used NumPy function

----------

## 2. `np.zeros()`

**Signature**

`np.zeros(shape, dtype=float)`

**Parameters**

-   `shape` → tuple specifying dimensions
-   `dtype` → data type

**Output**

Array filled with zeros.

**Common Usage**

-   Initialization of matrices
-   Placeholder arrays

**Possible Errors**

`TypeError`: '`int`' object is not iterable

Occurs when incorrect shape provided.

----------

## 3. `np.ones()`

**Signature**

`np.ones(shape, dtype=float)`

**Output**

Array filled with ones.

**Common Usage**

-   Machine learning weight initialization
-   Matrix operations

----------

## 4. `np.full()`

**Signature**

`np.full(shape, fill_value, dtype=None)`

**Parameters**

-   `shape`
-   `fill_value`

**Output**

Array filled with a constant value.

----------

## 5. `np.arange()`

**Signature**

`np.arange(start, stop, step, dtype=None)`

**Output**

1D array.

Example:

`array([0,2,4,6,8])`

**Common Usage**

Generating numeric sequences.

**Common Error**

Floating step sometimes produces unexpected results due to precision.

----------

## 6. `np.linspace()`

**Signature**

`np.linspace(start, stop, num=50)`

**Output**

Evenly spaced array.

**Important Note**

Includes the stop value.

----------

## 7. `np.eye()`

**Signature**

`np.eye(N, M=None, k=0)`

**Parameters**

-   N rows
-   M columns
-   k diagonal offset

**Output**

Identity matrix.

----------

## 8. `np.random.rand()`

**Signature**

`np.random.rand(d0, d1, ..., dn)`

**Output**

Random array with values between 0 and 1.

----------
## Table (Beginner Level)

| S.No | Method | Purpose | Example | Input | Output | Key Concept | When to Use | Important Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | np.array() | Convert Python data to NumPy array | np.array([1,2,3]) | List / tuple | n-D array | Basic conversion | Almost always first step | Creates a new array |
| 2 | np.zeros() | Create array of zeros | np.zeros((2,3)) | Shape | Numeric array | Initialization | Default values | dtype defaults to float |
| 3 | np.ones() | Create array of ones | np.ones((3,3)) | Shape | Numeric array | Matrix creation | ML / matrices | Efficient initialization |
| 4 | np.full() | Create constant array | np.full((2,2),7) | Shape + value | Numeric array | Constant arrays | Defaults | Flexible dtype |
| 5 | np.arange() | Create sequence with step | np.arange(0,10,2) | Start/stop/step | 1D array | Range generation | Loops / sequences | Stop excluded |
| 6 | np.linspace() | Evenly spaced values | np.linspace(0,1,5) | Start/stop/count | 1D array | Fixed number of values | Plotting | Includes endpoint |
| 7 | np.eye() | Identity matrix | np.eye(3) | Size | Square matrix | Linear algebra basics | Matrix math | Supports diagonal offset |
| 8 | np.random.rand() | Random floats | np.random.rand(2,2) | Dimensions | Numeric array | Random generation | Simulations | Uniform distribution |



## Script

```python

# NumPy Array Creation Examples
# Beginner level
import numpy as np

# 1 np.array()
# NumPy array from a Python list. All elements are of the same type (integers in this case).
a = np.array([1,2,3])  
print(a)

# Possible error:
# np.array([[1,2],[3,4,5]])  # This will raise a ValueError because the inner lists have different lengths, making it impossible to create a regular 2D array. NumPy expects all rows to have the same number of columns for a 2D array.

# 2 np.zeros()  # NumPy array filled with zeros. The argument specifies the shape of the array. 
# In this case, (2, 3) creates a 2D array with 2 rows and 3 columns, all initialized to zero.
b = np.zeros((2,3))
print(b)

# 3 np.ones()  # NumPy array filled with ones. The argument specifies the shape of the array. 
# In this case, (3, 3) creates a 2D array with 3 rows and 3 columns, all initialized to one.
c = np.ones((3,3))
print(c)

# 4 np.full()  # NumPy array filled with a constant value. The first argument specifies the shape, 
# and the second argument specifies the fill value.
d = np.full((2,2),7)
print(d)

# 5 np.arange()  # NumPy array with a range of values. 
# The arguments specify the start, stop, and step values.
e = np.arange(0,10,2)
print(e)

# 6 np.linspace()  # NumPy array with linearly spaced values. 
# The arguments specify the start, stop, and number of values.
f = np.linspace(0,1,5)
print(f)

# 7 np.eye()  # NumPy array representing an identity matrix. 
# The argument specifies the size of the matrix.
g = np.eye(3)
print(g)

# 8 np.random.rand()  # NumPy array with random values between 0 and 1. 
# The arguments specify the shape of the array.
h = np.random.rand(2,2)
print(h)




```



# INTERMEDIATE LEVEL FUNCTIONS

----------

## 9. `np.empty()`

**Signature**

`np.empty(shape, dtype=float)`

**Output**

Uninitialized array.

**Important**

Contains random memory values.

**Common Error**

Dont assume it contains zeros because it does not.

----------

## 10. `np.zeros_like()`

**Signature**

`np.zeros_like(a)`

Creates zero array matching structure.

----------

## 11. `np.ones_like()`

Same as above but fills with ones.

----------

## 12. `np.full_like()`

Copies structure with constant value.

----------

## 13. `np.identity()`

Simpler identity matrix function.

----------

## 14. `np.diag()`

Creates or extracts diagonal.

Common confusion:  
Behavior depends on input dimension.

----------

## 15. `np.logspace()`

Logarithmic scale array.

Used in scientific computing.

----------

## 16. `np.meshgrid()`

Used for coordinate grids.

Important in plotting surfaces.

----------

## 17. `np.indices()`

Creates index matrices.

Used in image processing and matrix math.

----------

## Table (Intermediate level)

  

| S. No | Method | Purpose | Example | Input | Output | Shape Rule | Key Feature | Typical Use | Important Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9 | np.empty() | Allocate array without initialization | np.empty((3,3)) | Shape | Numeric array | User-defined | Very fast allocation | Performance computing | Contains garbage values |
| 10 | np.zeros_like() | Copy shape but fill with zeros | np.zeros_like(A) | Array | Same shape array | Matches input | Template arrays | Algorithms | Keeps structure |
| 11 | np.ones_like() | Copy structure filled with ones | np.ones_like(A) | Array | Same shape | Same as source | Efficient replication | ML models | Keeps dtype |
| 12 | np.full_like() | Copy shape with constant value | np.full_like(A,9) | Array | Same shape | Based on input | Structured duplication | Matrix templates | Consistent structure |
| 13 | np.identity() | Identity matrix | np.identity(4) | Size | Square matrix | n × n | Simpler syntax | Linear algebra | Same as eye |
| 14 | np.diag() | Create or extract diagonal | np.diag([1,2,3]) | Array | Matrix/vector | Depends on input | Dual behavior | Matrix operations | Input type matters |
| 15 | np.logspace() | Logarithmic spacing | np.logspace(1,3,5) | Start/stop exp | 1D array | Fixed length | Log progression | Scientific computing | Engineering uses |
| 16 | np.meshgrid() | Create coordinate grid | np.meshgrid(x,y) | Arrays | Grid arrays | Expanded grid | Useful in plotting | 3D surfaces | Visualization |
| 17 | np.indices() | Create index grid | np.indices((3,3)) | Shape | Index arrays | Multi-dimensional | Matrix coordinates | Image processing | Advanced indexing |


## Script (For Intermediate)


```python

# NumPy Array Creation Examples
# Intermediate level
import numpy as np

# 9 np.empty()  # NumPy array that is uninitialized. The values in the array will be 
# whatever happens to already be in that memory location, which can be random and 
# unpredictable.
a = np.empty((3,3))   # contains garbage values
print("np.empty():->\n", a)

# 10 zeros_like  # NumPy array filled with zeros, having the same shape and type as a 
# given array.
b = np.zeros_like(a)
print("np.zeros_like():->\n", b)

# 11 ones_like  # NumPy array filled with ones, having the same shape and type as a 
# given array.
c = np.ones_like(a)
print("np.ones_like():->\n", c)

# 12 full_like  # NumPy array filled with a specified value, having the same shape 
# and type as a given array.
d = np.full_like(a,9)
print("np.full_like():->\n", d)

# 13 identity  # NumPy array representing an identity matrix. The argument specifies 
# the size of the matrix.
e = np.identity(4)
print("np.identity():->\n", e)

# 14 diag  # NumPy array with a diagonal. The argument specifies the values for the 
# diagonal.
f = np.diag([1,2,3])  # f will be a 3x3 array with 1, 2, and 3 on the diagonal and zeros elsewhere.
print("np.diag():->\n", f)  # np.diag() gives diagnol elements in a list. Here [1, 2, 3]

# extract diagonal. This will extract the diagonal elements from the array f and return 
# them as a 1D array. In this case, it will return [1, 2, 3].
print("np.diag(f):->\n", np.diag(f))  # np.diag(f) extracts the diagonal elements from the array f.

# 15 logspace  # NumPy array with logarithmically spaced values. The arguments specify the start, stop, and number of values.
g = np.logspace(1,3,5)  # 5 values from 10^1 to 10^3
print("np.logspace():->\n", g)

# 16 meshgrid  # NumPy arrays representing a grid. The arguments specify the ranges 
# for the x and y coordinates.
x = np.arange(3)  # This creates a 1D array with values [0, 1, 2]. It will be used as the x-coordinates for the grid.
y = np.arange(3)  # This creates a 1D array with values [0, 1, 2]. It will be used as the y-coordinates for the grid.
X, Y = np.meshgrid(x,y)  # This creates two 2D arrays, X and Y, that represent the grid of coordinates.
print("np.meshgrid():->\n", X)
print("np.meshgrid():->\n", Y)

# 17 indices  # NumPy array representing the indices of a grid. The argument specifies the shape of the grid.
print("np.indices():->\n", np.indices((2,2)))  # This will create a 3D array where the first sub-array contains the row indices and the second sub-array contains the column indices for a 2x2 grid. The output will be:


```





# ADVANCED LEVEL FUNCTIONS

----------

## 18. `np.fromiter()`

**Signature**

`np.fromiter(iterable, dtype)`

Efficient creation from generators.

----------

## 19. `np.fromfunction()`

**Signature**

`np.fromfunction(function, shape)`

Generates array based on formula.

----------

## 20. `np.asarray()`

Converts input to array without copying if possible.

Memory efficient.

----------

## 21. `np.asanyarray()`

Similar to asarray but preserves subclasses.

----------

## 22. `np.random.randint()`

Random integers.

----------

## 23. `np.random.randn()`

Normal distribution values.

----------

## 24. `np.random.choice()`

Sampling from dataset.

----------

## 25. `np.random.uniform()`

Uniform distribution random numbers.


## Table (Advance Level)


  

| S. No. | Method | Purpose | Example | Input | Output | Key Idea | Performance Benefit | Typical Use | Important Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 18 | np.fromiter() | Create array from iterator | np.fromiter(range(5), int) | Iterable | 1D array | Stream processing | Memory efficient | Large data streams | dtype required |
| 19 | np.fromfunction() | Generate array using formula | np.fromfunction(lambda i,j:i+j,(3,3)) | Function + shape | Computed array | Index-based creation | Vectorized generation | Mathematical modeling | Very powerful |
| 20 | np.asarray() | Convert without copying | np.asarray(data) | Sequence | Array | Memory sharing | Avoid duplication | Performance tuning | Faster conversion |
| 21 | np.asanyarray() | Preserve subclasses | np.asanyarray(data) | Array-like | Array/subclass | Flexible conversion | Specialized arrays | Advanced workflows | Rare in beginners |
| 22 | np.random.randint() | Random integers | np.random.randint(0,10,(3,3)) | Range + shape | Integer array | Discrete random | Dataset generation | Simulations | ML datasets |
| 23 | np.random.randn() | Gaussian distribution | np.random.randn(3,3) | Shape | Numeric array | Normal distribution | Statistical modeling | ML initialization | Standard normal |
| 24 | np.random.choice() | Random sampling | np.random.choice(a,5) | Dataset | Random array | Sampling method | Supports probabilities | Data science | With/without replacement |
| 25 | np.random.uniform() | Uniform distribution | np.random.uniform(0,5,10) | Range + size | Numeric array | Continuous random | Flexible distribution | Simulations | Common in statistics |


## Script (Advanced)


```python

# NumPy Array Creation Examples
# Advance level
import numpy as np

# 18 fromiter
# np.fromiter() creates a NumPy array from an iterable object. 
# The first argument is the iterable, and the second argument is the data type of 
# the resulting array. In this example, we are creating an array from a range of 
# integers from 0 to 4, and specifying that the data type should be integer.
a = np.fromiter(range(5), dtype=int)
print("np.fromiter():->\n", a)

# 19 fromfunction
# np.fromfunction() creates a NumPy array by executing a function over each coordinate.
# The first argument is a function that takes as input the indices of the array, and 
# the second argument is the shape of the array. In this example, we are creating 
# a 3x3 array where each element is the sum of its row and column indices. 
# The lambda function takes two arguments, i and j, which represent the row and 
# column indices, respectively. The function returns the sum of i and j, which is used 
# to populate the array.      
b = np.fromfunction(lambda i, j: i + j, (3,3))
print("np.fromfunction():->\n", b)

# 20 asarray
# np.asarray() converts the input to a NumPy array. If the input is already a NumPy array, it will not create a new array but will 
# return the original array. In this example, we are converting a Python list to a NumPy array. The 
# resulting array will have the same values as the list, but it will be of type numpy.ndarray.   
c = np.asarray([1,2,3])
print("np.asarray():->\n", c)

# 21 asanyarray
# np.asanyarray() is similar to np.asarray(), but it will not convert subclasses of ndarray to a base ndarray. 
# If the input is already a NumPy array or a subclass of ndarray, it will return the original array. In this example, 
# we are converting a NumPy array to a NumPy array using np.asanyarray(). Since the input is already a NumPy array, 
# np.asanyarray() will simply return the original array without creating a new one. The output will be the same as 
# the input array c. 
d = np.asanyarray(c)
print("np.asanyarray():->\n", d)

# 22 randint
# np.random.randint() generates random integers from a specified range. The first two arguments specify 
# the lower and upper bounds of the range (inclusive of the lower bound and exclusive of the upper bound), 
# and the third argument specifies the shape of the output array. In this example, we are generating 
# a 3x3 array of random integers between 0 and 9 (inclusive of 0 and exclusive of 10). The resulting 
# array will contain random integers in the specified range, and the shape of the array will be 
# 3 rows and 3 columns.     
e = np.random.randint(0,10,(3,3))
print("np.random.randint():->\n", e)

# 23 randn
# np.random.randn() generates random numbers from a standard normal distribution (mean 0 and standard deviation 1). 
# The arguments specify the shape of the output array. In this example, we are generating a 3x3 array of random 
# numbers from a standard normal distribution. The resulting array will contain random floating-point numbers 
# that are drawn from the specified distribution, and the shape of the array will be 3 rows and 3 columns. 
# Each time you run this code, you will get different random numbers in the array. 
f = np.random.randn(3,3)
print("np.random.randn():->\n", f)

# 24 random choice
# np.random.choice() generates a random sample from a given 1D array of values. 
# The first argument is the array of values to choose from, and 
# the second argument is the number of samples to generate. 
# In this example, we are generating an array of 5 random samples from the array [10, 20, 30]. 
# The resulting array will contain 5 random values that are selected from the specified array, 
# and the values will be either 10, 20, or 30. Each time you run this code, you may get a 
# different set of random values in the output array.   
g = np.random.choice([10,20,30],5)
print("np.random.choice():->\n", g)

# 25 uniform
# np.random.uniform() generates random floating-point numbers from a uniform distribution over a specified range. 
# The first two arguments specify the lower and upper bounds of the range, and 
# the third argument specifies the shape of the output array. 
# In this example, we are generating a 1D array of 10 random floating-point numbers 
# between 0 and 5 (inclusive of 0 and exclusive of 5). The resulting array will contain 
# random floating-point numbers that are uniformly distributed in the specified range, 
# and the shape of the array will be 10 elements in a single dimension. Each time you run this code, 
# you will get different random numbers in the array.  
h = np.random.uniform(0,5,10)
print("np.random.uniform():->\n", h)


```

## Complete NumPy Array Creation Map

```python

NumPy Array Creation
│
├── From Existing Data
│   ├── array
│   ├── asarray
│   ├── asanyarray
│   ├── fromiter
│   ├── fromfunction
│   ├── frombuffer
│   ├── loadtxt
│   ├── genfromtxt
│
├── Basic Arrays
│   ├── zeros
│   ├── ones
│   ├── full
│   ├── empty
│
├── Template-Based Arrays
│   ├── zeros_like
│   ├── ones_like
│   ├── full_like
│   ├── empty_like
│
├── Sequence Arrays
│   ├── arange
│   ├── linspace
│   ├── logspace
│   ├── geomspace
│
├── Matrix / Diagonal Arrays
│   ├── eye
│   ├── identity
│   ├── diag
│   ├── diagflat
│   ├── tri
│   ├── tril
│   ├── triu
│
├── Grid / Coordinate Arrays
│   ├── meshgrid
│   ├── indices
│   ├── mgrid
│   ├── ogrid
│
├── Random Arrays
│   ├── rand
│   ├── randn
│   ├── randint
│   ├── random
│   ├── random_sample
│   ├── choice
│   ├── uniform
│   ├── normal
│
├── Structured / Special Arrays
│   ├── copy
│   ├── tile
│   ├── repeat
│
└── File / External Data Arrays
    ├── load
    ├── savez
    ├── savez_compressed
    ├── fromfile


```














