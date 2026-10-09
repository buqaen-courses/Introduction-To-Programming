# String Operations: Working with Text in Programs

## Introduction: Text as Data

In the real world, we work with text constantly:
- Searching for a name in a contact list
- Replacing a word in a document
- Checking if a password is long enough
- Combining first and last names

In programming, these actions are called **string operations**. A "string" is just a sequence of characters stored in the computer's memory.

---

## What is a String?

### Definition

A **string** is a sequence of characters treated as a single unit.

```
String: "Hello, World!"
Characters: H-e-l-l-o-,- -W-o-r-l-d-!
Positions:  0-1-2-3-4-5-6-7-8-9-10-11-12
```

### Strings in Memory

```
Text:   H    e    l    l    o    ,    _    W    o    r    l    d    !
ASCII:  72  101  108  108  111   44   32   87  111  114  108  100   33
Bytes:  48   65   6C   6C   6F   2C   20   57   6F   72   6C   64   21
```

**Key concept:** Strings are stored as a sequence of numbers, one per character.

---

## Basic String Operations

### 1. Creating Strings

```python
# Using quotes
name = "Alice"
message = 'Hello, World!'
paragraph = """This is a
multi-line string"""

# From other data
number = 42
string_num = str(number)  # "42"

# Empty string
empty = ""
```

### 2. Getting String Length

**Length** = Number of characters in the string.

```python
text = "Hello"
length = len(text)  # 5

text2 = "Hello, World!"
length2 = len(text2)  # 13 (includes spaces and punctuation)
```

**Important:** Length counts characters, not bytes! Emoji 😀 is 1 character but 4 bytes in UTF-8.

### 3. Accessing Individual Characters

Use **indexing** (position numbers starting from 0):

```python
text = "Python"

first = text[0]   # 'P' (position 0)
second = text[1]  # 'y' (position 1)
last = text[5]    # 'n' (position 5)

# From the end (negative indices)
last = text[-1]   # 'n' (last character)
second_last = text[-2]  # 'o'
```

**Visual:**
```
String:  P   y   t   h   o   n
Index:   0   1   2   3   4   5
Reverse: -6  -5  -4  -3  -2  -1
```

### 4. Slicing (Getting Substrings)

Extract a portion of the string using `[start:end]`:

```python
text = "Hello, World!"

# From position 0 to 4 (not including 5)
hello = text[0:5]    # "Hello"

# From position 7 to end
world = text[7:12]   # "World"

# Shorthand - start from beginning
hello = text[:5]     # "Hello"

# Shorthand - go to end
world = text[7:]     # "World!"

# The whole string
copy = text[:]       # "Hello, World!"

# Skip characters (step)
every_second = text[::2]  # "Hlo ol!"
reverse = text[::-1]      # "!dlroW ,olleH"
```

**Visual:**
```
H   e   l   l   o   ,   _   W   o   r   l   d   !
0   1   2   3   4   5   6   7   8   9   10  11  12

[0:5] → positions 0,1,2,3,4 = "Hello"
[7:12] → positions 7,8,9,10,11 = "World"
```

---

## Common String Operations

### 1. Changing Case

```python
text = "Hello, World!"

upper = text.upper()      # "HELLO, WORLD!"
lower = text.lower()      # "hello, world!"
title = text.title()      # "Hello, World!" (each word capitalized)
capitalized = text.capitalize()  # "Hello, world!" (first letter only)
```

**Use case:** Case-insensitive comparison
```python
# Bad
if user_input == "yes":  # Only matches "yes", not "YES" or "Yes"

# Good
if user_input.lower() == "yes":  # Matches "yes", "YES", "Yes", etc.
```

### 2. Finding and Searching

```python
text = "The quick brown fox jumps over the lazy dog"

# Find first occurrence
position = text.find("fox")       # 16 (position where "fox" starts)
position = text.find("cat")       # -1 (not found)

# Check if contains (returns True/False)
has_fox = "fox" in text           # True
has_cat = "cat" in text           # False

# Count occurrences
count_the = text.count("the")     # 2
```

### 3. Replacing Text

```python
text = "I like cats. Cats are great!"

# Replace all occurrences
new_text = text.replace("cats", "dogs")
# "I like dogs. Cats are great!" (only lowercase changed!)

# Case-insensitive replacement (manual)
new_text = text.lower().replace("cats", "dogs")
# "i like dogs. dogs are great!"

# Replace only first N occurrences
new_text = text.replace("a", "X", 2)
# "I like cXts. CXts are great!"
```

### 4. Removing Whitespace

```python
text = "   Hello, World!   \n\t"

# Remove from both ends
stripped = text.strip()       # "Hello, World!"

# Remove from left only
left_stripped = text.lstrip()  # "Hello, World!   \n\t"

# Remove from right only
right_stripped = text.rstrip() # "   Hello, World!"

# Remove specific characters
cleaned = "...Hello...".strip(".")  # "Hello"
```

