



## Why Do We Need Violin Plots?

### The Problem with Box Plots

> **A box plot summarizes data using five numbers** (minimum, Q1, median, Q3, maximum), but it **hides the shape** of the distribution.

### Real Question A Beginner Asks:

>"I have a box plot. Can I tell if my data has one peak or two peaks?"                                                   Answer: NO! The box plot hides this information completely.     
Solution: Use a violin plot!   

### What Each Plot Type Reveals
| **Plot Type** | **Shows** | **Hides** |
| --- | --- | --- |
| **Histogram** | Exact frequencies, detailed shape | Takes more space, harder to compare multiple groups |
| **Box Plot** | Median, quartiles, outliers | Distribution shape, peaks, clusters |
| **Violin Plot** | Shape + summary statistics | Exact frequencies, individual data points |


## What Is a Violin Plot?

### Simple Definition

> A **violin plot** combines a **box plot** with a **density curve**. It shows both the statistical summary AND the shape of the data distribution.

### Why Is It Called a "Violin" Plot?

The graph often looks like a musical violin:

```python
     Wide section = Many data points here
         /\
        /  \
       /    \    ← Mirror image of density curve
       \    /
        \  /
         \/
     Narrow section = Few data points here
```

### Concept Box: Understanding Width

 - Width Does NOT Mean Value!  Common Mistake:  To think wider = larger value  
 - Correct Understanding: Wider = MORE observations at that value
 - Narrower = FEWER observations        
 - Think of it like a crowd: 
   - Wide area = crowded (many people).
   - Narrow area = empty (few people)

### Component Breakdown

| Component | What It Shows | Visual Appearance |
| --- | --- | --- |
| **Density curve** | Shape of distribution | Mirrored violin shape (blue) |
| **Median** | Centre value | Thick red line inside violin |
| **Mean** | Average value | Green triangle marker |
| **Q1 and Q3** | Quartiles (25th and 75th percentile) | Horizontal lines marking box edges |
| **Width** | Number of observations | Wider = more data points |


### From Histogram to Violin Plot: The Transformation

### Step-by-Step Process
![From Histogram to Violin Plot](/resources/ch15-matplotlib-violin-steps-in-making.png)



### What Happens at Each Step?


| Step | Action | Result |
| --- | --- | --- |
| 1 | Collect data | List of numbers (e.g., exam scores) |
| 2 | Create histogram | Bars show how many values in each range |
| 3 | Smooth the bars | Continuous curve replaces stepped bars |
| 4 | Mirror the curve | Flip curve horizontally to create symmetry |
| 5 | Add statistics | Overlay median, quartiles, mean |
| 6 | Final violin | Combines shape + summary in one view |


### Comparison: Histogram vs. Box Plot vs. Violin Plot

### Feature Comparison Table

| Feature | Histogram | Box Plot | Violin Plot |
| --- | --- | --- | --- |
| Shows frequencies | Yes (exact counts) | No | Indirectly (via width) |
| Shows median | No | Yes | Yes |
| Shows quartiles | No | Yes | Yes |
| Shows outliers | Difficult | Yes (clear) | Sometimes |
| Shows distribution shape | Yes (detailed) | No | Yes (smoothed) |
| Shows multiple peaks | Yes | No | Yes |
| Space required | More | Very little | Moderate |
| Compare multiple groups | Harder | Easy | Easy |
| Best for | Exploring one dataset | Quick summary | Shape + summary together |


### When Each Plot Shines
Choose Based on Your Goal:

 - Use HISTOGRAM when you need:  
   - Exact frequency counts To see every    detail of shape . 
   - To understand bin boundaries  
 - Use BOX PLOT when you need: 
   - Quick statistical summary 
   - To compare many groups
   - To identify outliers clearly Space-efficient display  
 - Use VIOLIN PLOT when you need:
   - Distribution shape + summary 
   - To detect multiple peaks 
   - To see skewness clearly Better than box plot but more compact than histogram

       


### Typical Violin Plot Shapes

