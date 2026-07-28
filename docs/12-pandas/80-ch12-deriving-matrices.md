



# Basic Data Manipulations

## Research Topic: Deriving Metrics and Organizing Penguin Morphology

**Research Question:** _How can derived metrics be constructed from existing data, irrelevant data be removed, and the resulting dataset be sorted to facilitate comparative biological analysis?_

**Project Scenario:** A marine biologist hypothesizes that the ratio of bill length to bill depth (the "Slenderness Index") varies significantly between species. To test this, the dataset must be manipulated to:

1.  Calculate a new column: `slenderness_index` (Bill Length / Bill Depth).
2.  Remove non-essential categorical data (`sex`, `island`) to focus purely on physical morphology.
3.  Sort the dataset to identify penguins with the most extreme body structures.

**Task:** Using the Palmer Penguins dataset, write a script to generate the new metric, clean the dataframe using both `inplace` and reassignment methods, and sort the results by species and body mass.

----------

## 1. Conceptual Deep Dive

Before execution, one must understand the mechanics of vectorization, deletion strategies, and sorting algorithms in Pandas.

### A. Adding New Columns

Pandas allows for **vectorized operations**, meaning one can perform math on entire columns without writing loops.

  

| Syntax | Description | Example |
| --- | --- | --- |
| `df['new'] = df['a'] + df['b']` | Element-wise addition (or any math). | `df['total'] = df['x'] + df['y']` |
| `df['new'] = df['col'].str.upper()` | String manipulation. | `df['name'] = df['name'].str.upper()` |

```python
# ERROR EXAMPLE: Mismatched lengths
# df['new_col'] = [1, 2, 3] 
# ValueError: Length of values (3) does not match length of index (344)
```

## B. Deleting Columns

There are two primary ways to remove data, with distinct behavioral differences.

| Method | Syntax | Behavior |
| --- | --- | --- |
| `.drop()` | `df.drop('col', axis=1)` | Returns a new DataFrame. Original remains unchanged unless inplace=True. Flexible (can drop rows too). |
| `del` | `del df['col']` | Directly deletes from the original DataFrame. Returns nothing. Permanent immediately. |


## C. Inplace vs. Reassignment

This is a fundamental concept in Python data science.


| Parameter | Mode | Explanation |
| --- | --- | --- |
| `inplace=True` | In-place | The operation modifies the object itself. No value is returned (returns None). |
| `inplace=False (Default)` | Copy | The operation creates a copy of the data, modifies it, and returns the new copy. The original object is untouched. |


## D. Sorting Data

The `.sort_values()` method arranges rows based on column values.

  

| Parameter | Option | Effect |
| --- | --- | --- |
| `by` | String or List | Determines which column(s) to sort by. |
| `ascending` | Boolean or List | True (Low to High), False (High to Low). Can differ per column in a list. |
| `na_position` | first' or 'last' | Where to place missing values (NaN). |


# Example script


