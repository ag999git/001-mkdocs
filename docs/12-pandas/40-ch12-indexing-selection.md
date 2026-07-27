# Research Project: Advanced Indexing and Selection in Pandas using Palmer Penguins Dataset

## Research Project: Advanced Indexing and Selection in Pandas using Palmer Penguins Dataset

### Research Question

> **How can different indexing and selection techniques in Pandas (`[]`, `.`, `.loc[]`, `.iloc[]`, and slicing) be used to efficiently extract, filter, and manipulate structured data, and what are their comparative advantages, limitations, and appropriate use cases when working with real-world datasets such as the Palmer Penguins dataset?**

***

### Task / Project Brief

You are required to:

1. Load and explore the **Palmer Penguins dataset**
2. Perform **column selection** using:
   * Bracket `[]`
   * Dot `.` notation
3. Perform **row selection** using:
   * `.loc[]` (label-based indexing)
   * `.iloc[]` (position-based indexing)
4. Perform **combined slicing of rows and columns**
5. Compare all methods in terms of:
   * Syntax
   * Flexibility
   * Limitations
6. Handle possible **errors/exceptions**
7. Document your findings with:
   * Tables
   * Code with comments
   * Flowcharts

***

## Model Solution

***

#### Step 1: Import Libraries and Load Dataset

```python
import pandas as pd  # Step1 Import libraries and load dataset
import seaborn as sns

# Load dataset
df = sns.load_dataset("penguins")
```

#### Step 2: Understanding the Data Structure

**Step 2(A)**

```python
# Step 2:  Understanding the Data Structure
# 2. A. df.info() gives us a concise summary of the DataFrame, including the number of non-null entries, 
# data types of each column, and memory usage. 
# This is crucial for understanding the structure of our dataset and identifying any potential 
# issues such as missing values or incorrect data types.
print("df.info():->", df.info())  

"""Output:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 344 entries, 0 to 343
Data columns (total 7 columns): 
 #   Column           Non-Null Count  Dtype  
---  ------           --------------  -----
 0   species          344 non-null    object
 1   island           344 non-null    object
 2   bill_length_mm   342 non-null    float64
 3   bill_depth_mm    342 non-null    float64
 4   flipper_length_mm 342 non-null    float64
 5   body_mass_g      342 non-null    float64
 6   sex              333 non-null    object
dtypes: float64(4), object(3)
memory usage: 18.9+ KB
"""
# df.info():-> None. This method prints the summary information to the console but does not return any value, hence it outputs None.

```

**Step 2(B)**

```python

# 2. B. df.describe() provides a statistical summary of the numerical columns in the DataFrame, 
# including count, mean, standard deviation, minimum, and maximum values.
print("df.describe():->\n", df.describe())

"""Output:
df.describe():->
        bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g
count     342.000000     342.000000        342.000000    342.000000
mean       43.921930      17.151754         200.915205   4201.754386
std         5.459584       1.974603          14.061714   801.954380
min        32.100000      13.100000         172.000000  2700.000000
25%        39.225000      15.600000         190.000000  3550.000000
50%        44.450000      17.300000         197.000000  4050.000000
75%        48.100000      18.700000         213.000000  4750.000000
max        59.600000      21.500000         231.000000  6300.000000
"""

```

**Step 2(C)**

```python
# 2. C. df.columns and df.index provide information about the column names and row indices of the DataFrame, respectively.
print("df.columns:->", df.columns)

"""Output:
df.columns:-> Index(['species', 'island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex'], dtype='object')
"""

```

**Step 2(D)**

```python
# 2. D. df.index gives us the row labels of the DataFrame, which can be useful for accessing specific rows or understanding 
# the structure of the data.
print("df.index:->", df.index)
"""Output:
df.index:-> RangeIndex(start=0, stop=344, step=1)
"""
```

#### Step 3 Selelcting columns using -3(A). Bracket notation and -3(B). Dot notation

**Step 3(A): Using bracket `[]` notation**

