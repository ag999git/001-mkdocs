


## Part 1: 30 Conceptual Questions & Answers

**1. What is the fundamental goal of inheritance in Python?** 

The primary goal of inheritance is code reusability. It allows a child class to reuse and extend the logic written in a parent class without rewriting it.

**2. Which built-in class sits at the very top of the Python class hierarchy?** 

The object class is the root of all classes in Python. Every class created automatically inherits from it.

**3. Define the "Is-A" relationship in the context of OOP.** 

An "Is-A" relationship is a structural link where a subclass is a specific type of its superclass (e.g., a Dog is-a Pet).

**4. What happens if you define a child class using the pass keyword?** 

The child class becomes an exact clone of the parent class, inheriting all its attributes and methods without adding or changing anything.

**5. What is the difference between Single Inheritance and Multiple Inheritance?** 

Single inheritance involves one parent class, whereas multiple inheritance allows a child class to inherit from more than one immediate parent class.

**6. Explain the concept of "Transitivity" in inheritance.** 

Transitivity means that if Class B inherits from Class A, and Class C inherits from Class B, then Class C automatically possesses the traits of Class A.

**7. What is Method Overriding?** 

Overriding occurs when a child class changes the implementation of a specific method inherited from the parent class to suit its own needs.

**8. What does MRO stand for, and what is its purpose?** MRO stands for Method Resolution Order. It is the deterministic order in which Python searches for a method or attribute through the class hierarchy.

**9. In a standard class hierarchy, where does the MRO search always end?** The MRO search always ends at the built-in object class.

**10. What is the default behavior of the __str__ method inherited from the object class?** 

It returns a string containing the class name and the memory address of the object (e.g., <ClassName object at 0x...>).

**11. Why is the super() function used?** 

super() is used to call methods from the parent class (or the next class in the MRO) from within the child class, allowing for code reuse and refinement.

**12. Does super() always call the immediate parent class?** 

Not necessarily. In multiple inheritance, super() follows the Method Resolution Order (MRO), which might lead to a "sibling" class before a parent.

**13. What is the "Depth-First, Left-to-Right" rule?** 

It is the basic logic Python uses to search for methods in multiple inheritance: it searches the leftmost parent and its entire ancestry before moving to the next parent on the right.

**14. What is a "Namespace" in Python?** 

A namespace is a container (technically a dictionary) that maps variable names (keys) to their corresponding objects (values).

**15. List the four levels of the LEGB rule for namespaces.** 

The levels are Local, Enclosing, Global, and Built-in.

**16. What information do the locals() and globals() functions provide?** 

They return dictionaries containing all the variables available in the current local and global scopes, respectively.

**17. How can you access the namespace dictionary of a class or an instance?** 

You can access it using the __dict__ attribute.

**18. Are the namespaces of a Class and its Instance the same?** 

No. A class has its own namespace (containing class variables and methods), and each instance has its own separate namespace (containing instance-specific attributes).

**19. Define "Composition" (the "Has-A" relationship).** 

Composition is when one class contains an instance of another class as an attribute, implying ownership rather than a type relationship (e.g., a Dog has-a Collar).

**20. What is an Abstract Method?** 

An abstract method is a placeholder method declared in a parent class that has no implementation; it forces subclasses to provide their own specific logic.

**21. How do you informally create an abstract method in Python?** 

By defining a method in the parent class that simply contains raise NotImplementedError("message").

**22. What is "Multilevel Inheritance"?** 

It is a chain of inheritance where a class is derived from another derived class (e.g., Grandchild inherits from Child, who inherits from Parent).

**23. What is "Hierarchical Inheritance"?** 

It is a structure where one single parent class serves as the base for multiple different subclasses.

**24. Explain "Cooperative Is-A" (Refinement).** 

It is a pattern where a child class uses super() to let the parent handle part of a task, while the child adds its own specialized logic on top.

**25. What is "Replacement Is-A" (Total Overriding)?** 

It is when a child class completely ignores the parent's logic for a method and provides a totally different implementation.

**26. Why would a developer use Admin(User): pass?** 

This is an "Implicit Is-A" (Pass-through) used to create semantic roles in code, even if the data structure remains the same as the parent.

**27. What happens if a child class defines an __init__ method but does not call super().__init__?** 

The parent’s constructor is never called, and any attributes initialized in the parent class will not exist in the child object.

**28. How does Python link variable names to objects internally?** 

Python identifies each object with a unique id() and maps the variable name to that ID within a namespace dictionary.

**29. What is the benefit of Composition over Inheritance?** 

Composition offers more flexibility because it allows combining functionalities from multiple sources without the rigid restrictions of a class hierarchy.

**30. What is "Hybrid Inheritance"?** 

Hybrid inheritance is a combination of two or more types of inheritance (e.g., mixing multiple and multilevel inheritance).







