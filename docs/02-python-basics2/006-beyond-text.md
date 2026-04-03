
## Beyond text book ##
### 1.  Study `pip` (short for "Pip Installs Packages") which is the standard package manager for Python


#### 1\. What is `pip`?

`pip` (Pip Installs Packages) is the tool that lets you download and install libraries that other people have written (like `pandas` for data or `flask` for websites).

> **Analogy:** If Python is the smartphone, `pip` is the **App Store**. It's how you get new features that didn't come with the phone.

* * *

#### 2\. Common Commands (The Basics)

| Goal | Command |
| --- | --- |
| Install a package | `pip install <package_name>` |
| Upgrade a package | `pip install --upgrade <package_name>` |
| Uninstall a package | `pip uninstall <package_name>` |
| List everything installed | `pip list` |
| Save your list for others | `pip freeze > requirements.txt` |
| Install everything on a list | `pip install -r requirements.txt` |

* * *

#### 3\. Common Errors & How to Fix Them

*   **`pip` is not recognized as an internal or external command"**
    
    *   **Cause:** Python wasn't added to your system's "`PATH`" during installation.
        
    *   **Fix:** Use `python -m pip install ...` instead, or reinstall Python and check the box that says **"Add Python to PATH."**
        
*   **"Permission Denied" (or EACCES errors)**
    
    *   **Cause:** You are trying to install a package into a folder that only "Admins" can touch.
        
    *   **Fix:** Use `pip install --user <package_name>` to install it just for you, or better yet, use a **Virtual Environment**.
        
*   **"WARNING: You are using pip version X; however, version Y is available."**
    
    *   **Fix:** This is just a friendly reminder. Run `python -m pip install --upgrade pip` to update the tool itself.
        

* * *

#### 4\. Dos and Don'ts 

 **DOs:**

*   **Use Virtual Environments (`venv`):** Think of these as "project rooms." Installing everything globally is like throwing all your clothes in one giant pile; `venv` gives you a separate closet for every project.
    
*   **Check the spelling:** `pip install request` (singular) is different from `pip install requests` (plural).
    

**DON'T:**

*   **Don't use `sudo pip`:** If you are on Mac/Linux, never use `sudo`. It can break your operating system's built-in Python.
    
*   **Don't ignore `requirements.txt`:** If you are sharing code with a friend, always include this file so they can install exactly what you used.
    

* * *

### 2. The Modern Alternative: `uv`. 

### Introduction to `uv`


**`uv`** is an extremely fast Python package and project manager written in Rust. In 2026, it has become the professional standard because it replaces multiple tools (`pip`, `venv`, `pyenv`, and `pipx`) with one single, blazing-fast binary.

#### Why is everyone switching to `uv`?

## 

*   **Speed:** It is **10–100x faster** than `pip`.
    
*   **Zero-Config Virtual Envs:** It manages environments for you automatically.
    
*   **Disk Space:** It uses a **Global Cache**. If you have 5 projects using `pandas`, `uv` only stores it once on your hard drive, whereas `pip` would save 5 separate copies.
    

* * *

#### 1\. Common Commands


##   

  

  

| Command | What it does |
| --- | --- |
| `uv init` | Creates a new Python project folder with a pyproject.toml. |
| `uv add <package>` | Installs a package AND adds it to your project file automatically. |
| `uv remove <package>` | Uninstalls a package and cleans up your project file. |
| `uv run <script.py>` | Runs your code in the correct virtual environment (no need to "activate" anything!). |
| `uv python install 3.12` | Downloads and installs a specific version of Python itself. |
| `uv pip install -r req.txt` | A "compatibility mode" that works exactly like the old pip command. |

* * *

#### 2\. Common Errors & Fixes

## 

*   **"Failed to build ... missing header: Python.h"**
    
    *   **Cause:** You are trying to install a package that needs to be "compiled" but your computer lacks building tools.
        
    *   **Fix:** On Windows, install _Visual Studio Build Tools_. On Ubuntu/Linux, run `sudo apt install build-essential`.
        
*   **"No interpreter found"**
    
    *   **Cause:** `uv` can't find Python on your system.
        
    *   **Fix:** Run `uv python install` to let `uv` download a fresh version for you.
        
*   **"Relative imports outside of package"**
    
    *   **Cause:** Usually happens when running `uv run` on a file in a sub-folder.
        
    *   **Fix:** Always run commands from the **root folder** of your project (where `pyproject.toml` is).
        

* * *

#### 3\. Dos and Don'ts

## 

 **DO:**

