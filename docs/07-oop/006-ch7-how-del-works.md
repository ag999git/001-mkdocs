

### How `del` command and **`__del__()`** work

To understand how `del` command and **`__del__()`** work, one needs to understand how objects are stored in Python.

·       In Python there are the objects that live in a specific location in memory (the "Heap").

·       **The Heap:** This is a large area of memory where the actual objects live. This is where the "Pet" data (name, breed, etc.) is stored.

·       **The Reference:** Is just a pointer (a label) stored in the "Stack" that tells Python where the object is.

·       **The Stack:** This is a small, fast area of memory. It stores the names of your variables (like p1 and p2). Think of it as a **list of pointers**.

·       **The "Link":** In Python, a variable in the Stack simply holds the memory address of the object in the Heap.

·       **The del Action**: When you call del p1, Python removes the entry from the Stack. The object in the Heap remains untouched until the very last link is snapped.

·       **Manual Deletion:** Suppose you have an object of **Pet** class named **p1** and an alias to **p1** named **p2**. When you type **del p1**, you aren't touching the memory space. You are just cutting the link (Think of a wire connecting the reference to object in heap) that connects the reference to that memory space. It is a common misconception that the del command deletes an object. It does not.

·       **Automatic Deletion:** The memory space is only reclaimed by the **Garbage Collector** when the object’s "Reference Count" drops to zero. So till both p1 and p2 are deleted the space occupied by the object will not be reclaimed by the Garbage collector.

*   **The del command:** This only removes a **label** (alias) from an object. It unbinds the name from the memory address.
*   **The `__del__()` method:** This is the **Destructor**. It is called by the Python interpreter only when the "Reference Count" of an object hits zero—meaning there are no more labels attached to it. So if you do del p1, \_\_del\_\_() wont be triggered because p2 exists. But once you also do del p2, then \_\_del\_\_() will be triggered automatically.
*   **The Difference between del and `__del__()`:** del is a manual action to remove a label (reference). `__del__()` is an automatic reaction by Python to remove the object from memory.
*   **The Zero-Threshold**: The Destructor (`__del__()`) is a "patient" method. It waits until the absolute last link is broken before it clears the memory.
*   You don't know exactly when `__del__()` will run. While it usually happens as soon as the count hits zero, Python's Garbage Collector might wait a few milliseconds if it's busy doing other things. This is why we call it Automatic Memory Management.

**Counting Aliases with** **sys.getrefcount()**:- In Python, the **sys.getrefcount(obj)** function returns the number of references to an object. Note that this function always returns a count one higher than you expect. This is because passing the object to the getrefcount() function itself creates a temporary alias inside the function.

The following script shows hoe del and `__del__()`work. To do reference counting we use sys.getrefcount() . So we have to import sys.

```python

import sys

class Pet:
    def __init__(self, name):
        self.name = name
        print(f"Pet object-> {self.name} allocated memory in the Heap")

    def __del__(self):  # Called automatically when reference count hits 0
        print(f"Reference count is 0. Memory for Pet {self.name} is freed")

# 1. Create the original object p1
p1 = Pet("Tiger")  # Reference count for "Tiger" is now 1
count = sys.getrefcount(p1) - 1  #Subtract 1 (temp ref in getrefcount())
print(f"Count on creating p1-> {count}")  # Count on creating p1-> 1

# 2. Create an alias of p1 as p2
p2 = p1  # Reference count for "Tiger" is now 2 (p1 and p2 both point to it)
print(f"Count after alias p2 (p1 + p2):-> {sys.getrefcount(p1) - 1}")

# 3. Delete the first reference p1
del p1 
# Note: __del__ will NOT be called here because p2 still exists.
print("p1 is gone, but the object survives because p2 still points to it.")
print(f"Object Count-> {sys.getrefcount(p2) - 1}")

# 4. Delete the second (final) reference p2
del p2 
# Note: NOW the __del__ method will trigger automatically.
print("End of script.")

```

The following table shows the status of reference count and the triggering of __del__() by the Python interpreter after p1 and p2 are created and deleted:-

  

| Action | What happens to the Reference Count? | Does __del__ run? |
| --- | --- | --- |
| p1 = Pet() | Count becomes 1. | No. |
| p2 = p1 | Count becomes 2. | No. |
| del p1 | Count becomes 1. | No. |
| del p2 | Count becomes 0. | Yes! Memory is released. |

The following figure shows how del and `__del__()` operate:


![Figure: How del works](/resources/ch07-oop-del.png)





#### Note about overriding __del__()

When you "override" __del__, you aren't replacing Python's ability to delete memory.

When the reference count hits zero, the following sequence takes place:

1.  **The Trigger:** is when the reference count for your object reaches zero. (Meaning all references to the object have been deleted.)
2.  **The User's Turn:** Python looks at your class. It sees you have overridden __del__. It calls your method first. This allows you to close files, log messages, or clean up your own data.
3.  **The System's Turn:** Once _your_ code in __del__ finishes running, Python’s internal **Garbage Collector** takes over. It performs the actual "low-level" work of clearing the bits and bytes from the RAM (the Heap).
4.  **You don't "kill" the process:** Overriding __del__ does not stop Python from reclaiming memory. It just allows you to "hook" into the moment right before it happens.
5.  **Automatic Execution:** You never have to manually call __del__. The interpreter handles the call automatically.
6.  **The Final Step:** Python's internal memory management is written in **C**. After your Python-level __del__ finishes, the C-level code (which you cannot override) actually wipes the memory address.






