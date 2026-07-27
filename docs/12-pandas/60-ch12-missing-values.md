# Project: Handling Missing Values in Pandas using Palmer Penguins Dataset

## Project: Handling Missing Values in Pandas using Palmer Penguins Dataset

***

### Research Question

> **How can missing data in a real-world dataset such as the Palmer Penguins dataset be identified, analyzed, and handled using Pandas techniques like `.isna()`, `.dropna()`, and `.fillna()`, and what are the conceptual and practical trade-offs between dropping and imputing missing values?**

***

### Task / Project Description

You are required to:

1. Identify missing values in the dataset
2. Quantify and analyze missing data
3. Apply strategies to handle missing data:
   * Dropping missing values
   * Filling (imputing) missing values
4. Compare different strategies (Mean, Median, Mode)
5. Understand when to use each method
6. Document findings with:
   * Code and comments
   * Tables
   * Flowcharts

### How to handle missing data

Data is real world is not perfect. So when you see missing values or wrong values in a dataset, you have 2 options

* Drop that data row/ or column containing the missing/ wrong data
* Fill up the missing data with some value (What you should fill would depend upon the data and your understanding of the data. It could be mean if the data is numeric or mode if the data is categorical etc)
* Dropping data has its consequences. Especially if you are dropping columns, you should be aware that it would reduce the "features" of your data set. Similarly dropping rows can also have consequences. It could create a "bias" in the data set

The following flow chart shows how missing data may be handled depending upon whether it is small or large (Few or many):

![Missing data small/ large](../.gitbook/assets/ch12-missing-data-small-large.png)

### 1. Important Methods with Signatures

***

#### 1. (A) `.isna()`

`df.isna()`

* Returns: Boolean DataFrame
* Limitation: Needs aggregation for counts

***

#### 1. (B) `.dropna(axis = 0)` for `axis =0`

`df.dropna(axis=0, how='any')`

* `axis=0` → rows
* `axis=1` → columns
* `how='any'` or `'all'`
* Returns: New DataFrame

**Pandas removes the entire row even if just one value in that row is missing.**

**When you run:**

`df_drop_rows = df.dropna()`

Pandas applies the default behavior:

`df.dropna(axis=0, how='any')`

**Interpretation:**

* `axis=0` → operate on **rows**
* `how='any'` → if **any column in a row has NaN**, drop that row

> Row is treated as a unit. If any part is incomplete, the whole row is removed. You may lose a lot of data unintentionally In real datasets (like penguins), many rows have at least one missing value. So, you need to be careful and know the consequences of using `.dropna()`

***

#### 1. (C) `.dropna(axis = 1)` for axis =1

**When you run:**

`df_drop_cols = df.dropna(axis=1)`

Pandas internally treats it as:

`df.dropna(axis=1, how='any')`

***

**Interpretation**

* `axis=1` → operate on **columns**
* `how='any'` → if **any row in a column has NaN**, drop that column

> In `.dropna(axis=1)` Column is treated as a unit. If any value is missing anywhere in that column, the whole column is removed.

**Why this is risky**

In real datasets (like Penguins):

* Many columns have at least one missing value
* Using this blindly may **remove most of your dataset**

**For example:**

* `sex` column has missing values → will be dropped
* numeric columns may also be dropped if any NaN exists

#### 1. (D) `.fillna()`

`df.fillna(value)`

* Input: scalar, dict, or method
* Returns: New DataFrame
* Limitation: May introduce bias

### 2. Conceptual Understanding

#### Identifying Missing Values

| Method    | Description           | Output            |
| --------- | --------------------- | ----------------- |
| .isna()   | Detect missing values | Boolean DataFrame |
| .isnull() | Same as .isna()       | Boolean DataFrame |
| .sum()    | Count missing values  | Series            |

***

#### Dropping vs Filling

| Aspect     | Dropping (dropna)  | Filling (fillna)   |
| ---------- | ------------------ | ------------------ |
| Data Loss  | High               | Low                |
| Simplicity | Easy               | Moderate           |
| Bias Risk  | Low                | Possible           |
| Use Case   | Small missing data | Large missing data |

***

#### Imputation Techniques

