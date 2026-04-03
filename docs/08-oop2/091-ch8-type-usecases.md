## Using metaclasses (Advance topic)


### Use Case 1: Enforce Rules on Classes


Example: The following script shows a use case where every `Pet` class must have a `speak()` method
It creates 2 classes `Dog` and `Cat`. The `Dog` class implements `speak()` so it works. But the `Cat` class does not implement `speak()` so it doesnt work and throws an error

```python

# In Python, a metaclass is a class of a class that defines how a class behaves. 
# A class is an instance of a metaclass. The most common use of metaclasses is 
# to create APIs, enforce coding standards, or implement design patterns. 
# A metaclass can be defined by inheriting from the built-in `type` class 
# and overriding its methods to customize class creation. 

# 1. Define a metaclass that checks for the presence of a specific method (e.g., speak()) in any class that uses it as a metaclass. If the method is not implemented, raise an error at the time of class creation.
class PetMeta(type):
    def __new__(mcs, name, bases, dct):
        if "speak" not in dct:
            raise TypeError(f"{name} must implement speak()")  # Check if speak() method is implemented in the class
        return super().__new__(mcs, name, bases, dct)  # Create the class using the standard type.__new__ method

# 2. Create Dog that implements speak() 
# PetMeta is a metaclass that checks if any class that uses it as a metaclass implements the speak() method.
# Since Dog implements speak(), it will be created successfully.
class Dog(metaclass=PetMeta):  # Dog class uses PetMeta as its metaclass
    def speak(self):
        print("Bark")

# 3. Create Cat that does NOT implement speak()
# Our PetMeta metaclass checks for the presence of the speak() method in any class that uses it as a metaclass.
# If a class does not implement speak(), a TypeError is raised at the time of class creation.
# Error here at class creation because Cat does not implement speak() method, 
# so we cannot create an object of Cat class.
class Cat(metaclass=PetMeta):
    pass   #  TypeError: Cat must implement speak() 


```


### Use Case 2: Automatic Registration
Used in: 
-  Plugins
-  Frameworks
-  Django models

```python

# This code demonstrates the use of metaclasses in Python to automatically register subclasses of 
# a base class (Pet) in a registry list. Instead of manually doing: registry.append(Dog),
# We can use a metaclass to automatically register all subclasses of Pet in a registry list.
# In this example, we have defined a metaclass called PetMeta that 
# automatically registers any new pet classes that are defined using it.

# A. Define a global registry list to hold pet classes. Whenever a new class is defined 
# that uses PetMeta as its metaclass, it will automatically be added to this registry list, 
# allowing us to keep track of all pet classes in one place without having to manually add them. 
# This makes it easier to manage and use the pet classes dynamically later on in the code.
registry = []  # Global registry list to hold pet classes
# *********************************

# B. Define a metaclass that checks for the presence of a specific method (e.g., speak()). 
# It inherits from the built-in `type` class, which is the default metaclass for all classes in Python. 
# in any class that uses it as a metaclass. 
# If the method is not implemented, raise an error at the time of class creation.
class PetMeta(type):  # This is a metaclass that inherits from the built-in `type` class.
    def __new__(mcs, name, bases, dct):
        cls = super().__new__(mcs, name, bases, dct)
        if name != "Pet":  # Avoid registering the base class itself
            registry.append(cls)
        return cls
# *********************************

# C. Define pet classes that will be automatically registered in the Pet registry
# When we define a new class that uses PetMeta as its metaclass, it will automatically be added to the registry list. 
# This allows us to keep track of all pet classes in one place without having to manually add them, 
# making it easier to manage and use them dynamically later on in the code.
# Pet need not implement speak() method because we are not creating an object of Pet class,
# we are only using it as a base class for other pet classes like Dog and Cat
class Pet(metaclass=PetMeta):  # This is the base class for all pets. 
    pass
# *********************************

# D. Define pet classes Dog and Cat that will be automatically registered in the Pet registry
class Dog(Pet):  # This is a subclass of Pet that represents a Dog class. It inherits from the Pet class.
    # Must implement the speak() method for Dog class. Else it will raise an error at the time of class creation 
    # because our PetMeta metaclass checks for the presence of the speak() method in any class that uses it 
    # as a metaclass.
    def speak(self):
        print("Dog barks")  # This is an instance method that defines the behavior of the Dog class when the speak() method is called. It will print "Dog barks" to indicate that the dog is making a barking sound, which is a characteristic behavior of dogs.

class Cat(Pet):  # This is another subclass of Pet that represents a Cat class. Like the Dog class, it inherits from the Pet class.
    # Must implement the speak() method for Cat class. Else it will raise an error at the time of class creation because our PetMeta metaclass checks for the presence of the speak() method in any class that uses it as a metaclass.
    def speak(self):
        print("Cat meows")  # This is an instance method that defines the behavior of the Cat class when the speak() method is called. It will print "Cat meows" to indicate that the cat is making a meowing sound, which is a characteristic behavior of cats.

print(registry)  # Output: [<class '__main__.Dog'>, <class '__main__.Cat'>]
# **********************************

# E. Dynamic usage of the registry to create pet objects and call their speak() method
# We can use the registry list to dynamically create instances of the pet classes and call their methods without having to hardcode the class names. 
# This allows for more flexible and dynamic code, as we can easily add new pet classes to   the registry without having to modify the code that creates instances and calls methods on those classes.
for cls in registry:
    obj = cls()  # This line creates an instance of the pet class represented by cls, which is a subclass of Pet. The cls variable holds a reference to the class itself, so calling cls() creates a new instance of that class.
    obj.speak()  # This line calls the speak() method on the created object, which will execute the specific implementation of the speak() method defined in each pet class (Dog and Cat in this case), demonstrating polymorphism as the same method name (speak()) can have different behaviors based on the type of pet object created.  

# Output:
# <class '__main__.Dog'>, <class '__main__.Cat'>
# Dog barks
# Cat meows



```

