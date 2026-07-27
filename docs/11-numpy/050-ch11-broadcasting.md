
# Broadcasting in NumPy
Broadcasting is a mechanism in NumPy that allows arrays of different shapes to work together during arithmetic operations. In simple terms: Broadcasting allows NumPy to automatically expand the smaller array so that operations can be performed on arrays with different sizes.
The following script shows the way in which NumPy applies broadcasting to a scalar, a row-vector and a column vector:-

```python

import numpy as np

# 1. Broadcasting with a scalar
arr = np.array([1,2,3])
result = arr + 10  # Broadcasts 10 to [10 10 10] & adds to each element of arr
print(result)  # Output [11 12 13]

# 2. Broadcasting with a matrix and a  row vector
matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
row_vector = np.array([10,20,30])
# Shape of row vector is (3,) & shape of matrix is (3,3). 
# The row vector is broadcasted to (3,3) for addition.
result3 = matrix + row_vector  
print(result3)  # Output [[11 22 33]
#                        [14 25 36]
#                        [17 28 39]]

# 3. Broadcasting with a matrix and a column vector
# Shape of column vector is (3,1) & shape of matrix is (3,3). 
# The column vector is broadcasted to (3,3) for addition.
column_vector = np.array([
                        [10],
                        [20],
                        [30]])

result4 = matrix + column_vector  # Broadcasts the column vector to each column of the matrix
print(result4)  # Output [[11 12 13]
#                        [24 25 26]
#                        [37 38 39]]
```


Note: NumPy broadcasts a row vector by adding more rows and broadcasts a column vector by adding more columns to match the shape of the matrix to which it is being added. 

### The following figure shows how broadcasting was done on a scalar in the script above:

![Broadcasting of a scalar](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch11-broadcast-scalar.png)

### The following figure shows how broadcasting was done on a row vector in the above script

![Broadcasting a row vector](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch11-broadcast-row-vector.png)

### The following figure shows how broadcasting was done on a column vector in the above script

![Broadcasting Column Vector](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch11-broadcast-column-vector.png)

## The Master Flowchart: How NumPy Decides

Before diving into the rules, look at this flowchart. Every time you write `A + B` in NumPy, the C-engine runs through this exact decision tree.


![Broadcasting Decision Tree](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch11-broadcast-rule-flowchart.png)


## Rule 1: Right-Alignment and Left-Padding (The Prepend Rule)

**The Rule:** When comparing two array shapes, NumPy aligns them starting from the **trailing (right-most) dimension** and works its way left. If one array has fewer dimensions than the other, the missing left-side dimensions are padded with a size of `1`.

**Simple Explanation:** Think of aligning numbers in grade school math. You align the ones column on the right, and if a number is shorter, you mentally pad it with zeros on the left. NumPy pads with `1`s.

**Example:**
#### Step 1:
-   Array A shape: `(8, 1, 6, 1)` (4 dimensions)
-   Array B shape: `(7, 1, 5)` (3 dimensions)

#### Step 2:
NumPy compares right-to-left: `1` vs `5`, `6` vs `1`, `1` vs `7`. Then it runs out of dimensions for B. It pads B with a `1` on the left.

-   Effective Shape A: `(8, 1, 6, 1)`
-   Effective Shape B: `(1, 7, 1, 5)` _(The leading 1 was padded)_

#### Step 3:
Wherever dimension is 1, Numpy stretches it to match the dimension of the other array
-   Effective Shape A: `(8, 7, 6, 5)`
-   Effective Shape B: `(8, 7, 6, 5)` 
Now shape and dimensions of both arrays match and mathematical operations can take place

### The following figure shows the steps in broadcasting of 
-   Array A shape: `(8, 1, 6, 1)` (4 dimensions)
-   Array B shape: `(7, 1, 5)` (3 dimensions)

![Flow chart showing broadcasting of A (8,1,6,1) and B (7,1,5)](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch11-broadcast-2-matrices-different-dimensions.png)



**Do's and Don'ts:**

-  **DO:** Rely on this for adding a 1D vector to a 2D matrix. `(3, 4) + (4,)` becomes `(3, 4) + (1, 4)`.
-  **DON'T:** Assume it pads on the right. `(3,) + (3, 4)` will fail. B is not padded to `(3, 4, 1)`; A is padded to `(1, 3)`, which then clashes with `4`.

----------

## Rule 2: The "One or Equal" Rule (The Stretching Rule)

**The Rule:** Two dimensions are compatible for broadcasting if they are exactly equal, OR if one of them is exactly `1`.

**Simple Explanation:** If you are comparing a dimension of size `5` with a dimension of size `5`, they match perfectly. If you are comparing a dimension of size `1` with size `5`, NumPy says, "I can stretch that `1` into five `1`s to make it fit."

**Example:**

-   Comparing Dimension: `1` vs `4`  →  **Compatible**. The `1` is stretched to `4`.
-   Comparing Dimension: `6` vs `6`  →  **Compatible**. They are identical.
-   Comparing Dimension: `3` vs `4`  →  **Incompatible** (See Rule 3).

**Do's and Don'ts:**

-   **DO:** Use `(3, 1)` to apply an operation across columns of a `(3, 4)` matrix. The `1` stretches to `4`.
-   **DON'T:** Forget that the _result_ shape takes the maximum of the two. `(5, 1) + (1, 5)` results in a `(5, 5)` matrix, not `(1, 1)`.

----------

## Rule 3: The Incompatibility Error (The Failure Rule)

**The Rule:** If two dimensions are not equal, AND neither of them is `1`, broadcasting is strictly impossible. NumPy will immediately throw a `ValueError: operands could not be broadcast together`.

