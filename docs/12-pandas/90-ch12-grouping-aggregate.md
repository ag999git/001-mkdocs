# Grouping and Aggregation

## Grouping and Aggregation

### Research Topic: Comparative Morphology and Population Stability

**Research Question:** _How can the "Split-Apply-Combine" philosophy be utilized to analyze biological differences between penguin species and filter environmental variables based on population significance?_

**Project Scenario:** A research team requires a statistical breakdown of the Palmer Penguins data to support a hypothesis. Specifically, they need:

1. **Descriptive Statistics:** Average bill length and flipper length per species.
2. **Complex Metrics:** A simultaneous calculation of the mean and maximum body mass for each island.
3. **Data Quality Control:** Filtering out islands that have fewer than 100 observations to ensure statistical significance (islands with too few samples are considered outliers or insufficient for the study).

**Student Task:** Using the Palmer Penguins dataset, write a script to group data by species and island, calculate aggregate metrics, and filter out groups with low sample counts.

***

### 1. Conceptual Deep Dive

Grouping and Aggregation is the core of data analysis. It relies on the **Split-Apply-Combine** paradigm, originally defined by Hadley Wickham.

### The Split-Apply-Combine Strategy

1. **Split:** Break the DataFrame into distinct groups based on a key (e.g., "Species"). The DataFrame is not actually copied into separate variables; it is virtually partitioned.
2. **Apply:** Perform a calculation (aggregate) or transformation on each group independently.
3. **Combine:** Merge the results of the applied functions back into a new DataFrame or Series.

**Flowchart of Grouping:**

![Flowchart of Grouping](../.gitbook/assets/ch12-grouping.png)

### What is `.groupby()`

#### Definition

`groupby()` is a Pandas method used to **split a DataFrame into groups based on one or more keys**, so that operations can be applied **independently to each group**.

Philosophy: _Split → Apply → Combine_

| Stage   | Meaning                         | Example                   |
| ------- | ------------------------------- | ------------------------- |
| Split   | Divide data into groups         | Group penguins by species |
| Apply   | Perform operation on each group | Compute mean body mass    |
| Combine | Merge results into output       | Return summary table      |

**2. Method Signature of `.groupby()`**

```python
DataFrame.groupby(  
  by=None,  
  axis=0,  
  level=None,  
  as_index=True,  
  sort=True,  
  group_keys=True,  
  observed=False,  
  dropna=True  
)
```

***

**3. Parameter Explanation Table**

##

| Parameter   | Type                    | Default | Description                          | Example                         |
| ----------- | ----------------------- | ------- | ------------------------------------ | ------------------------------- |
| by          | label / list / function | None    | Column(s) used for grouping          | species', \['species','island'] |
| axis        | 0 or 1                  | 0       | Group along rows (0) or columns (1)  | Usually 0                       |
| level       | int / name              | None    | For MultiIndex grouping              | level=0                         |
| as\_index   | bool                    | TRUE    | Group labels become index            | False → regular column          |
| sort        | bool                    | TRUE    | Sort group keys                      | False → faster                  |
| group\_keys | bool                    | TRUE    | Include keys in output when applying | Used with .apply()              |
| observed    | bool                    | FALSE   | Only show observed categories        | For categorical data            |
| dropna      | bool                    | TRUE    | Drop NA group keys                   | Include NaN groups if False     |

**4. What Does `groupby()` Return?**

**5. Return Type**

`DataFrameGroupBy` OR `SeriesGroupBy`

**6. Important Insight**

> `groupby()` **does NOT compute anything immediately**\
> It returns a **lazy object** (GroupBy object)

***

**7. Example**

```python
grouped  =  df.groupby("species")  
print(type(grouped))
```

**8. Output:**

`<class 'pandas.core.groupby.generic.DataFrameGroupBy'>`

**9. Typical Usage Patterns**

**A. Simple Aggregation**

`df.groupby("species")["body_mass_g"].mean()`

\*\* Output: `Series`\*\*

***

**B. Multiple Aggregations**

`df.groupby("species").agg(["mean", "max"])`

**Output: `DataFrame (MultiIndex columns)`**

***

**C. Multi-column Grouping**

`df.groupby(["species", "island"]).mean()`

**Output: MultiIndex**

***

**D. Filtering Groups**

`df.groupby("species").filter(lambda x: x["body_mass_g"].mean() > 4000)`

**Output: Filtered DataFrame**

***

**E. Transformation (Same Shape Output)**

```python
df["mean_mass"] =  df.groupby("species")["body_mass_g"].transform("mean")
```

### Aggregation methods (1) `.agg()` (2) `.transform()` (3) `.filter()`

***

#### `.agg()` (Aggregation)

**Description**

Applies one or more functions to each group and **returns a reduced summary**.

**Key Idea**

> “Give me one (or few) values per group”

***

**Example**

`df.groupby("species")["body_mass_g"].agg(["mean", "max"])`

***

**Output**

* DataFrame (often with **MultiIndex columns**)
* One row per group

