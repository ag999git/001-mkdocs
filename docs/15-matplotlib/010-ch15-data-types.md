


## Data Types and Data Visualization Before Learning Matplotlib

**Objective:** Before visualizing data or writing any code, a data scientist must understand the anatomy of their data.

**The Research Question:** "Given a dataset with variables of different types—nominal, ordinal, interval, and ratio—how does one systematically decide which type of plot (line, bar, scatter, histogram, pie, box, heatmap, etc.) is most appropriate, and what are the consequences of choosing an inappropriate visualization?"

In this project, you will investigate how the fundamental types of statistical data dictate the geometric forms (plots) used to represent them. Choosing the wrong plot can distort the truth or obscure critical insights.
## Chapter Introduction

Before learning Matplotlib, it is important to understand the nature of data. Different types of data require different kinds of visual representation. A graph that is suitable for one type of data may be completely unsuitable for another.

For example:

-   A line graph is excellent for showing changes over time.
-   A bar chart is useful for comparing categories.
-   A histogram is useful for understanding distribution.
-   A scatter plot helps identify relationships between variables.

Therefore, data visualization is not merely about drawing graphs. It is about selecting the most meaningful visual representation for the given data.

In this chapter, we shall study:

1.  Types of data
2.  Types of plots
3.  Relationship between data and visualization
4.  How to choose an appropriate graph
5.  Common mistakes in visualization

This understanding forms the conceptual foundation required before learning Matplotlib programming.

## Types of Data

Data can broadly be classified into the following categories:

| Data Type | Description | Examples |
| --- | --- | --- |
| Nominal Data | Categories without order | Gender, Blood Group, City |
| Ordinal Data | Categories with order | Rank, Grades, Satisfaction Level |
| Interval Data | Numeric data without true zero | Temperature in Celsius |
| Ratio Data | Numeric data with true zero | Height, Weight, Age |
| Discrete Data | Countable values | Number of students |
| Continuous Data | Measurable values | Time, Distance, Speed |


## 1. Nominal Data

Nominal data represents categories or labels. The categories do not possess any natural order.

Examples:

-   Colours
-   Religion
-   Country names
-   Types of vehicles

Suitable plots:

-   Bar chart
-   Pie chart

Unsuitable plots:

-   Line graph

----------

## 2. Ordinal Data

Ordinal data contains categories that possess a meaningful order.

Examples:

-   Class ranks
-   Satisfaction levels
-   Education levels

Suitable plots:

-   Ordered bar charts
-   Horizontal bar charts

----------

## 3. Interval Data

Interval data consists of numeric values where differences are meaningful but zero does not indicate absence.

Example:

-   Temperature in Celsius

----------

## 4. Ratio Data

Ratio data has all properties of interval data and also contains a true zero.

Examples:

-   Weight
-   Height
-   Income

Suitable plots:

-   Histogram
-   Scatter plot
-   Box plot
-   Line graph

----------

## 5. Discrete Data

Discrete data consists of countable values.

Examples:

-   Number of books
-   Number of cars

Suitable plots:

-   Bar chart
-   Stem plot

----------

## 6. Continuous Data

Continuous data can take infinitely many values within a range.

Examples:

-   Height
-   Speed
-   Temperature

Suitable plots:

-   Histogram
-   Density plot
-   Line graph

### Comparison of properties of the various data types

| Property | Nominal | Ordinal | Interval | Ratio |
| --- | --- | --- | --- | --- |
| Categories/Labels | Yes | Yes | No | No |
| Meaningful Order | No | Yes | Yes | Yes |
| Equal Intervals | No | No | Yes | Yes |
| True Zero | No | No | No | Yes |
| Arithmetic Mean | No | No | Yes | Yes |
| Median | No | Yes | Yes | Yes |
| Mode | Yes | Yes | Yes | Yes |
| Examples | Color, Gender, Country | Rank, Rating, Grade | Temperature (°C), Year | Height, Weight, Income |
| Also Called | Named, Categorical (unordered) | Categorical (ordered) | Scaled, Numeric (no zero) | Scaled, Numeric (with zero) |




### Further differentiation of data types on various parameters/ characteristics

