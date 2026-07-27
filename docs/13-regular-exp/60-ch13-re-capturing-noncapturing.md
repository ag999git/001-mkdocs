




## Capturing versus non-capturing groups

We need to understand the difference between capturing and non-capturing groups

Parentheses in regex serve two separate purposes:

**Grouping-** To control precedence, repetition, alternation, etc using (...)

**Capturing-** To store matched text for later use.

You can do (a) Grouping with capturing and (b) grouping without capturing.

So far we have discussed capturing groups which use the syntax:- (......)

A non-capturing group is a group that is used only for grouping and not for capturing text.

Its Syntax is  **(?:pattern)**

Unlike normal parentheses (pattern), a non-capturing group:

-   does not store the matched text
-   does not create a group number
-   cannot be referenced using backreferences like \1

When Should Non-Capturing Groups Be Used? Non-capturing groups are used when:

-   You don’t want backreferences
-   You don’t need to store matched text
-   You only need grouping
-   You want cleaner group numbering
-   You want better performance
-   You want to avoid confusion caused by extra groups

**Common Uses of Non-Capturing Groups are as follows:-**

**A. Grouping for Repetition (Quantifiers). This is the most common use**

You often need to apply *, +, {m,n} to more than one token. Example: Grouping for Repetition
```python
text = "ababab"
# The regex pattern (?:ab)+ matches one or more occurrences
# of the sequence 'ab' without capturing it as a group.
pattern = re.findall(r"(?:ab)+", text)
print(pattern)
# Output: ['ababab']
```
Note:- (1) ab is grouped (2) + applies to the whole group (3) No unwanted capturing occurs

**B. Grouping for Alternation (OR)**

Used when alternatives should be treated as **one logical unit**. The following example shows use of alternation without capturing and with capturing groups.

```python
import  re
# Using non-capturing groups with (?:...) allows us to match patterns without
# creating separate capture groups, resulting in a simpler output from re.findall.
# 1. Non-capturing group (?:cat|dog|rat) matches 'cat', 'dog', or 'rat'
# It allows us to group alternatives together without creating separate
# capture groups. re.findall returns list of matched strings directly.
# For example:
pattern1 = re.findall(r"(?:cat|dog|rat)", "cat dog rat bat")
print("Non-capturing-> ", pattern1)
# Output: Non-capturing-> ['cat', 'dog', 'rat']
# 2. If we use capturing groups (i.e., (cat|dog|rat)), re.findall
# would return list of tuples with each matched string in its own
# tuple because each match is captured in its own group.
# For example:
pattern2 = re.findall(r"(cat|dog|rat)", "cat dog rat bat")
print("Capturing-> ", pattern2)
# Output
# [('cat',), ('dog',), ('rat',)]

```

**Performance Benefits of Non-Capturing Groups**

Capturing groups require the regex engine to: (1) Store matched text. (2) Track group numbers (3) Manage additional backtracking states

Non-capturing groups **avoid all of this**. Non-capturing groups are:- (1) lighter (2) faster (3) easier to maintain

**Avoiding Unwanted Backreferences**

Capturing groups can unintentionally create backreferences that:- (1) May confuse the code user (2) May break group numbering. (3) May cause bugs in group(n) access

Example: Comparing Non-capturing to unwanted Capturing

```python
import  re
# 1. Original Version Using Capturing Group
pattern = re.search(r"(Mr|Ms|Dr)\.  (\w+)", "Dr. John")
print(pattern.groups())
# Output: ('Dr', 'John')
# 2. But if title not needed , capturing is unnecessary.
# Improved Version Using Non-Capturing Group
pattern = re.search(r"(?:Mr|Ms|Dr)\.  (\w+)", "Dr. John")
print(pattern.groups())
# Output: ('John',)
```
**Non-capturing can provide cleaner Numbering of Capturing Groups**
Unnecessary capturing shifts group numbers and makes code harder to read.
Suppose you want to capture only the group containing dog.
The doing **`(a)(b)(c)(dog)`**  is bad practice because here, **`"dog"`** becomes **group(4)**

Better Practice would be **`(?:a)(?:b)(?:c)(dog)`**. Now **`"dog"`** \is: **group(1)**.

This is (1) Cleaner (2) Less error-prone

The following script shows difference in use of capturing and non-capturing groups:-

```python
import  re
text = "Here are some files: report.pdf, notes.docx, image.png, summary.txt."
# 1. Using non-capturing group for filename to focus on capturing the file extension
# The regex r"(?:\w+)\.(pdf|docx|txt)" is in 3 parts:
# A. (?:\w+) → non-capturing group for the filename (we don't need to capture it)
# B. \. → literal dot before the file extension
# C. (pdf|docx|txt) → capturing group for specific file extensions we want to match
m1 = re.search(r"(?:\w+)\.(pdf|docx|txt)", text) # Selecting only pdf, docx, txt files
print(m1.group(1)) # docx
# 2. Using capturing group for filename to capture the filename part
m2 = re.search(r"(\w+)\.(pdf|docx|txt)", text)
print(m2.group(1)) # notes
# In m1, we use a non-capturing group (?:...) for the filename part since we only need to capture the file extension.
# In m2, we use a capturing group (...) for the filename part to capture 'notes'.
# 3. If you want to capture both filename and extension, you can do:
m3 = re.search(r"(\w+)\.(pdf|docx|txt)", text)
print(m3.group(1)) # notes
print(m3.group(2)) # docx
```