### Use Case 3: Automatically Add Methods/Attributes

```python

# Use Case 3: Automatically Add Methods/Attributes
# In this example, we have defined a metaclass called PetMeta that automatically adds a new attribute called 
# "category" with the value "Animal" to any class that uses it as a metaclass. This means that any class that 
# uses PetMeta as its metaclass will automatically have this category attribute set to "Animal", allowing us 
# to easily categorize all pet classes without having to manually add this attribute to each class definition.

# A. Define a metaclass that automatically adds a new attribute to classes that use it as a metaclass
class PetMeta(type):
    def __new__(mcs, name, bases, dct):  
        # The above line is the __new__ method of the PetMeta metaclass. 
        # It is called when a new class is being created that uses PetMeta as its metaclass. 
        # The parameters are:
        # 1. mcs: This is the metaclass itself (PetMeta in this case).
        # 2. name: This is the name of the class being created.
        # 3. bases: This is a tuple containing the base classes of the class being created.
        # 4. dct: This is a dictionary containing the attributes and methods of the class being created.

        dct["category"] = "Animal"  
        # The above line adds a new attribute called "category" with the value "Animal" to the class being created. 
        # This means that any class that uses PetMeta as its metaclass will automatically have this category attribute set to "Animal", 
        # allowing us to easily categorize all pet classes without having to manually add this attribute to each class definition.
        return super().__new__(mcs, name, bases, dct)  # This line calls the __new__ method of the parent class (which is type in this case) to create the class using the standard class creation process. It passes the modified dictionary (dct) that now includes the category attribute, ensuring that the new class is created with all the necessary attributes and behaviors defined in the metaclass.

# B. Define a pet class that uses the PetMeta metaclass
class Dog(metaclass=PetMeta):
    def speak(self):
        print("Bark")

# C. Create an object of the Dog class and access the category attribute added by the PetMeta metaclass
dog = Dog()  # This line creates an instance of the Dog class, which uses PetMeta as its metaclass
print("Dog category:->", Dog.category)  # Output: Dog category:-> Animal
# The above line accesses the category attribute of the Dog class, which was automatically added by 
# the PetMeta metaclass.  

# D. Access the category attribute through the dog instance as well
# Dog and dog both can be used to access the category attribute because it is defined at the class level 
# by the PetMeta metaclass,
print(f"Dog category through instance: {dog.category} ->", dog.category)  # Output: Dog category through instance: Animal ->
# The above line accesses the category attribute of the dog instance. Since the category attribute is defined 
# at the class level by the PetMeta metaclass, it is inherited by all instances of the Dog class, 
# allowing us to access it through the instance as well.    

# E. Creating Cat class that does not implement speak() method but uses PetMeta as its metaclass
# Following if uncommented will give error because Cat does not implement speak() method, 
# so we cannot create an object of Cat class.
#class Cat(metaclass=PetMeta):  # Uncommenting gives error.
    #pass   # Uncommenting gives TypeError: Cat must implement speak() because our PetMeta metaclass checks for the presence of the speak() method in any class that uses it as a metaclass.    




```















