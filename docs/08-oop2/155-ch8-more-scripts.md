


## Python Scripting Scenarios


The transition from conceptual theory to algorithmic implementation requires translating "Is-A" and "Has-A" logic into executable code. Scripting these relationships allows a developer to verify the flow of data through the MRO and ensure that namespaces are respected across various scopes. The following exercises demonstrate the application of inheritance, abstract classes, and scope management in professional Python development.
```

1. Checking instance relationships using `isinstance()` for parent and child classes.

```python


class Parent:
    pass

class Child(Parent):
    pass

p = Parent()
c = Child()

# isinstance() identifies an object as its class or any base class
print(f"Is c a Child? {isinstance(c, Child)}")   # True
print(f"Is c a Parent? {isinstance(c, Parent)}") # True (due to Is-A relationship)
print(f"Is p a Child? {isinstance(p, Child)}")   # False (base class is not a subclass)
```

2. Visualizing MRO using the `__mro__` attribute.

```python


class A: pass
class B(A): pass
class C(B): pass

# __mro__ provides the deterministic linearization of the search path
print(C.__mro__) 
# Resolution Path: C -> B -> A -> object (root)
```

3. Implementing a `super().__init__ `call to ensure parent attributes exist in the child.

```python


class Pet:
    def __init__(self, name):
        self.name = name # Attribute defined in parent scope

class Dog(Pet):
    def __init__(self, name, breed):
        # Mandatory call to ensure 'name' is bound to the instance
        super().__init__(name) 
        self.breed = breed # Child specific state

d = Dog("Buddy", "Golden Retriever")
print(f"{d.name} is a {d.breed}")
```

4. Demonstrating "Replacement Is-A" by overriding a method completely.

```python


class Pet:
    def speak(self):
        print("Generic pet sound")

class Cat(Pet):
    def speak(self):
        # Replaces parent logic entirely; parent's print is ignored
        print("Meow!")

c = Cat()
c.speak() # Only child logic executes
```

5. Demonstrating "Additive Is-A" by adding a unique method to a `Pet` subclass.

```python


class Pet:
    def eat(self):
        print("Eating...")

class Dog(Pet):
    def fetch(self): # New specialized method not present in Pet
        print("Fetching the ball!")

d = Dog()
d.eat()   # Inherited behavior
d.fetch() # Extended behavior
```

6. Demonstrating "Cooperative Is-A" where `super().method()` refines parent behavior.

```python


class Pet:
    def speak(self):
        print("...and makes a generic sound.")

class Dog(Pet):
    def speak(self):
        print("Dog barks...", end=" ") # Unique Child logic
        super().speak()               # Cooperatively call Parent logic

d = Dog()
d.speak() # Combines both layers of behavior
```

7. Resolving method conflicts in Multiple Inheritance.

```python


class Walker:
    def action(self):
        print("Walking...")

class Swimmer:
    def action(self):
        print("Swimming...")

# MRO is determined by the order of parents in the declaration
class Dog1(Walker, Swimmer): pass # Walker takes priority
class Dog2(Swimmer, Walker): pass # Swimmer takes priority

d1, d2 = Dog1(), Dog2()
d1.action() # Output: Walking...
d2.action() # Output: Swimming...
```

8. Implementing a basic "Has-A" relationship (Composition) between a `Dog` and a `Collar`.

```python


class Collar:
    def __init__(self, color):
        self.color = color

class Dog:
    def __init__(self, name, color):
        self.name = name
        # Composition: The Dog instance 'owns' a Collar instance
        self.collar = Collar(color) 

d = Dog("Tommy", "Red")
print(f"{d.name} has a {d.collar.color} collar.")
```

9. Using raise `NotImplementedError` in a base class to enforce method implementation.

```python


class Pet:
    def speak(self):
        # Informal abstract method; fails only when called at runtime
        raise NotImplementedError("Subclasses must override speak()")

class Cat(Pet):
    pass # Failed to implement speak()

c = Cat()
# c.speak() # This would trigger the runtime crash
```

10. Using the `abc` module to create a formal `Abstract Base Class`.

```python


