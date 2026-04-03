


## Part 1: Study Topic. The Anatomy of Data Flow: Investigating Standard Streams in Python.

**Research Question:**

> "In the context of modern Operating Systems (Windows/Linux) and Python 3.x, investigate the architecture of the three 'Standard Streams' (stdin, stdout, stderr). Your research must explain:
> 
> 1.  What are File Descriptors and how do they relate to these streams?
>     
> 2.  Why does the Operating System separate 'Regular Output' from 'Error Output'?
>     
> 3.  How can a user 'redirect' or 'pipe' these streams using the command line without modifying the Python source code?
>     
> 4.  How can a Python developer programmatically force a message to a specific stream using the `sys` module?"
>     

----------

## Part 2: Answer (Resource Guide)

### 1. The Three Pillars of I/O

Standard streams are pre-connected input and output communication channels between a computer program and its environment.

  

| Stream | File Descriptor | Python Object | Purpose | Default Device |
| --- | --- | --- | --- | --- |
| stdin | 0 | sys.stdin | Accepting input data | Keyboard |
| stdout | 1 | sys.stdout | Displaying program results | Screen (Console) |
| stderr | 2 | sys.stderr | Displaying diagnostic/error messages | Screen (Console) |


### 2. Why separate STDOUT and STDERR?

It allows for **Clean Data Processing**.

-   Imagine a script that calculates thousands of bank balances and saves them to a file.
    
-   If an error occurs on the 500th calculation, you don't want the error message ("Division by Zero!") to be written into the middle of your financial data file.
    
-   By keeping them separate, the data stays clean in the file, and the error appears on the screen for the developer to see.
    

### 3. Redirection Mechanics (The "Pipes")

The symbols in the Terminal/Command Prompt are:

-   `>` : Redirects **stdout** to a file (overwrites).
    
-   `>>` : Appends **stdout** to a file.
    
-   `2>` : Redirects **stderr** only.
    
-   `2>&1` : Merges **stderr** into **stdout**.
    
-   `<` : Feeds a file into **stdin**.
    

----------

## Part 3: Coding Task

**The Challenge:**

> "Write a Python script named `stream_demo.py`. The script should:
> 
> 1.  Use `sys.stdin` to read a user's name.
>     
> 2.  Use a standard `print()` to greet the user.
>     
> 3.  Use `sys.stderr` to print a 'Warning' message if the name is shorter than 3 characters.
>     
> 4.  Demonstrate how to run this script from the command line so that the greeting goes to `output.txt` and the warning goes to `logs.txt`."
>     

----------

## Part 4: Solution (Python Script)

>Copy and save the script below into a file location (Eg stream_demo.py)


```python

import sys

def main():
    # 1. Handling STDIN (Standard Input)
    # We use sys.stdin.readline() as an alternative to input()
    # Prompt user for input (this will appear in the console)
    # file parameter allows us to specify the stream (stdout in this case)
    print("Please enter your name: ", file=sys.stdout, end="")  
    
    # Flush the output to ensure the prompt appears before we wait for input
    # If we don't flush, the prompt might not appear before input is expected in some environments
    sys.stdout.flush() 
    
    # Read user input and remove any trailing newline
    name = sys.stdin.readline().strip()  

    # 2. Logic Check
    if len(name) < 3:
        # 3. Handling STDERR (Standard Error)
        # We send this specifically to the error stream
        # This is useful for logging warnings or errors separately from normal output
        # file parameter allows us to specify the stream (stderr in this case)
        print(f"DEBUG-WARNING: Name '{name}' is very short!", file=sys.stderr)
    
    # 4. Handling STDOUT (Standard Output)
    # This is the 'successful' result of our program because we got a valid name > 3 characters
    if name:
        # Greet the user with their name
        print(f"Hello, {name}! Welcome to the Python Streams Tutorial.")
    else:
        # If no name was provided, we treat it as an error and write to stderr
        print("ERROR: No name provided.", file=sys.stderr)  

if __name__ == "__main__":  # This ensures that main() is called only when this script is run directly, not when imported as a module
    main()


```


### Important: How to run this script


**Assuming (1) Your script is in file named `stream_demo.py` (2) The file for stdout is `output.txt` (3) The file for stderr is `logs.txt`**

#### Run this in your terminal

`python "stream_demo.py" > output.txt 2> logs.txt`

#### Case 1: You generate an error using a name of less than 3 characters (Example: You type 'Ab')

**Sample output in logs.txt if you type "Ab"**

`DEBUG-WARNING: Name 'Ab' is very short!`

#### Case 2: You give a name of 3 or more characters (Example "Anurag") then output.txt will have the message but logs.txt will not have any text.

**Sample output in output.txt if you type "Anurag"**

`Please enter your name: Hello, anurag! Welcome to the Python Streams Tutorial.`