| Data Type | Description | Ordering Meaningful? | Arithmetic Meaningful? | True Zero Exists? | Nature of Values | Examples | Suitable Plots | Common Mistake |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Nominal Data | Categories or labels without any natural order | No | No | No | Qualitative | Gender, Blood Group, City, Religion, Department | Bar Chart, Pie Chart | Using line graphs for unrelated categories |
| Ordinal Data | Categories having meaningful order or ranking | Yes | Limited | No | Qualitative | Rank, Grades, Satisfaction Level, Education Level | Ordered Bar Chart, Horizontal Bar Chart | Assuming equal spacing between categories |
| Interval Data | Numeric data where differences are meaningful but zero is arbitrary | Yes | Addition/Subtraction only | No | Quantitative | Temperature in Celsius/Fahrenheit, Calendar Years | Line Plot, Histogram | Interpreting ratios meaningfully |
| Ratio Data | Numeric data having meaningful differences and true zero | Yes | Yes | Yes | Quantitative | Height, Weight, Age, Salary, Distance | Scatter Plot, Histogram, Box Plot, Line Plot | Ignoring scale or outliers |
| Discrete Data | Countable numeric values | Yes | Yes | Usually Yes | Quantitative | Number of students, Cars sold, Books issued | Bar Chart, Stem Plot | Treating as continuous data |
| Continuous Data | Measurable values that can take infinitely many values within a range | Yes | Yes | Usually Yes | Quantitative | Time, Distance, Speed, Temperature, Height |  |  |


## Plot types








| Plot Type | Primary Purpose | Best Suitable For | Type of Data Required | Main Strength | Main Limitation | Real-World Examples | Unsuitable For | Important Observation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Line Plot | Showing trends and changes over continuous intervals | Continuous and time-series data | Continuous numeric data | Clearly shows trends and movement over time | Misleading for unrelated categories | Stock prices, temperature changes, rainfall trends | Nominal categories | Consecutive points imply continuity |
| Bar Chart | Comparing categories | Nominal and ordinal data | Categorical or discrete data | Easy comparison between groups | Becomes cluttered with too many categories | Survey results, sales comparison, student strength by department | Continuous distributions | Height of bars represents magnitude |
| Histogram | Analysing distribution and frequency | Continuous numeric data | Continuous data grouped into intervals | Shows spread, concentration, and skewness | Exact values difficult to identify | Age distribution, marks distribution, salary analysis | Nominal categories | Adjacent bars touch because data is continuous |
| Scatter Plot | Studying relationships between two variables | Ratio and interval data | Two numeric variables | Reveals correlation, clusters, and outliers | Difficult to interpret for extremely large datasets | Height vs weight, advertising vs sales | Pure categorical data | Useful for detecting patterns and anomalies |
| Pie Chart | Showing proportions of a whole | Nominal categorical data | Categorical data with percentages | Simple visual representation of parts of a whole | Difficult comparison when many categories exist | Budget allocation, market share, election votes | Continuous data and large datasets | Total of all slices represents 100% |
| Box Plot | Showing spread, median, and outliers | Continuous numeric data | Continuous data | Excellent summary of distribution | Less intuitive for beginners | Salary comparison, exam score analysis | Small categorical datasets | Quickly identifies outliers |
| Area Plot | Showing cumulative trends over time | Time-series data | Continuous numeric data | Emphasizes total magnitude over time | Overlapping areas may confuse interpretation | Population growth, cumulative sales | Independent categories | Similar to line plot but filled with colour |
| Heatmap | Showing intensity, density, or correlation | Matrix and tabular data | Numerical matrix data | Excellent for pattern recognition | Exact values harder to interpret visually | Correlation matrices, attendance tracking, weather intensity maps | Small simple datasets | Colour intensity represents magnitude |


### Additional Comparison Table

| Plot Type | Best For Comparison | Best For Trend Analysis | Best For Distribution | Best For Relationship Analysis | Best For Outlier Detection |
| --- | --- | --- | --- | --- | --- |
| Line Plot | Moderate | Excellent | Poor | Poor | Poor |
| Bar Chart | Excellent | Poor | Poor | Poor | Poor |
| Histogram | Moderate | Poor | Excellent | Poor | Moderate |
| Scatter Plot | Moderate | Moderate | Poor | Excellent | Excellent |
| Pie Chart | Limited | Poor | Poor | Poor | Poor |
| Box Plot | Moderate | Poor | Excellent | Poor | Excellent |
| Area Plot | Moderate | Excellent | Poor | Poor | Poor |
| Heatmap | Excellent | Moderate | Moderate | Excellent | Moderate |