```python

"""
PROJECT: Basic Data Manipulations in Pandas
DATASET: Palmer Penguins

OBJECTIVE:
1. Add calculated columns
2. Delete columns using different methods
3. Understand inplace vs reassignment
4. Sort data

NOTE:
This script is structured for teaching with detailed explanations.
"""

# ==========================================================
# STEP 0: IMPORT LIBRARIES AND LOAD DATASET
# ==========================================================

print("\nSTEP 0: IMPORT LIBRARIES AND LOAD DATASET")

import pandas as pd
import seaborn as sns

df = sns.load_dataset('penguins')

print("\nInitial Data Overview:")
print(df.head())  # Display the first 5 rows to understand the structure and columns of the dataset.
print("Data types:\n", df.dtypes)  # Show the data types of each column to identify any potential issues for calculations or sorting.
print("Shape:", df.shape)  # Show the number of rows and columns in the dataset to understand its size and dimensionality.


# ==========================================================
# PHASE 1: DATA PREPARATION
# ==========================================================

print("\nPHASE 1: DATA PREPARATION")

# ----------------------------------------------------------
# STEP 1.1: Handling Missing Values (Basic Strategy)
# ----------------------------------------------------------
print("\nSTEP 1.1: Handling Missing Values")

# NOTE:
# Filling all missing values with 0 is simple but NOT always ideal.
# It is done here only to avoid division errors in teaching context.

df = df.fillna(0)  # This replaces all NaN values in the DataFrame with 0.
print("Missing values handled using fillna(0)")

# Better practice (not used here for simplicity):
# df['bill_length_mm'].fillna(df['bill_length_mm'].mean())


# ==========================================================
# PHASE 2: ADDING CALCULATED COLUMNS
# ==========================================================

print("\nPHASE 2: ADDING CALCULATED COLUMNS")

# ----------------------------------------------------------
# STEP 2.1: Create Slenderness Index
# ----------------------------------------------------------
print("\nSTEP 2.1: Creating 'slenderness_index'")

# Formula:
# slenderness_index = bill_length_mm / bill_depth_mm
# This new column will give us an idea of how slender the penguin's bill is.
# Potential issue: If 'bill_depth_mm' is 0 (after fillna), this will result in division by zero, 
# which will produce inf values in 'slenderness_index'.
df['slenderness_index'] = df['bill_length_mm'] / df['bill_depth_mm']

# In a real dataset, we would want to handle this more carefully 
# (e.g., by filling missing values with mean or median instead of 0, or 
# by adding a small constant to the denominator to avoid division by zero).
# If bill_depth_mm = 0 → division by zero → inf values

# ERROR EXAMPLE: Creating a new column based on non-existing columns will raise a KeyError.
# df['new_col'] = df['unknown_column'] * 2 
# This will raise an error because 'unknown_column' does not exist in the DataFrame. 

print("\nNew column preview:")
print(df[['bill_length_mm', 'bill_depth_mm', 'slenderness_index']].head())  
# Shows the original bill_length_mm and bill_depth_mm along with the new slenderness_index for the first 5 rows.


# ==========================================================
# PHASE 3: DELETING COLUMNS
# ==========================================================

print("\nPHASE 3: DELETING COLUMNS")

# ----------------------------------------------------------
# STEP 3.1: Using drop() with Reassignment
# ----------------------------------------------------------
print("\nSTEP 3.1: Using drop() with reassignment")

cols_to_remove = ['sex']  # We will only remove 'sex' here, leaving 'island' for the next step.

# drop() returns a new DataFrame with the specified columns removed, so we need to assign it back to a variable.
df_reassigned = df.drop(columns=cols_to_remove)

print(f"Does Original df have column for 'sex'?->: {'sex' in df.columns}") # True, because we haven't modified the original df yet.
print(f"Does df_reassigned have column for 'sex'?->: {'sex' in df_reassigned.columns}") # False, because we dropped 'sex' in df_reassigned. 


# ----------------------------------------------------------
# STEP 3.2: Using del (In-place Deletion)
# ----------------------------------------------------------
print("\nSTEP 3.2: Using del")

# 'del' permanently modifies the DataFrame
del df_reassigned['island']  # This will remove the 'island' column from df_reassigned permanently.

print(f"Has column 'island' been removed using del? -> {'island' not in df_reassigned.columns}")  # True, because 'island' has been deleted from df_reassigned.

# ERROR EXAMPLE: Using del on a non-existing column will raise a KeyError.
# del df['non_existing_column']


# ----------------------------------------------------------
# STEP 3.3: Using drop() with inplace=True
# ----------------------------------------------------------
print("\nSTEP 3.3: Using drop() with inplace=True")
# inplace=True modifies the DataFrame directly, so we don't need to assign it back to df_reassigned.
df_reassigned.drop(columns=['species'], inplace=True)

print(f"Has column 'species' been removed using inplace? -> {'species' not in df_reassigned.columns}")  # True, because 'species' has been deleted from df_reassigned.

# ERROR EXAMPLE: Using drop() without assignment or inplace=True will have no effect.
# df.drop(columns=['col'])  # No assignment → no effect


# ==========================================================
# PHASE 4: SORTING DATA
# ==========================================================

print("\nPHASE 4: SORTING DATA")

# NOTE:
# Sorting is performed on original df to preserve all columns


# ----------------------------------------------------------
# STEP 4.1: Single Column Sorting
# ----------------------------------------------------------
print("\nSTEP 4.1: Sorting by single column")

# Sort by body mass (descending)
df_heaviest = df.sort_values(by='body_mass_g', ascending=False)

print("\nTop 3 heaviest penguins:")
# This will show the top 3 rows of the DataFrame sorted by body mass in descending order, 
# which corresponds to the 3 heaviest penguins.
print(df_heaviest[['species', 'body_mass_g']].head(3))


# ----------------------------------------------------------
# STEP 4.2: Multi-Column Sorting
# ----------------------------------------------------------
print("\nSTEP 4.2: Sorting by multiple columns")

# Sort by species (ascending) and then by body mass (descending)
# This will sort the DataFrame first by 'species' in alphabetical order, and then within each species, 
# it will sort by 'body_mass_g' from heaviest to lightest. 
sort_criteria = ['species', 'body_mass_g']  # 
ascending_rules = [True, False]  # True for species (A-Z), False for body mass (heaviest to lightest)

df_sorted_complex = df.sort_values(by=sort_criteria, ascending=ascending_rules)

# Filter Adelie penguins
# After sorting, we filter the DataFrame to only include rows where the 'species' column is 'Adelie'.
adelies = df_sorted_complex[df_sorted_complex['species'] == 'Adelie']

print("\nLast 3 Adelie penguins (sorted by mass):")
# This will show the last 3 rows of the filtered DataFrame, which corresponds to the 
# 3 lightest Adelie penguins due to the sorting order because we had earlier sorted by body mass in descending order.
# So lightest Adelie penguins will be at the end of the Adelie group in the sorted DataFrame.
print(adelies[['species', 'body_mass_g', 'island']].tail(3))

# ERROR EXAMPLE: Sorting by a non-existing column will raise a KeyError.
# df.sort_values(by='non_existing_column')


# ==========================================================
# STEP 5: SUMMARY
# ==========================================================

print("\nSTEP 5: SUMMARY")

print("""
KEY LEARNINGS:

1. New columns can be derived using arithmetic operations
2. Columns can be deleted using drop() or del
3. inplace=True modifies the DataFrame directly
4. Sorting helps organize and analyze data efficiently

BEST PRACTICE:

- Prefer reassignment over inplace for clarity
- Always check column names before operations
- Handle missing values thoughtfully (avoid blind fillna(0))
""")

```