| Method | Suitable For     | Advantage         | Limitation           |
| ------ | ---------------- | ----------------- | -------------------- |
| Mean   | Numeric data     | Simple            | Affected by outliers |
| Median | Numeric data     | Robust            | Ignores distribution |
| Mode   | Categorical data | Works for strings | May be ambiguous     |

## Script (in steps) and explanation of each step

The following script shows how these methods work. The script is in 6 steps. Each of the 6 steps are discussed below seperately and then finally a combined script of all the 6 steps is given. For each step first the theoretical portion is explained and then the actual script dealing with that part is discusses. The flow chart of these 6 steps is as shown in the diagram below:-

![Script flow chart- Missing data](../.gitbook/assets/ch12-handling-missing-data-script-6steps.png)

### STEP 1: IMPORT LIBRARIES AND LOAD DATASET

***

#### Why this step is done

This step prepares the environment for data analysis.\
Before performing any operation on data, the required libraries must be loaded and the dataset must be brought into a Pandas DataFrame.

Without this step, no further data inspection, cleaning, or analysis is possible.

***

#### How it is done

* The `pandas` library is imported for data manipulation
* The `seaborn` library is used to load the Palmer Penguins dataset
* The dataset is stored in a DataFrame (`df`)

***

#### What to do

* Use standard aliases:
  * `import pandas as pd`
  * `import seaborn as sns`
* Load dataset once and reuse it
* Display initial rows using `head()`
* Check shape using `.shape` to understand size

***

#### What not to do

* Avoid reloading dataset multiple times
* Avoid modifying original dataset without creating a copy
* Avoid skipping initial inspection

***

#### Important Features / Sub-steps

* Import libraries
* Load dataset
* Store in DataFrame
* Perform initial inspection (`head()`, `shape`)

***

#### Methods / Attributes

***

**`sns.load_dataset(name)`**

`df = sns.load_dataset("penguins")`

* **Input:** Dataset name (string)
* **Output:** Pandas DataFrame
* **Use:** Loads built-in dataset

***

**`df.head(n=5)`**

`df.head()`

* **Input:** Number of rows (optional)
* **Output:** First `n` rows
* **Use:** Quick inspection

***

**`df.shape`**

`df.shape`

* **Output:** Tuple `(rows, columns)`
* **Use:** Understand dataset size

***

#### Limitations

* `sns.load_dataset()` may require internet access in some environments
* `head()` shows only a small sample, not full dataset
* Initial inspection does not reveal deeper data issues

***

#### Role of Step 1

> “The first step in any data analysis task is to load the dataset and understand its basic structure, as this forms the foundation for all subsequent operations.”

#### Script for Step 1

```python

# STEP 1: IMPORT LIBRARIES AND LOAD DATASET
print("\n STEP 1. IMPORT LIBRARIES AND LOAD DATASET")

import pandas as pd
import seaborn as sns

df = sns.load_dataset("penguins")
# The dataset contains information about penguins, including their species, island, bill length, 
# bill depth, flipper length, body mass, and sex

print("\n--- FIRST 5 ROWS OF ORIGINAL DATAFRAME ---")
print(df.shape)  # (344, 7) - 344 rows and 7 columns
print("df.head()->", df.head())  # First 5 rows of the original DataFrame.

```

**Output for Step 1**

```python
STEP 1. IMPORT LIBRARIES AND LOAD DATASET

--- FIRST 5 ROWS OF ORIGINAL DATAFRAME ---
(344, 7)
df.head()->   species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g     sex
0  Adelie  Torgersen            39.1           18.7              181.0       3750.0    Male
1  Adelie  Torgersen            39.5           17.4              186.0       3800.0  Female
2  Adelie  Torgersen            40.3           18.0              195.0       3250.0  Female
3  Adelie  Torgersen             NaN            NaN                NaN          NaN     NaN
4  Adelie  Torgersen            36.7           19.3              193.0       3450.0  Female

```

### STEP 2: IDENTIFYING MISSING VALUES

***

#### Why this step is done

Before cleaning data, it is essential to **detect and quantify missing values**. Without this step, any cleaning strategy would be uninformed and potentially harmful.

***

### 2(A) `.isna()` – Detect Missing Values

#### What it does

