# Python Modules: Organizing Code into Files

## Introduction: Why Modules?

As programs grow larger, putting all code in one file becomes messy. **Modules** let you:
- **Organize** code into logical groups
- **Reuse** functions across multiple projects
- **Collaborate** with others on different files
- **Maintain** code more easily (find and fix bugs faster)

### The Module Metaphor

Think of modules like chapters in a book:
- Chapter 1: Introduction
- Chapter 2: Characters
- Chapter 3: Plot

Each chapter focuses on one topic. You can read chapters in order or jump to specific ones.

### What is a Module?

A **module** is simply a Python file (`.py`) that contains code:
- Functions
- Variables
- Classes (we'll learn these later)

---

## Part 1: Creating Your First Module

### Step 1: Create a Module File

Create a file named `math_utils.py`:

```python
# math_utils.py
"""A collection of useful math functions."""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b (with error handling)."""
    if b == 0:
        return "Cannot divide by zero"
    return a / b

PI = 3.14159  # Module-level constant
```

### Step 2: Use the Module

Create another file in the same folder, `main.py`:

```python
# main.py
import math_utils  # Import the module

# Use functions from the module
result = math_utils.add(5, 3)
print(result)  # 8

result = math_utils.multiply(4, 7)
print(result)  # 28

# Use constants
print(math_utils.PI)  # 3.14159
```

**Key Point**: The module name is the filename without `.py`

---

## Part 2: Different Ways to Import

### Method 1: Import the Whole Module

```python
import math_utils

result = math_utils.add(5, 3)
```

**Pros**: Clear where functions come from
**Cons**: Longer to type

### Method 2: Import Specific Items

```python
from math_utils import add, subtract, PI

result = add(5, 3)        # No need for math_utils.
result = subtract(10, 4)  # Direct access
print(PI)                 # 3.14159
```

**Pros**: Shorter code
**Cons**: Less clear where things come from

### Method 3: Import with Alias

```python
import math_utils as mu  # mu is the alias

result = mu.add(5, 3)
result = mu.multiply(4, 2)
```

**Useful when**: Module names are long

```python
import my_really_long_module_name as short
```

### Method 4: Import Everything (Not Recommended!)

```python
from math_utils import *  # Import all functions

result = add(5, 3)
result = multiply(4, 2)
```

**⚠️ Warning**: Can cause name conflicts! Avoid this pattern.

---

## Part 3: Module Search Path

### Where Does Python Look for Modules?

```python
import sys

# See where Python looks
print("Python looks in these folders:")
for path in sys.path:
    print(f"  {path}")
```

**Search Order:**
1. Current directory
2. Python's standard library
3. Third-party packages (site-packages)

### Adding Custom Paths

```python
import sys

# Add your own folder
sys.path.append("/path/to/my/modules")

# Now you can import from there
import my_custom_module
```

---

## Part 4: The `__name__ == "__main__"` Pattern

### The Problem

When you import a module, Python runs all the code in it. What if you have test code?

```python
# math_utils.py
def add(a, b):
    return a + b

# This runs when file is imported!
print("Testing add function:")
print(add(2, 3))  # This executes during import!
```

### The Solution

```python
# math_utils.py
def add(a, b):
    return a + b

# This only runs when file is executed directly
if __name__ == "__main__":
    print("Testing add function:")
    print(add(2, 3))
    print("All tests passed!")
```

**How it works:**
- When file is run directly: `__name__` = `"__main__"`
- When file is imported: `__name__` = module name (e.g., `"math_utils"`)

### Practical Example

```python
# calculator.py
"""A simple calculator module."""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# Test code (only runs when file is executed directly)
if __name__ == "__main__":
    print("Running calculator tests...")
    assert add(2, 3) == 5
    assert subtract(10, 4) == 6
    assert multiply(3, 3) == 9
    assert divide(10, 2) == 5
    print("All tests passed!")
```

Now you can:
```python
# Import and use
from calculator import add, subtract
result = add(5, 3)

# Or run directly to test
# python calculator.py
```

---

## Part 5: Organizing Multi-File Projects

### Project Structure Example

```
my_project/
├── main.py              # Entry point
├── config.py            # Settings and constants
├── utils/
│   ├── __init__.py      # Makes it a package
│   ├── file_utils.py    # File operations
│   └── math_utils.py    # Math functions
├── data/
│   ├── __init__.py
│   └── student_data.py  # Data handling
└── tests/
    └── test_calculator.py
```

### Example: Gradebook Project

**config.py** - Settings
```python
"""Configuration settings for the gradebook."""

DATA_FILE = "grades.txt"
REPORT_FILE = "report.txt"
PASSING_GRADE = 60
MAX_STUDENTS = 100
```

**utils/file_utils.py** - File operations
```python
"""File handling utilities."""

def read_lines(filename):
    """Read all lines from file."""
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def write_lines(filename, lines):
    """Write lines to file."""
    with open(filename, 'w') as file:
        file.writelines(lines)
```

**utils/grade_utils.py** - Grade calculations
```python
"""Grade calculation utilities."""

def calculate_average(scores):
    """Calculate average of scores."""
    if not scores:
        return 0
    return sum(scores) / len(scores)

def get_letter_grade(average):
    """Convert average to letter grade."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'
```

**main.py** - Main program
```python
"""Student Gradebook Application."""

import config
from utils.file_utils import read_lines, write_lines
from utils.grade_utils import calculate_average, get_letter_grade

def process_grades():
    """Main function to process student grades."""
    lines = read_lines(config.DATA_FILE)

    students = []
    for line in lines:
        parts = line.strip().split(',')
        if len(parts) >= 2:
            name = parts[0]
            scores = [int(s) for s in parts[1:] if s.isdigit()]
            avg = calculate_average(scores)
            grade = get_letter_grade(avg)

            students.append({
                'name': name,
                'average': avg,
                'grade': grade
            })

    return students

def generate_report(students):
    """Generate and save report."""
    lines = ["STUDENT GRADE REPORT\n", "="*50 + "\n\n"]

    for student in students:
        lines.append(f"{student['name']}: {student['average']:.1f} ({student['grade']})\n")

    write_lines(config.REPORT_FILE, lines)
    print(f"Report saved to {config.REPORT_FILE}")

if __name__ == "__main__":
    students = process_grades()
    for student in students:
        print(f"{student['name']}: {student['average']:.1f} ({student['grade']})")

    generate_report(students)
```

---

## Part 6: Built-in Modules

### Common Built-in Modules

```python
# os - Operating system functions
import os

print(os.getcwd())              # Current directory
print(os.listdir('.'))          # List files
os.mkdir('new_folder')          # Create folder
os.path.exists('file.txt')      # Check if exists

# sys - System functions
import sys

print(sys.argv)                 # Command line arguments
print(sys.path)                 # Module search path
sys.exit()                      # Exit program

# datetime - Date and time
from datetime import datetime

now = datetime.now()
print(now.strftime("%Y-%m-%d"))  # 2024-01-15

# random - Random numbers
import random

print(random.randint(1, 10))    # Random 1-10
print(random.choice(['a', 'b', 'c']))  # Random choice

# json - JSON data
import json

data = {'name': 'Alice', 'age': 25}
json_string = json.dumps(data, indent=2)
parsed = json.loads(json_string)

# math - Math functions
import math

print(math.sqrt(16))            # 4.0
print(math.pi)                  # 3.14159...
print(math.floor(4.7))          # 4
```

---

## Part 7: Best Practices

### DO:

```python
# 1. Use clear module names
# good: student_grades.py
# bad: sg.py

# 2. Add docstrings
"""This module handles student grade calculations."""

# 3. Use __name__ == "__main__" for test code
if __name__ == "__main__":
    # Test code here
    pass

# 4. Group related functions
# math_utils.py - only math functions
# file_utils.py - only file operations

# 5. Import at the top
import os
import sys
from datetime import datetime
```

### DON'T:

```python
# 1. Don't use 'import *'
from module import *  # Avoid this!

# 2. Don't put all code in one file
# Split into logical modules

# 3. Don't create circular imports
# file_a.py imports file_b.py
# file_b.py imports file_a.py  # BAD!

# 4. Don't execute code at module level
# (unless it's constants or simple setup)
print("This runs on import!")  # Avoid this
```

---

## Practice Exercises

### Exercise 1: Create a String Utilities Module

Create `string_utils.py` with these functions:
- `count_words(text)` - Count words in text
- `reverse_string(text)` - Reverse a string
- `is_palindrome(text)` - Check if palindrome
- `capitalize_words(text)` - Capitalize each word

Then create `main.py` that uses these functions.

### Exercise 2: Build a Multi-File Calculator

Create a calculator project with this structure:
```
calculator/
├── main.py
├── operations.py    # +, -, *, /
├── validation.py    # Input checking
└── display.py       # Output formatting
```

### Exercise 3: Refactor a Messy Program

Take this single-file program and split it into modules:

```python
# messy_program.py (current)
def read_data():
    pass

def validate_data():
    pass

def process_data():
    pass

def save_results():
    pass

def format_report():
    pass

def main():
    data = read_data()
    validate_data(data)
    process_data(data)
    save_results(data)
    format_report(data)

main()
```

Convert to:
- `data_io.py` - Read/save functions
- `validation.py` - Validation functions
- `processing.py` - Processing functions
- `reporting.py` - Report formatting
- `main.py` - Main program

---

## Key Takeaways

1. **Modules are just `.py` files** - Create them by writing Python code
2. **`import module_name`** brings in all the code
3. **`from module import function`** brings specific items
4. **`if __name__ == "__main__"`** separates import code from run code
5. **Organize by purpose** - Group related functions together
6. **Use clear names** - Module names should describe contents

## Quick Reference

```python
# Import styles
import math_utils                    # math_utils.add(5, 3)
from math_utils import add           # add(5, 3)
import math_utils as mu              # mu.add(5, 3)

# __name__ pattern
if __name__ == "__main__":
    # Code that runs when file is executed
    pass

# Creating a module
# 1. Write functions in a .py file
# 2. Import it in another file
# 3. Use the functions!
```

---

## Further Reading

- **Next**: Session 21 - Mini-project (combining all concepts)
- **Practice**: Split one of your old projects into modules
- **Challenge**: Create a reusable module library
- **Explore**: Learn about Python packages (folders with `__init__.py`)
