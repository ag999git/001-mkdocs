
## Write a regexp which places certain restrictions on a password that a user may select



### Problem:- Write a regexp which places the following restrictions on a password that a user may select:-

The password should have the following:-

-  At least one small alphabet ie [a-z]

-  At least one large (capital) alphabet ie [A-Z]

-  At least one digit ie [0-9]

-  At least one special character from [!@#$%^&*]

-  The password should have a minimum length of 6 and maximum of 12 characters


## The script is as follows:-


```python
import re

# Complete password validation pattern
password_pattern = (
    r'^'                    # Start of string
    r'(?=.*[a-z])'           # At least one lowercase letter
    r'(?=.*[A-Z])'           # At least one uppercase letter
    r'(?=.*[0-9])'           # At least one digit
    r'(?=.*[!@#$%^&*])'      # At least one special character
    r'[A-Za-z0-9!@#$%^&*]'   # Allowed characters
    r'{6,12}$'               # Length between 6 and 12
)

# List of test passwords
test_passwords = [
    #  Valid passwords
    "Ab1@xy",
    "Good1@Pwd",
    "Xy9#Ab",
    "Pass1$word",
    "Z9@abc",

    #  Invalid passwords
    "abc123@",          # No uppercase letter
    "ABC123@",          # No lowercase letter
    "Abcdef@",          # No digit
    "Ab1xyz",           # No special character
    "Ab1@x",            # Too short
    "Ab1@xyzabcdef",    # Too long
    "Ab1@xy!",          # Too long (7 but extra special allowed? no length OK — keep for discussion)
    "Ab1@xy ",          # Contains space
    "Ab1@xy?",          # Invalid special character '?'
    "123@ABC",          # No lowercase
]

# Validate each password
for pwd in test_passwords:
    if re.match(password_pattern, pwd):
        print(f"{pwd:15} → GOOD")
    else:
        print(f"{pwd:15} → BAD")

```


```python
Ab1@xy          → GOOD
Good1@Pwd       → GOOD
Xy9#Ab          → GOOD
Pass1$word      → GOOD
Z9@abc          → GOOD
abc123@         → BAD
ABC123@         → BAD
Abcdef@         → BAD
Ab1xyz          → BAD
Ab1@x           → BAD
Ab1@xyzabcdef   → BAD
Ab1@xy!         → GOOD
Ab1@xy          → BAD
Ab1@xy?         → BAD
123@ABC         → BAD

```




## 1. Detailed explanation of the RegEx Pattern

**The RegEx Pattern used is as follows**

```python
password_pattern = (
    r'^'                    # Start of string
    r'(?=.*[a-z])'           # At least one lowercase letter
    r'(?=.*[A-Z])'           # At least one uppercase letter
    r'(?=.*[0-9])'           # At least one digit
    r'(?=.*[!@#$%^&*])'      # At least one special character
    r'[A-Za-z0-9!@#$%^&*]'   # Allowed characters
    r'{6,12}$'               # Length between 6 and 12
)
```



### The Anchors (`^` and `$`)

-   `^`: Forces the match to start at the very beginning of the string.
    
-   `$`: Forces the match to end at the very last character. Without these, the regex might match a valid _substring_ inside an otherwise invalid password.
    

### The Lookahead Assertions `(?=...)`

There are 4 look ahead assertions, namely:

```python
r'(?=.*[a-z])'           # At least one lowercase letter
r'(?=.*[A-Z])'           # At least one uppercase letter
r'(?=.*[0-9])'           # At least one digit
r'(?=.*[!@#$%^&*])'      # At least one special character
```
These four blocks are the **"requirements checklist."** They all start with `(?=.*...)`.

-   `(?= )`: This is the syntax for a **Positive Lookahead**.
    
-   `.*`: This means "skip over any number of characters." This allows the required character to appear anywhere in the string (start, middle, or end).

| Regex Snippet | Requirement |
| --- | --- |
| (?=.*[a-z]) | Peeks ahead to find at least one lowercase letter. |
| (?=.*[A-Z]) | Peeks ahead to find at least one uppercase letter. |
| (?=.*[0-9]) | Peeks ahead to find at least one digit. |
| (?=.*[!@#$%^&*]) | Peeks ahead to find at least one special character from the set. |


### The Character Set and Quantifier

`[A-Za-z0-9!@#$%^&*]{6,12}` Once the lookaheads are satisfied, the engine returns to the start of the string and actually **matches** the characters:

-   `[...]`: Defines the **allowed characters**. If the password contains a space or a `?`, it will fail here because those characters aren't in this list.
    
-   `{6,12}`: This is the **Quantifier**. It specifies that the total length of the string must be at least 6 and no more than 12 characters.
    

----------

## 2. Why is it structured this way?

If you tried to write this without lookaheads, you would have to account for every possible permutation (e.g., "digit first, then letter" or "letter first, then special char"). That would result in a massive, unreadable regex.

**Lookaheads allow us to "stack" conditions independently.** The engine checks condition 1, resets to the start; checks condition 2, resets to the start; and so on.

----------

## 3. Detailed Breakdown of a "BAD" Match

Let's look at why `"Ab1xyz"` fails:

1.  `^`: Start at index 0.
    
2.  `(?=.*[a-z])`: Looks ahead, finds 'b'. **Pass.**
    
3.  `(?=.*[A-Z])`: Looks ahead, finds 'A'. **Pass.**
    
4.  `(?=.*[0-9])`: Looks ahead, finds '1'. **Pass.**
    
5.  `(?=.*[!@#$%^&*])`: Looks ahead through the entire string. **No special character found.**
    
6.  **FAIL:** The engine stops because one of the requirements wasn't met.



















