


## Part 1: Script Questions Based on Chapter 10 (20 Questions)


**1. Write a script that uses the with statement to create a file named practice.txt, writes three separate lines of text to it, and then attempts to print the closed attribute both inside and outside the block. Explain the result.**

```python

with open("practice.txt", "w") as f:
    f.write("Line A\nLine B\nLine C\n")
    print("Inside block, is closed?:", f.closed)
print("Outside block, is closed?:", f.closed)
```
The with statement acts as a Context Manager that automatically triggers the `.close()` method once the indented block is exited. Inside the block, the closed attribute returns False because the file handle is active and available for I/O operations. Once the indentation ends, Python guarantees the file is closed, so the second print statement returns True. This pattern prevents resource leaks and ensures data is flushed to the disk safely even if an error occurs.


**2. A student writes `f.write(["Hello", "World"])` and receives a `TypeError`. Rewrite this script using the correct method to write a list of strings to a file named list_data.txt.**

```python

data_list = ["Hello\n", "World\n"]
with open("list_data.txt", "w") as f:
    f.writelines(data_list)

```
The `write()` method only accepts a single str (or bytes in binary mode) as its argument, which is why passing a list causes a TypeError. To handle a sequence of strings, Python provides the `writelines()` method. It is important to remember that writelines() does not automatically add newline characters; therefore, each element in the list must explicitly include \n to prevent the words from being joined together on a single line in the output file.


**3. Develop a script that opens a text file, reads exactly 10 characters, and then uses `tell()` to report the pointer position. Finally, use seek(0) to return to the start and read the first line.**

```python

with open("sample.txt", "r") as f:
    print("Initial position:", f.tell())
    content = f.read(10)
    print("Position after reading 10 chars:", f.tell())
    f.seek(0)
    print("Back at start, first line is:", f.readline())
```

The `tell()` method provides the current byte offset of the file pointer; after reading 10 characters in a standard encoding, the pointer moves from 0 to 10. The seek(0) method is then used to manually reset the "cursor" back to the beginning of the file. This allows the script to call `readline()`, which starts its scan from the absolute beginning of the file rather than from where the previous read(10) left off.


**4. Create a script that demonstrates the "Exclusive Creation" mode. What happens if you run the script twice in a row?**

```python

try:
    with open("unique_log.txt", "x") as f:
        f.write("System Initialized.")
except FileExistsError:
    print("Error: The file already exists!")
```

The 'x' mode is designed for safety, ensuring that a file is only created if it does not already exist on the disk. On the first run, the script creates unique_log.txt and writes to it successfully. On the second run, Python detects the existing file and raises a `FileExistsError` instead of overwriting it like the 'w' mode would. This is a best practice for preventing accidental data loss in applications that generate unique session reports.


**5. Write a memory-efficient script to count the total number of lines in a 1GB text file without crashing the computer.**

```python

line_count = 0
with open("large_data.txt", "r") as f:
    for line in f:
        line_count += 1
print("Total Lines:", line_count)
```

Using `readlines()` or `read()` on a 1GB file would attempt to load the entire content into RAM, likely causing a "Memory Error" or system freeze. Instead, iterating directly over the file object (the f handle) utilizes a "lazy loading" approach where Python only loads one line into memory at a time. As the loop moves to the next line, the previous one is discarded from RAM, allowing the script to process files of virtually any size with minimal memory consumption.


**6. Provide a script that opens an image file called `photo.jpg` for reading and a new file called `backup.jpg` for writing. What specific mode suffixes must be used?**

```python

with open("photo.jpg", "rb") as source, open("backup.jpg", "wb") as dest:
    data = source.read()
    dest.write(data)
```

Because images are binary data, the mode must include the 'b' suffix (e.g., 'rb' for read-binary and 'wb' for write-binary). Using standard text modes would cause the interpreter to attempt to decode the image bytes into Unicode characters, leading to a UnicodeDecodeError or a corrupted copy. Binary mode ensures that the raw bytes are copied exactly as they exist on the disk, preserving the integrity of the image data.


**7. Write a script that uses `truncate(20)` on a file. Explain what happens to the content that existed at character 21 and beyond.**

```python

with open("test.txt", "r+") as f:
    f.truncate(20)
```

The `truncate()` method resizes the file to the exact number of bytes specified in the argument. If the file originally contained 100 characters, calling `truncate(20)` will keep the first 20 bytes and immediately delete everything else. This operation is irreversible; the data from position 21 to 100 is permanently removed from the storage medium. If no argument is provided, the file is truncated at the current pointer position as determined by `tell()`.


