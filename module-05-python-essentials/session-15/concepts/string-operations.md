# String Operations: Working with Text

## What You'll Learn
- How to create and use strings in Python
- How to access individual characters in a string
- How to combine and manipulate strings
- Essential string methods for everyday tasks

## What is a String? (The Box of Letters Analogy)

Think of a **string** like a string of beads - each character (letter, number, or symbol) is a bead, and they're all connected in a specific order.

In Python, we use strings to work with text:

```python
# Strings are text enclosed in quotes
name = "Alice"           # Double quotes
city = 'New York'        # Single quotes work too!
sentence = "Python is fun!"
```

### Why Strings Matter

Strings are everywhere in programming:
- Displaying messages to users
- Reading user input
- Working with names, emails, and addresses
- Creating formatted output

---

## Creating Strings

### Three Ways to Create Strings

```python
# Method 1: Single quotes (great for simple text)
message = 'Hello, World!'

# Method 2: Double quotes (use when text has apostrophes)
quote = "Don't worry, be happy!"

# Method 3: Triple quotes (for multi-line text)
poem = """Roses are red
Violets are blue
Python is awesome
And so are you!"""
```

### Converting Numbers to Strings

```python
# Numbers can become strings
age = 25
age_text = str(age)           # "25"

price = 19.99
price_text = str(price)       # "19.99"
```

---

## Accessing Characters

### Understanding Index Positions

Every character in a string has a position number starting from 0:

```
String:  P  y  t  h  o  n
Index:   0  1  2  3  4  5
```

```python
word = "Python"

# Access by index (position)
first_letter = word[0]    # 'P'
second_letter = word[1]   # 'y'
last_letter = word[5]     # 'n'
```

### Negative Indexing (Counting from the End)

```python
word = "Python"

# Negative indices count from the end
last = word[-1]           # 'n' (last character)
second_last = word[-2]    # 'o' (second to last)
```

### Getting the Length

```python
text = "Hello, World!"
length = len(text)        # 13 (counts every character)
```

---

## String Slicing: Getting Parts of Strings

Slicing means extracting a portion of a string:

```python
text = "Python Programming"

# Syntax: string[start:end] (end is NOT included)
substring = text[0:6]     # "Python" (positions 0 to 5)

# From start to position 6
beginning = text[:6]       # "Python"

# From position 7 to end
ending = text[7:]          # "Programming"
```

### Practical Slicing Examples

```python
# Get file extension
filename = "document.pdf"
extension = filename[-3:]   # "pdf" (last 3 characters)

# Remove extension
name_only = filename[:-4]   # "document" (everything except last 4)

# Get first name from full name
full_name = "Alice Johnson"
first_name = full_name[:5]  # "Alice"
```

---

## Basic String Operations

### 1. Concatenation: Joining Strings

```python
# Using + to join strings
first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name
# Result: "Alice Smith"

# Joining with other text
greeting = "Hello, " + first_name + "!"
# Result: "Hello, Alice!"
```

### 2. Repetition: Repeating Strings

```python
# Using * to repeat strings
line = "=" * 20
# Result: "===================="

# Create a pattern
stars = "* " * 5
# Result: "* * * * * "
```

### 3. Checking if Text is Inside

```python
text = "Python is amazing"

# Check if substring exists
"Python" in text      # True
"java" in text        # False

# Check if NOT in string
"C++" not in text     # True
```

---

## Essential String Methods

Methods are actions you can perform on strings. Think of them as built-in tools.

### Changing Case

```python
text = "Hello World"

# Convert to uppercase
shouting = text.upper()         # "HELLO WORLD"

# Convert to lowercase
quiet = text.lower()            # "hello world"

# Capitalize first letter of each word
title = text.title()            # "Hello World"
```

### Finding and Counting

```python
text = "Python is powerful. Python is easy."

# Find first occurrence (returns position or -1)
position = text.find("Python")      # 0
not_found = text.find("Java")       # -1 (not found)

# Count occurrences
count = text.count("Python")          # 2
```

### Replacing Text

```python
text = "I love Java programming"

# Replace all occurrences
new_text = text.replace("Java", "Python")
# Result: "I love Python programming"

# Remove characters by replacing with nothing
clean = "Hello, World!".replace(",", "").replace("!", "")
# Result: "Hello World"
```

### Splitting and Joining

