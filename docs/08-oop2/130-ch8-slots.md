


# PROJECT TASK — `__slots__` (Memory Optimization)



## “Optimizing Pet Objects Using `__slots__` in Python”

----------

## OBJECTIVE 

By completing this you will:

-   Understand **why `__dict__` consumes memory**
-   Learn how `__slots__` **removes `__dict__`**
-   Compare behavior of:
    -   Normal class
    -   Class with `__slots__`
-   Understand **limitations and trade-offs**

----------

## TASK DESCRIPTION. You are required to:

### STEP 1: Create a normal class

-   Create class `PetNormal`
-   Add:
    -   `name`
    -   `age`
-   Store them using `self.name`, `self.age`

----------

### STEP 2: Create a class using `__slots__`

-   Create class `PetSlots`
-   Define:

`__slots__  = ['name', 'age']`

-   Use same attributes as above

----------

### STEP 3: Create objects

-   Create:
    -   `p1 = PetNormal("Tommy", 5)`
    -   `p2 = PetSlots("Bruno", 3)`

----------

### STEP 4: Compare namespaces

-   Print: `print(p1.__dict__)`

-   Try: `print(p2.__dict__)`

Observe and explain difference

----------

### STEP 5: Add new attribute dynamically

-   Try:

`p1.color =  "Brown"  `
`p2.color =  "Black"`

Observe:

-   Which works?
-   Which fails?

----------

### STEP 6: Memory comparison (conceptual)

-   Use:


```python
import  sys  
print(sys.getsizeof(p1))  
print(sys.getsizeof(p2))
```
Compare sizes (even if small difference)



### STEP 7: Write explanation

Student must explain:

-   What is `__dict__`
-   What `__slots__` does
-   Why dynamic attributes fail
-   When to use `__slots__`

----------

### 8. DOs and DON’Ts

#### DO:

-   Use same attributes in both classes
-   Print outputs clearly
-   Add comments explaining behavior

#### DON’T:

-   Don’t use different attribute names
-   Don’t skip error handling
-   Don’t assume `__slots__` improves speed (focus on memory)

----------

### 9. HINTS (Very Important)

-   `__slots__` → **removes instance `__dict__`**
-   Without `__dict__` → no dynamic attributes
-   Think:  Fixed structure vs flexible structure”

----------

### Expected Observations

  

| Feature | `PetNormal` | `PetSlots` |
| --- | --- | --- |
| Has `__dict__` | Yes | No |
| Dynamic attributes | Allowed | Not allowed |
| Memory usage | Higher | Lower |
| Flexibility | High | Low |


### Script


```python


# STEP 1: NORMAL CLASS

class PetNormal:  # Normal class without __slots__
    def __init__(self, name, age):
        self.name = name
        self.age = age

# STEP 2: CLASS WITH __slots__

class PetSlots:  # Class with __slots__
    __slots__ = ['name', 'age']  # __slots__ restricts attributes to only 'name' and 'age'. 
    # This means that instances of PetSlots can only have these two attributes, and they will 
    # not have a __dict__ to store attributes dynamically.

    def __init__(self, name, age):  # The __init__ method initializes the name and age attributes for instances of PetSlots.
        self.name = name
        self.age = age

# STEP 3: OBJECT CREATION

p1 = PetNormal("Tommy", 5)  # This line creates an instance of the PetNormal class with the name "Tommy" and age 5. Since PetNormal does not use __slots__, it has a __dict__ that can store attributes dynamically.
p2 = PetSlots("Bruno", 3)


# STEP 4: NAMESPACE COMPARISON

print("PetNormal __dict__:", p1.__dict__)  
# Output: PetNormal __dict__: {'name': 'Tommy', 'age': 5}. 
# This line prints the __dict__ of p1 instance, which shows the attributes and their values in a dictionary 
# format. Since PetNormal does not use __slots__, it has a __dict__ that can store attributes dynamically.

try:  # This block attempts to access the __dict__ attribute of the p2 instance, which is an instance of 
    # PetSlots. Since PetSlots uses __slots__, it does not have a __dict__ attribute, and trying to access 
    # it will raise an AttributeError. The except block catches this error and prints a message indicating 
    # that PetSlots has no __dict__.
    print("PetSlots __dict__:", p2.__dict__)
except AttributeError as e:
    print("PetSlots has no __dict__:", e)  # error message in e indicates 'PetSlots' object has no attribute '__dict__'. 


# STEP 5: DYNAMIC ATTRIBUTE ADDITION

# This Works because PetNormal allows dynamic attributes due to the presence of __dict__. When we add a new attribute 'color' to the p1 instance, it is stored in the __dict__ and can be accessed without any issues.
p1.color = "Brown"
print("PetNormal new attribute:", p1.color)

# This Fails because PetSlots does not allow dynamic attributes due to the use of __slots__. When we try to add a new attribute 'color' to the p2 instance, it raises an AttributeError. The except block catches this error and prints a message indicating that we cannot add new attributes to PetSlots.
try:
    p2.color = "Black"
except AttributeError as e:
    print("Cannot add new attribute to PetSlots:", e)

# STEP 6: MEMORY COMPARISON. Using __slots__ can save memory by preventing the creation of a __dict__ for each instance, which can be beneficial when creating many instances of a class. The sys.getsizeof() function is used to compare the memory usage of instances of PetNormal and PetSlots. We expect that the instance of PetSlots will use less memory than the instance of PetNormal due to the absence of a __dict__.

from shutil import which
from shutil import which
import sys

print("Memory (PetNormal):", sys.getsizeof(p1)) 
# Output: Memory (PetNormal): 48. 
# This line prints the memory size of the p1 instance, which is an instance of PetNormal. 
# The memory size includes the __dict__ that allows for dynamic attributes, which contributes 
# to a larger memory footprint.

print("Memory (PetSlots):", sys.getsizeof(p2))  
# Output: Memory (PetSlots): 48. 
# This line prints the memory size of the p2 instance, which is an instance of PetSlots. 
# The memory size may be smaller than that of PetNormal due to the use of __slots__, which prevents 
# the creation of a __dict__ and thus reduces memory usage. However, the actual memory size can 
# vary based on the implementation and may not always be smaller than PetNormal, but it 
# generally allows for more efficient memory usage when creating many instances.


```













