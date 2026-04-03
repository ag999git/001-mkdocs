


## Part 2: 20 Programming Script Questions & Answers

1. Create a `Vehicle` parent class and a `Car` child class. Use the pass keyword to demonstrate "Implicit Is-A" inheritance.
```python
class Vehicle:
    def move(self):
        print("This vehicle is moving")

# Child class inheriting everything without changes
class Car(Vehicle):
    pass

c = Car()
c.move() # Output: This vehicle is moving
```

2. Write a script that uses `isinstance()` to check if a `Puppy` object is an instance of `Dog` and an instance of `Pet`.

```python
class Pet: pass
class Dog(Pet): pass
class Puppy(Dog): pass

p = Puppy()
# Checking inheritance relationships
print(f"Is p a Dog? {isinstance(p, Dog)}")  # True
print(f"Is p a Pet? {isinstance(p, Pet)}")  # True

```

3. Demonstrate the `__mro__` attribute by creating a three-level hierarchy: `Animal -> Mammal -> Cat`.

```python

class Animal: pass
class Mammal(Animal): pass
class Cat(Mammal): pass

# Printing the Method Resolution Order
print(Cat.__mro__)

```

4. Create a class where the `__init__` method of the child class explicitly calls the `__init__` method of the parent class using `super()`.

```python

class Bird:
    def __init__(self, species):
        self.species = species

class Parrot(Bird):
    def __init__(self, species, color):
        # Initialize parent attributes using super()
        super().__init__(species)
        self.color = color

p = Parrot("Parrot", "Green")
print(p.species, p.color)
```

5. Write a script that creates a class attribute and an instance attribute, then prints the `__dict__` of both the class and the instance.

```python

class Robot:
    laws = "Protect humans" # Class attribute

    def __init__(self, name):
        self.name = name # Instance attribute

r = Robot("R2D2")
print("Class Dict:", Robot.__dict__)
print("Instance Dict:", r.__dict__)
```

6. Use multiple inheritance to create a `FlyingFish` class that inherits from both `Bird` (for flying) and `Fish` (for swimming).

```python

class Bird:
    def fly(self): print("Flying...")

class Fish:
    def swim(self): print("Swimming...")

# Multiple inheritance
class FlyingFish(Bird, Fish):
    pass

ff = FlyingFish()
ff.fly()
ff.swim()
```

7. Demonstrate "Method Overriding" by creating a parent class `Shape` with a `draw()` method and a child class `Circle` that changes the `draw()` message.

```python

class Shape:
    def draw(self):
        print("Drawing a generic shape")

class Circle(Shape):
    def draw(self):
        # This overrides the parent method
        print("Drawing a circle")

c = Circle()
c.draw()
```

8. Write a script showing "Cooperative Inheritance" where a child method calls `super().speak()` and then adds its own text.

```python

class Person:
    def speak(self):
        print("Hello", end=" ")

class Student(Person):
    def speak(self):
        super().speak() # Call parent logic
        print("I am a student.")

s = Student()
s.speak()
```

9. Create a "Has-A" relationship (Composition) between a CPU class and a `Computer` class.

```python

class CPU:
    def __init__(self, brand):
        self.brand = brand

class Computer:
    def __init__(self, name, cpu_brand):
        self.name = name
        # Composition: Computer HAS-A CPU
        self.processor = CPU(cpu_brand)

pc = Computer("MyPC", "Intel")
print(f"{pc.name} has an {pc.processor.brand} CPU")
```

10. Implement an abstract method using `NotImplementedError` in a class ElectronicDevice and implement it in a `Phone` class.

```python

class ElectronicDevice:
    def power_on(self):
        # Abstract placeholder
        raise NotImplementedError("Must implement power_on in subclass")

class Phone(ElectronicDevice):
    def power_on(self):
        print("Phone screen lights up")

p = Phone()
p.power_on()
```

11. Write a script that uses `locals()` inside a function to show the names and values of local variables.

```python

def my_function():
    a = 10
    b = "```python"
    # Returns the local namespace dictionary
    print(locals())

my_function()
```

12. Demonstrate the "Diamond Problem" in multiple inheritance and show the resulting MRO.

```python

class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

# D inherits from B and C, which both inherit from A
print(D.__mro__)
```

13. Create a class `Account` and manually add an attribute to its instance using the `__dict__` dictionary.

```python

class Account:
    def __init__(self, owner):
        self.owner = owner

acc = Account("Anurag")
# Injecting attribute directly into namespace
acc.__dict__['balance'] = 5000
print(f"Owner: {acc.owner}, Balance: {acc.balance}")
```

14. Write a script that defines a global variable and a function, then uses `globals()` to check if they exist in the global namespace.

```python

top_score = 100

def play(): pass

# Checking the global namespace keys
print('top_score' in globals())
print('play' in globals())
```

15. Create a `Manager` class that inherits from `Employee` and adds a list of subordinates. Use `super()` in the constructor.

```python

class Employee:
    def __init__(self, name):
        self.name = name

class Manager(Employee):
    def __init__(self, name, staff_list):
        super().__init__(name)
        self.subordinates = staff_list

m = Manager("Gupta", ["Alice", "Bob"])
print(m.name, "manages", m.subordinates)
```

16. Demonstrate "Replacement Is-A" where a `SilentPet` class overrides `speak()` to do absolutely nothing.

```python

class Pet:
    def speak(self):
        print("Some sound")

class SilentPet(Pet):
    def speak(self):
        # Replaces parent logic with a silent pass
        pass

s = SilentPet()
s.speak() # Nothing is printed
```

17. Use the `@property` decorator to create a "getter" for a `Circle` class that calculates area based on radius.

```python

import math

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        # Calculated attribute
        return math.pi * (self._radius ** 2)

c = Circle(5)
print(f"Area: {c.area:.2f}")
```

18. Implement a "Custom Container" using `__getitem__` to allow square bracket access to a `PetBox` class.

```python

class PetBox:
    def __init__(self, pets):
        self.pets = pets

    def __getitem__(self, index):
        # Allows access like: box[0]
        return self.pets[index]

box = PetBox(["Dog", "Cat", "Hamster"])
print(box[1]) # Output: Cat
```


19. Create a script that shows "Hierarchical Inheritance" with one parent `Weapon` and two children `Sword` and `Bow`.

```python

class Weapon:
    def attack(self): print("Attacking!")

class Sword(Weapon): pass
class Bow(Weapon): pass

s = Sword()
b = Bow()
s.attack()
b.attack()
```

20. Use `__slots__` to restrict a `Point` class to only have `x` and `y` attributes, preventing the creation of `__dict__`.

```python

class Point:
    # Memory optimization: no __dict__ created
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(10, 20)
print(p.x, p.y)
# Attempting p.z = 30 would now raise an AttributeError
```










