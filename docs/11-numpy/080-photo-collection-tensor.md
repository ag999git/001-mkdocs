



# Case Study: Organizing a Large Photo Archive into a Structured Tensor


## 1. Research Scenario

Alex, a field researcher and photographer, has collected thousands of images over several years. His dataset includes photographs from different domains such as:

### Collections (`C`)

1.  **Wildlife Expedition**
2.  **Family Events**
3.  **Urban Landscapes**

----------

### Categories within each collection (K)

#### Wildlife Expedition

-   Safari (daytime animals)
-   Night Watch (nocturnal animals)

#### Family Events

-   Weddings
-   Birthdays

#### Urban Landscapes

-   Architecture
-   Street Life

----------

### Images within each category (N)

Each category contains multiple images:

Example (Wildlife → Safari):

-   `lion_01.jpg`
-   `elephant_02.jpg`
-   `deer_03.jpg`
-   `zebra_04.jpg`

Example (Urban → Street Life):

-   `market_01.jpg`
-   `traffic_02.jpg`
-   `vendor_03.jpg`
-   `crowd_04.jpg`

----------

## 2. Research Problem

Alex wants to:

> Convert this unstructured collection of images into a structured format suitable for machine learning analysis.

----------

### 3. Constraints

To process the data using **NumPy**, the dataset must satisfy:

-   All images must have the **same resolution** → `(H, W)`
-   All images must have **3 channels (RGB)**
-   Each category must contain the **same number of images (N)**

----------

### 4. Target Tensor Structure

`(C, K, N, H, W, 3)`

  

| Symbol | Meaning |
| --- | --- |
| C | Collections |
| K | Categories per collection |
| N | Images per category |
| H | Height |
| W | Width |
| 3 | RGB channels |


### 5. Task

#### Objective

Convert the dataset into a **6D tensor** of shape:

(3, 2, 4, 64, 64, 3)

----------

#### Tasks

1.  Assume:
    -   3 collections
    -   2 categories per collection
    -   4 images per category
    -   Resolution = 64 × 64
    -   RGB channels = 3
2.  Simulate image data using random numbers
3.  Build:
    -   One collection → `(2, 4, 64, 64, 3)`
    -   Multiple collections → stack into `(3, 2, 4, 64, 64, 3)`
4.  Verify shapes at each step

----------

## 6. Conceptual Theory (Step-by-Step)**


### Step 1: Pixel Level

[R, G, B]

----------

### Step 2: Image Level

(H, W, 3)

----------

### Step 3: Category Level

(N, H, W, 3)

----------

### Step 4: Collection Level

(K, N, H, W, 3)

----------

### Step 5: Dataset Level

(C, K, N, H, W, 3)

----------

### Conceptual visualization

```
Dataset
│
├── Collection 1 (Wildlife)
│   ├── Safari
│   │   ├── lion_01
│   │   ├── elephant_02
│   │   └── ...
│   └── Night Watch
│
├── Collection 2 (Family)
│   ├── Wedding
│   └── Birthday
│
└── Collection 3 (Urban)
    ├── Architecture
    └── Street Life
```



## 7. Full Script with Explanation

### 7.(A) How a 5D Tensor with random integers is created
Before writing the script, let us understand how a tensor can be created 


### How `np.random.randint()` Creates a Multi-Dimensional Tensor

In **NumPy**, the function:

```python
one_collection  =  np.random.randint(  
  0, 256,  
  size=(K, N, H, W, CH),  
  dtype=np.uint8  
)
```
is used to generate a **multi-dimensional array (tensor)** filled with random values.

----------

### How it Works

#### 1. Range of Values

`0, 256`

-   Generates integers from **`0 to 255`**
-   Suitable for **RGB pixel values**

----------

#### 2. Total Number of Elements

The `size` parameter:

`(K, N, H, W, CH)`

tells NumPy how many values to generate:

`Total elements = K × N × H × W × CH`

**NumPy first creates these many random numbers.**

----------

#### 3. Reshaping into Dimensions

