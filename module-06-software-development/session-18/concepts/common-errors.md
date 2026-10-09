# Common Python Errors: What They Mean and How to Fix Them

## Introduction: Errors Are Your Friends

When Python shows you an error, it's trying to help! Error messages are clues that point you to what's wrong. Learning to read them is a crucial programming skill.

### The Three Types of Errors

| Error Type | When It Happens | Python's Reaction |
|------------|-----------------|-------------------|
| **Syntax Error** | Before running | "I can't understand this code!" |
| **Runtime Error** | While running | "Something went wrong!" |
| **Logic Error** | After running | "The answer is wrong, but no crash" |

---

## Part 1: Syntax Errors (Grammar Mistakes)

Syntax errors happen when you break Python's grammar rules. Python won't run any code until these are fixed.

### Common Syntax Mistakes

#### 1. Missing Colon

```python
# WRONG - Missing colon after if statement
if x > 5
    print("Big")

# SyntaxError: invalid syntax
# Python says: "I expected a colon here!"
```

```python
# RIGHT
if x > 5:
    print("Big")
```

#### 2. Incorrect Indentation

```python
# WRONG - No indentation inside function
def greet():
print("Hello")  # This should be indented!

# IndentationError: expected an indented block
```

```python
# RIGHT
def greet():
    print("Hello")  # 4 spaces indentation
```

#### 3. Mismatched Quotes

```python
# WRONG - String never ends
message = "Hello, world!

# SyntaxError: EOL while scanning string literal
# EOL = "End of Line" - Python hit the end while still inside a string
```

```python
# RIGHT
message = "Hello, world!"  # Both quotes present
```

#### 4. Assignment vs Comparison

```python
# WRONG - Using = instead of ==
if x = 5:  # = assigns, == compares
    print("x is 5")

# SyntaxError: invalid syntax
# Python says: "You probably meant to use =="
```

```python
# RIGHT
if x == 5:  # Two equals signs for comparison
    print("x is 5")
```

#### 5. Forgetting Parentheses

```python
# WRONG - Missing parentheses (Python 3 only)
print "Hello"

# SyntaxError: Missing parentheses in call to 'print'
```

```python
# RIGHT
print("Hello")  # Parentheses required in Python 3
```

#### 6. Unclosed Brackets

```python
# WRONG - Missing closing brackets
my_list = [1, 2, 3

# SyntaxError: unexpected EOF while parsing
# EOF = "End of File" - Python hit the end looking for ]
```

```python
# RIGHT
my_list = [1, 2, 3]  # Closing bracket present
```

### How to Fix Syntax Errors

**The error message tells you exactly where the problem is:**

```
  File "my_program.py", line 5
    if x > 5
            ^
SyntaxError: invalid syntax
```

**Breakdown:**
- **File**: Which file has the error
- **Line 5**: Error is on line 5
- **^**: Points to where Python got confused
- **SyntaxError**: What kind of error

**Tips:**
1. The error might be *before* the line shown
2. Look for missing colons, quotes, or brackets
3. Check indentation (use 4 spaces consistently)

---

## Part 2: Runtime Errors (Crashes While Running)

Runtime errors happen when Python is running your code but encounters a problem it can't handle.

### Type Errors: Wrong Type of Data

```python
# WRONG - Adding string and number
result = "Hello" + 5

# TypeError: can only concatenate str (not "int") to str
# Translation: "You can't add text and numbers together"
```

```python
# RIGHT - Convert to string first
result = "Hello" + str(5)  # "Hello5"
# Or use f-string
result = f"Hello {5}"      # "Hello 5"
```

### Name Errors: Undefined Variables

```python
# WRONG - Using variable that doesn't exist
print(my_variable)

# NameError: name 'my_variable' is not defined
# Translation: "I don't know what my_variable is"
```

```python
# RIGHT - Define the variable first
my_variable = 42
print(my_variable)
```

**Common Causes:**
- Typo in variable name
- Using variable before creating it
- Variable only exists inside a function

### Attribute Errors: Wrong Method/Attribute

```python
# WRONG - List doesn't have .length()
numbers = [1, 2, 3]
print(numbers.length())

# AttributeError: 'list' object has no attribute 'length'
# Translation: "Lists don't have a length() method"
```

```python
# RIGHT - Use len() function
numbers = [1, 2, 3]
print(len(numbers))  # 3
```

### Index Errors: Out of Range

```python
# WRONG - Asking for item that doesn't exist
my_list = [1, 2, 3]
print(my_list[5])  # Only has indices 0, 1, 2

# IndexError: list index out of range
# Translation: "There's no item at position 5"
```

