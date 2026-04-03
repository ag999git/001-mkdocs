



## 1. PROJECT “Study of seek(offset, whence) in Python and Its Behavior in Text vs Binary Files”



## Problem Statement

Write a Python program to investigate the behavior of the `seek()` method using different values of `offset` and `whence`.

Your program must:

### A. Understand Method Signature

Study and explain:

-   `seek(offset[, whence])`

Where:

-   **offset (Required):** Number of bytes to move the cursor
-   **whence (Optional):**
    -   `0 (SEEK_SET)` → from beginning
    -   `1 (SEEK_CUR)` → from current position
    -   `2 (SEEK_END)` → from end

----------

### B. Experimental Tasks

1.  Demonstrate:
    -   `seek(offset, 0)`
    -   `seek(offset, 1)`
    -   `seek(offset, 2)`
2.  Compare behavior in:
    -   Text mode
    -   Binary mode
3.  Show pointer movement using `tell()`

----------

### C. Critical Investigation 

Demonstrate the following caution:

> Seeking to an arbitrary byte offset in a multi-byte encoded file (like UTF-8) may land the cursor in the middle of a character, causing a `UnicodeDecodeError`.

----------

### D. Best Practices

-   Use `with` statement
-   Use proper encoding (`utf-8`)
-   Handle exceptions
-   Demonstrate correct vs incorrect usage

----------

## 2. EXPECTED ANSWER (CONCEPTUAL)

### Key Observations

1.  `seek(offset, 0)`
    -   Moves pointer relative to **start**
    -   Works in both text and binary modes
2.  `seek(offset, 1)` and `seek(offset, 2)`
    -   Reliable only in **binary mode**
    -   Limited or unsafe in text mode
3.  **Binary Mode Advantage**
    -   Precise byte-level control
    -   Suitable for random access
4.  **Text Mode Limitation**
    -   Encoding-dependent
    -   Pointer may not align with characters

----------

### Critical Insight

In UTF-8:

-   Some characters use **multiple bytes**
-   If `seek()` lands in the middle → decoding fails

----------

## 3.  Script


```python

# Study: seek(offset, whence) in Python

# STEP 1: Create a UTF-8 file with multi-byte characters
with open("utf_demo.txt", "w", encoding="utf-8") as f:  # Open for writing with UTF-8 encoding
    # 'é' and '€' are multi-byte characters in UTF-8 (2 bytes for 'é' and 3 bytes for '€')
    f.write("AéB€C\n")  # Total bytes: 1 (A) + 2 (é) + 1 (B) + 3 (€) + 1 (C) + 1 (\n) = 9 bytes

# STEP 2: Basic seek() usage in TEXT MODE
with open("utf_demo.txt", "r", encoding="utf-8") as f:  # Open for reading with UTF-8 encoding
    
    print("Initial position:", f.tell())  # 0
    
    # seek from beginning
    f.seek(1, 0)
    print("After seek(1,0):", f.read(1))  # May work but can cause issues if it lands in the middle of 'é' or '€'
    
    # NOTE:
    # seek(offset,1) and seek(offset,2) are NOT reliable in text mode
    # Uncommenting below may raise errors or behave inconsistently

    # f.seek(1, 1)  # Not recommended in text mode 
    # f.seek(-2, 2) # Not recommended in text mode


# STEP 3: Demonstrating the CAUTION (UnicodeDecodeError)
try:
    with open("utf_demo.txt", "r", encoding="utf-8") as f:
        
        # Move to arbitrary byte position (middle of multi-byte char)
        f.seek(2)   # This may land inside 'é' or '€'
        
        print("Attempting to read after unsafe seek:")
        print(f.read())   # May raise UnicodeDecodeError

except UnicodeDecodeError:
    print("UnicodeDecodeError occurred due to improper seek in UTF-8 file")

# STEP 4: Correct approach using BINARY MODE
with open("utf_demo.txt", "rb") as f:
    
    print("--- Binary Mode Demonstration ---")
    
    # seek from beginning
    f.seek(1, 0)  # Move 1 byte from start (may land in middle of 'é')
    print("seek(1,0):", f.read(2))  # Output may be b'\xc3\xa9' (raw bytes for 'é')
    
    # seek from current position
    f.seek(1, 1)  # Move 1 byte from current position (may land in middle of 'B' or '€')
    print("seek(1,1):", f.read(2))  # Output may be b'B\xc2\x80' (raw bytes for 'B' and part of '€')
    
    # seek from end
    f.seek(-4, 2)  # Move 4 bytes back from end (may land in middle of '€' or 'C')
    print("seek(-4,2):", f.read())  #Output may be b'B\xc2\x80C\n' (raw bytes)


# STEP 5: Safe method (read then process)
with open("utf_demo.txt", "r", encoding="utf-8") as f:  # Open for reading with UTF-8 encoding
    data = f.read()   # Safe full read
    print("Safe full read:", data)  # Output: AéB€C



```







