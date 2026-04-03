



# PROJECT 2: Property Decorators (`@property`)

<details>

<summary>Understanding the three attributes `fget`, `fset` and `fdel` (Which all property objects have) (Click ► to expand)</summary>


### Before we proceed further, we need to understand `fget`, `fset` and `fdel` 
#### What is fset in `Pet.age.fset(p, 10)`?



#### Answer:

`fset` is the **setter function** associated with the property.

So:

`Pet.age.fset(p, 10)`

means:

“Call the setter function of the property `age` manually”



### Step-by-Step Understanding

#### 1. What is `Pet.age` actually?

When you write:

```python

class  Pet:  
  @property  
  def  age(self):  
  return  self._age
  ```

-    `age` is **not a normal method**
- It becomes a **property object**

So:

`print(type(Pet.age))`

Output:

`<class 'property'>`



#### 2. What does a property object contain?

A property internally stores 3 important functions:

  

  

| Attribute | Meaning |
| --- | --- |
| fget | Getter function |
| fset | Setter function |
| fdel | Deleter function |


#### 3. Your class internally becomes

**Your code:**

```python

class Pet:
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

```

**Is Internally equivalent to:**

```python

class Pet:
    def get_age(self):
        return self._age

    def set_age(self, value):
        self._age = value

    age = property(get_age, set_age)

```




#### What happens in:

`Pet.age.fset(p, 10)`

Step-by-step:

1.  `Pet.age` → property object
2.  `.fset` → setter function
3.  `(p, 10)` → call setter with:
    -   `self = p`
    -   `value = 10`

So it executes:

`p._age =  10`


Key Takeaways
-    Every property has fget, fset, fdel
-    They may be None if not defined
-    They are not dunder methods
-    They belong to the property object, not the class directly
-    They store the actual functions used for attribute control



### End of collapsable section on the three attributes `fget`, `fset` and `fdel`

</details>






<details>
<summary>Discussion on `@property` and `@age.setter` (Click ► to expand)</summary>
Before we take up the project, it is important to understand how `@property` and `@age.setter` work.



## A. `@property`

### 1. What does `@property` do? The Core Idea:
`@property` **converts a method into an attribute**

### 2. Without `@property`:

```python

def  age(self):  
  return  self._age  
  
print(p.age()) # must call like a function
```


### 3. With `@property`:

```python

@property  
def  age(self):  
  return  self._age  
  
print(p.age) # looks like attribute

```

### So:

> `@property` allows a method to behave like a variable


## B. `@age.setter`
### 1. What does `@age.setter` do? The Core Idea:

It defines **what should happen when you assign a value**

`p.age =  10`

### 2. Internally, Python converts this to:

`Pet.age.fset(p, 10)`

Which calls:

`def  age(self, value):`

### 3. So:

> `@age.setter` defines how assignment works

## C. What is the link between `@property` and `@age.setter`?

This is the **most important concept**.

### 1: `@property` creates a property object

```python
@property  
def  age(self):
```

This creates:

`age  =  property(getter_function)`

### 2: `@age.setter` attaches setter to same property
```python
@age.setter  
def  age(self, value):
```

This modifies the SAME property:

`age  =  property(getter, setter)`



### 3. So:

> Both getter and setter belong to the same "property object"

----------

### 4. You can visualise the scheme as follows:

age (property object)  
 ├── getter → returns _age  
 └── setter → validates and sets _age


## D. Where are `@property` and `@age.setter` defined?

## 1. Answer:

They are **built-in in Python**

No import needed.



### 2. Internally:

-   `property` is a built-in class
-   `@property` is just syntactic sugar

</details>









## Project/ Assignment Task is as follows

Modify a `Pet` class to implement **encapsulation using property decorators**.

----------

### Instructions

-   Use attribute:

     -  `_age`

-   Provide:
    -   Getter
    -   Setter
    -   (Optional) Deleter


#### Hints

-   Use:

    -    `@property  `
    -    `@age.setter`

-   Raise error if:

`age  <  0`

----------

#### Dos and Don’ts

-  Use `_age` internally  
-  Validate age  
-  Do not assign `self.age = value` inside setter


### Answer/ Solution

-   Property allows controlled access to attributes.
-   It replaces getter/setter methods.
-   Validation logic can be added without changing syntax.



### Table

  

| Feature | Traditional | Property |
| --- | --- | --- |
| Access | `get_age()` | `obj.age` |
| Modify | `set_age()` | `obj.age = value` |
| Validation | Manual | Built-in |


## Solution script


```python

# This script defines the Pet class with instance attributes "name" and "age", and a property for age with validation. 
# The @property decorator is used to create a getter for the age attribute, allowing us to access it as if it were a regular attribute. 
# The @age.setter decorator is used to define a setter for the age property, which includes validation to ensure 
# that the age cannot be set to a negative value. # If an attempt is made to set a negative age, a ValueError 
# is raised with the message "Invalid age". # Finally, we test the class by creating an instance of Pet, 
# accessing the age property, and setting a new valid age. We also demonstrate that setting an invalid age raises an error.  


# A. Define the Pet class.
class Pet:
    def __init__(self, name, age):
        self.name = name
        self._age = age
    
    # B. @property for age with validation. 
    # The @property decorator is used to create a getter for the age attribute, allowing us to access it as 
    # if it were a regular attribute. The method simply returns the value of the private attribute _age, 
    # which is where we store the actual age value. By using @property, we can add validation logic in 
    # the setter method while still allowing users to access the age attribute in a natural way.
    
    @property
    def age(self):  
        return self._age
    
    # C. Setter for age with validation
    # The @age.setter decorator allows us to define a setter method for the age property. This means that when 
    # we assign a value to pet_instance.age, this setter method will be called with the new value. 
    # Inside the setter, we can add validation logic to ensure that the age being set is 
    # valid (in this case, non-negative). If the value is less than 0, we raise a ValueError to indicate 
    # that the age is invalid. If the value is valid, we assign it to the private attribute _age. 
    # This way, we can control how the age attribute is set and ensure that it always contains a valid value.   
    
    @age.setter
    def age(self, value):  
        if value < 0:
            raise ValueError("Invalid age")
        self._age = value


# C. Testing
p = Pet("Tommy", 5)
print(p.age)  # Output: 5. 

p.age = 10
print(p.age)  # Output: 10.

# p.age = -5  # Error: Invalid age


```














