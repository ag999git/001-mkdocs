



**1. Why does data visualization help spot anomalies faster than tables?**

Data visualization exploits the human brain's visual cortex, processing shapes, lines, and color gradients simultaneously in a pre-attentive phase. Conversely, reading a numerical table requires serial processing, where the brain must evaluate each text cell individually and store values in short-term memory to construct comparison metrics. For instance, a negative or missing data point in a column of 10,000 positive integers easily escapes manual inspection but manifests instantly as a sharp, broken line or an isolated scatter point standing apart from a geometric cluster.

**2. Contrast nominal, ordinal, interval, and ratio data visualization strategies.**

The statistical scale of an input variable strictly limits its geometric mapping choice. Nominal data (labels like country names) lacks inherent order and is best shown using a bar chart with distinct categorical bins. Ordinal data (like survey ratings) possesses a sequence but lacks mathematically consistent intervals, requiring ordered horizontal bars or custom index alignments. Interval data (like temperature in Celsius) preserves stable distances but lacks a true zero, allowing plot trend lines but making pie charts misleading. Ratio data (like revenue) contains a true absolute zero, enabling calculations of proportion and making it suitable for pie charts or dynamic scatter point sizing.

**3. Differentiate between the pyplot state-based interface and the object-oriented API.**

The pyplot state-based dialect relies on a hidden global engine that tracks the "active" chart frame implicitly. Invoking a functional call like plt.plot() forces Matplotlib to automatically find or create the most recent canvas, making it fast for interactive command-line environments but error-prone when managing multiple figures. The object-oriented API explicitly splits the structural elements into variable handles using fig, ax = plt.subplots(). Developers execute modifications directly on these handles via target methods like ax.plot(), isolating each canvas and preventing cross-contamination in multi-window scripts.

**4. Explain the physical components and structural hierarchy of a Matplotlib chart window.**

Matplotlib organizes its graphical workspace as a nested container architecture resembling a professional picture frame. The highest container is the Figure (represented by the fig object), which acts as the outer structural frame handling the display window, global background canvas, size dimensions, and layout engines. Inside this frame sits one or more Axes (represented by the ax object), which serves as the actual drawing canvas. The Axes container holds the coordinate plane, grid lines, tick labels, title boxes, and the actual geometric plots.

```mermaid
graph TD
    Figure[Figure Object: Top-Level Canvas Window] --> Axes1[Axes Object 1: Coordinate Canvas]
    Figure --> Axes2[Axes Object 2: Coordinate Canvas]
    Axes1 --> AxisX[X-Axis: Ticks & Gridlines]
    Axes1 --> AxisY[Y-Axis: Ticks & Gridlines]
    Axes1 --> Artist[Artist Elements: Line2D, Patches, Text]


```



**5. What happens behind the scenes if len(x) does not equal len(y)?**

When a data binding method like ax.plot(x, y) is executed, Matplotlib checks the shape of the inputs to verify that the independent sequence aligns perfectly with the dependent metric. The internal mapping engine requires a direct one-to-one index pairing to build Cartesian coordinate vectors (x[i], y[i]). If the sequences are mismatched, the library drops the operation and throws a ValueError: x and y must have same first dimension. This halts execution before any canvas rendering steps take place.

**6. Why does a single-array input to ax.plot() still generate an X-axis?**

If you pass only one sequence argument to ax.plot(y), the plotting engine assumes the input array represents the vertical coordinates (Y). To draw a continuous line across a 2-D plane, it auto-generates a sequence of horizontal coordinates (X). It constructs a standard numerical sequence using a step-counter equivalent to range(len(y)), positioning the first data point at index position 0, the second at 1, and continuing until the array is fully mapped.

**7. Contrast standard lists, NumPy arrays, and Pandas DataFrames as inputs.**

