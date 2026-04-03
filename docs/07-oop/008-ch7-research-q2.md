


### Research Question 2: Compare and contrast Shallow Copy and Deep Copy. When should a programmer use one over the other when working with nested objects (like a list of Pet objects)?

**Answer:**

In Python, the copy module provides two ways to duplicate data:

1.  **Shallow Copy (`copy.copy()`):** It creates a new collection object, but it fills it with **references** to the same child objects. If you change a pet's name in the copy, it changes in the original too.
2.  **Deep Copy (`copy.deepcopy()`):** It creates a new collection **and** recursively creates new copies of every object found inside. It is a total, independent clone.



  

| Feature | Shallow Copy | Deep Copy |
| --- | --- | --- |
| New Container? | Yes | Yes |
| New Inner Objects? | No (Shared) | Yes (Independent) |
| Performance | Fast | Slower (More memory) |


The following script shows the difference between shallow copy and deep copy:-


```python

import copy

class Pet:
    def __init__(self, name):
        self.name = name

# 1. Create original list of pets
dog = Pet("Tiger")
original_shelter = [dog]

# 2. Perform Shallow Copy
# This copies the LIST, but points to the SAME 'Tiger' object in memory.
shallow_shelter = copy.copy(original_shelter)

# 3. Perform Deep Copy
# This copies the LIST AND creates a BRAND NEW 'Tiger' object.
deep_shelter = copy.deepcopy(original_shelter)

print(f"Original Name: {dog.name}")
print("-" * 30)

# 4. THE TEST: Change the original dog's name
print("ACTION: Changing Tiger's name to 'Sheru' in the original list...")
dog.name = "Sheru"

# 5. Check the results
# Shallow copy 'sees' the change because it shares the same memory address.
print(f"Shallow Copy result: {shallow_shelter[0].name} (Points to same memory)")

# Deep copy 'stays' the same because it is a completely independent clone.
print(f"Deep Copy result:    {deep_shelter[0].name} (Is a separate object)")

# PROOF using id()
print(f"\nOriginal ID: {id(original_shelter[0])}")
print(f"Shallow ID:  {id(shallow_shelter[0])} -> Identical to Original")
print(f"Deep ID:     {id(deep_shelter[0])} -> Different from Original")



```