Creates a Boolean DataFrame:

* `True` → Missing value
* `False` → Present value

#### How it is done

`df.isna()`

#### Output

* Same shape as original DataFrame
* Boolean values

***

#### What to do

* Use `.head()` to avoid large output
* Use it for visual inspection

#### What not to do

* Avoid printing full DataFrame for large datasets

***

#### Method Signature

DataFrame.isna()

* **Input:** None
* **Output:** DataFrame (Boolean)
* **Limitation:** Does not give counts directly

#### Script for 2(A)

```python
# 2(A) Use .isna() to check missing values (True -> missing, False -> not missing)
print("\nMissing values (True/False):->")
# .isna() detects missing values in the DataFrame and returns a DataFrame of the same shape as df, where each 
# cell contains True if the original cell in df is NaN (missing) and False otherwise.   
print("df.isna().head()->", df.isna().head()) 
# This allows us to quickly see which values are missing in the dataset. 
# For example, if the 'bill_length_mm' column has a missing value in the 4th row, the corresponding cell 
# in the output will show True for that position. 

```

#### Output for Step 2(A)

```python
Missing values (True/False):->
df.isna().head()->    species  island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g    sex
0    False   False           False          False              False        False  False
1    False   False           False          False              False        False  False
2    False   False           False          False              False        False  False
3    False   False            True           True               True         True   True
4    False   False           False          False              False        False  False

```

### 2(B) `.isna().sum()` – Count Missing Values

#### Why

To quantify missing data per column

#### How

`df.isna().sum()`

> This is **method chaining**

***

#### Output

* Pandas Series
* Index → column names
* Values → count of missing values

***

#### Method Signatures

`df.isna() # Assume df is a DataFrame`

* Returns a **DataFrame of the same shape**
* Each value is:
  * `True` → if original value is missing (NaN)
  * `False` → if value is present

`DataFrame.sum(axis=0)` This tells us:

* Method name → `sum`
* Parameter → `axis`
* Default value → `axis=0`

> The default value of `axis =0`. This means that if you dont give any value for axis parameter, it will take a default of `axis =0` and therefore add/ Sum down rows (column-wise). But you can override/ change this behavior by giving axis =1. This will add/ Sum across columns (row-wise).

| Parameter | Meaning                       |
| --------- | ----------------------------- |
| axis=0    | Sum down rows (column-wise)   |
| axis=1    | Sum across columns (row-wise) |

***

#### Limitations

* Works column-wise by default
* Requires understanding Boolean arithmetic

***

#### Script for 2(B)

```python
# 2(B) Use .isna().sum() to count missing values per column
# We are "method chaining" .isna() with .sum() to get a count of how many missing values are in each column.
# The result is a Series where the index is the column names and the values are the count of missing values 
# in each column.
print("\nMissing values count per column:->")
print("df.isna().sum()->", df.isna().sum())
# This shows how many missing values are in each column. For example, if 'body_mass_g' has 2 missing values, 
# it will show 2 for that column.

```

#### Output for Step 2(B)

```python
Missing values count per column:->
df.isna().sum()-> species               0
island                0
bill_length_mm        2
bill_depth_mm         2
flipper_length_mm     2
body_mass_g           2
sex                  11
dtype: int64

```

### 2(C) `.isnull()`

#### Why

Alternative to `.isna()`

#### Key Point

> `.isnull()` and `.isna()` are identical

#### Script for 2(C)

```python
# 2(C) Use .isnull() to check missing values (same as .isna())
print("\nUsing isnull():->")
# We are "method chaining" .isnull() with .sum() to confirm that it gives the same result as .isna().
print("df.isnull().sum()->", df.isnull().sum())
# Output will be the same as using isna(), confirming that both methods are interchangeable 
# for detecting missing values.

```

#### Output for Step 2(C)

```python
Using isnull():->
df.isnull().sum()-> species               0
island                0
bill_length_mm        2
bill_depth_mm         2
flipper_length_mm     2
body_mass_g           2
sex                  11
dtype: int64

```

### STEP 3: DROPPING MISSING VALUES

#### Why this step is done

To remove incomplete data when missing values are small or insignificant.

***

### 3(A) Drop Rows → `.dropna(axis=0)`

