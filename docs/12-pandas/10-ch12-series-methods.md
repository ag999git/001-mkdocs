# Methods of Series in Pandas

### Methods of Series in Pandas

For easy understanding and usage, I have divided the methods of Series in Pandas into "Pillars" or "macro-groups". The 4 "pillars" or "macro-groups" are shown in table below:

| Macro-Group                 | What it means                                                 | Merges these old categories                         |
| --------------------------- | ------------------------------------------------------------- | --------------------------------------------------- |
| 1. Inspection & Retrieval   | "Show me the data, or give it to me in a different format."   | Accessing/Viewing, Conversion/Export                |
| 2. Analysis & Summarization | "Give me the big picture. What are the trends and totals?"    | Descriptive Statistics, Counts/Unique               |
| 3. Cleaning & Manipulation  | "Fix the errors, remove the bad rows, and change the values." | Missing Data, Transformation, Filtering, Sorting    |
| 4. Type-Specific Operations | "This is text/time, treat it with special tools."             | String Operations (.str), DateTime Operations (.dt) |

### These 4 "Pillars" or "Macro-groups" contain a number of categories which are given below

1. Viewing & Accessing
2. Conversion & Export
3. Descriptive Statistics
4. Counts & Unique Values
5. Handling Missing Data
6. Filtering & Conditions
7. Transformation
8. Sorting & Ranking
9. String Methods (.str)
10. DateTime Methods (.dt)

### The Key methods of each category are given below:

| Pillar                      | Category               | Key Methods                | Brief Purpose                                      |
| --------------------------- | ---------------------- | -------------------------- | -------------------------------------------------- |
| 1. Inspection & Retrieval   | Viewing & Accessing    | .loc\[], .iloc\[]          | Select data by label or integer position.          |
|                             |                        | .head(), .tail()           | Preview the first or last n elements.              |
|                             |                        | .get()                     | Safe access (returns default if label is missing). |
|                             | Conversion & Export    | .to\_list()                | Convert Series to a standard Python list.          |
|                             |                        | .to\_dict()                | Convert Series to a Python dictionary.             |
|                             |                        | .to\_frame()               | Convert a 1D Series into a 2D DataFrame.           |
| 2. Analysis & Summarization | Descriptive Statistics | .sum(), .min(), .max()     | Basic arithmetic aggregates.                       |
|                             |                        | .mean(), .median(), .std() | Calculate central tendency and spread.             |
|                             |                        | .describe()                | Generate a complete summary statistics table.      |
|                             | Counts & Unique Values | .value\_counts()           | Count the frequency of each unique value.          |
|                             |                        | .unique(), .nunique()      | Get array of unique values or count of them.       |
| 3. Cleaning & Manipulation  | Handling Missing Data  | .isna() (or .isnull())     | Detect missing values (returns boolean mask).      |
|                             |                        | .fillna()                  | Fill NaN values with a specific value/method.      |
|                             |                        | .dropna()                  | Remove rows that contain missing values.           |
|                             | Filtering & Conditions | .between()                 | Filter values within a specific range.             |
|                             |                        | .isin()                    | Filter values present in a given list.             |
|                             |                        | .duplicated()              | Flag rows that have appeared before.               |
|                             | Transformation         | .map()                     | Substitute values using a dict or function.        |
|                             |                        | .apply()                   | Apply a custom function to all elements.           |
|                             |                        | .replace()                 | Swap out exact values (e.g., replace(1, 100)).     |
|                             |                        | .astype()                  | Cast the Series to a different data type.          |
|                             | Sorting & Ranking      | .sort\_values()            | Sort the Series by its actual data values.         |
|                             |                        | .sort\_index()             | Sort the Series by its index labels.               |
|                             |                        | .rank()                    | Assign a competitive rank to each value.           |
| 4. Type-Specific Operations | String Methods (.str)  | .str.upper(), .str.lower() | Convert string case.                               |
|                             |                        | .str.contains()            | Check if a substring/pattern exists.               |
|                             |                        | .str.replace()             | Replace parts of a string.                         |
|                             | DateTime Methods (.dt) | .dt.year, .dt.month        | Extract specific date components as integers.      |
|                             |                        | .dt.day\_name()            | Extract the name of the day (e.g., 'Monday').      |
|                             |                        | .dt.strftime()             | Format dates into custom string formats.           |

### Flowchart

The following diagram shows all the key methods grouped into categories and "Pillars"

![Flowchart of Methods of Series](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch12-pandas-series-methods.png)

![Flowchart of Methods of Series](../.gitbook/assets/ch12-pandas-series-methods.png)

### Script

The following script shows the usage of the various Series methods:-

