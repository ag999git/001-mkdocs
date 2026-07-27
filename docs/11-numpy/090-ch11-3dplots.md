# PROJECT: Visualizing Surfaces using NumPy and Matplotlib

***

## Objective

Understand how:

* `linspace()` creates values
* `meshgrid()` creates coordinate grids
* functions $$Z=f(X,Y)$$ create surfaces
* Matplotlib visualizes them

***

## PART A — Conceptual Study

### Study the following:

1. What does `np.linspace()` do?
2. How does `np.meshgrid()` convert 1D arrays into 2D grids?
3. What does each of these represent:
   * X → x-coordinates
   * Y → y-coordinates
   * Z → height (function output)

***

### Study these matplotlib functions

| Function                                    | Purpose            |
| ------------------------------------------- | ------------------ |
| plt.figure()                                | Create a figure    |
| add\_subplot(projection='3d')               | Enable 3D plotting |
| plot\_surface(X, Y, Z)                      | Plot surface       |
| set\_xlabel(), set\_ylabel(), set\_zlabel() | Label axes         |
| set\_title()                                | Add title          |
| plt.show()                                  | Display plot       |

<details>

<summary>Matplotlib Functions Used (Explained Simply- Click to expand)</summary>

### Matplotlib Functions Used (Explained Simply)

***

#### 1. `plt.figure()`

**Role:**\
Creates a new drawing canvas (called a _figure_).

**Purpose:**\
To start a new plot. Without it, plots may overlap or reuse old figures.

**Input parameters (common):**

* `figsize=(width, height)` → optional size of figure

**Output:**\
Returns a figure object (stored as `fig`)

**Example:**

fig = plt.figure()

**Key Idea:**

> Think of this as opening a blank page for drawing.

***

#### 2. `fig.add_subplot(projection='3d')`

**Role:**\
Adds a plotting area (axes) inside the figure.

**Purpose:**\
Enables **3D plotting**.

**Input parameters:**

* `projection='3d'` → required for 3D plots

**Output:**\
Returns an axes object (stored as `ax`)

**Example:**

ax = fig.add\_subplot(projection='3d')

**Key Idea:**

> Converts the blank page into a 3D coordinate system.

***

#### 3. `ax.plot_surface(X, Y, Z)`

**Role:**\
Plots a 3D surface.

**Purpose:**\
To visualize a function Z=f(X,Y)Z = f(X,Y)Z=f(X,Y)

**Input parameters:**

* `X, Y, Z` → NumPy arrays of same shape

**Output:**\
Draws a surface plot on the axes

**Example:**

ax.plot\_surface(X, Y, Z)

**Key Idea:**

> Uses grid points (X,Y) and heights (Z) to draw a surface.

***

#### 4. `ax.set_xlabel()`, `set_ylabel()`, `set_zlabel()`

**Role:**\
Labels the axes.

**Purpose:**\
To make plots understandable.

**Input parameters:**

* A string (label name)

**Output:**\
Updates axis labels

**Example:**

ax.set\_xlabel("X")\
ax.set\_ylabel("Y")\
ax.set\_zlabel("Z")

**Key Idea:**

> Always label axes—otherwise plots are meaningless.

***

#### 5. `ax.set_title()`

**Role:**\
Adds a title to the plot.

**Purpose:**\
To describe what the plot represents.

**Input:**

* A string

**Output:**\
Displays title above plot

**Example:**

ax.set\_title("Z = X + Y")

***

#### 6. `plt.show()`

**Role:**\
Displays the plot window.

**Purpose:**\
To render all figures created

**Input:**\
None

**Output:**\
Shows the final plot

**Example:**

plt.show()

**Key Idea:**

> Without this, plots may not appear.

| Function          | Role          | Input         | Output         |
| ----------------- | ------------- | ------------- | -------------- |
| figure()          | Create canvas | optional size | figure         |
| add\_subplot()    | Create axes   | projection    | axes           |
| plot\_surface()   | Draw surface  | X,Y,Z arrays  | 3D plot        |
| set\_xlabel() etc | Label axes    | string        | labeled axes   |
| set\_title()      | Add title     | string        | titled plot    |
| show()            | Display plot  | none          | visible output |

</details>

## Part B — Task

Write a program that:

1. Creates a grid using `linspace()` and `meshgrid()`
2. Plots two surfaces:

***

### Surface 1 (Plane)

## $$Z=X+Y$$

### Surface 2 (Cone-like surface)

$$Z= \sqrt{X^2 + Y^2}$$

Derived from $$Z^2 =X^2+Y^2$$

***

### Hints

* Use same X and Y for both surfaces
* Z must have same shape as X and Y
* Use two different figures
* Keep grid symmetric (e.g., -5 to 5)

### Flowchart of the process

![Flowchart](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch11-numpy-flowchart-matplotlib.png)

## Script

```python

# Project: Visualizing surfaces using NumPy and Matplotlib

import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create values

x = np.linspace(-5, 5, 50)   # With 50 points from -5 to 5 we get smoother surfaces
y = np.linspace(-5, 5, 50)   # 50 points from -5 to 5

# Step 2: Create grid
# meshgrid creates 2D arrays for X and Y. Each (i,j) gives a pair (X[i,j], Y[i,j]) which is one input to f(x,y).
X, Y = np.meshgrid(x, y)

# Step 3: Define surfaces

# Surface 1: Plane. It is a slanted plane where Z increases as X and Y increase. 
Z1 = X + Y

# Surface 2: Inverted Cone-like surface. It is a cone where Z increases with the distance from the origin.
Z2 = np.sqrt(X**2 + Y**2)  #

# Step 4: Plot Surface 1
fig1 = plt.figure()  # separate figure for first surface
ax1 = fig1.add_subplot(projection='3d')  # 3D subplot for surface plot
ax1.plot_surface(X, Y, Z1)
ax1.set_title("Z = X + Y (Plane)")
ax1.set_xlabel("X")  # X-axis label
ax1.set_ylabel("Y")  # Y-axis label
ax1.set_zlabel("Z")  # Z-axis label

# Step 5: Plot Surface 2
fig2 = plt.figure()  # separate figure for second surface
ax2 = fig2.add_subplot(projection='3d')  # 3D subplot for surface plot
ax2.plot_surface(X, Y, Z2)  # cone-like surface. As the distance from origin increases, Z increases.
ax2.set_title("Z = sqrt(X^2 + Y^2) (Cone)")  # title indicates the function being plotted
ax2.set_xlabel("X")  # X-axis label
ax2.set_ylabel("Y")  # Y-axis label
ax2.set_zlabel("Z")  # Z-axis label

# Step 6: Show plots
# Displays both surface plots. Each plot is in a separate window. The first shows the plane Z=X+Y, 
# and the second shows the cone-like surface Z=sqrt(X^2 + Y^2).
plt.show()  # show() renders the plots on the screen.

# Key Ideas:
# X,Y → coordinates
# Z → height at each coordinate

```

### Output Figure (Plane)

![Figure Plane](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch11-numpy-matplotlib-plane.png)

### Output Figure (Cone)

![Figure Cone](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch11-numpy-matplotlib-cone.png)
