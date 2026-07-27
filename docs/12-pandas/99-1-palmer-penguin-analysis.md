# Research Project: Exploring the Palmer Penguins Dataset

## Research Project: Exploring the Palmer Penguins Dataset (Solution in the online resource)

You are given a real-world dataset containing observations of penguins, including their species, island location, and physical measurements. **Problem Statement:** Using Python and pandas, perform a structured analysis of the Palmer Penguins dataset to understand its composition, clean the data, and derive meaningful insights.

### Tasks to Perform

#### 1. Load the Dataset

Load the dataset into a pandas DataFrame from an appropriate source (Excel/CSV/online dataset). Determine the size of the dataset (number of rows and columns).

#### 2. Explore the Structure

Display the column names and data types. View a small sample of the dataset. Present the data in a way that makes all column names easy to read at once.

#### 3. Work with Individual Columns

Select a categorical column (such as species). Display a few sample values from this column.

#### 4. Analyze Categorical Data

* Determine how many unique categories exist.
* Count the number of occurrences of each category.

#### 5. Generate Summary Statistics

* Produce a statistical summary of the dataset.
* Compare how summary statistics differ for numeric and non-numeric columns.

#### 6. Handle Missing Data

* Identify columns with missing values.
* Apply an appropriate strategy to handle missing data.
* Verify that the issue has been resolved.

#### 7. Improve Data Types

* Identify columns where data types can be optimized.
* Convert at least one suitable column to a more efficient type.
* Explain why this conversion is beneficial.

#### 8. Aggregate Data

* Group the dataset based on a categorical column (e.g., island).
* Compute the number of observations in each group. Present the result in a structured format.

#### 9. Visualize Results

* Create a suitable plot to represent the aggregated data.
* Clearly label axes and provide a meaningful title.

### Expected Outcome: By completing this project, you should be able to:

* Load and inspect real-world datasets
* Clean and prepare data for analysis Perform categorical and statistical analysis
* Use grouping and aggregation effectively Present insights visually using plots

## Project 1 (Solution)

#### 1. Dataset Details

* Source: Palmer Penguins Dataset (Gorman, Williams, Fraser 2014).
* Format: Excel file (**.xlsx**).
* License: CC0 (Public Domain).
* Columns: (Total 7 as follows)
  * **species** (Categorical): The penguin species (Adelie, Chinstrap, Gentoo).
  * **island** (Categorical): Island where observed (Dream, Torgersen, Biscoe).
  * **bill\_length\_mm** (Numerical): Length of the bill.
  * **bill\_depth\_mm** (Numerical): Depth of the bill.
  * **flipper\_length\_mm** (Numerical): Length of flipper.
  * **body\_mass\_g** (Numerical): Body mass in grams.
  * **sex** (Categorical): Male or Female.

#### 2. Learning Objectives

In this exercise, you will learn to:

1. Load data from an Excel file using **read\_excel()**.
2. Inspect DataFrame structure using **shape**, **columns**, and **dtypes**.
3. Rename columns and use **head().T** to view data transposed.
4. Analyze categorical data using **value\_counts()** and **describe()**.
5. Identify and remove missing data (**NaN**) using **isnull()** and **dropna()**.
6. Convert data types (e.g., Object to Category).
7. Aggregate data using **groupby()** to find counts per category.
8. Plot the aggregated data using **matplotlib**.

#### 3. The Python Script

Prerequisites: Ensure you have the **openpyxl** library installed to read Excel files:

`pip install openpyxl`

#### Step 1: Load Data and Inspect Shape

The first task in any data project is to load the data into the computer's memory.

For this exercise we will use the Palmer Penguins dataset is released under the CC0 (Creative Commons Zero) license. This dataset is built directly into the seaborn library. So you can use it from there. You can also use a direct link from GitHub: [**https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv**](https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv) **.** Once loaded, the data is stored in a variable called **`my_df`**, which is a DataFrame. Think of a DataFrame as a super-powered Excel spreadsheet inside Python. We use **`my_df.shape`** to instantly see how much data we have. It returns a tuple **(rows, columns)**. For example, **(344, 7)** means we have 344 penguins (rows) and 7 details (columns) recorded for each penguin.

