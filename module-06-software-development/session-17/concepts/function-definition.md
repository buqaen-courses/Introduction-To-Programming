# Function Definition: Creating Reusable Code

## What is a Function?

A **function** is a reusable block of code that performs a specific task. Think of it like a mini-program within your program - you give it some input, it does work, and (optionally) gives you back a result.

### Real-World Analogy

Functions are like kitchen appliances:
- **Toaster**: Put in bread → Get toast
- **Blender**: Put in ingredients → Get smoothie
- **Function**: Put in data → Get result

### Why Use Functions?

1. **Reusability**: Write once, use many times
2. **Organization**: Break big problems into smaller pieces
3. **Readability**: Give complex operations meaningful names
4. **Testing**: Test small pieces independently
5. **Collaboration**: Different people can work on different functions

---

## Basic Function Syntax

### Defining a Simple Function

```python
# Function definition
def say_hello():
    """This is a docstring - explains what the function does."""
    print("Hello, World!")

# Function call (using the function)
say_hello()
say_hello()
```

### Function Anatomy

```
def function_name():
    """Documentation (optional but recommended)"""
    # Function body
    # Code that runs when called
    return  # Optional - sends back a value
```

| Part | Purpose | Example |
|------|---------|---------|
| `def` | Tells Python you're defining a function | `def` |
| `function_name` | How you call the function | `say_hello` |
| `()` | Holds parameters (inputs) | `(name, age)` |
| `:` | Ends the definition line | `:` |
| Indentation | Marks code inside function | 4 spaces |
| Docstring | Explains what function does | `"""Greets user"""` |
| `return` | Sends back a result | `return 42` |

---

## Functions with Parameters

### Single Parameter

```python
def greet(name):
    """Greet a person by name."""
    print(f"Hello, {name}!")

# Call with argument
greet("Alice")    # Output: Hello, Alice!
greet("Bob")      # Output: Hello, Bob!
```

### Multiple Parameters

```python
def introduce(first_name, last_name, age):
    """Introduce a person."""
    print(f"This is {first_name} {last_name}, who is {age} years old.")

# Call with multiple arguments (order matters!)
introduce("Alice", "Smith", 25)
# Output: This is Alice Smith, who is 25 years old.
```

**Important**: Arguments must be provided in the same order as parameters!

### Default Parameters

```python
def greet_with_time(name, time="morning"):
    """Greet someone with time of day."""
    print(f"Good {time}, {name}!")

# Call with both arguments
greet_with_time("Alice", "evening")   # Good evening, Alice!

# Call with just required argument (uses default)
greet_with_time("Bob")                 # Good morning, Bob!

# Call with keyword arguments
greet_with_time("Charlie", time="afternoon")  # Good afternoon, Charlie!
```

**Best Practice**: Put default parameters AFTER required parameters!

```python
# WRONG
def wrong_order(time="morning", name):
    pass  # SyntaxError!

# RIGHT
def correct_order(name, time="morning"):
    pass  # Works!
```

---

## Returning Values

### Returning a Single Value

```python
def calculate_square(number):
    """Return the square of a number."""
    result = number ** 2
    return result

# Capture the returned value
answer = calculate_square(5)
print(answer)        # 25

# Use directly in expression
total = calculate_square(3) + calculate_square(4)
print(total)        # 9 + 16 = 25
```

### Returning Multiple Values

```python
def get_circle_info(radius):
    """Return area and circumference of a circle."""
    import math
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

# Unpack multiple return values
area, circumference = get_circle_info(5)
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")

# Or get as tuple
result = get_circle_info(5)
print(result)        # (78.54..., 31.41...)
```

### Early Returns

```python
def divide_safely(a, b):
    """Divide two numbers with error checking."""
    # Check for division by zero first
    if b == 0:
        return "Error: Cannot divide by zero"

    # Check for valid types
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Error: Both must be numbers"

    # If we get here, inputs are valid
    return a / b

# Test
print(divide_safely(10, 2))      # 5.0
print(divide_safely(10, 0))      # Error message
print(divide_safely(10, "2"))    # Error message
```

---

## Variable Scope: Local vs Global

### Local Variables (Inside Function)

```python
def calculate_area(length, width):
    """Calculate rectangle area."""
    area = length * width   # 'area' is LOCAL to this function
    return area

result = calculate_area(5, 3)
print(result)           # 15

# This would cause an error:
# print(area)           # NameError! 'area' is not defined here
```