```python
# RIGHT - Check length first
my_list = [1, 2, 3]
if len(my_list) > 5:
    print(my_list[5])
else:
    print("List doesn't have that many items")

# Or use safe access
index = 5
if index < len(my_list):
    print(my_list[index])
```

### Key Errors: Missing Dictionary Key

```python
# WRONG - Accessing key that doesn't exist
my_dict = {"name": "Alice", "age": 25}
print(my_dict["email"])  # No "email" key!

# KeyError: 'email'
# Translation: "There's no 'email' in this dictionary"
```

```python
# RIGHT - Use .get() method
my_dict = {"name": "Alice", "age": 25}
print(my_dict.get("email", "No email found"))  # "No email found"

# Or check first
if "email" in my_dict:
    print(my_dict["email"])
```

### Value Errors: Wrong Value

```python
# WRONG - Can't convert "hello" to number
number = int("hello")

# ValueError: invalid literal for int() with base 10: 'hello'
# Translation: "I can't turn 'hello' into a number"
```

```python
# RIGHT - Check if it looks like a number
user_input = "hello"
if user_input.isdigit():
    number = int(user_input)
else:
    print("Please enter a valid number")
```

### ZeroDivisionError: Division by Zero

```python
# WRONG - Can't divide by zero
result = 10 / 0

# ZeroDivisionError: division by zero
# Translation: "You can't divide by zero - it's undefined in math!"
```

```python
# RIGHT - Check before dividing
def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print(safe_divide(10, 0))  # "Cannot divide by zero"
print(safe_divide(10, 2))  # 5.0
```

### FileNotFoundError: Missing File

```python
# WRONG - File doesn't exist
with open("nonexistent.txt", "r") as f:
    content = f.read()

# FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent.txt'
```

```python
# RIGHT - Check if file exists first
import os

filename = "nonexistent.txt"
if os.path.exists(filename):
    with open(filename, "r") as f:
        content = f.read()
else:
    print(f"File '{filename}' not found")
```

### Import Errors: Can't Find Module

```python
# WRONG - Module doesn't exist
import nonexistent_module

# ModuleNotFoundError: No module named 'nonexistent_module'
```

```python
# RIGHT - Make sure module is installed
# Check: pip install module_name
import os  # Built-in, always available
import sys  # Built-in, always available
```

### Runtime Error Quick Reference

| Error | Meaning | Example Fix |
|-------|---------|-------------|
| `TypeError` | Wrong type of data | Convert types: `str(5)` |
| `NameError` | Variable doesn't exist | Check spelling and scope |
| `AttributeError` | Wrong method/attribute | Check documentation |
| `IndexError` | Position doesn't exist | Check `len()` first |
| `KeyError` | Dictionary key missing | Use `.get()` method |
| `ValueError` | Value is wrong | Validate input first |
| `ZeroDivisionError` | Dividing by zero | Check if denominator is 0 |
| `FileNotFoundError` | File doesn't exist | Check `os.path.exists()` |

---

## Part 3: Logic Errors (Silent But Wrong)

Logic errors are the trickiest because Python doesn't crash - it just gives the wrong answer.

### Off-by-One Errors

```python
# WRONG - Misses last element
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers) - 1):  # range(4) → 0,1,2,3
    print(numbers[i])  # Misses numbers[4]!

# Output: 1, 2, 3, 4 (5 is missing!)
```

```python
# RIGHT - Include all elements
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):  # range(5) → 0,1,2,3,4
    print(numbers[i])

# Even better - iterate directly
for num in numbers:
    print(num)
```

### Wrong Comparison Operators

```python
# WRONG - Excludes boundary values
def is_valid_age(age):
    if age > 0 and age < 120:  # Excludes 0 and 120!
        return True
    return False

print(is_valid_age(0))    # False (should be True)
print(is_valid_age(120))  # False (should be True)
```

```python
# RIGHT - Include boundaries
def is_valid_age_fixed(age):
    return 0 <= age <= 120  # Includes 0 and 120!

print(is_valid_age_fixed(0))    # True
print(is_valid_age_fixed(120))  # True
```

### Floating Point Precision

```python
# WRONG - Floating point surprise
a = 0.1 + 0.2
b = 0.3
print(a == b)  # False! (a is 0.30000000000000004)
```

```python
# RIGHT - Use tolerance for float comparison
def float_equal(a, b, tolerance=0.0000001):
    return abs(a - b) < tolerance

print(float_equal(0.1 + 0.2, 0.3))  # True
```

### Infinite Loops

```python
# WRONG - Counter never changes
count = 0
while count < 10:
    print(count)
    # Forgot: count += 1

# Runs forever! (Press Ctrl+C to stop)
```

