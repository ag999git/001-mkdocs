




## Has-A Relationships (Composition, Aggregation, Dependency)

----------

### 1. Introduction

In object-oriented design, not all relationships are hierarchical (Is-A).  
Very often, objects are **built using other objects**. This leads to:

> **Has-A relationships**

However, not all Has-A relationships are the same. They differ based on:

-   **Ownership**
    
-   **Object creation**
    
-   **Object lifetime**
    
-   **Degree of dependency**
    

----------

### 2. The Three Types of Has-A Relationships

----------

#### 2.1 Composition (Strong Has-A Relationship)

##### Definition

> Composition is a relationship where one class **strongly owns** another class, and the contained object **cannot logically exist independently** of the owner.

----------

##### Key Characteristics

-   Object is **created inside the class**
    
-   Strong ownership
    
-   Not shared with other objects
    
-   Lifetime is **dependent on the owner**
    
-   Represents a **whole–part relationship**
    

----------

##### Conceptual Example

> A **Dog has a Collar**

-   Collar is tightly linked to Dog
    
-   If Dog is removed → Collar is also removed (conceptually). So in a Strong Has-A Relationship, the object of class Collar is created inside the object of class Dog and it dies with the Dog object.
    


#### Strong Relationship (Composition)

-   Whole **controls the lifecycle** of part
    
-   Part has **no independent identity**
    
-   Tight coupling
    

Example:

> Collar belongs only to one Dog



----------

##### Interpretation

>“Built inside, owned completely”



----------

#### 2.2 Aggregation (Weak Has-A Relationship)

##### Definition

> Aggregation is a relationship where one class **uses or contains another class**, but the contained object **exists independently**.

----------

##### Key Characteristics

-   Object is **created outside the class**
    
-   Weak ownership
    
-   Can be shared among multiple objects
    
-   Lifetime is **independent**
    
-   Represents a **container–content relationship**
    

----------

##### Conceptual Example

> A **Dog has a Toy**

-   Toy exists independently
    
-   Same Toy can be used by multiple Dogs. So in a Weak Has-A Relationship, the object of Toy class has an existence independent of the object of Dog class. The object of Toy class does not die with the object of the Dog class
    

----------

##### Interpretation

>“Received from outside, not owned”



#### Weak Relationship (Aggregation)

-   Whole does **not control lifecycle**
    
-   Part has **independent identity**
    
-   Loose coupling
    

Example:

> Toy can exist without Dog

#### When to Use Aggregation

-   When objects are **loosely related**
    
-   When reuse and sharing is required



----------

#### 2.3 Dependency (Uses-A Relationship)

##### Definition

> Dependency is a relationship where one class **temporarily uses another class** without storing or owning it.

----------

##### Key Characteristics

-   Object is **used temporarily**
    
-   Not stored as attribute
    
-   Very weak relationship
    
-   Exists only during method execution
    
-   No ownership
    

----------

##### Conceptual Example

> A **Dog uses a Toy to play**

-   Toy is passed as a parameter
    
-   Used only within method
    

----------

##### Interpretation

“Used when needed, then forgotten”

----------


#### When to Use Dependency

-   When object is needed **only for a task**
    
-   Avoid unnecessary storage

#### 3. Comparative Table


  

  

| Feature | Composition (Strong) | Aggregation (Weak) | Dependency (Very Weak) |
| --- | --- | --- | --- |
| Relationship type | Strong Has-A | Weak Has-A | Uses-A |
| Ownership | Strong | Weak | None |
| Object creation | Inside class | Outside class | Outside class |
| Lifetime dependency | Dependent | Independent | Independent |
| Sharing | Not shared | Can be shared | Not relevant |
| Storage | Stored as attribute | Stored as attribute | Not stored |
| Duration | Permanent | Long-term | Temporary |
| Coupling | High | Medium | Low |
| Example | Dog–Collar | Dog–Toy | Dog uses Toy |
| Destruction effect | Part destroyed with whole | Part survives | No effect |