While Matplotlib accepts all three structures, its core math engine is built on top of NumPy arrays (numpy.ndarray). When you pass a standard Python list, Matplotlib copies the data and converts it to a NumPy array before calculating positions. This causes a minor performance penalty with massive datasets. Pandas DataFrames add an extra layer of organization, letting you pass column labels directly. However, you must extract the underlying values or pass the Series object to keep the internal matrix calculations efficient.

| Attribute Matrix | Python Standard List | NumPy Array (ndarray) | Pandas DataFrame / Series |
| --- | --- | --- | --- |
| Memory Architecture | Pointers to scattered objects; high tracking overhead. | Contiguous memory allocation; extremely compact. | Wraps NumPy blocks; includes index and label overhead. |
| Vector Math Processing | requires slow loops or list comprehensions. | Fast, hardware-accelerated vectorized operations. | Supports vectorized alignment across index labels. |
| Native Plot Labeling | Handled manually using raw string arrays. | Handled manually via array coordinate slicing. | Automatically extracts index columns for axis labels. |

**8. Why does calling plt.show() pause script execution?**

The plt.show() method starts a local interactive window loop that takes control of your operating system's main thread. It hands control over to a backend engine (like TkAgg or Qt5Agg) to render the window frame and handle user inputs like zooming, panning, and saving. Because this window loop runs on the main thread, Python pauses the rest of your script until you close the graph window, at which point the script resumes.

**9. Detail the syntax mechanics and limitations of legacy shortcut format strings.**

Legacy format strings allow you to quickly configure basic line styles using a compact 3-character code, such as 'ro-' (Red color, Circle marker, Solid line). The plotting engine parses this string by checking for color characters ('r', 'g', 'b'), marker shapes ('o', 's', '^'), and line styles ('-', '--'). While convenient for quick test plots, this format is highly limited because it does not support advanced settings like marker face colors, custom hex codes, or variable line weights. For production code, using explicit keyword arguments like color='#FF5733', marker='o', and linestyle='-' is preferred.

**10. Explain the sorting and rendering workflow of the ax.hist() method.**

Unlike simple bar charts that map explicit values directly, ax.hist() calculates the chart structure on the fly. It scans your raw dataset, finds the minimum and maximum boundaries, and divides that range into equal, consecutive mathematical windows called **bins**. It then acts as a data filter, counting how many data values fall into each bin window. Finally, it uses these counts to set the heights of a series of touching vertical rectangle blocks on the canvas.

```python
# Description: Demonstrates internal bin counting mechanics
import matplotlib.pyplot as plt
import numpy as np
# Generate raw unsorted numeric measurements
raw_data = [12, 15, 13, 22, 28, 24, 25, 29, 31, 35]
fig, ax = plt.subplots(figsize=(6, 3))
# Matplotlib calculates limits, creates 3 bins, and counts frequencies
# Bin 1: [12 to 19.67], Bin 2: (19.67 to 27.33], Bin 3: (27.33 to 35]
# The counts are: Bin 1 has 3 values, Bin 2 has 4 values, Bin 3 has 3 values
# counts, bins, patches are returned by hist() for further analysis if needed 
# The bins are automatically determined based on the data range and number of bins specified (default is 10, but here it is 3).    
# ax.hist() creates the histogram and also returns 3 values:
# 1. the counts of values in each bin, 
# 2. the edges of the bins, and 
# 3. the patch objects for the bars. patch object is a container for the rectangles that make up the bars of the histogram.
# patch objects can be used to customize the appearance of the bars after they have been created.
counts, bins, patches = ax.hist(raw_data, bins=3, edgecolor='black', color='skyblue')
plt.close() # Clean up memory allocations
# Print the mathematical results calculated behind the scenes
print("Calculated Bin Edges:", bins)
print("Frequency Count Per Bin Window:", counts)
print("Patch Objects for Each Bin:", patches)

```

**The Ougput is**

```python

Calculated Bin Edges: [12.         19.66666667 27.33333333 35.        ]
Frequency Count Per Bin Window: [3. 3. 4.]
Patch Objects for Each Bin: <BarContainer object of 3 artists>

```