# Step by Step explanation of the script



## STEP-WISE EXPLANATION



### STEP 0: Import Libraries and Load Dataset

### Purpose

To initialize the working environment and load the dataset into a Pandas DataFrame.

----------

### Methods Used

#### 1. `sns.load_dataset()`

`df  =  sns.load_dataset('penguins')`

**Signature**

`seaborn.load_dataset(name)`

| Aspect | Explanation |
| --- | --- |
| Input | Dataset name (string) |
| Output | Pandas DataFrame |
| Dependency | Internet required |

### 2. `df.head()`

`df.head()`

| Purpose | Preview first 5 rows |  
| Output | DataFrame subset |

----------

### 3. `df.dtypes`

-    Purpose → Shows data types   
-    Output → Series

----------

### 4. `df.shape`

-    Purpose → Dimensions   
-    Output → Tuple `(rows, columns)` 

----------

### Script for STEP 0

```python

# ==========================================================
# STEP 0: IMPORT LIBRARIES AND LOAD DATASET
# ==========================================================

print("\nSTEP 0: IMPORT LIBRARIES AND LOAD DATASET")

import pandas as pd
import seaborn as sns

df = sns.load_dataset('penguins')

print("\nInitial Data Overview:")
print(df.head())  # Display the first 5 rows to understand the structure and columns of the dataset.
print("Data types:\n", df.dtypes)  # Show the data types of each column to identify any potential issues for calculations or sorting.
print("Shape:", df.shape)  # Show the number of rows and columns in the dataset to understand its size and dimensionality.


```

### Output for Script of Phase 0

```python
STEP 0: IMPORT LIBRARIES AND LOAD DATASET

Initial Data Overview:
  species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g     sex
0  Adelie  Torgersen            39.1           18.7              181.0       3750.0    Male
1  Adelie  Torgersen            39.5           17.4              186.0       3800.0  Female
2  Adelie  Torgersen            40.3           18.0              195.0       3250.0  Female
3  Adelie  Torgersen             NaN            NaN                NaN          NaN     NaN
4  Adelie  Torgersen            36.7           19.3              193.0       3450.0  Female
Data types:
 species               object
island                object
bill_length_mm       float64
bill_depth_mm        float64
flipper_length_mm    float64
body_mass_g          float64
sex                   object
dtype: object
Shape: (344, 7)



```



### Output Explanation

-   First 5 rows → shows structure (columns like species, bill_length_mm, etc.)
-   `dtypes` → identifies numeric vs categorical columns
-   `shape` → typically `(344, 7)`

----------

## PHASE 1: DATA PREPARATION

### STEP 1.1: Handling Missing Values

### Purpose

To ensure operations like division do not fail due to missing values.

----------

### Method Used

### `.fillna()`

