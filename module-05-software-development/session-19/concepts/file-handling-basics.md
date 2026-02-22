# File Handling Basics: Reading and Writing Text Files

## Introduction: Why Files Matter

Programs need to remember things even after they close. Files let you:
- **Save data** that persists after the program ends
- **Read data** created by other programs
- **Share information** between different runs of your program
- **Process large amounts** of data that won't fit in memory

### The File Metaphor

Think of a file like a notebook:
- You **open** it to read or write
- You **read** what's already there
- You **write** new information
- You **close** it when done

---

## Part 1: Understanding File Paths

### What is a File Path?

A path tells Python where to find a file on your computer.

```
Windows: C:\Users\Alice\Documents\data.txt
Mac/Linux: /Users/Alice/Documents/data.txt
```

### Path Types

```python
# Absolute path - starts from the root
c:\\Users\\Alice\\Documents\\file.txt       # Windows
/home/alice/documents/file.txt            # Linux/Mac

# Relative path - starts from current location
file.txt                                   # In current folder
../data/file.txt                          # Go up one folder, then into data
./file.txt                                # Explicitly current folder
```

### Working with Paths in Python

```python
import os

# Get current working directory
print(os.getcwd())  # Where am I right now?

# Check if file exists
if os.path.exists("data.txt"):
    print("File exists!")
else:
    print("File not found")

# Join paths safely (handles \ vs / automatically)
folder = "data"
filename = "results.txt"
full_path = os.path.join(folder, filename)
print(full_path)  # data/results.txt or data\results.txt

# Get file information
if os.path.exists("data.txt"):
    size = os.path.getsize("data.txt")
    print(f"File size: {size} bytes")
```

---

## Part 2: Reading Files

### Method 1: The `with` Statement (Best Way)

```python
# Read entire file at once
with open("story.txt", "r") as file:
    content = file.read()
    print(content)

# File automatically closes when you exit the 'with' block!
```

**Why use `with`?**
- Automatically closes the file (even if errors occur)
- Cleaner and safer code
- Recommended for all file operations

### Method 2: Read Line by Line

```python
# Process file one line at a time (memory efficient)
with open("story.txt", "r") as file:
    for line_number, line in enumerate(file, 1):
        print(f"Line {line_number}: {line.strip()}")
```

