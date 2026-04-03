



## PROJECT



## Title

**“Design and Comparison of Algorithms for Inserting Data at Arbitrary Positions in a File in Python”**



## Problem Statement

In Python, file operations allow writing data either by **overwriting (`'w'`)** or **appending (`'a'`)**. However, Python does **not provide a direct method** to insert data at an arbitrary position (beginning or middle) within a file.

----------

## Tasks

### Task 1: Conceptual Understanding

1.  Explain why Python does not support direct insertion in the middle of a file.
2.  Explain the concept of **sequential file access**.
3.  Explain why insertion becomes a **read–modify–write problem**.

----------

### Task 2: Algorithm Design

Design and explain **two algorithms** for inserting a line at a given position in a file:

----------

### Algorithm 1: Temporary File Approach

-   Use a second file to store modified data
-   Insert data while copying

----------

### Algorithm 2: In-Memory List Approach

-   Read file into a list
-   Modify list
-   Write back

----------

### Task 3: Implementation

Write Python programs to implement both approaches with:

-   Proper function design
-   Meaningful variable names
-   Inline comments explaining each step

----------

### Task 4: Testing

#### Use a sample source file:  (Here in the solution script it is named source.txt)

11111111  
22222222  
33333333  
44444444  
55555555


#### Use a destination file: (Here in the solution script it is named destination.txt)

0000000

#### Insert above '0000000' at line number **2**


----------

### Task 5: Comparison

Compare both approaches based on:

-   Memory usage
-   Performance
-   Ease of implementation
-   Suitability for large files

----------


## ANSWER

----------

## 1. Conceptual Explanation**

----------

### Why direct insertion is not possible?

-   Files are stored as **continuous byte streams**
-   No built-in mechanism to “shift” data forward
-   Hence, inserting data requires:
    -   Reading existing data
    -   Modifying it
    -   Writing it back

----------

### Sequential Access

-   File is processed **line by line or byte by byte**
-   No random insertion support

----------

### Read–Modify–Write Model

-   Read original file
-   Modify content
-   Write new file

----------


## 2. Algorithm 1: Temporary File Approach**

----------

### Steps

1.  Open source file in read mode
2.  Open destination file in write mode
3.  Read line by line
4.  Insert new data at required position
5.  Copy remaining data
6.  Save result

----------

### Script (Method 1: Memory Efficient)


```python

import os

def insert_line_temp(src_file, dest_file, new_line, line_no):  # Define a function to insert a line into a file using a temporary file approach
    """
    Inserts a line into a file using a temporary file approach.
    Suitable for large files (memory efficient).
    """

    # STEP 1: Open source (read) and destination (write)
    with open(src_file, 'r') as f1, open(dest_file, 'w') as f2:  # Open source file for reading and destination file for writing
        
        current_line = 1  # Track current line number
        
        # STEP 2: Read file line-by-line
        for line in f1:  # Iterate through each line in the source file
            
            # STEP 3: Insert new line at desired position
            if current_line == line_no:  # Check if current line number matches the desired line number for insertion
                f2.write(new_line + '\n')   # Insert new content
                print(f"Inserted at line {line_no}: {new_line}")
            
            # STEP 4: Copy existing line
            f2.write(line)  # Write the current line from source to destination
            print(f"Copied line {current_line}: {line.strip()}")
            
            current_line += 1  # Increment line number for next iteration

        # STEP 5: If line_no is beyond file length → append
        if line_no >= current_line:  # Check if desired line number is greater than or equal to total lines in source file
            f2.write(new_line + '\n')  # Append new content at the end of destination file
            print(f"Appended at end: {new_line}")

    # OPTIONAL: Replace original file
    # os.replace(dest_file, src_file)  # Uncomment to replace original file with modified file (be cautious with this step)

"""
Create a sample source.txt file with following content for testing:
11111111
22222222
33333333
44444444
55555555

Insert:

0000000

at line number 2
"""

# Example usage
# Define source and destination file paths, new content, and line number to insert at 
# Note: Ensure 'source.txt' exists with enough lines for testing
# print source.txt content before running this code to see the effect of insertion
print("Before insertion:")
with open("source.txt", "r") as f:  # Open source file in read mode to display its content before insertion
    print(f.read())
    
src = "source.txt"  # Source file to read from
dest = "destination.txt"  # Destination file to write to
new_content = "00000000"  # New line to insert
line_number = 2  # Line number to insert at (1-based index)
insert_line_temp(src, dest, new_content, line_number)  # Call the function to perform the line insertion using a temporary file approach

# After running the code, check 'destination.txt' to see the inserted line and copied content
print("\nAfter insertion:")
with open(dest, "r") as f:  # Open destination file in read mode to display its content after insertion
    print(f.read())
    # Output will show the new line inserted at the specified line number, with existing lines copied over. If line_number is greater than the total lines in source.txt, the new line will be appended at the end of destination.txt.
    # Note: The original 'source.txt' remains unchanged. The new content is in 'destination.txt'.
    



```






## Algorithm 2: List-Based Approach



### Steps

1.  Read file into list using `readlines()`
2.  Insert new line in list
3.  Write list back to file

----------

### Script (Method 2: Simple but Memory Heavy)

```python

def insert_line_list(src_file, dest_file, new_line, line_no):  # Define a function to insert a line into a file using list manipulation approach
    """
    Inserts a line using list manipulation.
    Suitable for small files (easy to implement).
    """

    # STEP 1: Read entire file into memory
    with open(src_file, 'r') as f:  # Open source file in read mode to read its content
        lines = f.readlines()  # Read all lines into a list (each line is an element in the list)
    
    # STEP 2: Insert or append
    if line_no <= len(lines):  # Check if desired line number is within the range of existing lines
        lines.insert(line_no - 1, new_line + '\n')  # Insert at position
        print(f"Inserted at line {line_no}: {new_line}")
    else:
        lines.append(new_line + '\n')  # Append at end
        print(f"Appended at end: {new_line}")
    
    # STEP 3: Write modified content back
    with open(dest_file, 'w') as f:  # Open destination file in write mode to write the modified content
        f.writelines(lines)  # Write the modified lines back to the destination file
        
# See source.txt content before running this code to see the effect of insertion
print("Before insertion:")
with open("source.txt", "r") as f:  # Open source file in read mode to display its content before insertion
    print(f.read())

# Example usage
src = "source.txt"  # Source file to read from  
dest = "destination.txt"  # Destination file to write to
new_content = "00000000"  # New line to insert  
line_number = 2  # Line number to insert at (1-based index)
insert_line_list(src, dest, new_content, line_number)  # Call the function to perform the line insertion using list manipulation approach

# After running the code, check 'destination.txt' to see the inserted line and copied content
print("\nAfter insertion:")
with open(dest, "r") as f:  # Open destination file in read mode to display its content after insertion
    print(f.read())
    # Output will show the new line inserted at the specified line number, with existing lines copied over. If line_number is greater than the total lines in source.txt, the new line will be appended at the end of destination.txt.
    # Note: The original 'source.txt' remains unchanged. The new content is in 'destination.txt'.
    
    



```




### Comparison table (For the two algorithms)


| Feature | JSON | Pickle | Use Case |
| --- | --- | --- | --- |
| Portability | High | Low | APIs |
| Security | High | Low | Web |
| Object Support | Limited | Full | Python apps |
| Speed | Medium | High | Internal storage |


  
### Key Observations
Temporary file method:
-    Preferred in real-world systems
-    Scales well

List method:
-    Easier for beginners
-    Not suitable for large files









