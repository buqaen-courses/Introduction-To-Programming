# Exception Handling: Catching and Managing Errors

## Introduction: What Are Exceptions?

An **exception** is an event that disrupts the normal flow of a program. When Python encounters a problem it can't handle, it "raises" an exception. Your job is to "catch" these exceptions and handle them gracefully.

### The Exception Metaphor

Think of exceptions like catching a ball:
- Someone **throws** (raises) the ball
- You **catch** (handle) the ball
- Or the ball hits the ground (program crashes)

```python
# Without exception handling - program crashes
number = int("not a number")  # ValueError - program stops!
print("This never runs")      # Never reached

# With exception handling - program recovers
try:
    number = int("not a number")
except ValueError:
    print("Please enter a valid number")  # Graceful recovery
print("Program continues...")             # This runs!
```

---

## Part 1: Basic Try-Except

### The Simplest Form

```python
try:
    # Code that might fail
    result = 10 / 0
except ZeroDivisionError:
    # Code that runs if it fails
    print("Can't divide by zero!")

print("Program keeps running...")
```

**How it works:**
1. Python tries the code in the `try` block
2. If an error occurs, it looks for a matching `except`
3. If found, it runs that code and continues
4. If not found, the program crashes

### Catching Specific Exceptions

```python
def safe_divide(a, b):
    """Divide two numbers safely."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Both must be numbers"

# Test
print(safe_divide(10, 2))      # 5.0
print(safe_divide(10, 0))      # "Cannot divide by zero"
print(safe_divide(10, "2"))    # "Both must be numbers"
```

### Getting Error Details

```python
try:
    number = int("hello")
except ValueError as e:  # 'e' contains the error message
    print(f"Error occurred: {e}")
    print(f"Error type: {type(e).__name__}")

# Output:
# Error occurred: invalid literal for int() with base 10: 'hello'
# Error type: ValueError
```

---

## Part 2: The Full Exception Structure

### try-except-else-finally

```python
try:
    # Try this first
    print("Attempting to open file...")
    with open("data.txt", "r") as f:
        content = f.read()

except FileNotFoundError:
    # Runs if FileNotFoundError occurs
    print("File not found!")
    content = None

else:
    # Runs ONLY if no exception occurred
    print("File read successfully!")
    print(f"Content: {content[:50]}...")

finally:
    # ALWAYS runs (whether exception or not)
    print("Cleanup complete")

print("Program continues...")
```

### Execution Flow

```
Scenario 1: No errors
    try → (success) → else → finally → continue

Scenario 2: Error occurs and is caught
    try → (error) → except → finally → continue

Scenario 3: Error occurs, no matching except
    try → (error) → finally → CRASH
```

### Practical Example: File Processing

```python
def process_user_file(filename):
    """Process user data from file with full error handling."""
    users = []

    try:
        print(f"Opening {filename}...")
        with open(filename, 'r') as f:
            lines = f.readlines()

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return []

    except PermissionError:
        print(f"Error: No permission to read '{filename}'")
        return []

    else:
        # File opened successfully
        print(f"Processing {len(lines)} lines...")

        for line_num, line in enumerate(lines, 1):
            try:
                name, age = line.strip().split(',')
                users.append({"name": name, "age": int(age)})
            except ValueError:
                print(f"Warning: Invalid data on line {line_num}: {line.strip()}")

        print(f"Successfully loaded {len(users)} users")
        return users

    finally:
        # This always runs
        print("Processing complete")

# Usage
users = process_user_file("users.txt")
```

---

## Part 3: Common Exception Types

### The Exception Family Tree

```
BaseException
├── SystemExit          (raised by sys.exit())
├── KeyboardInterrupt   (Ctrl+C)
└── Exception           (this is what we usually catch)
    ├── ArithmeticError
    │   └── ZeroDivisionError
    ├── LookupError
    │   ├── IndexError       (list index too big)
    │   └── KeyError         (dict key missing)
    ├── TypeError            (wrong type)
    ├── ValueError           (wrong value)
    ├── FileNotFoundError
    └── ... many more
```

### Most Common Exceptions You'll Meet

| Exception | When It Happens | Example |
|-----------|-----------------|---------|
| `ZeroDivisionError` | Dividing by zero | `10 / 0` |
| `ValueError` | Wrong value for operation | `int("abc")` |
| `TypeError` | Operation on wrong type | `"hello" + 5` |
| `IndexError` | List index doesn't exist | `[1,2,3][10]` |
| `KeyError` | Dictionary key missing | `{"a":1}["b"]` |
| `FileNotFoundError` | File doesn't exist | `open("missing.txt")` |
| `NameError` | Variable doesn't exist | `print(undefined)` |
| `AttributeError` | Object has no attribute | `"hi".nonexistent()` |

### Catching Multiple Exceptions

