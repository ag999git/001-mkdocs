



### **Research Question**

> Investigate the difference between `__str__()` and `__repr__()` methods in Python classes.  
> When should each method be used? What happens when only one of them is defined?



In this chapter in the book, we learned how to define the string representation of an object using the `__str__()` method. However, Python provides another important method called `__repr__()`.

Although the difference between these two methods is subtle, it is very important.

### Key Differences

-   `__str__()`
    
    -   Called by the built-in function `str()` and by `print()`
        
    -   Provides a **user-friendly (informal)** string representation
        
    -   Intended for end users
        
-   `__repr__()`
    
    -   Called by the built-in function `repr()`
        
    -   Provides an **official (formal)** string representation
        
    -   Intended for developers (debugging, logging)
        

### Important Rule

If a class defines `__repr__()` but does **not** define `__str__()`, then calling `str()` (or `print()`) will automatically use the `__repr__()` method.

### **Task Instructions**

1.  Create a class `Pet` with attributes like `name` and `type`.
    
2.  Implement both `__str__()` and `__repr__()` methods.
    
3.  Observe outputs of:
    
    -   `print(object)`
        
    -   `str(object)`
        
    -   `repr(object)`
        
4.  Remove the `__str__()` method and observe the change.
    
5.  Write your conclusions.

----------

### Case 1: When both __str__() and __repr__() are defined
The following script shows the output when both`__str__()` and `__repr__()`are defined

```python

# Example demonstrating __str__() and __repr__()

class Pet:
    def __init__(self, name, animal_type):
        self.name = name  # This is an instance variable to store the name of the pet
        self.animal_type = animal_type  # This is an instance variable to store the type of animal (e.g., Dog, Cat)

    def __repr__(self):
        # Developer-friendly representation
        # This should ideally be a string that, if evaluated, would recreate the object.
        return f"Pet(name='{self.name}', animal_type='{self.animal_type}')"

    def __str__(self):
        # User-friendly representation
        # This is what gets printed when you use print() or str() on the object.
        return f"{self.name} is a {self.animal_type}"


# Creating an object
pet1 = Pet("Tommy", "Dog")  # This creates an instance of the Pet class with name "Tommy" and animal type "Dog"

# Calling different representations
print("Using print():", pet1)        # Calls __str__()
# Output: Using print(): Tommy is a Dog
print("Using str():", str(pet1))    # Calls __str__()
# Output: Using str(): Tommy is a Dog
print("Using repr():", repr(pet1))  # Calls __repr__()
# Output: Using repr(): Pet(name='Tommy', animal_type='Dog')

```

### Case : When both __str__() is not defined nut `__repr__()` is defined:
The following script shows the output when str__() is not defined nut `__repr__()` is defined:

```python

class Pet:
    def __init__(self, name, animal_type):
        self.name = name  # This is an instance variable to store the name of the pet
        self.animal_type = animal_type  # This is an instance variable to store the type of animal (e.g., Dog, Cat)

    def __repr__(self):
        # Developer-friendly representation
        # This should ideally be a string that, if evaluated, would recreate the object.
        return f"Pet(name='{self.name}', animal_type='{self.animal_type}')"


pet1 = Pet("Tommy", "Dog")

print(pet1)        # Uses __repr__()
# Output: Pet(name='Tommy', animal_type='Dog')
print(str(pet1))   # Also uses __repr__()
# Output: Pet(name='Tommy', animal_type='Dog')
print(repr(pet1))  # Uses __repr__()
# Output: Pet(name='Tommy', animal_type='Dog')

```

#### The following figure shows how str() and repr() interact:

![Figure](/resources/ch-7-oop-str-vs-repr.png)








