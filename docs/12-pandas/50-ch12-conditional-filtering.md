# Conditional Filtering in Pandas

## Research Question

> **How can conditional filtering techniques in Pandas (Boolean indexing, logical operators, `.isin()`, and string-based filtering using `.str.contains()`) be used to efficiently extract meaningful subsets of data from a real-world dataset such as the Palmer Penguins dataset, and what are their comparative advantages, limitations, and common sources of error?**

### PROJECT: Conditional Filtering in Pandas

DATASET: Palmer Penguins

> OBJECTIVE: To demonstrate:
>
> 1. Boolean indexing
> 2. Logical operators (&, |, \~)
> 3. .isin() method
> 4. .str.contains() for string filtering
> 5. Common errors and handling

***

## Task / Project Description

You are required to:

1. Load and explore the **Palmer Penguins dataset**
2. Apply **basic Boolean filtering**
3. Combine multiple conditions using:
   * `&` (AND)
   * `|` (OR)
   * `~` (NOT)
4. Use `.isin()` for filtering multiple values
5. Use `.str.contains()` for string-based filtering
6. Identify and handle **common errors**
7. Present findings using:
   * Tables
   * Code with comments
   * Flowcharts

***

## Solution

### STEP 0: Import Libraries and Load Dataset

**Why this step is done**

This step initializes the working environment. Without loading the required libraries and dataset, no data analysis can be performed.

**How it is done**

* Import `pandas` for data manipulation
* Import `seaborn` to access the Palmer Penguins dataset
* Load dataset into a DataFrame

**What to do**

* Use standard aliases (`pd`, `sns`)
* Ensure dataset loads correctly

**What not to do**

* Avoid reloading dataset multiple times unnecessarily
* Avoid modifying original dataset unintentionally

***

**Key Features / Sub-steps**

* Library import
* Dataset loading
* Initial inspection (`head()` optional)

***

**Methods / Attributes**

**`sns.load_dataset(name)`**

* **Input:** Dataset name (string)
* **Output:** Pandas DataFrame
* **Limitation:** Requires internet (in some environments)

#### Script for implementing STEP 0

```python
# STEP 0: IMPORT LIBRARIES AND LOAD DATASET
print("\n STEP 0. IMPORT LIBRARIES AND LOAD DATASET")
import pandas as pd
import seaborn as sns

df = sns.load_dataset("penguins")

print("\n--- FIRST 5 ROWS ---")
print("df.head()->", df.head())  # Display the first 5 rows of the dataset to understand its structure and columns

```

**Output**

```python
 STEP 0. IMPORT LIBRARIES AND LOAD DATASET

--- FIRST 5 ROWS ---
df.head()->   species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g     sex
0  Adelie  Torgersen            39.1           18.7              181.0       3750.0    Male
1  Adelie  Torgersen            39.5           17.4              186.0       3800.0  Female
2  Adelie  Torgersen            40.3           18.0              195.0       3250.0  Female
3  Adelie  Torgersen             NaN            NaN                NaN          NaN     NaN
4  Adelie  Torgersen            36.7           19.3              193.0       3450.0  Female

```

### STEP 1: Basic Boolean Indexing\*\*

**Why this step is done**

Boolean indexing is the **foundation of filtering**. It allows selection of rows based on conditions.

**How it is done**

A condition is applied to a column, producing `True/False`, which filters rows.

***

**What to do**

* Use clear conditions
* Ensure correct column names

**What not to do**

* Avoid mixing data types improperly
* Avoid forgetting brackets

***

**Key Features**

* Produces Boolean Series
* Filters rows directly

***

**Methods / Syntax**

`df[condition]`

**Example:**

`df[df['body_mass_g'] > 4000]`

* **Input:** Boolean Series
* **Output:** Filtered DataFrame
* **Limitation:** Cannot handle multiple conditions without operators

#### Script for Step 1

```python
# STEP 1: BASIC BOOLEAN INDEXING
print("\n STEP 1. BASIC BOOLEAN FILTERING")

# Filter penguins with body mass greater than 4000 grams
# This creates a Boolean Series where True indicates rows that satisfy the condition
heavy_penguins = df[df['body_mass_g'] > 4000]  

print("\nPenguins with body_mass_g > 4000:")
print("heavy_penguins.head()->", heavy_penguins.head())

# Explanation:
# df['body_mass_g'] > 4000 creates a Boolean Series (True/False)
# Pandas uses this to filter rows

```