```python
# Method 1: Separate except blocks
def load_data(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File {filename} not found")
    except json.JSONDecodeError:
        print(f"File {filename} contains invalid JSON")
    except PermissionError:
        print(f"No permission to read {filename}")

# Method 2: Group related exceptions
def load_data_v2(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Cannot access file: {e}")
    except json.JSONDecodeError:
        print(f"Invalid JSON in file")

# Method 3: Catch all (use carefully!)
def load_data_v3(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except Exception as e:  # Catches everything
        print(f"Something went wrong: {e}")
```

---

## Part 4: Raising Your Own Exceptions

### When to Raise Exceptions

Raise exceptions when:
- Invalid arguments are passed to your function
- A required condition isn't met
- Something unexpected happens that callers should know about

### Basic Raising

```python
def validate_age(age):
    """Validate age and raise exception if invalid."""
    if not isinstance(age, int):
        raise TypeError(f"Age must be integer, got {type(age)}")

    if age < 0:
        raise ValueError(f"Age cannot be negative, got {age}")

    if age > 150:
        raise ValueError(f"Age seems unrealistic: {age}")

# Usage
try:
    validate_age("twenty")  # Raises TypeError
except TypeError as e:
    print(f"Type error: {e}")

try:
    validate_age(-5)  # Raises ValueError
except ValueError as e:
    print(f"Value error: {e}")
```

### Creating Custom Exceptions

```python
# Define custom exception
class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds."""
    pass

class InvalidAmountError(Exception):
    """Raised when amount is invalid."""
    pass

# Bank account example
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        """Withdraw money with validation."""
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive")

        if amount > self.balance:
            raise InsufficientFundsError(
                f"Balance ${self.balance} is less than ${amount}"
            )

        self.balance -= amount
        return self.balance

# Usage
account = BankAccount(100)

try:
    account.withdraw(150)  # Will raise InsufficientFundsError
except InsufficientFundsError as e:
    print(f"Cannot withdraw: {e}")
except InvalidAmountError as e:
    print(f"Invalid amount: {e}")
```

### Advanced Custom Exceptions

```python
class ValidationError(Exception):
    """Base class for validation errors."""
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")

class InvalidEmailError(ValidationError):
    """Raised when email format is invalid."""
    def __init__(self, email):
        super().__init__("email", f"'{email}' is not a valid email")

class InvalidPasswordError(ValidationError):
    """Raised when password doesn't meet requirements."""
    def __init__(self, reason):
        super().__init__("password", reason)

# Usage
def validate_user(email, password):
    if "@" not in email:
        raise InvalidEmailError(email)

    if len(password) < 8:
        raise InvalidPasswordError("must be at least 8 characters")

try:
    validate_user("invalid-email", "short")
except ValidationError as e:
    print(f"Validation failed on field '{e.field}': {e.message}")
```

---

## Part 5: Resource Management with Context Managers

### The Problem: Resource Cleanup

```python
# Without context manager - cleanup might be missed
def read_file_bad(filename):
    file = open(filename, 'r')
    try:
        data = file.read()
        return data
    except Exception:
        return None
    # If exception occurs, file might not close!
    file.close()

# With try-finally - guaranteed cleanup
def read_file_okay(filename):
    file = open(filename, 'r')
    try:
        data = file.read()
        return data
    finally:
        # This ALWAYS runs, even if exception
        file.close()
```

### The Solution: with Statement

```python
# Best way: context manager
def read_file_good(filename):
    with open(filename, 'r') as file:
        data = file.read()
        return data
    # File automatically closed here!
```

### How Context Managers Work

```python
class DatabaseConnection:
    """Example of a custom context manager."""

    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None

    def __enter__(self):
        # Called when entering 'with' block
        print(f"Connecting to {self.connection_string}...")
        self.connection = "DatabaseConnection"
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Called when exiting 'with' block
        # Runs even if exception occurred
        print("Closing connection...")
        self.connection = None
        # Return False to propagate exception, True to suppress
        return False

# Usage
with DatabaseConnection("localhost:5432") as conn:
    print(f"Using connection: {conn}")
    # If error happens here, __exit__ still runs
# Connection automatically closed
```

### Multiple Context Managers

```python
# Processing data from one file to another
with open("input.txt", "r") as input_file, \
     open("output.txt", "w") as output_file:

    for line in input_file:
        processed = line.upper()
        output_file.write(processed)

# Both files automatically closed
```

---

## Part 6: Best Practices

### 1. Be Specific About Exceptions

```python
# BAD - Catches everything, including KeyboardInterrupt (Ctrl+C)
try:
    do_something()
except:  # Bare except - bad!
    print("Error")

# BETTER - Catch specific exceptions
try:
    do_something()
except ValueError:
    print("Invalid value")
except FileNotFoundError:
    print("File not found")

# OKAY - If you really need to catch all
try:
    do_something()
except Exception as e:  # Explicitly catch Exception
    print(f"Unexpected error: {e}")
```