#### How

`df.dropna(axis=0)`

***

#### Meaning

* Remove row if **any value is missing**

***

#### Signature

`DataFrame.dropna(axis=0, how='any', subset=None)`

* **`axis=0`** → rows (This is the default value.)
* **`how='any'`** → default

***

#### Limitations

* Can remove large amount of data
* May introduce bias

***

#### What to do

* Check `.shape` before and after

#### What not to do

* Avoid blind usage

***

#### Script for Step 3(A)

```python
# 3(A) Use .dropna(axis=0) to drop ROWS with any missing value
df_drop_rows = df.dropna(axis=0)  # axis = 0 means we are dropping rows. 
# This will remove any row that contains at least one NaN value. 
# If a row has missing data in any column, that row will be dropped from the resulting DataFrame.

print("\nAfter dropping rows with missing values:")
print("df_drop_rows.shape->", df_drop_rows.shape)  # (311, 7) - Earlier was (344, 7)
# So 344-311 = 33 rows were dropped because they contained at least one missing value.
# Shows the new shape of the DataFrame after dropping rows
print("df_drop_rows.head()->", df_drop_rows.head())  # Displays the first 5 rows of the new DataFrame to confirm that rows with missing values have been removed
# All rows in this new DataFrame should have complete data with no NaN values.

```

#### Output for Step 3(A)

```python
After dropping rows with missing values:
df_drop_rows.shape-> (333, 7)
df_drop_rows.head()->   species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g     sex
0  Adelie  Torgersen            39.1           18.7              181.0       3750.0    Male
1  Adelie  Torgersen            39.5           17.4              186.0       3800.0  Female
2  Adelie  Torgersen            40.3           18.0              195.0       3250.0  Female
4  Adelie  Torgersen            36.7           19.3              193.0       3450.0  Female
5  Adelie  Torgersen            39.3           20.6              190.0       3650.0    Male

```

### 3(B) Drop Columns → `.dropna(axis=1)`

#### How

`df.dropna(axis=1)`

***

#### Meaning

* Remove column if **any value is missing**

***

#### Limitations

* May remove important features
* Very aggressive

***

#### Important Parameters

`df.dropna(axis=1, how='all', thresh=n)`

| Parameter | Meaning                          |
| --------- | -------------------------------- |
| how='all' | Drop only if all values missing  |
| thresh    | Minimum non-null values required |

#### Script for Step 3(B)

```python
# 3(B) Use .dropna(axis=1) to drop COLUMNS with any missing value
df_drop_cols = df.dropna(axis=1)  # axis = 1 means we are dropping columns. 
# This will remove any column that contains at least one NaN value. 
# If a column has missing data in any row, that column will be dropped from the resulting DataFrame.

print("\nAfter dropping columns with missing values:")
print("df_drop_cols.shape->", df_drop_cols.shape)  # (344, 5) - Earlier was (344, 7)
# So 7-5 = 2 columns were dropped because they contained at least one missing value.
# Shows the new shape of the DataFrame after dropping columns
# The dropped columns are likely 'bill_length_mm' and 'body_mass_g' since they had missing values.
print("df_drop_cols.head()->", df_drop_cols.head())  # Displays the first 5 rows of the new DataFrame to confirm that columns with missing values have been removed
print("df_drop_cols.columns->", df_drop_cols.columns)  # Displays the remaining columns after dropping those with missing values


```

#### Output for Step 3(B)

```python

After dropping columns with missing values:
df_drop_cols.shape-> (344, 2)
df_drop_cols.head()->   species     island
0  Adelie  Torgersen
1  Adelie  Torgersen
2  Adelie  Torgersen
3  Adelie  Torgersen
4  Adelie  Torgersen
df_drop_cols.columns-> Index(['species', 'island'], dtype='object')

```

### STEP 4: FILLING MISSING VALUES (IMPUTATION)

***

#### Why this step is done

To **preserve data** instead of removing it

***

### 4(A) Mean Imputation

#### How

`df['col'].fillna(df['col'].mean())`

***

#### Use Case

* Numeric data
* No extreme outliers

***

#### Limitation

* Affected by outliers

***

#### Script for Step 4(A)