```python

# Step 3 Selelcting columns using A. Bracket notation and B. Dot notation

# 3 (A) Bracket Notation: This method allows us to select one or more columns from the DataFrame using square brackets. 
# For example, df['column_name'] will return a Series containing the data from that column
# To select multiple columns, we can pass a list of column names inside the brackets, like df[['col1', 'col2']].

# (1) Selecting single column
species = df['species']
print("species.head()->\n", species.head())
"""
species.head()->
0    Adelie
1    Adelie
2    Adelie
3    Adelie
4    Adelie
Name: species, dtype: object
"""

# (2) Selecting multiple columns
subset = df[['species', 'bill_length_mm', 'body_mass_g']]
print("subset.head()->\n", subset.head())

"""Output:
subset.head()->
  species  bill_length_mm  body_mass_g
0  Adelie           39.1        3750.0
1  Adelie           39.5        3800.0
2  Adelie           40.3        3250.0
3  Adelie           Nan         Nan
4  Adelie           36.7        3450.0

"""

# Advantages of Bracket Notation
# - Works with any column name (even with spaces)
# - Flexible for multiple column selection


```

**Step 3(B): Using dot `.` notation**

```python

# 3 (B) Dot Notation: This method allows us to access columns as attributes of the DataFrame. For example, df.column_name will return a Series containing the data from that column. 
# However, this method only works if the column name is a valid Python identifier (no spaces, special characters, and doesn't start with a number). 
# Selecting single column using dot notation
species_dot = df.species
print("species_dot.head()->\n", species_dot.head())

"""Output:
species_dot.head()->
0    Adelie
1    Adelie
2    Adelie
3    Adelie
4    Adelie
Name: species, dtype: object
"""


# Advantages of Dot Notation
# - More concise and easier to read for simple column names
# - Can be more convenient for quick access to columns with valid names

# Limitations of Dot Notation
# - Column name must be valid Python identifier
# - Cannot use for multiple columns
# - May conflict with pd.DataFrame methods

```

**Table comparing bracket `[]` notation to dot `.` notation**

| Feature            | `[]` Notation | `.` Notation        |
| ------------------ | ------------- | ------------------- |
| Multiple columns   | Yes           | No                  |
| Special characters | Supported     | Not supported       |
| Safe usage         | Recommended   | Risky in some cases |
| Readability        | Moderate      | High                |

#### Step 4 Selecting Rows using -4(A) `.loc[]` (Label-based) and -4(B) `.iloc[]` (Integer-based)

**Step 4(A): Selecting using `.loc` (label-based)**

4. (A) `.loc[]` is used for label-based indexing, which means we can select rows and columns by their labels. For example, `df.loc[row_label, column_label]` allows us to select specific rows and columns based on their labels.

```python

# Step 4. Selecting Rows using .loc[] (Label-based) and .iloc[] (Integer-based)

# 4. (A) .loc[] is used for label-based indexing, which means we can select rows and columns by their labels. For example, df.loc[row_label, column_label] allows us to select specific rows and columns based on their labels.
# Selecting using .loc (label-based)

# (1) Selecting a single row by index label
row_0 = df.loc[0]
print("row_0->\n", row_0)

"""Output:
row_0-> 
species            Adelie
island             Torgersen
bill_length_mm        39.1
bill_depth_mm         18.7
flipper_length_mm     181.0
body_mass_g          3750.0
sex                  Male
Name: 0, dtype: object
"""


# (2) Selecting multiple rows by index label (note: .loc includes the end label in slicing)
rows_0_5 = df.loc[0:5]
print("rows_0_5->\n", rows_0_5)

"""Output:
rows_0_5->
  species     island  bill_length_mm  bill_depth_mm  flipper_length_mm   body_mass_g    sex
0  Adelie  Torgersen           39.1            18.7              181.0       3750.0   Male
1  Adelie  Torgersen           39.5            17.4              186.0       3800.0 Female
2  Adelie  Torgersen           40.3            18.0              195.0       3250.0 Female
3  Adelie  Torgersen            NaN             NaN              NaN          NaN      NaN
4  Adelie  Torgersen           36.7            19.3              193.0       3450.0 Female
5  Adelie  Torgersen           39.3            20.6              190.0       3650.0   Male

"""


# (3) Selecting range of rows and specific columns
subset_loc = df.loc[0:5, ['species', 'body_mass_g']]
print("subset_loc->\n", subset_loc)

"""Output:
subset_loc-> 
  species  body_mass_g
0  Adelie       3750.0
1  Adelie       3800.0
2  Adelie       3250.0
3  Adelie          NaN
4  Adelie       3450.0
5  Adelie       3650.0
"""

```

**Step 4(B) Selecting Rows using .iloc\[] (Position/ Integer-based)**

