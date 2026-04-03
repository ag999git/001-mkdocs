


**Q1. What is the fundamental difference between a Class and an Object?**

**Answer:** A **Class** is a blueprint or a logical template (e.g., the concept of a "`Pet`"), while an **Object** is a physical instance of that blueprint (e.g., a specific dog named "`Tiger`"). The class defines the structure; the object holds the actual data.

**Q2. Why does Python use the self parameter in methods?**

**Answer:** Since a class can have many instances, self is the bridge that tells Python _which_ specific object is calling the method. It allows the code to access the unique attributes (like self.name) of that particular instance.

**Q3. Does Python support "True" Function Overloading? Explain.**

**Answer:** No. In Python, if you define two functions with the same name, the second one replaces the first. We achieve "overloading-like" behavior using default arguments or variable-length arguments (`*args`).

**Q4. What is "Name Mangling" in Python and how is it triggered?**

**Answer:** Name mangling is Python's way of protecting data. It is triggered by prefixing an attribute with double underscores (e.g., __price). Python internally renames it to `_ClassName__attribute` to make it harder to access from outside the class.

**Q5. Explain the purpose of the `__init__` method.**

**Answer:** It is the "Constructor." It is automatically called when an object is created to initialize the object's attributes with specific values.

**Q6. What is the difference between a Class Variable and an Instance Variable?**

**Answer:** A **Class Variable** (e.g., `count`) is shared by all instances of the class. An **Instance Variable** (e.g., `self.name`) is unique to each individual object.

**Q7. What is a "Dunder" method? Provide an example from your chapter.**

**Answer:** "Dunder" stands for Double Under (underscore). These are special methods like `__init__` or `__str__` that have pre-defined meanings in Python’s OOP logic.

**Q8. How does a Static Method differ from an Instance Method?**

**Answer:** An instance method requires self and acts on a specific object. A static method (decorated with `@staticmethod`) does not take self and behaves like a regular function that is logically grouped within the class.

**Q9. What is Abstraction in the context of your "Pet" example?**

**Answer:** Abstraction is picking only the relevant details. For a vet clinic, we care about the pet's species and age, but we "abstract away" (ignore) irrelevant details like the pet's favorite toy color.

**Q10. What happens if you forget to include `self` in a method definition?**

**Answer:** If you call that method on an instance (e.g., `my_dog.bark()`), Python will throw a `TypeError`, stating that the method takes 0 positional arguments but 1 was given (because Python always passes the instance automatically).

**Q11. What is encapsulation in Python?

**Answer:**  
Encapsulation is the process of **wrapping data (variables) and methods (functions) together into a single unit (class)** and restricting direct access to some of the object’s components.

**Q12. What is the "Top-Down" vs "Bottom-Up" approach?** **Answer:** POP (Procedure-Oriented) is Top-Down, focusing on the sequence of steps/functions. OOP is Bottom-Up, focusing on building independent objects that interact with each other.

**Q13. Can a Class Attribute be accessed without creating an object?**

**Answer:** Yes. You can access it using the class name directly (e.g., Pet.species).

**Q14. What is the role of a "Decorator" like @staticmethod?** **Answer:** A decorator modifies the behavior of the function following it. @staticmethod tells Python not to pass the instance (self) to that method automatically.

**Q15. Why is OOP better for "Large, complex applications" compared to POP?** 
**Answer:** OOP allows for modularity, easier debugging through encapsulation, and code reuse through inheritance, making it more scalable than a long list of procedural functions.


**Q16. Why is encapsulation important?**
**Answer:**  Encapsulation helps to:

-   Protect data from accidental modification
    
-   Improve code security
    
-   Achieve data hiding
    
-   Make code more modular and maintainable

**Q17. How is encapsulation implemented in Python?**

**Answer:**  
Encapsulation is implemented using:

-   **Classes** to bundle data and methods
    
-   **Access specifiers (by convention):**
    
    -   Public (`name`)
        
    -   Protected (`_name`)
        
    -   Private (`__name`)

**Q18. What is the difference between public, protected, and private members?**

**Answer:**

| Type | Syntax | Accessibility |
| --- | --- | --- |
| Public | name | Accessible everywhere |
| Protected | _name | Accessible within class and subclasses |
| Private | __name | Accessible only within the class (name mangled) |

**Q19. What is name mangling in Python?**

**Answer:**  
Name mangling is a mechanism where Python internally changes the name of private variables:

`__var  →  _ClassName__var`

This prevents accidental access from outside the class.

**Q20. Does Python truly enforce data hiding?**

**Answer:**  
No, in Python even private members can still be accessed (though not recommended), e.g.:

`obj._ClassName__var`

**Q21. What is the difference between encapsulation and abstraction?**
**Answer**

| Encapsulation | Abstraction |
| --- | --- |
| Hides data | Hides implementation details |
| Focus on data protection | Focus on functionality |
| Achieved using classes | Achieved using abstract classes/interfaces |

**Q22. What is the role of @property in encapsulation?**

**Answer:**  
`@property` allows methods to be accessed like attributes, improving readability and control.
The following script shows this:

```python

class Student:
    def __init__(self):
        self.__marks = 0

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if value >= 0:
            self.__marks = value


```