**11. Contrast the structural insights provided by box plots vs. violin plots.**

A box plot provides a clean, abstract summary of a dataset using five key landmarks: the minimum, lower quartile ($Q1$), median ($Q2$), upper quartile ($Q3$), and maximum. It strips away individual data points to focus on variance and easily flags outliers as isolated dots beyond the whiskers. A violin plot displays the same summary metrics but adds a symmetrical curve around the center line. This curve represents the probability density of the data, showing exactly where values cluster or thin out.

**12. How does ax.legend() match label strings to colored chart lines?**

When you call a plotting method with a label argument, like ax.plot(x, y, label="Revenue"), Matplotlib creates a Line2D object and stores your text tag inside its internal metadata. When you later call ax.legend(), the engine scans the axis container, extracts all these hidden metadata tags, and pairs them with their matching line colors. It then builds an overlay box containing these color keys and text descriptions, placing it on the canvas based on your location settings.

**13. Why does ax.twinx() create an independent Y-axis on a shared X-axis?**

When you create a dual-axis layout using ax2 = ax1.twinx(), Matplotlib creates a brand new, transparent Axes object and overlays it directly on top of the original axis frame. This new axis object shares the exact same horizontal coordinate plane ($X$) as the original, but contains its own vertical coordinate plane ($Y$). This allows you to overlay two lines with completely different data units and scales (such as tracking temperature in degrees alongside rainfall in millimeters) on the same graph without distorting the layout.

