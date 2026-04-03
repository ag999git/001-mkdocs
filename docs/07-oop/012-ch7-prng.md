



#### Research / Study Question

**Topic: Cryptographic Vulnerability in Pseudorandom Number Generators (PRNGs)**

> **Question:** "In the context of the Linear Congruential Generator (LCG), how does the mathematical relationship between successive outputs $(X_n, X_{n+1}, X_{n+2})$ allow an observer to reverse-engineer hidden parameters like the multiplier ($a$) and increment ($c$)? Discuss the implications of this predictability for security-sensitive applications and demonstrate the 'break' using a Python-based reconstruction script."

----------

#### Answer

**The Mathematical Vulnerability**

The LCG relies on a simple linear equation:

$$X_{n+1} = (a \cdot X_n + c) \pmod m$$

Because this is a linear relationship, knowing just a few consecutive outputs allows us to set up a system of equations.

1.  **Finding $c$ (Multiplier $a$ and Modulus $m$ are known):**
    
    If we have two consecutive numbers, $X_0$ and $X_1$, we can rearrange the formula:
    
    $$c \equiv (X_1 - a \cdot X_0) \pmod m$$
    
    In Python, we use the modulo operator `%` to ensure $c$ stays within the range $[0, m-1]$.
    
2.  **Finding $a$ and $c$ (Only Modulus $m$ is known):**
    
    With three consecutive numbers ($X_0, X_1, X_2$), we have:
    
    1.  $X_1 \equiv a \cdot X_0 + c \pmod m$
        
    2.  $X_2 \equiv a \cdot X_1 + c \pmod m$
        
    
    Subtracting (1) from (2) eliminates $c$:
    
    $$X_2 - X_1 \equiv a(X_1 - X_0) \pmod m$$
    
    To find $a$, we need to multiply $(X_2 - X_1)$ by the **Modular Multiplicative Inverse** of $(X_1 - X_0)$.
    
    _Note: In your original hint, simple division $(X_2 - X_1) / (X_1 - X_0)$ only works in standard algebra. In modular arithmetic, we must use `pow(diff_x, -1, m)`._
    

### **Implications**

This research shows that LCG is **not cryptographically secure**. If an attacker can see just three random values (like three session IDs or three "random" passwords), they can predict every future value the system will ever generate.

----------

#### 3. The Python Script (The "LCG Breaker")

This script implements the LCG class and then uses two "Breaker" functions to recover the hidden parameters.


```python

class LCG:
    def __init__(self, seed, a=1103515245, c=12345, m=2**31):
        self.state = seed
        self.a = a
        self.c = c
        self.m = m

    def next(self):
        self.state = (self.state * self.a + self.c) % self.m
        return self.state

# --- ASSIGNMENT SOLUTIONS ---

def break_lcg_find_c(x0, x1, a, m):
    """Assignment 1: Recovers c when a and m are known"""
    c = (x1 - a * x0) % m
    return c

def break_lcg_find_a_and_c(x0, x1, x2, m):
    """Assignment 2: Recovers a and c when only m is known"""
    # Formula: (X2 - X1) = a * (X1 - X0) (mod m)
    diff_y = (x2 - x1) % m
    diff_x = (x1 - x0) % m
    
    # To solve for 'a', we find the modular inverse of diff_x
    # Python 3.8+ handles this with pow(val, -1, mod)
    try:
        inv_diff_x = pow(diff_x, -1, m)
        recovered_a = (diff_y * inv_diff_x) % m
        recovered_c = (x1 - recovered_a * x0) % m
        return recovered_a, recovered_c
    except ValueError:
        return None, "Inverse does not exist (GCD != 1)"

# --- TESTING THE ATTACK ---

# Known outputs from the user's list
outputs = [829870797, 1533044610, 1478614675]
m_val = 2**31
a_val = 1103515245

print("--- Assignment 1: Finding C ---")
found_c = break_lcg_find_c(outputs[0], outputs[1], a_val, m_val)
print(f"Recovered c: {found_c}")

print("\n--- Assignment 2: Finding A and C ---")
found_a, found_c2 = break_lcg_find_a_and_c(outputs[0], outputs[1], outputs[2], m_val)
print(f"Recovered a: {found_a}")
print(f"Recovered c: {found_c2}")


```












