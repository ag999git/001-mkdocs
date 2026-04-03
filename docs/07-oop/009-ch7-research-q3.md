


### **Research Question 3:**Define a **Memory Leak** in the context of a Python application. Since Python has an automatic Garbage Collector, how is it still possible for a memory leak to occur?

**Answer:**

A **Memory Leak** happens when a program retains memory that it no longer needs. Even with an automatic "Janitor" (Garbage Collector), leaks happen in Python when:

-   **Forgotten References:** You accidentally keep adding objects to a global list or dictionary and forget to remove them.
-   **Complex Circular References:** While Python can catch most circular links, certain complex objects (especially those involving __del__ in older Python versions) can confuse the collector.
-   **Result:** The RAM usage of your program keeps growing (leaking) until the computer runs out of memory and the program crashes.