**8. Construct a script that demonstrates how to handle a FileNotFoundError using a `try...except` block when opening `config.json`.**

```python

try:
    with open("config.json", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("The configuration file is missing. Please check the directory.")
```

In Python, attempting to open a non-existent file in read mode results in a `FileNotFoundError`. By wrapping the `open()` call in a try block, the programmer can catch this specific exception and provide a user-friendly message or trigger a fallback mechanism (like creating a default config). This prevents the entire program from crashing and allows for "graceful degradation" of the software's functionality.


**9. Show a script that uses `f.seek(0, 2)` to move to the end of a file and then prints the total size of the file in bytes.**

```python

with open("data.bin", "rb") as f:
    f.seek(0, 2)
    file_size = f.tell()
    print(f"The file size is {file_size} bytes.")
```

In binary mode, the `seek()` method's second argument (`whence`) allows for relative movement. Passing 2 as the reference point tells Python to move the pointer relative to the end of the file. By using an offset of 0, the pointer lands exactly on the last byte. Calling `tell()` immediately afterward returns the offset from the beginning, which effectively gives the total byte count (size) of the file without having to read any of its content.


**10. Write a script to replace all occurrences of the word "Python" with "Java" in a file called `notes.txt` using the "Read-then-Write" approach.**

```python

with open("notes.txt", "r") as f:
    content = f.read()
    
new_content = content.replace("Python", "Java")

with open("notes.txt", "w") as f:
    f.write(new_content)
```

This script follows a two-step process: first, it opens the file in read mode to load the content into a variable. It then uses the string `.replace()` method to modify the data in memory. Finally, it re-opens the same file in write mode ('w'), which clears the old content, and writes the updated string back to the disk. While simple, this approach should only be used for smaller files, as loading the entire file into a string can be memory-intensive.


**11. Create a script that prints the name, mode, and encoding attributes of an open file object.**

```python

f = open("report.csv", "r", encoding="utf-16")
print(f"File Name: {f.name}")
print(f"Active Mode: {f.mode}")
print(f"Encoding Used: {f.encoding}")
f.close()
```

File object attributes provide metadata about the stream rather than the data itself. The name attribute returns the path provided during the `open()` call, mode confirms the permissions (like 'r'), and encoding shows how the bytes are being translated into text. These attributes are highly useful for debugging purposes, ensuring that a function receiving a file handle is working with the correct file and character set.


**12. Write a script that opens a file in a+ mode, writes a new log entry, and then reads the entire file from the beginning.**

```python

with open("log.txt", "a+") as f:
    f.write("New Entry: 10:00 AM\n")
    f.seek(0)
    print(f.read())
```

The a+ (Append and Read) mode is unique because it allows for both operations. However, after the `write()` call, the file pointer is automatically moved to the end of the file. If the programmer immediately calls `read()`, they will receive an empty string because there is no data "after" the end. To see the content, `f.seek(0)` must be used to manually move the pointer back to the start of the file before reading.


**13. A user wants to write the string "© 2024" to a file. Write a script that specifies the encoding as 'utf-8' to ensure the symbol is saved correctly.**

```python

with open("copyright.txt", "w", encoding="utf-8") as f:
    f.write("© 2024")
```

Special characters like the copyright symbol (©) are not part of the basic ASCII character set. If the encoding is not specified, Python may use a system-default encoding (like cp1252 on older Windows systems) that might not support this symbol, leading to a UnicodeEncodeError. Explicitly setting the encoding to 'utf-8' ensures that the character is stored using a globally recognized standard, making the file readable across different operating systems.


**14. Write a script that demonstrates using writelines() with a list of numbers. Explain why you must convert the numbers to strings first.**

```python

numbers = [10, 20, 30]
# Convert to strings: ["10\n", "20\n", "30\n"]
string_numbers = [str(n) + "\n" for n in numbers]

with open("numbers.txt", "w") as f:
    f.writelines(string_numbers)
```

The file writing methods in Python, including write() and writelines(), only accept string or bytes data types. Attempting to pass raw integers would result in a TypeError because the file system requires character-encoded data to be written to a text file. Converting the integers to strings using str() and adding \n allows the data to be formatted as a readable list of lines in the destination file.


**15. Develop a script that reads a file and uses the errors="ignore" parameter. When is this parameter useful?**

```python

with open("corrupted_data.txt", "r", encoding="utf-8", errors="ignore") as f:
    print(f.read())
```