***

**Typical Use Cases**

| Use Case           | Example          |
| ------------------ | ---------------- |
| Summary statistics | mean, sum, count |
| Reporting          | group-wise KPIs  |
| Data reduction     | compress dataset |

**Important parameters**

| Parameter  | Description                                |
| ---------- | ------------------------------------------ |
| func       | Function or list ('mean', \['mean','sum']) |
| \*\*kwargs | Named aggregations                         |

#### `.transform()` (Same Shape Transformation)

**Description**

Applies a function **to each group** and returns output of **same size as original data**.

**Key Idea**

> “Compute something per group, but keep all rows”

***

**Example**

```python
df["mean_mass"] =  df.groupby("species")["body_mass_g"].transform("mean")
```

***

**Output**

* Series or DataFrame
* Same length as original

***

**Typical Use Cases**

| Use Case            | Example              |
| ------------------- | -------------------- |
| Feature engineering | group mean column    |
| Normalization       | z-score within group |
| Comparison          | row vs group average |

#### `.filter()` (Group Filtering)

**Description**

Filters entire groups based on a condition and returns **subset of original rows**.

**Key Idea**

> “Keep or remove entire groups”

***

**Example**

`df.groupby("species").filter(lambda x: x["body_mass_g"].mean() > 4000)`

***

**Output**

* DataFrame (subset of original rows)

***

**Typical Use Cases**

| Use Case              | Example                   |
| --------------------- | ------------------------- |
| Remove weak groups    | low average               |
| Data cleaning         | small groups              |
| Conditional selection | threshold-based filtering |

**Important Parameters**

| Parameter | Description                   |
| --------- | ----------------------------- |
| func      | Function returning True/False |
| dropna    | Keep NaN groups               |

**Common Errors**

\*\*Passing string instead of function \*\* `df.groupby("species").filter("body_mass_g > 4000") # TypeError`

#### Comparison of Aggregation Methods

| Method         | Syntax                 | Input Type     | Returns            | Output Shape                | Use Case                                | Typical Example                               | Affects Original Data   | Common Pitfall                                                |
| -------------- | ---------------------- | -------------- | ------------------ | --------------------------- | --------------------------------------- | --------------------------------------------- | ----------------------- | ------------------------------------------------------------- |
| `.agg()`       | `.agg(['mean','sum'])` | GroupBy object | DataFrame / Series | Reduced (one row per group) | Calculate multiple summary statistics   | Mean and max body mass per species            | No (returns new object) | Using invalid function names (e.g., 'avg' instead of 'mean')  |
| `.transform()` | `.transform('mean')`   | GroupBy object | Series / DataFrame | Same as original data       | Add group-level values to each row      | Add species average mass to every penguin row | No                      | Expecting reduced output (it does NOT summarize)              |
| `.filter()`    | `.filter(func)`        | GroupBy object | DataFrame          | Subset of original rows     | Remove entire groups based on condition | Keep species with avg mass > 4000             | No                      | Writing condition incorrectly (must use function, not string) |

### Solution Script

The following script performs grouping, calculates complex aggregates, and filters out islands with insufficient data volume.

