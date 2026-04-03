



## **Problem Statement**

You are required to design and implement a **Python-based Animal Management System** to demonstrate advanced concepts of **inheritance and object-oriented programming**.

Your solution must include multiple classes, inheritance relationships, and method implementations that collectively demonstrate key OOP features.


### PART A: CLASS DESIGN

#### 1. Create an Abstract Base Class

-   Create a class `Animal` using `ABC`
    
-   Include:
    
    -   `__init__(self, name)`
        
    -   A **private attribute** `__secret`
        
    -   A concrete method `walk()`
        
    -   An **abstract method** `speak()`
        

----------

#### 2. Create an Additional Class

-   Create a class `Friendly`
    
-   Include method:
    
    -   `nature()` → prints behavior of the animal
        

----------

#### 3. Create Derived Classes

**A. Class `Dog`**

-   Inherit from both `Animal` and `Friendly`
    
-   Add attribute `color`
    
-   Implement:
    
    -   Constructor using `super()` (**constructor chaining**)
        
    -   Override `speak()`
        
    -   Method `show_secret()` to access private variable
        

----------

**B. Class `Cat`**

-   Inherit from `Animal`
    
-   Override `speak()`
    

----------

### PART B: FUNCTIONAL REQUIREMENTS

Write code to demonstrate the following:

----------

#### 1. Code Reuse

-   Call `walk()` method using object of `Dog` and `Cat`
    

----------

#### 2. Method Overriding

-   Show that `Dog` and `Cat` override `speak()`
    

----------

#### 3. Polymorphism (Dynamic Binding)

-   Create a list of animals
    
-   Use a loop to call `speak()` for each object
    

----------

#### 4. Use of `super()`

-   Ensure parent constructor is called from child
    

----------

#### 5. Multiple Inheritance

-   Call `nature()` method using `Dog`
    

----------

#### 6. Encapsulation (Private Members)

-   Access private variable using method inside class
    

----------

#### 7. Type Checking

-   Use:
    
    -   `isinstance()`
        
    -   `issubclass()`
        

----------

#### 8. Method Resolution Order (MRO)

-   Print `__mro__` of class `Dog`
    

----------

### SOLUTION


**The following script implements all of above**


