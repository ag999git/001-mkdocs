




Question 1: Write a Python script using regular expressions to check whether a string contains only digits. The script should print whether the input is valid or invalid. Use re.fullmatch().

```python
import re

# Input string
text = "123456"

# Regex Explanation:
# ^ and $ are not needed because fullmatch() already checks the entire string
# \d  -> matches one digit
# +   -> one or more digits
pattern = r"\d+"


def validate_numeric_string(s):
    # fullmatch() checks whether the entire string satisfies the regex
    result = re.fullmatch(pattern, s)  # Returns a match object if the entire string matches, otherwise None

    if result:  # If result is not None, it means the entire string matches the pattern
        return "Valid numeric string"
    else:
        return "Invalid string"

# Test the function with a valid numeric string
result = validate_numeric_string(text)
print(result)
# OUTPUT: Valid numeric string

# Test the function with an invalid string (contains letters)
invalid_text = "123abc"
result = validate_numeric_string(invalid_text)
print(result)
# OUTPUT: Invalid string

```
Question 2: Write a script to extract all email addresses from a paragraph using re.findall().

```python
import re

text = """
Contact us at admin@test.com or support123@company.org
"""

# Regex Explanation:
# [a-zA-Z0-9._%+-]+  -> username part
#     ._%+- are allowed special characters in the username
#     + means one or more of the preceding characters
# @                  -> literal @ symbol
# [a-zA-Z0-9.-]+     -> domain name
# \.                 -> literal dot
# [a-zA-Z]{2,}       -> extension like com, org, edu

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

emails = re.findall(pattern, text)  # findall() returns a list of all matches in the text

print(emails)
# Output:
# ['admin@test.com', 'support123@company.org']

```
Question 3: Write a script to find all words beginning with a capital letter.

```python
import re

text = "Alice, Bob and Charlie work with Donald"

# Regex Explanation:
# \b       -> word boundary
# [A-Z]    -> one uppercase letter
# [a-z]+   -> one or more lowercase letters

pattern = r"\b[A-Z][a-z]+"

matches = re.findall(pattern, text)

print(matches)
# Output:
# ['Alice', 'Bob', 'Charlie', 'Donald']

```
Question 4: Write a script to validate a PIN code containing exactly 6 digits.

```python
import re

# Regex Explanation:
# \d{6} -> exactly 6 digits

pattern = r"\d{6}"
def is_valid_pin(pin):
    if re.fullmatch(pattern, pin):
        print("Valid PIN")
    else:
        print("Invalid PIN")

# Example valid PIN
is_valid_pin("123456")  # Valid PIN

# Example invalid PINs
is_valid_pin("12345")      # Invalid PIN (too short)
is_valid_pin("1234567")    # Invalid PIN (too long)
is_valid_pin("12A456")     # Invalid PIN (contains letter)


```
Question 5: Write a script to split a sentence wherever multiple spaces occur. Use re.split().

```python
import re
text = "Python    is   very     useful"

# Regex Explanation:
# \s+ -> one or more whitespace characters

pattern = r"\s+"

# Use re.split() to split the text at each sequence of whitespace
# The regex pattern \s+ matches sequences of whitespace characters, 
# and re.split() breaks the text into parts wherever this pattern is found. 
# The result is a list of non-whitespace substrings.
parts = re.split(pattern, text)  # 

print(parts)
# Output:
# ['Python', 'is', 'very', 'useful']

```
Question 6: Write a script to replace all digits in a string with the symbol #. Use re.sub().

```python
import re

text = "Order 123 was shipped on 2025-05-10"

# Regex Explanation:
# \d -> matches one digit

pattern = r"\d"

# Replace all digits with "#"
# The re.sub() function takes the pattern, replacement string, and original text as arguments. 
# It searches for all occurrences of the pattern in the text and replaces them with the specified replacement string.
result = re.sub(pattern, "#", text)  

print(result)

# Output:
# Order ### was shipped on ####-##-##

```
Question 7: Write a script to extract all years from a text using capturing groups.

```python
import re

text = """
Some important battles in Indian history:
Battle of the Hydaspes (326 BCE)
Kalinga War (261 BCE)
First Battle of Tarain (1191 CE)
First Battle of Panipat (1526 CE)
Second Battle of Panipat (1556 CE)
Third Battle of Panipat (1761 CE)
Battle of Buxar (1764 CE)

"""

# Regex Explanation:
# (      ) -> capturing group
# \d{4}   -> exactly 4 digits

pattern = r"(\d{4})"

# findall() returns all matches as a list of strings (the captured groups)
matches = re.findall(pattern, text)

print(matches)
# Output:
# ['326', '261', '1191', '1526', '1556', '1761', '1764']

```
Question 8: Write a script to find repeated words such as 'the the' using backreferences.

```python
import re

text = "This is is a test test sentence"

# Regex Explanation:
# (\w+)   -> capture a word
# \s+     -> one or more spaces
# \1      -> same word as captured in group 1

pattern = r"(\w+)\s+\1"

matches = re.findall(pattern, text)

print(matches)

# Output:
# ['is', 'test']

```
Question 9: Write a script to demonstrate greedy matching and non-greedy matching.