The following script shows use of non-capturing and capturing groups in removing duplicate words in a sentence:-

```python
# Difference between (\b\w+)(?:\s+\1)+ and (\b\w+)(\s+\1)+
import  re
# 1. Using non-capturing group for the repeated duplicates
# Explanation for (\b\w+)(?:\s+\1)+
# In this pattern, the first group (\b\w+) captures a word.
# The second part (?:\s+\1)+ is a non-capturing group that matches
# one or more occurrences of whitespace followed by the same word
# captured in the first group. Since it is a non-capturing group,
# it does not create a separate capturing group for the repeated matches.
def  remove_duplicates_non_capturing(some_text):
    # Using non-capturing group for the repeated duplicates
    without_dup_text = re.sub(r'(\b\w+)(?:\s+\1)+', r'\1', some_text)
    return  without_dup_text

# Test the function
text_with_dup = 'The The cat cat cat sat sat on on the the wall wall.'
text_without_dup = remove_duplicates_non_capturing(text_with_dup)
print("Using non-capturing->", text_without_dup) # Output: 'The cat sat on the wall.'
# Explanation: Capturing vs Non-Capturing Groups
# In capturing, the pattern is (\b\w+)(\s+\1)+. The second group (\s+\1)
# captures the whitespace and the repeated word. This means that every
# time a duplicate is found, it is captured again, which can lead to more
# complex backreferences.
# In contrast, using a non-capturing group (?:\s+\1)+ means that we are only interested in matching the duplicates without capturing them again.
# This simplifies the pattern and makes it more efficient for the purpose of removing duplicates.
# Both patterns will effectively remove duplicates, but the non-capturing group is more efficient in this context.
# The output will be the same for both patterns:
# 'The cat sat on the wall.'
# However, using the non-capturing group is generally preferred when the repeated matches do not need to be referenced later.
# 2. Using capturing group for the repeated duplicates
# Explanation for (\b\w+)(\s+\1)+
# In this pattern, the first group (\b\w+) captures a word.
# The second part (\s+\1)+ is a capturing group that matches one or more
# occurrences of whitespace followed by the same word captured in the first group.
# Since it is a capturing group, it creates a separate capturing group for the repeated matches.
# This means that every time a duplicate is found, it is captured again, which can lead to more
# complex backreferences.
def  remove_duplicates_capturing(some_text):
    without_dup_text = re.sub(r'(\b\w+)(\s+\1)+', r'\1', some_text)
    return  without_dup_text

# Test the function
text_with_dup = 'The The cat cat cat sat sat on on the the wall wall.'
text_without_dup_capturing = remove_duplicates_capturing(text_with_dup)
print("Using capturing-> ", text_without_dup_capturing) # Output: 'The cat sat on the wall.'
# Both functions produce the same output, but the first function uses a non-capturing group for efficiency.

```

**Example Python Script which removes duplicate words using non-capturing groups.**

```python
import  re
text = "The The cat cat cat sat sat on on the the wall wall"
pattern = re.compile(r"(\b\w+)(?:\s+\1)+") # Pattern to find duplicate words
matches = pattern.finditer(text)
for  m  in  matches:
    print("Duplicate word:", m.group(1))

# Output:
# Duplicate word: The
# Duplicate word: cat
# Duplicate word: sat
# Duplicate word: on
# Duplicate word: the
# Duplicate word: wall
```
The regex rconsists of 2 groups. The components of these groups are

**1. The First Group: (\b\w+)**

This part identifies the "original" word you are looking for.

-   **(...) (Capturing Group):** The parentheses tell Python to "remember" whatever matches inside. This becomes **Group 1**.
-   **\b (Word Boundary):** This ensures the match starts at the beginning of a word (so it doesn't match "ear" inside "near").
-   **\w+:** This matches one or more "word characters" (letters, numbers, or underscores).

**2. The Second Group: (?:\s+\1)+**

This part looks for the repeats.

-   **(?: ... ) (Non-Capturing Group):** These parentheses group the instructions together so the + at the end applies to the whole set, but it doesn't "save" this match as a separate group.
-   **\s+:** This matches one or more whitespace characters (spaces, tabs, or newlines).
-   **\1 (Backreference):** This is the magic part. It tells the regex to match **exactly** what was found in **Group 1**. If Group 1 found "the", \1 will only match "the".
-   **+ (Quantifier):** The plus sign at the very end means "one or more of the preceding group." This allows the pattern to catch "hello hello" as well as "hello hello hello."

**Table: Meanings of "Parts" of Regular Expression (r"(\b\w+)(?:\s+\1)+")**

| Part | Meaning |
| --- | --- |
| \b | Start at a word boundary. |
| \w+ | Match the word (e.g., "apple"). |
| (...) | Capture that word so we can refer to it later. |
| \s+ | Look for one or more spaces after that word. |
| \1 | Look for the exact same word again. |
| (?:...)+ | Repeat the "space + same word" logic one or more times. |



**Table: Comparison of capturing to non-capturing groups:-**

| Feature | Stores matched text | Creates group number | Supports backreferences | Used for extraction | Used for grouping only | Better performance | Cleaner group numbering |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Capturing Group ( ) | Yes | Yes | Yes | Yes | Sometimes | Slightly slower | No |
| Non-Capturing Group (?: ) | No | No | No | No | Ideal | Faster | Yes |





