





## RESEARCH / PROJECT QUESTION:- Design a Pet Registration System Using 3 Approaches

You are required to design a **Pet Management System** that demonstrates three different ways of registering classes in Python.

----------

### Requirements

#### Part A: Manual Registration

1.  Create a class `PetRegistryManual`
    
2.  Maintain a dictionary `registry`
    
3.  Provide a method `register(name, cls)`
    
4.  Create classes:
    
    -   `Dog`
        
    -   `Cat`
        
5.  Manually register them
    
6.  Dynamically create objects and call `speak()`
    

----------

#### Part B: Decorator-Based Registration

1.  Create a class `PetRegistryDecorator`
    
2.  Implement a decorator method `register(name)`
    
3.  Register classes using `@decorator`
    
4.  Create:
    
    -   `Bird`
        
    -   `Fish`
        
5.  Dynamically call their methods
    

----------

#### Part C: Automatic Registration (`__init_subclass__`)

1.  Create base class `Pet`
    
2.  Automatically register subclasses using:
    
    `__init_subclass__()`
    
3.  Create:
    
    -   `Horse`
        
    -   `Cow`
        
4.  Print all registered subclasses
    
5.  Dynamically create objects
    

----------

#### Final Task

-   Compare all 3 approaches
    
-   State advantages and disadvantages
    

----------

## PART 2: SOLUTION/ EXPLANATION


### Core Idea

All three approaches aim to:

> Store class references so they can be used dynamically

----------

### Approach 1: Manual Registration

#### Idea

-   Programmer explicitly registers classes
    

#### Why used?

-   Simple and easy for beginners
    

----------

### Approach 2: Decorator Registration

#### Idea

-   Registration happens automatically at class definition
    

#### Why used?

-   Cleaner and safer
    

----------

### Approach 3: Automatic Registration

#### Idea

-   Base class tracks all subclasses automatically
    

#### Why used?

-   Best for large systems and frameworks
    

----------

## PART 3: SCRIPTS



### 1. Manual Registration

```python

# A. Manual registration of pet classes in a registry
class PetRegistryManual:  # Manual registration of pet classes
    registry = {}  # This is a class attribute that will hold the mapping of pet names to their corresponding classes. It is shared across all instances of the PetRegistryManual class.

    @classmethod
    def register(cls, name, pet_class):  # (class method) This is a class method that allows us to register a pet class with a specific name. The cls parameter refers to the class itself (PetRegistryManual), and it is used to access the class attribute registry.
        cls.registry[name] = pet_class

# B. Define pet classes to be registered
class Dog:
    def speak(self):  # This is an instance method that defines the behavior of the Dog class when the speak() method is called. It will print "Dog barks" to indicate that the dog is barking.
        print("Dog barks")

# C. Define another pet class
class Cat:
    def speak(self):  # This is an instance method that defines the behavior of the Cat class when the speak() method is called. It will print "Cat meows" to indicate that the cat is meowing.
        print("Cat meows")


# D. Manual registration of pet classes in the registry
PetRegistryManual.register("dog", Dog)  # This line registers the Dog class with the name "dog" in the PetRegistryManual registry. It allows us to later retrieve the Dog class using the name "dog" from the registry.
PetRegistryManual.register("cat", Cat)  # This line registers the Cat class with the name "cat" in the PetRegistryManual registry. It allows us to later retrieve the Cat class using the name "cat" from the registry.

# E. Dynamic usage of the registry to create pet objects and call their speak() method
# E1. Create Dog object using registry
PetClass = PetRegistryManual.registry["dog"]  # This line retrieves the Dog class from the PetRegistryManual registry using the name "dog" and assigns it to the variable PetClass. Now, PetClass holds a reference to the Dog class, and we can use it to create an instance of the Dog class.
pet = PetClass() # This line creates an instance of the Dog class by calling the constructor of the Dog class (which is now referenced by PetClass). The parentheses () indicate that we are calling the constructor to create an object of the Dog class, and the resulting object is assigned to the variable pet.    
pet.speak()  # This line calls the speak() method on the pet object, which is an instance of the Dog class. It will print "Dog barks" to indicate that the dog is barking.

# E2. Create Cat object using registry
PetClass = PetRegistryManual.registry["cat"]  # This line retrieves the Cat class from the PetRegistryManual registry using the name "cat" and assigns it to the variable PetClass. Now, PetClass holds a reference to the Cat class, and we can use it to create an instance of the Cat class.
pet = PetClass() # This line creates an instance of the Cat class by calling the constructor of the Cat class (which is now referenced by PetClass). The parentheses () indicate that we are calling the constructor to create an object of the Cat class, and the resulting object is assigned to the variable pet.
pet.speak()  # This line calls the speak() method on the pet object, which is an instance of the Cat class. It will print "Cat meows" to indicate that the cat is meowing.


```