```python
# 4(A) Fill numeric columns with mean
df_mean = df.copy()  # Create a copy of the original DataFrame to avoid modifying it directly
mean_value = df_mean['body_mass_g'].mean()  # Calculate the mean of the 'body_mass_g' column
print("\nMean of body_mass_g:->", mean_value)  # Displays the mean value of the 'body_mass_g' column
df_mean['body_mass_g'] = df_mean['body_mass_g'].fillna(mean_value)
# This will replace all NaN values in the 'body_mass_g' column with the mean of that column.

print("\nFilled with mean:")
print("df_mean['body_mass_g'].isna().sum()->", df_mean['body_mass_g'].isna().sum())

```

#### Output for Step 4(A)

```python
Mean of body_mass_g:-> 4201.754385964912

Filled with mean:
df_mean['body_mass_g'].isna().sum()-> 0

```

### 4(B) Median Imputation

#### How

`df['col'].fillna(df['col'].median())`

***

#### Use Case

* Skewed data

***

#### Advantage

* Robust to outliers

***

### 4(C) Mode Imputation

#### How

`df['col'].fillna(df['col'].mode()[0])`

***

#### Use Case

* Categorical data

***

#### Limitation

* Multiple modes possible

***

#### Method Signature

`DataFrame.fillna(value)` `Series.fillna(value)`

* **Input:** scalar / Series / dict
* **Output:** New object

***

#### Important Concept

> `fillna()` does NOT modify original DataFrame unless assigned

#### Script for Step 4(C)

```python
# 4(C) Fill categorical columns with mode
df_mode = df.copy()  # Create a copy of the original DataFrame to avoid modifying it directly
mode_value = df_mode['sex'].mode()[0]  # Calculate the mode of the 'sex' column. mode() returns a Series, so we take the first element [0] to get the actual mode value.
print("\nMode of sex:->", mode_value)
df_mode['sex'] = df_mode['sex'].fillna(mode_value)
# This will replace all NaN values in the 'sex' column with the mode of that column.

print("\nFilled with mode:")
print("df_mode['sex'].isna().sum()->", df_mode['sex'].isna().sum())

```

#### Output for Step 4(C)

```python
Mode of sex:-> Male

Filled with mode:
df_mode['sex'].isna().sum()-> 0

```

### STEP 5: ERROR DEMONSTRATIONS

***

#### Why this step is done

The purpose of this step is to know **what not to do**, and improving debugging skills

***

#### Common Errors

***

#### 5(A) Wrong Imputation Type

`# df['sex'].mean()`

Mean cannot be applied to categorical data

**The problem**

The problem is attempting to compute the **mean** of a column (`sex`) and use it for filling missing values.

***

**Why this is wrong**

**1. Nature of Data**

* `sex` is a **categorical column** (e.g., `'male'`, `'female'`)
* Mean requires **numeric data**

***

**2. What “mean” actually means**

```
$$
Mean = \frac{Sum of Values}{Number of Values}
$$.
```

> This only works for numbers, not text

***

**3. What happens internally**

`df['sex'].mean()`

Pandas tries to:

* Add values → `'male' + 'female'` (invalid)
* Divide result → Error

Leads to:

`TypeError: Could not convert string to numeric`

***

**Correct Approach\*\***

Use **mode (most frequent value)**:

`df['sex'].fillna(df['sex'].mode()[0])`

***

#### 5(B) Logical Misunderstanding

`# df.dropna(axis=1, how='all')`

Beginners often misunderstand behavior

**5(B) Logical Misunderstanding**

`# df.dropna(axis=1, how='all')`

***

**The confusion is they often believe:**

> “This will drop all columns that have missing values”

***

**Actual meaning**

`df.dropna(axis=1, how='all')`

> Drops a column **ONLY IF ALL values in that column are missing**

***

**Example**

```python
A: [1, 2, 3] →  kept    
B: [NaN, NaN, NaN] →  dropped    
C: [1, NaN, 3] →  kept
```

### **Why confusion happens**

The following table explains why confusion happens:

| Parameter   | Meaning                    |
| ----------- | -------------------------- |
| `how='any'` | Drop if ANY value missing  |
| `how='all'` | Drop if ALL values missing |