### 2. Don't Swallow Errors Silently

```python
# BAD - Error is hidden
try:
    result = risky_operation()
except:
    pass  # Error disappears!

# GOOD - At minimum log the error
import logging

try:
    result = risky_operation()
except Exception as e:
    logging.error(f"Operation failed: {e}")
    # Or re-raise if you can't handle it
    raise
```

### 3. Use else for Success-Only Code

```python
# Without else
try:
    data = fetch_data()
    process_data(data)  # What if fetch_data raises?
except NetworkError:
    print("Network failed")

# With else - clearer separation
try:
    data = fetch_data()
except NetworkError:
    print("Network failed")
else:
    # Only runs if no exception
    process_data(data)
```

### 4. Chain Exceptions for Context

```python
# Without chaining - loses original error info
def parse_config(text):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        raise ValueError("Invalid configuration")

# With chaining - preserves original error
def parse_config_better(text):
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        raise ValueError("Invalid configuration") from e

# Result shows full chain:
# ValueError: Invalid configuration
# from JSONDecodeError: Expecting property name...
```

### 5. Don't Use Exceptions for Control Flow

```python
# BAD - Using exceptions for normal logic
items = [1, 2, 3]
try:
    while True:
        item = items.pop()
        process(item)
except IndexError:
    pass  # List is empty - this is normal!

# BETTER - Use normal control flow
items = [1, 2, 3]
while items:
    item = items.pop()
    process(item)
```

---

## Part 7: Practical Examples

### Example 1: Safe User Input

```python
def get_integer_input(prompt, min_val=None, max_val=None):
    """Get integer from user with validation."""
    while True:
        try:
            value = input(prompt)
            number = int(value)

            if min_val is not None and number < min_val:
                print(f"Please enter a number >= {min_val}")
                continue

            if max_val is not None and number > max_val:
                print(f"Please enter a number <= {max_val}")
                continue

            return number

        except ValueError:
            print("That's not a valid number. Please try again.")

# Usage
age = get_integer_input("Enter your age: ", min_val=0, max_val=150)
quantity = get_integer_input("How many items? ", min_val=1)
```

### Example 2: Robust File Operations

```python
import os
import json
from datetime import datetime

def backup_data(source_file, backup_dir="backups"):
    """Backup data file with comprehensive error handling."""
    try:
        # Validate source exists
        if not os.path.exists(source_file):
            raise FileNotFoundError(f"Source file not found: {source_file}")

        # Ensure backup directory exists
        os.makedirs(backup_dir, exist_ok=True)

        # Create backup filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.basename(source_file)
        backup_file = os.path.join(backup_dir, f"{filename}.{timestamp}.bak")

        # Read and backup
        with open(source_file, 'r') as src:
            data = src.read()

        with open(backup_file, 'w') as dst:
            dst.write(data)

        print(f"Backup created: {backup_file}")
        return backup_file

    except PermissionError:
        print(f"Error: No permission to access files")
        return None
    except IOError as e:
        print(f"IO error during backup: {e}")
        return None

# Usage
backup_data("important_data.json")
```

### Example 3: API Call with Retry

```python
import time
import random

def unreliable_api_call():
    """Simulate API that sometimes fails."""
    if random.random() < 0.7:  # 70% failure rate
        raise ConnectionError("Network timeout")
    return {"status": "success", "data": "api_response"}

def call_api_with_retry(max_attempts=3, delay=1):
    """Call API with exponential backoff retry."""
    for attempt in range(max_attempts):
        try:
            result = unreliable_api_call()
            print(f"Success on attempt {attempt + 1}")
            return result

        except ConnectionError as e:
            print(f"Attempt {attempt + 1} failed: {e}")

            if attempt < max_attempts - 1:
                wait_time = delay * (2 ** attempt)  # 1, 2, 4 seconds
                print(f"Waiting {wait_time} seconds before retry...")
                time.sleep(wait_time)
            else:
                print("All attempts failed")
                raise  # Re-raise the last error

# Usage
try:
    result = call_api_with_retry()
    print(f"API result: {result}")
except ConnectionError:
    print("Could not reach API after multiple attempts")
```

---

## Part 8: Testing Exception Handling

### Testing That Exceptions Are Raised

```python
def test_exceptions():
    """Test that functions raise correct exceptions."""

    # Test 1: Division by zero raises ZeroDivisionError
    try:
        result = 10 / 0
        assert False, "Should have raised ZeroDivisionError"
    except ZeroDivisionError:
        print("✓ ZeroDivisionError raised correctly")

    # Test 2: Invalid conversion raises ValueError
    try:
        number = int("not a number")
        assert False, "Should have raised ValueError"
    except ValueError:
        print("✓ ValueError raised correctly")

    # Test 3: Your function raises expected exception
    def validate_positive(number):
        if number <= 0:
            raise ValueError("Number must be positive")
        return number

    try:
        validate_positive(-5)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "positive" in str(e)
        print("✓ Custom validation raises correct exception")

# Run tests
test_exceptions()
```