**Output**

```python
 STEP 1. BASIC BOOLEAN FILTERING

Penguins with body_mass_g > 4000:
heavy_penguins.head()->    species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g   sex
7   Adelie  Torgersen            39.2           19.6              195.0       4675.0  Male
9   Adelie  Torgersen            42.0           20.2              190.0       4250.0   NaN
14  Adelie  Torgersen            34.6           21.1              198.0       4400.0  Male
17  Adelie  Torgersen            42.5           20.7              197.0       4500.0  Male
19  Adelie  Torgersen            46.0           21.5              194.0       4200.0  Male

```

### STEP 2: Combining Conditions

#### Why this step is done

Real-world filtering often requires **multiple conditions simultaneously**.

***

#### How it is done

Using:

* `&` → AND
* `|` → OR
* `~` → NOT

***

#### What to do

* Always use parentheses
* Use vectorized operators (`&`, `|`)

#### What not to do

* Do NOT use `and`, `or`
* Do NOT skip parentheses

***

#### Key Features

* Supports complex filtering
* Works element-wise

***

#### Operators

```python
# STEP 2: COMBINING CONDITIONS

print("\n STEP 2. COMBINING CONDITIONS")

# Condition using AND (&)
# To combine conditions, we use & for AND, | for OR, and ~ for NOT. 
# Each condition must be enclosed in parentheses.
cond_and = df[(df['body_mass_g'] > 4000) & (df['species'] == 'Adelie')]
print("\nAdelie penguins with body_mass_g > 4000:")
print("cond_and.head()->", cond_and.head())

# Condition using OR (|)
# This will filter penguins that are either Adelie OR Chinstrap, regardless of their body mass.
cond_or = df[(df['species'] == 'Adelie') | (df['species'] == 'Chinstrap')]
print("\nAdelie OR Chinstrap penguins:")
print("cond_or.head()->", cond_or.head())

# Condition using NOT (~)
# This will filter penguins that are NOT Adelie.
cond_not = df[~(df['species'] == 'Adelie')]
print("\nPenguins that are NOT Adelie:")
print("cond_not.head()->", cond_not.head())

# IMPORTANT:
# Always use parentheses around conditions

```

**Output**

```python
 STEP 2. COMBINING CONDITIONS

Adelie penguins with body_mass_g > 4000:
cond_and.head()->    species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g   sex
7   Adelie  Torgersen            39.2           19.6              195.0       4675.0  Male
9   Adelie  Torgersen            42.0           20.2              190.0       4250.0   NaN
14  Adelie  Torgersen            34.6           21.1              198.0       4400.0  Male
17  Adelie  Torgersen            42.5           20.7              197.0       4500.0  Male
19  Adelie  Torgersen            46.0           21.5              194.0       4200.0  Male

Adelie OR Chinstrap penguins:
cond_or.head()->   species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g     sex
0  Adelie  Torgersen            39.1           18.7              181.0       3750.0    Male
1  Adelie  Torgersen            39.5           17.4              186.0       3800.0  Female
2  Adelie  Torgersen            40.3           18.0              195.0       3250.0  Female
3  Adelie  Torgersen             NaN            NaN                NaN          NaN     NaN
4  Adelie  Torgersen            36.7           19.3              193.0       3450.0  Female

Penguins that are NOT Adelie:
cond_not.head()->        species island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g     sex
152  Chinstrap  Dream            46.5           17.9              192.0       3500.0  Female
153  Chinstrap  Dream            50.0           19.5              196.0       3900.0    Male
154  Chinstrap  Dream            51.3           19.2              193.0       3650.0    Male
155  Chinstrap  Dream            45.4           18.7              188.0       3525.0  Female
156  Chinstrap  Dream            52.7           19.8              197.0       3725.0    Male

```

### STEP 3: Using `.isin()`

#### Why this step is done

Used when filtering against **multiple values in a clean and readable way**.

***

#### How it is done