```python
# RIGHT - Increment the counter
count = 0
while count < 10:
    print(count)
    count += 1  # Now it will stop at 10
```

### Modifying List While Iterating

```python
# WRONG - Skips elements
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:  # If even
        numbers.remove(num)  # This causes skipping!

print(numbers)  # [1, 3, 5] - wait, that's actually right?

# Try with [2, 4, 6, 8, 10]
numbers = [2, 4, 6, 8, 10]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)
print(numbers)  # [4, 8] - Wrong! Should be empty!
```

```python
# RIGHT - Create new list
def remove_evens(numbers):
    return [num for num in numbers if num % 2 != 0]

numbers = [2, 4, 6, 8, 10]
result = remove_evens(numbers)
print(result)  # [] - Correct!
```

### Wrong Average Calculation

```python
# WRONG - Integer division in Python 2 style
# (In Python 3 this actually works, but let's show the concept)
def average(a, b):
    return (a + b) / 2  # This is correct in Python 3

# But watch out for:
def average_three(a, b, c):
    return a + b + c / 3  # WRONG! Only divides c by 3
```

```python
# RIGHT - Use parentheses
def average_three_fixed(a, b, c):
    return (a + b + c) / 3  # Divides sum by 3
```

---

## Part 4: Defensive Programming (Preventing Errors)

Defensive programming means writing code that anticipates problems and handles them gracefully.

### Validate Inputs

```python
def calculate_rectangle_area(width, height):
    """Calculate area with validation."""

    # Check types
    if not isinstance(width, (int, float)):
        raise TypeError(f"Width must be a number, got {type(width)}")
    if not isinstance(height, (int, float)):
        raise TypeError(f"Height must be a number, got {type(height)}")

    # Check values
    if width <= 0:
        raise ValueError(f"Width must be positive, got {width}")
    if height <= 0:
        raise ValueError(f"Height must be positive, got {height}")

    return width * height

# Test
try:
    area = calculate_rectangle_area(5, 10)
    print(f"Area: {area}")
except (TypeError, ValueError) as e:
    print(f"Error: {e}")
```

### Safe Access Functions

```python
def safe_list_get(items, index, default=None):
    """Get list item safely."""
    try:
        return items[index]
    except IndexError:
        return default

# Usage
numbers = [1, 2, 3]
print(safe_list_get(numbers, 0))      # 1
print(safe_list_get(numbers, 100))    # None (instead of crash)
print(safe_list_get(numbers, 100, 0)) # 0 (custom default)
```

```python
def safe_int_convert(value, default=0):
    """Convert to int safely."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

# Usage
print(safe_int_convert("42"))        # 42
print(safe_int_convert("hello"))     # 0
print(safe_int_convert("hello", -1)) # -1
```

### Check Before Acting

```python
# Check if key exists
def get_user_email(user_data):
    if "email" not in user_data:
        return "No email provided"
    return user_data["email"]

# Check if file exists
import os

def read_file_safely(filename):
    if not os.path.exists(filename):
        return None, "File not found"
    try:
        with open(filename, 'r') as f:
            return f.read(), None
    except Exception as e:
        return None, str(e)
```

---

## Part 5: Error Handling Patterns

### Try-Except Blocks

```python
def read_number_from_file(filename):
    """Read a number from file with error handling."""
    try:
        with open(filename, 'r') as f:
            content = f.read()
            number = int(content)
            return number
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return None
    except ValueError:
        print(f"File doesn't contain a valid number")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Usage
result = read_number_from_file("data.txt")
if result is not None:
    print(f"Number: {result}")
```

### Graceful Degradation

```python
def load_configuration(filename="config.json"):
    """Load config with fallback to defaults."""
    import json
    import os

    # Try to load from file
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            print(f"Warning: Could not load {filename}")

    # Fallback to default configuration
    return {
        "debug": False,
        "port": 8080,
        "host": "localhost"
    }

# This always works, even if file is missing
config = load_configuration()
print(f"Running on port {config['port']}")
```

### Retry Logic

```python
import time
import random

def unreliable_operation():
    """Simulates a sometimes-failing operation."""
    if random.random() < 0.7:  # 70% failure rate
        raise Exception("Network timeout")
    return "Success!"

def retry_operation(max_attempts=3, delay=1):
    """Try operation multiple times."""
    for attempt in range(max_attempts):
        try:
            return unreliable_operation()
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_attempts - 1:
                time.sleep(delay)

    raise Exception(f"Failed after {max_attempts} attempts")

# Usage
try:
    result = retry_operation()
    print(f"Success: {result}")
except Exception as e:
    print(f"Failed: {e}")
```