```python
import  pandas  as  pd
import  seaborn  as  sns
import  matplotlib.pyplot  as  plt

# Step 1: Load Data and Inspect Shape
# Seaborn downloads the dataset automatically
my_df = sns.load_dataset('penguins')
# Get shape (rows, columns)
print(f'Shape: {my_df.shape}') # Output: (344, 7)
print(f'Rows: {my_df.shape[0]}') # Output: 344
print(f'Columns: {my_df.shape[1]}') # Output: 7
```

#### Step 2: Rename Column and Transpose View

Column names should always be clear and descriptive. The dataset originally calls the first column **'species'**, but we rename it to **`'penguin_species'`** to be more specific. We then use **`.head(1)`** to look at just the very first row of data. By adding **`.T`** (which stands for Transpose), we flip the table: the columns become rows and rows become columns. This is extremely useful when you have many columns, as it lets you read every column header vertically down the screen without scrolling sideways.

```python
# Step 2: Rename Column and Transpose View
# Rename the first column from 'species' to 'penguin_species'
my_df.rename(columns={'species': 'penguin_species'}, inplace=True)
# View first row transposed to see all column headers clearly
print('\nFirst row (Transposed):') # Column names as rows → for readability
print(my_df.head(1).T) # First row of data with column names as rows
```

#### Step 3: Check Data Types and Select Data

We verify the data type of each column and select a specific column to view the first few entries.We check this using .dtypes.

* **float64** means a decimal number (like 39.1).
* **object** usually means text or strings. We also learn how to select just one column (like **penguin\_species**) using square brackets **\['...']**. This extracts a Series, which is essentially a single list of data, rather than the whole table.

```python
# Step 3: Check Data Types and Select Data
# Check data types
print('\nData Types:') # Show data types of each column
print(my_df.dtypes)
# Select first 5 entries of the 'penguin_species' column
print('\nFirst 5 entries of species:')
print(my_df['penguin_species'].head(5))
```

#### Step 4: Analyze Categorical Data

When data represents categories (like Species or Island), we often want to know the variety and frequency.

* **nunique()** tells us how many unique categories exist (e.g., there are 3 types of penguins).
* **value\_counts()** is one of the most useful methods. It counts exactly how many times each category appears. For instance, it quickly tells us that there are more Adelie penguins in our dataset than Chinstrap penguins.

```python
# Step 4: Analyze Categorical Data
# Count unique species
print(f'\nUnique Species count: {my_df.penguin_species.nunique()}')

# Count of each species
print('\nSpecies distribution:')
print(my_df.penguin_species.value_counts()) # Counts each species in dataset
```

#### Step 5: Summarize Statistics

The **`describe()`** method provides a statistical summary. By default, it summarizes numeric columns; **`include='all'`** summarizes everything. It forces Pandas to calculate statistics for every column, both numeric and non-numeric (text/categories).

How it works: When you run **describe(include='all')**, Pandas looks at the data type of each column and decides which statistics are relevant:

1. For Numeric columns (int/float): It calculates count, mean, std, min, 25%, 50%, 75%, max.
2. For Non-Numeric columns (object/category): Concepts like "mean" or "standard deviation" don't exist for text. So, instead, it calculates: count, unique, top (most frequent value), and freq (frequency of that top value).

Since Pandas prints this as one big table, the columns that don't match a specific statistic will show NaN (Not a Number).

```python
# Step 5: Summarize Statistics
# Summary of ALL columns (numeric and categorical)
# For numeric columns: gives mean, std, min, max, etc.
# For text columns: gives unique count, top value, frequency, etc.
print('\nSummary of all data:')
print(my_df.describe(include='all'))
### <![if !supportLists]>12.1.9. <![endif]>Step 6: Handle Missing Data
```