Variables created inside a function only exist inside that function!

### Global Variables (Outside Function)

```python
# Global variable
counter = 0

def increment():
    """Increment the global counter."""
    global counter          # Tell Python we mean the global one
    counter += 1
    print(f"Counter is now: {counter}")

increment()     # Counter is now: 1
increment()     # Counter is now: 2
print(counter)  # 2
```

**Best Practice**: Avoid global variables when possible. Pass data as parameters instead!

### Better Alternative to Global Variables

```python
# Instead of global state, pass and return values
def increment_counter(current):
    """Return incremented counter."""
    return current + 1

# Usage
counter = 0
counter = increment_counter(counter)   # 1
counter = increment_counter(counter)   # 2
```

---

## Documenting Functions

### Docstrings

```python
def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index (BMI).

    Parameters:
        weight_kg (float): Weight in kilograms
        height_m (float): Height in meters

    Returns:
        float: BMI value

    Raises:
        ValueError: If weight or height are not positive

    Example:
        >>> calculate_bmi(70, 1.75)
        22.86
    """
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Weight and height must be positive")

    return weight_kg / (height_m ** 2)

# Access docstring
print(calculate_bmi.__doc__)
```

### Type Hints (Optional but Helpful)

```python
def greet(name: str, age: int) -> str:
    """
    Create a greeting message.

    Args:
        name: Person's name
        age: Person's age

    Returns:
        Formatted greeting string
    """
    return f"Hello {name}, you are {age} years old!"

# Type hints don't enforce types, but help with:
# - Documentation
# - IDE autocomplete
# - Code readability
```

---

## Practical Examples

### Example 1: Input Validator

```python
def get_valid_number(prompt, min_value=None, max_value=None):
    """
    Get a valid number from user.

    Args:
        prompt: Message to show user
        min_value: Minimum allowed value
        max_value: Maximum allowed value

    Returns:
        Valid number
    """
    while True:
        try:
            value = float(input(prompt))

            if min_value is not None and value < min_value:
                print(f"Please enter a value >= {min_value}")
                continue

            if max_value is not None and value > max_value:
                print(f"Please enter a value <= {max_value}")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")

# Usage
age = get_valid_number("Enter your age: ", min_value=0, max_value=150)
```

### Example 2: Grade Calculator

```python
def calculate_letter_grade(score):
    """
    Convert numeric score to letter grade.

    Args:
        score: Numeric score (0-100)

    Returns:
        Letter grade (A, B, C, D, F)
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def calculate_statistics(grades):
    """
    Calculate grade statistics.

    Args:
        grades: List of numeric grades

    Returns:
        Dictionary with statistics
    """
    if not grades:
        return None

    return {
        "count": len(grades),
        "average": sum(grades) / len(grades),
        "highest": max(grades),
        "lowest": min(grades),
        "letter_grades": [calculate_letter_grade(g) for g in grades]
    }

# Usage
scores = [85, 92, 78, 96, 88]
stats = calculate_statistics(scores)
print(f"Average: {stats['average']:.1f}")
print(f"Grades: {', '.join(stats['letter_grades'])}")
```

### Example 3: Password Generator

```python
import random
import string

def generate_password(length=12, use_upper=True, use_numbers=True, use_special=True):
    """
    Generate a random password.

    Args:
        length: Password length
        use_upper: Include uppercase letters
        use_numbers: Include numbers
        use_special: Include special characters

    Returns:
        Generated password string
    """
    chars = string.ascii_lowercase

    if use_upper:
        chars += string.ascii_uppercase
    if use_numbers:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    return ''.join(random.choice(chars) for _ in range(length))

# Usage
print(generate_password())                    # Default 12 chars
print(generate_password(16, use_special=False))  # 16 chars, no specials
```

### Example 4: Menu System

```python
def show_menu(options):
    """
    Display a menu and get user choice.

    Args:
        options: Dictionary of {choice_number: description}

    Returns:
        User's choice as string
    """
    print("\n" + "="*30)
    for num, desc in options.items():
        print(f"{num}. {desc}")
    print("="*30)

    while True:
        choice = input("Enter your choice: ")
        if choice in options:
            return choice
        print("Invalid choice. Please try again.")

# Usage
options = {
    "1": "View balance",
    "2": "Deposit money",
    "3": "Withdraw money",
    "4": "Exit"
}

# Uncomment to run:
# choice = show_menu(options)
# print(f"You chose: {options[choice]}")
```

---