```python


from abc import ABC, abstractmethod

# Abstract Base Class
class Animal(ABC):
    def __init__(self, name):
        self.name = name
        self.__secret = "I am hidden"   # Private variable

    def walk(self):  # Concrete method available to all subclasses
        print(f"{self.name} is walking")

    @abstractmethod
    def speak(self):  # Abstract method to be implemented by subclasses
        pass


# First Parent
class Friendly:  # This is a separate parent class to demonstrate multiple inheritance
    def nature(self):  # Method to demonstrate multiple inheritance
        print("I am friendly and love to socialize!")


# Derived Class
class Dog(Animal, Friendly):  # Dog inherits from both Animal and Friendly, demonstrating multiple inheritance

    def __init__(self, name, color):
        super().__init__(name)   # Calling the constructor of the parent class (Animal) to initialize the name attribute. This is an example of constructor chaining, where the child class constructor calls the parent class constructor
        # Constructor chaining allows us to reuse the initialization logic of the parent class, ensuring that the common attributes are properly set up without having to duplicate code in the child class.
        self.color = color

    # Overriding
    def speak(self):  # Implementing the abstract method
        print(f"{self.name} says Bark!")  # This is an example of method overriding, where the Dog class provides its own implementation of the speak() method defined as an abstract method in the Animal class. By overriding the speak() method, the Dog class can provide

    def show_secret(self):
        # Access private variable (name mangling)
        print(self._Animal__secret)  # This is how we can access the private variable __secret from the Animal class using name mangling. The variable is accessed as _Animal__secret, where _Animal is the name of the class and __secret is the name of the private variable. This allows us to access the private variable even though it is not directly accessible from outside the class.


class Cat(Animal):  # Cat inherits from Animal, demonstrating single inheritance

    def speak(self):  # Implementing the abstract method
        print(f"{self.name} says Meow!")  # This is an example of method overriding, where the Cat class provides its own implementation of the speak() method defined as an abstract method in the Animal class. By overriding the speak() method, the Cat class can provide



# Demonstration of all concepts together


d = Dog("Tommy", "Black")  # Create an instance of Dog with name "Tommy" and color "Black"
c = Cat("Kitty")  # Create an instance of Cat with name "Kitty"

# 1. Code reuse
d.walk()  # Tommy is walking
c.walk()  # Kitty is walking
# Both Dog and Cat can use the walk() method defined in the Animal class, demonstrating code reuse through inheritance. This allows us to avoid duplicating the walk() method in both classes, as they can inherit it from the common parent class (Animal).

# 2. Overriding
d.speak()  # Tommy says Bark!
c.speak()  # Kitty says Meow!
# The speak() method is overridden in both the Dog and Cat classes to provide specific implementations for each type of animal. This allows us to have different behaviors for the same method name (speak()) based on the type of object (Dog or Cat), demonstrating method overriding.

# 3. Polymorphism
pets = [d, c]  # List of pets (Dog and Cat) demonstrating polymorphism
for p in pets:
    p.speak()  # This will call the appropriate speak() method for each pet, demonstrating polymorphism
# Output: 
    # Tommy says Bark!
    # Kitty says Meow!


# 4. Multiple inheritance
d.nature()
# The Dog class inherits from both the Animal and Friendly classes, allowing it to access methods from both parent classes. This demonstrates multiple inheritance, where a class can inherit from more than one parent class, enabling it to combine behaviors and attributes from multiple sources.

# 5. Private access
d.show_secret()
# The show_secret() method in the Dog class accesses the private variable __secret from the Animal class using name mangling. This demonstrates how we can access private variables from a parent class in a child class, even though they are not directly accessible from outside the class.

# 6. isinstance and issubclass
print(isinstance(d, Dog))  # True, because d is an instance of Dog
print(isinstance(d, Animal))  # True, because Dog is a subclass of Animal
print(isinstance(c, Cat))  # True, because c is an instance of Cat
print(issubclass(Dog, Animal)) # True, because Dog is a subclass of Animal

# 7. MRO (Method Resolution Order)
print(Dog.__mro__)  # This will show the method resolution order for the Dog class, which is the order in which Python looks for methods in the class hierarchy. The output will show that Python first looks in the Dog class, then in the Animal class, and finally in the Friendly class, demonstrating how Python resolves method calls in a multiple inheritance scenario.
# Output: (<class '__main__.Dog'>, <class '__main__.Animal'>, <class '__main__.Friendly'>, <class 'object'>)



```






### PART C: TABLE

The following table analyses all the important concepts given in the script:


  

  

| Property | Description | Key Idea | Syntax / Tool | Example | Output Behavior |
| --- | --- | --- | --- | --- | --- |
| Code Reuse | Subclass uses parent methods | No need to rewrite code | Inheritance | Dog.walk() | Uses Animal.walk() |
| Overriding | Subclass redefines method | Child has priority | Same method name | Dog.speak() | Dog version runs |
| Polymorphism | Same method, different behavior | Runtime decision | Same interface | pet.speak() | Different outputs |
| super() | Calls parent method | Extend parent logic | super() | super().__init__() | Parent + child both run |
| MRO | Method search order | Avoid ambiguity | __mro__ | Dog.__mro__ | Shows lookup chain |
| ABC | Enforce method implementation | Blueprint class | ABC, @abstractmethod | speak() | Must override |
| Encapsulation (Private) | Restrict access | Name mangling | __var | _Class__var | Hidden access |
| isinstance() | Check object type | Runtime check | isinstance() | isinstance(d, Dog) | True/False |
| issubclass() | Check class relation | Inheritance check | issubclass() | issubclass(Dog, Animal) | True/False |
| Constructor chaining | Parent + child init | Proper initialization | super().__init__() | Dog init | Both run |
| Dynamic Binding | Method resolved at runtime | Late decision | Polymorphism | loop pets | Correct method called |

#### The following flowchart shows the parent and the derived classes
It also shows the attributes and methods of each class. 

![Diagram](/resources/ch8-inheritence-cat-dog.png)












