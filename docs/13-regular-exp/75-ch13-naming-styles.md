


### Naming styles in Python programming






```python
import re

# 1. snake_case to camelCase conversion

def snake_to_camel(snake_name):
    """
    Convert a snake_case string into camelCase.

    Example:
    - snake_case → snakeCase
    """

    # Split the string using underscore
    parts = snake_name.split('_')

    # First word remains lowercase
    first_word = parts[0]

    # Capitalize the first letter of remaining words
    remaining_words = [word.capitalize() for word in parts[1:]]

    # Join everything together
    return first_word + ''.join(remaining_words)
# Demonstration
print(" snake to camel-> ", snake_to_camel("snake_case_example"))  # snake to camel->  snakeCaseExample

# 2. camelCase to snake_case conversion

def camel_to_snake(camel_name: str) -> str:
    """
    Convert a camelCase or PascalCase string into snake_case.

    Examples:
    - camelCase  → camel_case
    - PascalCase → pascal_case
    """

    # Step 1:
    # Insert an underscore between:
    #   - any character (.)
    #   - followed by an uppercase letter and lowercase letters
    # Example: "abcXyz" → "abc_Xyz"
    # r'(.)([A-Z][a-z]+' → capture any char + uppercase + lowercase(s)
    step1 = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', camel_name)

    # Step 2:
    # Handle remaining cases where:
    #   - a lowercase letter or digit
    #   - is followed directly by an uppercase letter
    # Example: "XMLFile" → "XML_File"
    # r'([a-z0-9])([A-Z])' → capture lowercase/digit + uppercase
    snake_name = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', step1)

    # Step 3:
    # Convert the entire string to lowercase
    return snake_name.lower()
# Demonstration
print("camel to snake-> ", camel_to_snake("camelCaseExample"))  # camel to snake->  camel_case_example

# 3. Pascal to snake case conversion
def pascal_to_snake(pascal_name):   
    """
    Convert a PascalCase string into snake_case.

    Examples:
    - PascalCase → pascal_case
    """

    # Insert an underscore before each uppercase letter (except the first)
    # r'(?<!^)(?=[A-Z])' → negative lookbehind for start + positive lookahead for uppercase
    snake_name = re.sub(r'(?<!^)(?=[A-Z])', '_', pascal_name).lower()  # 

    return snake_name
# Demonstration
print("pascal to snake-> ", pascal_to_snake("PascalCaseExample")) # pascal to snake->  pascal_case_example

# 4. snake_case to PascalCase conversion
def snake_to_pascal(snake_name):
    """
    Convert a snake_case string into PascalCase.

    Examples:
    - snake_case → SnakeCase
    """

    # Split the string using underscore
    parts = snake_name.split('_')

    # Capitalize the first letter of each part
    pascal_name = ''.join(word.capitalize() for word in parts)

    return pascal_name
# Demonstration
print("snake to pascal-> ", snake_to_pascal("snake_case_example"))  # snake to pascal->  SnakeCaseExample

# 5. camelCase to PascalCase conversion
def camel_to_pascal(camel_name):
    """
    Convert a camelCase string into PascalCase.

    Examples:
    - camelCase → CamelCase
    """

    if not camel_name:
        return camel_name

    # Capitalize the first letter
    pascal_name = camel_name[0].upper() + camel_name[1:]

    return pascal_name  
# Demonstration
print("camel to pascal-> ", camel_to_pascal("camelCaseExample"))  # camel to pascal->  CamelCaseExample

# 6. PascalCase to camelCase conversion
def pascal_to_camel(pascal_name):
    """
    Convert a PascalCase string into camelCase.

    Examples:
    - PascalCase → pascalCase
    """

    if not pascal_name:
        return pascal_name

    # Lowercase the first letter
    camel_name = pascal_name[0].lower() + pascal_name[1:]

    return camel_name   
# Demonstration
print("pascal to camel-> ", pascal_to_camel("PascalCaseExample"))  # pascal to camel->  pascalCaseExample

# 7. Uppercase to snake_case conversion
def upper_to_snake(upper_name):
    """
    Convert an UPPERCASE string with underscores into snake_case.

    Examples:
    - UPPER_CASE → upper_case
    """

    # Convert the entire string to lowercase
    snake_name = upper_name.lower()

    return snake_name
# Demonstration
print("upper to snake-> ", upper_to_snake("UPPER_CASE_EXAMPLE"))  # upper to snake->  upper_case_example
# 8. snake_case to UPPERCASE conversion
def snake_to_upper(snake_name):
    """
    Convert a snake_case string into UPPERCASE with underscores.

    Examples:
    - snake_case → SNAKE_CASE
    """

    # Convert the entire string to uppercase
    upper_name = snake_name.upper()

    return upper_name
# Demonstration
print("snake to upper-> ", snake_to_upper("snake_case_example"))  # snake to upper->  SNAKE_CASE_EXAMPLE
# 9. UPPERCASE to camelCase conversion
def upper_to_camel(upper_name):
    """
    Convert an UPPERCASE string with underscores into camelCase.

    Examples:
    - UPPER_CASE → upperCase
    """

    # First convert to snake_case
    snake_name = upper_to_snake(upper_name)

    # Then convert to camelCase
    camel_name = snake_to_camel(snake_name)

    return camel_name
# Demonstration
print("upper to camel-> ", upper_to_camel("UPPER_CASE_EXAMPLE"))  # upper to camel->  upperCaseExample

# 10. camelCase to UPPERCASE conversion

def camel_to_upper(camel_name):
    """
    Convert a camelCase string into UPPERCASE with underscores.

    Examples:
    - camelCase → CAMEL_CASE
    """

    # First convert to snake_case
    snake_name = camel_to_snake(camel_name)

    # Then convert to UPPERCASE
    upper_name = snake_to_upper(snake_name)

    return upper_name
# Demonstration
print("camel to upper-> ", camel_to_upper("camelCaseExample"))  # camel to upper->  CAMEL_CASE_EXAMPLE

# 11. UPPERCASE to PascalCase conversion

def upper_to_pascal(upper_name):
    """
    Convert an UPPERCASE string with underscores into PascalCase.

    Examples:
    - UPPER_CASE → UpperCase
    """

    # First convert to snake_case
    snake_name = upper_to_snake(upper_name)

    # Then convert to PascalCase
    pascal_name = snake_to_pascal(snake_name)

    return pascal_name
# Demonstration
print("upper to pascal-> ", upper_to_pascal("UPPER_CASE_EXAMPLE"))  # upper to pascal->  UpperCaseExample

# 12. PascalCase to UPPERCASE conversion
def pascal_to_upper(pascal_name):   
    """
    Convert a PascalCase string into UPPERCASE with underscores.

    Examples:
    - PascalCase → PASCAL_CASE
    """

    # First convert to snake_case
    snake_name = pascal_to_snake(pascal_name)

    # Then convert to UPPERCASE
    upper_name = snake_to_upper(snake_name)

    return upper_name
# Demonstration
print("pascal to upper-> ", pascal_to_upper("PascalCaseExample"))  # pascal to upper->  PASCAL_CASE_EXAMPLE

```



