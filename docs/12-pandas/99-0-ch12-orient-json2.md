

# Detailed discussion on the script given in the book


## STEP 1: LOAD DATA FROM CSV

### Code Snippet

```python
df  =  pd.read_csv(url)  
print(df.head())
```
### What happens

-   `pd.read_csv()` reads a CSV file from a URL
-   Converts it into a **DataFrame (tabular structure)**

### Output Structure (Tabular)

```python
total_bill   tip   sex     smoker  
16.99        1.01  Female  No  
10.34        1.66  Male    No
```
### Concept

This is **flat (2D) data**

-   Rows = observations
-   Columns = variables

----------

## STEP 2: SAVE INTO DIFFERENT JSON FORMATS

### Code Snippet

```python
df.to_json("tips_records.json", orient="records")  
df.to_json("tips_columns.json", orient="columns")  
df.to_json("tips_index.json", orient="index")  
df.to_json("tips_split.json", orient="split")
```


### What happens

-   `to_json()` converts DataFrame → JSON
-   `orient` controls **structure of JSON**

### Concept

>Same data → **4 different storage structures**

----------

## STEP 3: READ JSON (records)

###  Code Snippet

```python
df_records  =  pd.read_json("tips_records.json", orient="records")
```

### What happens

-   `read_json()` reconstructs DataFrame
-   Uses `orient='records'`

### Output

Same as original table

### Concept

>Pandas understands **row-wise JSON**

----------

## STEP 4: RAW JSON (records)

### Code Snippet

```python
data_records  =  json.load(f)  
print(data_records[:2])
```

### Actual JSON Structure

```python
[  
 {"total_bill": 16.99, "tip": 1.01, "sex": "Female"},  
 {"total_bill": 10.34, "tip": 1.66, "sex": "Male"}  
]
```

### Concept

>This **is nested JSON (Level 2 nesting)**

Structure:

-   List → rows
-   Each element → dictionary

Hierarchy:

```python
list  
 ├── dict (row1)  
 ├── dict (row2)
```
----------

## STEP 5: READ JSON (columns)

### Code Snippet

```python
df_columns  =  pd.read_json("tips_columns.json", orient="columns")
```

### Concept

>Pandas reconstructs from **column-wise storage**

----------

## STEP 6: RAW JSON (columns)

### Structure

```python
{  
 "total_bill": {"0": 16.99, "1": 10.34},  
 "tip": {"0": 1.01, "1": 1.66}  
}
```

#### Concept

>Nested JSON (Level 2)

Hierarchy:

```python
dict (columns)  
 ├── dict (row index → value)
```

>Column → Row → Value

----------

## STEP 7: READ JSON (index)

### Code Snippet

```python
df_index  =  pd.read_json("tips_index.json", orient="index")

```
### Concept

>Rebuild DataFrame from row-based dictionary

----------

## STEP 8: RAW JSON (index)

### Structure

```python
{  
 "0": {"total_bill": 16.99, "tip": 1.01},  
 "1": {"total_bill": 10.34, "tip": 1.66}  
}
```

### Concept

>Nested JSON (Level 2)

Hierarchy:
```python
dict (rows)  
 ├── dict (columns)
```
>Row → Column → Value

----------

## STEP 9: READ JSON (split)

### Code Snippet

```python
df_split  =  pd.read_json("tips_split.json", orient="split")
```
#### Concept

>Uses metadata + data separation

----------

## STEP 10: RAW JSON (split)

### Structure

```python
{  
 "columns": ["total_bill", "tip"],  
 "index": [0, 1],  
 "data": [[16.99, 1.01], [10.34, 1.66]]  
}
```

### Concept

>Semi-nested structure

Hierarchy:

```python
dict  
 ├── list (columns)  
 ├── list (index)  
 ├── list of lists (data)
```
----------

## STEP 11: VERIFY EQUALITY

### Code Snippet

```python
df_records.equals(df_columns)
```

### Output

```python
True  
True  
True
```
### Concept

>Different formats → **same data**

