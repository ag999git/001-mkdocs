
Part A: Questions Based Mainly on the Chapter Topics
1. Write a Python script using re.findall() to extract all digit sequences from a string. The script should show the difference between \d and \d+.
```python
import re
# Sample string containing isolated and grouped digits
text = "My marks are 7, 89, and 1234."
# \d matches ONE digit at a time
single_digits = re.findall(r"\d", text)  # Finds each digit separately
print("Using \\d:", single_digits)  # Using \d: ['7', '8', '9', '1', '2', '3', '4']
# \d+ matches one or more consecutive digits
number_groups = re.findall(r"\d+", text)  # Finds groups of digits as whole numbers
print("Using \\d+:", number_groups)  # Using \d+: ['7', '89', '1234']
# Explanation:
# \d finds every individual digit separately.
# \d+ combines consecutive digits into a single match.
```

________________________________________
2. Write a script that checks whether a string starts with the word Python using the ^ anchor.
```python
import re
# Input string
text = "Python is powerful"
# ^ means start of string
result = re.search(r"^Python", text)  # Checks if string starts with "Python"
# Check whether match succeeded
if result:
    print("String starts with Python")
else:
    print("String does not start with Python")
# Explanation:
# The caret ^ checks the beginning position.
# It does not consume characters itself.
```
________________________________________
3. Write a script that checks whether a string ends with .com using the $ anchor.
```python
import re
# Sample domain name
text = "example.com"
# $ checks end of string
result = re.search(r"\.com$", text)  # Checks if string ends with ".com"
if result:
    print("Valid .com domain")
else:
    print("Does not end with .com")
# Explanation:
# \. matches a literal dot.
# $ ensures that .com appears at the end.
```
________________________________________
4. Write a script that extracts all lowercase letters from a string using the character class [a-z].
```python
import re
text = "PyThOn123abcXYZ"
# Find all lowercase letters
lowercase_letters = re.findall(r"[a-z]", text)  # Character class for lowercase letters
print(lowercase_letters)  # ['y', 'h', 'n', 'a', 'b', 'c']
# Explanation:
# [a-z] represents any lowercase English letter.
# Each matching character is returned individually.
```
________________________________________
5. Write a script that extracts all non-digit characters from a string using \D.
```python
import re
text = "Room45A7"
# \D matches anything that is NOT a digit
result = re.findall(r"\D", text)  # Finds all non-digit characters. Digits are ignored.
print(result)  # ['R', 'o', 'o', 'm', 'A']
# Explanation:
# Digits are ignored.
# Letters and symbols are matched instead.
```
________________________________________
6. Write a script that replaces all whitespace characters in a string with a single dash (-). Use re.sub().
```python
import re
text = "Python   is\tvery\nuseful"
# Replace one or more whitespace characters
cleaned = re.sub(r"\s+", "-", text)  # Replaces sequences of whitespace with a single dash
print(cleaned) # Python-is-very-useful
# Explanation:
# \s matches spaces, tabs, and newlines.
# + combines consecutive whitespace into one match.

```
________________________________________
7. Write a script that validates whether a PIN code contains exactly six digits.
```python
import re
pin = "834001"
# Fullmatch ensures ENTIRE string follows pattern
result = re.fullmatch(r"\d{6}", pin)
if result:
print("Valid PIN")
else:
print("Invalid PIN")
# Explanation:
# \d{6} means exactly six digits.
# re.fullmatch() prevents partial matching.
```
________________________________________
8. Write a script that demonstrates the difference between re.match() and re.search().
```python
import re
text = "Welcome to Python programming"
# match() checks only at beginning
m1 = re.match(r"Python", text)  # This will fail because "Python" is not at the start of the string.
# search() checks anywhere
m2 = re.search(r"Python", text)  # This will succeed because "Python" is found within the string.
print("re.match():", m1)  # Output: None, because the pattern "Python" does not match the start of the string.
print("re.search():", m2)  # Output: <re.Match object; span=(11, 17), match='Python'>, because the pattern "Python" is found starting at index 11 and ending at index 17 in the string.
# Explanation:
# match() fails because Python is not at start.
# search() succeeds because it scans entire string.
```
________________________________________
9. Write a script that uses alternation (|) to search for either cat or dog in a sentence.
```python
import re
text = "I have a dog at home"
# Alternation means OR
result = re.search(r"cat|dog", text)  # Checks for "cat" OR "dog" in the text
if result:
    print("Animal found:", result.group())  # Output: Animal found: dog, because "dog" is present in the text and is the first successful match found by the regex engine.
else:
    print("No animal found")  # Explanation:
# The regex engine tries "cat" first, which fails, then tries "dog", which succeeds, so "dog" is returned as the match.
# Explanation:
# Regex tries both alternatives.
# The first successful alternative is returned.
```