```python

# =====================================================================
# EXAMPLE: Dual Y-Axis Plot Using Matplotlib
#
# GOAL
# ----
# Display two different measurements on the same chart:
#
#   1. Temperature (°C)
#   2. Humidity (%)
#
# These variables use different units and scales.
#
# If we plotted them on the same Y-axis, the chart could become
# misleading or difficult to interpret.
#
# Therefore we use:
#
#   LEFT Y-AXIS   -> Temperature
#   RIGHT Y-AXIS  -> Humidity
#
# Both datasets share the same X-axis (Days).
#
# =====================================================================


# =====================================================================
# STEP 1: Import Matplotlib
# =====================================================================
#
# matplotlib.pyplot contains functions used to create figures,
# axes, lines, labels, legends, and more.
#
# The alias "plt" is the standard convention.
#
# =====================================================================

import matplotlib.pyplot as plt


# =====================================================================
# STEP 2: Define the data
# =====================================================================
#
# The X-axis values represent days.
#
# Day 1
# Day 2
# Day 3
# Day 4
#
# =====================================================================

days = [1, 2, 3, 4]


# Temperature values corresponding to each day.
#
# Day 1 -> 22°C
# Day 2 -> 25°C
# Day 3 -> 21°C
# Day 4 -> 24°C
#
temperature = [22, 25, 21, 24]


# Humidity values corresponding to each day.
#
# Day 1 -> 60%
# Day 2 -> 85%
# Day 3 -> 70%
# Day 4 -> 75%
#
humidity = [60, 85, 70, 75]


# =====================================================================
# STEP 3: Create Figure and Primary Axis
# =====================================================================
#
# plt.subplots() returns:
#
#   fig  -> entire drawing canvas
#   ax1  -> first plotting area (primary axis)
#
# Think of it like:
#
#   Figure = sheet of paper
#   Axis   = chart drawn on the paper
#
# =====================================================================

fig, ax1 = plt.subplots(figsize=(8, 5))


# =====================================================================
# STEP 4: Plot Temperature on Primary Axis
# =====================================================================
#
# We use ax1.plot() because temperature belongs to the
# primary (left-side) Y-axis.
#
# color='crimson'
#     Makes the line red.
#
# marker='o'
#     Places a circular marker at each data point.
#
# =====================================================================

ax1.plot(
    days,
    temperature,
    color='crimson',
    marker='o',
    linewidth=2,
    label="Temperature"
)


# =====================================================================
# STEP 5: Configure X-Axis
# =====================================================================
#
# Since both datasets share the same timeline,
# only one X-axis is needed.
#
# =====================================================================

ax1.set_xlabel("Timeline (Days)")


# =====================================================================
# STEP 6: Configure Left Y-Axis
# =====================================================================
#
# This Y-axis belongs to temperature.
#
# We color the axis label red so that it visually matches
# the temperature line.
#
# =====================================================================

ax1.set_ylabel(
    "Temperature (°C)",
    color='crimson'
)


# =====================================================================
# STEP 7: Color Tick Labels on Left Y-Axis
# =====================================================================
#
# Tick labels are the numeric values shown along the axis.
#
# Example:
#
#   20
#   22
#   24
#   26
#
# Coloring them red makes it easier to identify which
# axis belongs to which line.
#
# =====================================================================

ax1.tick_params(
    axis='y',
    labelcolor='crimson'
)


# =====================================================================
# STEP 8: Create Secondary Y-Axis
# =====================================================================
#
# twinx() means:
#
#   "Create another Y-axis that shares the same X-axis."
#
# Internally:
#
#          Humidity Axis (Right)
#                    |
#                    |
# Temperature Axis (Left)
#
# Both axes occupy the same plotting area.
#
# =====================================================================

ax2 = ax1.twinx()


# =====================================================================
# STEP 9: Plot Humidity on Secondary Axis
# =====================================================================
#
# Humidity belongs to ax2, not ax1.
#
# color='navy'
#     Dark blue line
#
# linestyle='--'
#     Dashed line
#
# =====================================================================

ax2.plot(
    days,
    humidity,
    color='navy',
    linestyle='--',
    linewidth=2,
    label="Humidity"
)


# =====================================================================
# STEP 10: Configure Right Y-Axis
# =====================================================================
#
# This axis represents humidity values.
#
# =====================================================================

ax2.set_ylabel(
    "Humidity (%)",
    color='navy'
)


# =====================================================================
# STEP 11: Color Tick Labels on Right Y-Axis
# =====================================================================
#
# The blue tick labels visually connect to the blue humidity line.
#
# =====================================================================

ax2.tick_params(
    axis='y',
    labelcolor='navy'
)


# =====================================================================
# STEP 12: Add Chart Title
# =====================================================================
#
# A title helps explain what the chart represents.
#
# =====================================================================

plt.title(
    "Temperature and Humidity Over Time",
    fontsize=14,
    fontweight='bold'
)


# =====================================================================
# STEP 13: Add Grid (Optional)
# =====================================================================
#
# Grids make it easier to read values.
#
# alpha controls transparency:
#
#   0.0 = invisible
#   1.0 = fully opaque
#
# =====================================================================

ax1.grid(
    True,
    linestyle=':',
    alpha=0.6
)


# =====================================================================
# STEP 14: Adjust Layout
# =====================================================================
#
# Prevent labels and titles from overlapping.
#
# Highly recommended before displaying or saving figures.
#
# =====================================================================

plt.tight_layout()


# =====================================================================
# STEP 15: Display Figure
# =====================================================================
#
# block=False means:
#
#     Show the figure window
#     BUT continue executing the remaining code.
#
# Without block=False, execution would stop here until
# the user manually closes the window.
#
# =====================================================================

plt.show(block=False)


# =====================================================================
# STEP 16: Keep Figure Visible
# =====================================================================
#
# Pause execution for 5 seconds.
#
# During this time the figure remains visible.
#
# You can increase or decrease the number.
#
# Examples:
#
#     plt.pause(2)
#     plt.pause(10)
#     plt.pause(30)
#
# =====================================================================

plt.pause(5)


# =====================================================================
# STEP 17: Close Figure Automatically
# =====================================================================
#
# After the pause completes, the figure is closed.
#
# Useful for:
#
# • Automated demos
# • Batch report generation
# • Educational examples
# • Previewing plots briefly
#
# =====================================================================

plt.close()


# =====================================================================
# END RESULT
# =====================================================================
#
# LEFT AXIS (Red)
# ----------------
# Temperature (°C)
#
# RIGHT AXIS (Blue)
# -----------------
# Humidity (%)
#
# SHARED X-AXIS
# -------------
# Day 1  Day 2  Day 3  Day 4
#
# The plot appears for 5 seconds and then closes
# automatically.
#
# =====================================================================

```
**14. Explain how multi-dimensional datasets map to a 2-D heatmap via ax.imshow().**