### Quick Plot Selection Guide

| Situation | Recommended Plot |
| --- | --- |
| Comparing categories | Bar Chart |
| Showing changes over time | Line Plot |
| Showing distribution | Histogram |
| Showing relationship between variables | Scatter Plot |
| Showing percentages or proportions | Pie Chart |
| Detecting outliers | Box Plot |
| Showing cumulative growth | Area Plot |
| Showing correlations or intensity | Heatmap |

## Important Conceptual Notes

### 1. Line Plot vs Bar Chart

-   Line plots imply continuity.
-   Bar charts compare independent categories.

Therefore:

-   Monthly temperature → Line Plot
-   Population of cities → Bar Chart

----------

### 2. Histogram vs Bar Chart

Although both use bars, they are fundamentally different.


| Histogram | Bar Chart |
| --- | --- |
| Continuous data | Categorical data |
| Bars touch | Bars separated |
| Shows distribution | Shows comparison |


### 3. Scatter Plot Importance

Scatter plots are extremely important in:

-   Data science
-   Machine learning
-   Statistics

They help identify:

-   Positive correlation
-   Negative correlation
-   No correlation
-   Clusters
-   Outliers

----------

### Common Visualization Mistakes

| Mistake | Problem Created |
| --- | --- |
| Using pie charts for many categories | Difficult interpretation |
| Using line plots for nominal data | False trends implied |
| Excessive colours | Visual clutter |
| Using 3D effects unnecessarily | Distorted perception |
| Wrong scaling | Misleading conclusions |



### Script 1

Given below is a  Python script that uses the famous **"tips"** dataset from Seaborn. It acts as an excellent teaching tool because it contains all four major data types in a single, small dataframe:

-   **Nominal:** `sex`, `smoker`, `day` (unordered categories)
    
-   **Ordinal:** `time` (Lunch $\rightarrow$ Dinner has a clear sequence)
    
-   **Interval/Ratio:** `total_bill`, `tip`, `size` (numerical measurements)

