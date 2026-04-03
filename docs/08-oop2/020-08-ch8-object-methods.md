







##**Problem Statement**

#### 1. Write code to list all attributes and methods available in the object class using an appropriate built-in function.

#### 2. Create an object of class **`Pet`**. Write a statement to check whether: The Pet class uses the same **`__str__`** method as provided by the object class.



#### The script which implements the above exercise does the following:

1.  It uses a built-in function to retrieve a complete list of all attributes and methods provided by the object class. Print this list in a numbered format (e.g., 01. `__init__`, 02. `__str__`, etc.) to see the "default features" every Python object starts with.
2.  It defines a simple, empty class named `Pet` using the pass statement.
3.  Then, it creates an instance of `Pet`.
4.  It then performs an identity check (using the is operator) to prove that Pet is using the exact same `__str__` method defined in the object class, even though you never explicitly wrote one.

```python

# 1. List all methods inherited from the object class
print("\n--- Methods provided by the 'object' class ---")
methods = dir(object)
for i, method in enumerate(methods, 1):
    print(f"{i}. {method}", end = '')  # i is index, method is method name
    # end='' keeps it on the same line.
    # Output: 1. __class__ 2. __delattr__ 3. __dir__ 4. __doc__ 5. __eq__ 6. __format__ 7. __ge__ 8. __getattribute__ 9. __gt__ 10. __hash__ 11. __init__ 12. __init_subclass__ 13. __le__ 14. __lt__ 15. __ne__ 16. __new__ 17. __reduce__ 18. __reduce_ex__ 19. __repr__ 20. __setattr__ 21. __sizeof__ 22. __str__ 23. __subclasshook__

# 2. Demonstration of Inheritance
class Pet:  # This is a simple class definition for a Pet. It doesn't have any attributes or methods defined, but it will still inherit from the base 'object' class.
    pass

p = Pet()  # Create an instance of the Pet class. This will allow us to check if it inherits methods from the object class.
print(f"Does Pet inherit __str__ from object? {Pet.__str__ is object.__str__}")  
# This checks if the __str__ method of Pet is the same as that of object, confirming inheritance.
# Output: Does Pet inherit __str__ from object? True


```