If you wanted to remove columns with missing values: USE

`df.dropna(axis=1) # correct for that intention`

But if instead you wrote:

`df.dropna(axis=1, how='all')`

**Almost nothing gets removed**

***

#### 5(C) Not Assigning Result

`# df.fillna(0)`

No change occurs

**5(C) Not Assigning Result**

`# df.fillna(0)`

***

**What you might expect**

You might think:

> “This will replace all missing values with 0 in the DataFrame”

***

**What actually happens**

> Nothing changes in `df`

***

**Why?**

Most Pandas methods:

* Do NOT modify the original DataFrame
* Return a **new modified copy**

***

**Internally:**

`df.fillna(0)`

> Creates a **new DataFrame**, but you are **not storing it**

***

**Correct Ways**

**Method 1: Assign back**

`df = df.fillna(0)`

***

**Method 2: Use inplace**

`df.fillna(0, inplace=True)`

#### Script for Step 5 (Errors: Commented out)

```python

# STEP 5: ERROR DEMONSTRATIONS (COMMENTED OUT)
print("\n STEP 5. ERROR DEMONSTRATIONS (COMMENTED OUT)")

# 5(A) ERROR 1: Filling string column with mean
# df['sex'].fillna(df['sex'].mean())

# 5(B) ERROR 2: Dropping all data accidentally
# df.dropna(axis=1, how='all')

# 5(C) ERROR 3: Not assigning result back
# df.fillna(0)  # No effect unless assigned

```

### STEP 6: SUMMARY

***

#### Why this step is done

To reinforce:

* Concepts
* Best practices
* Decision-making

***

#### Script for Step 6

```python
# STEP 6: SUMMARY
print("\n STEP 6. SUMMARY")


print("""
KEY LEARNINGS:

1. Use isna() or isnull() to detect missing values
2. dropna() removes missing data
3. fillna() replaces missing data
4. Mean/Median for numeric data
5. Mode for categorical data
6. Always analyze before choosing method

BEST PRACTICE:
Understand the data before cleaning it
""")

```

#### The output of Step 6

It is just a long print giving summary of all the steps in the script

## The entire script in a single block:-

