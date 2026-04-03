





## Part 1: Research Question: Study the Python `requests` library and explain how it simplifies reading files/data from the internet compared to `urllib`.

----------

### Instructions

1.  What is the `requests` library?
2.  How is it different from `urllib`?
3.  Study the following:
    -   `requests.get()`
    -   `response.text`
    -   `response.content`
    -   `response.status_code`
4.  What is:
    -   `raise_for_status()`?
5.  Identify common exceptions:
    -   `RequestException`
    -   `HTTPError`
    -   `ConnectionError`
    -   `Timeout`
6.  Write a small script to:
    -   Read and display first 100 characters from a GitHub file

----------

### Answer (Key Points)

-   `requests` is a **third-party library**
-   It provides a **simple and readable API**
-   `get()` → sends HTTP request
-   `response.text` → string data
-   `response.content` → raw bytes
-   `raise_for_status()`:
    -   Raises error for HTTP issues (like 404)

----------

## Part 2: Project Question (Applied Learning)

### Project Task

> Develop a Python program using `requests` that:

1.  Downloads a file from GitHub (raw URL)
2.  Displays part of the content
3.  Handles:
    -   Invalid URL
    -   Network failure
    -   Timeout
    -   HTTP errors (404, 500)
4.  Demonstrates:
    -   Successful execution
    -   Multiple error scenarios

----------

## Part 3: Script

```python

import requests

# This function demonstrates handling various exceptions that can occur when trying to read 
# content from an online file using the requests library. It includes specific except blocks 
# for HTTP errors, connection errors, timeouts, and a general catch-all for any other 
# request-related exceptions. The else block executes if the request is successful, 
# and the finally block executes regardless of the outcome to indicate that the operation is complete.
def read_online_file(url):
    try:
        print("1. Sending request...")

        response = requests.get(url, timeout=5)  # may raise ConnectionError, Timeout, or HTTPError for bad status codes

        print("2. Checking response...")
        response.raise_for_status()   # raises HTTPError if bad status

        print("3. Reading content...")
        content = response.text  # may raise UnicodeDecodeError if decoding fails

    except requests.exceptions.HTTPError as e:  # Handle HTTP errors (e.g., 404, 500)
        print("HTTP Error:", e)

    except requests.exceptions.ConnectionError:  # Handle connection errors (e.g., server unreachable)
        print("Connection Error: Unable to connect")

    except requests.exceptions.Timeout:  # Handle timeout errors
        print("Timeout Error: Request took too long")

    except requests.exceptions.RequestException as e:  # Generic except for any other request-related exceptions
        print("General Request Error:", e)

    else:
        print("4. Success! First 200 characters:\n")  # Show first 200 characters of content if no exceptions occur
        print(content[:200])

    finally:
        print("5. Operation completed")  # This will always execute regardless of exceptions
        

# Case 1: Valid GitHub file
print("Case 1: Valid URL")
read_online_file("https://raw.githubusercontent.com/python/cpython/main/README.rst")
# Output: try → else → finally

# Case 2: Invalid URL
print("Case 2: Invalid URL")
read_online_file("https://invalid-url.com/file.txt")
# Output: try → except(ConnectionError) → finally

# Case 3: HTTP Error (404)
print("Case 3: HTTP Error (404)")
read_online_file("https://raw.githubusercontent.com/python/cpython/main/NOFILE.txt")
# Output: try → except(HTTPError) → finally

# Case 4: Timeout simulation (very slow site)
print("Case 4: Timeout simulation (very slow site)")
read_online_file("https://httpstat.us/200?sleep=7000")
# Output: try → except(Timeout) → finally

```

## Part 3:Error Comparison Table


  

  

| Exception Type | Cause | Handling |
| --- | --- | --- |
| HTTPError | 404, 500 errors | Specific except |
| ConnectionError | Network failure | Specific except |
| Timeout | Slow response | Specific except |
| RequestException | Base class (all errors) | Generic except |


## Part 4: Exception Hierarchy

```python

RequestException
│
├── HTTPError
├── ConnectionError
├── Timeout
├── TooManyRedirects

```

## Part 5:  Comparison of urllib with requests


  

| Feature | urllib | requests |
| --- | --- | --- |
| Ease of use | Moderate | Very easy |
| Readability | Low | High |
| Built-in | Yes | No |
| Error handling | Complex | Cleaner |