from abc import ABC, abstractmethod

class Pet(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Pet):
    def speak(self):
        print("Bark!")

# pet = Pet() # This would trigger a TypeError (Instantiation Failure)
```

11. Registering a virtual subclass and verifying its absence from MRO.

```python


from abc import ABC

class Pet(ABC): pass

class RobotDog: 
    def beep(self): print("Beep!")

# Logical registration: RobotDog is now a 'type' of Pet
Pet.register(RobotDog)

r = RobotDog()
print(f"Is RobotDog a Pet? {isinstance(r, Pet)}") 
print(f"RobotDog MRO: {RobotDog.__mro__}") 
# Note: RobotDog's MRO does NOT contain Pet; it inherits no code.
```

12. Creating a custom container using `__setitem__` and `__getitem__`.

```python


class VehicleRegistry:
    def __init__(self, capacity):
        self._vehicles = [None] * capacity

    def __setitem__(self, index, value):
        self._vehicles[index] = value # Enables obj[i] = val syntax

    def __getitem__(self, index):
        return self._vehicles[index] # Enables val = obj[i] syntax

v = VehicleRegistry(2)
v[0] = "Truck"
print(v[0])
```

13. Accessing and modifying attributes through the `__dict__` namespace.

```python


class Dog:
    def __init__(self, name):
        self.name = name

d = Dog("Bruno")
# Bypassing standard attribute access to modify the internal dictionary
d.__dict__["breed"] = "Boxer" 
print(d.breed) # Attribute exists in instance namespace
```

14. Demonstrating variable shadowing and the `LEGB` lookup order.

```python


scope = "Global"

def outer():
    scope = "Enclosing"
    def inner():
        scope = "Local" # Shadows both Enclosing and Global
        print(f"Inner sees: {scope}")
    inner()

outer() # Standard LEGB resolution finds 'Local' first
```

15. Using the `nonlocal` keyword to modify an enclosing variable.

```python


def tracker():
    count = 0
    def update():
        # Bind 'count' to the Enclosing scope, skipping the Local search
        nonlocal count 
        count += 1
        return count
    return update

my_tracker = tracker()
print(my_tracker()) # Output: 1 (Enclosing state preserved)
```

16. Using the `global` keyword to modify a file-level variable.

```python


system_status = "Offline"

def activate():
    # Instructs the interpreter to target the module-level namespace
    global system_status 
    system_status = "Online"

activate()
print(system_status) # Global state successfully mutated
```

17. Implementing `__repr__` for professional debugging.

```python


class Dog:
    def __init__(self, name, age):
        self.name, self.age = name, age
    
    def __repr__(self):
        # Returns string suitable for recreating the object state
        return f"Dog(name='{self.name}', age={self.age})"

d = Dog("Rex", 5)
print(f"Debug log: {repr(d)}")
```

18. Enforcing consistency between `__eq__` and `__hash__`.

```python


class IDCard:
    def __init__(self, uid):
        self.uid = uid
    def __eq__(self, other):
        return isinstance(other, IDCard) and self.uid == other.uid
    def __hash__(self):
        # Objects that compare equal must return the same hash
        return hash(self.uid)

cards = {IDCard(101), IDCard(101)}
print(f"Unique cards in set: {len(cards)}") # Output: 1 (Correct)
```

19. Automating registration via a class decorator.

```python


registry = []

def register_pet(cls):
    registry.append(cls)
    return cls

@register_pet
class Dog: pass

@register_pet
class Cat: pass

print(f"Registered pets: {[c.__name__ for c in registry]}")
```

20. Demonstrating the Instantiation Guard of ABCs.

```python


from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def run(self): pass

class Concrete(Base):
    def run(self): print("Running...")

try:
    # Cannot instantiate a class that hasn't fulfilled the abstract contract
    b = Base() 
except TypeError as e:
    print(f"Guard triggered: {e}")
Mastering these 50 items establishes a rigorous foundation for high-tier Python software architecture, ensuring that inheritance structures are efficient, the Open-Closed Principle is respected, and namespaces are managed with professional-grade precision.

```