________________________________________
10. Write a script that uses grouping to repeat the word abc one or more times.
```python
import re
text = "abcabcabc"
# Group repeated using +
result = re.fullmatch(r"(abc)+", text)  # Checks if the entire string is one or more repetitions of "abc"
print(result)  # Output: <re.Match object; span=(0, 9), match='abcabcabc'>, because the entire string "abcabcabc" is made up of three repetitions of the substring "abc", which matches the pattern defined by the regex.
# Explanation:
# Parentheses treat abc as one unit.
# + repeats the entire group.
```

________________________________________
11. Write a script that extracts both username and domain name from an email address using capturing groups.
```python
import re
email = "student@gmail.com"
# Two capturing groups
match = re.search(r"(\w+)@(\w+\.\w+)", email)  # Captures username and domain parts of the email
if match:
    print("Username:", match.group(1))  # Output: Username: student, because the first capturing group (\w+) matches the username part of the email before the "@" symbol.
    print("Domain:", match.group(2))  # Output: Domain: gmail.com, because the second capturing group (\w+\.\w+) matches the domain part of the email after the "@" symbol, which consists of a word followed by a dot and another word.
# Explanation:
# Group 1 captures username.
# Group 2 captures domain portion.
```

________________________________________
12. Write a script that demonstrates the use of group(), start(), end(), and span() methods.
```python
import re
text = "Order number is 5678"
match = re.search(r"\d+", text)  # Finds the first sequence of digits in the text
if match:
    print("Matched text:", match.group())  # Output: Matched text: 5678, because the first sequence of digits found in the text is "5678".
    print("Start index:", match.start())  # Output: Start index: 16, because the sequence "5678" starts at index 16 in the text.
    print("End index:", match.end())  # Output: End index: 20, because the sequence "5678" ends at index 20 in the text.
    print("Span:", match.span())  # Output: Span: (16, 20), because the span of the matched sequence "5678" is from index 16 to 20.
# Explanation:
# group() returns matched text.
# start() and end() return positions.
# span() combines both indices.
```

________________________________________
13. Write a script that demonstrates partial consumption using re.match(r"\\d+", text).
```python
import re
text = "123 abc"
match = re.match(r"\d+", text)  # Matches the digits at the start of the string
if match:
    print("Matched:", match.group())  # Output: Matched: 123, because the first sequence of digits found in the text is "123".
    print("Consumed span:", match.span())  # Output: Consumed span: (0, 3), because the span of the matched sequence "123" is from index 0 to 3.
    print("Remaining text:", text[match.end():])  # Output: Remaining text:  abc, because the remaining text after the matched sequence is " abc".
# Explanation:
# Only digits are consumed.
# Remaining characters are untouched.
```

________________________________________
14. Write a script that demonstrates full consumption of a string using .*.
```python
import re
text = "123 abc"
# Consume everything after digits
match = re.match(r"\d+.*", text)  # Matches digits followed by any characters until the end of the string
if match:
    print("Entire consumed text:", match.group())  # Output: Entire consumed text: 123 abc, because the entire string is matched.
    print("Span:", match.span())  # Output: Span: (0, 7), because the span of the matched sequence is from index 0 to 7.
# Explanation:
# .* consumes remaining characters.
# Entire string becomes part of match.
```