**When to use line-by-line:**
- Large files (doesn't load everything into memory)
- Processing files as streams
- Log file analysis

### Method 3: Read All Lines into a List

```python
# Get all lines as a list
with open("story.txt", "r") as file:
    lines = file.readlines()
    print(f"Total lines: {len(lines)}")
    print(f"First line: {lines[0]}")
```

### Reading Methods Comparison

| Method | Best For | Memory Usage |
|--------|----------|--------------|
| `read()` | Small files, need all content | Loads entire file |
| `readline()` | Read one line at a time | Minimal |
| `readlines()` | Need list of all lines | Loads entire file |
| `for line in file` | Large files, processing | Minimal |

### Handling Newlines

```python
text = "Hello\nWorld\n"
print(f"Original: {repr(text)}")

# strip() removes whitespace including newlines
print(f"Stripped: {repr(text.strip())}")

# rstrip() removes only from the end
print(f"Right stripped: {repr(text.rstrip())}")
```

---

## Part 3: Writing Files

### Writing Text to a File

```python
# 'w' mode = write (creates new file or overwrites existing)
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is line 2\n")
    file.write("This is line 3\n")

print("File written successfully!")
```

**Warning**: `'w'` mode deletes existing content! Use with caution.

### Appending to a File

```python
# 'a' mode = append (adds to end of existing file)
with open("output.txt", "a") as file:
    file.write("This line is appended!\n")

print("Content appended!")
```

### Writing Multiple Lines at Once

```python
lines = [
    "First line\n",
    "Second line\n",
    "Third line\n"
]

with open("output.txt", "w") as file:
    file.writelines(lines)

print("All lines written!")
```

### File Modes Reference

| Mode | Meaning | File Exists | File Doesn't Exist |
|------|---------|-------------|-------------------|
| `'r'` | Read | Opens it | Error |
| `'w'` | Write | Overwrites | Creates new |
| `'a'` | Append | Adds to end | Creates new |
| `'r+'` | Read + Write | Opens it | Error |
| `'x'` | Exclusive creation | Error | Creates new |

---

## Part 4: Practical File Operations

### Example 1: Count Words in a File

```python
def count_words_in_file(filename):
    """Count total words in a text file."""
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return 0

# Usage
count = count_words_in_file("story.txt")
print(f"Word count: {count}")
```

### Example 2: Copy a File

```python
def copy_file(source, destination):
    """Copy contents of one file to another."""
    try:
        with open(source, 'r') as src:
            content = src.read()

        with open(destination, 'w') as dst:
            dst.write(content)

        print(f"Copied {source} to {destination}")
        return True

    except FileNotFoundError:
        print(f"Error: Source file {source} not found")
        return False
    except PermissionError:
        print(f"Error: Permission denied writing to {destination}")
        return False

# Usage
copy_file("original.txt", "backup.txt")
```

### Example 3: Process CSV Data

```python
def process_student_grades(filename):
    """Read student grades from CSV-like file."""
    students = []

    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, 1):
                line = line.strip()
                if not line:  # Skip empty lines
                    continue

                parts = line.split(',')
                if len(parts) < 2:
                    print(f"Warning: Invalid data on line {line_number}")
                    continue

                name = parts[0]
                try:
                    scores = [int(score) for score in parts[1:]]
                    average = sum(scores) / len(scores)

                    students.append({
                        'name': name,
                        'scores': scores,
                        'average': average
                    })
                except ValueError:
                    print(f"Warning: Non-numeric score on line {line_number}")

    except FileNotFoundError:
        print(f"Error: File {filename} not found")

    return students

# Usage
students = process_student_grades("grades.txt")
for student in students:
    print(f"{student['name']}: {student['average']:.1f}")
```

### Example 4: Write a Report

```python
def generate_report(students, output_file):
    """Generate a formatted report file."""
    with open(output_file, 'w') as file:
        file.write("STUDENT GRADE REPORT\n")
        file.write("=" * 50 + "\n\n")

        for student in students:
            name = student['name']
            avg = student['average']
            status = "PASS" if avg >= 60 else "FAIL"

            file.write(f"Student: {name}\n")
            file.write(f"  Average: {avg:.1f}\n")
            file.write(f"  Status: {status}\n\n")

        # Add summary
        if students:
            class_avg = sum(s['average'] for s in students) / len(students)
            file.write("-" * 50 + "\n")
            file.write(f"Class Average: {class_avg:.1f}\n")

    print(f"Report saved to {output_file}")

# Usage
students = process_student_grades("grades.txt")
generate_report(students, "report.txt")
```

---

## Part 5: Error Handling

### Common File Errors

```python
def safe_file_operations(filename):
    """Demonstrate handling common file errors."""

    # Error 1: File doesn't exist
    try:
        with open("nonexistent.txt", 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print("That file doesn't exist!")

    # Error 2: Permission denied
    try:
        with open("/etc/passwd", 'w') as file:  # System file
            file.write("test")
    except PermissionError:
        print("You don't have permission to write there!")

    # Error 3: File is a directory
    try:
        with open(".", 'r') as file:  # Current directory
            content = file.read()
    except IsADirectoryError:
        print("That's a directory, not a file!")

    # Error 4: Disk full (rare but possible)
    try:
        with open("huge_file.txt", 'w') as file:
            file.write("x" * 100000000000)  # Too big!
    except OSError as e:
        print(f"OS Error: {e}")
```

### Safe File Reading Pattern

```python
def read_file_safely(filename):
    """Read file with comprehensive error handling."""
    try:
        with open(filename, 'r') as file:
            return file.read(), None  # (content, error)

    except FileNotFoundError:
        return None, "File not found"
    except PermissionError:
        return None, "Permission denied"
    except UnicodeDecodeError:
        return None, "File is not text (might be binary)"
    except Exception as e:
        return None, f"Unexpected error: {e}"

# Usage
content, error = read_file_safely("data.txt")
if error:
    print(f"Error: {error}")
else:
    print(f"Content: {content[:100]}...")
```

---

## Part 6: Best Practices

### Do's and Don'ts

**✅ DO:**
```python
# Use 'with' statement (auto-closes file)
with open("file.txt", 'r') as file:
    data = file.read()

# Check if file exists before reading
import os
if os.path.exists("file.txt"):
    with open("file.txt", 'r') as file:
        data = file.read()

# Use specific exception handling
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
```

**❌ DON'T:**
```python
# Don't forget to close files
file = open("file.txt", 'r')
data = file.read()
# Missing: file.close()

# Don't use bare except clauses
except:  # Too broad!
    print("Error")

# Don't ignore errors silently
try:
    os.remove("file.txt")
except:
    pass  # Error ignored!
```

### Working with Different File Types

```python
# JSON files (structured data)
import json

# Read JSON
with open("data.json", 'r') as file:
    data = json.load(file)

# Write JSON
with open("output.json", 'w') as file:
    json.dump(data, file, indent=2)

# CSV files (tabular data)
import csv

# Read CSV
with open("data.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

---

## Practice Exercises

### Exercise 1: File Analyzer

Create a function that analyzes a text file and returns statistics:
- Total lines
- Total words
- Total characters
- Average words per line

```python
def analyze_file(filename):
    """Analyze a text file and return statistics."""
    # Your code here
    pass

# Test
stats = analyze_file("story.txt")
print(f"Lines: {stats['lines']}")
print(f"Words: {stats['words']}")
print(f"Characters: {stats['chars']}")
```

### Exercise 2: File Search

Create a function that searches for a word in a file and returns all lines containing it:

```python
def search_in_file(filename, search_word):
    """Find all lines containing search_word."""
    # Your code here
    pass

# Test
results = search_in_file("story.txt", "python")
for line_num, line in results:
    print(f"Line {line_num}: {line}")
```

### Exercise 3: Data Converter

Convert a simple data format to another:

```python
def convert_data(input_file, output_file):
    """
    Read input.txt with format:
        Alice,25
        Bob,30
    Write output.txt with format:
        Name: Alice, Age: 25
        Name: Bob, Age: 30
    """
    # Your code here
    pass
```

---

## Key Takeaways

1. **Always use `with`** - It automatically closes files
2. **Handle errors** - Files might not exist or be accessible
3. **Choose the right mode** - 'r' for read, 'w' for write (careful!), 'a' for append
4. **Use relative paths** - Makes code more portable
5. **Process large files line-by-line** - Saves memory
6. **Check file existence** - Before trying to open

## Quick Reference

```python
# Reading
with open("file.txt", 'r') as f:
    content = f.read()        # All content
    lines = f.readlines()     # List of lines
    for line in f:            # Line by line
        process(line)

# Writing
with open("file.txt", 'w') as f:  # Overwrites!
    f.write("text\n")
    f.writelines(["line1\n", "line2\n"])

with open("file.txt", 'a') as f:  # Appends
    f.write("more text\n")

# Checking
import os
os.path.exists("file.txt")   # File exists?
os.path.getsize("file.txt")  # File size
os.path.join("folder", "file.txt")  # Safe path joining
```

---

## Further Reading

- **Next**: Session 20 - Modules and organizing code
- **Practice**: Create a program that processes a directory of text files
- **Challenge**: Build a simple text search engine
- **Explore**: Learn about binary file handling