### 1. Symmetric Distribution (Bell-Shaped)

**Characteristics:**

-   Widest in the middle
-   Narrow at both ends
-   Mirror image on top and bottom
-   Median in centre

**What It Means:** Data is evenly distributed around the centre (like a normal distribution).

### 2. Right-Skewed Distribution

**Characteristics:**

-   Wide at the bottom (lower values)
-   Long narrow tail at the top (higher values)
-   Median shifted toward bottom

**What It Means:** Most values are low, but a few very high values exist.

### 3. Left-Skewed Distribution

**Characteristics:**

-   Wide at the top (higher values)
-   Long narrow tail at the bottom (lower values)
-   Median shifted toward top

**What It Means:** Most values are high, but a few very low values exist.

### 4. Bimodal Distribution (Two Peaks) ⭐

**Characteristics:**

-   Two wide sections separated by a narrow section
-   Looks like two violins stacked

**What It Means:** Data has **two distinct groups or clusters**.

> **Critical Insight**: A box plot would completely hide the bimodal shape! This is the **"aha!" moment** for violin plots.

----------

## Basic Violin Plot Script

### What This Script Does

> Creates a simple violin plot showing exam scores with mean, median, and extreme values marked.

## Script

```python
# Step 1: Import required libraries
import numpy as np
import matplotlib.pyplot as plt

# Step 2: LAYER 1 - Prepare the DATA
# Set random seed for reproducible results
np.random.seed(10)

# Generate bell-shaped exam scores
# loc=70 means average score is 70
# scale=10 means standard deviation is 10
# size=100 means 100 students
scores = np.random.normal(loc=70, scale=10, size=100)

# Add a few unusual values (outliers)
scores = np.append(scores, [25, 30, 105])

# Step 3: Create figure and axis
fig, ax = plt.subplots(figsize=(7, 4))

# Step 4: LAYER 2 - Create violin plot with OPTIONS
ax.violinplot(
    scores,              # The data to plot
    showmeans=True,      # Show mean as green triangle. Green triangle is default marker for mean in violin plot
    showmedians=True,    # Show median as red line. Red line is default marker for median in violin plot
    showextrema=True     # Show minimum and maximum
)

# Step 5: LAYER 3 - Add CHART ELEMENTS
ax.set_title("Violin Plot of Exam Scores")
ax.set_ylabel("Marks")
ax.set_xlabel("Distribution")
# Add grid for better readability. 
# True means show grid, alpha=0.3 makes it lighter, axis='y' means only horizontal grid lines
ax.grid(True, alpha=0.3, axis='y')

# Step 6: Display the plot
plt.show()

```

### Output of the script

![Plot generated by above script](/resources/ch15-matplotlib-violin1.png)




### Why This Script Is Written This Way

> **Design Logic**:
> 
> **1. Reproducible Results**  
> • `np.random.seed(10)` ensures same random data every run  
> • Students can compare their output with book examples
> 
> **2. Realistic Data**  
> • `loc=70, scale=10` creates scores centred around 70  
> • Adding outliers `[25, 30, 105]` shows how violin plots handle extremes
> 
> **3. Three-Layer Structure**  
> • Data preparation isolated in Layer 1  
> • Plot options (`showmeans`, `showmedians`) in Layer 2  
> • Titles, labels, grid in Layer 3
> 
> **4. One Option Per Line**  
> • Each parameter on its own line with comment  
> • Easy to read, modify, or remove one setting at a time
> 
> **5. What You Will See**  
> • Violin shape widest around 70 (where most scores are)  
> • Green triangle marks the mean  
> • Red line marks the median  
> • Narrow tails at 25, 30, and 105 (outliers)

## Bimodal Distribution

### Why Bimodal Data Proves Violin Plots Are Essential

> **Scenario**: You have two different classes (Class A and Class B) with 50 students each.  . One class (Class A) performed poorly (average 50), another (Class B) performed well (average 80). Suppose the scores of the two classes (of 50 students each) is combined and the scores of the combined group (100 students) is given to you.