>`df  =  df.fillna(0)`
>Signature
>`DataFrame.fillna(value, axis=None, inplace=False)`


----------

### Do’s and Don’ts

Use for quick fixes  
Avoid blindly replacing all NaN with 0  
Can distort statistical meaning


### Script for Phase 1

```python
# ==========================================================
# PHASE 1: DATA PREPARATION
# ==========================================================

print("\nPHASE 1: DATA PREPARATION")

# ----------------------------------------------------------
# STEP 1.1: Handling Missing Values (Basic Strategy)
# ----------------------------------------------------------
print("\nSTEP 1.1: Handling Missing Values")

# NOTE:
# Filling all missing values with 0 is simple but NOT always ideal.
# It is done here only to avoid division errors in teaching context.

df = df.fillna(0)  # This replaces all NaN values in the DataFrame with 0.
print("Missing values handled using fillna(0)")

# Better practice (not used here for simplicity):
# df['bill_length_mm'].fillna(df['bill_length_mm'].mean())



```

### Output for PHASE 1

```python

PHASE 1: DATA PREPARATION

STEP 1.1: Handling Missing Values
Missing values handled using fillna(0)

```

### Output Explanation

All NaN → replaced with 0




----------

### Common Issue

`df['bill_length_mm'] /  df['bill_depth_mm']`

>If denominator = 0 → **inf values**

----------

## PHASE 2: ADDING CALCULATED COLUMNS

### STEP 2.1: Create Slenderness Index

#### Purpose

To derive a new feature (feature engineering)

-----

#### Operation Used

`df['new_col'] =  df['col1'] /  df['col2']`

#### Explanation

| Column | Meaning |
| --- | --- |
| bill_length_mm | Length |
| bill_depth_mm | Depth |
| slenderness_index | Ratio |


### Script for PHASE 2

```python
# ==========================================================
# PHASE 2: ADDING CALCULATED COLUMNS
# ==========================================================

print("\nPHASE 2: ADDING CALCULATED COLUMNS")

# ----------------------------------------------------------
# STEP 2.1: Create Slenderness Index
# ----------------------------------------------------------
print("\nSTEP 2.1: Creating 'slenderness_index'")

# Formula:
# slenderness_index = bill_length_mm / bill_depth_mm
# This new column will give us an idea of how slender the penguin's bill is.
# Potential issue: If 'bill_depth_mm' is 0 (after fillna), this will result in division by zero, 
# which will produce inf values in 'slenderness_index'.
df['slenderness_index'] = df['bill_length_mm'] / df['bill_depth_mm']

# In a real dataset, we would want to handle this more carefully 
# (e.g., by filling missing values with mean or median instead of 0, or 
# by adding a small constant to the denominator to avoid division by zero).
# If bill_depth_mm = 0 → division by zero → inf values

# ERROR EXAMPLE: Creating a new column based on non-existing columns will raise a KeyError.
# df['new_col'] = df['unknown_column'] * 2 
# This will raise an error because 'unknown_column' does not exist in the DataFrame. 

print("\nNew column preview:")
print(df[['bill_length_mm', 'bill_depth_mm', 'slenderness_index']].head())  
# Shows the original bill_length_mm and bill_depth_mm along with the new slenderness_index for the first 5 rows.




```

### Output for PHASE 2

```python
PHASE 2: ADDING CALCULATED COLUMNS

STEP 2.1: Creating 'slenderness_index'

New column preview:
   bill_length_mm  bill_depth_mm  slenderness_index
0            39.1           18.7           2.090909
1            39.5           17.4           2.270115
2            40.3           18.0           2.238889
3             0.0            0.0                NaN
4            36.7           19.3           1.901554


```

### Output Explanation
From above output you can see that the script is working correctly.
For example in row numbered 0 we have 39.1/18.7 =  2.090909
And in row numbered 3 we have 0.0/0.0 = NaN (Not infinity)



## PHASE 3: DELETING COLUMNS

### STEP 3.1: Using `.drop()` with Reassignment

### Purpose

To remove columns safely without modifying original DataFrame

----------

### Method

>`df.drop(columns=['col'])`

Signature

>`DataFrame.drop(labels=None, axis=0, columns=None, inplace=False)`

----------

## STEP 3.2: Using `del`

### Purpose

To remove column permanently (in-place)

----------

### Method

`del  df['col']`

----------

### Behavior

| Feature | Result |
| --- | --- |
| Returns | Nothing |
| Effect | Permanent |

## STEP 3.3: Using `.drop(inplace=True)`

### Purpose

