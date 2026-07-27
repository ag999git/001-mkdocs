


# 1D Arrays: 

#### Note
-    **`np.concatenate()` is the foundation → you control the axis manually.**
-    **`np.hstack()` and `np.vstack()` are shortcuts built on top of it.**
-    **`hstack = horizontal (columns), vstack = vertical (rows).`**
-    **For 1D arrays, `vstack()` adds a new dimension, while `hstack()` does not.**

### So arrays behave differently in 1D scenario. The following exercise explains the difference, its how and why. It also tries to visualize the prcess

## Step-by-Step Visualization

We start with two 1D arrays in **NumPy**:

`x  =  np.array([1, 2])`
`y  =  np.array([3, 4])`

----------

### Step 1: How NumPy “sees” 1D arrays

A 1D array has **shape `(2,)`**, meaning:
For x
```python
     x → [1   2]  
          ↑   ↑  
    index 0,  1  
```
For y
```python
     y → [3   4]
          ↑   ↑  
    index 0,  1 
```
👉 Important:

-   There is **no row/column distinction yet**
-   It is just a **flat vector**

----------

### Step 2: `np.hstack((x, y))`

#### Operation: “Join along existing axis”

Since 1D arrays only have **axis = 0**, `hstack` behaves like:

```python
[1   2]  +  [3   4]  
 ↓           ↓  
Concatenate along axis 0
```

#### Result:

[1   2   3   4]

#### Shape:

(4,)

----------

### Step 3: `np.concatenate((x, y), axis=0)`

This is exactly the same operation:

```python
[1   2]  +  [3   4]  
 ↓           ↓  
axis = 0
```

#### Result:

[1   2   3   4]

####  Key Insight:

> For 1D arrays, **`hstack()` = `concatenate(axis=0)`**

----------

###  Step 4: `np.vstack((x, y))`

Now things change 

#### Step 4A: Implicit reshaping

`vstack()` first converts 1D arrays into **row vectors (2D)**:

`x → [[1   2]]`   `shape (1,2)`  ie 1 row and 2 columns

`y → [[3   4]]`   `shape (1,2)` ie 1 row and 2 columns

##### This step is **hidden but crucial**

----------

#### Step 4B: Stack along axis 0

Now we stack rows:

```
[[1   2]]  
[[3   4]]
```
#### Final Result:
```
[[1   2]  
 [3   4]]
```

#### Shape:
(2, 2)

### Side-by-Side Comparison

  

| Operation | Internal Step | Result | Shape |
| --- | --- | --- | --- |
| hstack | No reshape | [1 2 3 4] | (4,) |
| concatenate(axis=0) | No reshape | [1 2 3 4] | (4,) |
| vstack | Reshape → (1,2) | [[1 2],[3 4]] | (2,2) |


## Script
The following script shows how hstack(), vstack() and concatenate() operate on a 1D array


```python

import numpy as np

a = np.array([[1, 2]])
b = np.array([[3, 4]])

# Horizontal stack (axis=1)
h_stack = np.hstack((a, b))
print(f"Horizontal stack:->{h_stack} \nShape:-> {h_stack.shape}\n")
# Output:
# Horizontal stack:->[[1 2 3 4]]
# Shape:-> (1, 4)

# Horizontal stack using np.concatenate with axis=1
h_stack_concat = np.concatenate((a, b), axis=1)
print(f"Horizontal stack using concatenate:->{h_stack_concat} \nShape:-> {h_stack_concat.shape}\n")
# Output:
# Horizontal stack using concatenate:->[[1 2 3 4]]
# Shape:-> (1, 4)

# Vertical stack using np.vstack (axis=0 is implicit for vstack)
v_stack = np.vstack((a, b))
print(f"Vertical stack:->{v_stack} \nShape:-> {v_stack.shape}\n")
# Output:
# Vertical stack:->[[1 2]
#                   [3 4]]
# Shape:-> (2, 2)

# Vertical stack using np.concatenate with axis=0 (axis has to be specified for concatenate)
v_stack_concat = np.concatenate((a, b), axis=0)
print(f"Vertical stack using concatenate:->{v_stack_concat} \nShape:-> {v_stack_concat.shape}\n")
# Output:
# Vertical stack using concatenate:->[[1 2]
#                                      [3 4]]
# Shape:-> (2, 2)




```