The errors="ignore" parameter tells the Python interpreter to simply skip over any bytes that it cannot successfully decode into the specified encoding. This is particularly useful when dealing with "noisy" data, such as log files that might have mixed encodings or legacy files containing corrupted bytes. While it allows the script to continue running without crashing, it does result in the loss of those specific unreadable characters.


**16. Write a script that checks the newlines attribute of a file after reading it. Why might this return None initially?**

```python

with open("os_demo.txt", "r") as f:
    print("Before reading:", f.newlines)
    f.read()
    print("After reading:", f.newlines)
```

The newlines attribute is dynamic; it records the types of line endings (like \r\n for Windows or \n for Linux) that the interpreter actually "sees" while scanning the file. Initially, it returns None because Python has not yet interacted with the content to determine the formatting. Once a read operation occurs, the attribute is populated with the detected newline style, which is helpful for scripts that need to maintain cross-platform formatting consistency.


**17. Create a script that creates a backup of original.txt by reading and writing 4096 bytes at a time (chunking).**

```python

with open("original.txt", "rb") as src, open("backup.txt", "wb") as dest:
    while True:
        chunk = src.read(4096)
        if not chunk:
            break
        dest.write(chunk)
```

Chunking is the process of reading a fixed-size block of data (in this case, 4096 bytes) rather than the whole file. By using a while loop that checks if not chunk, the script knows when it has reached the end of the file (EOF). This technique is essential for system stability when copying massive files (like movies or databases), as it prevents the script from consuming an excessive amount of system memory.


**18. Write a script that tries to write to a file opened in 'r' mode and catches the resulting exception.**

```python

try:
    with open("readonly.txt", "r") as f:
        f.write("Attempting to write...")
except UnsupportedOperation:
    print("Error: You cannot write to a file opened in read-only mode.")
```

In Python, file objects enforce the permissions defined in the mode argument. Opening a file with 'r' creates a read-only stream; calling .write() on this object triggers an io.UnsupportedOperation exception. This demonstrates the "Mode attribute" logic discussed in the document, ensuring that the script cannot perform actions that violate the initial opening contract with the operating system.


**19. Demonstrate the use of flush() in a script that writes "Step 1" and "Step 2" with a 10-second pause in between. Why use flush() here?**

```python

import time
with open("progress.log", "w") as f:
    f.write("Step 1 Complete\n")
    f.flush()
    time.sleep(10)
    f.write("Step 2 Complete\n")
```

Normally, Python buffers writes to improve performance, meaning "Step 1" might not actually appear on the disk until the file is closed or the buffer fills up. By calling flush(), the script forces the data out of the RAM buffer and onto the physical disk immediately. This is critical for long-running processes or installers; if the power fails during the 10-second sleep, "Step 1" will still be saved in the file for the user to see.


**20. Write a script that moves the pointer to the 5th character using seek(5) and then reads the rest of the file.**

```python

with open("intro.txt", "r") as f:
    f.seek(5)
    remaining_text = f.read()
    print(remaining_text)
```

The seek(offset) method moves the file pointer to the absolute index provided as the argument. By moving to 5, the script skips the first 5 characters of the file. When read() is called thereafter, it begins capturing data starting from that new position until it hits the end of the file. This is a fundamental technique for "skipping headers" or reading specific records within a fixed-width data file.


## Part 2: Advanced Topics & Best Practices (10 Questions)


**21. How does the pathlib module simplify path joining compared to traditional string concatenation? Show a script example.**

```python

from pathlib import Path
folder = Path("data_files")
file_path = folder / "results.txt"  # Using the / operator
file_path.write_text("Success")
```

The pathlib module treats paths as objects rather than strings. The / operator is overloaded to join paths correctly regardless of whether the OS uses backslashes (Windows) or forward slashes (Linux/macOS). This eliminates errors caused by missing slashes in string concatenation and makes the code highly portable across different operating systems.


**22. Write a script demonstrating an "Atomic Write" using os.replace(). Why is this safer than standard writing?**

```python

import os
with open("temp.txt", "w") as f:
    f.write("Final Data")
os.replace("temp.txt", "original.txt")
```

