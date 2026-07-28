
## Conceptual questions on Regular Expression (re)

###  Beginner Level



#### **Q1. What are the similarities and differences between** `re.match()` **and** `re.search()`**?**

**Answer:**

-   `re.match()` checks for a match **only at the beginning** of the string.

-   `re.search()` scans the **entire string** and returns the first match found.

-   Both return a `Match` object if a match is found, otherwise `None`.

```python         
import re print(re.match(r"cat", "catfish"))   # Match at start
print(re.search(r"cat", "dogcat"))   # Match found later 
```

**Learning Points:**

-   Match position matters.

-   Many beginner errors come from misusing `re.match()`.

#### **Q2. What is the role of the backslash (**`\`**) in regular expressions?**

**Answer:**

-   Escapes special characters (e.g., `\.` matches a literal dot).

-   Introduces special sequences like `\d`, `\w`, and `\s`.



```python         
re.search(r"\d+", "abc123")  # Matches digits 
```

**Learning Points:**

-   Backslash is central to regex syntax.

-   Regex has its own language inside Python strings.

#### **Q3. What is raw string notation in Python, and why is it used with regex?**

**Answer:**

-   Raw strings (`r"..."`) treat backslashes literally.

-   Prevents double escaping (`\\d` vs `\d`).



```python         
import re
print(re.search(r"\bword\b", "a word here"))  # Match object for 'word' in the string 
```

**Learning Points:**

-   Improves readability.

-   Avoids common escaping bugs.

#### **Q4. Why is** `[...]` **called a character class?**

**Answer:**

-   It defines a set of characters.

-   Matches **one character** from that set.


```python         
re.search(r"[aeiou]", "sky")  # No match 
```

**Learning Points:**

-   Character classes match single characters, not sequences.

#### **Q5. What is the difference between** `*` **and** `+`**?**

**Answer:**

-   `*` → zero or more occurrences

-   `+` → one or more occurrences



```python         
re.search(r"\d*", "abc123")  # Matches empty string
re.search(r"\d+", "abc123")  # Matches "123" 
```

**Learning Points:**

-   `*` can match empty strings.

-   Important for validation logic.

#### **Q6. What does the dot (**`.`**) character match?**

**Answer:**

-   Matches any character **except newline** (`\n`).

-   Equivalent to `[^ \n]`.

**Learning Points:**

-   Leads to understanding `re.S` / DOTALL flag.

#### **Q7. List the special (meta) characters in regex.**

**Answer:**

Code

```python         
\ ^ $ . | ? * + ( ) [ { 
```

**Learning Points:**

-   These characters have special meanings and often need escaping.

#### **Q8. What does** `re.sub()` **do?**

**Answer:**

-   Replaces matched text with a replacement string.



```python         
re.sub(r"\d+", "#", "abc123xyz456") 
```

**Learning Points:**

-   Regex can transform data, not just search.

#### **Q9. What does** `re.split()` **do?**

**Answer:**

-   Splits a string using a regex pattern.



```python         
re.split(r"\d+", "abc123xyz456") 
```

**Learning Points:**

-   More powerful than `str.split()`.
 


### Intermediate Level


#### **Q10. What is the difference between greedy and non-greedy quantifiers?**

**Answer:**

-   Greedy quantifiers match **as much as possible**.

-   Non-greedy (lazy) quantifiers match **as little as possible**.



```python         
text = "<tag>content</tag>" re.search(r"<.*>", text).group()    # Greedy
re.search(r"<.*?>", text).group()   # Non-greedy 
```

**Learning Points:**

-   Prevents over-matching.

#### **Q11. What does** `^` **mean inside a character class?**

**Answer:**

-   Negates the class.

-   Matches characters **not** listed.



```python         
re.search(r"[^0-9]", "123a") 
```

**Learning Points:**

-   Meaning depends on context.

#### **Q12. What are position anchors in regex?**

**Answer:**

-   `^` → start of string/line

-   `$` → end of string/line



```python         
re.match(r"^Hello", "Hello World") 
```

**Learning Points:**

-   Used for validation.

#### **Q13. What do** `\b` **and** `\B` **represent?**

**Answer:**

-   `\b` → word boundary

-   `\B` → non-word boundary



```python         
re.search(r"\bcat\b", "a cat here") 
```

**Learning Points:**

-   Prevents partial word matches.

#### **Q14. What objects do** `search()`**,** `findall()`**, and** `finditer()` **return?**

**Answer:**

-   `search()` → Match or None

-   `findall()` → list

-   `finditer()` → iterator of Match objects

**Learning Points:**

-   Choose based on output needs and memory use.

#### **Q15. What is the role of** `|` **in regex?**

**Answer:**

-   Acts like logical OR.



```python         
re.search(r"cat|dog", "I love dogs") 
```

**Learning Points:**

-   Allows alternatives.

#### **Q16. Explain** `{2,4}`**,** `{2}`**,** `{,4}`**,** `{2,}`**.**

**Answer:**

-   `{2,4}` → 2 to 4 occurrences

-   `{2}` → exactly 2

-   `{,4}` → up to 4

-   `{2,}` → 2 or more

**Learning Points:**

-   Precise repetition control.

#### **Q17. How can regex be made case-insensitive?**

**Answer:**

-   Use `re.I` / `re.IGNORECASE`

-   Use inline flag `(?i)`



```python         
re.search(r"(?i)cat", "CAT") 
```

**Learning Points:**

-   Flags modify matching behavior.



### Advanced Level


#### **Q18. What is the difference between a Pattern object and a Match object?**

**Answer:**

-   **Pattern** → compiled regex, reusable.

-   **Match** → result of applying regex to a string.



```python         
p = re.compile(r"\d+") p.findall("abc123xyz456") 
```

**Learning Points:**

-   Object-oriented regex model.

#### **Q19. For regex** `(\d\d)-(\d\d)`**, what are the groups?**

**Answer:**

-   `group(0)` → entire match

-   `group(1)` → first group

-   `group(2)` → second group



```python         
m = re.search(r"(\d\d)-(\d\d)", "12-34") 
```

**Learning Points:**

-   Group numbering and extraction.

#### **Q20. What is** `re.VERBOSE` **used for?**

**Answer:**

-   Allows whitespace and comments in regex.



```python         
re.compile(r""" \d+     # digits \s*     # optional space """, re.VERBOSE) 
```

**Learning Points:**

-   Improves readability and maintenance.

#### **Q21. What is the difference between** `re.compile()` **and direct use of** `re` **functions?**

**Answer:**

-   `compile()` creates a reusable Pattern object.

-   More efficient for repeated use.

**Learning Points:**










