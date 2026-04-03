

### The "Same Address" Experiment


In Python, every object created is stored at a specific unique address in the computer's memory. 

The `id()` function returns this "memory address." 
The address of the object outside the class is **identical** to the address of `self` inside the class. 
This shows that `self` isn't some magical Python command—it is literally just a nickname for the object itself.

Here is a script that proves that an object created has same id as `self`.

```python

# This code demonstrates how the 'self' parameter in a class method refers to 
# the specific instance of the class that is calling the method. 
# Each object (instance) of the class has its own unique ID, 
# and when we call a method on that object, 'self' refers to that particular instance.

class Pet:
    def __init__(self, name):
        self.name = name

    def show_id(self):  # This method will show the ID of the instance that is calling it
        # This will print the ID of whichever object is 'acting' right now
        print(f"Inside method for {self.name}, id(self) is: {id(self)}")

# --- Creating Two Separate Objects ---
p1 = Pet("Tiger")  # This creates the first object 'p1' of class Pet with name "Tiger"
p2 = Pet("Kittie")  # This creates the second object 'p2' of class Pet with name "Kittie"

# --- Checking Pet 1 ---
print(f"Outside class, id(p1) is: {id(p1)}")  # This will print the ID of the object 'p1' outside the class
p1.show_id() # This will call the method 'show_id' on 'p1', and inside that method, 'self' will refer to 'p1', so it will print the ID of 'p1'

print("-" * 30)

# --- Checking Pet 2 ---
print(f"Outside class, id(p2) is: {id(p2)}")  # This will print the ID of the object 'p2' outside the class
p2.show_id()  # This will call the method 'show_id' on 'p2', and inside that method, 'self' will refer to 'p2', so it will print the ID of 'p2'


```