### 2. Decorator Registration

```python

# A. Define a pet registry class with a class attribute and a class method for registration
class PetRegistryDecorator:
    registry = {}                           # This is a class attribute that will hold the mapping of pet names to their corresponding classes. It is shared across all instances of the PetRegistryDecorator class.

    # B. Define a class method that acts as a decorator for registering pet classes
    @classmethod                            
    def register(cls, name):                # This is a class method that allows us to register a pet class with a specific name. The cls parameter refers to the class itself (PetRegistryDecorator), and it is used to access the class attribute registry. The name parameter is the name under which the pet class will be registered in the registry.
        def wrapper(pet_class):             # This is a closure function that takes the pet class as an argument, registers it in the registry, and returns the pet class.
            cls.registry[name] = pet_class  # This line registers the pet class in the registry under the specified name. It adds an entry to the registry dictionary where the key is the name and the value is the pet class.
            return pet_class                # This line returns the pet class after registering it. This allows us to use the decorator syntax to register the pet class while defining it, making the registration process more elegant and concise.
        return wrapper                      # This line returns the wrapper function, which is the actual decorator that will be applied to the pet classes when they are defined. The wrapper function will handle the registration of the pet class in the registry when the decorator is used.

# C. Define pet classes to be registered using the decorator syntax
@PetRegistryDecorator.register("bird")      # This line uses the decorator syntax to register the Bird class under the name "bird" in the PetRegistryDecorator registry. When the Bird class is defined, it will be automatically registered in the registry with the name "bird".
class Bird:                                 # This is the definition of the Bird class, which will be registered in the PetRegistryDecorator registry under the name "bird" due to the use of the @PetRegistryDecorator.register("bird") decorator. The Bird class has a speak() method that defines its behavior when the speak() method is called.
    def speak(self):                        # This is an instance method that defines the behavior of the Bird class when the speak() method is called. It will print "Bird chirps" to indicate that the bird is chirping, which is a common behavior of birds.
        print("Bird chirps")                # This line prints "Bird chirps" to indicate that the bird is making a chirping sound, which is a characteristic behavior of birds.

# D. Define another pet class using the decorator syntax
@PetRegistryDecorator.register("fish")      # This line uses the decorator syntax to register the Fish class under the name "fish" in the PetRegistryDecorator registry. When the Fish class is defined, it will be automatically registered in the registry with the name "fish".
class Fish:                                 # This is the definition of the Fish class, which will be registered in the PetRegistryDecorator registry under the name "fish" due to the use of the @PetRegistryDecorator.register("fish") decorator. The Fish class has a speak() method that defines its behavior when the speak() method is called.
    def speak(self):                        # This is an instance method that defines the behavior of the Fish class when the speak() method is called. It will print "Fish bubbles" to indicate that the fish is making bubbles, which is a common behavior of fish in water.
        print("Fish bubbles")               # This line prints "Fish bubbles" to indicate that the fish is making bubbles, which is a characteristic behavior of fish.

# E. Dynamic usage of the registry to create pet objects and call their speak() method
# E1. Create Bird object using registry
PetClass = PetRegistryDecorator.registry["bird"]  # This line retrieves the Bird class from the PetRegistryDecorator registry using the name "bird" and assigns it to the variable PetClass. Now, PetClass holds a reference to the Bird class, and we can use it to create an instance of the Bird class.
pet = PetClass()                                  # This line creates an instance of the Bird class using the PetClass variable, which holds a reference to the Bird class.
pet.speak()                                       # This line calls the speak() method on the pet object, which is an instance of the Bird class. It will print "Bird chirps" to indicate that the bird is chirping.

# E2. Create Fish object using registry
PetClass = PetRegistryDecorator.registry["fish"]  # This line retrieves the Fish class from the PetRegistryDecorator registry using the name "fish" and assigns it to the variable PetClass. Now, PetClass holds a reference to the Fish class, and we can use it to create an instance of the Fish class.
pet = PetClass()                                  # This line creates an instance of the Fish class using the PetClass variable, which holds a reference to the Fish class.
pet.speak()                                       # This line calls the speak() method on the pet object, which is an instance of the Fish class. It will print "Fish bubbles" to indicate that the fish is making bubbles, which is a characteristic behavior of fish.

```