```python
# Split string into list
sentence = "Python is fun"
words = sentence.split()          # ["Python", "is", "fun"]

# Split on specific character
csv_data = "Alice,25,Engineer"
parts = csv_data.split(",")       # ["Alice", "25", "Engineer"]

# Join list into string
words = ["Hello", "World"]
sentence = " ".join(words)         # "Hello World"
```

### Removing Whitespace

```python
text = "   Hello World   "

# Remove from both ends
clean = text.strip()        # "Hello World"

# Remove from left only
left_clean = text.lstrip()  # "Hello World   "
```

---

## Common Beginner Mistakes

### Mistake 1: Mixing Numbers and Strings

```python
# ❌ Wrong - mixing numbers and strings causes error
message = "I am " + 25 + " years old"  # Error!

# ✅ Correct - convert number to string first
message = "I am " + str(25) + " years old"  # "I am 25 years old"

# ✅ Even better - use f-strings
message = f"I am {25} years old"
```

### Mistake 2: Index Out of Range

```python
# ❌ Wrong - index doesn't exist
word = "Hi"
letter = word[5]   # Error! IndexError

# ✅ Correct - check length first
if len(word) > 5:
    letter = word[5]
else:
    print("Word is too short!")

# ✅ Or use a safer approach
word = "Hi"
letter = word[-1]  # Always gets last character safely
```

### Mistake 3: Forgetting Strings Are Immutable

```python
# ❌ Wrong - strings can't be changed in place
text = "Hello"
text[0] = "J"   # Error! TypeError

# ✅ Correct - create a new string
text = "J" + text[1:]   # "Jello"
```

### Mistake 4: Confusing find() and index()

```python
text = "Hello"

# ✅ find() returns -1 if not found (safe)
result = text.find("z")   # -1

# ❌ index() raises an exception if not found
result = text.index("z")   # Error! ValueError
```

---

## Try It Yourself: Exercises

### Exercise 1: Name Formatter
Write a function that takes a full name and returns it in "Last, First" format.

```python
def format_name(full_name):
    # Find the space position
    space_pos = full_name.find(" ")
    # Split into first and last name
    first = full_name[:space_pos]
    last = full_name[space_pos + 1:]
    # Return in "Last, First" format
    return last + ", " + first

# Test
print(format_name("Alice Johnson"))  # Should print: "Johnson, Alice"
```

### Exercise 2: Email Extractor
Extract the username from an email address (everything before @).

```python
def get_username(email):
    # Find the @ symbol
    at_pos = email.find("@")
    # Return everything before it
    return email[:at_pos]

# Test
print(get_username("alice@example.com"))  # Should print: "alice"
```

### Exercise 3: Message Repeater
Create a function that repeats a message with a border.

```python
def repeat_message(message, count):
    border = "-" * 20
    repeated = (message + "\n") * count
    return border + "\n" + repeated + border

# Test
print(repeat_message("Hello!", 3))
```

---

## Quick Reference

| Task | Method/Operation | Example |
|------|-----------------|---------|
| Get length | `len(s)` | `len("Hi")` → 4 |
| Access character | `s[i]` | `"Hi"[0]` → 'H' |
| Slice | `s[start:end]` | `"Hello"[1:4]` → 'ell' |
| Join strings | `+` | `"Hi" + "!"` → 'Hi!' |
| Repeat | `*` | `"Ha" * 3` → 'HaHaHa' |
| Find substring | `s.find()` | `"abc".find("b")` → 1 |
| Replace | `s.replace()` | `"a,b".replace(",", "-")` → 'a-b' |
| Split | `s.split()` | `"a b".split()` → ['a', 'b'] |
| Join list | `sep.join()` | `"-".join(['a','b'])` → 'a-b' |
| Uppercase | `s.upper()` | `"hi".upper()` → 'HI' |
| Lowercase | `s.lower()` | `"HI".lower()` → 'hi' |
| Strip whitespace | `s.strip()` | `" hi ".strip()` → 'hi' |

---

## Key Takeaways

1. **Strings are sequences of characters** - you can access individual characters using indices
2. **Index starts at 0** - the first character is at position 0
3. **Slicing creates new strings** - use `[start:end]` to extract substrings
4. **Strings are immutable** - methods return new strings, they don't modify the original
5. **Use the right tool** - Python has many built-in string methods

## What's Next?

In the next lesson, you'll learn about **String Formatting** - how to create professional-looking output with variables, numbers, and formatted text. You'll learn about f-strings, the modern way to format strings in Python.