---

## Common Beginner Mistakes

### Mistake 1: Ignoring Error Messages

```python
# When you see:
# AttributeError: 'list' object has no attribute 'append'
#                         ^^^^^^^^^
# Check if you spelled 'append' correctly

# When you see:
# IndexError: list index out of range
#                   ^^^^^^^^^^^^^^^^
# Check if your index is too big
```

**Read error messages from bottom to top!** The last line is the most specific.

### Mistake 2: Using Bare Except

```python
# WRONG - Catches everything, including Ctrl+C
try:
    risky_operation()
except:
    print("Something went wrong")

# RIGHT - Catch specific exceptions
try:
    risky_operation()
except ValueError as e:
    print(f"Value error: {e}")
except FileNotFoundError:
    print("File not found")
```

### Mistake 3: Swallowing Errors

```python
# WRONG - Hiding errors makes debugging hard
try:
    result = calculate_something()
except:
    pass  # Error silently ignored!

# RIGHT - At minimum, log the error
import logging

try:
    result = calculate_something()
except Exception as e:
    logging.error(f"Calculation failed: {e}")
    result = None
```

### Mistake 4: Not Testing Edge Cases

```python
# WRONG - Only test "normal" case
def find_max(numbers):
    max_val = numbers[0]  # What if list is empty?
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

# RIGHT - Handle edge cases
def find_max_safe(numbers):
    if not numbers:
        return None  # Or raise ValueError
    return max(numbers)  # Or implement safely
```

---

## Practice Exercises

### Exercise 1: Fix Syntax Errors

This code has 3 syntax errors. Find and fix them:

```python
def greet(name
    print "Hello " + name
    return True

greet("World")
```

### Exercise 2: Fix Runtime Errors

Fix the runtime errors in this code:

```python
def process_data(data):
    first_item = data[0]  # What if data is empty?
    number = int(data)    # What if data isn't a number?
    result = 10 / number  # What if number is 0?
    return result

print(process_data([]))
print(process_data("hello"))
print(process_data("0"))
```

### Exercise 3: Fix Logic Errors

Find and fix the logic errors:

```python
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total = num  # Bug here
    return total / len(numbers)

print(calculate_average([1, 2, 3]))  # Should be 2.0
```

### Exercise 4: Write Defensive Code

Write a function that safely:
1. Takes a string that should be a number
2. Converts it to an integer
3. Returns the double
4. Handles all possible errors gracefully

```python
def safe_double(value):
    # Your code here
    pass

# Test cases:
print(safe_double("5"))      # Should return 10
print(safe_double("abc"))    # Should return "Invalid number"
print(safe_double(None))    # Should return "Invalid input"
```

---

## Key Takeaways

1. **Syntax errors** prevent code from running - fix grammar first
2. **Runtime errors** crash during execution - use try-except or validate inputs
3. **Logic errors** give wrong results - test thoroughly with edge cases
4. **Read error messages carefully** - they point to the problem
5. **Use defensive programming** - validate inputs and expect errors
6. **Test edge cases** - empty lists, zero values, huge numbers

## Quick Reference: Error Message Translation

| Python Says | Translation |
|-------------|-------------|
| `SyntaxError: invalid syntax` | Check for missing colons, quotes, or brackets |
| `NameError: name 'x' is not defined` | Variable doesn't exist - check spelling |
| `TypeError: unsupported operand type` | Wrong types - can't add string + int |
| `IndexError: list index out of range` | Index too big - check `len(list)` |
| `KeyError: 'name'` | Dictionary key doesn't exist - use `.get()` |
| `AttributeError: 'list' has no attribute 'x'` | Wrong method - check what type it is |
| `ValueError: invalid literal for int()` | Can't convert to number - use `.isdigit()` |
| `ZeroDivisionError: division by zero` | Check if denominator is 0 |
| `FileNotFoundError` | File doesn't exist - check path |

## Error Prevention Checklist

- [ ] Did I test with empty inputs?
- [ ] Did I test with zero values?
- [ ] Did I test with very large values?
- [ ] Did I check for None/Null cases?
- [ ] Did I validate user inputs?
- [ ] Did I use try-except for risky operations?
- [ ] Did I provide meaningful error messages?
- [ ] Did I log errors for debugging?

---

## Further Reading

- **Next Lesson**: Exception Handling - How to use try-except properly
- **Practice**: Write 10 functions with comprehensive error handling
- **Challenge**: Create a robust file parser that handles all edge cases
- **Explore**: Learn about Python's exception hierarchy