```python

import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load a built-in dataset from Seaborn
# This dataset contains an excellent mix of Nominal, Ordinal, and Ratio data.
data = sns.load_dataset("tips")  # A dataset about restaurant tips, perfect for demonstrating various data types.

# 2. Set up a Matplotlib figure with a grid of subplots (2 rows, 2 columns)
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))
fig.suptitle(
    "Mapping Data Types to Matplotlib Visualizations",  # Overall title for the entire figure
    fontsize=16,  # Font size for the title
    fontweight="bold",  # Make the title bold for emphasis
)

# ------------------------------------------------------------------
# SUBPLOT 1: LINE PLOT (Ordinal/Sequential Data)
# Scenario: Showing average bill trend across the day's timeline (Lunch -> Dinner)
# ------------------------------------------------------------------
# Grouping data by time order
# We use 'observed=False' to ensure that the order of time categories is preserved 
# as they appear in the dataset (Lunch, Dinner).
time_trends = data.groupby("time", observed=False)["total_bill"].mean()

axes[0, 0].plot(
    time_trends.index,  # The time categories (Lunch, Dinner) on the x-axis
    time_trends.values,  # The average total bill amounts on the y-axis
    marker="o",          # Add markers to the line plot for better visibility of data points
    color="#0d47a1",   # A deep blue color for the line
    linewidth=2.5,       # Thicker line for better visibility
)
# set_title, set_xlabel, and set_ylabel are used to add titles and labels to the axes for clarity.
# The grid is added for better readability of the plot.
axes[0, 0].set_title("1. Line Plot (Ordinal Timeline)", fontsize=12, pad=10)
axes[0, 0].set_xlabel("Time of Day (Ordered Sequence)")
axes[0, 0].set_ylabel("Avg. Total Bill ($)")
axes[0, 0].grid(True, linestyle="--", alpha=0.6)


# ------------------------------------------------------------------
# SUBPLOT 2: BAR CHART (Nominal / Categorical Comparison)
# Scenario: Comparing discrete counts of transactions across different days
# ------------------------------------------------------------------
day_counts = data["day"].value_counts()  # Count the number of transactions for each day of the week (Nominal categories)

axes[0, 1].bar(
    day_counts.index,   # The unique day categories (e.g., Thur, Fri, Sat, Sun) on the x-axis
    day_counts.values,   # The count of transactions for each day on the y-axis
    color="#4caf50",   # A vibrant green color for the bars
    edgecolor="#1b5e20"  # A darker green for the edges of the bars to enhance visual separation
)
# set_title, set_xlabel, and set_ylabel are used to add titles and labels to the axes for clarity.
axes[0, 1].set_title("2. Bar Chart (Nominal Comparison)", fontsize=12, pad=10)
axes[0, 1].set_xlabel("Day of the Week (Unordered)")
axes[0, 1].set_ylabel("Number of Tables Served")


# ------------------------------------------------------------------
# SUBPLOT 3: HISTOGRAM (Continuous Ratio Data Distribution)
# Scenario: Visualizing how the continuous variable 'total_bill' is spread out
# ------------------------------------------------------------------
axes[1, 0].hist(
    data["total_bill"],       # The continuous variable 'total_bill' on the x-axis
    bins=15,                  # Number of bins to divide the total bill amounts into for the histogram
    color="#ff9800",        # A bright orange color for the bars
    edgecolor="#e65100",    # A darker orange for the edges of the bars
    alpha=0.8                 # Transparency level for better visual appeal
)
axes[1, 0].set_title(
    "3. Histogram (Continuous Ratio Distribution)",   # Title for the histogram subplot
    fontsize=12,     # Font size for the subplot title
    pad=10    # Padding to add space between the title and the plot for better readability
)
# set_xlabel and set_ylabel are used to label the axes, providing context for what the histogram represents.
axes[1, 0].set_xlabel("Total Bill Amount ($)")
axes[1, 0].set_ylabel("Frequency (Count)")


# ------------------------------------------------------------------
# SUBPLOT 4: SCATTER PLOT (Ratio vs. Ratio Correlation)
# Scenario: Checking the mathematical relationship between Total Bill and Tips
# ------------------------------------------------------------------
axes[1, 1].scatter(  # We use a scatter plot to visualize the relationship between two continuous Ratio variables: 'total_bill' and 'tip'.
    data["total_bill"],   # The total bill amounts on the x-axis
    data["tip"],   # The tip amounts on the y-axis
    color="#e91e63",   # A vibrant pink color for the scatter points to make them stand out
    alpha=0.7,   # Set transparency to 0.7 for better visibility when points overlap
    edgecolors="none"  # Remove edge colors for a cleaner look of the scatter points
)
# set_title, set_xlabel, and set_ylabel are used to add titles and labels to the axes for clarity.
axes[1, 1].set_title(
    "4. Scatter Plot (Ratio vs. Ratio Relationship)", fontsize=12, pad=10
)
# The grid is added to the scatter plot to enhance readability and make it easier to see the distribution of points.
axes[1, 1].set_xlabel("Total Bill ($)")
axes[1, 1].set_ylabel("Tip Given ($)")
axes[1, 1].grid(True, linestyle="--", alpha=0.4)


# 3. Clean up the layout and render the plots
plt.tight_layout()

# Save the figure for the GitHub README documentation automatically
plt.savefig("data_types_visualization_matrix.png", dpi=300)

# Display the window to the student
plt.show()


```

#### The resulting plot is as follows:-

![Four plots](/resources/ch15-4-plots.png)



### Case Study: Analyzing Continuous Groups with Box Plots

When exploring data, you will often find yourself needing to compare a continuous numerical variable against distinct qualitative groups. For instance, if you are looking at a dataset of wild animals, you might wonder: _How does physical weight vary across different species? Do some species run a wider range of sizes while others remain uniform?_ To answer these questions visually, we use a **Box Plot** (sometimes called a box-and-whisker plot). A box plot is uniquely suited for mapping a **Ratio scale** variable (where values are measurable and have a true absolute zero, like weight in grams) across a **Nominal scale** variable (where values are purely distinct categories with no inherent order, like species names).

The following script loads a famous, real-world biological dataset called `penguins` using the Seaborn library. It cleans the data and uses a unified approach—combining the quick, automated charting power of Seaborn with the granular structural control of Matplotlib—to generate a professional distribution dashboard.