**What Happens:**

-   **Histogram**: Shows two clear peaks
-   **Box Plot**: Shows one box, completely hiding the two groups!
-   **Violin Plot**: Reveals both peaks clearly

### Comparison Script: Same Data, Three Views

```python

# Histogram vs Box Plot vs Violin Plot
# Bimodal Distribution (Where violin plot shines!)
# Bimodal distribution: Two distinct groups in the data. 
# Peak 1: Around 50 marks, Peak 2: Around 80 marks.
# Box plot hides this, but histogram and violin plot reveal it.

import numpy as np
import matplotlib.pyplot as plt

# Step 1: LAYER 1 - Prepare the DATA
# Set random seed for reproducible results
np.random.seed(42)

# Create BIMODAL data: two distinct groups
# Group A: 50 students with scores around 50
# loc=50 means average score is 50, scale=8 means standard deviation is 8, 
# size=50 means 50 students
group1 = np.random.normal(loc=50, scale=8, size=50)

# Group B: 50 students with scores around 80
# loc=80 means average score is 80, scale=8 means standard deviation is 8, 
# size=50 means 50 students
group2 = np.random.normal(loc=80, scale=8, size=50)

# Combine both groups to create a bimodal distribution
scores = np.concatenate([group1, group2])

# Step 2: Calculate quartiles for reference
# np.percentile() calculates the specified percentile values.
q1 = np.percentile(scores, 25)  # 25th percentile
q2 = np.percentile(scores, 50)  # Median
q3 = np.percentile(scores, 75)  # 75th percentile

# Step 3: Create three vertically stacked subplots
# gridspec_kw={"height_ratios": [3, 1, 2]} means histogram is taller- occupies 3 parts vertically,
# box plot is shorter occupies 1 part vertically, and violin plot is medium occupies 2 parts vertically.
fig, ax = plt.subplots(3, 1, figsize=(8, 10), 
                       gridspec_kw={"height_ratios": [3, 1, 2]})

# Panel 1: HISTOGRAM. It is top panel. Height ratio is 3 (taller).
# bins=15→ divide score range into 15 intervals, color and edgecolor for aesthetics, 
# alpha=0.8 for slight transparency
ax[0].hist(scores, bins=15, color="skyblue", 
           edgecolor="black", alpha=0.8)

# Add quartile reference lines
ax[0].axvline(q1, color="red", linestyle="--", 
              linewidth=2, label=f"Q1 ({q1:.1f})")
ax[0].axvline(q2, color="green", linestyle="-", 
              linewidth=2, label=f"Median ({q2:.1f})")
ax[0].axvline(q3, color="red", linestyle="--", 
              linewidth=2, label=f"Q3 ({q3:.1f})")

ax[0].set_title("Histogram: Shows TWO Clear Peaks", 
                fontsize=12, fontweight='bold')
ax[0].set_ylabel("Frequency")
ax[0].legend(loc='upper left')
ax[0].grid(axis="y", alpha=0.3)

# Panel 2: BOX PLOT. It is middle panel. Height ratio is 1 (shorter).
ax[1].boxplot(scores, vert=False, showmeans=True,
              patch_artist=True,
              boxprops=dict(facecolor='lightgreen'))

ax[1].set_title("Box Plot: HIDES the Two Peaks!", 
                fontsize=12, fontweight='bold', color='red')
ax[1].set_yticks([])
ax[1].set_xlabel("Score")

# Panel 3: VIOLIN PLOT. It is bottom panel. Height ratio is 2 (medium).
ax[2].violinplot(scores, showmeans=True, showmedians=True,
                 showextrema=True, vert=False)

ax[2].set_title("Violin Plot: REVEALS Both Peaks!", 
                fontsize=12, fontweight='bold', color='blue')
ax[2].set_xlabel("Score")
ax[2].set_yticks([])

# Add explanatory text
fig.suptitle("Bimodal Distribution: Same Data, Three Views\n"
             "Notice how box plot hides what histogram and violin plot reveal!",
             fontsize=14, fontweight='bold', y=0.995)

# Step 4: Adjust layout and display
plt.tight_layout()
plt.show()

# Step 5: Print quartile values
print("=" * 50)
print("STATISTICAL SUMMARY")
print("=" * 50)
print(f"Q1 (25th percentile): {q1:.2f}")
print(f"Median (50th percentile): {q2:.2f}")
print(f"Q3 (75th percentile): {q3:.2f}")
print(f"Minimum: {scores.min():.2f}")
print(f"Maximum: {scores.max():.2f}")
print("=" * 50)
print("KEY OBSERVATION:")
print("The box plot shows ONE box from Q1 to Q3,")
print("but the data actually has TWO distinct groups!")
print("=" * 50)

```
### Output plot

