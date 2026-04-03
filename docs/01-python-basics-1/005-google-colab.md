
You can access a working Google Colab Notebook by clicking the link below

[![Open In Colab](https://img.shields.io/badge/Google_Colab-Try_Interactive_Code-FFD700?style=for-the-badge&logo=googlecolab&logoColor=white&labelColor=228B22)](https://colab.research.google.com/github/ag999git/001-Python-book-2026/blob/main/colab-nb/01Chapter1_pep.ipynb)





### Table of Contents
- [Google Colab – Beginner-Friendly Guide](#google-colab-beginner-friendly-uide)
- [2. How to Access Google Colab](#2-how-to-access-google-colab)
- [3. How to Create a New Notebook](#3-how-to-create-a-new-notebook)
- [4. Basic Interface Overview](#4-basic-interface-overview)
- [5. How to Run Code](#5-how-to-run-code)
- [6. How to Install Libraries](#6-how-to-install-libraries)
- [7. Uploading and Downloading Files](#7-uploading-and-downloading-files)
- [8. Connecting to Google Drive](#8-connecting-to-google-drive)
- [9. Using GPU/TPU in Colab](#9-using-gputpu-in-colab)
- [FAQs on Google Colab](#faqs-on-google-colab)
    - [Difference between Google Colab and Jupyter Notebooks](#19-what-is-the-difference-between-colab-and-jupyter-notebook)
- [Summary](#summary)
- [Google Colab. Quick Cheatsheet](#google-colab-quick-cheatsheet)
    - [Magic commands](#9-magic-commands-very-useful)
    - [GPU/ TPU Usage](#10-gpu--tpu-usage)
    - [Markdown cheatsheet](#12-markdown-cheatsheet-for-text-cells)
- [Simple example scripts:- printing, variables, input, math, loops, lists, dictionaries, functions, string operations & error handling](#beginner-python-scripts-for-google-colab)
- [Beginner syllabus for learning Google colab](#beginner-syllabus-for-python--google-colab)

### Google Colab – Beginner-Friendly Guide

Google Colab (short for *Colaboratory*) is a free, cloud-based Jupyter Notebook environment provided by Google.  
It allows you to write and run Python code **in your browser**, without installing Python on your computer.

---

#### 1. What is Google Colab?

- A **browser-based Jupyter Notebook** environment.
- Runs entirely in the **cloud** (Google servers).
- Requires **no installation** on your computer.
- Great for:
  - Data science
  - Machine learning
  - Learning Python
  - Running experiments that need GPU/TPU

You only need **Google Chrome** (or any browser) and a **Google account**.

---

### 2. How to Access Google Colab
[Go back to Table of Contents](#table-of-contents)

#### Method 1 (Recommended)
Go to:- https://colab.research.google.com

#### Method 2 (From Google Drive)
1. Open **drive.google.com**
2. Click **New**
3. Click **More**
4. Choose **Google Colaboratory**

#### Method 3 (Open from GitHub)
1. Open any GitHub repo containing `.ipynb` notebook
2. Click **Open in Colab** button (if available)
3. OR manually change the URL:
   ```
   github.com → githubtocolab.com
   ```

---

### 3. How to Create a New Notebook
[Go back to Table of Contents](#table-of-contents)


From the Colab landing page:

- Click **File → New Notebook**

A new notebook opens with the first code cell ready.

File name will look like:

```
Untitled0.ipynb
```

You can rename it by clicking on the filename at the top.

---

### 4. Basic Interface Overview
[Go back to Table of Contents](#table-of-contents)


Google Colab provides:
- **Code cells** (for Python code)
- **Text/Markdown cells** (for explanations)
- **Run button** (`▶ Run`) to execute a cell
- **Runtime menu** for controlling the execution environment
- A **left sidebar** that contains:
  - File browser
  - Search
  - Table of contents
  - Variables view

---

### 5. How to Run Code
[Go back to Table of Contents](#table-of-contents)


Inside a code cell:

#### Option A — Click the `▶ Run` button  
#### Option B — Press:

```
Shift + Enter
```

Colab will execute the cell and show the output below it.

---

### 6. How to Install Libraries
[Go back to Table of Contents](#table-of-contents)


Colab already includes many libraries:

- NumPy  
- Pandas  
- Matplotlib  
- TensorFlow  
- PyTorch  
- Seaborn  
- scikit-learn  

To install a library that is not available:

#### Use `pip` inside notebook:

```python
!pip install library_name
```

Example:

```python
!pip install openpyxl
```

After installing, you can import:

```python
import openpyxl
```

> Note: The `!` tells Colab to run the command in the system shell.

---

### 7. Uploading and Downloading Files
[Go back to Table of Contents](#table-of-contents)


#### Upload a file from your computer:
```python
from google.colab import files
files.upload()
```

#### Download a file:
```python
files.download('filename.csv')
```

---

### 8. Connecting to Google Drive
[Go back to Table of Contents](#table-of-contents)


To use files stored in Google Drive:

```python
from google.colab import drive
drive.mount('/content/drive')
```

After this, you'll see:

```
/content/drive/MyDrive/
```

---

### 9. Using GPU/TPU in Colab
[Go back to Table of Contents](#table-of-contents)


#### Check if GPU is available:

```python
import tensorflow as tf
tf.config.list_physical_devi
```



### FAQs on Google Colab
[Go back to Table of Contents](#table-of-contents)


Google Colab is a free, cloud-based Python environment that lets you write and run code in your browser.  
Below are answers to the most common questions.

---

#### 1. What is Google Colab?

Google Colab (Colaboratory) is a **browser-based Jupyter Notebook** hosted on Google’s cloud servers.  
You write Python code in your browser, and Google runs the code on its machines.

---

#### 2. Do I need to install Python?

**No installation needed.**  
All Python execution happens on Google’s servers.

Just open Colab in your browser.

---

#### 3. How do I open Google Colab?

### Method 1:

`https://colab.research.google.com`

### Method 2 (From Google Drive):
`Drive → New → More → Google Colaboratory`

### Method 3 (From GitHub):
Open any `.ipynb` notebook → click **Open in Colab** (if available).



#### 4. Is Google Colab free?
[Go back to Table of Contents](#table-of-contents)


- Yes  
- Includes **free GPU / TPU** support  
- Free Google Drive integration

---

#### 5. What is a notebook (`.ipynb`)?

A notebook is a file containing:

- Python code cells  
- Text/Markdown cells  
- Outputs  
- Charts/graphs  

File extension:

```
.ipynb
```

---

#### 6. How do I run code?

Inside a code cell:

- Click the `▶ Run` button  
or  
- Press:

```
Shift + Enter
```

---

#### 7. How do I install Python libraries in Colab?
[Go back to Table of Contents](#table-of-contents)


Use `pip` with `!`:

```python
!pip install library_name
```

Examples:

```python
!pip install numpy
!pip install matplotlib
```

---

#### 8. Why is there a `!` before pip commands?

The exclamation mark runs the command in the **system shell**, not as Python code.

---

#### 9. How do I upload files from my computer?

Use:

```python
from google.colab import files
files.upload()
```

You can upload CSV, images, text files, etc.

---

#### 10. How do I download a file?

```python
from google.colab import files
files.download("myfile.csv")
```

---

#### 11. How do I access my Google Drive files?
[Go back to Table of Contents](#table-of-contents)


Mount Drive:

```python
from google.colab import drive
drive.mount('/content/drive')
```

Your Drive appears at:

```
/content/drive/MyDrive/
```

---

#### 12. Does Colab save my work automatically?

Yes if saved to **Google Drive**  
No if it's a temporary notebook (not saved)

Click:

**File → Save a copy in Drive**

---

#### 13. Why does Colab disconnect?

Common reasons:

- You left the notebook idle  
- You used too much RAM  
- The runtime session expired (free limit)  
- Too many users on free tier

---

#### 14. Will I lose everything if Colab disconnects?

You will NOT lose:

- Your notebook file (it stays saved)

You WILL lose:

- Variables  
- Temporary files  
- Installed libraries  

Just rerun the necessary cells.

---

#### 15. Can I use Colab offline?
[Go back to Table of Contents](#table-of-contents)


 **No**, Colab requires an internet connection.

---

#### 16. Is Google Colab good for beginners?

✔ Yes, excellent for beginners:

- No installation  
- Very easy to use  
- Free GPU  
- Works on any device  
- Perfect for learning Python / ML  

---

#### 17. Can I create Python `.py` files?

Yes, using:

```python
%%writefile script.py
print("hello")
```

---

#### 18. Is Colab good for machine learning?

- Good for small/medium ML models  
- Not for huge datasets or very large neural nets  

Colab offers:

- Free CPU
- Free GPU (limited)
- Free TPU (limited)

---

#### 19. What is the difference between Colab and Jupyter Notebook?
[Go back to Table of Contents](#table-of-contents)


| Feature | Google Colab | Jupyter Notebook |
|---------|--------------|------------------|
| Installation |  None |  Python required |
| Runs On | Google Cloud | Your computer |
| GPU |  Free GPU/TPU | Only if your PC has GPU |
| Saves Files | Temporary | Permanent |
| Requires Internet |  Yes |  No |

---

#### 20. Should I use Colab or VS Code?

Use **Colab** for:

- Learning Python  
- Machine learning practice  
- When installing Python is difficult

Use **VS Code** for:

- Real projects  
- App development  
- Offline coding  
- Managing virtual environments  

---

### Summary

Google Colab is one of the easiest tools for beginners.  
You get:

- Free Python + Jupyter  
- Free GPU  
- No installation  
- Browser-based workflow  
- Easy file handling  
- Google Drive integration  

Perfect for learning and experimentation!


### Google Colab. Quick Cheatsheet
[Go back to Table of Contents](#table-of-contents)


A short, practical cheat-sheet of commands and functions commonly used in Google Colab.

---

#### 1. Running Code

Run a cell:
- Click `▶ Run`  
- OR press:

```
Shift + Enter
```

Run a cell and insert a new one below:

```
Alt + Enter
```

---

#### 2. Installing Python Libraries

Use pip with `!`:

```python
!pip install library_name
```

Examples:

```python
!pip install numpy
!pip install pandas
!pip install matplotlib
!pip install openpyxl
```

Upgrade a library:

```python
!pip install --upgrade library_name
```

---

#### 3. Uploading & Downloading Files

##### Upload a file from your computer:

```python
from google.colab import files
files.upload()
```

##### Download a file from Colab:

```python
from google.colab import files
files.download("filename.csv")
```

---

#### 4. Working With Google Drive
[Go back to Table of Contents](#table-of-contents)


##### Mount Google Drive:

```python
from google.colab import drive
drive.mount('/content/drive')
```

Your Drive appears in:

```
/content/drive/MyDrive/
```

##### List files:

```python
!ls /content/drive/MyDrive/
```

---

#### 5. Saving Output Files

Save any object to a file:

```python
with open("output.txt", "w") as f:
    f.write("Hello Colab!")
```

Download:

```python
from google.colab import files
files.download("output.txt")
```

---

#### 6. Displaying Plots

Matplotlib example:

```python
import matplotlib.pyplot as plt

plt.plot([1,2,3,4], [10,20,25,30])
plt.title("Sample Plot")
plt.show()
```

---

#### 7. Importing Common Libraries

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

---

#### 8. System Commands

List files:

```python
!ls
```

Check Python version:

```python
!python --version
```

See current directory:

```python
!pwd
```

Change directory:

```python
%cd /content
```

---

#### 9. Magic Commands (Very Useful)
[Go back to Table of Contents](#table-of-contents)


Time execution:

```python
%%time
```

Run a shell command:

```python
!command_here
```

Show variables:

```python
%whos
```

---

#### 10. GPU / TPU Usage
[Go back to Table of Contents](#table-of-contents)


##### Enable GPU or TPU:

```
Runtime → Change runtime type → Hardware accelerator
```

Choose: **GPU** or **TPU**

##### Check GPU:

```python
!nvidia-smi
```

TensorFlow GPU check:

```python
import tensorflow as tf
tf.config.list_physical_devices('GPU')
```

---

#### 11. Clearing Variables & Environment

##### Clear variables:

```python
%reset -f
```

##### Restart runtime:

```
Runtime → Restart runtime
```

---

#### 12. Markdown Cheatsheet (For Text Cells)

##### Headings:
```markdown
# Heading 1
## Heading 2
### Heading 3
```

##### Bold & Italic:
```markdown
**bold**
*italic*
```

### Simple example scripts for writing markdown
[Go back to Table of Contents](#table-of-contents)


```markdown
`inline code`
```

### Lists:
```markdown
- item 1
- item 2
```

##### Python Code block in markdown cell:

```python
print("Hello")
```




### Beginner Python Scripts for Google Colab  
[Go back to Table of Contents](#table-of-contents)

These mini-scripts explain Python basics.  
You can paste each one into a Colab cell and run it.

---

#### 1. Print a Message (Hello World)

```python
print("Hello, world! This is my first Python program!")
```

---

#### 2. Variables and Basic Math

```python
a = 10
b = 5

sum_value = a + b
product = a * b

print("a =", a)
print("b =", b)
print("Sum =", sum_value)
print("Product =", product)
```

---

#### 3. Getting Input From User

```python
name = input("What is your name? ")
print("Hello", name, "welcome to Python!")
```

---

#### 4. If-Else Conditions

```python
number = 7

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")
```

---

#### 5. Simple For Loop

```python
for i in range(1, 6):
    print("Current number:", i)
```

---

#### 6. While Loop Example

```python
count = 1

while count <= 5:
    print("Count =", count)
    count += 1
```

---

#### 7. List Basics — Create & Access Elements

```python
fruits = ["apple", "banana", "mango"]

print("First fruit:", fruits[0])
print("All fruits:", fruits)

# Add a fruit
fruits.append("orange")
print("Updated list:", fruits)
```

---

#### 8. Looping Through a List

```python
students = ["Aditi", "Rahul", "Neha"]

for student in students:
    print("Student name:", student)
```

---

#### 9. Functions — Creating and Using Them

```python
def greet(name):
    print("Hello", name)

greet("Anurag")
greet("Sam")
```

---

#### 10. Function That Returns a Value

```python
def square(x):
    return x * x

print("Square of 5 is:", square(5))
```

---

#### 11. Dictionaries — Key-Value Pairs

```python
student = {
    "name": "Arjun",
    "age": 19,
    "course": "Python"
}

print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
```

---

#### 12. Basic String Operations
[Go back to Table of Contents](#table-of-contents)


```python
text = "Python Programming"

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Length:", len(text))
```

---

#### 13. Using `for` Loop With `range()`

```python
for i in range(3):
    print("Iteration number:", i)
```

---

#### 14. Writing a Simple Calculator

```python
x = 12
y = 4

print("Add:", x + y)    # 16
print("Subtract:", x - y)    # 8
print("Multiply:", x * y)    # 48
print("Divide:", x / y)    # 3
```

---

#### 15. Using Try-Except (Error Handling)

```python
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except:
    print("That was not a valid number!")
```

---

### Summary
[Go back to Table of Contents](#table-of-contents)


These scripts help beginners learn:
- printing  
- variables  
- input  
- math  
- loops  
- lists  
- dictionaries  
- functions  
- string operations  
- error handling  

All work directly in **Google Colab with zero installation**.


### Beginner Syllabus for Python + Google Colab  
[Go back to Table of Contents](#table-of-contents)

A simple, clear syllabus designed for absolute beginners learning Python using Google Colab.

---

### 1. Introduction to Google Colab

#### Topics:
- What is Google Colab?
- How Colab works (cloud-based Jupyter)
- Benefits (no installation, free GPU, browser-based)
- Limitations (session timeout, temporary storage)

#### Hands-On:
- Opening Colab
- Creating a new notebook
- Running a code cell
- Adding text/markdown cells
- Saving notebook to Google Drive

---

### 2. Python Basics
[Go back to Table of Contents](#table-of-contents)


#### Topics:
- Printing output  
- Comments (`#`)  
- Variables and data types  
  - int, float, string, bool  
- Basic math operations  
- Using `input()`  

#### Hands-On:
- “Hello World”
- Simple calculator
- Taking user input and printing output

---

### 3. Control Flow (If, Else, Elif)

#### Topics:
- Making decisions with `if`
- Boolean expressions
- `elif` ladders
- Comparison operators  
  (`==`, `!=`, `<`, `>`, `<=`, `>=`)  
- Logical operators (`and`, `or`, `not`)

#### Hands-On:
- Even/odd checker
- Grade calculator
- Age eligibility logic

---

### 4. Loops (For & While)

#### Topics:
- `for` loops with `range()`
- Looping over lists
- `while` loops
- Breaking out of loops (`break`, `continue`)

#### Hands-On:
- Print numbers 1–10
- Loop through a list of names
- Simple number guessing simulation

---

### 5. Data Structures
[Go back to Table of Contents](#table-of-contents)


#### Topics:
- Lists  
  - indexing, slicing  
  - append, remove, sort  
- Tuples (basics)
- Dictionaries  
  - keys, values  
  - updating entries  
- Strings as sequences

#### Hands-On:
- Managing a student list  
- Creating a dictionary for a student record  
- Basic string methods (`upper`, `lower`, `split`, `replace`)

---

### 6. Functions

#### Topics:
- Defining functions (`def`)
- Parameters & arguments
- Return values
- Default arguments

#### Hands-On:
- Create a simple `greet()` function
- Function to find the square of a number
- Function to calculate price after discount

---

### 7. Error Handling (Try–Except)
[Go back to Table of Contents](#table-of-contents)


#### Topics:
- Why errors happen
- Using `try` and `except`
- Handling invalid input

#### Hands-On:
- Ask user for a number (handle wrong input)
- Safe division (avoid division by zero)

---

### 8. Working With Files in Colab

#### Topics:
- Upload & download using `google.colab.files`
- Reading text/CSV files
- Writing output files

#### Hands-On:
- Upload a file and print its contents
- Create and download a text file

---

### 9. Using Google Drive in Colab
[Go back to Table of Contents](#table-of-contents)


#### Topics:
- Mounting Google Drive
- Reading/writing files in Drive
- Directory navigation

#### Hands-On:
- Save notebook outputs to Drive
- Read a file from Drive

---

### 10. Basic Data Visualization (No External Install)

*(Using built-in Matplotlib which is pre-installed in Colab)*

#### Topics:
- Line plots
- Bar charts
- Simple scatter plots

#### Hands-On:
- Plot a sample line graph
- Visualize random numbers
- Create a simple bar chart

---

### 11. Introduction to GPU in Colab

#### Topics:
- What is a GPU?
- How to enable GPU in Colab
- Checking GPU availability

#### Hands-On:
- `!nvidia-smi`
- TensorFlow or PyTorch GPU check  
  *(No deep ML yet — just checking device)*

---

### 12. Mini Projects (Beginner Level)
[Go back to Table of Contents](#table-of-contents)


#### Suggested Mini Projects:
- Simple calculator app  
- Student grade tracker  
- To-do list using lists  
- Word frequency counter  
- Basic data visualization with random data  
- File uploader that counts lines in a file  

---

### End-of-Course Outcomes

By the end of this syllabus, students should be able to:

- Use Google Colab confidently  
- Write and execute Python code  
- Work with variables, loops, functions, and conditionals  
- Use lists, dictionaries, and strings effectively  
- Handle simple errors  
- Upload and download files in Colab  
- Use Google Drive for saving work  
- Plot basic charts  
- Understand GPU basics in Google Colab  

---

### Recommended Progression (Suggested Weekly Plan)
[Go back to Table of Contents](#table-of-contents)


| Week | Topics Covered |
|------|----------------|
| Week 1 | Colab basics, print, variables, input |
| Week 2 | Conditions & loops |
| Week 3 | Lists, dictionaries, strings |
| Week 4 | Functions & error handling |
| Week 5 | File upload/download & Google Drive |
| Week 6 | Simple graphs |
| Week 7 | Mini projects |
| Week 8 | Revision + final mini project |

---

### Happy Learning!

This syllabus is ideal for absolute beginners using Google Colab to learn Python interactively and easily.


[Go back to Table of Contents](#table-of-contents)
