



## Project 1: Study Python’s `urllib` library and explain how files can be read from the internet

### Instructions

1.  Explain:
    -   What is `urllib`?
    -   What is `urlopen()`?
2.  Differentiate between:
    -   Local file reading (`open`)
    -   Internet file reading (`urlopen`)
3.  Study:
    -   `.read()`
    -   `.decode()`
4.  Identify possible errors:
    -   `URLError`
    -   `HTTPError`
5.  Write a small script to:
    -   Read first 100 characters from a GitHub file

----------

## Answer (Summary Points)

-   `urllib.request` is used to **access URLs**
-   `urlopen()`:
    -   Opens a connection to a URL
    -   Returns a response object
-   `.read()`:
    -   Reads data in **bytes**
-   `.decode()`:
    -   Converts bytes → string


----------

## Part 2: Project Question (Applied Learning)

### Project Task

> Write a Python program that:

1.  Downloads a file from GitHub (or any URL)
2.  Displays part of the content
3.  Handles:
    -   Invalid URL
    -   Network failure
    -   Wrong encoding
4.  Demonstrates:
    -   Error-free execution
    -   Error-prone execution

----------

## Part 3: Script

```python


import urllib.request
import urllib.error

# Function to read content from an online file and demonstrate multiple except blocks
def read_online_file(url):  
    try:
        response = urllib.request.urlopen(url)  # may raise URLError if URL is invalid or server is unreachable

        print("2. Reading data...")
        data = response.read()  # may raise HTTPError for HTTP errors (e.g., 404) or URLError if connection issues occur

        print("3. Decoding data...")
        content = data.decode('utf-8')  # may raise UnicodeDecodeError if decoding fails

    except urllib.error.HTTPError as e:  # Handle HTTP errors (e.g., 404, 500)
        print("HTTP Error:", e.code)

    except urllib.error.URLError:  # Handle URL errors (e.g., invalid URL, server unreachable)
        print("URL Error: Cannot reach server")

    except UnicodeDecodeError:  # Handle decoding errors
        print("Error: Cannot decode content")

    except Exception as e:  # Generic except for any other unforeseen exceptions
        print("Other Error:", e)

    else:
        print("4. Success! Showing first 1000 characters:\n")  # Show first 1000 characters of content if no exceptions occur
        print(content[:1000])

    finally:
        print("5. Operation completed")

# Case 1: Correct URL
print("Case 1: Valid URL")
read_online_file("https://raw.githubusercontent.com/gvanrossum/peps/refs/heads/master/pep-0020.txt")

# Case 2: Invalid URL
print("Case 2: Invalid URL")
read_online_file("https://invalid-url.com/file.txt")

# Case 3: HTTP Error (404)
print("Case 3: HTTP Error (404)")
read_online_file("https://raw.githubusercontent.com/python/cpython/main/NOFILE.txt")

# Case 4: Encoding issue (rare but possible)
print("Case 4: Encoding issue (rare but possible)")
read_online_file("https://example.com/binaryfile")

```

## Part 4: Error Comparison Table

  

| Error Type | Cause | Handling |
| --- | --- | --- |
| HTTPError | File not found (404) | Specific except |
| URLError | Network failure | Specific except |
| UnicodeDecodeError | Encoding mismatch | Specific except |
| Exception | Any other issue | Generic except |


## Part 5: Exception Hierarchy

```python

Exception
│
├── URLError
│     └── HTTPError
│
├── UnicodeDecodeError
│
└── Other Exceptions

```


### Important Note

HTTPError is a subclass of URLError
So order matters:

`except HTTPError:` (More specific) should come before `except URLError`

Correct order (specific → general)
















