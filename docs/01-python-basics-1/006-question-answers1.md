## Chapter 1 Question and Answers
### Table of Contents
- [What does a Compiler do? Give its characteristics and some examples of compiled languages](#what-does-a-compiler-do-give-its-characteristics-and-some-examples-of-compiled-languages)
- [What are the Advantages of Using a Compiler?](#what-are-the-advantages-of-using-a-compiler)
- [What is an Interpreter? Give its characteristics and example of programming languages which use interpreter.](#what-is-an-interpreter-give-its-characteristics-and-example-of-programming-languages-which-use-interpreter)
- [Give differences between Compiler and Interpreter](#give-differences-between-compiler-and-interpreter)
- [Compare Python vs C++ / Java](#compare-python-vs-c--java)
- [What are Python's Key Disadvantages (as a programming language)](#what-are-pythons-key-disadvantages-as-a-programming-language)
- [Explain Open Source vs Proprietary Software (Simple Explanation)](#explain-open-source-vs-proprietary-software-simple-explanation)
- [What is Proprietary (Closed Source) Software?](#explain-open-source-vs-proprietary-software-simple-explanation)
- [What is Open Source Software?](#what-is-open-source-software)
- [What is Shareware?](#what-is-shareware)
- [What is Portability in Programming (Python and Other Languages)?](#what-is-portability-in-programming-python-and-other-languages)
- [Is Python considered portable?](#is-python-considered-portable)
- [When Python Is Not Automatically Portable?](#when-python-is-not-automatically-portable)
- [How Python Developers Improve Portability?](#how-python-developers-improve-portability)
- [Discuss portability in Other commonly used programming languages](#discuss-portability-in-other-commonly-used-programming-languages)
- [Give summary of why Python is considered portable](#give-summary-of-why-python-is-considered-portable)
- [What is Dynamic Typing (Dynamic Binding) in Python?](#what-is-dynamic-typing-dynamic-binding-in-python)
- [Why is it called “Dynamic Binding”?](#why-is-it-called-dynamic-binding)
- [Give Key points about dynamic typing in Python](#give-key-points-about-dynamic-typing-in-python)
- [Compare: Static Typing vs Dynamic Typing (In tabular format)](#compare-static-typing-vs-dynamic-typing-in-tabular-format)
- [Give simple definition of dynamic typing in Python](#give-simple-definition-of-dynamic-typing-in-python)
- [What is Automatic Memory Management in Python?](#what-is-automatic-memory-management-in-python)
- [What is the Command Line Mode (Interactive Mode)?](#what-is-the-command-line-mode-interactive-mode)
- [What is the Script Mode (Program/File Mode)? Give example](#what-is-the-script-mode-programfile-mode-give-example)
- [Give difference between Command Line Mode versus Script Mode in Python](#give-difference-between-command-line-mode-versus-script-mode-in-python)
- [Give differences between Command Line Mode and Script Mode (In tabular format)](#give-differences-between-command-line-mode-and-script-mode-in-tabular-format)
- [Explain the execution of Python from a File (Script Mode) instead of the Command Line](#explain-the-execution-of-python-from-a-file-script-mode-instead-of-the-command-line)
- [What are the steps to create and run a Python script?](#what-are-the-steps-to-create-and-run-a-python-script)
- [Why run Python from a script?](#why-run-python-from-a-script)
- [What is Python Indentation?](#what-is-python-indentation)
- [What are the differences between Keywords and Identifiers in Python?](#what-are-the-differences-between-keywords-and-identifiers-in-python)
- [What are the Common Mistakes Beginners Make with Identifiers in Python?](#what-are-the-common-mistakes-beginners-make-with-identifiers-in-python)
- [Essential Python Profiling Tools (Beginner + Intermediate Friendly)](#essential-python-profiling-tools-beginner--intermediate-friendly)
- [Give summary of common profiling tools for Python in form of a Table](#give-summary-of-common-profiling-tools-for-python-in-form-of-a-table)




### What does a Compiler do? Give its characteristics and some examples of compiled languages
[Go back to Table of Contents](#table-of-contents)

A compiler converts the entire source code into machine code *before* running the program.

####  Characteristics
- Translates whole code at once  
- Produces an executable file  
- Fast execution  
- Errors caught before running  
- Needs recompilation when code changes  

#### Examples
- **C++** → compiled to machine code  
- **Java** → compiled to bytecode first, then executed by JVM  


### What are the Advantages of Using a Compiler?
[Go back to Table of Contents](#table-of-contents)

* **Faster Execution:** Compiled code runs faster since it's directly translated to machine code, eliminating runtime translation overhead.
* **Optimized Code:** Compilers perform complex analyses and optimizations, resulting in more efficient machine code that uses fewer resources.
* **Early Error Detection:** All syntax and certain semantic errors are detected during the **compilation phase**, preventing runtime failures caused by basic errors.
* **Portability:** Source code can be compiled for different target platforms (OS/Architecture) using different compilers, allowing for wide distribution without major code changes.
* **Security:** Compiled executables hide the original source code, offering a layer of protection for intellectual property.
* **Debugging Tools:** Compilers provide robust error messages and strong support for integrated debugging tools.
* **No Runtime Dependency:** Compiled programs run independently without requiring the compiler (or a dedicated interpreter environment) to be present on the end-user's machine.
* **Abstraction:** Allows programmers to write high-level code, abstracting away the low-level details of the underlying hardware.




### What is an Interpreter? Give its characteristics and example of programming languages which use interpreter.
[Go back to Table of Contents](#table-of-contents)
An interpreter executes the code **line-by-line**, converting it to machine actions during runtime.

#### Characteristics
- No executable file  
- Slower execution (translation happens at runtime)  
- Errors appear during execution  
- Quick to test and modify  

#### Examples
- **Python**  
- **JavaScript**  




### Give differences between Compiler and Interpreter
[Go back to Table of Contents](#table-of-contents)

| Feature |  Compiler |  Interpreter |
| :--- | :--- | :--- |
| **Translation** | Translates the **entire source code** into machine code before running. | Translates and executes the code **line by line** (on the fly). |
| **Output** | Generates an intermediate **executable file** (e.g., `.exe`). | No intermediate machine code file is generated. |
| **Execution Speed** | **Faster** execution because the translation is already complete. | **Slower** execution because translation happens during runtime. |
| **Error Reporting** | Reports **all errors at once** after the entire compilation process. | Stops the program and reports the error **at the specific line** where it occurs. |
| **Build Time** | **Slower** to start (initial compilation time is required). | **Faster** to start (no separate compilation step needed). |
| **Development Cycle** | Requires a **rebuild/recompile** after every change to the source code. | Easier for rapid development and testing since there's **no rebuilding required**. |
| **Examples** | C, C++, (Java uses a mix). | Python, JavaScript, Ruby. |

---

### Compare Python vs C++ / Java
[Go back to Table of Contents](#table-of-contents)

| Feature            | Python (Interpreter)            | C++ / Java (Compiler-based)         |
|--------------------|----------------------------------|--------------------------------------|
| Translation        | Line-by-line                     | Entire program                       |
| Output             | No executable (unless packaged)  | Executable / bytecode                |
| Execution speed    | Slower                           | Faster                               |
| Error detection    | At runtime                       | At compile-time                      |
| Ideal for          | Scripting, AI, quick development | High-performance apps, large systems |


### What is Python good for?
[Go back to Table of Contents](#table-of-contents)
- Python does **not** require a separate compilation step.
- The Python interpreter reads and executes each line directly.
- This makes Python:
  - easier for beginners
  - good for experimentation
  - useful for quick testing

---

### What are Python's Key Disadvantages (as a programming language)
[Go back to Table of Contents](#table-of-contents)

1.  **Slower Execution Speed:** As an interpreted language, Python is generally slower than compiled languages (like C++ or Java), making it less suitable for performance-critical applications.
    
2.  **Higher Memory Consumption:** Python often uses more memory (RAM) compared to other languages, which can be a limiting factor in resource-constrained or memory-intensive tasks.
    
3.  **Errors Found Late (Runtime):** Due to dynamic typing, errors are often only discovered when the program is running, requiring more extensive testing and debugging effort.
    
4.  **Multithreading Bottleneck (GIL):** The Global Interpreter Lock (GIL) prevents true parallel execution of threads for CPU-intensive tasks, limiting performance on modern multi-core processors.
    
5.  **Weak Platform Support:** It is not the primary choice for native mobile application development or highly demanding real-time/embedded systems due to performance and limited framework support.
    
6.  **Limited Low-Level Access:** Python's high-level nature makes it difficult to interact directly with hardware or perform deep system-level programming.
    
7.  **Deployment Security:** When compared to some other languages, its security features can sometimes raise more concerns for large-scale web deployments, necessitating robust external security measures.





### Explain Open Source vs Proprietary Software (Simple Explanation)
[Go back to Table of Contents](#table-of-contents)

Understanding the terms **open source**, **closed source**, **free**, and **paid** can be made easy with a simple analogy involving **cake**, **baking**, and **recipes**.

---

#### 1. The Cake Analogy (Simple Version)

- **Cake** = The software you can use.
- **Cake recipe** = Source code (human-readable instructions).
- **Baking the cake** = Compiling the source code into an executable program.
- **Price of the cake** = Whether the software is free or paid.

---

#### What is Proprietary (Closed Source) Software?

- You **get the cake**, but **not the recipe**.
- You can **eat** the cake (use the software), but:
  - You cannot see how it is made.
  - You cannot modify it.
  - You cannot improve it.
  - You cannot fix bugs in it.
- Even if the cake is **free of cost**, it is still **closed source** if the recipe is not given.
- Examples:
  - Microsoft Windows
  - Adobe Photoshop
  - Many commercial apps

---

#### What is Open Source Software?
[Go back to Table of Contents](#table-of-contents)

- You get the **cake** AND the **recipe**.
- The recipe (source code) may be:
  - Free
  - Paid
  - Freely editable or licensed with conditions
- With source code, anyone can:
  - Make their own version
  - Modify or improve it
  - Fix bugs
  - Contribute to the community
- Examples:
  - Linux
  - Python
  - Android (based on Linux)
  - Firefox

---

#### Understanding Compilation (Baking the Cake)

- Programmers write source code (the recipe).
- Before distribution, they **compile** it.
- Compilation converts human-readable code into:
  - Executables
  - Binary files
  - Machine code
- These cannot be easily reverse-engineered, similar to a baked cake not revealing the recipe.

---

### What is Shareware?
[Go back to Table of Contents](#table-of-contents)

- **Shareware** = Free to try, but still closed source.
- Features may be:
  - Limited-time usage  
  - Limited features  
  - Trial or demo version
- Shareware is **NOT** open source unless the source code is provided.

Examples:
- WinRAR trial versions  
- Many small commercial utilities

---

### Give Comparison Table: Open Source vs Closed Source vs Free vs Paid
[Go back to Table of Contents](#table-of-contents)

| Feature | Open Source | Closed Source | Free Software | Paid Software |
|--------|-------------|---------------|----------------|----------------|
| Source code available |  Yes |  No | Depends | Depends |
| Can modify the code |  Yes |  No | If open source | If license permits |
| Can redistribute |  Usually |  No | Depends | Usually no |
| Cost | Free or paid | Free or paid |  Free |  Paid |
| Examples | Linux, Python, Android | Windows, MS Office | VS Code, Firefox | Photoshop, MS Office |
| Who controls the software? | Community or developers | Company/vendor | Depends | Vendor |
| Can users find and fix bugs? |  Yes |  No | If source is open | Usually no |
| Requires a license? | ✔ Yes (open licenses) | ✔ Yes | Sometimes | ✔ Always |

---

#### Summary (Quick Points)

- **Open Source** = You get the recipe (source code).  
- **Closed Source** = You only get the cake.  
- **Free Software** = Costs ₹0, but may be closed source.  
- **Paid Software** = You pay money, but it may still be open source.  
- **Shareware** = Trial version but still closed source.  
- A software can be:
  - Open source + free  
  - Open source + paid  
  - Closed source + free  
  - Closed source + paid  

Examples:
- **Open + Free** → Python, Linux  
- **Open + Paid** → Red Hat Enterprise Linux  
- **Closed + Free** → Free antivirus trials  
- **Closed + Paid** → Windows, Adobe Photoshop  


### What is Portability in Programming (Python and Other Languages)?
[Go back to Table of Contents](#table-of-contents)


- **Portability** refers to how easily a program or programming language can be moved from one computer system or operating system to another **with little or no modification**.
- A highly portable language allows the same code to run on different platforms such as:
  - Windows  
  - Linux  
  - macOS  
  - Unix  
  - Mobile operating systems (Android / iOS, through specific frameworks)

In simple terms:  
**Portable code works everywhere, not just on one type of computer.**

---

### Is Python considered portable?
[Go back to Table of Contents](#table-of-contents)

Python is considered **highly portable** because:

##### 1. Python interpreter is available on almost every platform  
- The standard implementation, **CPython**, is written in **ANSI C**, a very portable systems language.  
- This allows Python to be compiled and run on almost any device where a C compiler exists.

##### 2. Python code usually requires **no changes** across platforms  
For example, this code:

```python
print("Hello")
```

Behaves the same on:
- Windows  
- macOS  
- Linux  
- Raspberry Pi  
- Cloud servers  
- Mobile devices (via special runtimes)  

##### 3. Python hides platform differences  
Most of the time, Python abstracts away OS-level differences.  
Example:  
File handling, networking, mathematical operations work consistently across systems.

##### 4. Cross-platform libraries  
Many Python libraries (NumPy, Pandas, Flask, Django) work the same on all systems.

---

### When Python Is *Not* Automatically Portable?
[Go back to Table of Contents](#table-of-contents)

Although Python *itself* is portable, sometimes scripts depend on:

- OS-specific file paths  
- Windows-only modules (e.g., `win32com`)  
- Linux-only commands (shell utilities like `grep`, `sed`, `ls`)  
- Hardware-specific dependencies (GPU, TPU, microcontrollers)  
- Installation-dependent paths or environment variables  

These reduce portability unless handled carefully.

---

### How Python Developers Improve Portability?
[Go back to Table of Contents](#table-of-contents)

Python developers improve portability by using:

##### 1. OS-independent modules
```python
import os
import pathlib
```

##### 2. Virtual environments
Ensure dependencies are portable using:
```
requirements.txt
```

##### 3. Avoid hardcoding file paths  
Use `os.path.join()` instead of `"C:\\Users\\name\\"`.

##### 4. Use cross-platform libraries  
Avoid platform-specific APIs unless necessary.

---

### Discuss portability in Other commonly used programming languages
[Go back to Table of Contents](#table-of-contents)

##### **C / C++**
- Very portable when written using standard libraries.
- But OS-specific system calls reduce portability.

##### **Java**
- Extremely portable due to the **Java Virtual Machine (JVM)**.
- “Write once, run anywhere.”

##### **JavaScript**
- Portable in browsers, but Node.js code may depend on OS-specific functions.

##### **Go**
- Highly portable due to cross-compilation (`go build` for different OS targets).

##### **Rust**
- Very portable using standard library, but unsafe or OS-specific code reduces it.

##### **C#**
- Originally Windows-only, but now portable with .NET Core / .NET 5+.

---

### Give summary of why Python is considered portable

- **Portability = How easily software runs on different systems.**
- **Python is highly portable** because:
  - CPython is written in portable ANSI C.
  - Python code rarely needs modification across OSes.
  - Cross-platform standard library and packages.
- Portability depends on avoiding OS-specific code.

### What is Dynamic Typing (Dynamic Binding) in Python?
[Go back to Table of Contents](#table-of-contents)


- **Dynamic typing** means that **you do not need to declare the type of a variable before using it**.
- In Python, **a variable’s type is decided at runtime**, based on the value assigned to it.
- The same variable can hold **different types of data at different times**.
- Python automatically tracks and updates the type internally — the programmer does not need to specify it.

---

### Give example of Dynamic Typing in Action in Python
[Go back to Table of Contents](#table-of-contents)

```python
x = 10        # x is now an integer
x = "hello"   # now x becomes a string
x = 3.14      # now x becomes a float
```

Python does not complain because it binds the variable `x` to the value **and its type** at runtime.

---

### Why is it called “Dynamic Binding”?
[Go back to Table of Contents](#table-of-contents)

- “Binding” means **linking a name (variable) to a value and its type**.
- In Python, this binding happens **dynamically** (during program execution), not in advance.
- The interpreter keeps track of:
  - the object in memory  
  - its type  
  - which variable name refers to it  

Example:

```python
x = 10     # x → integer object 10
x = "hi"   # x → string object "hi"
```

`x` gets *re-bound* dynamically each time.

---

### Give Key points about dynamic typing in Python
[Go back to Table of Contents](#table-of-contents)

- Variables **do not have fixed types**; values do.
- A variable can be reassigned to any type.
- Type checking happens at runtime, not at compile time.
- This makes Python:
  - very flexible  
  - easy for beginners  
  - faster to write  

But sometimes:
- errors appear **at runtime** instead of earlier  
- large codebases may need type hints for clarity  

---

### Compare: Static Typing vs Dynamic Typing (In tabular format)
[Go back to Table of Contents](#table-of-contents)

| Feature | Static Typing (e.g., C, Java) | Dynamic Typing (Python) |
|--------|-------------------------------|--------------------------|
| Type declared before use |  Yes |  No |
| Type checked | At compile time | At runtime |
| Variable type | Fixed | Can change |
| Example | `int x = 5;` | `x = 5` |
| Flexibility | Low | High |
| Errors caught | Early | Later |

---

### Give simple definition of dynamic typing in Python
[Go back to Table of Contents](#table-of-contents)

Dynamic typing in Python means the type of a variable is determined automatically at runtime, based on the value assigned, without requiring any type declarations.

### What is Automatic Memory Management in Python?
[Go back to Table of Contents](#table-of-contents)

It means
- Python handles memory allocation and deallocation automatically.
- Programmers do not need to manually free memory.
- When objects are no longer needed, Python reclaims the memory they occupy.

#### How Python manages memory
- When a variable is assigned a value, Python allocates memory for that object.
- Multiple variables can reference the same object.
- Python tracks how many references point to each object (reference counting).
- When an object's reference count becomes zero, it becomes eligible for garbage collection.

#### Garbage collection
- Python periodically checks for unused objects.
- These unused objects are removed from memory.
- This prevents memory leaks and helps programs use memory efficiently.

#### Example
```python
x = [1, 2, 3]   # memory allocated for the list
y = x           # both variables refer to the same list
del x           # one reference removed
del y           # reference count becomes zero; memory can be reclaimed
```

#### Summary
- Memory allocation and cleanup happen automatically.
- Python uses reference counting plus a garbage collector.
- This makes Python easier and safer for beginners and reduces manual memory errors.





### What is the Command Line Mode (Interactive Mode)?
[Go back to Table of Contents](#table-of-contents)

- You start the Python interpreter and type code **one line at a time**.
- Each line is executed immediately.
- Useful for:
  - Testing small code fragments
  - Learning Python
  - Trying mathematical expressions
  - Debugging logic quickly

#### How to enter Interactive Mode in Python? Give examples.
[Go back to Table of Contents](#table-of-contents)

```bash
python
```

##### Example session
```python
>>> x = 10
>>> x + 5
15
>>> print("Hello")
Hello
```

---



### What is the Script Mode (Program/File Mode)? Give example
[Go back to Table of Contents](#table-of-contents)

- You write a full Python program in a file with a `.py` extension.
- The entire script is run at once by the interpreter.
- Useful for:
  - Larger programs
  - Assignments and projects
  - Code that needs to be saved and reused
  - Automation scripts

#### Example
Contents of `hello.py`:
```python
print("Hello from script mode!")
```

Run it:
```bash
python hello.py
```

---

### Give difference between Command Line Mode versus Script Mode in Python
[Go back to Table of Contents](#table-of-contents)

#### Overview
- Python is an interpreted language.
- This means you can run Python code **line by line** or **as a complete script**.
- Python supports two main modes of execution:
  - **Command Line Mode (Interactive Mode / REPL)**
  - **Script Mode (File Mode)**

#### What happens in compiled languages (like C++ or Java)
- The programmer must:
  1. Write the complete program.
  2. Compile it.
  3. Run the compiled output.
- These languages **cannot** normally execute code line-by-line.
- You cannot test a single line quickly without creating a full program.



### Give differences between Command Line Mode and Script Mode (In tabular format)
[Go back to Table of Contents](#table-of-contents)

| Feature | Command Line Mode | Script Mode |
|--------|-------------------|-------------|
| Execution | Line by line | Entire file at once |
| Usage | Quick tests, learning | Full programs, reusable code |
| Saved as a file? | No | Yes (`.py` file) |
| Typical environment | Python shell / REPL | Code editor / IDE |
| Good for beginners? | Yes | Yes |
| Multiline code | Harder | Easy |

---

#### Summary
- Python supports **interactive execution** and **script execution**.
- Command Line Mode executes code immediately and is ideal for experimentation.
- Script Mode runs a complete program saved in a file and is used for real development.
- This flexibility is one of the reasons Python is easy to learn and powerful for real-world use.

### Explain the execution of Python from a File (Script Mode) instead of the Command Line

##### Difference
- In interactive mode, Python statements were executed **directly in the command line** .
- In command line mode, you usually type **one statement at a time**, and the result appears immediately.
- This mode is useful for quick testing, checking logic, and learning the language.

##### What script mode adds
- Instead of typing commands one by one, you can write **multiple lines of Python code** in a single file.
- A file that contains Python code and ends with `.py` is called a **Python script**.
- A script:
  - can contain many statements
  - can be saved permanently
  - can be reused or shared
  - can be executed any number of times

---

### What are the steps to create and run a Python script?
[Go back to Table of Contents](#table-of-contents)

##### 1. Create a new Python file  
Create a file named:
```
hello.py
```

##### 2. Add Python code to the file
```python
print("Hello from a Python script!")
```

##### 3. Run the script from the terminal / command prompt
Use:
```
python hello.py
```
(or `python3 hello.py` depending on your system)

##### 4. Output
```
Hello from a Python script!
```

---

### Why run Python from a script?
[Go back to Table of Contents](#table-of-contents)

Running Python from a `.py` file is preferred when:

- You want to **save** your code permanently.
- The program is **long, structured, or contains many functions**.
- You need **loops**, **conditional logic**, and **modules**.
- You want to **share** your program with others.
- You want to **automate tasks**, run batch jobs, or schedule repeated jobs.
- You need to integrate with files, networks, or external systems.

Interactive mode is great for experimentation, but script mode is required for real programs.

---

### Compare Python Shell (Interactive Mode) vs Script Mode (In tabular format)
[Go back to Table of Contents](#table-of-contents)

| Feature | Python Shell (Command Line) | Python Script (`.py` file) |
|---------|------------------------------|------------------------------|
| Saves code | No | Yes |
| Good for trying small lines | Yes | Not ideal |
| Suitable for full programs | No | Yes |
| Can be reused later | No | Yes |
| Good for automation | No | Yes |
| Execution style | Line-by-line | All at once |
| Best for beginners | Quick testing | Writing real programs |

---

#### Summary
- **Interactive mode** is best for learning and testing short code snippets.
- **Script mode** is essential for writing full programs you want to save and reuse.
- Both modes are important parts of learning Python, and you will use both depending on the task.


### What is Python Indentation?

#### Key Ideas
- Most programming languages (C, C++, Java) use **braces `{ }`** to define code blocks.
- **Python does not use braces.**  
  Instead, it relies on **indentation** (spaces at the start of a line) to group statements together.

#### How indentation works in Python
- A code block begins when a line is followed by an indented set of statements.  
  Examples of blocks:
  - inside an `if` statement  
  - inside a `for` or `while` loop  
  - inside a function or class  
- The block ends when Python encounters a line that is **not indented** at that level.

#### Rules about indentation
- The number of spaces used for indentation is flexible (2, 3, 4, etc.).
- However, indentation must be **consistent within the same block**.
- The widely accepted standard is:
  - **4 spaces per indentation level** (PEP 8 style guide).
- Mixing **tabs and spaces** should be avoided:
  - It can lead to errors such as `IndentationError`.
  - Some editors render tabs differently, causing misaligned code.

#### Why indentation matters
- In Python, indentation is not just formatting — it is part of the **syntax**.
- Incorrect indentation changes the meaning of the program or may cause it to fail.
- Proper indentation improves:
  - readability  
  - code structure  
  - debugging and maintenance

#### Example
```python
if x > 10:
    print("Large number")
    print("This is inside the block")
print("This is outside the block")
```

### What are the differences between Keywords and Identifiers in Python?
[Go back to Table of Contents](#table-of-contents)

| Feature | Keywords | Identifiers |
|--------|----------|-------------|
| Definition | Reserved words predefined by Python | Names given by the programmer |
| Purpose | Used to define syntax and structure of the language | Used to name variables, functions, classes, etc. |
| Can you create them? | No, fixed by Python | Yes, created by the user |
| Can they be changed or reused? | No | Yes, you can choose any valid identifier |
| Examples | `if`, `else`, `for`, `while`, `class`, `def`, `import`, `return` | `x`, `total_sum`, `Student`, `calculate_area` |
| Number of items | Limited (about 35 keywords in Python 3) | Unlimited — you can create as many as needed |
| Case sensitivity | Yes (`True` is a keyword, `true` is not) | Yes (`Value`, `value`, and `VALUE` are different identifiers) |
| Role in program | Control the flow and structure; part of the language syntax | Store data and define custom names used in the program |
| Can they start with numbers? | Not applicable | No — identifiers cannot start with digits |
| Can they contain symbols? | No | Only underscores (`_`), letters, and digits allowed |

### What are the Common Mistakes Beginners Make with Identifiers in Python?
[Go back to Table of Contents](#table-of-contents)

#### 1. Starting an identifier with a number
Incorrect:
```python
2name = "John"
```
Correct:
```python
name2 = "John"
```

#### 2. Using spaces in identifiers
Incorrect:
```python
my name = "Alice"
```
Correct:
```python
my_name = "Alice"
```

#### 3. Using special characters (other than underscore)
Incorrect:
```python
total$amount = 100
```
Correct:
```python
total_amount = 100
```

#### 4. Using Python keywords as identifiers
Incorrect:
```python
class = 10   # 'class' is a keyword
```
Correct:
```python
class_num = 10
```

#### 5. Mixing uppercase and lowercase unintentionally
Python is case-sensitive:
```python
value = 10
Value = 20     # different identifier
```

#### 6. Making identifiers too short or unclear
Incorrect:
```python
x = 100
```
Better:
```python
total_marks = 100
```

#### 7. Making identifiers too long or complicated
Incorrect:
```python
totalMarksOfAllStudentsInClassSectionA = 5000
```
Better:
```python
total_marks_section_A = 5000
```

#### 8. Using inconsistent naming style
Incorrect:
```python
studentName = "Raj"
student_age = 21   # two different naming styles
```
Better (pick one style and stick to it):
```python
student_name = "Raj"
student_age = 21
```

#### 9. Using leading underscores unnecessarily
Leading underscores have special meaning in Python (private/internal use).
Beginners should avoid this unless required.

Incorrect:
```python
__count = 5
```
Correct:
```python
count = 5
```

#### 10. Using confusing or misleading names
Incorrect:
```python
list = [1, 2, 3]  # shadows built-in type 'list'
```
Correct:
```python
numbers_list = [1, 2, 3]
```




### Advanced


### Essential Python Profiling Tools (Beginner + Intermediate Friendly)
[Go back to Table of Contents](#table-of-contents)

This list includes the most important, practical, and widely used tools for profiling and optimizing Python code.  
Unnecessary or overly advanced tools have been removed.

---

#### 1. cProfile (Built-in Profiler – Most Important)

- Comes built into Python.
- Produces function-level performance stats.
- Best **first tool** for profiling any code.

Run:
```bash
python -m cProfile your_script.py
```

Save to file:
```bash
python -m cProfile -o out.prof your_script.py
```

---

#### 2. pstats + SnakeViz (Visualization for cProfile)

- `pstats` helps analyze `.prof` files.
- **SnakeViz** provides interactive visualization.
- Makes profiling results easy to understand.

Install:
```bash
pip install snakeviz
```

Run:
```bash
snakeviz out.prof
```

---

#### 3. line_profiler (Line-by-line CPU Profiler)

- Shows **which exact line** is slow inside a function.
- Best for loops, math functions, transformations.

Install:
```bash
pip install line_profiler
```

Use inside code:
```python
@profile
def my_function():
    ...
```

Run:
```bash
kernprof -l your_script.py
python -m line_profiler your_script.py.lprof
```

---

#### 4. memory_profiler (Line-by-line Memory Profiler)
[Go back to Table of Contents](#table-of-contents)

- Monitors RAM usage per line.
- Helps detect memory leaks or inefficient memory usage.

Install:
```bash
pip install memory_profiler
```

Use:
```python
from memory_profiler import profile

@profile
def func():
    ...
```

Run:
```bash
python -m memory_profiler your_script.py
```

---

#### 5. py-spy (Low-overhead sampling profiler – Production Safe)

- Works on **running processes**.
- Extremely low overhead.
- Generates flame graphs.
- Great for debugging performance issues in production.

Install:
```bash
pip install py-spy
```

Run:
```bash
py-spy top --pid <process_id>
```

---

#### 6. Pyinstrument (Beautiful HTML Reports)

- Cleanest and most beginner-friendly profiler.
- Makes easy-to-read interactive reports.
- Great for teaching and classroom use.

Install:
```bash
pip install pyinstrument
```

Run:
```bash
pyinstrument your_script.py
```

---

#### 7. Scalene (Advanced CPU + Memory + GPU Profiler)
[Go back to Table of Contents](#table-of-contents)

- Excellent for data science and scientific computing.
- Shows:
  - Python vs Native time
  - Memory usage
  - GPU usage
  - Line-level CPU/memory stats

Install:
```bash
pip install scalene
```

Run:
```bash
scalene your_script.py
```

---

#### 8. timeit (Micro-benchmarking Small Snippets)

- Best for measuring **small pieces** of code.
- Built into Python.

Example:
```python
import timeit
print(timeit.timeit("sum(range(1000))", number=1000))
```

---

#### 9. Yappi (Thread + Async Profiler)

- Useful when profiling:
  - multithreaded apps  
  - asyncio programs  
- Supports per-thread statistics.

Install:
```bash
pip install yappi
```

---



### Give summary of common profiling tools for Python in form of a Table
[Go back to Table of Contents](#table-of-contents)

| Tool | Type | Strength | Beginner-Friendly |
|------|-------|----------|--------------------|
| **cProfile** | CPU | General profiling | Very friendly |
| **SnakeViz** | Visualization | Call graph/heatmap | Very Friendly|
| **line_profiler** | CPU (line) | Find slow lines | Friendly |
| **memory_profiler** | Memory | Memory leaks |  |
| **py-spy** | Sampling | Production debugging | Somewhat friendly |
| **Pyinstrument** | CPU | Best UI for beginners | Very friendly |
| **Scalene** | CPU + MEM + GPU | Scientific workloads | Friendly |
| **timeit** | Timing | Micro-benchmarks | Very friendly |
| **Yappi** | CPU/Concurrency | Threads and async | Somewhat friendly |

---


[Go back to Table of Contents](#table-of-contents)