________________________________________
15. Write a script that extracts all words from a sentence using \w+.
```python
import re
text = "Python is fun!"
words = re.findall(r"\w+", text)  # Finds all sequences of word characters (letters, digits, underscore)
print(words)  # Output: ['Python', 'is', 'fun'], because the regex \w+ matches sequences of word characters, which in this case are "Python", "is", and "fun". The exclamation mark is not included because it is not a word character.
# Explanation:
# \w matches letters, digits, and underscore.
# + groups consecutive word characters.
```

________________________________________
16. Write a script that splits a sentence into words using re.split().
```python
import re
text = "Apple,Orange;Banana Grape"
# Split using comma, semicolon, or whitespace
parts = re.split(r"[,;\s]+", text)  # Splits the text into parts based on the specified delimiters (comma, semicolon, or whitespace)
print(parts)  # Output: ['Apple', 'Orange', 'Banana', 'Grape'], because the regex [,;\s]+ matches one or more occurrences of comma, semicolon, or whitespace.
# Explanation:
# Character class contains separators.
# + combines consecutive separators.
```

________________________________________
17. Write a script that demonstrates the difference between greedy and non-greedy matching.
```python
import re
text = "<b>Python</b><b>Java</b>"
# Greedy match
greedy = re.findall(r"<b>.*</b>", text)  # Matches from first <b> to last </b>, consuming as much as possible
print("Greedy:", greedy)  # Output: Greedy: ['<b>Python</b><b>Java</b'], because .* matches as much as possible.
# Non-greedy match
nongreedy = re.findall(r"<b>.*?</b>", text)  # Matches from first <b> to first </b>, consuming as little as possible
print("Non-greedy:", nongreedy)  # Output: Non-greedy: ['<b>Python</b>', '<b>Java</b>'], because .*? matches as little as possible.
# Explanation:
# .* grabs maximum possible text.
# .*? grabs minimum possible text.
```

________________________________________
18. Write a script that counts how many replacements were made using re.subn().
```python
import re
text = "Marks: 45, 67, 89"
# Replace numbers with #
result = re.subn(r"\d+", "#", text)  # Replaces all sequences of digits with "#" and also returns the number of replacements made
print(result)  # Output: ('Marks: #, #, #', 3), because all sequences of digits are replaced with "#" and there are 3 replacements.
# Explanation:
# subn() returns tuple.
# First item = modified string.
# Second item = number of replacements.
```

________________________________________
19. Write a script that uses named groups to extract a date in the format DD-MM-YYYY.
```python
import re
text = "Today's date is 08-05-2026"
pattern = r"(?P<day>\d{2})-(?P<month>\d{2})-(?P<year>\d{4})"  # Named groups for day, month, year
match = re.search(pattern, text)  # Searches for the date pattern in the text and captures day, month, and year as named groups 
if match:
    print(match.groupdict())  # Output: {'day': '08', 'month': '05', 'year': '2026'}, because the regex pattern captures the day, month, and year from the date in the text and returns them as a dictionary with keys corresponding to the group names defined in the regex.
# Explanation:
# Named groups create dictionary-like access.
# Keys become group names.
```
________________________________________
20. Write a script that uses re.escape() to safely search for the literal text a+b.
```python
import re
text = "a+b"
# Escape special regex symbols
safe_pattern = re.escape("a+b")  # Escapes the special characters in the string "a+b" so that they are treated as literal characters in the regex pattern
result = re.fullmatch(safe_pattern, text)  # Checks if the entire string matches the escaped pattern
print(result)  # Output: <re.Match object; span=(0, 3), match='a+b'>, because the re.escape() function has escaped the special characters in the string "a+b", allowing it to be treated as a literal string in the regex pattern. The re.fullmatch() function then successfully matches the entire string "a+b" against the escaped pattern, resulting in a match object.
# Explanation:
# + normally means repetition.
# re.escape() removes special meaning.
```