```python
"""
PROJECT: Handling Missing Values in Pandas
DATASET: Palmer Penguins

OBJECTIVE:
1. Identify missing values
2. Drop missing values
3. Fill missing values (mean, median, mode)
4. Compare strategies

NOTE:
This script is written with detailed comments for teaching purposes.
"""

# STEP 1: IMPORT LIBRARIES AND LOAD DATASET
print("\n STEP 1. IMPORT LIBRARIES AND LOAD DATASET")

import pandas as pd
import seaborn as sns

df = sns.load_dataset("penguins")
# The dataset contains information about penguins, including their species, island, bill length, 
# bill depth, flipper length, body mass, and sex

print("\n--- FIRST 5 ROWS OF ORIGINAL DATAFRAME ---")
print(df.shape)  # (344, 7) - 344 rows and 7 columns
print("df.head()->", df.head())  # First 5 rows of the original DataFrame.

# STEP 2: IDENTIFYING MISSING VALUES
print("\n STEP 2. IDENTIFYING MISSING VALUES")

# 2(A) Use .isna() to check missing values (True -> missing, False -> not missing)
print("\nMissing values (True/False):->")
# .isna() detects missing values in the DataFrame and returns a DataFrame of the same shape as df, where each 
# cell contains True if the original cell in df is NaN (missing) and False otherwise.   
print("df.isna().head()->", df.isna().head()) 
# This allows us to quickly see which values are missing in the dataset. 
# For example, if the 'bill_length_mm' column has a missing value in the 4th row, the corresponding cell 
# in the output will show True for that position. 

# 2(B) Use .isna().sum() to count missing values per column
# We are "method chaining" .isna() with .sum() to get a count of how many missing values are in each column.
# The result is a Series where the index is the column names and the values are the count of missing values 
# in each column.
print("\nMissing values count per column:->")
print("df.isna().sum()->", df.isna().sum())
# This shows how many missing values are in each column. For example, if 'body_mass_g' has 2 missing values, 
# it will show 2 for that column.

# 2(C) Use .isnull() to check missing values (same as .isna())
print("\nUsing isnull():->")
# We are "method chaining" .isnull() with .sum() to confirm that it gives the same result as .isna().
print("df.isnull().sum()->", df.isnull().sum())
# Output will be the same as using isna(), confirming that both methods are interchangeable 
# for detecting missing values.

# STEP 3: DROPPING MISSING VALUES

print("\n STEP 3. DROPPING MISSING VALUES")

# 3(A) Use .dropna(axis=0) to drop ROWS with any missing value
df_drop_rows = df.dropna(axis=0)  # axis = 0 means we are dropping rows. 
# This will remove any row that contains at least one NaN value. 
# If a row has missing data in any column, that row will be dropped from the resulting DataFrame.

print("\nAfter dropping rows with missing values:")
print("df_drop_rows.shape->", df_drop_rows.shape)  # (311, 7) - Earlier was (344, 7)
# So 344-311 = 33 rows were dropped because they contained at least one missing value.
# Shows the new shape of the DataFrame after dropping rows
print("df_drop_rows.head()->", df_drop_rows.head())  # Displays the first 5 rows of the new DataFrame to confirm that rows with missing values have been removed
# All rows in this new DataFrame should have complete data with no NaN values.

# 3(B) Use .dropna(axis=1) to drop COLUMNS with any missing value
df_drop_cols = df.dropna(axis=1)  # axis = 1 means we are dropping columns. 
# This will remove any column that contains at least one NaN value. 
# If a column has missing data in any row, that column will be dropped from the resulting DataFrame.

print("\nAfter dropping columns with missing values:")
print("df_drop_cols.shape->", df_drop_cols.shape)  # (344, 5) - Earlier was (344, 7)
# So 7-5 = 2 columns were dropped because they contained at least one missing value.
# Shows the new shape of the DataFrame after dropping columns
# The dropped columns are likely 'bill_length_mm' and 'body_mass_g' since they had missing values.
print("df_drop_cols.head()->", df_drop_cols.head())  # Displays the first 5 rows of the new DataFrame to confirm that columns with missing values have been removed
print("df_drop_cols.columns->", df_drop_cols.columns)  # Displays the remaining columns after dropping those with missing values


# STEP 4: FILLING MISSING VALUES (IMPUTATION)

print("\n STEP 4. FILLING MISSING VALUES (IMPUTATION)")

# 4(A) Fill numeric columns with mean
df_mean = df.copy()  # Create a copy of the original DataFrame to avoid modifying it directly
mean_value = df_mean['body_mass_g'].mean()  # Calculate the mean of the 'body_mass_g' column
print("\nMean of body_mass_g:->", mean_value)  # Displays the mean value of the 'body_mass_g' column
df_mean['body_mass_g'] = df_mean['body_mass_g'].fillna(mean_value)
# This will replace all NaN values in the 'body_mass_g' column with the mean of that column.

print("\nFilled with mean:")
print("df_mean['body_mass_g'].isna().sum()->", df_mean['body_mass_g'].isna().sum())

# 4(B) Fill numeric columns with median
df_median = df.copy()  # Create a copy of the original DataFrame to avoid modifying it directly
median_value = df_median['body_mass_g'].median()  # Calculate the median of the 'body_mass_g' column
print("\nMedian of body_mass_g:->", median_value)  # Displays the median value of the 'body_mass_g' column
df_median['body_mass_g'] = df_median['body_mass_g'].fillna(median_value)
# This will replace all NaN values in the 'body_mass_g' column with the median of that column.
print("\nFilled with median:")
print("df_median['body_mass_g'].isna().sum()->", df_median['body_mass_g'].isna().sum())

# 4(C) Fill categorical columns with mode
df_mode = df.copy()  # Create a copy of the original DataFrame to avoid modifying it directly
mode_value = df_mode['sex'].mode()[0]  # Calculate the mode of the 'sex' column. mode() returns a Series, so we take the first element [0] to get the actual mode value.
print("\nMode of sex:->", mode_value)
df_mode['sex'] = df_mode['sex'].fillna(mode_value)
# This will replace all NaN values in the 'sex' column with the mode of that column.

print("\nFilled with mode:")
print("df_mode['sex'].isna().sum()->", df_mode['sex'].isna().sum())


# STEP 5: ERROR DEMONSTRATIONS (COMMENTED OUT)
print("\n STEP 5. ERROR DEMONSTRATIONS (COMMENTED OUT)")

# 5(A) ERROR 1: Filling string column with mean
# df['sex'].fillna(df['sex'].mean())

# 5(B) ERROR 2: Dropping all data accidentally
# df.dropna(axis=1, how='all')

# 5(C) ERROR 3: Not assigning result back
# df.fillna(0)  # No effect unless assigned


# STEP 6: SUMMARY
print("\n STEP 6. SUMMARY")


print("""
KEY LEARNINGS:

1. Use isna() or isnull() to detect missing values
2. dropna() removes missing data
3. fillna() replaces missing data
4. Mean/Median for numeric data
5. Mode for categorical data
6. Always analyze before choosing method

BEST PRACTICE:
Understand the data before cleaning it
""")



```