```python
import re

text = "<h1>Hello</h1><p>World</p>"

# Greedy matching
# .* consumes as much as possible
greedy = re.search(r"<.*>", text)

print("Greedy:")
print(greedy.group())
# Output: <h1>Hello</h1><p>World</p>

# Non-greedy matching
# .*? consumes as little as possible
# The pattern <.*?> matches the smallest possible substring that starts with "<" and ends with ">".
lazy = re.search(r"<.*?>", text)

print("\nNon-Greedy:")
print(lazy.group())
# Output: <h1>

```
Question 10: Write a script to validate whether a password contains at least one uppercase letter and one digit.

```python
import re



# Regex Explanation:
# (?=.*[A-Z]) -> positive lookahead for uppercase
#         The (?=...) checks a condition without consuming text. It asserts that at the current position 
#         in the string, there must be a match for the pattern inside the lookahead. In this case, 
#         (?=.*[A-Z]) means that somewhere ahead in the string (after any characters, due to .*) there must 
#         be at least one uppercase letter [A-Z].
# (?=.*\d)    -> positive lookahead for digit
#         Similarly, (?=.*\d) asserts that somewhere ahead in the string there must be at least one digit \d.
# .{8,}       -> minimum 8 characters

pattern = r"(?=.*[A-Z])(?=.*\d).{8,}"

def validate_password(pw):
    if re.fullmatch(pattern, pw):
        print("Valid Password")
    else:
        print("Invalid Password")

good_password = "GoodPass1"
validate_password(good_password)
# OUTPUT: Valid Password

bad_password = "badpass"
validate_password(bad_password)
# OUTPUT: Invalid Password
```
Question 11: Write a script to extract hashtags from a social media post.

```python
import re



# Regex Explanation:
# r"#\w+" is a raw string literal that defines the regex pattern to match hashtags in the text.
# #      -> literal hash
# \w+    -> one or more word characters

pattern = r"#\w+"

def extract_hashtags(text):
    return re.findall(pattern, text)

text_with_hashtags = "Learning #Python and #DataScience is fun"
with_hashtags = extract_hashtags(text_with_hashtags)
print(with_hashtags)
# OUTPUT: ['#Python', '#DataScience']

text_without_hashtags =  "A day without hashtags is like a day without sunshine"
without_hashtags = extract_hashtags(text_without_hashtags)
print(without_hashtags)
# OUTPUT: []

```
Question 12: Write a script to remove duplicate spaces from a paragraph.

```python
import re

text = "Python     is     powerful"

# Regex Explanation:
# \s+ -> one or more spaces

result = re.sub(r"\s+", " ", text)

print(result)

# Output:
# Python is powerful

```
Question 13: Write a script to extract file extensions from filenames.

```python
import re

text = "report.pdf image.png notes.docx"

# Regex Explanation:
# \w+     -> filename
# \.      -> literal dot
# (\w+)   -> capture extension

pattern = r"\w+\.(\w+)"

extensions = re.findall(pattern, text)

print(extensions)

# Output:
# ['pdf', 'png', 'docx']

```
Question 14: Write a script using non-capturing groups to match titles such as Mr, Ms, and Dr.

```python
import re

text = "Dr. Sharma met Mr. Verma"

# Regex Explanation:
# (?:...) -> non-capturing group
# Used for grouping without storing match

pattern = r"(?:Mr|Ms|Dr)\."

matches = re.findall(pattern, text)

print(matches)

# Output:
# ['Dr.', 'Mr.']

```
Question 15: Write a script to check whether a string starts with 'Python'.

```python
import re

text = "Python is easy"

# Regex Explanation:
# ^ -> start anchor

pattern = r"^Python"

if re.search(pattern, text):
    print("Starts with Python")
else:
    print("Does not start with Python")

```
Question 16: Write a script to check whether a string ends with '.com'.

```python
import re

website = "example.com"

# Regex Explanation:
# \.com$ -> ends with .com

pattern = r"\.com$"

if re.search(pattern, website):
    print("Valid .com domain")
else:
    print("Invalid domain")

```
Question 17: Write a script to extract all floating-point numbers from text.

```python
import re

text = "Prices are 45.67 and 89.5 dollars"

# Regex Explanation:
# \d+    -> digits before decimal
# \.     -> decimal point
# \d+    -> digits after decimal

pattern = r"\d+\.\d+"

numbers = re.findall(pattern, text)

print(numbers)

# Output:
# ['45.67', '89.5']
________________________________________
```
Question 18: Write a script to validate Indian mobile numbers starting with 6, 7, 8, or 9.

```python
import re

mobile = "9876543210"

# Regex Explanation:
# [6789] -> first digit
# \d{9}  -> remaining 9 digits

pattern = r"[6789]\d{9}"

if re.fullmatch(pattern, mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")

```
Question 19: Write a script to extract dates in DD-MM-YYYY format.

```python
import re

text = "Exam dates are 12-05-2025 and 15-08-2026"

# Regex Explanation:
# \d{2} -> day
# -     -> separator
# \d{2} -> month
# -     -> separator
# \d{4} -> year

pattern = r"\d{2}-\d{2}-\d{4}"

dates = re.findall(pattern, text)

print(dates)

```
Question 20: Write a script using re.finditer() to display all numbers and their positions in a string.

```python
import re

text = "abc 123 def 456"

pattern = r"\d+"

matches = re.finditer(pattern, text)

for m in matches:

    print("Match:", m.group())
    print("Start:", m.start())
    print("End:", m.end())
    print("Span:", m.span())

# group() -> matched text
# start() -> starting index
# end()   -> ending index
# span()  -> tuple of start and end