```python

# 4.(B) Selecting Rows using .iloc[] (Position/ Integer-based)
# Select rows by their integer position. 
# Selecting using .iloc (integer-based)
# (1) Selecting first row
row_0_iloc = df.iloc[0]
print("row_0_iloc->\n", row_0_iloc)

"""Output:
row_0_iloc-> 
species            Adelie
island             Torgersen
bill_length_mm        39.1
bill_depth_mm         18.7
flipper_length_mm     181.0
body_mass_g          3750.0
sex                  Male
Name: 0, dtype: object
"""


# (2) Selecting multiple rows by integer position
rows_iloc = df.iloc[0:5]
print("rows_iloc->\n", rows_iloc)

"""Output:
rows_iloc->
  species     island  bill_length_mm  bill_depth_mm  flipper_length_mm   body_mass_g      sex
0  Adelie  Torgersen           39.1            18.7              181.0       3750.0     Male
1  Adelie  Torgersen           39.5            17.4           186.0          3800.0   Female
2  Adelie  Torgersen           40.3            18.0              195.0       3250.0   Female
3  Adelie  Torgersen            NaN             NaN              NaN          NaN        NaN
4  Adelie  Torgersen           36.7            19.3              193.0       3450.0   Female
"""

# (3) Selecting range of rows and specific columns
subset_iloc = df.iloc[0:5, 0:3]
print("subset_iloc->\n", subset_iloc)


"""Output:
subset_iloc-> 
  species     island  bill_length_mm
0  Adelie  Torgersen           39.1
1  Adelie  Torgersen           39.5
2  Adelie  Torgersen           40.3
3  Adelie  Torgersen            NaN
4  Adelie  Torgersen           36.7
"""

```

**Comparison Table: `.loc[]` vs `.iloc[]`**

| Feature          | `.loc[]`             | `.iloc[]`         |
| ---------------- | -------------------- | ----------------- |
| Basis            | Labels (index names) | Integer positions |
| End index        | Included             | Excluded          |
| Flexibility      | High                 | High              |
| Boolean indexing | Supported            | Not directly      |

#### Step 5 Slicing Rows and Columns Simultaneously

**Step 5(A) Using .loc\[] for slicing by labels**

```python
# 5. Slicing Rows and Columns Simultaneously
# 5. (A) Using .loc[] for slicing by labels
# Slicing rows and columns using .loc
# Slice rows and columns together
slice_loc = df.loc[10:20, ['species', 'island', 'body_mass_g']]
print("slice_loc->\n", slice_loc)

"""Output:
slice_loc-> 
   species     island  body_mass_g
10  Adelie  Torgersen       3750.0
11  Adelie  Torgersen       3800.0
12  Adelie  Torgersen       3250.0
13  Adelie  Torgersen          NaN
14  Adelie  Torgersen       3450.0
15  Adelie  Torgersen       3650.0
16  Adelie  Torgersen       3800.0
17  Adelie  Torgersen       3700.0
18  Adelie  Torgersen       3600.0
19  Adelie  Torgersen       3500.0
20  Adelie  Torgersen       3400.0
"""

```

**Step 5(B): Using `.iloc[]` for slicing by integer position**

```python

# 5. (B) Using .iloc[] for slicing by integer position
# Slicing rows and columns using .iloc
slice_iloc = df.iloc[10:20, 0:3]  # Slice rows 10 to 19 and columns 0 to 2
print("slice_iloc->\n", slice_iloc)

"""Output:
slice_iloc-> 
    species     island  bill_length_mm
10  Adelie  Torgersen           37.8
11  Adelie  Torgersen           37.8
12  Adelie  Torgersen           41.1
13  Adelie  Torgersen           38.6
14  Adelie  Torgersen           34.6
15  Adelie  Torgersen           36.6
16  Adelie  Torgersen           38.7
17  Adelie  Torgersen           42.5
18  Adelie  Torgersen           34.4
19  Adelie  Torgersen           46.0
"""

```

**Table: When to Use What**

| Scenario                    | Recommended Method |
| --------------------------- | ------------------ |
| Selecting one column        | `df['col']`        |
| Selecting multiple columns  | `df[['col1']]`     |
| Filtering by row labels     | `.loc[]`           |
| Filtering by position       | `.iloc[]`          |
| Complex slicing             | `.loc[] / .iloc[]` |
| Safe, production-level code | `[] + .loc[]`      |

#### Flow chart shows how indexing is done

![FlowChart](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch12-pandas-indexing.png)

![FlowChart](../.gitbook/assets/ch12-pandas-indexing.png)