The ax.imshow() method processes a structured 2-D grid or nested array matrix where data points are arranged in explicit rows and columns. Instead of drawing coordinate points, the engine treats each cell in the matrix as a square pixel. It maps the numerical value inside each cell to a specific color along a gradient scale, converting raw data tables into a visual matrix of color intensities.


```
Code snippet

graph TD

Subscript1[Raw Nested Matrix Array] -->|Row 0, Col 0: Value 10| B(Normalizing Engine)

Subscript1 -->|Row 0, Col 1: Value 50| B

B -->|Maps 10 to Min Boundary| C[Color Mapping Palette]

B -->|Maps 50 to Max Boundary| C

C --> D[Visual Output: Dark Purple Box next to Bright Yellow Box]
```
**15. Differentiate between plt.tight_layout() and layout="constrained".**

Both tools prevent text overlapping by automatically adjusting the spacing between subplots, but they do so using different timing and logic. plt.tight_layout() is an optimization step run at the end of your script. It analyzes the positions of text labels and shifts subplots around after they have been drawn, which can sometimes break user-defined dimensions. The newer layout="constrained" option is set inside the initial subplot initialization call, like plt.subplots(layout="constrained"). It activates a live constraint solver that dynamically calculates padding and margins as layout elements are added, making it more stable for complex, multi-panel layouts.

**16. How does indexing work when plt.subplots() creates a multi-row grid?**
When you generate a single plot, plt.subplots() returns an individual Axes object. However, if you create a multi-row, multi-column grid using plt.subplots(2, 2), the method returns a 2-D NumPy array containing four distinct axes containers. To select a specific panel, you must navigate this array using standard grid indexing syntax: ax[row_index, col_index].

```python
# =====================================================================
# File: github_subplot_matrix.py
# Description: Demonstrates multidimensional axes tracking indices
# =====================================================================
import matplotlib.pyplot as plt

# Generates a 2x2 grid (Two rows, Two columns)
fig, ax = plt.subplots(2, 2)

# Index positions are structured as multidimensional coordinates
ax[0, 0].set_title("Top-Left Panel Position")
ax[0, 1].set_title("Top-Right Panel Position")
ax[1, 0].set_title("Bottom-Left Panel Position")
ax[1, 1].set_title("Bottom-Right Panel Position")

# Troubleshooting Note (Commented out to prevent runtime failure):
# ---------------------------------------------------------------------
# # COMMON STUDENT ERROR: Using a flat index on a 2-D axes layout array
# ax[3].plot([1, 2], [10, 20]) 
# # IndexError: index 3 is out of bounds for axis 0 with size 2
# ---------------------------------------------------------------------

plt.show(block=False)  # Display the plot without blocking further code execution
plt.pause(15)          # Keep the plot open for 15 seconds to allow for viewing
plt.close()            # Close the plot after the pause duration



```



**17. What is the execution danger of mixing global styles with local overrides?**

Global themes set via plt.style.use('ggplot') update universal default settings across your entire Python session. If you change global styles in the middle of a script, it alters how text, lines, and colors render across every plot window initialized afterward. Local overrides, such as setting custom face colors using ax.set_facecolor('black'), modify only that specific axis container. The danger of mixing them is that a global theme change can silently overwrite your local settings if the global theme configuration file contains explicit styling overrides for those same parameters.