```python

import matplotlib.pyplot as plt
import seaborn as sns

# ==============================================================================
# STEP 1: LOADING THE REAL-WORLD DATASET
# ==============================================================================
# We fetch the built-in 'penguins' dataset from Seaborn.
# This dataset is ideal for teaching because it cleanly separates categories from measurements.
# We use '.dropna()' to instantly remove any rows containing missing or blank values,
# ensuring Matplotlib doesn't encounter gaps or null values while drawing.
penguins = sns.load_dataset("penguins").dropna()


# ==============================================================================
# STEP 2: INITIALIZING THE MATPLOTLIB CANVAS
# ==============================================================================
# We create a single figure (the window) and a single axis (the plot grid area).
# 'figsize=(8, 6)' sets the window dimensions to 8 inches wide by 6 inches tall,
# providing an ideal square-like aspect ratio for viewing a box plot.
# 'fig' is the overall figure object, and 'ax' is the specific subplot (axis) where we will draw our box plot.
fig, ax = plt.subplots(figsize=(8, 6))


# ==============================================================================
# STEP 3: RENDERING THE BOX PLOT WITH SEABORN
# ==============================================================================
# We use Seaborn to draw the box plot, but we explicitly tell it to draw on our
# Matplotlib axis using 'ax=ax'. This blends the ease of Seaborn with the layout control of Matplotlib.
#
# Data-to-Axis Mapping:
# - x="species": This is our Nominal (Categorical) variable. It creates 3 distinct columns.
# - y="body_mass_g": This is our Ratio (Numerical) variable. It sets the vertical weight scale.
# - hue="species": This tells Seaborn to color each species box differently.
# - legend=False: Since the species names are already written on the X-axis, we turn off 
#   the redundant floating legend box to keep the chart clean.
# - palette="pastel": Applies a soft, highly readable color scheme to the boxes.
sns.boxplot(
    data=penguins,        # The DataFrame containing our data, which includes both the 'species' and 'body_mass_g' columns.
    x="species",          # The column name in the DataFrame that contains the categorical variable (Nominal) we want to plot on the x-axis.
    y="body_mass_g",      # The column name in the DataFrame that contains the numerical variable (Ratio) we want to plot on the y-axis.
    hue="species",        # This parameter tells Seaborn to color the boxes based on the 'species' categories, creating a visual distinction between them.
    legend=False,         # This parameter disables the legend that would normally be created by the 'hue' parameter, since the x-axis labels already indicate the species.
    ax=ax,                # This tells Seaborn to draw the box plot on the specific Matplotlib axis 'ax' that we created earlier, allowing us to customize the layout and appearance using Matplotlib functions.
    palette="pastel"      # This sets the color palette for the boxes to a soft pastel scheme, enhancing visual appeal and readability.
)


# ==============================================================================
# STEP 4: CUSTOMIZING LABELS AND GRAPHICAL TITLES
# ==============================================================================
# A professional plot must clearly tell the viewer what the axes and data represent.
# 'pad=15' adds a clean visual breathing space between the title text and the top of the chart grid.
ax.set_title("Distribution of Penguin Body Mass by Species", fontsize=14, fontweight="bold", pad=15)

# Give explicit, human-readable labels to our axes instead of relying on raw variable names.
ax.set_xlabel("Penguin Species (Nominal Category)", fontsize=11, labelpad=10)
ax.set_ylabel("Body Mass in Grams (Ratio Scale)", fontsize=11, labelpad=10)


# ==============================================================================
# STEP 5: AESTHETIC POLISH & RENDER
# ==============================================================================
# We add a horizontal grid along the Y-axis. This makes it incredibly easy for students
# to look across from a box's median line or an outlier dot and read its exact numerical value.
# 'linestyle="--"' makes the grid lines dashed, and 'alpha=0.5' makes them faint and non-distracting.
ax.grid(True, axis="y", linestyle="--", alpha=0.5)

# 'tight_layout' automatically cleans up the margins so no axis labels or titles get clipped or cut off.
plt.tight_layout()

# Save a high-resolution (300 dots-per-inch) image file directly into your working directory.
# This image can be uploaded directly to your GitHub accompanying resource repository.
plt.savefig("penguins_boxplot_distribution.png", dpi=300)

# Finally, launch the interactive window on the student's screen so they can view their work.
plt.show()

```