________________________________________
21. Write a script that demonstrates the use of a compiled Pattern object.
```python
import re
# Compile pattern once
pattern = re.compile(r"\d+")  # Compiles the regex pattern for matching one or more digits, allowing it to be reused efficiently for multiple searches without recompiling the pattern each time.
text1 = "123"
text2 = "456"
print(pattern.match(text1))  # Output: <re.Match object; span=(0, 3), match='123'>
print(pattern.match(text2))  # Output: <re.Match object; span=(0, 3), match='456'>
# Explanation:
# Compiled patterns are reusable.
# Useful for repeated matching.
```

________________________________________
22. Write a script that prints the attributes pattern, groups, and groupindex of a compiled Pattern object.
```python
import re
# r"(?P<word>\w+)-(\d+)" is just a normal Python string.
pattern = re.compile(r"(?P<word>\w+)-(\d+)")  # Pattern with named and unnamed groups
# The re.compile() function compiles the regex pattern into a regex object, which can be used for matching operations. The pattern itself is a raw string that contains the regex syntax, including named groups (like (?P<word>\w+)) and unnamed groups (like (\d+)).
print("Pattern:", pattern)  # Output: Pattern: re.compile('(?P<word>\\w+)-(\\d+)'), because the re.compile() function compiles the regex pattern and returns a regex object, which is displayed as re.compile('(?P<word>\\w+)-(\\d+)').
# Double backslashes are used in the output to represent literal backslashes in the regex pattern, which is a common way Python represents strings that contain backslashes.

print("Pattern:", pattern.pattern)  # Output: Pattern: (?P<word>\w+)-(\d+), because the .pattern attribute of the compiled regex object returns the original regex pattern as a string.
# pattern.pattern gives the original regex string, which is useful for reference or debugging, while pattern itself is a compiled object that can be used for matching operations.

print("Groups:", pattern.groups)  # Output: Groups: 2, because the .groups attribute of the compiled regex object returns the total number of capturing groups in the pattern.
print("Named groups:", pattern.groupindex)  # Output: Named groups: {'word': 1}, because the .groupindex attribute of the compiled regex object returns a dictionary mapping named group names to their corresponding group numbers.
# Explanation:
# pattern stores regex text.
# pattern.pattern gives original pattern string.
# groups stores total capturing groups.
# groupindex maps names to numbers.
```

________________________________________
23. Write a script that validates whether a password contains at least one digit and one uppercase letter.
```python
import re
password = "Python123"
# Positive lookaheads used for validation
# (?=.*[A-Z]) checks for at least one uppercase letter.
# (?=.*\d) checks for at least one digit.
# .{8,} ensures minimum length.
pattern = r"(?=.*[A-Z])(?=.*\d).{8,}"  
result = re.fullmatch(pattern, password)  # Checks if the entire password string meets the criteria defined by the regex pattern, which includes having at least one uppercase letter, at least one digit, and being at least 8 characters long.
if result:
    print("Strong password")
else:
    print("Weak password")
# Explanation:
# (?=.*[A-Z]) checks uppercase letter.
# (?=.*\d) checks digit.
# .{8,} ensures minimum length.
```

________________________________________
24. Write a script that extracts all words beginning with a capital letter.
```python
import re
text = "Python and Java are Programming Languages"
# \b ensures we match only at the start of a word, so we get whole words that start with uppercase letters.
# [A-Z] checks that the first letter is uppercase.
# \w* allows for any additional word characters after the first uppercase letter, so we get the full word.
result = re.findall(r"\b[A-Z]\w*", text)  # Finds words that start with an uppercase letter, using a word boundary to ensure it matches the start of a word
print(result)
# Explanation:
# \b ensures word boundary.
# [A-Z] checks first letter uppercase.
# \w* allows for any additional word characters after the first uppercase letter.

```

________________________________________
25. Write a script that finds all repeated vowels in a string using quantifiers.
```python
import re
text = "cooool beeaautiful"
# Find repeated vowels
# [aeiou] matches any vowel.
# {2,} means two or more repetitions of the preceding character class, which in this case is any vowel.
result = re.findall(r"[aeiou]{2,}", text)
print(result)  # Output: ['ooo', 'eeaa', 'uu'], because the regex pattern [aeiou]{2,} matches sequences of two or more consecutive vowels in the text, which are "ooo", "eeaa", and "uu".
# Explanation:
# {2,} means two or more repetitions.
# Character class limits search to vowels.
```

