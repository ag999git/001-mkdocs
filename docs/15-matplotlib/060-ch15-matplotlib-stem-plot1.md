




# Stem Plots

## Introduction

A **stem plot** displays data using vertical lines (called stems) extending from a baseline to individual data values.

Unlike a line graph, consecutive points are **not connected**. Each observation is shown separately.

Stem plots are useful when:

-   data values are discrete
-   the order of observations is important
-   we wish to emphasize individual values rather than trends

Common applications include:

-   signal processing
-   digital electronics
-   sampled data
-   time-series measurements




----------

## Stem Plot vs Line Plot

| Feature | Line Plot | Stem Plot |
| --- | --- | --- |
| Connects points | Yes | No |
| Shows trend | Excellent | Moderate |
| Shows individual values | Moderate | Excellent |
| Best for continuous data | Yes | No |
| Best for discrete samples | No | Yes |

### Common Parameters

| Parameter | Affects | Result | Useful For | Example |
| --- | --- | --- | --- | --- |
| stem(x,y) | Plot | Creates stem plot | Discrete data | Basic usage |
| linefmt="r-" | Stem lines | Changes stem style | Formatting | Red stems |
| markerfmt="bo" | Markers | Changes marker style | Highlight points | Blue circles |
| basefmt="k-" | Baseline | Changes baseline style | Visibility | Black baseline |

## Simplified Signatures

### State-Based

```python
plt.stem(x, y)
```

### OOP-Based

```python
ax.stem(x, y)
```

## Script

```python

# Stem Plot Example

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5, 6]
y = [3, 7, 4, 8, 5, 6]

# Create figure and subplot
fig, ax = plt.subplots()

# Create stem plot
ax.stem(
    x,
    y,
    linefmt="b-",      # Blue stems
    markerfmt="ro",    # Red circle markers
    basefmt="k-"       # Black baseline
)

# Add title and labels
ax.set_title("Stem Plot Example")
ax.set_xlabel("Sample Number")
ax.set_ylabel("Value")

# Add grid
ax.grid(True)

# Display graph
plt.show()


```

### Output plot (From above script)

![Stem Plot](/resources/ch15-matplotlib-stem1.png)

# FIGURE


## What This Script Demonstrates

-   creating a stem plot
-   displaying individual observations
-   customizing stems and markers
-   comparing discrete values

----------

## When Should We Use Stem Plots?

Use a stem plot when:

-   observations occur at distinct positions
-   individual values are important
-   data represents sampled measurements
-   connecting points with lines would be misleading

Examples:

-   daily sensor readings
-   digital signals
-   stock price samples
-   laboratory measurements

----------

## Histogram vs Stem Plot vs Line Plot

| Feature | Histogram | Stem Plot | Line Plot |
| --- | --- | --- | --- |
| Shows frequencies | Yes | No | No |
| Shows individual values | No | Yes | Partly |
| Connects observations | No | No | Yes |
| Best for distributions | Yes | No | No |
| Best for sampled data | No | Yes | Yes |


## Key Idea

A stem plot may be viewed as a compromise between a scatter plot and a line plot:

```python
Scatter Plot
      ↓
Stem Plot
      ↓
Line Plot
```

It preserves individual observations while making the magnitude of each value easy to compare.





## Scatter Plot vs Stem Plot vs Line Plot

The following example uses the same dataset to create a scatter plot, stem plot and line plot.

This comparison helps illustrate the strengths of each graph type.

-   A **scatter plot** shows only the individual observations.
-   A **stem plot** shows both the observations and their magnitudes relative to a baseline.
-   A **line plot** emphasizes the overall trend by connecting consecutive points.

By comparing the three graphs, students can better understand when each type of plot is most appropriate.

### Comparison Script

```python

# Scatter Plot vs Stem Plot vs Line Plot

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [2, 7, 3, 8, 4, 9, 5, 6]

# Create three vertically stacked subplots
fig, ax = plt.subplots(
    3,  # Number of rows
    1,  # Number of columns
    figsize=(8, 8)  # Figure size in inches (width, height)
)

# 1. Scatter Plot. It is top panel.
ax[0].scatter(
    x,
    y,
    s=80,  # Marker size
    marker="o",  # Circle markers
    color="blue"  # Marker color
)

ax[0].set_title("Scatter Plot")  # Title for the first subplot
ax[0].set_ylabel("Value")        # Y-axis label for the first subplot
ax[0].grid(True)                 # Add grid to the first subplot

# 2. Stem Plot. It is middle panel.
ax[1].stem(
    x,
    y,
    linefmt="b-",       # Blue stems
    markerfmt="ro",     # Red circle markers
    basefmt="k-"        # Black baseline
)

ax[1].set_title("Stem Plot")  # Title for the second subplot
ax[1].set_ylabel("Value")     # Y-axis label for the second subplot
ax[1].grid(True)              # Add grid to the second subplot

# 3. Line Plot. It is bottom panel.
ax[2].plot(
    x,
    y,
    marker="o",  # Circle markers
    linewidth=2  # Line width
)

ax[2].set_title("Line Plot")          # Title for the third subplot
ax[2].set_xlabel("Sample Number")     # X-axis label for the third subplot
ax[2].set_ylabel("Value")             # Y-axis label for the third subplot
ax[2].grid(True)                      # Add grid to the third subplot

# Adjust spacing
plt.tight_layout()  # Automatically adjust subplot parameters to give specified padding

# Display graphs
plt.show()


```

### Output Plot

![Plot from above script](/resources/ch15-matplotlib-scatter-stem-line.png)

### What to Observe

| **Plot Type** | Main Focus | Best Shows |
| --- | --- | --- |
| **Scatter Plot** | Individual points | Exact observations |
| **Stem Plot** | Points + height from baseline | Magnitude of observations |
| **Line Plot** | Connected observations | Trend and progression |

### Visual Interpretation

```python
Scatter Plot
      ↓
Shows where observations occur

Stem Plot
      ↓
Shows where observations occur
and how far they are from zero

Line Plot
      ↓
Shows overall trend by
connecting observations
```

### Key Learning Point

The same dataset can be represented in different ways depending on the objective:

-   Use a **scatter plot** when individual observations are important.
-   Use a **stem plot** when individual observations and their magnitudes must be emphasized.
-   Use a **line plot** when the primary goal is to show a trend or progression over time.













