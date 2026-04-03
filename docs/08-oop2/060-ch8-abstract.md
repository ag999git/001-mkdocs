







## PROJECT: Designing a Robust Pet System Using Abstract Classes

----------

### Problem Statement

Design a system where:

-   All pets must implement:
    
    -   `speak()`
        
    -   `move()`
        
-   Some pets:
    
    -   Walk
        
    -   Swim
        
    -   Do both (multiple inheritance)
        

----------

### Requirements

#### 1. Create Abstract Base Class `Pet`

-   Methods:
    
    -   `speak()` → abstract
        
    -   `move()` → abstract
        

----------

#### 2. Create Classes

##### Dog

-   speak → Bark
    
-   move → Walk
    

##### Fish

-   speak → (silent or "blub")
    
-   move → Swim
    

----------

#### 3. Multiple Inheritance

Create:

`class  Amphibian(Walker, Swimmer)`

-   Should:
    
    -   Walk AND Swim
        
    -   Use `super()` properly
        

----------

#### 4. Enforce Rules

-   Use `ABC` and `@abstractmethod`
    
-   Ensure:
    
    -   Cannot create incomplete classes
        

----------

#### 5. Show Output

-   Create objects
    
-   Call methods
    
-   Print MRO
    

----------

### Script
The following script shows the solution to the problem.

```python

from abc import ABC, abstractmethod

# A. ABSTRACT BASE CLASS
class Pet(ABC):

    @abstractmethod
    def speak(self):  # Abstract method that must be implemented by all subclasses
        pass

    @abstractmethod
    def move(self):  # Abstract method for movement
        pass


# B. WALKER CLASS
class Walker(Pet):

    def move(self):  # Concrete method that implements move() for Walker
        print("Walking...")
        super().move()


# C. SWIMMER CLASS
class Swimmer(Pet):

    def move(self):  # Concrete method that implements move() for Swimmer
        print("Swimming...")
        super().move()


# D. DOG CLASS
class Dog(Walker):

    def speak(self):  # Concrete method that implements speak() for Dog
        print("Dog barks")

    def move(self):  # Concrete method that implements move() for Dog
        print("Dog moves")
        super().move()


# E. FISH CLASS
class Fish(Swimmer):

    def speak(self):  # Concrete method that implements speak() for Fish
        print("Fish makes sound")

    def move(self):  # Concrete method that implements move() for Fish
        print("Fish moves")
        super().move()

# F. TESTING MRO and functionality of Dog and Fish classes

# (1). For Dog class
# print("MRO for Dog:", Dog.__mro__)
# Expected MRO for Dog: Dog → Walker → Pet → object
d = Dog()  # Create Dog object
d.speak()  # Dog barks
d.move() # Dog moves
# Expected Output:
# Dog moves
# Walking...

# (2). For Fish class
print("MRO for Fish:", Fish.__mro__)
# MRO for Fish: Fish → Swimmer → Pet → object
f = Fish()  # Create Fish object
f.speak()  # Fish makes sound
f.move() 
# Expected Output:
# Fish moves
# Swimming...


# G. MULTIPLE INHERITANCE
class Amphibian(Walker, Swimmer):

    def speak(self):  # Concrete method that implements speak() for Amphibian
        print("Amphibian sound")

    def move(self):  # Concrete method that implements move() for Amphibian
        print("Amphibian moves")
        super().move()


# H. TESTING MRO and functionality of Amphibian class
print("MRO for Amphibian:", Amphibian.__mro__)
# Expected MRO: Amphibian → Walker → Swimmer → Pet → object
a = Amphibian()  # Create Amphibian object
a.speak() # Amphibian sound
a.move()  
# Expected Output:
# Amphibian moves
# Walking...
# Swimming...



```





#### Comparison of Basic Abstract (Usong NotImplementedError) to ABC Module
  

| Feature | Basic Abstract | ABC Module |
| --- | --- | --- |
| Enforcement | Weak | Strong |
| Error Time | Runtime | Instantiation |
| Standard Practice | No | Yes |
| Used in Industry | Rare | Very Common |




  

  #### Role of various components

| Concept | Role |
| --- | --- |
| Abstract Class | Defines rules |
| Child Class | Implements behavior |
| super() | Chains execution |
| MRO | Controls order |






