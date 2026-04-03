



## 1. PROJECT

## Title: “Investigation of File Capability Methods in Python: `readable()`, `writable()`, and `seekable()`”

----------

## Problem Statement

Write a Python program to study and demonstrate the behavior of the following file object methods:

-   `file.readable()`
-   `file.writable()`
-   `file.seekable()`

----------

## Objectives

Your program must:

### A. Functional Study

1.  Open files in different modes:
    -   `'r'`, `'w'`, `'a'`, `'r+'`, `'rb'`
2.  For each mode, check:
    -   Whether file is readable
    -   Whether file is writable
    -   Whether file is seekable

----------

### B. Experimental Verification

-   Attempt operations based on capability:
    -   Call `read()` only if `readable() == True`
    -   Call `write()` only if `writable() == True`
    -   Call `seek()` only if `seekable() == True`

----------

### C. Error Demonstration

-   Show what happens if:
    -   You try to read from a non-readable file
    -   You try to write to a non-writable file
-   Include these as **commented (unhashed) lines**

----------

### D. Best Practices

-   Use `with` statement
-   Avoid unsafe operations
-   Use capability checks before operations

----------

## Learning Outcomes

By using  File Capability Methods in Python one can:

-   Predict file behavior based on mode
-   Write safe file-handling code
-   Avoid runtime errors using capability checks

----------

## 2. EXPECTED ANSWER (CONCEPTUAL)

### `readable()`

Returns `True` if the file is opened in a mode that allows reading.  
Example: `'r'`, `'r+'`, `'rb'`

----------

### `writable()`

Returns `True` if writing is allowed.  
Example: `'w'`, `'a'`, `'r+'`

----------

### `seekable()`

Returns `True` if the file supports random access (moving pointer).  
Most disk files return `True`.



  ### Key Insight: These methods help **avoid errors before they occur**

| Mode | readable() | writable() |
| --- | --- | --- |
| r' | True | False |
| w' | False | True |
| a' | False | True |
| r+' | True | True |

### Script

```python

# Study: File Capability Methods
# readable(), writable(), seekable()

# STEP 1: Create a sample file
with open("cap_demo.txt", "w") as f:
    f.write("Hello File Handling\n")

# STEP 2: Test different modes
modes = ["r", "w", "a", "r+", "rb"]

for mode in modes:
    print(f"\n--- Opening file in mode: {mode} ---")
    
    with open("cap_demo.txt", mode) as f:
        
        # Check capabilities
        print("Readable?:", f.readable())  # True for 'r' and 'r+', False for 'w', 'a', 'rb'
        print("Writable?:", f.writable())  # True for 'w', 'a', 'r+', False for 'r', 'rb'
        print("Seekable?:", f.seekable())  # True for all modes except some special files
        
        # Safe operations based on capability
        
        # Read only if allowed
        if f.readable():  # Only attempt to read if the file is opened in a mode that allows reading
            print("Reading content:", f.read(10))
        else:
            print("Read not allowed in this mode")
        
        # Write only if allowed
        if f.writable():  # Only attempt to write if the file is opened in a mode that allows writing
            f.write("Test\n")
            print("Write operation performed")
        else:
            print("Write not allowed in this mode")
        
        # Seek only if allowed
        if f.seekable():  # Only attempt to seek if the file is opened in a mode that allows seeking
            f.seek(0)
            print("Pointer reset using seek()")


# STEP 3: Demonstrating errors (commented)

# ERROR: Reading from write-only file
# with open("cap_demo.txt", "w") as f:  # Opened in write mode
#     f.read()   # UnsupportedOperation: not readable

# ERROR: Writing to read-only file
# with open("cap_demo.txt", "r") as f:  # Opened in read mode
#     f.write("Hello")   # UnsupportedOperation: not writable


# STEP 4: Conclusion message
print("\nProgram completed safely using capability checks.")


```


