`df['column'].isin(list_of_values)`

***

#### What to do

* Use for multiple value checks
* Pass list or iterable

#### What not to do

* Avoid chaining multiple OR conditions unnecessarily

***

#### Key Features

* Cleaner than multiple ORs
* Efficient

***

#### Method

**`.isin(values)`**

* **Input:** List / iterable
* **Output:** Boolean Series
* **Limitation:** Exact match only (no partial matching)

```python
# STEP 3: USING .isin()

print("\n STEP 3. USING .isin() ================")
# Filter multiple species
# This will filter penguins that belong to either the 'Adelie' or 'Chinstrap' species.
species_filter = df[df['species'].isin(['Adelie', 'Chinstrap'])]

print("\nPenguins belonging to Adelie or Chinstrap:")
print("species_filter.head()->", species_filter.head())

# Explanation:
# .isin() checks membership in a list of values

```

**Output**

```python
 STEP 3. USING .isin() ================

Penguins belonging to Adelie or Chinstrap:
species_filter.head()->   species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g     sex
0  Adelie  Torgersen            39.1           18.7              181.0       3750.0    Male
1  Adelie  Torgersen            39.5           17.4              186.0       3800.0  Female
2  Adelie  Torgersen            40.3           18.0              195.0       3250.0  Female
3  Adelie  Torgersen             NaN            NaN                NaN          NaN     NaN
4  Adelie  Torgersen            36.7           19.3              193.0       3450.0  Female

```

### STEP 4: String Filtering using `.str.contains()`

#### Why this step is done

Used for filtering **text data and patterns**.

***

#### How it is done

`df['column'].str.contains(pattern)`

***

#### What to do

* Use `case=False` when needed
* Use `na=False` for missing values

#### What not to do

* Avoid applying on non-string columns

***

#### Key Features

* Supports regex
* Case-sensitive by default

***

#### Method

**`.str.contains(pattern, case=True, na=None)`**

* **Input:** String or regex
* **Output:** Boolean Series
* **Limitations:**
  * Fails with NaN unless handled
  * Slower than numeric filtering

```python
# STEP 4: STRING FILTERING USING .str.contains()

print("\n STEP 4. STRING FILTERING ================")

# Filter rows where island contains 'Dream'
# This will filter penguins that are from islands whose names contain the substring 'Dream'.
dream_island = df[df['island'].str.contains('Dream')]

print("\nPenguins from Dream island:")
print("dream_island.head()->", dream_island.head())

# Case-insensitive search
# This will filter penguins from islands that contain 'dream' in any case (e.g., 'Dream', 'dream', 'DREAM').
dream_case_insensitive = df[df['island'].str.contains('dream', case=False)]

print("\nCase-insensitive filtering:")
print("dream_case_insensitive.head()->", dream_case_insensitive.head())

```

### STEP 5: Handling Missing Values in String Operations\*\*

#### Why this step is done

Real-world datasets contain **missing values**, which can break string operations.

***

#### How it is done

`.str.contains('value', na=False)`

***

#### What to do

* Always handle NaN explicitly

#### What not to do

* Avoid ignoring missing values

***

#### Key Features

* Prevents errors
* Ensures clean filtering

***

#### Limitations

* May silently exclude missing data

```python
# STEP 5: HANDLING MISSING VALUES IN STRING OPERATIONS

print("\n STEP 5. HANDLING NaN IN STRING FILTERING")

# Safe filtering with na=False
# This will filter penguins whose 'sex' column contains 'male', while safely handling any NaN values 
# in the 'sex' column by treating them as False. 
safe_filter = df[df['sex'].str.contains('male', case=False, na=False)]

print("\nFiltering 'male' safely (ignoring NaN):")
print("safe_filter.head()->", safe_filter.head())

```

**Output**

```python
 STEP 5. HANDLING NaN IN STRING FILTERING

Filtering 'male' safely (ignoring NaN):
safe_filter.head()->   species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g     sex
0  Adelie  Torgersen            39.1           18.7              181.0       3750.0    Male
1  Adelie  Torgersen            39.5           17.4              186.0       3800.0  Female
2  Adelie  Torgersen            40.3           18.0              195.0       3250.0  Female
4  Adelie  Torgersen            36.7           19.3              193.0       3450.0  Female
5  Adelie  Torgersen            39.3           20.6              190.0       3650.0    Male

```