**Use case:** Cleaning user input
```python
username = input("Enter username: ").strip()
# Removes accidental spaces
```

---

## String Checking Operations

### Testing String Content

```python
text = "Hello123"

# Check if all alphabetic
is_alpha = text.isalpha()       # False (has numbers)

# Check if all digits
is_digit = text.isdigit()       # False (has letters)

# Check if alphanumeric
is_alnum = text.isalnum()       # True (letters + numbers)

# Check if all uppercase
is_upper = text.isupper()       # False

# Check if all lowercase
is_lower = text.islower()       # False

# Check if whitespace only
is_space = "   ".isspace()      # True

# Check if starts with...
starts_with_hello = text.startswith("Hello")  # True

# Check if ends with...
ends_with_123 = text.endswith("123")        # True
```

### Practical Example: Input Validation

```python
def validate_username(username):
    """Check if username is valid."""
    
    # Remove whitespace
    username = username.strip()
    
    # Check length
    if len(username) < 3:
        return False, "Username must be at least 3 characters"
    
    if len(username) > 20:
        return False, "Username must be at most 20 characters"
    
    # Check characters
    if not username.isalnum():
        return False, "Username must contain only letters and numbers"
    
    # Check doesn't start with number
    if username[0].isdigit():
        return False, "Username cannot start with a number"
    
    return True, "Username is valid"

# Test
print(validate_username("alice"))      # Valid
print(validate_username("123bob"))     # Invalid (starts with number)
print(validate_username("bob@email"))  # Invalid (special character)
print(validate_username("ab"))         # Invalid (too short)
```

---

## String Splitting and Joining

### Splitting: Breaking Strings Apart

```python
# Split by spaces (default)
text = "The quick brown fox"
words = text.split()  # ["The", "quick", "brown", "fox"]

# Split by specific character
csv = "apple,banana,cherry"
fruits = csv.split(",")  # ["apple", "banana", "cherry"]

# Split by newline
lines = "Line 1\nLine 2\nLine 3".split("\n")
# ["Line 1", "Line 2", "Line 3"]

# Split with max splits
text = "a,b,c,d,e"
parts = text.split(",", 2)  # ["a", "b", "c,d,e"]

# Split from the right
parts = text.rsplit(",", 2)  # ["a,b,c", "d", "e"]
```

### Joining: Putting Strings Together

```python
# Join with spaces
words = ["The", "quick", "brown", "fox"]
sentence = " ".join(words)  # "The quick brown fox"

# Join with commas
fruits = ["apple", "banana", "cherry"]
csv = ",".join(fruits)  # "apple,banana,cherry"

# Join with nothing (concatenate)
letters = ["H", "e", "l", "l", "o"]
word = "".join(letters)  # "Hello"

# Join with newlines
lines = ["Line 1", "Line 2", "Line 3"]
text = "\n".join(lines)
# "Line 1\nLine 2\nLine 3"
```

### Split and Join Together

```python
def reverse_words(sentence):
    """Reverse the order of words."""
    words = sentence.split()
    reversed_words = words[::-1]  # Reverse the list
    return " ".join(reversed_words)

# Example
print(reverse_words("Hello World"))  # "World Hello"
print(reverse_words("The quick brown fox"))  # "fox brown quick The"
```

---

## Formatting Strings

### Method 1: Concatenation (Joining with +)

```python
name = "Alice"
age = 25

# Using +
message = "Hello, " + name + "! You are " + str(age) + " years old."
# "Hello, Alice! You are 25 years old."

# Hard to read and error-prone!
```

### Method 2: %-formatting (Old Style)

```python
name = "Alice"
age = 25

message = "Hello, %s! You are %d years old." % (name, age)
# "Hello, Alice! You are 25 years old."

# Format codes:
# %s - string
# %d - integer
# %f - float
# %.2f - float with 2 decimal places
```

### Method 3: str.format() (Newer Style)

```python
name = "Alice"
age = 25

# Positional arguments
message = "Hello, {}! You are {} years old.".format(name, age)

# Named arguments
message = "Hello, {name}! You are {age} years old.".format(name=name, age=age)

# Reordering
message = "{1} is {0} years old.".format(age, name)
# "Alice is 25 years old."

# Formatting numbers
price = 19.99
print("Price: ${:.2f}".format(price))  # "Price: $19.99"
```

### Method 4: F-strings (Modern, Recommended)

```python
name = "Alice"
age = 25

message = f"Hello, {name}! You are {age} years old."
# "Hello, Alice! You are 25 years old."

# Expressions inside
a = 5
b = 3
print(f"{a} + {b} = {a + b}")  # "5 + 3 = 8"

# Formatting
price = 19.99
print(f"Price: ${price:.2f}")  # "Price: $19.99"

# Alignment
text = "Hello"
print(f"[{text:>10}]")  # "[     Hello]" (right align)
print(f"[{text:<10}]")  # "[Hello     ]" (left align)
print(f"[{text:^10}]")  # "[  Hello   ]" (center)
```

