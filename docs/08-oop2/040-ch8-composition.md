



## Exploring Advanced “Has-A” Relationships in Python (Composition, Aggregation, Dependency)

----------

### Objective

In this exercise, you will:

-   Understand different forms of **Has-A relationships**
    
-   Implement **composition, aggregation, and dependency**
    
-   Analyse **ownership and lifecycle of objects**
    
-   Design a system using **Pet, Dog, Collar, and Toy classes**
    

### Problem Statement

You are required to design a small system involving pets and their accessories. 
Your implementation must demonstrate the following:

----------

#### PART A: Class Design

1.  Create the following classes:
    
    -   `Pet` (base class)
        
    -   `Dog` (derived from Pet)
        
    -   `Collar`
        
    -   `Toy`
        

----------

#### PART B: Composition (Strong Has-A)

2.  Implement **Composition** such that:
    
    -   A `Dog` **creates its own Collar internally**
        
    -   The Collar should NOT be passed from outside
        
    -   Add attributes to Collar (e.g., color)
        
    -   Provide a method in Collar to display its details
        

👉 Hint: Create Collar object inside `Dog.__init__()`

----------

#### PART C: Aggregation (Weak Has-A)

3.  Implement **Aggregation** such that:
    
    -   A `Toy` object is created **outside the Dog class**
        
    -   The `Dog` receives this Toy as a parameter
        
    -   Store the Toy inside Dog
        

Hint: Pass Toy as an argument to Dog constructor

----------

#### PART D: Dependency (Uses-A)

4.  Implement **Dependency** such that:
    
    -   Dog has a method that accepts a Toy as parameter
        
    -   Dog uses the Toy temporarily (without storing it)
        

Hint: Method like `play_with_toy(self, toy)`

----------

#### PART E: Functionality

5.  Your program must:
    
    -   Create at least:
        
        -   One Collar (internally via Dog)
            
        -   Two Toy objects (externally)
            
    -   Create a Dog object
        
    -   Demonstrate:
        
        -   Accessing Collar (composition)
            
        -   Accessing stored Toy (aggregation)
            
        -   Using another Toy temporarily (dependency)
            

----------

#### PART F: Conceptual Questions (Must Answer in Comments)

6.  Answer the following inside your code as comments:
    
    -   Why is Collar an example of composition?
        
    -   Why is Toy an example of aggregation?
        
    -   What makes dependency different from aggregation?
        
    -   What happens to:
        
        -   Collar if Dog is deleted?
            
        -   Toy if Dog is deleted?
            

----------

#### PART G: Advanced Task (Very Important)

7.  Modify your program so that:
    
    -   The same Toy is shared between **two Dog objects**
        
    -   Explain (in comments):
        
        -   What type of relationship this now represents
            
        -   Why it is not composition
            

----------

#### Expected Outcome

Your program should clearly demonstrate:

-   Strong ownership (composition)
    
-   Weak ownership (aggregation)
    
-   Temporary usage (dependency)
    

----------

### **ANSWER (SOLUTION)**


In the solution there are the following 4 classes:
  

| No. | Class | Concept |
| --- | --- | --- |
| -1 | Pet | Base class |
| -2 | Dog | Main class |
| -3 | Collar | Composition |
| -4 | Toy | Aggregation + Dependency |

#### The script is as follows:

```python

# A. CLASS DEFINITIONS

class Collar:  # Component class for composition
    def __init__(self, color):  #color is an attribute of Collar and not of Dog, so it is not passed from outside (composition)
        self.color = color

    def show(self):
        print(f"Collar color: {self.color}")

class Toy:  # Independent class for aggregation and dependency
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"Playing with {self.name}")

class Pet:  # Base class for inheritance
    def __init__(self, name):
        self.name = name


class Dog(Pet):  # Dog inherits from Pet (IS-A relationship)
    def __init__(self, name, toy):  # Constructor with parameters. toy is for aggregation (passed from outside)
        # Call parent constructor to initialize "name"
        super().__init__(name)  # Constructor chaining (IS-A relationship)

        # COMPOSITION (Strong Has-A)
        # Collar is created inside Dog
        # It is owned by Dog and not shared

        self.collar = Collar("Red")  # Composition (Collar is created inside Dog)

        # AGGREGATION (Weak Has-A)
        # Toy is passed from outside
        # Dog does not own the Toy

        self.toy = toy  # Aggregation (Toy can exist independently)

    def show_details(self):  # Method to demonstrate composition and aggregation
        print(f"Dog Name: {self.name}")

        # Composition usage
        print("Collar details (Composition):")
        self.collar.show()  # Accessing the composed object

        # Aggregation usage
        print("Toy details (Aggregation):")  
        print(f"Toy name: {self.toy.name}")  # Accessing the aggregated object (Toy)


    # DEPENDENCY (Uses-A)
    # Toy is used temporarily, not stored

    def play_with_toy(self, toy):  # Dependency (Uses-A)
        print(f"{self.name} is playing...")
        toy.play()  # Using the toy temporarily (dependency)


# B. MAIN PROGRAM

# 1. Creating toys externally (independent objects)
t1 = Toy("Ball")  # Toy created outside Dog (aggregation)
t2 = Toy("Bone")  # Another toy for dependency demonstration

# 2. Creating Dog with one toy (aggregation)
d1 = Dog("Tommy", t1)  # Dog created with a toy (aggregation)

# Demonstration
d1.show_details()  # Shows composition (Collar) and aggregation (Toy)

print("\nDependency Example:")
d1.play_with_toy(t2)  # Using a toy temporarily (dependency)

# 3. ADVANCED TASK: SHARING TOY

# Same toy shared between two dogs
d2 = Dog("Bruno", t1)  # Another dog created with the same toy (aggregation)

print("Shared Toy Example:")
print(d1.name, "has toy:", d1.toy.name)  # Accessing the toy of d1
print(d2.name, "has toy:", d2.toy.name)  # Accessing the toy of d2 (same toy as d1)


# C. CONCEPTUAL ANSWERS (AS COMMENTS)

# 1. Collar is composition because:
#    - It is created inside Dog
#    - It cannot exist independently (conceptually)

# 2. Toy is aggregation because:
#    - It is created outside Dog
#    - It can exist independently

# 3. Dependency vs Aggregation:
#    - Aggregation stores the object
#    - Dependency only uses it temporarily

# 4. If Dog is deleted:
#    - Collar is also deleted (strong ownership)
#    - Toy still exists (independent object)

# 5. Shared Toy:
#    - Same Toy used by multiple Dogs
#    - This is aggregation (not composition)
#    - Because ownership is not exclusive

```

### The following diagram shows the relationships between the classes for the above script

![Diagram](/resources/ch8-composition.png)