### 3. Automatic Registration

```python

# A. Define a registry class to hold pet classes
class Pet:
    registry = []                         # This is a class attribute that will hold a list of pet classes. It is shared across all instances of the Pet class, and it will be used to store references to all subclasses of Pet that are defined in the code. This allows us to keep track of all pet classes in one place, making it easier to manage and use them dynamically later on.

    # B. Define a special class hook to automatically register subclasses
    def __init_subclass__(cls):           # (special class hook)  This is a special class method that is called whenever a new subclass of Pet is defined. The cls parameter refers to the subclass that is being created. By overriding this method, we can automatically register any new pet class that inherits from Pet into the registry list without having to manually add it. This allows for a more elegant and automated way of keeping track of all pet classes as they are defined.
        super().__init_subclass__()       # This line calls the __init_subclass__ method of the parent class (which is object in this case) to ensure that any necessary initialization logic defined in the parent class is executed
        Pet.registry.append(cls)          # This line adds the newly created subclass (cls) to the Pet.registry list. This means that every time a new pet class is defined that inherits from Pet, it will automatically be added to the registry, allowing us to easily access and manage all pet classes in one place.

# C. Define pet classes that will be automatically registered in the Pet registry
class Horse(Pet):
    def speak(self):                      # This is an instance method that defines the behavior of the Horse class when the speak() method is called. It will print "Horse neighs" to indicate that the horse is making a neighing sound, which is a characteristic behavior of horses.
        print("Horse neighs")             # This line prints "Horse neighs" to indicate that the horse is making a neighing sound, which is a characteristic behavior of horses.

# D. Define another pet class
class Cow(Pet):
    def speak(self):                      # This is an instance method that defines the behavior of the Cow class when the speak() method is called. It will print "Cow moos" to indicate that the cow is making a mooing sound, which is a characteristic behavior of cows.
        print("Cow moos")                 # This line prints "Cow moos" to indicate that the cow is making a mooing sound, which is a characteristic behavior of cows.

# E. Dynamic usage of the registry to create pet objects and call their speak() method
for cls in Pet.registry:
    obj = cls()                           # This line creates an instance of the pet class represented by cls, which is a subclass of Pet.
    obj.speak()                           # This line calls the speak() method on the created object, which will execute the specific implementation of the speak() method defined in each pet class (Horse and Cow in this case), demonstrating polymorphism as the same method name (speak()) can have different behaviors based on the type of pet object created.


```

### Comparison Table

  

| Feature | Manual | Decorator | Auto (__init_subclass__) |
| --- | --- | --- | --- |
| Registration | Explicit | Automatic | Fully automatic |
| Ease | Easy | Medium | Medium |
| Flexibility | Low | High | Medium |
| Risk of error | High | Low | Very Low |
| Best use | Small scripts | Apps | Frameworks |



