After generating values, NumPy **organizes them into a structured tensor**:

`(K, N, H, W, CH)`

Where:

-   **K** → categories
-   **N** → images per category
-   **H** → height
-   **W** → width
-   **CH** → channels (RGB)

----------

#### 4. Interpretation

The resulting tensor represents:

Categories → Images → Pixels → RGB values

Each element at the deepest level is:

`[R, G, B]`

----------

#### 5. Data Type

`dtype=np.uint8`

-   Stores values as **8-bit unsigned integers**
-   Efficient for image data (0–255)

----------

####  Key Insight

> `np.random.randint()` first generates a flat set of random numbers and then arranges them into the specified multi-dimensional shape.

----------

#### Summary

> The `size` parameter defines the structure of the tensor, while `randint()` fills that structure with random integer values.




### 7.(B) How the 5D tensors get converted into 6D tensor

Building a 6D Tensor from 5D Tensors. In **NumPy**, complex datasets are often constructed step-by-step by combining smaller tensors.

----------

#### Step 1: Create a 5D Tensor (One Collection)

We first create a tensor representing **one collection of images**:

`(K, N, H, W, CH)`

Where:

-   **K** → number of categories
-   **N** → number of images per category
-   **H, W** → height and width of each image
-   **CH** → number of channels (e.g., 3 for RGB)

This tensor represents **one complete collection** (e.g., Wildlife photos).

----------

#### Step 2: Store Multiple Collections in a List

Next, we create multiple such collections and store them in a Python list:

`collection_list  = [collection1, collection2, collection3]`

>Each element in the list is a **5D tensor** of shape:

`(K, N, H, W, CH)`



Important:

-   This is still a **Python list**, of 5D Tensors, not a higher-dimensional (6D) tensor yet

----------

#### Step 3: Use `np.stack()` to Create a New Axis

We now convert the list into a single tensor:

`dataset  =  np.stack(collection_list, axis=0)`

----------

#### What does `np.stack()` do?

-   It **takes each element of the list**
-   Assigns it a position along a **new axis**
-   Combines them into one tensor

----------

Conceptually, It is somewhat like

**Before stack**

```
Collection 1 → (K,N,H,W,CH)
Collection 2 → (K,N,H,W,CH)
Collection 3 → (K,N,H,W,CH)

```
**After stack**

```
[  
 Collection 1,  
 Collection 2,  
 Collection 3  
]
```


#### Resulting Shape

(C, K, N, H, W, CH)

Where:

-   **C** = number of collections (length of the list)

----------

### Key Insight

> `np.stack()` uses the **index of each element in the list** to create a new dimension (axis).

----------

### Visual Interpretation

Before stacking:
```
collection_list = [  
 collection0,  
 collection1,  
 collection2  
]
```
After stacking:
```
dataset[0] → collection0   
dataset[1] → collection1   
dataset[2] → collection2 
```

The list index becomes:

`axis = 0  (Collections dimension)`

----------

#### Final Understanding

-   A **5D tensor** represents one collection
-   A **list of 5D tensors** represents multiple collections (unstructured)
-   `np.stack(axis=0)` converts this into a **6D tensor** by introducing a new dimension

----------

## Summary of the process

> We first construct individual 5D tensors representing separate collections. These tensors are stored in a list, and `np.stack()` is then used to introduce a new axis corresponding to the list index, thereby creating a higher-dimensional tensor that organizes all collections into a single structured dataset.








### 7.(C) The complete script