#### Resulting plot is shown below

![Box plot](/resources/ch15-box-plot.png)

### Explanation (of the Script)

Now that you have run the code, let’s dissect exactly **how** Python constructed this chart and **why** certain structural choices were made.

#### 1. The Anatomy of a Box Plot

A box plot compresses hundreds of rows of data into a clean, five-number summary. When you look at the boxes generated on your screen, here is how to read them:

-   **The Box (Interquartile Range / IQR):** The main colored body of each box represents the middle **50%** of that penguin species' population. The bottom edge of the box is the 25th percentile (Q1), and the top edge is the 75th percentile (Q3).
    
-   **The Center Line (The Median):** The solid horizontal line slicing through the inside of the box represents the **Median** (the exact middle value of the dataset).
    
-   **The Whiskers:** The vertical lines extending out from the top and bottom of the boxes show the overall variability and spread of the remaining data points.
    
-   **The Floating Dots (Outliers):** Any individual dots drawn past the tips of the whiskers are mathematically classified as **outliers**. These represent unusually light or abnormally heavy penguins that fall far outside the expected norms for their specific species.
    

#### 2. Mechanics of the Code: How it Works

-   **Data Cleansing with `.dropna()`:** Real-world datasets often suffer from missing entries where a field scientist forgot to log a measurement. Passing `.dropna()` tells Pandas to instantly purge those incomplete rows. If we skip this step, Matplotlib might flag errors or create skewed gaps when calculating statistical distributions.
    
-   **The Seaborn-Matplotlib Alliance (`ax=ax`):** While we use `sns.boxplot()` to draw the actual shapes, we pass `ax=ax` as an argument. This is a critical hybrid workflow pattern. It means we use Seaborn for its beautiful default math and color palettes, but we retain Matplotlib's powerful `ax.set_title()` and `ax.grid()` syntax to shape the outer frame.
    
-   **The Modern `hue` and `legend` Rule:** In modern data visualization workflows, passing a custom color `palette` requires us to explicitly declare a `hue` parameter. Because mapping `hue="species"` tells Python exactly how to distribute the color layout, it automatically generates a floating side-legend box. Since the category names are already written directly under each column on our X-axis, we explicitly use `legend=False` to drop the redundant legend box and keep our visual canvas clean.
    
-   **Enhancing Readability with a Y-Axis Grid:** By explicitly invoking `ax.grid(True, axis="y")`, we place light, non-distracting dashed lines across the background horizontally. This simple design decision significantly upgrades the chart's user experience, allowing a reader's eyes to trace a straight line from a penguin's outlier dot over to the Y-axis to instantly read its weight in grams.


## Script 3: The Histogram (Visualizing Single-Variable Distribution)

### Explanatory Note of the Script

When you are handed a column full of continuous numeric data (like a list of salaries, home prices, or test scores), looking at the raw numbers tells you very little. You need to know how those numbers are distributed. _Are most values clustered in the lower range? Is there a long tail of high values? Is the distribution symmetrical like a bell curve, or is it skewed?_

To answer this, we use a **Histogram**. A histogram cuts a continuous numerical variable into equal intervals called **"bins"** and counts how many data points fall into each bin. The height of each bar represents the frequency (count) of data points within that range.

The script below uses the real-world `tips` dataset from Seaborn to show exactly how the continuous ratio variable `total_bill` behaves across an establishment's transactions.

