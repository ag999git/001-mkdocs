


## Functools

`functools` is a Python standard library module that provides tools for working with functions, especially higher-order functions such as decorators. These **higher-order functions**—functions **operate on other functions** (for example modifying them, wrapping them, or combining them).

The function `functools.wraps()` is commonly used in decorators to preserve the metadata of the original function.



#### Uses of functool
It is especially useful for:

-   **Decorators**
    
-   **Function caching**
    
-   **Partial functions**
   
-   **Functional programming utilities**



#### Commonly used tools in `functools` include:

| Function | Purpose |
| --- | --- |
| wraps | Used when writing decorators to preserve metadata |
| lru_cache | Caches function results for faster repeated calls |
| partial | Fixes some arguments of a function |
| reduce | Applies a function cumulatively to items of an iterable |
| total_ordering | Simplifies writing comparison methods in classes |


#### Why `functools` is important for **decorators**

When we create a decorator, the **original function gets wrapped by another function**.

Without `functools`, some important information about the original function is **lost**, such as:

-   function name
    
-   docstring
    
-   help documentation
    

`functools.wraps()` **copies this metadata from the original function to the wrapper function**.



#### The Problem of loss of identity when using wrappers
In Python, every function is an object. Like any object, it has an ID Card (Metadata). This card contains:

`__name__`: The name of the function (e.g., "bark").

`__doc__`: The docstring (e.g., """This function makes a sound.""").

`__annotations__`: Information about type hints.

When you decorate a function, you are performing a reassignment.

```python

# What the @ decorator actually does:
bark = log_action(bark)
```


Now, the variable bark no longer points to the original "barking" code. It points to the wrapper function inside your decorator. If a debugger or a documentation tool looks at bark, it sees the wrapper's identity (Such as `__name__`, `__doc__` etc), not the original one.


#### The solution is to use an "Identity Copier"
@functools.wraps(func) acts as an "Identity copier". 
What it does is that it copies the identity of the original (Wrapped) function and gives it to the wrapper inside the decorator. It does this by deep-copying the following attributes from the original function to the wrapper:

- Name: Changes wrapper back to bark.

- Docstring: Keeps your helpful documentation alive.

- Module: Keeps track of where the function was originally defined.

 
 Showing how identity of wrapped function changes Before vs. After bapplying `@functools.wraps(func)`.







#### Example 1

##### Case A: Without `@functools.wraps` (The Identity is Lost)

```python

# NO import functools used here!

# --- THE DECORATOR ---
def my_decorator(func):
    # NOTICE: The 'Identity Copier' is missing!
    def wrapper(*args, **kwargs):
        print("--- Start of Wrapper ---")
        result = func(*args, **kwargs)
        print("--- End of Wrapper ---")
        return result
    return wrapper

# --- THE FUNCTION ---
@my_decorator  
def bark():
    """Make Sound"""
    print("Woof!")

# --- THE TEST ---
# This is where you will see the problem:
print(f"1. Function Name: {bark.__name__}") 
# EXPECTED: bark | ACTUAL: wrapper

print(f"2. Function Doc:  {bark.__doc__}")  
# EXPECTED: Make Sound | ACTUAL: None

```


#### Case : With `@functools.wraps` (The Identity is Retained)


```python

import functools

# --- THE DECORATOR ---
def my_decorator(func):
    # This 'copies' the ID card from bark() to the wrapper
    @functools.wraps(func) 
    def wrapper(*args, **kwargs):
        print("--- Start of Wrapper ---")
        result = func(*args, **kwargs)
        print("--- End of Wrapper ---")
        return result
    return wrapper

# --- THE FUNCTION ---
@my_decorator
def bark():  # This is the function we are decorating
    """Make Sound"""  # This is the docstring (the 'manual')
    print("Woof!")

# --- THE TEST ---
print(f"1. Function Name: {bark.__name__}")  # EXPECTED: bark | ACTUAL: bark (because of functools.wraps())
print(f"2. Function Doc:  {bark.__doc__}")  # EXPECTED: Make Sound | ACTUAL: Make Sound (because of functools.wraps())

print("-" * 20)
bark()  # This will show the wrapper's print statements, but the function name and docstring will be correct due to functools.wraps()

```

#### Table showing the identity attributes of the "wrapped" function without using and with using functools.wraps

| Feature Tested | Before: Without functools.wraps | After: With functools.wraps |
| --- | --- | --- |
| bark.__name__ | "wrapper" (The generic mask) | "bark" (The correct name) |
| bark.__doc__ | None (The docstring is lost) | "Make Sound" (The docstring is preserved) |
| Debug Tracebacks | Show errors in wrapper. | Show errors in bark. |
| help(bark) | Shows info for the wrapper. | Shows info for the bark function. |


#### Diagram shows situation without and with using functools


![Diagram shows situation without and with using functools](/resources/ch-6-using-functools.png)


#### Example 2

##### Case A: Manual way to do exactly what functools.wraps does automatically.

Before functools.wraps existed, programmers had to manually "fix" the identity of the function. 
To do this, you manually overwrite the wrapper attributes with the values from the original func.



```python

def food_safety_check(func):
    def wrapper(food_type):
        prohibited_foods = ["Chocolate", "Cakes", "Ice Cream", "Onions"]
        if food_type in prohibited_foods:
            print(f"ALERT: {food_type} is dangerous for pets! Action blocked.")
        else:
            print(f"{food_type} is safe.")
            return func(food_type)

    # --- MANUAL IDENTITY COPIER ---
    # Instead of @functools.wraps(func), we do this:
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    wrapper.__module__ = func.__module__
    
    return wrapper

@food_safety_check
def feed_pet(food):
    """Feeds the pet the specified food item."""
    print(f"Eating the {food} now. Yum!")

# --- TEST ---
print(f"Function Name: {feed_pet.__name__}") # Shows 'feed_pet'
print(f"Function Doc:  {feed_pet.__doc__}")  # Shows the 'Feeds the pet...' string

```


##### Case B: Using functools

```python

import functools

def food_safety_check(func):
    @functools.wraps(func)
    def wrapper(food_type):
        prohibited_foods = ["Chocolate", "Cakes", "Ice Cream", "Onions"]
        if food_type in prohibited_foods:
            print(f"ALERT: {food_type} is dangerous for pets! Action blocked.")
        else:
            print(f"{food_type} is safe.")
            return func(food_type) # Run the original function
    return wrapper

@food_safety_check
def feed_pet(food):  # This is the function we are decorating
    print(f"Eating the {food} now. Yum!")

# Usage
feed_pet("Carrot")    # Allowed
feed_pet("Chocolate") # Blocked by decorator


```