*   **Use `uv run`:** Stop worrying about `source .venv/bin/activate`. Just type `uv run python script.py` and it will use the right environment every time.
    
*   **Commit `uv.lock`:** If you use Git, always upload the `uv.lock` file. This ensures your teammates have the _exact_ same versions as you.
    
*   **Use `uvx` for tools:** Want to use a tool like `ruff` or `black` without installing it into your project? Use `uvx ruff check .`. It runs the tool in a temporary "cloud" environment.
    

**DON'T:**

*   **Don't mix `pip` and `uv`:** Once you start a project with `uv`, avoid using `pip install`. It can confuse the `uv.lock` file.
    
*   **Don't manually edit `pyproject.toml` dependencies:** Use `uv add` instead. It checks for version compatibility so you don't break your code.
    

* * *

#### 4\. Comparison Table: `pip` vs `uv`


##   

  

  

| Feature | pip | uv |
| --- | --- | --- |
| Language | Python | Rust (Much faster) |
| Env Management | Manual (python -m venv) | Automatic |
| Python Versions | Requires manual install | Installs Python for you |
| Lockfiles | No (Needs pip-tools) | Yes (uv.lock built-in) |



### What is requirements.txt

  

#### Understanding `requirements.txt`

A `requirements.txt` file is a simple text file that lists all the external libraries (packages) your project needs to run.

> **Analogy:** If your Python project is a **recipe**, the `requirements.txt` is the **shopping list**. It ensures that anyone else trying to cook your dish buys the exact same ingredients and brands you used.


#### Common commands used (In tabular form)   

| Goal | Command |
| --- | --- |
| Create the list | pip freeze > requirements.txt |
| Install from the list | pip install -r requirements.txt |
| Check what is missing | pip check |


##   
_Note: The `>` symbol in the first command tells the computer: "Take the output of `pip freeze` and save it into this file."_


##   

  

#### 2\. Common Usage & Syntax

In your `requirements.txt`, you will see lines like these:

*   `requests==2.31.0` (Use **exactly** this version)
    
*   `numpy>=1.26.0` (Use this version **or anything newer**)
    
*   `pandas` (Use **any** version available)
    

**Best Practice:** Using `==` (version pinning) is the safest way to ensure their code doesn't break when a library updates six months later.

* * *

#### 3\. Common Errors & Fixes

*   **"Could not find a version that satisfies the requirement"**
    
    *   **Cause:** You likely have a typo in the package name or the version number doesn't exist.
        
    *   **Fix:** Check the spelling on [PyPI.org](https://pypi.org).
        
*   **"File not found: requirements.txt"**
    
    *   **Cause:** You are running the command in the wrong folder.
        
    *   **Fix:** Use the `ls` (Mac/Linux) or `dir` (Windows) command to make sure you are in the same directory as the file.
        
*   **The "Dirty" Freeze:**
    
    *   **Cause:** Running `pip freeze` in your global environment instead of a Virtual Environment. This adds 50+ unrelated packages to your list.
        
    *   **Fix:** Always use a **Virtual Environment** (venv) so your list only contains what your specific project needs.
        

* * *

#### 4\. Dos and Don’ts

**DOs:**

*   **Keep it at the root:** Always place `requirements.txt` in the top-level folder of your project.
    
*   **Include it in Git:** Always `git add requirements.txt` so your teammates can use it.
    
*   **Use it for Deployment:** If you host your code on GitHub or Heroku, they look for this file to know how to set up your app.
    

**DON'Ts:**

*   **Don't name it something else:** While you _can_ name it `libs.txt`, everyone expects `requirements.txt`. Stick to the standard!
    
*   **Don't put Python itself in there:** This file is only for _packages_. You specify the Python version separately (usually in a `runtime.txt` or `pyproject.toml`).
    

* * *

#### 5\. Modern Alternatives (The "New Standards")

While `requirements.txt` is the classic way, the industry is moving toward more robust systems:

1.  **`pyproject.toml` (The Official Successor):** This is now the recommended way to define project metadata and dependencies in one file.
    
2.  **`uv.lock` (The Fast Alternative): If you use **`uv`**, it creates a `uv.lock` file. This is better than `requirements.txt` because it records the _exact_ environment state, making it impossible for "version drift" to happen.
    
3.  **`Pipfile`:** Used by the tool `pipenv`, though it is losing popularity to `uv`.
    

* * *

#### Summary

*   **`pip freeze > requirements.txt`** = "Save my list"
    
*   **`pip install -r requirements.txt`** = "Load the list"