```python

import matplotlib.pyplot as plt
import seaborn as sns

# ==============================================================================
# STEP 1: LOAD THE REAL-WORLD DATASET
# ==============================================================================
# We fetch the built-in 'tips' dataset from Seaborn. 
# This dataset contains a continuous 'total_bill' column tracking restaurant bills.
tips = sns.load_dataset("tips")

# ==============================================================================
# STEP 2: INITIALIZE THE MATPLOTLIB CANVAS
# ==============================================================================
# Set up a single plot canvas measuring 8 inches wide by 6 inches tall.
# 'fig' is the overall figure object, and 'ax' is the specific subplot (axis) where we will draw our histogram.
fig, ax = plt.subplots(figsize=(8, 6))

# ==============================================================================
# STEP 3: RENDER THE HISTOGRAM
# ==============================================================================
# We use Matplotlib's native ax.hist() function.
# - data: tips["total_bill"] (The continuous numerical variable)
# - bins=15: Cuts the bill range into 15 equal slices along the X-axis.
# - color: Sets the main bar fill color.
# - edgecolor: Draws a clean darker border around each bar so they don't blend together.
# - alpha=0.8: Adds slight transparency so the chart feels light and professional.
ax.hist(
    tips["total_bill"],     # The 'total_bill' column from the 'tips' dataset, which contains continuous numerical values representing the total bill amounts for each transaction. This is the data we want to visualize in the histogram.
    bins=15,                # This parameter specifies that we want to divide the range of 'total_bill' values into 15 equal-width bins (or intervals). Each bin will count how many 'total_bill' values fall into that range, which is essential for creating the histogram.
    color="#ff9800",      # This sets the fill color of the bars in the histogram to a vibrant orange, making the chart visually appealing and easy to read.
    edgecolor="#e65100",  # This sets the color of the edges (borders) of the bars to a darker orange, which helps to visually separate each bar and enhance readability.
    alpha=0.8               # This sets the transparency level of the bars to 0.8 (on a scale from 0 to 1), making the bars slightly transparent. This can help to reduce visual clutter and give the chart a more polished, professional look.
)

# ==============================================================================
# STEP 4: CUSTOMIZE TITLES AND LABELS
# ==============================================================================
ax.set_title("Distribution of Restaurant Total Bills", fontsize=14, fontweight="bold", pad=15)
ax.set_xlabel("Total Bill Amount ($) (Continuous Ratio Scale)", fontsize=11, labelpad=10)
ax.set_ylabel("Frequency / Count of Tables", fontsize=11, labelpad=10)

# ==============================================================================
# STEP 5: AESTHETIC POLISH & DISPLAY
# ==============================================================================
# Add a dashed background grid along the Y-axis to make reading counts effortless.
ax.grid(True, axis="y", linestyle="--", alpha=0.4)

# Optimize canvas margins and output the chart.
plt.tight_layout()    # Automatically adjusts subplot parameters to give specified padding and prevent clipping of labels and titles.
plt.savefig("total_bill_histogram.png", dpi=300)    # Save the figure as a high-resolution PNG file for documentation purposes.
plt.show()

```

### The resulting plot is as follows

![Histogram](/resources/ch15-histogram.png)



#### Explanatory Note of the Script

Now that you have rendered the plot, let’s explore the technical nuances your students should look for:

-   **Understanding the X-Axis Gaps:** Notice that unlike a Bar Chart, a Histogram has **no gaps between the bars**. This is intentional! The X-axis represents a continuous numerical timeline. Gaps in a histogram would mathematically imply that there were ranges of bills (e.g., no bills between $20 and $22) where it was physically impossible to spend money.
    
-   **The Magic of the `bins` Parameter:** The choice of how many bins to display drastically alters a histogram. If `bins` is too low (e.g., `bins=3`), the data gets lumped into massive blocks, hiding the underlying patterns. If `bins` is too high (e.g., `bins=100`), the chart turns into a jagged, unreadable mess of tiny toothpicks. Setting it between 10 and 25 is generally the sweet spot for data exploration.
    
-   **Reading the Skewness:** Looking at the generated chart, students will see a sharp peak around $13 to $18, with a long tail stretching out to the right toward $50. This tells an analyst that while the vast majority of dining parties spend a modest amount, a few rare, high-spending tables drag the distribution out, creating a **right-skewed** distribution.



## Script 4: The Scatter Plot (Visualizing Two-Variable Correlation)

#### Explanatory Note Before the Script

While a histogram isolates a single variable, data analysts frequently need to look at two continuous variables simultaneously to find out if they influence one another. _Does an increase in a company's advertising budget lead to an increase in product sales? Does a student's study time correlate with their final exam score?_

To track these interactions, we use a **Scatter Plot**. A scatter plot projects data points onto an X/Y coordinate grid, where the horizontal position represents the value of the first continuous variable, and the vertical position represents the second. It is the ultimate diagnostic tool for detecting patterns, patterns of movement, and clusters between two continuous variables.

The script below maps the relationship between the `total_bill` left on a restaurant table and the subsequent `tip` amount given to the server.