```python

"""
PROJECT: Grouping and Aggregation in Pandas
DATASET: Palmer Penguins

OBJECTIVE:
1. Understand Split–Apply–Combine
2. Perform grouping using groupby()
3. Apply aggregation functions using agg()
4. Filter groups based on conditions

NOTE:
This script is written for teaching purposes.
Each step includes explanation, purpose, and output hints.
"""

# ==========================================================
# STEP 1: IMPORT LIBRARIES AND LOAD DATASET
# ==========================================================

print("\nSTEP 1: IMPORT LIBRARIES AND LOAD DATASET")

import pandas as pd
import seaborn as sns

# Load dataset
df = sns.load_dataset("penguins")

# ----------------------------------------------------------
# STEP 1.1: INITIAL DATA INSPECTION
# ----------------------------------------------------------

print("\n--- FIRST 5 ROWS ---")
print(df.head())
# OUTPUT HINT:
# Displays first 5 rows of the dataset.
# Helps identify column names and structure.
# Columns include: species, island, bill_length_mm, etc.
# Some rows may contain missing values (NaN).

print("\n--- SHAPE OF DATA ---")
print("Shape:", df.shape)
# OUTPUT HINT:
# Shape is (rows, columns)
# (344, 7) → 344 rows and 7 columns


# ==========================================================
# STEP 2: BASIC GROUPING USING groupby()
# ==========================================================

print("\nSTEP 2: BASIC GROUPING USING groupby()")

# ----------------------------------------------------------
# STEP 2.1: SPLIT (Group the data)
# ----------------------------------------------------------

grouped_species = df.groupby("species")

# Explanation:
# The DataFrame is split into groups based on unique values in 'species'.
# Each group represents one species (Adelie, Chinstrap, Gentoo).

# grouped_species is a DataFrameGroupBy object:
# - It does NOT store separate DataFrames explicitly
# - It stores grouping instructions

# No computation happens here → only grouping (Split step)

# Example access:
# grouped_species['body_mass_g']


# ----------------------------------------------------------
# STEP 2.2: APPLY + COMBINE (Calculate mean)
# ----------------------------------------------------------

mean_mass = grouped_species["body_mass_g"].mean()

# Explanation:
# Apply → mean() is applied to each group
# Combine → results are combined into a single Series

# Output:
# Index → species
# Values → mean body mass

print("\nMean body mass by species:")
print(mean_mass)

# OUTPUT HINT:
# species
# Adelie       ~3700
# Chinstrap    ~3700+
# Gentoo       ~5000


# ----------------------------------------------------------
# STEP 2.3: COMMON ERROR
# ----------------------------------------------------------

# ERROR:
# Using a non-existing column raises KeyError
# df.groupby("wrong_column")


# ==========================================================
# STEP 3: MULTIPLE AGGREGATIONS USING .agg()
# ==========================================================

print("\nSTEP 3: MULTIPLE AGGREGATIONS USING .agg()")

# ----------------------------------------------------------
# STEP 3.1: APPLY MULTIPLE FUNCTIONS
# ----------------------------------------------------------

agg_results = df.groupby("species").agg({
    "body_mass_g": ["mean", "sum", "count"],
    "bill_length_mm": ["mean", "max"]
})

# Explanation:
# .agg() applies multiple functions at once.

# Dictionary structure:
# Key → column name
# Value → list of functions

# Result:
# DataFrame with MultiIndex columns:
# Level 1 → column name
# Level 2 → function name

print("\nAggregated results:")
print(agg_results)

# OUTPUT HINT:
# Multi-level columns:
# body_mass_g → mean, sum, count
# bill_length_mm → mean, max


# ----------------------------------------------------------
# STEP 3.2: IMPORTANT CONCEPT
# ----------------------------------------------------------

# .agg() reduces data → one row per group

# Original → many rows per species
# After agg → one row per species

# Use .transform() if original shape must be preserved


# ----------------------------------------------------------
# STEP 3.3: COMMON ERROR
# ----------------------------------------------------------

# ERROR:
# Invalid function name raises error
# df.groupby("species").agg({"body_mass_g": "average"})


# ==========================================================
# STEP 4: GROUPING BY MULTIPLE COLUMNS
# ==========================================================

print("\nSTEP 4: GROUPING BY MULTIPLE COLUMNS")

# ----------------------------------------------------------
# STEP 4.1: MULTI-LEVEL GROUPING
# ----------------------------------------------------------

group_multi = df.groupby(["species", "island"])["body_mass_g"].mean()

# Explanation:
# Groups are formed using combinations:
# (species, island)

# Example groups:
# (Adelie, Biscoe), (Adelie, Dream), etc.

print("\nMean body mass by species and island:")
print(group_multi)

# OUTPUT HINT:
# MultiIndex output:
# (species, island) → mean value


# ----------------------------------------------------------
# STEP 4.2: IMPORTANT CONCEPT
# ----------------------------------------------------------

# Output uses MultiIndex (hierarchical index):
# Level 1 → species
# Level 2 → island


# ==========================================================
# STEP 5: FILTERING GROUPS
# ==========================================================

print("\nSTEP 5: FILTERING GROUPS")

# ----------------------------------------------------------
# STEP 5.1: DEFINE FILTER CONDITION
# ----------------------------------------------------------

filtered_groups = df.groupby("species").filter(
    lambda x: x["body_mass_g"].mean() > 4000
)

# Explanation:
# filter() keeps/removes entire groups

# Function (lambda):
# Input → group DataFrame
# Output → True/False

# True → keep group
# False → remove group

print("\nFiltered dataset (species with avg mass > 4000):")
print(filtered_groups.head())

# OUTPUT HINT:
# Likely only "Gentoo" remains


# ----------------------------------------------------------
# STEP 5.2: IMPORTANT CONCEPT
# ----------------------------------------------------------

# filter() returns original rows (not summary)

# Comparison:
# agg() → summary
# filter() → subset of original data


# ----------------------------------------------------------
# STEP 5.3: COMMON ERROR
# ----------------------------------------------------------

# ERROR:
# filter() expects a function, not a string
# df.groupby("species").filter("body_mass_g > 4000")


# ==========================================================
# STEP 6: SUMMARY
# ==========================================================

print("\nSTEP 6: SUMMARY")

print("""
KEY LEARNINGS:

1. groupby() implements Split–Apply–Combine
2. agg() computes multiple statistics
3. groupby() + column → Series output
4. filter() removes entire groups
5. Multi-column grouping creates MultiIndex

IMPORTANT DIFFERENCE:

- groupby().agg() → REDUCES data
- groupby().filter() → FILTERS rows

BEST PRACTICES:

- Inspect data before grouping
- Handle missing values carefully
- Use valid aggregation functions
- Understand output structure (Series vs DataFrame vs MultiIndex)
""")


```