```python

"""
PANDAS SERIES METHODS: THE 4 PILLARS

Methods grouped by how they are actually used in a data workflow.
"""

import pandas as pd
import numpy as np

# ============================================================================
# PILLAR 1: INSPECTION & RETRIEVAL
# Purpose: Looking at data or pulling it out of Pandas into standard Python
# ============================================================================

print("PILLAR 1: INSPECTION & RETRIEVAL")

scores = pd.Series([85, 90, 78, 92], index=['Alice', 'Bob', 'Charlie', 'Diana'])

# 1. --- VIEWING & ACCESSING ---
print("Original Data:\n", scores)

# .loc[] (by label) and .iloc[] (by position number). Can access by both label and position!
# But remember: .loc[] is for LABELS (like 'Bob') and .iloc[] is for INTEGER POSITIONS (like 0, 1, 2...)
print("\nGet Bob's score using label (.loc[]):", scores.loc['Bob'])  # Output: 90. Use the label 'Bob' to access his score
print("Get 3rd score using position (.iloc[]):", scores.iloc[2])  # Output: 78. Use the position number 2 to access the 3rd score

# .head() and .tail() to quickly peek at data
print("\nFirst 2 rows (.head()):\n", scores.head(2))  # Output: Alice and Bob's scores. .head(2) shows the first 2 rows
print("Last 2 rows (.tail()):\n", scores.tail(2))  # Output: Charlie and Diana's scores. .tail(2) shows the last 2 rows

# 2. --- EXPORTING / CONVERSION ---
# Sometimes you need to leave the Pandas world and go back to standard Python
print("\nConvert back to a Python list (.to_list()):", scores.to_list())  
# Output: [85, 90, 78, 92]. Converts the Series values to a regular Python list
print("Convert to a Python dictionary (.to_dict()):", scores.to_dict())  
# Output: {'Alice': 85, 'Bob': 90, 'Charlie': 78, 'Diana': 92}. Converts the Series to a dictionary where the index 
# labels become keys and the values become dictionary values
print("Convert 1D Series into a 2D DataFrame (.to_frame()):\n", scores.to_frame())  
# Output: A DataFrame with one column (the original Series values) and the same index labels. .to_frame() converts 
# the Series into a DataFrame format, which is 2D, while the original Series is 1D.


# ============================================================================
# PILLAR 2: ANALYSIS & SUMMARIZATION
# Purpose: Understanding the "big picture" without changing the original data
# ============================================================================
print("\n" + "="*60)
print("PILLAR 2: ANALYSIS & SUMMARIZATION")
print("="*60)

# 3. --- MATH & STATISTICS ---
prices = pd.Series([10, 20, 30, 40, 50])
print("Prices:\n", prices)

print("\nSum:", prices.sum())  # Output: 150. Adds up all the values in the Series
print("Min:", prices.min())  # Output: 10. Finds the smallest value in the Series
print("Max:", prices.max())  # Output: 50. Finds the largest value in the Series
print("Mean:", prices.mean())  # Output: 30. Calculates the average of the values in the Series
print("Median:", prices.median())  
# Output: 30. Finds the middle value when the values are sorted. If there is an even number of values, it averages 
# the two middle values.    
print("Average (Mean):", prices.mean()) # Output: 30. Calculates the average of the values in the Series
print("Minimum / Maximum:", prices.min(), "/", prices.max()) 
# Output: 10 / 50. Shows the minimum and maximum values in the Series

# .describe() does all the above at once (great for a quick health check)
print("\nSummary Table (.describe()):\n", prices.describe()) 
# Output: A table that includes count (number of non-missing values), mean, std (standard deviation), 
# min, 25% (1st quartile), 50% (median), 75% (3rd quartile), and max. 
# This gives a quick overview of the distribution and key statistics of the data in the Series.

# 4. --- COUNTING & FREQUENCY ---
fruits = pd.Series(['Apple', 'Banana', 'Apple', 'Orange', 'Apple'])  
# Output: A Series of fruit names, where 'Apple' appears 3 times, 'Banana' appears once, and 'Orange' appears once.
print("\nFruits:\n", fruits)

# How many unique items exist?
print("Unique items (.unique()):", fruits.unique())  
# Output: ['Apple', 'Banana', 'Orange']. Shows the unique values in the Series, without duplicates
print("Count of unique items (.nunique()):", fruits.nunique())  
# Output: 3. Counts how many unique values are in the Series
print("Frequency of each item (.value_counts()):\n", fruits.value_counts())  
# Output: A Series that counts how many times each unique value appears in the original Series. 
# For this example, it will show 'Apple' with a count of 3, 'Banana' with a count of 1, and 'Orange' with a count of 1. 
# This is very useful for understanding the distribution of categorical data.

# How many times does each item appear? (Very common in data analysis!)
print("Frequency table (.value_counts()):\n", fruits.value_counts())
# Output: A Series that counts how many times each unique value appears in the original Series. 
# For this example, it will show 'Apple' with a count of 3, 'Banana' with a count of 1, and 'Orange' with a count of 1. 
# This is very useful for understanding the distribution of categorical data.


# ============================================================================
# PILLAR 3: CLEANING & MANIPULATION
# Purpose: Fixing bad data, removing unwanted rows, or changing values
# ============================================================================
print("\n" + "="*60)
print("PILLAR 3: CLEANING & MANIPULATION")
print("="*60)

raw_data = pd.Series([15, np.nan, 35, 15, np.nan, 50])  
# Output: A Series with some numeric values (15, 35, 15, 50) and some missing values represented as NaN (Not a Number). 
# The NaN values indicate that there is missing or undefined data in those positions. 
# This is common in real-world datasets where some information may be incomplete or unavailable.
print("Raw Data (with missing NaN values):\n", raw_data)  
# Output: The original Series with the numeric values and NaN values as they are, showing the raw data before 
# any cleaning or manipulation has been done.

# 5. --- HANDLING MISSING DATA ---
print("\nFind missing data (.isna()):\n", raw_data.isna())  
# Output: A Series of boolean values indicating which elements are NaN (True) and which are not (False)
print("Fill holes with 0 (.fillna(0)):\n", raw_data.fillna(0))  # Output: A Series where all NaN values are replaced with 0
print("Drop the bad rows entirely (.dropna()):\n", raw_data.dropna())  # Output: A Series with all NaN values removed

# 6. --- FILTERING (Subsetting) ---
clean_data = raw_data.dropna()
print("\nFilter: Keep only values > 20:\n", clean_data[clean_data > 20])  # Output: A Series that includes only the values from clean_data that are greater than 20. In this case, it will show 35 and 50, since those are the only values in clean_data that are greater than 20.
print("Filter: Keep only values in a list [15, 50] (.isin()):\n", clean_data[clean_data.isin([15, 50])]) # Output: A Series that includes only the values from clean_data that are either 15 or 50. In this case, it will show 15 and 50, since those are the values in clean_data that match the list provided to .isin().

# 7. --- TRANSFORMING (Changing values) ---
print("\nAdd 5 bonus points to everyone (.apply()):\n", clean_data.apply(lambda x: x + 5))  
# Output: A Series where each value from clean_data has been increased by 5
print("Replace 15 with 18 (.replace()):\n", clean_data.replace(15, 18))  
# Output: A Series where all occurrences of 15 in clean_data are replaced with 18

# 8. --- SORTING ---
print("\nSort by values (.sort_values()):\n", clean_data.sort_values())  
# Output: A Series sorted by its values in ascending order
print("Assign ranks (1st, 2nd, 3rd...):\n", clean_data.rank())  
# Output: A Series where each value is replaced by its rank in the sorted order


# ============================================================================
# PILLAR 4: TYPE-SPECIFIC OPERATIONS
# Purpose: Using special "accessor" tools (.str and .dt) for text and dates
# ============================================================================
print("\n" + "="*60)
print("PILLAR 4: TYPE-SPECIFIC OPERATIONS (.str and .dt)") 
print("="*60)

# 9. --- STRING OPERATIONS ---
# You CANNOT do: sentences.upper(). You MUST use the .str gateway.
sentences = pd.Series(['hello world', 'python code'])  
# Output: A Series of strings, where the first element is 'hello world' and the second element is 'python code'. 
# This Series can be used to demonstrate string operations using the .str accessor in Pandas.
print("Strings:\n", sentences)

print("\nUpper case (.str.upper()):\n", sentences.str.upper())  
# Output: A Series where each string is converted to uppercase
print("Contains 'o'? (.str.contains()):\n", sentences.str.contains('o'))  
# Output: A Series of boolean values indicating whether each string contains the letter 'o'
print("Replace space with dash (.str.replace()):\n", sentences.str.replace(' ', '-'))  
# Output: A Series where spaces in each string are replaced with dashes

# 10. --- DATETIME OPERATIONS ---
# You CANNOT do: dates.year. You MUST use the .dt gateway.
dates = pd.Series(pd.date_range('2024-01-15', periods=3))  
# Output: A Series of datetime objects, starting from January 15, 2024, and including the next two consecutive 
# days (January 16 and January 17, 2024). 
# This Series can be used to demonstrate datetime operations using the .dt accessor in Pandas.
print("\nDates:\n", dates)

print("\nExtract Year (.dt.year):", dates.dt.year.tolist())  
# Output: A list of the years extracted from each date in the Series
print("Extract Month Name (.dt.day_name()):", dates.dt.day_name().tolist())  
# Output: A list of the day names extracted from each date in the Series


```
