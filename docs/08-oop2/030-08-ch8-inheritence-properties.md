





## **Problem Statement**

### Design a Python program that demonstrates all major properties of inheritance, including: (1) Is-A relationship. (2) Code reuse. (3) Method Resolution Order (MRO). (4) Overriding. (5) Polymorphism. (6) super(). (7) Constructor behavior. (8) Dynamic binding. (9) Encapsulation. (10) Extensibility. (11) Maintainability.

### The given script does the following
### 1. Creates Base Class: `Pet`

This class includes:

-   Attribute: `name`
    
-   Private attribute: `__secret`
    
-   Methods:
    
    -   `walk()` → prints a message
        
    -   `speak()` → generic message
        
    -   Constructor `__init__()`
        

----------

### 2. Creates derived Class: `Dog`
This class does the following
-   Inherits from `Pet`
    
-   Adds attribute: `color`
    
-   Overrides:
    
    -   `speak()`
        
    -   `walk()`
        
-   Uses `super()` in constructor and methods
    

----------

### 3. Creates derived Class: `Cat`
This does the following
-   Inherits from `Pet`
    
-   Overrides `speak()`
    

----------



### The script also demonstrates:

----------

#### 1. Is-A Relationship

-   Shows that `Dog` and `Cat` are types of `Pet`
    

----------

#### 2. Does code reuse

-   Uses inherited `walk()` where applicable
    

----------

#### 3. Overrides 

-   Shows different `speak()` implementations
    

----------

### 4. Implements polymorphism

-   Creates a list of pets and call `speak()` using a loop
    

----------

### 5. Shows usage of `super()`

-   Calls parent constructor and methods
    

----------

### 6. Shows constructor Behavior

-   Shows how constructors behave in parent and child
    

----------

### 7. Uses MRO

-   Prints method resolution order
    

----------

### 8. Shows encapsulation

-   Accesses private variable using a method
    

----------

### 9. Shows dynamic binding

-   Demonstrates runtime method selection
    

----------

### 10. Shows extensibility

-   Adds a new attribute in child class
    

----------

### 11. Shows maintainability

-   Shows how modifying parent affects child


### The script is as follows:

```python

# BASE CLASS: Pet

class Pet:
    def __init__(self, name):  # Constructor to initialize the name of the pet
        self.name = name              # Public attribute
        self.__secret = "Hidden"      # Encapsulation (private variable)
        print("Pet constructor called")  # This will show when the Pet constructor is called, which will help us understand constructor chaining when we create instances of Dog and Cat.

    def walk(self):  # Concrete method available to all subclasses
        print(f"{self.name} is walking (Pet method)")   # Code reuse

    def speak(self):  # Method to be overridden by subclasses
        print(f"{self.name} makes a sound (Pet method)")  # This is a placeholder method that can be overridden by subclasses to provide specific behavior for different types of pets.

    def show_secret(self):  # Method to demonstrate encapsulation
        print("Accessing private:", self._Pet__secret)  # Encapsulation access


# DERIVED CLASS: Dog
class Dog(Pet):   # Is-A relationship: Dog is a Pet

    def __init__(self, name, color):  # Constructor chaining + Extensibility
        print("Dog constructor called")
        super().__init__(name)   # super() → constructor chaining
        self.color = color       # Extensibility (new attribute)

    def speak(self):             # Overriding
        print(f"{self.name} says Bark!")

    def walk(self):              # Overriding + super()
        print(f"{self.name} walks like a dog")
        super().walk()           # Call parent method

# DERIVED CLASS: Cat
class Cat(Pet):   # Is-A relationship

    def speak(self):             # Overriding
        print(f"{self.name} says Meow!")

# OBJECT CREATION
d = Dog("Tommy", "Black")
c = Cat("Kitty")

# 1. Code Reuse
d.walk()   # Uses Dog + Pet method
c.walk()   # Uses Pet method (inherited)


# 2. Overriding
d.speak()  # Dog's speak() overrides Pet's speak()
c.speak()  # Cat's speak() overrides Pet's speak()

# 3. Polymorphism + Dynamic Binding
pets = [d, c]

for p in pets:
    p.speak()   # Runtime decision (dynamic binding)

# 4. Encapsulation
d.show_secret()


# 5. isinstance() → Is-A check
print(isinstance(d, Dog))   # True
print(isinstance(d, Pet))   # True → Is-A relationship


# 6. issubclass()
print(issubclass(Dog, Pet))  # True
print(issubclass(Cat, Pet))  # True
print(issubclass(Dog, Cat))  # False

# 7. MRO (Method Resolution Order)
print("Dog MRO:", Dog.__mro__)
print("Cat MRO:", Cat.__mro__)

# 8. Constructor Behavior
# Dog constructor → calls Pet constructor via super()

# 9. Maintainability
# If we change Pet.walk(), both Dog and Cat behavior changes

# 10. Extensibility
print(d.color)   # New feature added in child
# Note: We can also add new methods in Dog or Cat without affecting Pet, demonstrating extensibility.

```

#### The following table summarizes important properties of inheritence


  
  

| S. No | Property | Simple Meaning | Technical Description | Example | Output / Behavior | Related Concept |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Is-A Relationship | One class is a type of another | Establishes inheritance hierarchy | Dog(Pet) | Dog is treated as Pet | OOP Design |
| 2 | Code Reuse | Use existing code | Child inherits methods/attributes | d.walk() | Uses Pet.walk() | DRY Principle |
| 3 | Implicit Method Lookup | Python searches automatically | If method not in child → check parent | No __init__ in Dog | Parent constructor runs | MRO |
| 4 | Method Resolution Order (MRO) | Search order for methods | Defined linear order of lookup | Dog.__mro__ | (Dog, Pet, object) | C3 Linearization |
| 5 | Polymorphism | Same method, different behavior | Method overridden in subclasses | speak() | Dog → Bark, Cat → Meow | Dynamic Binding |
| 6 | Overriding | Replace parent method | Child defines same method name | Dog.speak() | Child method runs first | Runtime Behavior |
| 7 | super() Usage | Call parent explicitly | Used to access parent methods | super().__init__() | Parent + child both run | Constructor chaining |
| 8 | Constructor Behavior | How objects are initialized | Depends on presence of __init__ | Dog with/without init | Different flows | Object lifecycle |
| 9 | Dynamic Binding | Decision at runtime | Method call resolved dynamically | Loop over pets | Correct method runs | Polymorphism |
| 10 | Extensibility | Add new features | Child adds attributes/methods | color in Dog | More functionality | Design flexibility |
| 11 | Encapsulation Support | Protect data | Private variables inherited with name mangling | __var | Access via _Class__var | Data hiding |
| 12 | Hierarchy Formation | Class structure | Forms tree-like structure | Pet → Dog → Puppy | Multi-level relation | System design |
| 13 | Reusability Across Levels | Use features from any level | Child can access grandparent methods | Multi-level inheritance | Deep reuse | MRO |
| 14 | Maintainability | Easy to update code | Change parent → affects children | Modify Pet.walk() | All subclasses updated | Clean code |