________________________________________
26. Write a script that extracts all hexadecimal numbers from a string.
```python
import re
text = "Colors: #FFAA00 and #12BC9A"
# # matches literal hash symbol.
# [A-Fa-f0-9] matches any hexadecimal digit (case-insensitive).
# {6} ensures exactly six digits.
result = re.findall(r"#[A-Fa-f0-9]{6}", text)
print(result)  # Output: ['#FFAA00', '#12BC9A'], because the regex pattern #[A-Fa-f0-9]{6} matches sequences that start with a "#" followed by exactly six hexadecimal digits (which can be uppercase A-F, lowercase a-f, or digits 0-9), resulting in the matches "#FFAA00" and "#12BC9A".
# Explanation:
# Hexadecimal digits include 0-9 and A-F.
# {6} ensures exactly six digits.
```
________________________________________
27. Write a script that checks whether a string contains only alphabets and spaces.
```python
import re
text = "Python Programming"
# [A-Za-z ] matches uppercase letters, lowercase letters, and spaces.
# + means one or more of the preceding character class, so it matches sequences of letters and spaces that are at least one character long.
result = re.fullmatch(r"[A-Za-z ]+", text)
if result:
    print("Valid text")  # Output: Valid text, because the regex pattern [A-Za-z ]+ matches the entire string "Python Programming", which consists of uppercase letters, lowercase letters, and spaces, and is at least one character long.
else:
    print("Contains invalid characters")  # 
# Explanation:
# Character class includes letters and spaces.
# + ensures one or more characters.
```

________________________________________
28. Write a script that extracts all hashtags from a social media post.
```python
import re
text = "Learning #Python and #Regex is fun"
# #\w+ matches a literal "#" followed by one or more word characters (letters, digits, or underscores), which captures the hashtags in the text.
hashtags = re.findall(r"#\w+", text)
print(hashtags)  # Output: ['#Python', '#Regex'], because the regex pattern #\w+ matches sequences that start with a "#" followed by one or more word characters (which include letters, digits, and underscores), resulting in the matches "#Python" and "#Regex".
# Explanation:
# # matches literal hashtag symbol.
# \w+ captures hashtag text.
```

________________________________________
29. Write a script that demonstrates re.finditer() by printing all matches and their positions.
```python
import re
text = "cat bat rat"
# finditer() returns iterator of Match objects
# \w+ matches sequences of word characters (words) in the text.
for match in re.finditer(r"\w+", text):  # Iterates over each match of the regex pattern \w+ in the text, which finds sequences of word characters (words) and returns an iterator of Match objects for each match found.
    print("Word:", match.group())  # Output: Word: cat, Word: bat, Word: rat, because the regex pattern \w+ matches each word in the text "cat bat rat", and the finditer() function returns an iterator of Match objects for each match found. The group() method is then used to extract the matched word from each Match object, resulting in the output of each word on a separate line.
    print("Position:", match.start(), match.end())  # Output: Position: 0 3, Position: 4 7, Position: 8 11, because the start() and end() methods of the Match object return the starting and ending indices of each matched word in the original text. For "cat", the start index is 0 and the end index is 3; for "bat", the start index is 4 and the end index is 7; for "rat", the start index is 8 and the end index is 11.
# Explanation:
# Each iteration produces one Match object.
# Position information is available.
```

________________________________________
30. Write a script that extracts only the file extensions from filenames.
```python
import re
text = "report.pdf image.png notes.txt"
# \. matches a literal dot.
# [A-Za-z0-9]+ matches the file extension consisting of letters and digits.
# + means one or more of the preceding character class, so it matches file extensions that are at least one character long.
# The regex pattern \.([A-Za-z0-9]+) captures the file extensions from the text, where the parentheses create a capturing group that extracts the extension part after the dot.
extensions = re.findall(r"\.([A-Za-z0-9]+)", text)
print(extensions)  # Output: ['pdf', 'png', 'txt'], because the regex pattern \.([A-Za-z0-9]+) matches a literal dot followed by one or more alphanumeric characters, capturing the file extensions.
# Explanation:
# \. matches literal dot.
# Parentheses capture extension only.
```