To modify DataFrame directly

----------

### Method

>`df.drop(columns=['col'], inplace=True)`

----------

### Comparison

| Approach | Safe | Recommended |
| --- | --- | --- |
| `inplace=True` | Less | Avoid |
| `reassignment` | Yes | Preferred |

###  Error

`df.drop(columns=['col']) # No effect`


### Script for PHASE 3

```python

# ==========================================================
# PHASE 3: DELETING COLUMNS
# ==========================================================

print("\nPHASE 3: DELETING COLUMNS")

# ----------------------------------------------------------
# STEP 3.1: Using drop() with Reassignment
# ----------------------------------------------------------
print("\nSTEP 3.1: Using drop() with reassignment")

cols_to_remove = ['sex']  # We will only remove 'sex' here, leaving 'island' for the next step.

# drop() returns a new DataFrame with the specified columns removed, so we need to assign it back to a variable.
df_reassigned = df.drop(columns=cols_to_remove)

print(f"Does Original df have column for 'sex'?->: {'sex' in df.columns}") # True, because we haven't modified the original df yet.
print(f"Does df_reassigned have column for 'sex'?->: {'sex' in df_reassigned.columns}") # False, because we dropped 'sex' in df_reassigned. 


# ----------------------------------------------------------
# STEP 3.2: Using del (In-place Deletion)
# ----------------------------------------------------------
print("\nSTEP 3.2: Using del")

# 'del' permanently modifies the DataFrame
del df_reassigned['island']  # This will remove the 'island' column from df_reassigned permanently.

print(f"Has column 'island' been removed using del? -> {'island' not in df_reassigned.columns}")  # True, because 'island' has been deleted from df_reassigned.

# ERROR EXAMPLE: Using del on a non-existing column will raise a KeyError.
# del df['non_existing_column']


# ----------------------------------------------------------
# STEP 3.3: Using drop() with inplace=True
# ----------------------------------------------------------
print("\nSTEP 3.3: Using drop() with inplace=True")
# inplace=True modifies the DataFrame directly, so we don't need to assign it back to df_reassigned.
df_reassigned.drop(columns=['species'], inplace=True)

print(f"Has column 'species' been removed using inplace? -> {'species' not in df_reassigned.columns}")  # True, because 'species' has been deleted from df_reassigned.

# ERROR EXAMPLE: Using drop() without assignment or inplace=True will have no effect.
# df.drop(columns=['col'])  # No assignment → no effect


```

### Output for PHASE 3

```python

PHASE 3: DELETING COLUMNS

STEP 3.1: Using drop() with reassignment
Does Original df have column for 'sex'?->: True
Does df_reassigned have column for 'sex'?->: False

STEP 3.2: Using del
Has column 'island' been removed using del? -> True

STEP 3.3: Using drop() with inplace=True
Has column 'species' been removed using inplace? -> True

```

### Explanation of output

STEP 3.1 -> `.drop()` does NOT modify original. Creates new DataFrame


STEP 3.2 -> `'island'` removed from df_reassigned. Change is permanent

STEP 3.3-> `.drop(inplace=True)` directly modifies df_reassigned. No new object created

## PHASE 4: SORTING DATA


### STEP 4.1: Single Column Sorting

#### Purpose

To rank data

----------

### Method

`df.sort_values(by='column', ascending=False)`

### Signature

`DataFrame.sort_values(by, ascending=True)`

----------

### STEP 4.2: Multi-Column Sorting

### Purpose

To perform hierarchical sorting

----------

#### Method

`df.sort_values(by=[col1, col2], ascending=[True, False])`

----------

#### Logic

1.  Sort by species (A–Z)
2.  Within species → sort by mass (descending)

----------

### Filtering

`df[df['species'] ==  'Adelie']`

----------

### Error

`df.sort_values(by='wrong_column')`



### Script for PHASE 4

