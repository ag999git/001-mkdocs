




### Design a `Pet` class to demonstrate:

-   Instance Method
-   Class Method (Factory Method)
-   Static Method (Utility Function)

----------

#### Instructions

1.  Create a class named `Pet`
2.  Use variables:
    -   `name`
    -   `age`
    -   `species = "Animal"`



#### Required Methods

Method Name

Type

`show()`

Instance

`create_from_string()`

Class Method

`is_valid_age()`

Static Method

----------

#### Hints

-   Use:

`@classmethod  `
`@staticmethod`

-   Input format for factory:

"Tommy-5"

----------

#### Dos and Don’ts

 - Use `cls` in class method   
 - Use no parameter in static method except
   inputs   
   Do not use `self` in static method



### Answer - Explanation

-   Instance methods operate on object data using `self`.
-   Class methods operate on class using `cls` and can create objects.
-   Static methods are utility functions and do not depend on class or object.

----------

#### Table


  

| Method Type | First Parameter | Purpose | Example |
| --- | --- | --- | --- |
| Instance | self | Works on object | show() |
| Class | cls | Factory creation | create_from_string() |
| Static | None | Utility | is_valid_age() |



#### The script is as follows

```python

# This script defines the Pet class with (1) class attribute  "species", (2) instance attributes "name" and "age", 
# and (3) classmethod "create_from_string" and (4) static method "is_valid_age". 
# The class also has a (5) method "show" to display the attributes.
# The class method creates an instance using "create_from_string" to create an instance from a string, 
# The static method checks if an age is valid (non-negative). 
# Finally, we test the class by creating instances using both the constructor and the class method, and 
# we check the validity of ages using the static method.

# A. Define the Pet class
class Pet:  
    species = "Animal"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"{self.name}, {self.age}, {Pet.species}")

    # B. Class method to create an instance from a string
    @classmethod
    def create_from_string(cls, data):  # This line defines a class method called create_from_string. The @classmethod decorator indicates that this method is a class method, which means it receives the class (cls) as the first argument instead of an instance (self). The data parameter is expected to be a string in the format "name-age". Inside the method, we split the input string using the hyphen as a delimiter to extract the name and age. We then convert the age from a string to an integer and return a new instance of the Pet class using cls(name, int(age)). This allows us to create a Pet object directly from a formatted string, providing an alternative constructor for our class.
        name, age = data.split("-")  # This line splits the input string data into two parts using the hyphen as a delimiter. The split() method returns a list of substrings, and we unpack it into the variables name and age. For example, if data is "Bruno-3", then name will be "Bruno" and age will be "3" (as a string). This allows us to extract the necessary information to create a new Pet instance in the next step.
        return cls(name, int(age))  # This line creates and returns a new instance of the Pet class using the cls parameter, which refers to the class itself. We pass the name and age (converted to an integer) as arguments to the constructor of the Pet class. This allows us to create a Pet object directly from a formatted string, providing an alternative way to instantiate our class without having to call the constructor directly with separate arguments.

    # C. Static method to check if an age is valid
    @staticmethod
    def is_valid_age(age):  # This line defines a static method called is_valid_age. The @staticmethod decorator indicates that this method does not receive an implicit first argument (neither self nor cls) and is not bound to the class or instance
        return age >= 0  # This line checks if the provided age is valid by ensuring it is greater than or equal to 0. The method returns True if the age is valid (non-negative) and False otherwise. This static method can be called without needing an instance of the Pet class, making it a convenient utility function for validating ages in various contexts.


# D. Testing
p1 = Pet("Tommy", 5)  # This line creates an instance of the Pet class using the constructor. We pass the name "Tommy" and the age 5 as arguments to the constructor, which initializes the instance attributes accordingly.
p1.show()  # Output: Tommy, 5, Animal. This line calls the show() method on the p1 instance, which prints the name, age, and species of the pet in a formatted string.

p2 = Pet.create_from_string("Bruno-3")  # This line creates an instance of the Pet class using the class method create_from_string. We pass the string "Bruno-3" as an argument, which is processed by the class method to extract the name and age, and then a new Pet instance is created with those values. This demonstrates how we can use a class method as an alternative constructor to create instances from different types of input.
p2.show()  # Output: Bruno, 3, Animal. This line calls the show() method on the p2 instance, which prints the name, age, and species of the pet in a formatted string.

print(Pet.is_valid_age(5))  # Output: True. This line calls the static method is_valid_age on the Pet class, passing the age 5 as an argument. The method checks if 5 is a valid age (non-negative) and returns True, which is then printed to the console.
print(Pet.is_valid_age(-1))  # Output: False. This line calls the static method is_valid_age on the Pet class, passing the age -1 as an argument. The method checks if -1 is a valid age (non-negative) and returns False, which is then printed to the console.

```


#### Step by Step explanation

1.  Constructor initializes object
2.  Instance method accesses object data
3.  Class method:
    -   Parses string
    -   Creates object using `cls`
4.  Static method:
    -   Validates age independently



