________________________________________
Part B: Advanced and Extension Questions
31. Write a script that validates IPv4 addresses using Regular Expressions.
```python
import re
ip = "192.168.1.1"
# Simplified IPv4 regex
# Each octet must be between 0 and 255.
# ^ and $ ensure the entire string matches the pattern.
# (25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d) matches valid octet values.
# Breakup of octet pattern:
# (25[0-5]) matches 250-255.
# (2[0-4]\d) matches 200-249. Because 2 followed by 0-4 and then any digit (0-9) gives us the range of 200-249.
# (1\d\d) matches 100-199. Because 1 followed by any digit (0-9) and then another digit (0-9) gives us the range of 100-199.
# ([1-9]?\d) matches 0-99. Because it optionally matches a digit from 1-9 (which allows for numbers 1-9) followed by any digit (0-9), which allows for numbers 0-99.
# \. matches literal dots between octets.
# 
pattern = r"^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}$"
result = re.fullmatch(pattern, ip)
if result:
    print("Valid IP")
else:
    print("Invalid IP")
# Explanation:
# Each number must be between 0 and 255.
# Dot-separated structure enforced.
```
________________________________________
32. Write a script that masks credit card numbers except the last four digits.
```python
import re
text = "My card number is 1234567812345678"
# Replace first 12 digits
# \d matches a digit, and {4} means exactly four digits. 
# So \d{4} matches the last four digits of the card number.
# (?=\d{4}) is a positive lookahead that asserts that the preceding \d{4} (the last four digits) 
# must be present immediately after the current position in the string, 
# but it does not consume those digits as part of the match. 
# This allows us to target only the digits that come before the last four digits for replacement.

masked = re.sub(r"\d(?=\d{4})", "*", text)  # Replaces digits that are followed by exactly four digits with "*", effectively masking all but the last four digits of the card number.
print(masked)  # Output: My card number is ************5678, because the regex pattern \d(?=\d{4}) matches any digit that is immediately followed by exactly four digits, and replaces it with "*". This results in all digits of the card number being replaced with "*" except for the last four digits, which remain visible.
# Explanation:
# Positive lookahead keeps last 4 digits visible.
# Earlier digits are replaced.
```

________________________________________
33. Write a script that removes duplicate consecutive words from a sentence.
```python
import re
text = "This is is a test test sentence"
# Backreference used
# \b ensures we match whole words.
# (\w+) captures a word and assigns it to group 1.
# \s+ matches the whitespace between the two occurrences of the word.
# \1 refers back to the first capturing group, so it matches the same word again.
# \b ensures we match the end of the word, so we only match repeated words that are whole words and not part of larger words.
# The regex pattern \b(\w+)\s+\1\b matches any instance of a word followed by whitespace and then the same word again, effectively identifying repeated words in the text.
cleaned = re.sub(r"\b(\w+)\s+\1\b", r"\1", text)
print(cleaned)
# Explanation:
# (\w+) captures a word.
# \1 refers back to same word.
```

________________________________________
34. Write a script that extracts all HTML tag names from a string.
```python
import re
html = "<html><body><h1>Title</h1></body></html>"
# Capture tag names
# <\/? matches either opening or closing tags.
# ([a-zA-Z0-9]+) captures the tag name consisting of letters and digits.
# + means one or more of the preceding character class, so it matches tag names that are at least one character long.
# The regex pattern <\/?([a-zA-Z0-9]+) matches both opening and closing HTML tags and captures the tag names, allowing us to extract the names of the tags used in the HTML string.
result = re.findall(r"<\/?([a-zA-Z0-9]+)", html)
print(result)  # Output: ['html', 'body', 'h1', 'h1', 'body', 'html'], because the regex pattern <\/?([a-zA-Z0-9]+) matches both opening and closing HTML tags in the string, capturing the tag names "html", "body", and "h1". The pattern matches the opening tags <html>, <body>, and <h1>, as well as the closing tags </h1>, </body>, and </html>, resulting in the list of tag names extracted from the HTML string.
# Explanation:
# \/? optionally matches closing slash.
# Capturing group extracts tag names.
```

