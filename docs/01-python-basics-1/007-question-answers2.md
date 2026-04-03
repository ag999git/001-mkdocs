## Python Programming: Exercise 

### Exercise Questions and Answers

---

#### a. What is the file extension name for python scripts?
**Answer:** The standard file extension for Python scripts is **`.py`**.

* **Further Study:** [Python Get Started - W3Schools](https://www.w3schools.com/python/python_getstarted.asp)

---

#### b. What is an Integrated Development Environment (IDE)? What are common IDEs for python?
**Answer:** An **IDE** is a software application that provides a complete set of tools for writing code. It usually includes a text editor (to write code), build automation tools, and a debugger (to find and fix errors).

**Common Python IDEs include:**
* **IDLE:** (Bundled with Python) Great for beginners.
* **VS Code:** A very popular, lightweight, and powerful editor.
* **VS Code forks** VS Code forks are  independent IDEs built on the open-source Visual Studio Code codebase. Some prominent examples are:- (a) Cursor (b) VSCodium (c) Google AntiGravity (d) Code-Server and (e) Windsurf (Codeium)
* **PyCharm:** A professional-grade IDE specifically for Python.


* **Further Study:** [What is an IDE? - Codecademy](https://www.codecademy.com/article/what-is-an-ide)

---

#### c. What is the advantage of using Interactive mode (a.k.a. shell mode)?
**Answer:** Interactive mode is very handy for running a single line of code or a small block of code to see immediate results. It is excellent for testing new ideas, checking how a function works, or doing quick calculations without needing to save a file.

* **Further Study:** [Python Interactive Mode - GeeksforGeeks](https://www.geeksforgeeks.org/python-interactive-shell/)

---

#### d. What does the `>>>` on python shell indicate?
**Answer:** The `>>>` is called the **Python Prompt**. It indicates that the Python interpreter is ready and waiting for you to type a command. Once you press Enter, Python will execute that command immediately.

* **Further Study:** [The Python Interpreter - Python Docs](https://docs.python.org/3/tutorial/interpreter.html)

---

#### e. What is script mode (a.k.a. program mode)?
**Answer:** Script mode is used when you want to write a complete program. Unlike interactive mode, you type your code into a text file (saved with a `.py` extension). This allows you to save your work, run all the code at once, and share your program with others to run on their computers.

* **Further Study:** [Script Mode vs Interactive Mode - Programiz](https://www.programiz.com/python-programming/interactive-vs-script-mode)

---

#### f. What does the comma do when placed between items to be printed?
**Answer:** When you use a comma inside a `print()` function, it does two things:
1.  It allows you to print multiple different items (like a string and a number) at the same time.
2.  It automatically adds a **single space** between each item.

**Example:** `print("Age:", 15)` will output `Age: 15`.

* **Further Study:** [Python print() Function - W3Schools](https://www.w3schools.com/python/ref_func_print.asp)

---

#### g. What are triple quoted strings in python? What are their advantage(s)?
**Answer:** Triple quoted strings are strings enclosed in three single quotes (`'''`) or three double quotes (`"""`).

**Key Advantages:**
* **Multi-line Strings:** They allow a string to span across several lines without needing special characters.
* **No Escaping:** You can include regular single quotes (`'`) or double quotes (`"`) inside them without breaking the code.
* **Docstrings:** They are the standard way to write documentation for functions and classes.

* **Further Study:** [Python Multi-line Strings - Real Python](https://realpython.com/python-strings/#triple-quoted-strings)


#### h. What are some other good naming conventions in python?

·       Avoid using names that are too general or too wordy. Strike a good balance between the two.

·       Bad: data\_structure, my\_list, info\_map, dictionary\_for\_the\_purpose\_of\_storing\_data\_representing\_word\_definitions

·       Good: user\_profile, menu\_options, word\_definitions

·       Don’t use names like “O”, “l”, or “i”

·       When using CamelCase names, capitalize all letters of an abbreviation (e.g. HTTPServer because HTTP is an abbreviation.)

  

Taken from:- [Here](https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html)

## Python Programming: 
### Exercise 2

#### a. What does the term “dynamic typing” mean?
**Answer:** In Python, you don't have to declare what type of data a variable holds (like an integer or a string) beforehand. The "type" is determined automatically at runtime based on the value you assign to it. You can even change a variable from a number to a string later in the same program.

* **Further Study:** [Dynamic Typing in Python - GeeksforGeeks](https://www.geeksforgeeks.org/dynamic-typing-in-python/)

---

#### b. What does the term “automatic memory management” mean?
**Answer:** This means the programmer doesn't have to manually allocate or free up computer memory. Python has a built-in "Garbage Collector" that automatically detects when an object is no longer being used and clears it from memory to make room for new data.

* **Further Study:** [Memory Management in Python - Real Python](https://realpython.com/python-memory-management/)

---

#### c. What is the difference between “source code” and “object code”?
**Answer:** * **Source Code:** This is the code written by the human (you) in a high-level language like Python. It is readable by people.
* **Object Code:** This is the low-level code (often called bytecode or machine code) that the computer's processor can actually understand and execute.

* **Further Study:** [Source Code vs Object Code - TechTarget](https://www.techtarget.com/searchitoperations/definition/source-code)

---

#### d. What is the difference between “open source code” and “proprietary code”?
**Answer:** * **Open Source:** The source code is free for anyone to look at, modify, and distribute (e.g., Python).
* **Proprietary:** The code is owned by an individual or a company. Users cannot see or change the inner workings; they can only use the software as provided (e.g., Microsoft Windows or Adobe Photoshop).

* **Further Study:** [Open Source vs Proprietary - Red Hat](https://www.redhat.com/en/topics/open-source/what-is-open-source)

---

#### e. What are CPython, Jython, and IronPython and how are they different?
**Answer:** Python is a set of rules (a language description). Different "implementations" are built to run these rules in different environments:
* **CPython:** The standard version written in C (the one you download from python.org).
* **Jython:** Allows Python to run on the Java platform.
* **IronPython:** Designed to work with Microsoft’s .NET framework.

* **Further Study:** [Python Implementations - Python.org](https://www.python.org/download/alternatives/)

---

#### f. Is Python a case-sensitive language?
**Answer:** **Yes.** Python treats uppercase and lowercase letters differently. For example, a variable named `Age` is completely different from a variable named `age`.

* **Further Study:** [Case Sensitivity in Python - W3Schools](https://www.w3schools.com/python/gloss_python_variable_names.asp)

---

#### g. Can mutable objects change their value but keep their id()?
**Answer:** **Yes.** "Mutable" means changeable. For example, if you have a list, you can add or remove items from it. The content changes, but the list remains the same "object" in memory, so its `id()` (the memory address) stays the same.

* **Further Study:** [Mutable vs Immutable - Programiz](https://www.programiz.com/python-programming/methods/built-in/id)

---

#### h. When we say that Jupyter Notebook is a “server-client” application, what does it mean?
**Answer:** It means the application has two parts:
1.  **The Server:** A program running on your computer (or a remote web server) that does the heavy lifting and runs your Python code.
2.  **The Client:** The web browser (like Chrome or Firefox) where you type your code and see the results.

* **Further Study:** [How Jupyter Works - Jupyter Documentation](https://jupyter.readthedocs.io/en/latest/architecture/how_jupyter_ipynb_works.html)

---

#### i. Print is a statement in Python 2.x but it is a function in Python 3.x. Explain the difference.
**Answer:** * In **Python 2**, `print` was a keyword (like `if` or `while`), so you wrote `print "Hello"`.
* In **Python 3**, `print()` is a function, meaning you **must** use parentheses: `print("Hello")`. This change makes the language more consistent and allows for extra settings, like changing how lines end.

* **Further Study:** [Python 2 print vs Python 3 print - Real Python](https://realpython.com/python-print/#python-2-vs-python-3-print)

---

#### j. What do the terms “explicit line continuation” and “implicit line continuation” mean?
**Answer:** * **Explicit:** Using a backslash (`\`) to tell Python that a single line of code continues on the next line.
* **Implicit:** Python automatically knows a line continues if you haven't closed a parenthesis `()`, bracket `[]`, or brace `{}`. This is the preferred way to write long lines.

* **Further Study:** [Python Line Continuation - GeeksforGeeks](https://www.geeksforgeeks.org/line-continuation-in-python/)

---

#### k. What is an “identifier” in Python? What are the common rules for writing identifiers?
**Answer:** An identifier is a name given to entities like variables, functions, or classes. 

**Common Rules:**
1.  Can contain letters (a-z, A-Z), digits (0-9), or underscores (`_`).
2.  Must **not** start with a digit.
3.  Cannot be a Python keyword (like `if`, `else`, or `for`).
4.  Cannot contain special symbols like `!`, `@`, `#`, or `$`.

* **Further Study:** [Python Identifiers - TutorialsPoint](https://www.tutorialspoint.com/python/python_basic_identifiers.htm)



##### l. What are the differences between interpreted and compiled language?

| Compiled | Interpreted |
| --- | --- |
| Faster performance by directly using the native code of the target machine | Slow to execute because each statement had to be interpreted into machine code every time it was executed |
| Need to run a compilation stage | No need to run a compilation stage: can execute code directly "on the fly" |
| An advantage of compiled code is that it hides the source code from the end user (which might be intellectual property) because instead of deploying the original human-readable source code, you deploy an obscure binary executable file. | Source code is difficult to hide |
| If your source code is compiled, you need to compile a different executable for each type of processor and/or platform that you want your program to run on | Interpreted languages are more portable |
| Compiled programs are already converted into an executable and so are “ready to run”. | They are not “ready to run”. Rather have to be interpreted |


  

#### j. Give point-wise Comparison between Hash (#) and triple quotes (`'''` or `"""`)

**1. Hash (#) — Single-Line Comments**

-   Starts with # and continues to the end of the line.
-   Used mainly for explaining **logic**, **steps**, or **reasoning** inside the code.
-   Helpful for programmers who want to **understand, debug, or modify** the code.
-   Typically scattered throughout functions and code blocks.
-   Can be used for multi-line comments by repeating # on each line.
-   Ignored entirely by the Python interpreter.

**2 Triple Quotes (''' or """) — Multi-Line Strings Used as Comments**

-   Written using triple single quotes ''' or triple double quotes """.
-   Technically creates a **multi-line string**, not a true comment — but becomes a "comment" only if unused.
-   Mainly used for **docstrings**: documentation for modules, classes, and functions.
-   Appears immediately after a def or class statement.
-   Describes **usage**, **purpose**, **arguments**, and **returns** — the _user interface_.
-   Tools like Sphinx, pydoc, and IDEs can automatically extract them.
-   Can also be placed on one line as a single-line docstring.

  

  

Comparison:-

| Feature / Purpose | # Single-Line Comment | ''’ / """ Multi-Line Comment (Docstring) |
| --- | --- | --- |
| Syntax | # comment | """ comment """ or ''' comment ''' |
| Type | True comment | Multi-line string used as a comment or docstring |
| Interpreter behavior | Completely ignored | Created as a string; ignored only if not assigned or used |
| Typical use | Explain logic or code steps | Document modules, classes, and functions |
| Audience | Programmers modifying/understanding code | Users who want to know how to use the code |
| Location | Anywhere in code | Usually immediately after def, class, or module top |
| Extraction by tools | Not extracted | Automatically extracted by documentation tools |
| Best for | Inline explanations and quick notes | Official documentation of API/usage |
| Multi-line use | Yes, by repeating # on each line | Naturally supports multi-line formatting |
| Single-line use | Yes | Possible by placing opening and closing quotes on the same line |