In real-world data is rarely perfect and often gas "missing values". In Pandas, missing data is represented as **NaN** (Not a Number). First, we use **.isnull().sum()** to count how many such "missing values" are in each column. This is called "Data Profiling." Once we find missing values (in the **sex** column), we have to decide what to do. In this script, we use **.dropna()** to delete any row that has missing information. The argument **inplace=True** means "save these changes directly to **my\_df**," so we don't need to create a new variable.

```python
# Step 6: Handle Missing Data
# Check for NaN counts before cleaning
print('\nNull counts before cleaning:')
print(my_df.isnull().sum()) # No of Missing values (each column) before cleaning
# Drop rows where 'sex' is NaN and update the dataframe
my_df.dropna(subset=['sex'], inplace=True)
# Check that the NaN are removed
print('\nNull counts after cleaning:') #
print(my_df.isnull().sum()) # No of Missing values (each column) after cleaning
```

#### Step 7: Transform Data Types

Sometimes Python guesses the wrong data type. The **island** column contains words, but they are just names of locations, not sentences. We convert this column from a generic **object** (text) to a specific **category** type. In Pandas, **category** is a specific and distinct data type, just like **integer** (numbers), **float** (decimals), or **boolean** (True/False). This makes the computer more efficient.

```python
# Step 7: Transform Data Types
# Convert 'island' column from object to category for efficiency
my_df['island'] = my_df['island'].astype('category')
print('\nData types after converting island to category:')
print(my_df.dtypes)
```

#### Step 8: Aggregate Data (Grouping)

This step answers the question: "How many penguins are on each island?" We use a powerful concept called GroupBy.

1. Split: We tell Python to split the data into piles based on the **island** name (one pile for Biscoe, one for Dream, etc.).
2. Apply: We count the rows in each pile using **.agg('count')**.
3. Combine: We put the results back into a new DataFrame called **df\_penguins**. Finally, we clean up the result by renaming the generic column name to "Count" and setting the index name to "Island".

```python
# Step 8: Aggregate Data (Grouping)
# Group by 'island' and count entries
df_penguins = pd.DataFrame(my_df['island'].groupby(my_df.island).agg('count'))
# Rename the count column and the index
df_penguins.columns = ['Count']
df_penguins.index.names = ['Island']
print('\nPenguins per Island:')
print(df_penguins)
```

#### Step 9: Visualize Data

Visualizing data id often more insightful. We use **matplotlib**, Python's standard plotting library.

* **df\_penguins.plot(kind='bar')** tells Python to draw a bar chart.
* We set the X-axis to the Island names and the Y-axis to the Count.
* **plt.show()** is the final command that opens the window and displays the graph on your screen.
* We also apply a visual style (**seaborn-v0\_8-whitegrid**) to make the chart look modern and clean.

```python
# Step 9: Visualize Data
# Use a clean style (checking for compatibility with newer versions)
try:
    plt.style.use('seaborn-v0_8-whitegrid')
except:
    plt.style.use('seaborn')

ax = df_penguins.plot(kind='bar', color='skyblue', edgecolor='black')
# Set labels and title
ax.set_xlabel(df_penguins.index.name)
ax.set_ylabel('Count')
ax.set_title('Penguin Population per Island')
# Set x-tick labels to island names
ax.set_xticklabels(df_penguins.index, rotation=0)
plt.show()
```

### Flowchart showing flow of execution of above script

![Project1](../.gitbook/assets/ch12-project1-palmer-penguin.png)

#### The Difference Between object and category

<details>

<summary>The Difference Between object and category</summary>

\### The Difference Between object and category

1. **object** (The default for text): When Pandas reads text, it treats it as a generic "object." It stores the text exactly as it appears.

* How it works: If the word "Biscoe" appears 168 times in the dataset, the computer saves the word "Biscoe" 168 separate times in its memory.
* Pros: Very flexible. You can have anything in there (sentences, paragraphs, mixed text).
* Cons: It uses a lot of memory and can be slow if the text repeats over and over.

2. **category** (The optimized type for labels): The category data type is designed specifically for columns that have a limited, fixed set of values (like "Male/Female" or "Island Names").