________________________________________
35. Write a script that converts dates from DD/MM/YYYY format to YYYY-MM-DD format using re.sub().
```python
import re
text = "Today's date is 08/05/2026"
# Rearrange captured groups
# (\d{2}) captures the day, which is two digits.
# (\d{2}) captures the month, which is also two digits.
# (\d{4}) captures the year, which is four digits.
# The regex pattern (\d{2})/(\d{2})/(\d{4}) captures the day, month, and year from the date in the text, and the replacement string \3-\2-\1 rearranges these captured groups into the format "year-month-day".
# \3 refers to the third capturing group (year), 
# \2 refers to the second capturing group (month), and 
# \1 refers to the first capturing group (day). 
# By rearranging these groups in the replacement string, we can reformat the date from "08/05/2026" to "2026-05-08".
# The re.sub() function takes the regex pattern, the replacement string, and the original text, and performs the substitution based on the captured groups, resulting in the reformatted date string.
new_text = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\2-\1", text)
print(new_text)
# Explanation:
# Groups capture day, month, year.
# Replacement string rearranges them.
```

________________________________________
36. Write a script that tokenizes a sentence into words and punctuation marks separately.
```python
import re
text = "Hello, world! How are you?"
# Match words OR punctuation
# \w+ matches sequences of word characters (words) in the text.
# [^\w\s] matches any character that is not a word character and not whitespace, 
# which effectively captures punctuation marks.
# The regex pattern \w+|[^\w\s] uses alternation to match either sequences of word characters (words) 
# or individual punctuation characters, allowing us to extract both words and punctuation from the text 
# as separate tokens. 

tokens = re.findall(r"\w+|[^\w\s]", text)
print(tokens)  # Output: ['Hello', ',', 'world', '!', 'How', 'are', 'you', '?'], because the regex pattern \w+|[^\w\s] matches sequences of word characters (which are "Hello", "world", "How", "are", and "you") as well as individual punctuation characters (which are ",", "!", and "?"), resulting in a list of tokens that includes both words and punctuation from the original text.    
# Explanation:
# Alternation separates words and punctuation.
# Useful in Natural Language Processing.
```

________________________________________
37. Write a script that identifies repeated whitespace in a text file and compresses it into single spaces.
```python
import re
text = "Python    is\t\tvery\n\nuseful"
# Replace repeated whitespace
# \s+ captures all repeated whitespace characters (spaces, tabs, newlines) in the text.
# The regex pattern \s+ matches sequences of one or more whitespace characters, and 
# the re.sub() function replaces these sequences with a single space, effectively 
# normalizing the whitespace in the text and making it easier to read and process.    
# By replacing multiple whitespace characters with a single space, we can clean up the formatting 
# of the text and ensure that there are no unnecessary spaces, tabs, or newlines that could 
# interfere with further processing or analysis of the text.  

cleaned = re.sub(r"\s+", " ", text)
print(cleaned)  # Output: Python is very useful, because the regex pattern \s+ matches sequences of one or more whitespace characters in the original text, which includes multiple spaces, tabs, and newlines. The re.sub() function then replaces these sequences with a single space, resulting in the cleaned-up text "Python is very useful" where all extra whitespace has been normalized to single spaces between words.
# Explanation:
# \s+ captures all repeated whitespace.
# Single space normalizes formatting.
```