### Testing Exception Handling

```python
def safe_divide(a, b):
    """Divide with error handling."""
    try:
        return a / b
    except ZeroDivisionError:
        return None
    except TypeError:
        return "Invalid types"

def test_safe_divide():
    """Test that safe_divide handles errors correctly."""

    # Normal case
    result = safe_divide(10, 2)
    assert result == 5.0, f"Expected 5.0, got {result}"
    print("✓ Normal division works")

    # Zero division handled
    result = safe_divide(10, 0)
    assert result is None, f"Expected None, got {result}"
    print("✓ Division by zero handled")

    # Type error handled
    result = safe_divide(10, "2")
    assert result == "Invalid types", f"Expected 'Invalid types', got {result}"
    print("✓ Type error handled")

# Run tests
test_safe_divide()
```

---

## Common Beginner Mistakes

### Mistake 1: Catching Everything

```python
# BAD - Can't even stop the program with Ctrl+C
try:
    long_running_operation()
except:
    print("Something happened")

# RIGHT - Be specific
try:
    long_running_operation()
except NetworkError:
    print("Network problem")
except TimeoutError:
    print("Operation timed out")
```

### Mistake 2: Losing Error Information

```python
# BAD - Original error is lost
try:
    data = parse_json(raw_data)
except json.JSONDecodeError:
    raise ValueError("Parse failed")  # Original error info lost!

# RIGHT - Chain exceptions
try:
    data = parse_json(raw_data)
except json.JSONDecodeError as e:
    raise ValueError("Parse failed") from e
```

### Mistake 3: Using Exceptions for Normal Flow

```python
# BAD - Exceptions are slow and unclear
items = [1, 2, 3]
try:
    while True:
        item = items.pop()
        process(item)
except IndexError:
    pass  # List is empty - this is normal!

# RIGHT - Use normal control flow
items = [1, 2, 3]
while items:
    item = items.pop()
    process(item)
```

### Mistake 4: Not Cleaning Up Resources

```python
# BAD - File might not close
def process_file(filename):
    file = open(filename, 'r')
    return file.read()
    file.close()  # Never reached!

# RIGHT - Use context manager
def process_file(filename):
    with open(filename, 'r') as file:
        return file.read()
    # Automatically closed
```

---

## Practice Exercises

### Exercise 1: Safe Calculator

Create a calculator that handles all errors gracefully:

```python
def safe_calculator():
    """
    Get two numbers and operation from user.
    Handle all possible errors.
    """
    # Your code here
    pass

# Should handle:
# - Invalid numbers
# - Division by zero
# - Unknown operations
# - Keyboard interrupt (Ctrl+C)
```

### Exercise 2: File Processor

Write a function that reads a file and processes each line, handling all errors:

```python
def process_data_file(filename):
    """
    Read file, convert each line to integer, return sum.
    Handle: file not found, permission denied, invalid data.
    """
    # Your code here
    pass
```

### Exercise 3: Custom Exceptions

Create a login system with custom exceptions:

```python
class AuthenticationError(Exception):
    pass

class InvalidCredentialsError(AuthenticationError):
    pass

class AccountLockedError(AuthenticationError):
    pass

def login(username, password):
    """
    Authenticate user.
    Raise appropriate exceptions for different failures.
    """
    # Your code here
    pass
```

---

## Key Takeaways

1. **Try-except** prevents crashes and enables graceful recovery
2. **Be specific** - catch particular exceptions, not everything
3. **Use else** for code that runs only when no exception occurs
4. **Use finally** for cleanup that always runs
5. **Context managers** (with statement) handle resources automatically
6. **Raise exceptions** to signal problems in your own code
7. **Custom exceptions** make error handling clearer
8. **Don't use exceptions** for normal program flow

## Quick Reference Card

| Pattern | Syntax | When to Use |
|---------|--------|-------------|
| Basic | `try...except Error` | Catch specific errors |
| With message | `except Error as e` | Need error details |
| Multiple | `except (A, B)` | Same handling for multiple |
| Success only | `else` | Code that needs success |
| Cleanup | `finally` | Always run this code |
| All | `except Exception` | Last resort, log and re-raise |
| Resources | `with` statement | Automatic cleanup |

---

## Further Reading

- **Next**: Session 19 - Working with Files
- **Practice**: Add exception handling to all your existing functions
- **Challenge**: Create a robust command-line tool that never crashes
- **Explore**: Look up Python's full exception hierarchy