**18. Why does ax.text() use data coordinates while annotations use reference arrows?**

The standard ax.text(x, y, "Label") method adds text labels directly to specific coordinate positions on the plot canvas, meaning the label shifts or rescales if you adjust your axis limits. The advanced ax.annotate() method separates the text location from the data target point. It allows you to point an arrow at a specific data coordinate (xy=(x, y)) while positioning the descriptive text box at a stable layout position (xytext=(x_offsets, y_offsets)). This ensures your labels remain readable and beautifully arranged even if the underlying plot scales change.

**19. Detail how to clear memory when drawing thousands of plots in a loop.**

By default, Matplotlib keeps every figure you create open in your system memory until you manually close it or end your Python session, allowing you to view and interact with multiple windows. If you generate thousands of charts inside a loop without clearing this cache, your system will quickly run out of RAM, leading to memory leaks and performance crashes. To prevent this, you must explicitly free up memory at the end of each loop iteration by calling plt.close(fig).

```python

# =====================================================================
# Example: Clearing Memory When Generating Thousands of Plots
#
# Description:
# This script simulates a batch-reporting pipeline that creates
# many plots inside a loop.
#
# IMPORTANT:
# Every call to plt.subplots() creates a new Figure object that
# consumes memory.
#
# If figures are never closed, memory usage will continuously grow.
#
# The solution is to explicitly call:
#
#     plt.close(fig)
#
# after saving or displaying each figure.
#
# =====================================================================

import matplotlib.pyplot as plt
import numpy as np


# =====================================================================
# STEP 1: Generate a large number of plots
# =====================================================================

for plot_id in range(1000):

    # -----------------------------------------------------------------
    # STEP 2: Create a new figure
    #
    # A Figure object allocates memory for:
    #   - Axes
    #   - Lines
    #   - Labels
    #   - Tick marks
    #   - Rendering information
    # -----------------------------------------------------------------

    fig, ax = plt.subplots()

    # -----------------------------------------------------------------
    # STEP 3: Create sample data
    # -----------------------------------------------------------------

    x = np.linspace(0, 10, 100)

    y = np.sin(x + plot_id * 0.1)

    # -----------------------------------------------------------------
    # STEP 4: Draw the plot
    # -----------------------------------------------------------------

    ax.plot(x, y)

    ax.set_title(f"Plot {plot_id}")

    # -----------------------------------------------------------------
    # STEP 5: Save the figure
    #
    # In real-world batch pipelines this could be:
    #   report_001.png
    #   report_002.png
    #   ...
    # -----------------------------------------------------------------

    fig.savefig(f"plot_{plot_id}.png")

    # -----------------------------------------------------------------
    # STEP 6: CRITICAL MEMORY CLEANUP
    #
    # Remove the figure from Matplotlib's internal figure manager
    # and release the memory associated with this figure.
    #
    # Without this line:
    #
    #     plt.close(fig)
    #
    # all 1000 figures remain in memory, causing memory usage
    # to grow continuously.
    #
    # -----------------------------------------------------------------

    plt.close(fig)


# =====================================================================
# STEP 7: Completion Message
# =====================================================================

print("Finished generating plots.")

```

**20. How does plt.subplot2grid() build irregular grid layouts?**


Standard subplot functions such as plt.subplot() and plt.subplots() divide a figure into a uniform grid where each subplot occupies exactly one grid cell. This works well for simple visualizations but becomes limiting when building dashboards, report layouts, or analytical interfaces where some charts need more space than others.

plt.subplot2grid() solves this problem by treating the entire figure as a coordinate-based grid system. First, you define the total grid dimensions using the shape=(rows, cols) parameter. Each cell in this grid acts like a coordinate location. You then specify where a subplot should begin using loc=(row, column) and optionally allow it to span multiple rows or columns using the rowspan and colspan parameters.

This makes it possible to create asymmetric dashboard layouts such as:

A wide header chart spanning the full width of the figure
A tall navigation or sidebar panel
A large main analysis panel
Multiple small supporting charts

Internally, Matplotlib reserves the requested cells and merges them into a single plotting area. By combining different spans, you can construct complex dashboard-style interfaces while still working within a single figure canvas.

```python
# =====================================================================
# File: github_subplot2grid_dashboard.py
#
# Description:
# Demonstrates how subplot2grid() creates irregular dashboard layouts.
#
# Dashboard Structure:
#
#   +-----------------------------+
#   |        Banner Plot          |
#   +---------+-------------------+
#   | Sidebar |                   |
#   |         |   Main Plot       |
#   |         |                   |
#   +---------+-------------------+
#
# =====================================================================

import matplotlib.pyplot as plt
import numpy as np


# =====================================================================
# STEP 1: Define overall dashboard grid
#
# We create a 3-row x 3-column grid.
#
# Grid Coordinates:
#
#       Col0   Col1   Col2
#
# Row0  (0,0) (0,1) (0,2)
# Row1  (1,0) (1,1) (1,2)
# Row2  (2,0) (2,1) (2,2)
#
# =====================================================================

grid_dimensions = (3, 3)


# =====================================================================
# STEP 2: Create Banner Panel
#
# Start at cell (0,0)
#
# colspan=3 means:
# occupy all three columns across the top row.
#
# =====================================================================

ax_banner = plt.subplot2grid(
    shape=grid_dimensions,
    loc=(0, 0),
    colspan=3
)

x = np.linspace(0, 10, 100)

ax_banner.plot(
    x,
    np.sin(x),
    color="crimson",
    linewidth=2
)

ax_banner.set_title(
    "Banner Plot (Spans Entire Top Row)"
)


# =====================================================================
# STEP 3: Create Sidebar Panel
#
# Start at cell (1,0)
#
# rowspan=2 means:
# occupy both lower rows.
#
# =====================================================================

ax_sidebar = plt.subplot2grid(
    shape=grid_dimensions,
    loc=(1, 0),
    rowspan=2
)

sidebar_data = [12, 18, 9, 14]

ax_sidebar.bar(
    ["A", "B", "C", "D"],
    sidebar_data,
    color="steelblue"
)

ax_sidebar.set_title(
    "Sidebar Panel"
)


# =====================================================================
# STEP 4: Create Main Analytics Panel
#
# Start at cell (1,1)
#
# rowspan=2
# colspan=2
#
# Occupies:
#
#   (1,1) (1,2)
#   (2,1) (2,2)
#
# =====================================================================

ax_main = plt.subplot2grid(
    shape=grid_dimensions,
    loc=(1, 1),
    rowspan=2,
    colspan=2
)

x = np.linspace(0, 20, 200)

ax_main.plot(
    x,
    np.sin(x),
    label="sin(x)"
)

ax_main.plot(
    x,
    np.cos(x),
    label="cos(x)"
)

ax_main.set_title(
    "Main Analytics Area"
)

ax_main.legend()


# =====================================================================
# STEP 5: Improve spacing
#
# Prevents titles and labels from overlapping.
#
# =====================================================================

plt.tight_layout()


# =====================================================================
# STEP 6: Display dashboard
#
# block=False allows execution to continue.
#
# =====================================================================

plt.show(block=False)


# =====================================================================
# STEP 7: Keep dashboard visible for 5 seconds
#
# Useful for demonstrations and teaching examples.
#
# =====================================================================

plt.pause(5)


# =====================================================================
# STEP 8: Close figure and release memory
#
# =====================================================================

plt.close()


# =====================================================================
# KEY TAKEAWAY
#
# shape     -> size of overall grid
# loc       -> starting cell
# rowspan   -> number of rows occupied
# colspan   -> number of columns occupied
#
# subplot2grid() allows multiple cells to be merged,
# enabling flexible dashboard-style layouts.
#
# =====================================================================

```