________________________________________
38. Write a script that extracts URLs beginning with either http or https.
```python
import re
text = "Visit https://python.org and http://example.com"
# https? matches "http" followed by an optional "s", allowing for both "http" and "https" URLs.
# :// matches the literal characters "://", which are part of the URL structure.
# \S+ matches one or more non-whitespace characters, which captures the rest of the URL 
# after "http://" or "https://", including the domain and any path or query parameters.   
# The regex pattern https?://\S+ matches URLs that start with either "http://" or "https://", 
# followed by any sequence of non-whitespace characters, effectively capturing the full URLs present in the text. 
# This allows us to extract the URLs from the given string for further processing or analysis.

urls = re.findall(r"https?://\S+", text)
print(urls)  # Output: ['https://python.org', 'http://example.com'], because the regex pattern https?://\S+ matches both "https://python.org" and "http://example.com" in the text. The pattern allows for both "http" and "https" URLs by making the "s" optional, and then captures the rest of the URL using \S+, which matches any sequence of non-whitespace characters following the "http://" or "https://" prefix.

# Explanation:
# s? makes 's' optional.
# \S+ captures remaining non-space characters.

```

________________________________________
39. Write a script that demonstrates catastrophic backtracking using a badly designed regex and explain why it is dangerous.
```python
import re
import time
# Poorly designed regex. 
pattern = r"(a+)+$"
# (a+)+ means one or more groups of one or more 'a's.
# Nested quantifiers  mean the regex engine has to try many combinations of 'a's when it encounters a long string of 'a's followed by a character that does not match the pattern (like 'X'), leading to excessive backtracking and performance issues.  
# This regex has nested quantifiers (a+)+, which can cause excessive backtracking when the input 
# string has many 'a's followed by a character that does not match the pattern (like 'X').   
# Long failing string
text = "a" * 25 + "X"
start = time.time()
result = re.match(pattern, text)
end = time.time()
print("Match:", result)  # Output: Match: None, because the regex pattern (a+)+$ does not match the input string "aaaaaaaaaaaaaaaaaaaaaaaaaX". The pattern expects one or more groups of one or more 'a's followed by the end of the string, but since the input string ends with 'X' instead of 'a', the regex engine will try many combinations of 'a's and backtrack excessively before ultimately failing to find a match, resulting in None.
print("Time taken:", end - start)  
# Output: Time taken: (a significant amount of time, depending on the system), 
# because the regex pattern (a+)+$ causes excessive backtracking when processing the 
# input string "aaaaaaaaaaaaaaaaaaaaaaaaaX". The regex engine will try many combinations of 'a's and 
# backtrack repeatedly before ultimately failing to find a match, which can lead to a significant increase 
# in processing time, especially as the number of 'a's increases in the input string.

# Explanation:
# Nested quantifiers can trigger excessive backtracking.
# Regex engine tries many combinations before failing.
# Dangerous in performance-sensitive systems.

```

________________________________________
40. Write a script that builds a mini regex tester where the user enters a pattern and a test string, and the script reports whether a match exists.
```python
import re
# User inputs
pattern = input("Enter regex pattern: ")
text = input("Enter test string: ")
try:
    # Try searching pattern
    result = re.search(pattern, text)  # Searches for the first occurrence of the user-provided regex pattern in the user-provided test string, and returns a match object if a match is found, or None if no match is found. The try-except block is used to catch any potential re.error exceptions that may arise from invalid regex patterns entered by the user, allowing the program to handle such errors gracefully without crashing.
    if result:
        print("Match found:", result.group())  # Output: Match found: (matched text), because if the regex pattern matches a portion of the input string, the result.group() method returns the matched text.
        print("Span:", result.span())  # Output: Span: (start, end), because the result.span() method returns a tuple indicating the start and end positions of the matched text within the input string.
    else:
        print("No match found")  # Output: No match found, because if the regex pattern does not match any portion of the input string, the re.search() function returns None, and the else block is executed, printing "No match found".
except re.error as e:
    print("Invalid regex pattern:", e)  # Output: Invalid regex pattern: (error message), because if the user enters an invalid regex pattern, the re.search() function will raise a re.error exception. The except block catches this exception and prints an error message indicating that the regex pattern is invalid, along with the specific error message provided by the exception.
# Explanation:
# Allows experimentation with regex.
# try-except handles invalid patterns safely.
# Useful educational mini-project.

```