```python

import numpy as np

# <------------------ONE---------------->
# STEP 1: Define dataset structure

# Number of collections (Wildlife, Family, Urban)
C = 3  # Axis 0: Collections. This will be the new axis we create when we stack the collections together using np.stack. 
# But for now, we will create each collection of 5D tensors and then stack them together later. 
# Categories per collection (e.g., Safari, Night)
K = 2  # Axis 1: Categories

# Images per category
N = 4  # Axis 2: Images

# Image resolution
H = 64  # Axis 3: Height
W = 64  # Axis 4: Width

# RGB channels
CH = 3  # Axis 5: Channels


#<------------------TWO---------------->
# STEP 2: Create ONE collection

# This simulates one collection (e.g., Wildlife)
# Shape: (categories, images, height, width, channels)

# Create a tensor of dimensions (K, N, H, W, CH) filled with random integers 
# between 0 and 255 (inclusive) representing pixel values in RGB format.
# Notice it has 5 dimensions corresponding to the structure we defined:
# The 6th dimension collections (C) will be added later using stacking.
one_collection = np.random.randint(
    0, 256,
    size=(K, N, H, W, CH),
    dtype=np.uint8
)

print("One collection shape:", one_collection.shape)
# Output: One collection shape: (2, 4, 64, 64, 3)
print(f"Items in one collection: {one_collection.size}")  # Total number of elements
#Output: Items in one collection: 98304 = 2 categories x 4 images x 64 height x 64 width x 3 channels
# Interpretation:
# 2 categories → each has 4 images → each image is 64×64×3

#<-----------------THREE---------------->
# STEP 3: Create multiple collections

collection_list = []

for i in range(C):
    # Simulate a collection (e.g., Family or Urban)
    collection = np.random.randint(
        0, 256,
        size=(K, N, H, W, CH),
        dtype=np.uint8
    )
    # Add this collection to the list
    collection_list.append(collection)


print(f"Number of collections created: {len(collection_list)}")  
# Output: Number of collections created: 3
print(f"Shape of each collection: {collection_list[0].shape}")  
# Output: Shape of each collection: (2, 4, 64, 64, 3)

# Notice we have a list of 3 collections, each with the same shape (2, 4, 64, 64, 3).
# Each collection is a 5D tensor representing categories, images, height, width, and channels.

#<-----------------FOUR---------------->
# STEP 4: Stack collections
# Now we want to combine these 3 collections into a single dataset tensor.
# We will use np.stack to combine the collections along a new axis (axis=0) 
# which will represent the collection dimension (C).
# This new axis will basically be the "index" of the list of collections we created.
# We will stack along a new axis (axis=0) to create a 6D tensor with shape (C, K, N, H, W, CH).

# Add a new axis → collections dimension

# Stacking along axis 0 creates a new "collection" dimension at the front
# The resulting shape will be (3, 2, 4, 64, 64, 3) which corresponds to:
# 3 collections (C) → 2 categories (K) → 4 images (N) → 64 height (H) → 64 width (W) → 3 channels (CH)
# The np.stack function takes a sequence of arrays (in this case, the list of collections) 
# and stacks them along a new axis specified by the axis parameter.
# By using axis=0, we are creating a new dimension at the front of the shape, 
# which will represent the different collections in our dataset.
# So the index of the list collection_list becomes the index of the new collection 
# dimension in the resulting dataset tensor.
dataset = np.stack(collection_list, axis=0) # axis = 0 

print("Final dataset shape:", dataset.shape)
# Output: Final dataset shape: (3, 2, 4, 64, 64, 3)

#<-----------------FIVE---------------->
# STEP 5: Verify structure

print("\nDataset interpretation:")
print(f"Collections (C): {dataset.shape[0]}")  # Output: Collections (C): 3
print(f"Categories (K): {dataset.shape[1]}")  # Output: Categories (K): 2
print(f"Images (N): {dataset.shape[2]}")  # Output: Images (N): 4
print(f"Height (H): {dataset.shape[3]}")  # Output: Height (H): 64
print(f"Width (W): {dataset.shape[4]}")  # Output: Width (W): 64
print(f"Channels: {dataset.shape[5]}")  # Output: Channels: 3   


#<-----------------SIX---------------->
# STEP 6: Access a specific image

# Example: First collection → first category → first image

image = dataset[0, 0, 0]

print("\nSingle image shape:", image.shape)  # Output: Single image shape: (64, 64, 3)
print(f"Pixel value at (0,0) in this image: {image[0, 0]}")  
# Output: Pixel value at (0,0) in this image: [R, G, B] values of the top-left pixel


```






