### STEP 6: Error Demonstrations

#### Why this step is done

Understanding errors improves debugging and conceptual clarity.

#### Common errors

| Error Type     | Cause               |
| -------------- | ------------------- |
| Syntax Error   | Missing parentheses |
| ValueError     | Wrong operator      |
| AttributeError | Wrong method usage  |

#### What to do

* Learn from errors
* Read error messages carefully

#### What not to do

* Do not ignore warnings/errors

```python
# STEP 6: ERROR DEMONSTRATIONS (COMMENTED OUT)

# ERROR 1: Missing parentheses
# This will raise an error because the conditions are not properly grouped with parentheses.
# df[df['body_mass_g'] > 4000 & df['species'] == 'Adelie']

# ERROR 2: Using 'and' instead of '&'
# This will raise an error because 'and' cannot be used for element-wise logical operations in Pandas.
# df[(df['body_mass_g'] > 4000) and (df['species'] == 'Adelie')]

# ERROR 3: .str.contains() on non-string column
# This will raise an error because 'body_mass_g' is a numeric column, and .str.contains() cannot be applied to it.
# df[df['body_mass_g'].str.contains('4000')]

# ERROR 4: NaN issue in string filtering
# This will raise an error because there are NaN values in the 'sex' column, and .str.contains() 
# cannot handle NaN without the na=False parameter.
# df[df['sex'].str.contains('male')]

```

### STEP 7: Summary

#### Why this step is done

To consolidate learning and reinforce key ideas.

***

#### Key Takeaways

* Boolean indexing is fundamental
* Logical operators combine conditions
* `.isin()` simplifies multiple comparisons
* `.str.contains()` handles text filtering
* Missing values must be handled carefully

```python
# STEP 7: SUMMARY
print("\n STEP 7. SUMMARY")

print("""
KEY LEARNINGS:

1. Boolean indexing filters rows using True/False conditions
2. Use & (AND), | (OR), ~ (NOT) for combining conditions
3. Use .isin() for filtering multiple values
4. Use .str.contains() for string filtering
5. Handle missing values using na=False
6. Always use parentheses in conditions

BEST PRACTICE:
Use clear and well-structured conditions for readability and correctness
""")

```

### The entire script as a single block is given below:-