An atomic write involves writing to a temporary file first. If the program crashes during the write, the original.txt remains safe and untouched. The os.replace() call is an atomic operation at the OS level, meaning it either succeeds completely or fails completely, ensuring that you never end up with a half-written or corrupted file.
•	Further Study: StackOverflow: Atomic File Writes in Python. [stackoverflow](https://stackoverflow.com/questions/2333872/atomic-writing-to-file-with-python)


**23. Create a script to save a dictionary using json.dump(). What are the advantages of JSON over a standard text file?**

```python

import json
user_config = {"theme": "dark", "fontsize": 14}
with open("config.json", "w") as f:
    json.dump(user_config, f, indent=4)
```

JSON (JavaScript Object Notation) allows you to save complex data structures (like lists and dictionaries) in a human-readable format that can be read by almost any programming language. Unlike standard text files, JSON preserves the "data types"—when you load it back, strings remain strings and integers remain integers, which saves the programmer from manually parsing text.
•	Further Study: [Python Docs: json module[(https://docs.python.org/3/library/json.html)


**24. Write a script to "Pickle" a Python list and read it back. Why should you avoid pickle for untrusted data?**

```python

import pickle
data = [1, 2, 3]
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)
```

pickle is a Python-specific serialization tool. While it is very powerful and can save almost any Python object, it is insecure because it can execute arbitrary code during the "unpickling" process. A malicious user could send you a "pickled" file that deletes your hard drive the moment you try to open it; therefore, never unpickle data from an unknown source.
•	Further Study: [Python Docs: pickle security](https://docs.python.org/3/library/pickle.html)


**25. Use the tempfile module to create a temporary file that deletes itself automatically. When is this useful?**

```python

import tempfile
with tempfile.NamedTemporaryFile(delete=True) as temp:
    temp.write(b"Processing...")
    print("Temp file created at:", temp.name)
# File is deleted here
```

The tempfile module is used for creating short-lived files used for intermediate calculations or processing. Because it automatically handles the creation of a unique filename and ensures the file is deleted after the with block, it prevents "cluttering" the user's hard drive with useless junk files.
•	Further Study: [Python Docs: tempfile module](https://docs.python.org/3/library/tempfile.html)


**26. Write a script to read a CSV file using the csv module's DictReader. How does this differ from f.readlines()?**

```python

import csv
with open("users.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["username"])
```

DictReader maps the information in each row to a dictionary, using the first line of the CSV as the "keys." This is much more robust than readlines() because if the order of columns in the CSV changes (e.g., "username" moves from the 1st column to the 3rd), your script will still work correctly by looking up the name instead of a position index.
•	Further Study: Real Python: [Reading and Writing CSV Files](https://realpython.com/python-csv/)


**27. Demonstrate how to compress a file into a ZIP archive using the zipfile module.**

```python

import zipfile
with zipfile.ZipFile("archive.zip", "w") as myzip:
    myzip.write("notes.txt")
```

The zipfile module allows Python to interact with compressed archives. This is a common requirement for software that needs to package multiple reports together or reduce the size of data before sending it over a network. It supports various compression methods like ZIP_DEFLATED to ensure the final file size is as small as possible.
•	Further Study: [Python Docs: zipfile module](https://docs.python.org/3/library/zipfile.html)

**28. Use the os.path.getsize() function to check the size of a file before opening it. Why is this a good practice?**

```python

import os
size = os.path.getsize("huge_video.mp4")
if size > 1024**3: # If larger than 1GB
    print("File is too large for this operation!")
```

Checking the file size before opening it is a form of "Defensive Programming." It allows the script to decide if it has enough RAM to process the file or if it should switch to a "chunking" method. This prevents the program from hanging or crashing when a user accidentally tries to open a massive file that the script wasn't designed to handle all at once.
•	Further Study: [Python Docs: os.path](https://docs.python.org/3/library/os.path.html)

**29. What is mmap (Memory Mapping), and why is it used for high-performance file access?**

```python

import mmap
with open("data.txt", "r+b") as f:
    mm = mmap.mmap(f.fileno(), 0)
    print(mm[:10]) # Read first 10 bytes like a list
    mm.close()
```

Memory mapping (mmap) creates a "virtual" view of a file that allows the programmer to treat the entire file like a huge string or list in memory. Instead of using read() and write(), you can use slicing. This is extremely fast for random access because the Operating System only loads the specific parts of the file that you are currently touching, making it the preferred method for high-performance database engines.

**30. Explain how the shutil module can be used to copy an entire directory. Provide a script example.**

```python

import shutil
shutil.copytree("my_project", "project_backup")
```

While the built-in open() methods work on individual files, the shutil (Shell Utilities) module is used for high-level operations on files and folders. copytree is particularly powerful because it recursively copies all files, subfolders, and metadata, allowing a programmer to perform complex "backup" or "deployment" tasks with a single line of code.
•	Further Study: [Python Docs: shutil module](https://docs.python.org/3/library/shutil.html)













