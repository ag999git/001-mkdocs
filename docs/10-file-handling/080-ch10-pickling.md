




## PROJECT/ TASK QUESTION

## Title

**“Study of Object Serialization in Python using Pickle: Features, Limitations, and Security Concerns”**

----------

## Problem Statement

Design a Python program to explore **pickling and unpickling** of different Python objects and analyze:

1.  Behavior with multiple data types
2.  Binary representation of stored data
3.  Security risks of unpickling
4.  Error handling

----------

## Objectives

### A. Functional Study

-   Pickle and unpickle:
    -   List
    -   Dictionary
    -   Custom class object

----------

### B. Binary Inspection

-   Read raw file content using `read()`
-   Analyze byte stream

----------

### C. Error Demonstration

-   Try:
    -   Loading from empty file
    -   Loading corrupted file

----------

### D. Security Awareness

-   Understand why unpickling untrusted data is dangerous

----------

## ANSWER (CONCEPTUAL)

### Key Observations

1.  Pickle stores:
    -   Object data
    -   Instructions to reconstruct object
2.  Unpickling:
    -   Recreates object instance
    -   Restores attributes
3.  Pickle is:
    -   Python-specific
    -   Not secure for untrusted data

----------

### Table of common errors and their causes in Pickling/ Unpickling


  

| Error | Cause |
| --- | --- |
| `EOFError` | Empty file |
| `pickle.UnpicklingError` | Corrupted file |
| `AttributeError` | Class not defined |


## Script

```python

# PROJECT: Advanced Pickling in Python

import pickle

# STEP 1: Define a custom class to demonstrate pickling of complex objects
class Student:
    def __init__(self, name, marks):
        self.name = name  # Student's name
        self.marks = marks  # Student's marks

    def display(self):  # Method to display student information
        return f"{self.name}: {self.marks}"

# STEP 2: Create objects to be pickled
data = {
    "list": [1, 2, 3],
    "dict": {"a": 10, "b": 20},
    "object": Student("Anurag", 95)
}

# STEP 3: Pickle data
# adv.pkl is the file where we will store the pickled data
# .pkl is a common extension for pickle files, but you can use any extension you like
# We use binary mode 'wb' to write the pickled data to the file.
# The pickle.dump() function takes the data object and the file object as arguments and writes the pickled data to the file.
with open("adv.pkl", "wb") as f:
    pickle.dump(data, f)

# STEP 4: Inspect raw binary
# This will show the raw bytes of the pickled data, which is not human-readable.
# We use binary mode 'rb' to read the pickled data from the file.
# The pickle.load() function reads the pickled data from the file and converts it back to a Python object.
with open("adv.pkl", "rb") as f:
    print("Raw Bytes:", f.read())

# STEP 5: Unpickle data
# We read the pickled data from the file and convert it back to a Python object.
# The loaded variable will contain the original data structure (list, dict, and Student object) that we pickled.
# We can then access the contents of the loaded data to verify that it was correctly unpickled.
with open("adv.pkl", "rb") as f:
    loaded = pickle.load(f)

# STEP 6: Verify data
print("\nLoaded Data:")  
print(loaded["list"])  # Output: [1, 2, 3]
print(loaded["dict"])  # Output: {'a': 10, 'b': 20}
print(loaded["object"].display())  # Output: Anurag: 95

# STEP 7: Error demonstration (uncomment to test)
# with open("empty.pkl", "rb") as f:
#     pickle.load(f)   # EOFError - End of File error when trying to load from an empty file

# STEP 8: Security warning
# This can execute arbitrary code if the file is malicious. 
# Always ensure you trust the source of the pickle file before loading it.

# Never do this with untrusted files:
# pickle.load(open("unknown.pkl", "rb"))  # Dont load pickles from untrusted sources! 


```








