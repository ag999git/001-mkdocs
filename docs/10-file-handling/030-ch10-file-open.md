




## PART 1: RESEARCH / PROJECT QUESTION 

### Title: “Comprehensive Study of Python File Opening Mechanism and File Object Behavior”

----------

### Problem Statement

Write a Python program that explores the `open()` function in detail, including:

### 1. Parameter Exploration

Study and demonstrate the use of:

-   `file`
-   `mode`
-   `encoding`
-   `errors`
-   `buffering`

----------

### 2. File Object Behavior

Using the file object, demonstrate:

-   Reading methods (`read`, `readline`)
-   Writing methods (`write`)
-   Control methods (`seek`, `tell`)
-   File attributes (`name`, `mode`, `encoding`, `closed`)

----------

### 3. Error Handling

Demonstrate and explain:

-   `FileNotFoundError`
-   `PermissionError`
-   `UnicodeDecodeError`
-   Writing string in binary mode error

----------

### 4. Best Practices

Your script must:

-   Use `with` statement
-   Use encoding properly
-   Handle exceptions using `try-except`
-   Avoid memory-heavy operations

----------

### 5. Experimental Requirements

-   Create at least one text file
-   Perform read/write operations
-   Demonstrate pointer movement
-   Include **intentional error cases (commented out)**

----------

### 6. Expected Output

-   Correct file reading/writing
-   Display of file attributes
-   Demonstration of pointer movement
-   Clear handling of exceptions

----------

## PART 2: Script (With explanation)

```python

# PROJECT: Detailed Study of open() in Python

# STEP 1: Writing to a file using good practices

# Using 'with' ensures automatic closing of file
with open("research_demo.txt", mode="w", encoding="utf-8") as f:
    
    # Writing text to file
    f.write("Line 1: Hello World\n")  # Remember to add newline for proper formatting
    f.write("Line 2: Python File Handling\n")  # Another line with newline at the end

    # Checking file attributes inside block
    print("File Name:", f.name)  # research_demo.txt
    print("Mode:", f.mode)  # w
    print("Encoding:", f.encoding)  # utf-8
    print("Is Closed (inside block):", f.closed)  # False

# Outside 'with', file is automatically closed
print("Is Closed (after block):", f.closed)


# STEP 2: Reading from file

with open("research_demo.txt", mode="r", encoding="utf-8") as f:  # Open for reading
    
    # tell() shows pointer position
    print("Initial Pointer:", f.tell())  # 0 at start

    # Read first 10 characters
    print("Read 10 chars:", f.read(10))  # Reads 'Line 1: He' (10 chars)

    # Pointer has moved
    print("Pointer after read:", f.tell())  # 10 after reading 10 chars

    # Move pointer back to beginning
    f.seek(0)  

    # Read one line
    print("First line:", f.readline())  # Line 1: Hello World

    # Read remaining lines
    print("Remaining lines:", f.readlines())  # ['Line 2: Python File Handling\n']

# STEP 3: Demonstrating buffering and errors parameter

with open("research_demo.txt", mode="r", encoding="utf-8", buffering=1, errors="strict") as f:
    print("\nReading with buffering and strict error handling:")
    print(f.read())

# STEP 4: Exception Handling Demonstration

try:
    # File does not exist
    f = open("non_existing.txt", "r")  # This will raise FileNotFoundError
except FileNotFoundError:
    print("Error: File not found")

try:
    # Wrong encoding (simulate error)
    f = open("research_demo.txt", "r", encoding="ascii")  # This may raise UnicodeDecodeError if file contains non-ASCII chars
    f.read()
except UnicodeDecodeError:
    print("Error: Encoding issue occurred")

# STEP 5: Common Mistakes (Commented Out)

# ERROR 1: FileNotFoundError
# f = open("no_file.txt", "r")  # This will raise FileNotFoundError since no_file.txt does not exist

# ERROR 2: Writing string in binary mode
# with open("file.bin", "wb") as f:  # Opened in binary mode
#     f.write("Hello")   # should be bytes → b"Hello"

# ERROR 3: Using file after closing
# f = open("research_demo.txt", "r")  # Opened for reading
# f.close()  # File is closed here
# f.read()   # ValueError: I/O operation on closed file. Error occurs because we are trying to read from a closed file object

# ERROR 4: Wrong mode usage
# f = open("research_demo.txt", "r")  # Opened in read mode
# f.write("Hello")   # Not allowed in read mode 

# ERROR 5: Forgetting newline
# with open("file.txt", "w") as f:  # This will create/overwrite file.txt with content "Line1Line2" without newline in between
#     f.write("Line1") # Writes 'Line1' without newline
#     f.write("Line2")   # Lines will join


# STEP 6: Demonstrating safe append

with open("research_demo.txt", "a", encoding="utf-8") as f:
    f.write("Line 3: Appended safely\n")  # This will add a new line without overwriting existing content

# STEP 7: Final Read (Verification)

with open("research_demo.txt", "r", encoding="utf-8") as f:
    print("Final File Content:")  # Reads entire file content
    for line in f:   # memory efficient reading
        print(line.strip())  # strip() to remove extra newlines for cleaner output



```






