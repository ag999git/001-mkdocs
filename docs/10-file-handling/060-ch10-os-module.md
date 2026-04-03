


## Study Extended Concepts & Additional Methods of the `os` module

### 1. `os.remove(path)`

Deletes a file.

-   Raises `FileNotFoundError` if file does not exist
-   Raises `PermissionError` if file is in use

----------

### 2. `os.rmdir(path)`

Removes an **empty directory**

-   Fails if directory is not empty

----------

### 3. `os.makedirs(path, exist_ok=True)`

Creates directories (including nested ones)

----------

### 4. `os.path` Utilities 

  

| Function | Purpose |
| --- | --- |
| os.path.exists(path) | Check if path exists |
| os.path.isfile(path) | Check if file |
| os.path.isdir(path) | Check if directory |
| os.path.join(a,b) | Safe path joining |

### Summary Table

  

| Operation | Function | Works On | Error Type |
| --- | --- | --- | --- |
| Rename | `os.rename()` | File/Dir | `FileNotFoundError` |
| Delete file | `os.remove()` | File | `PermissionError` |
| Remove dir | `os.rmdir()` | Empty dir | `OSError` |
| List files | `os.listdir()` | Directory | `FileNotFoundError` |


### Common Errors & Exceptions

  

| Error | Cause |
| --- | --- |
| `FileNotFoundError` | File/path does not exist |
| `PermissionError` | No permission |
| `OSError` | Invalid operation |


## Script

```python

import os

# STEP 1: Check current directory
cwd = os.getcwd()
print("Current Directory:", cwd)  # Current Directory: <your_current_directory>

# STEP 2: Create a new directory
os.makedirs("test_dir", exist_ok=True)  
print("Directory 'test_dir' created or already exists.")

# STEP 3: Create a file inside it
# Construct file path using os.path.join for better compatibility across OS
file_path = os.path.join("test_dir", "sample.txt")  
with open(file_path, "w") as f:  
    f.write("Hello OS Module")
print("File 'sample.txt' (1) opened OR (2) created & opened in 'test_dir'")

# STEP 4: Check file existence
if os.path.exists(file_path):
    print("File exists")

# STEP 5: Rename file
new_path = os.path.join("test_dir", "renamed.txt")
os.rename(file_path, new_path)
print("File renamed to 'renamed.txt'.")

# STEP 6: List contents
print("Directory contents:", os.listdir("test_dir"))

# STEP 7: Delete file safely
if os.path.isfile(new_path):
    os.remove(new_path)
    print("File 'renamed.txt' deleted.")

# STEP 8: Remove directory
os.rmdir("test_dir")
print("Directory 'test_dir' deleted.")


```




















