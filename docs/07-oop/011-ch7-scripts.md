
## Scripting Questions

_Focusing on implementation, constructors, and methods._

**Q1. Create a class `Car` with a constructor that takes `brand` and `model`. Instantiate two different cars.**

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Tata", "Nexon")
car2 = Car("Mahindra", "XUV700")

```

**Q2. Add a class variable `wheels = 4` to the `Car` class and print it using the Class name.**
```python

class Car:
    wheels = 4
print(Car.wheels)

```

**Q3. Write a method `start_engine` that prints "The [brand] [model] engine is running."**

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def start_engine(self):
        print(f"The {self.brand} {self.model} engine is running.")

my_car = Car("Toyota", "Camry")
my_car.start_engine()

```

**Q4. Create a `Student` class where the `age` has a default value of 18.**


```python
class Student:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

s1 = Student("Anil") # Uses 18
s2 = Student("Sunita", 20) # Overrides with 20

```

**Q5. Implement a `Bank` class with a private attribute `__balance`. Create a method to check the balance.**


```python
class Bank:
    def __init__(self, amount):
        self.__balance = amount # Private attribute
    def get_balance(self):
        return f"Current Balance: {self.__balance}"

account = Bank(5000)
print(account.get_balance())

```

**Q6. Write a script to count how many `User` objects have been created using a class variable.**


```python
class User:
    count = 0
    def __init__(self):
        User.count += 1

u1 = User()
u2 = User()
print(f"Total Users: {User.count}")

```

**Q7. Create a method `update_email` that takes a new email and updates the instance attribute.**


```python
class User:
    def __init__(self, email):
        self.email = email
    def update_email(self, new_email):
        self.email = new_email

user = User("test@old.com")
user.update_email("test@new.com")

```

**Q8. Script an example of Operator Overloading using `+` for two strings.**


```python
x, y = "Python", "999"
result = x + y # Overloaded for concatenation
print(result) # Python999

```

**Q9. Create a static method `info()` that prints "This is a utility class for Math."**


```python
class MyMath:
    @staticmethod
    def info():
        print("This is a utility class for Math.")

MyMath.info()

```

**Q10. Use the `__dict__` attribute to print all attributes of a `Pet` object.**



``` python
p = Pet("Tiger", "Dog")
print(p.__dict__) 

```

**Q1. Write a class `Product` with `price` and a method `apply_discount(percent)` that changes the price.**


``` python
class Product:
    def __init__(self, price):
        self.price = price
    def apply_discount(self, percent):
        self.price -= self.price * (percent / 100)

p = Product(100)
p.apply_discount(10) # Price becomes 90

```

**Q12. Demonstrate what happens when you redefine a function name in Python.**


``` python
def check(): print("First")
def check(): print("Second")
check() # Output: Second (First is forgotten)

```

**Q13. Create a class `Circle` that takes `radius` and has a method `area`. (Use 3.14).**


``` python
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * (self.radius ** 2)

```

**Q14. Write a script where an object attribute is initialized inside `__init__` but not passed as a parameter.**


``` python
class Game:
    def __init__(self, player_name):
        self.player_name = player_name
        self.score = 0 # Default starting score

g = Game("Arjun")
print(g.score) # 0

```

**Q15. Create a class `Temperature` and use a setter method to ensure the temperature cannot be below Absolute Zero (-273.15°C).**


``` python
class Temperature:
    def __init__(self, celsius):
        self.set_temp(celsius)
    def set_temp(self, celsius):
        if celsius < -273.15:
            self.celsius = -273.15
        else:
            self.celsius = celsius

t = Temperature(-500)
print(t.celsius) # Output: -273.15

```

----------