```python

"""
PROJECT: Conditional Filtering in Pandas
DATASET: Palmer Penguins

OBJECTIVE:
To demonstrate:
1. Boolean indexing
2. Logical operators (&, |, ~)
3. .isin() method
4. .str.contains() for string filtering
5. Common errors and handling

NOTE:
This script is written for teaching purposes with detailed comments.
"""

# STEP 0: IMPORT LIBRARIES AND LOAD DATASET
print("\n STEP 0. IMPORT LIBRARIES AND LOAD DATASET")
import pandas as pd
import seaborn as sns

df = sns.load_dataset("penguins")

print("\n--- FIRST 5 ROWS ---")
print("df.head()->", df.head())  # Display the first 5 rows of the dataset to understand its structure and columns

#------------------------------------------------------------
# STEP 1: BASIC BOOLEAN INDEXING
print("\n STEP 1. BASIC BOOLEAN FILTERING")

# Filter penguins with body mass greater than 4000 grams
# This creates a Boolean Series where True indicates rows that satisfy the condition
heavy_penguins = df[df['body_mass_g'] > 4000]  

print("\nPenguins with body_mass_g > 4000:")
print("heavy_penguins.head()->", heavy_penguins.head())

# Explanation:
# df['body_mass_g'] > 4000 creates a Boolean Series (True/False)
# Pandas uses this to filter rows

#------------------------------------------------------------
# STEP 2: COMBINING CONDITIONS

print("\n STEP 2. COMBINING CONDITIONS")

# Condition using AND (&)
# To combine conditions, we use & for AND, | for OR, and ~ for NOT. 
# Each condition must be enclosed in parentheses.
cond_and = df[(df['body_mass_g'] > 4000) & (df['species'] == 'Adelie')]
print("\nAdelie penguins with body_mass_g > 4000:")
print("cond_and.head()->", cond_and.head())

# Condition using OR (|)
# This will filter penguins that are either Adelie OR Chinstrap, regardless of their body mass.
cond_or = df[(df['species'] == 'Adelie') | (df['species'] == 'Chinstrap')]
print("\nAdelie OR Chinstrap penguins:")
print("cond_or.head()->", cond_or.head())

# Condition using NOT (~)
# This will filter penguins that are NOT Adelie.
cond_not = df[~(df['species'] == 'Adelie')]
print("\nPenguins that are NOT Adelie:")
print("cond_not.head()->", cond_not.head())

# IMPORTANT:
# Always use parentheses around conditions

#------------------------------------------------------------
# STEP 3: USING .isin()

print("\n STEP 3. USING .isin() ================")
# Filter multiple species
# This will filter penguins that belong to either the 'Adelie' or 'Chinstrap' species.
species_filter = df[df['species'].isin(['Adelie', 'Chinstrap'])]

print("\nPenguins belonging to Adelie or Chinstrap:")
print("species_filter.head()->", species_filter.head())

# Explanation:
# .isin() checks membership in a list of values

#------------------------------------------------------------
# STEP 4: STRING FILTERING USING .str.contains()

print("\n STEP 4. STRING FILTERING ================")

# Filter rows where island contains 'Dream'
# This will filter penguins that are from islands whose names contain the substring 'Dream'.
dream_island = df[df['island'].str.contains('Dream')]

print("\nPenguins from Dream island:")
print("dream_island.head()->", dream_island.head())

# Case-insensitive search
# This will filter penguins from islands that contain 'dream' in any case (e.g., 'Dream', 'dream', 'DREAM').
dream_case_insensitive = df[df['island'].str.contains('dream', case=False)]

print("\nCase-insensitive filtering:")
print("dream_case_insensitive.head()->", dream_case_insensitive.head())

#------------------------------------------------------------
# STEP 5: HANDLING MISSING VALUES IN STRING OPERATIONS

print("\n STEP 5. HANDLING NaN IN STRING FILTERING")

# Safe filtering with na=False
# This will filter penguins whose 'sex' column contains 'male', while safely handling any NaN values 
# in the 'sex' column by treating them as False. 
safe_filter = df[df['sex'].str.contains('male', case=False, na=False)]

print("\nFiltering 'male' safely (ignoring NaN):")
print("safe_filter.head()->", safe_filter.head())

#------------------------------------------------------------
# STEP 6: ERROR DEMONSTRATIONS (COMMENTED OUT)

# ERROR 1: Missing parentheses
# This will raise an error because the conditions are not properly grouped with parentheses.
# df[df['body_mass_g'] > 4000 & df['species'] == 'Adelie']

# ERROR 2: Using 'and' instead of '&'
# This will raise an error because 'and' cannot be used for element-wise logical operations in Pandas.
# df[(df['body_mass_g'] > 4000) and (df['species'] == 'Adelie')]

# ERROR 3: .str.contains() on non-string column
# This will raise an error because 'body_mass_g' is a numeric column, and .str.contains() cannot be applied to it.
# df[df['body_mass_g'].str.contains('4000')]

# ERROR 4: NaN issue in string filtering
# This will raise an error because there are NaN values in the 'sex' column, and .str.contains() 
# cannot handle NaN without the na=False parameter.
# df[df['sex'].str.contains('male')]

#------------------------------------------------------------
# STEP 7: SUMMARY
print("\n STEP 7. SUMMARY")

print("""
KEY LEARNINGS:

1. Boolean indexing filters rows using True/False conditions
2. Use & (AND), | (OR), ~ (NOT) for combining conditions
3. Use .isin() for filtering multiple values
4. Use .str.contains() for string filtering
5. Handle missing values using na=False
6. Always use parentheses in conditions

BEST PRACTICE:
Use clear and well-structured conditions for readability and correctness
""")

```

### Flowchart

**The following flowchart shows all the steps of the above script**

![Filtering Flowchart](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch12-filtering.png)

![Filtering Flowchart](../.gitbook/assets/ch12-filtering.png)