### Combined output

```python

 STEP 1. IMPORT LIBRARIES AND LOAD DATASET

--- FIRST 5 ROWS OF ORIGINAL DATAFRAME ---
(344, 7)
df.head()->   species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g     sex
0  Adelie  Torgersen            39.1           18.7              181.0       3750.0    Male
1  Adelie  Torgersen            39.5           17.4              186.0       3800.0  Female
2  Adelie  Torgersen            40.3           18.0              195.0       3250.0  Female
3  Adelie  Torgersen             NaN            NaN                NaN          NaN     NaN
4  Adelie  Torgersen            36.7           19.3              193.0       3450.0  Female

 STEP 2. IDENTIFYING MISSING VALUES

Missing values (True/False):->
df.isna().head()->    species  island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g    sex
0    False   False           False          False              False        False  False
1    False   False           False          False              False        False  False
2    False   False           False          False              False        False  False
3    False   False            True           True               True         True   True
4    False   False           False          False              False        False  False

Missing values count per column:->
df.isna().sum()-> species               0
island                0
bill_length_mm        2
bill_depth_mm         2
flipper_length_mm     2
body_mass_g           2
sex                  11
dtype: int64

Using isnull():->
df.isnull().sum()-> species               0
island                0
bill_length_mm        2
bill_depth_mm         2
flipper_length_mm     2
body_mass_g           2
sex                  11
dtype: int64

 STEP 3. DROPPING MISSING VALUES

After dropping rows with missing values:
df_drop_rows.shape-> (333, 7)
df_drop_rows.head()->   species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g     sex
0  Adelie  Torgersen            39.1           18.7              181.0       3750.0    Male
1  Adelie  Torgersen            39.5           17.4              186.0       3800.0  Female
2  Adelie  Torgersen            40.3           18.0              195.0       3250.0  Female
4  Adelie  Torgersen            36.7           19.3              193.0       3450.0  Female
5  Adelie  Torgersen            39.3           20.6              190.0       3650.0    Male

After dropping columns with missing values:
df_drop_cols.shape-> (344, 2)
df_drop_cols.head()->   species     island
0  Adelie  Torgersen
1  Adelie  Torgersen
2  Adelie  Torgersen
3  Adelie  Torgersen
4  Adelie  Torgersen
df_drop_cols.columns-> Index(['species', 'island'], dtype='object')

 STEP 4. FILLING MISSING VALUES (IMPUTATION)

Mean of body_mass_g:-> 4201.754385964912

Filled with mean:
df_mean['body_mass_g'].isna().sum()-> 0

Median of body_mass_g:-> 4050.0

Filled with median:
df_median['body_mass_g'].isna().sum()-> 0

Mode of sex:-> Male

Filled with mode:
df_mode['sex'].isna().sum()-> 0

 STEP 5. ERROR DEMONSTRATIONS (COMMENTED OUT)

 STEP 6. SUMMARY

KEY LEARNINGS:

1. Use isna() or isnull() to detect missing values
2. dropna() removes missing data
3. fillna() replaces missing data
4. Mean/Median for numeric data
5. Mode for categorical data
6. Always analyze before choosing method

BEST PRACTICE:
Understand the data before cleaning it



```