```python

import matplotlib.pyplot as plt
import seaborn as sns

# ==============================================================================
# STEP 1: LOAD THE REAL-WORLD DATASET
# ==============================================================================
# We fetch the built-in 'tips' dataset again.
tips = sns.load_dataset("tips")

# ==============================================================================
# STEP 2: INITIALIZE THE MATPLOTLIB CANVAS
# ==============================================================================
fig, ax = plt.subplots(figsize=(8, 6))

# ==============================================================================
# STEP 3: RENDER THE SCATTER PLOT
# ==============================================================================
# We use Matplotlib's native ax.scatter() function.
# - X-axis: tips["total_bill"] (Independent Variable / Baseline)
# - Y-axis: tips["tip"] (Dependent Variable / Outcome)
# - color: Colors the interior of the coordinate dots.
# - alpha=0.7: Adds transparency so you can see where multiple dots overlap.
# - edgecolors="none": Removes outlines from individual dots for a cleaner visual profile.
ax.scatter(
    tips["total_bill"],     # The 'total_bill' column from the 'tips' dataset, which contains continuous numerical values representing the total bill amounts for each transaction. This will be plotted on the X-axis as the independent variable or baseline.
    tips["tip"],            # The 'tip' column from the 'tips' dataset, which contains continuous numerical values representing the tip amounts for each transaction. This will be plotted on the Y-axis as the dependent variable or outcome we want to analyze in relation to the total bill.
    color="#e91e63",      # This sets the color of the dots in the scatter plot to a vibrant pink, making the data points visually distinct and easy to identify on the chart.
    alpha=0.7,              # This sets the transparency level of the dots to 0.7 (on a scale from 0 to 1), allowing for better visibility when points overlap. This can help to reveal patterns in areas of high density where many points are clustered together.
    edgecolors="none"       # This removes the edges (borders) from the individual dots in the scatter plot, giving them a cleaner and more modern appearance. This can help to reduce visual clutter and make the overall pattern of the data points easier to see.
)

# ==============================================================================
# STEP 4: CUSTOMIZE TITLES AND LABELS
# ==============================================================================
ax.set_title("Relationship Between Total Bill and Tip Amount", fontsize=14, fontweight="bold", pad=15)
ax.set_xlabel("Total Bill ($) (Continuous Ratio Scale)", fontsize=11, labelpad=10)
ax.set_ylabel("Tip Amount ($) (Continuous Ratio Scale)", fontsize=11, labelpad=10)

# ==============================================================================
# STEP 5: AESTHETIC POLISH & DISPLAY
# ==============================================================================
# A scatter plot benefits immensely from a full grid layout (both X and Y axes)
# to let the reader track precise coordinate values anywhere on the canvas.
ax.grid(True, linestyle="--", alpha=0.4)    # Add a dashed grid to enhance readability and make it easier to see the distribution of points across the plot.

# Optimize canvas spacing and render.
plt.tight_layout()    # Automatically adjusts subplot parameters to give specified padding and prevent clipping of labels and titles.
plt.savefig("bill_vs_tip_scatterplot.png", dpi=300)    # Save the figure as a high-resolution PNG file for documentation purposes.
plt.show()

```

### The ouptut plot is as follows

![Scatter plot](/resources/ch15-scatter-plot.png)



### Explanatory Note After the Script

Let's analyze what the code reveals about the logic of data relationships:

-   **Identifying Correlation:** As your eyes move from left to right across the X-axis (higher total bills), the clouds of dots naturally trend upward along the Y-axis (higher tips). This upward slope demonstrates a **positive correlation**. It visually proves the real-world theory that as a restaurant bill grows, the tip scales up along with it.
    
-   **The Importance of Alpha (Opacity):** When thousands of data points are plotted, dots will inevitably land directly on top of one another, masking the density of clusters (a problem known as _overplotting_). By setting `alpha=0.7`, the dots become semi-transparent. Areas where dots heavily overlap will look darker and more vibrant, immediately showing students where the highest density of the restaurant's customer demographic sits.
    
-   **Spotting Variance and Anomalies:** Point out to students that while the overall trend is upward, the cloud widens as it moves right. At a $10 bill, the tip variance is tiny (roughly $1 to $3). At a $40 bill, the variance expands wildly (tips ranging from a low of $2 to a high of $10). A scatter plot is brilliant because it captures both the rule (the positive trend) and the exceptions (the generous or frugal tippers) simultaneously.