----------

## STEP 12: ABOUT NESTED JSON

Note that in this data set of tips, we **did see nested JSON**, but only **simple nesting (2 levels)**
To see nested JSON, a nested JSON structure has been created as follows:-
```python
nested_json  = [  
 {  
  "name": "Alice",  
  "grades": {"math": 90, "english": 85}  
 },  
 {  
  "name": "Bob",  
  "grades": {"math": 80, "english": 75}  
 }  
]  
  
df_nested  =  pd.json_normalize(nested_json)  
print(df_nested)
```
### Output

```python
name   grades.math   grades.english  
Alice       90              85  
Bob         80              75
```

# The entire script in one block is given below:


```python

import pandas as pd
import json

# STEP 1: LOAD DATA FROM CSV
# Read a real dataset from an online source into a DataFrame

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)  # Load dataset into DataFrame

print("\nSTEP 1: ORIGINAL DATAFRAME")
print(df.head())

# OUTPUT HINT:
# total_bill   tip   sex   smoker   day   time   size
# 16.99        1.01 Female  No      Sun   Dinner  2 
# 10.34        1.66 Male    No      Sun   Dinner  3 
# And so on...


# STEP 2: SAVE DATA INTO DIFFERENT JSON FORMATS
# Same DataFrame is stored in different JSON structures using 'orient'

df.to_json("tips_records.json", orient="records")  # Row-wise list of dictionaries
df.to_json("tips_columns.json", orient="columns")  # Column-wise dictionary of dictionaries
df.to_json("tips_index.json", orient="index")  # Row index as keys with row data as dictionaries
df.to_json("tips_split.json", orient="split")  # Dictionary with 'columns', 'index', and 'data' keys

print("\nSTEP 2: JSON FILES CREATED")



# STEP 3: READ JSON (records) INTO DATAFRAME
# Pandas reconstructs the DataFrame using correct orientation

print("\nSTEP 3: DATAFRAME FROM records FORMAT")

df_records = pd.read_json("tips_records.json", orient="records")
print(df_records.head())

# OUTPUT HINT:
# Same as original DataFrame
# total_bill   tip   sex   smoker   day   time   size
# 16.99        1.01 Female  No      Sun   Dinner  2 
# 10.34        1.66 Male    No      Sun   Dinner  3 
# And so on...

# STEP 4: VIEW RAW JSON STRUCTURE (records)
# Using Python's json module to see actual stored format

print("\nSTEP 4: RAW JSON (records FORMAT)")

with open("tips_records.json", "r") as f:
    data_records = json.load(f)

print(type(data_records))

# Show only first 2 rows to avoid huge output
print(data_records[:2])

# OUTPUT HINT:
# <class 'list'>
# [{'total_bill': 16.99, 'tip': 1.01, ...}, {...}]
# List of dictionaries → each dict = one row

# STEP 5: READ JSON (columns) INTO DATAFRAME

print("\nSTEP 5: DATAFRAME FROM columns FORMAT")

df_columns = pd.read_json("tips_columns.json", orient="columns")
print(df_columns.head())

# OUTPUT HINT:
# Same DataFrame again
# total_bill   tip   sex   smoker   day   time   size
# 16.99        1.01 Female  No      Sun   Dinner  2 
# 10.34        1.66 Male    No      Sun   Dinner  3 
# And so on...


# STEP 6: VIEW RAW JSON STRUCTURE (columns)

print("\nSTEP 6: RAW JSON (columns FORMAT)")

with open("tips_columns.json", "r") as f:
    data_columns = json.load(f)

print(type(data_columns))

keys = list(data_columns.keys())
print("Column names:", keys)  # Show all column names
print("First column data:", data_columns[keys[0]])  # Show data for the first column (total_bill) along with its row indices

# OUTPUT HINT:
# {'total_bill': {'0': 16.99, '1': 10.34, ...}}
# '0', '1', ... are row indices as keys in the column dictionary
# 16.99, 10.34, ... are the actual values for the 'total_bill' column



# STEP 7: READ JSON (index) INTO DATAFRAME

print("\nSTEP 7: DATAFRAME FROM index FORMAT")

df_index = pd.read_json("tips_index.json", orient="index")
print(df_index.head())

# OUTPUT HINT:
# Same table structure
# total_bill   tip   sex   smoker   day   time   size
# 16.99        1.01 Female  No      Sun   Dinner  2 
# 10.34        1.66 Male    No      Sun   Dinner  3 
# And so on...



# STEP 8: VIEW RAW JSON STRUCTURE (index)

print("\nSTEP 8: RAW JSON (index FORMAT)")

with open("tips_index.json", "r") as f:
    data_index = json.load(f)

print("type of data_index.json:->", type(data_index))  
# type of data_index.json:-> <class 'dict'>

keys = list(data_index.keys())
print("Row indices:", keys[:5])
# ['0', '1', '2', '3', '4']

print("First row data:", {keys[0]: data_index[keys[0]]})

# Output consists of a dictionary where each key is a row index and the value is another dictionary containing the full row data.
# {'0': {'total_bill': 16.99, 'tip': 1.01, 'sex': 'Female', 'smoker': 'No', 'day': 'Sun', 'time': 'Dinner', 'size': 2}, ...}    
# keys '0', '1', ... represent row indices,
# data_index[keys[0]] gives the full row data for the first row (index '0') as a dictionary.-,
# where the keys of this inner dictionary are the column names and the values are the corresponding 
# cell values for that row.

# STEP 9: READ JSON (split) INTO DATAFRAME

print("\nSTEP 9: DATAFRAME FROM split FORMAT")

df_split = pd.read_json("tips_split.json", orient="split")
print(df_split.head())
# total_bill  tip   sex   smoker   day   time   size
# 16.99        1.01 Female  No      Sun   Dinner  2 
# 10.34        1.66 Male    No      Sun   Dinner  3 
# And so on...

# Same DataFrame



# STEP 10: VIEW RAW JSON STRUCTURE (split)

print("\nSTEP 10: RAW JSON (split FORMAT)")

with open("tips_split.json", "r") as f:
    data_split = json.load(f)

print(type(data_split))  # <class 'dict'>

print("Columns:", data_split["columns"])
# Columns: ['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size']
# 'columns' contains a list of column names

print("Index (first 5):", data_split["index"][:5])
# Index (first 5): ['0', '1', '2', '3', '4']
# 'index' contains a list of row indices

print("Data (first 2 rows):", data_split["data"][:2])
# Data (first 2 rows): [[16.99, 1.01, 'Female', 'No', 'Sun', 'Dinner', 2], [10.34, 1.66, 'Male', 'No', 'Sun', 'Dinner', 3]]
# The 'split' format organizes the JSON into a dictionary with three keys: 'columns', 'index', and 'data'.
# 'data' contains a list of lists, 
# where each inner list represents a row of data corresponding to the columns.

# STEP 11: VERIFY ALL DATAFRAMES ARE IDENTICAL

print("\nSTEP 11: DATAFRAME EQUALITY CHECK")

print(df_records.equals(df_columns))
print(df_columns.equals(df_index))
print(df_index.equals(df_split))

# OUTPUT HINT:
# True
# True
# True



# STEP 12: EXAMPLE OF TRUE NESTED JSON (IMPORTANT CONCEPT)
# This shows deeper nesting like real-world APIs

print("\nSTEP 12: NESTED JSON EXAMPLE")

nested_json = [
    {
        "name": "Alice",
        "grades": {"math": 90, "english": 85}
    },
    {
        "name": "Bob",
        "grades": {"math": 80, "english": 75}
    }
]

print("Raw nested JSON:")
print(nested_json)

# Flatten nested JSON into DataFrame
df_nested = pd.json_normalize(nested_json)

print("\nFlattened DataFrame:")
print(df_nested)

# Output
# name  grades.math  grades.english
# Alice  90           85
# Bob    80           75

```