![Bimodal distribution](/resources/ch15-matplotlib-violin-bimodal.png)


### What to Observe

| Plot Type | What You See | What It Tells You |
| --- | --- | --- |
| Histogram | Two clear peaks at ~50 and ~80 | "There are two groups in the data" |
| Box Plot | One box from Q1 to Q3 | "Data ranges from X to Y" (but hides the two groups!) |
| Violin Plot | Two wide sections (bulges) | "There are two groups in the data" |



Why This Matters:       

 - Imagine you are a teacher analyzing exam scores from two classes. 
 - If you only use a box plot:   
   - You miss that Class A struggled You miss that Class B excelled.
   - You treat them as one group  
 - If you use histogram or violin:  
   - You see two distinct groups     
   - You investigate why they differ 
   - You tailor teaching strategies 
 - This is why violin    plots matter!


## Important Parameters for Violin Plots

### Key Options Table

| Parameter | Purpose | Example Value | When to Use |
| --- | --- | --- | --- |
| showmeans | Display mean marker | True or False | When you want to compare mean vs median |
| showmedians | Display median line | True or False | Always recommended for central tendency |
| showextrema | Show min/max points | True or False | When outliers matter |
| vert | Vertical or horizontal | True (vertical) or False (horizontal) | Use horizontal for long labels |
| widths | Width of violins | 0.8 (default) | Adjust when comparing many groups |
| points | Smoothness of curve | 100 (default) | Increase for smoother curves |


## When Should We Use a Violin Plot?

### Good Use Cases

| Situation | Why Violin Plot Works |
| --- | --- |
| Comparing exam scores across multiple classes | Shows if each class has one peak or multiple peaks |
| Analyzing survey responses | Reveals if respondents cluster into groups |
| Scientific measurements | Displays distribution shape + statistical summary |
| Financial data (stock returns) | Shows skewness and potential multiple regimes |
| Quality control | Detects if production has multiple modes (shifts) |


### When NOT to Use Violin Plots

| Situation | Better Alternative |
| --- | --- |
| Small datasets (< 10 points) | Box plot or strip plot |
| Need exact frequency counts | Histogram |
| Many outliers to identify | Box plot |
| Very limited space | Box plot (more compact) |
| Audience unfamiliar with statistics | Histogram (easier to understand) |

## Further challenges
```python
# Challenge 1: Change the bimodal data to trimodal (three peaks)
# Hint: Create three groups with different loc values
# group1 = np.random.normal(loc=40, scale=5, size=40)
# group2 = np.random.normal(loc=60, scale=5, size=40)
# group3 = np.random.normal(loc=85, scale=5, size=40)

# Challenge 2: Make the violin plots horizontal
# Hint: Change vert=False in violinplot() and adjust labels

# Challenge 3: Compare multiple groups side-by-side
# Hint: Pass a list of lists to violinplot()
# data = [group1, group2, group3]
# ax.violinplot(data, showmeans=True, showmedians=True)

# Challenge 4: Save the figure
# Hint: Add fig.savefig("violin_comparison.png", dpi=300, 
#                       bbox_inches='tight') before plt.show()

# Challenge 5: Change the smoothness
# Hint: Add points=200 to violinplot() for smoother curves
```