## Common Beginner Mistakes

### Mistake 1: Forgetting to Call the Function

```python
def say_hello():
    print("Hello!")

# WRONG - just references the function, doesn't call it
say_hello

# RIGHT - actually calls the function
say_hello()
```

### Mistake 2: Forgetting `return`

```python
# WRONG - doesn't return the result
def add(a, b):
    result = a + b   # Calculates but doesn't return!

answer = add(2, 3)
print(answer)        # None

# RIGHT
def add(a, b):
    return a + b

answer = add(2, 3)
print(answer)        # 5
```

### Mistake 3: Modifying Global Without Declaration

```python
counter = 0

# WRONG
def increment():
    counter += 1     # UnboundLocalError!

# RIGHT
def increment():
    global counter
    counter += 1

# BETTER - avoid global
def increment(current):
    return current + 1
```

### Mistake 4: Wrong Number of Arguments

```python
def greet(first, last):
    print(f"Hello {first} {last}")

# WRONG - missing argument
greet("Alice")       # TypeError!

# WRONG - too many arguments
greet("Alice", "Smith", "Extra")  # TypeError!

# RIGHT
greet("Alice", "Smith")

# Or use keyword arguments
greet(last="Smith", first="Alice")
```

---

## Practice Exercises

### Exercise 1: Temperature Converter
Create functions to convert between Celsius and Fahrenheit.

```python
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    # Your code here
    pass

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    # Your code here
    pass

# Test
print(celsius_to_fahrenheit(0))      # Should be 32.0
print(celsius_to_fahrenheit(100))    # Should be 212.0
print(fahrenheit_to_celsius(32))     # Should be 0.0
print(fahrenheit_to_celsius(212))    # Should be 100.0
```

### Exercise 2: Number Analyzer
Create a function that returns statistics about a list of numbers.

```python
def analyze_numbers(numbers):
    """
    Return dict with count, sum, average, min, max of numbers.
    Return None if list is empty.
    """
    # Your code here
    pass

# Test
result = analyze_numbers([1, 2, 3, 4, 5])
# Should return something like: {'count': 5, 'sum': 15, 'average': 3.0, 'min': 1, 'max': 5}
```

### Exercise 3: Simple Calculator
Create a calculator function that takes two numbers and an operation.

```python
def calculator(a, b, operation):
    """
    Perform operation on a and b.
    operation: 'add', 'subtract', 'multiply', 'divide'
    Return error message for invalid operation or division by zero.
    """
    # Your code here
    pass

# Test
print(calculator(10, 5, 'add'))       # 15
print(calculator(10, 5, 'divide'))    # 2.0
print(calculator(10, 0, 'divide'))    # Error message
print(calculator(10, 5, 'unknown'))   # Error message
```

### Exercise 4: Palindrome Checker
Create a function that checks if a word is a palindrome.

```python
def is_palindrome(word):
    """
    Return True if word is a palindrome (reads same forwards and backwards).
    Ignore case and non-alphanumeric characters.
    """
    # Your code here
    pass

# Test
print(is_palindrome("radar"))         # True
print(is_palindrome("A man a plan a canal Panama"))  # True (ignoring spaces)
print(is_palindrome("hello"))         # False
```

---

## Key Takeaways

1. **Functions encapsulate reusable code** - Define once, call many times
2. **Parameters receive input** - Data comes in through parameters
3. **Return sends output back** - Use `return` to give results to caller
4. **Variables are local by default** - Don't pollute the global namespace
5. **Document your functions** - Use docstrings to explain what they do
6. **One function = one task** - Keep functions focused and simple

## Quick Reference Card

| Task | Syntax | Example |
|------|--------|---------|
| Define function | `def name():` | `def greet():` |
| With parameters | `def name(p1, p2):` | `def greet(name, age):` |
| With defaults | `def name(p1="default"):` | `def greet(name, time="morning"):` |
| Return value | `return value` | `return a + b` |
| Call function | `name()` | `greet()` |
| With arguments | `name(arg1, arg2)` | `greet("Alice", 25)` |
| With keywords | `name(p1=val1)` | `greet(name="Alice")` |
| Access docstring | `function.__doc__` | `print(greet.__doc__)` |

---

## Further Reading

- **Next Lesson**: Function Parameters - Advanced argument handling
- **Practice**: Complete all exercises above
- **Challenge**: Create a mini-library of utility functions for common tasks
- **Explore**: Learn about lambda functions (small anonymous functions)