* How it works: Instead of saving the word "Biscoe" 168 times, Pandas creates an internal "ID card" system.
* It assigns "Biscoe" an ID number (e.g., 0).
* It assigns "Dream" an ID number (e.g., 1).
* It assigns "Torgersen" an ID number (e.g., 2).
* In the actual data column, it only stores the numbers 0, 1, 2. It keeps a master list (a dictionary) that tells it 0 = Biscoe.
* Pros: It uses much less memory and makes calculations (like grouping or sorting) much faster.
* Cons: You can only use it if the number of unique words is small. If every single row had a different unique name, this type wouldn't help.

**Why we use it for island:** In the Penguin dataset, there are only 3 islands (Biscoe, Dream, Torgersen), but there are 344 rows. Since those 3 names repeat hundreds of times, converting the column to category is much more efficient for the computer.

</details>

### The entire script as a single block is given below:-

```python

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load Data and Inspect Shape
# Seaborn downloads the dataset automatically
my_df = sns.load_dataset('penguins')  # Load Palmer Penguins dataset in DataFrame

# Get shape (rows, columns)
print(f'Shape: {my_df.shape}')  # Output: (344, 7)
print(f'Rows: {my_df.shape[0]}')  # Output: 344
print(f'Columns: {my_df.shape[1]}')  # Output: 7

# Step 2: Rename Column and Transpose View
# Rename the first column from 'species' to 'penguin_species'
my_df.rename(columns={'species': 'penguin_species'}, inplace=True)

# View first row transposed to see all column headers clearly
print('\nFirst row (Transposed):')  # Column names as rows → for readability
print(my_df.head(1).T)  # First row of data with column names as rows

# Step 3: Check Data Types and Select Data
# Check data types
print('\nData Types:')  # Show data types of each column
print(my_df.dtypes)

# Select first 5 entries of the 'penguin_species' column
print('\nFirst 5 entries of species:')  
print(my_df['penguin_species'].head(5))

# Step 4: Analyze Categorical Data

# Count unique species
print(f'\nUnique Species count: {my_df.penguin_species.nunique()}')

# Count of each species
print('\nSpecies distribution:')
print(my_df.penguin_species.value_counts())  # Counts each species in dataset

# Step 5: Summarize Statistics
# Summary of ALL columns (numeric and categorical)
# For numeric columns: gives mean, std, min, max, etc.
# For text columns: gives unique count, top value, frequency, etc.
print('\nSummary of all data:')
print(my_df.describe(include='all'))

# Step 6: Handle Missing Data
# Check for NaN counts before cleaning
print('\nNull counts before cleaning:')
print(my_df.isnull().sum())  # Missing values (each column) before cleaning

# Drop rows where 'sex' is NaN and update the dataframe
my_df.dropna(subset=['sex'], inplace=True)  

# Check that the NaN are removed
print('\nNull counts after cleaning:')  
print(my_df.isnull().sum()) #No of Missing values (each column) after cleaning

# Step 7: Transform Data Types
# Convert 'island' column from object to category for efficiency
my_df['island'] = my_df['island'].astype('category')
print('\nData types after converting island to category:')
print(my_df.dtypes)

# Step 8: Aggregate Data (Grouping)
# Group by 'island' and count entries. Gives number of penguins on each island
df_penguins = pd.DataFrame(my_df['island'].groupby(my_df.island).agg('count'))

# Rename the count column and the index for clarity
df_penguins.columns = ['Count']
df_penguins.index.names = ['Island']

print('\nPenguins per Island:')
print(df_penguins)

# Step 9: Visualize Data

# Use a clean style (checking for compatibility with newer versions)
try:
    plt.style.use('seaborn-v0_8-whitegrid')
except:
    plt.style.use('seaborn')

ax = df_penguins.plot(kind='bar', color='skyblue', edgecolor='black')

# Set labels and title
ax.set_xlabel(df_penguins.index.name)
ax.set_ylabel('Count')
ax.set_title('Penguin Population per Island')

# Set x-tick labels to island names
ax.set_xticklabels(df_penguins.index, rotation=0)

plt.show()

```

### The resulting plot is as follows

![Plot](../.gitbook/assets/ch12-project1-palmer-penguin-image.png)