```python

# ==========================================================
# PHASE 4: SORTING DATA
# ==========================================================

print("\nPHASE 4: SORTING DATA")

# NOTE:
# Sorting is performed on original df to preserve all columns


# ----------------------------------------------------------
# STEP 4.1: Single Column Sorting
# ----------------------------------------------------------
print("\nSTEP 4.1: Sorting by single column")

# Sort by body mass (descending)
df_heaviest = df.sort_values(by='body_mass_g', ascending=False)

print("\nTop 3 heaviest penguins:")
# This will show the top 3 rows of the DataFrame sorted by body mass in descending order, 
# which corresponds to the 3 heaviest penguins.
print(df_heaviest[['species', 'body_mass_g']].head(3))


# ----------------------------------------------------------
# STEP 4.2: Multi-Column Sorting
# ----------------------------------------------------------
print("\nSTEP 4.2: Sorting by multiple columns")

# Sort by species (ascending) and then by body mass (descending)
# This will sort the DataFrame first by 'species' in alphabetical order, and then within each species, 
# it will sort by 'body_mass_g' from heaviest to lightest. 
sort_criteria = ['species', 'body_mass_g']  # 
ascending_rules = [True, False]  # True for species (A-Z), False for body mass (heaviest to lightest)

df_sorted_complex = df.sort_values(by=sort_criteria, ascending=ascending_rules)

# Filter Adelie penguins
# After sorting, we filter the DataFrame to only include rows where the 'species' column is 'Adelie'.
adelies = df_sorted_complex[df_sorted_complex['species'] == 'Adelie']

print("\nLast 3 Adelie penguins (sorted by mass):")
# This will show the last 3 rows of the filtered DataFrame, which corresponds to the 
# 3 lightest Adelie penguins due to the sorting order because we had earlier sorted by body mass in descending order.
# So lightest Adelie penguins will be at the end of the Adelie group in the sorted DataFrame.
print(adelies[['species', 'body_mass_g', 'island']].tail(3))

# ERROR EXAMPLE: Sorting by a non-existing column will raise a KeyError.
# df.sort_values(by='non_existing_column')

```

### Output for PHASE 4

```python

PHASE 4: SORTING DATA

STEP 4.1: Sorting by single column

Top 3 heaviest penguins:
    species  body_mass_g
237  Gentoo       6300.0
253  Gentoo       6050.0
297  Gentoo       6000.0

STEP 4.2: Sorting by multiple columns

Last 3 Adelie penguins (sorted by mass):
   species  body_mass_g     island
58  Adelie       2850.0     Biscoe
64  Adelie       2850.0     Biscoe
3   Adelie          0.0  Torgersen


```

### Explanation of OUTPUT

STEP 4.1: Single Column Sorting. Sorted by body_mass_g (descending). Top rows = heaviest penguins

STEP 4.2: Multi-Column Sorting. Sort by: 1. species (A–Z) then by 2. body_mass_g (descending)

Sub-step 4.2.2: Filtering. Select only Adelie rows

Sub-step 4.2.3: .tail(3). Last 3 rows → lightest Adelie penguins


#### Important Observation
body_mass_g = 0.0. This comes from: `fillna(0)`

So: Originally missing value → now appears as lightest penguin

#### Important Hidden Lesson
Filling missing values with 0 can mislead analysis.

>**Example from output: 0.0 body mass appears as lightest penguin, but is actually missing data**

----------

## STEP 5: SUMMARY

### Purpose

To reinforce key concepts

----------

## MASTER COMPARISON TABLE


| Operation | Method | Returns New? | Risk |
| --- | --- | --- | --- |
| Add Column | `df['new']` | No | Division errors |
| Drop | `.drop()` | Yes | No assignment |
| Delete | `del` | No | Permanent |
| Inplace | `.drop(inplace=True)` | No | Hard to debug |
| Sort | `.sort_values()` | Yes | Wrong column |


## COMMON ERRORS SUMMARY

| Error | Cause |
| --- | --- |
| KeyError | Wrong column name |
| No change | No assignment |
| inf values | Division by zero |
| Wrong output | Sorting misunderstanding |


### Script for PHASE 5

```python

# ==========================================================
# STEP 5: SUMMARY
# ==========================================================

print("\nSTEP 5: SUMMARY")

print("""
KEY LEARNINGS:

1. New columns can be derived using arithmetic operations
2. Columns can be deleted using drop() or del
3. inplace=True modifies the DataFrame directly
4. Sorting helps organize and analyze data efficiently

BEST PRACTICE:

- Prefer reassignment over inplace for clarity
- Always check column names before operations
- Handle missing values thoughtfully (avoid blind fillna(0))
""")

```

### Output for PHASE 5


```python
STEP 5: SUMMARY

KEY LEARNINGS:

1. New columns can be derived using arithmetic operations
2. Columns can be deleted using drop() or del
3. inplace=True modifies the DataFrame directly
4. Sorting helps organize and analyze data efficiently

BEST PRACTICE:

- Prefer reassignment over inplace for clarity
- Always check column names before operations
- Handle missing values thoughtfully (avoid blind fillna(0))


```