---

## Advanced String Operations

### Regular Expressions (Pattern Matching)

```python
import re

# Find email pattern
text = "Contact me at alice@example.com or bob@test.org"
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
# ["alice@example.com", "bob@test.org"]

# Replace all digits
text = re.sub(r'\d+', 'X', "Room 101, Floor 3")
# "Room X, Floor X"

# Check if valid phone number
phone = "555-123-4567"
is_valid = re.match(r'\d{3}-\d{3}-\d{4}$', phone) is not None
# True
```

### String Translation

```python
# Replace multiple characters

# Remove punctuation
text = "Hello, World! How are you?"
no_punct = text.translate(str.maketrans("", "", "!?,.'\""))
# "Hello World How are you"

# Replace characters
text = "Hello World"
leet = text.translate(str.maketrans("ol", "01"))
# "He110 W0r1d"
```

---

## Common String Patterns

### Pattern 1: Building a String Incrementally

```python
def build_report(items):
    """Build a formatted report from a list."""
    lines = []
    lines.append("=" * 40)
    lines.append("REPORT")
    lines.append("=" * 40)
    
    for item in items:
        lines.append(f"- {item}")
    
    lines.append("=" * 40)
    
    return "\n".join(lines)

# Usage
report = build_report(["Item 1", "Item 2", "Item 3"])
print(report)
```

### Pattern 2: Safe String Conversion

```python
def safe_string(value):
    """Convert anything to string safely."""
    if value is None:
        return ""
    return str(value)

# Usage
print(safe_string(42))       # "42"
print(safe_string("hello"))  # "hello"
print(safe_string(None))     # ""
```

### Pattern 3: Normalizing Input

```python
def normalize_text(text):
    """Clean and standardize text."""
    # Remove leading/trailing whitespace
    text = text.strip()
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove extra spaces
    text = " ".join(text.split())
    
    # Remove special characters (keep only alphanumeric and spaces)
    text = "".join(c for c in text if c.isalnum() or c.isspace())
    
    return text

# Usage
print(normalize_text("  Hello,   WORLD!!!  "))
# "hello world"
```

---

## Practice Exercises

### Exercise 1: String Reversal
Write a function to reverse a string without using `[::-1]`.

```python
def reverse_string(text):
    # Your code here
    pass

# Test
print(reverse_string("Hello"))  # Should print "olleH"
```

### Exercise 2: Palindrome Checker
Write a function to check if a string is a palindrome (reads same forwards and backwards).

```python
def is_palindrome(text):
    # Ignore case and spaces
    # Your code here
    pass

# Test
print(is_palindrome("Race car"))  # True
print(is_palindrome("Hello"))     # False
```

### Exercise 3: Word Count
Write a function to count words in a sentence.

```python
def word_count(text):
    # Your code here
    pass

# Test
print(word_count("The quick brown fox"))  # 4
```

### Exercise 4: Password Strength
Write a function to check password strength.

Requirements:
- At least 8 characters
- Contains uppercase
- Contains lowercase
- Contains digits
- Contains special characters

```python
def check_password(password):
    # Return (is_valid, message)
    pass
```

---

## Key Takeaways

1. **Strings are sequences**: Access by index, slice to get portions
2. **Strings are immutable**: Operations return new strings, don't modify originals
3. **Common operations**: upper(), lower(), find(), replace(), split(), join()
4. **Formatting**: Use f-strings for readable, modern code
5. **Validation**: Use string methods to check content (isdigit(), isalpha(), etc.)

## Remember

| Operation | Method | Example |
|-----------|--------|---------|
| Get length | `len(s)` | `len("hello")` → 5 |
| Access char | `s[i]` | `"hello"[1]` → "e" |
| Slice | `s[start:end]` | `"hello"[1:4]` → "ell" |
| To uppercase | `s.upper()` | `"hi".upper()` → "HI" |
| To lowercase | `s.lower()` | `"HI".lower()` → "hi" |
| Find | `s.find(sub)` | `"hello".find("ll")` → 2 |
| Replace | `s.replace(old, new)` | `"a,b".replace(",", "-")` → "a-b" |
| Split | `s.split()` | `"a b".split()` → ["a", "b"] |
| Join | `sep.join(list)` | `" ".join(["a", "b"])` → "a b" |
| Strip | `s.strip()` | `"  hi  ".strip()` → "hi" |
| Check start | `s.startswith(x)` | `"hi".startswith("h")` → True |

---

## Next Steps

- Learn regular expressions for pattern matching
- Understand Unicode and string encoding
- Study string algorithms (searching, matching)
- Explore string manipulation in data processing