**Simple Explanation:** If you have a box of size `3` and a box of size `4`, NumPy refuses to guess how to smash them together. It does not stretch `3` to `4` (that would invent data) and it does not truncate `4` to `3` (that would delete data).

**Example:**

```python
import numpy as np
A = np.zeros((3, 4))
B = np.zeros((4, 3))
print(A + B)
# ValueError: operands could not be broadcast together with shapes (3,4) (4,3)
```
Why? Right-alignment compares `4` vs `3`. Neither is `1`. Error.

**Do's and Don'ts:**

-   DO: Use `.reshape()` or `.T` (transpose) to fix dimension ordering before adding.
-   DON'T: Try to wrap the operation in a `try/except` block to hide the error. It usually means your data logic is mathematically flawed.

----------

## Rule 4: Virtual Stretching (The Memory Rule)

**The Rule:** The array with the dimension of size `1` is _not_ actually copied in memory to match the larger array. It is "virtually" stretched using internal memory strides.

**Simple Explanation:** If you have an array of shape `(1, 1000000)` and broadcast it with `(1000, 1000000)`, NumPy does _not_ create a new array of 1 billion elements. It uses a clever C-level pointer trick to reuse the same 1 million elements 1000 times.

**Example (Proof of no memory copy):**

```python
import  numpy  as  np
A = np.ones((5, 4)) # 20 elements
B = np.array([1, 2, 3, 4]) # 4 elements

# Before broadcast -
# A is 20 bytes (5 rows x 4 columns x 4 bytes per float) and
# B is 16 bytes (4 elements x 4 bytes per int)

print(f"A size: {A.nbytes} bytes")
print(f"B size: {B.nbytes} bytes")

# During broadcast (we don't assign it, we just perform the math)
# NumPy uses 20 + 4 bytes of memory to do this, NOT 20 + 20 bytes.

C = A  +  B
print(f"Result C size: {C.nbytes} bytes") # Result is 20 bytesS
```

This code is a perfect demonstration of **NumPy Broadcasting** and why it is so highly optimized for performance and memory.

Here is a step-by-step breakdown of exactly how this code works under the hood.

### 1. Understanding the Shapes

Before NumPy can perform arithmetic between two arrays, it checks their shapes to see if they are compatible.

-   **Array A** has a shape of `(5, 4)`. It is a 2D matrix with 5 rows and 4 columns, filled with `1.` (ones).
    
-   **Array B** has a shape of `(4,)`. It is a 1D vector with 4 elements: `[1, 2, 3, 4]`.
    

### 2. The Broadcasting Rule

When you ask NumPy to compute `A + B`, it compares their shapes starting from the **rightmost** dimension:

-   **Rightmost dimension (Columns):** `A` has 4 columns. `B` has 4 elements. Because these match perfectly, NumPy permits the operation.
    
-   **Next dimension (Rows):** `A` has 5 rows. `B` has no row dimension (it's implicitly 1).
    

To make the math work, NumPy **broadcasts** (stretches) `B` down 5 times so that it conceptually acts like a `5 x 4` matrix.

### 3. The Math (What happens conceptually)

Conceptually, NumPy treats Array B as if it were duplicated across 5 rows to match Array A:

**Array A (5x4):**
```
[[1, 1, 1, 1],
 [1, 1, 1, 1],
 [1, 1, 1, 1],
 [1, 1, 1, 1],
 [1, 1, 1, 1]]
```

**Array B (Conceptually Broadcasted to 5x4):**

```
[[1, 2, 3, 4],
 [1, 2, 3, 4],
 [1, 2, 3, 4],
 [1, 2, 3, 4],
 [1, 2, 3, 4]]
```
When they are added together, element by element, the resulting **Array C** is:

```
[[2, 3, 4, 5],
 [2, 3, 4, 5],
 [2, 3, 4, 5],
 [2, 3, 4, 5],
 [2, 3, 4, 5]]
```

### 4. The Memory Magic (What the prints prove)

The most important part of the code is the comments and the `.nbytes` print statements.

If you were doing this in standard Python, you would have to actually create that `5x4` version of Array B, duplicating the data in memory before adding it.

**NumPy does not do this.** During broadcasting, NumPy does not actually allocate new memory to duplicate `B` five times. Instead, it uses a concept called **"strides"** at the C-language level. It simply loops over the existing 4 elements of `B` again and again for each row of `A`.

This is what is meant by the comments:

> _"NumPy uses 20 + 4 bytes of memory to do this, NOT 20 + 20 bytes."_

**Do's and Don'ts:**

-   DO: Use broadcasting confidently for massive arrays knowing it won't crash your RAM.
-   DON'T: Manually use `np.tile()` or `np.repeat()` to make arrays the same size before math. This defeats the entire purpose of broadcasting and wastes memory!


## Master Comparison Table: Shapes and Results

This table shows the most common broadcasting scenarios one encounter.

  

| Array A Shape | Array B Shape | Compatible? | Reasoning | Final Output Shape |
| --- | --- | --- | --- | --- |
| (5, 4) | (4,) | Yes | B padded to (1, 4). Dim 1 stretches. | (5, 4) |
| (5, 4) | (5, 1) | Yes | Dim 1 (1) stretches to 4. | (5, 4) |
| (5, 4) | (1, 4) | Yes | Dim 0 (1) stretches to 5. | (5, 4) |
| (5, 1, 4) | (1, 4) | Yes | B padded to (1, 1, 4). Dim 0 & 1 stretch. | (5, 1, 4) |
| (5, 4, 1) | (4, 1) | Yes | B padded to (1, 4, 1). Dims 0 & 1 stretch. | (5, 4, 1) |
| (5,) | (5, 4) | No | B padded to (1, 5, 4). Compare 5 vs 4 →Error! | ValueError |
| (3, 4) | (4, 3) | No | Compare 4 vs 3 →Error! | ValueError |






