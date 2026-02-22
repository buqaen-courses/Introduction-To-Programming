# Text Processing: Analyzing and Manipulating Text

## What is Text Processing?

**Text processing** is all about working with strings to extract information, transform data, and analyze content. Think of it like being a detective with text - searching for clues, organizing information, and finding patterns.

### Real-World Examples

- Counting words in an essay
- Finding all email addresses in a document
- Cleaning up messy user input
- Analyzing social media posts
- Extracting data from CSV files
- Checking if passwords meet requirements

---

## Searching in Strings

### Finding Substrings

```python
text = "Python is a powerful programming language. Python is fun!"

# Find first occurrence (returns position or -1)
position = text.find("Python")      # 0 (starts at position 0)
not_found = text.find("Java")        # -1 (not in string)

# Find starting from position 10 (finds second "Python")
second = text.find("Python", 10)    # 45

# Find using rfind (searches from the right/end)
last = text.rfind("is")              # 47
```

**Important**: `find()` returns -1 if not found, while `index()` raises an error. Use `find()` when you're not sure if the text exists.

### Checking Membership (the `in` operator)

```python
text = "Learning Python programming"

# Check if substring exists (returns True or False)
"Python" in text      # True
"Java" in text        # False

# Check if NOT in string
"Java" not in text    # True
"Python" not in text  # False

# Case-insensitive check (convert to same case first)
python_mentioned = "python" in text.lower()  # True
```

### Counting Occurrences

```python
text = "The quick brown fox jumps over the lazy dog"

# Count how many times a substring appears
t_count = text.count("t")           # 2 (lowercase t)
total_t = text.lower().count("t")   # 3 (counting all t's)

# Count specific words
the_count = text.count("the")       # 2
```

### Checking Start and End

```python
filename = "document.pdf"
url = "https://example.com"

# Check beginning
filename.startswith("doc")          # True
url.startswith("https://")          # True

# Check ending
filename.endswith(".pdf")           # True
url.endswith(".com")                # True

# Check multiple options
filename.endswith((".pdf", ".doc", ".txt"))  # True (any of these)
```

---

## Splitting and Joining Strings

### Splitting: Breaking Text Apart

```python
# Split on whitespace (default)
sentence = "Hello world how are you"
words = sentence.split()
# Result: ['Hello', 'world', 'how', 'are', 'you']

# Split on specific character
csv_line = "Alice,25,Engineer,New York"
fields = csv_line.split(",")
# Result: ['Alice', '25', 'Engineer', 'New York']

# Split only first N occurrences
sentence = "one:two:three:four:five"
parts = sentence.split(":", 2)
# Result: ['one', 'two', 'three:four:five']

# Split lines
multiline = "Line 1\nLine 2\nLine 3"
lines = multiline.split("\n")
# Result: ['Line 1', 'Line 2', 'Line 3']

# Split lines (better - handles different line endings)
lines = multiline.splitlines()
```

### Joining: Putting Text Together

```python
# Join list into string
words = ['Hello', 'world']
sentence = ' '.join(words)
# Result: "Hello world"

# Join with different separators
path_parts = ['home', 'user', 'documents']
path = '/'.join(path_parts)
# Result: "home/user/documents"

# Join numbers (must convert to strings first!)
numbers = [1, 2, 3, 4, 5]
result = ', '.join(str(n) for n in numbers)
# Result: "1, 2, 3, 4, 5"

# Create CSV line
data = ["Alice", "25", "Engineer"]
csv = ','.join(data)
# Result: "Alice,25,Engineer"
```

---

## Text Transformation and Cleaning

### Changing Case

```python
text = "Hello World"

upper = text.upper()          # "HELLO WORLD"
lower = text.lower()          # "hello world"
title = text.title()          # "Hello World"
capital = text.capitalize()   # "Hello world"
```

### Removing Unwanted Characters

```python
text = "   Hello World   "

# Remove whitespace from ends
clean = text.strip()          # "Hello World"
left = text.lstrip()          # "Hello World   "
right = text.rstrip()         # "   Hello World"

# Remove specific characters
messy = "xxxHelloxxx"
clean = messy.strip('x')      # "Hello"

# Remove all spaces
no_spaces = text.replace(" ", "")
# Result: "HelloWorld"
```

### Replacing Text

```python
text = "I like Java programming"

# Replace all occurrences
new_text = text.replace("Java", "Python")
# Result: "I like Python programming"

# Replace first N occurrences
partial = text.replace("a", "@", 1)
# Result: "I like J@va programming" (only first 'a')

# Remove by replacing with nothing
text = "Hello, World!"
clean = text.replace(",", "").replace("!", "")
# Result: "Hello World"
```

---

## Practical Text Processing Examples

### Example 1: Word Counter

```python
def count_words(text):
    """Count words in text."""
    # Clean the text
    cleaned = text.lower()

    # Remove punctuation (simple way)
    for char in ".,!?;:'\"()-":
        cleaned = cleaned.replace(char, " ")

    # Split into words
    words = cleaned.split()

    return len(words)

# Usage
essay = "Python is amazing. Python is powerful and fun!"
print(f"Word count: {count_words(essay)}")  # Word count: 9
```

### Example 2: Email Validator (Simple)

```python
def is_valid_email(email):
    """Basic email validation."""
    # Check basic structure
    if "@" not in email:
        return False

    # Split into parts
    parts = email.split("@")
    if len(parts) != 2:
        return False

    local, domain = parts

    # Check both parts exist
    if not local or not domain:
        return False

    # Check domain has a dot
    if "." not in domain:
        return False

    return True

# Test
print(is_valid_email("user@example.com"))     # True
print(is_valid_email("invalid-email"))        # False
print(is_valid_email("@example.com"))          # False
```

### Example 3: Text Cleaner

```python
def clean_text(text):
    """Clean and normalize text."""
    if not text:
        return ""

    # Convert to lowercase
    text = text.lower()

    # Remove extra whitespace
    text = ' '.join(text.split())

    # Remove common punctuation
    punctuation = ".,!?;:'\"()-"
    for char in punctuation:
        text = text.replace(char, "")

    return text

# Usage
messy = "  Hello, World!   HOW are you??  "
clean = clean_text(messy)
print(clean)  # "hello world how are you"
```

### Example 4: Password Strength Checker

```python
def check_password_strength(password):
    """Check if password is strong."""
    checks = {
        "length": len(password) >= 8,
        "has_upper": any(c.isupper() for c in password),
        "has_lower": any(c.islower() for c in password),
        "has_digit": any(c.isdigit() for c in password),
    }

    score = sum(checks.values())

    if score == 4:
        return "Strong"
    elif score >= 2:
        return "Medium"
    else:
        return "Weak"

# Test
print(check_password_strength("Hello123"))    # Strong
print(check_password_strength("hello"))       # Weak
print(check_password_strength("HELLO"))       # Weak
```

### Example 5: Simple CSV Parser

```python
def parse_csv_line(line):
    """Parse a CSV line into fields."""
    # Strip whitespace and split
    fields = [field.strip() for field in line.split(",")]
    return fields

def parse_csv_data(data_lines):
    """Parse multiple CSV lines."""
    result = []
    for line in data_lines:
        if line.strip():  # Skip empty lines
            result.append(parse_csv_line(line))
    return result

# Usage
csv_data = [
    "Alice,25,Engineer",
    "Bob,30,Designer",
    "Charlie,35,Manager"
]

parsed = parse_csv_data(csv_data)
for row in parsed:
    print(f"Name: {row[0]}, Age: {row[1]}, Job: {row[2]}")
```

---

## Text Analysis

### Finding the Most Common Words

```python
def word_frequency(text):
    """Count how often each word appears."""
    # Clean and split
    cleaned = text.lower()
    for char in ".,!?;:'\"()-":
        cleaned = cleaned.replace(char, " ")

    words = cleaned.split()

    # Count frequencies
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency

# Usage
text = "the quick brown fox jumps over the lazy dog"
freq = word_frequency(text)

# Find most common
most_common = max(freq.items(), key=lambda x: x[1])
print(f"Most common word: '{most_common[0]}' appears {most_common[1]} times")
```

### Text Statistics

```python
def text_statistics(text):
    """Calculate various text statistics."""
    # Basic counts
    char_count = len(text)
    char_count_no_spaces = len(text.replace(" ", ""))

    # Word count
    words = text.split()
    word_count = len(words)

    # Line count
    lines = text.splitlines()
    line_count = len(lines)

    # Average word length
    if words:
        avg_word_length = sum(len(word) for word in words) / len(words)
    else:
        avg_word_length = 0

    return {
        "characters": char_count,
        "characters_no_spaces": char_count_no_spaces,
        "words": word_count,
        "lines": line_count,
        "average_word_length": round(avg_word_length, 1)
    }

# Usage
text = """Hello world.
This is a test.
Python programming is fun!"""

stats = text_statistics(text)
for key, value in stats.items():
    print(f"{key}: {value}")
```

---

## Common Beginner Mistakes

### Mistake 1: Modifying String While Iterating

```python
# WRONG - this can skip items!
data = ["1", "2", "3", "a", "4", "b"]
for item in data:
    if not item.isdigit():
        data.remove(item)  # Dangerous!

# RIGHT - create a new list
data = ["1", "2", "3", "a", "4", "b"]
cleaned = [item for item in data if item.isdigit()]
# Result: ['1', '2', '3', '4']
```

### Mistake 2: Forgetting to Convert Numbers to Strings

```python
numbers = [1, 2, 3, 4, 5]

# WRONG
result = ", ".join(numbers)   # Error!

# RIGHT
result = ", ".join(str(n) for n in numbers)
# Result: "1, 2, 3, 4, 5"
```

### Mistake 3: Case-Sensitive Comparison

```python
text = "Python Programming"

# WRONG - case sensitive
if "python" in text:   # False!
    print("Found!")

# RIGHT - make case consistent
if "python" in text.lower():   # True!
    print("Found!")
```

### Mistake 4: Not Handling Empty Strings

```python
def get_first_char(text):
    # WRONG - crashes on empty string
    return text[0]

# RIGHT - check first
def get_first_char(text):
    if not text:
        return None
    return text[0]
```

---

## Practice Exercises

### Exercise 1: Sentence Reverser
Write a function that reverses the order of words in a sentence.

```python
def reverse_words(sentence):
    # Your code here
    pass

# Test
print(reverse_words("Hello world"))   # Should print: "world Hello"
print(reverse_words("The quick brown fox"))  # Should print: "fox brown quick The"
```

### Exercise 2: Palindrome Checker
Write a function that checks if a word/phrase is a palindrome (reads the same forwards and backwards).

```python
def is_palindrome(text):
    # Your code here (ignore spaces and case)
    pass

# Test
print(is_palindrome("radar"))     # Should print: True
print(is_palindrome("A man a plan a canal Panama"))  # Should print: True
print(is_palindrome("hello"))     # Should print: False
```

### Exercise 3: Extract Hashtags
Write a function that extracts all hashtags from a social media post.

```python
def extract_hashtags(text):
    # Your code here
    pass

# Test
post = "Learning #Python is fun! #coding #programming #learn"
print(extract_hashtags(post))
# Should print: ['#Python', '#coding', '#programming', '#learn']
```

### Exercise 4: Phone Number Formatter
Write a function that formats a 10-digit number as (XXX) XXX-XXXX.

```python
def format_phone(number):
    # Your code here
    pass

# Test
print(format_phone("5551234567"))   # Should print: (555) 123-4567
print(format_phone("555-123-4567")) # Should print: (555) 123-4567
```

---

## Key Takeaways

1. **Searching**: Use `find()` for safe searching (returns -1 if not found), `in` for simple True/False checks
2. **Splitting/Joining**: `split()` breaks strings apart, `join()` puts them back together
3. **Case matters**: Remember that "Python" and "python" are different - use `.lower()` for case-insensitive work
4. **Clean data first**: Always strip whitespace and normalize case before processing user input
5. **Lists vs strings**: Remember that `join()` works on lists but requires strings, not numbers
6. **Strings are immutable**: Methods return new strings; the original doesn't change

## Quick Reference

| Task | How to Do It | Example |
|------|-------------|---------|
| Find substring | `text.find("sub")` | `"abc".find("b")` → 1 |
| Check if contains | `"sub" in text` | `"b" in "abc"` → True |
| Count occurrences | `text.count("sub")` | `"aa".count("a")` → 2 |
| Starts with? | `text.startswith("pre")` | `"abc".startswith("a")` → True |
| Ends with? | `text.endswith("suf")` | `"abc".endswith("c")` → True |
| Split string | `text.split(sep)` | `"a,b".split(",")` → ['a','b'] |
| Join strings | `sep.join(list)` | `"-".join(['a','b'])` → 'a-b' |
| Strip whitespace | `text.strip()` | `" hi ".strip()` → 'hi' |
| Replace | `text.replace(old, new)` | `"a,b".replace(",", "-")` → 'a-b' |
| Upper case | `text.upper()` | `"hi".upper()` → 'HI' |
| Lower case | `text.lower()` | `"HI".lower()` → 'hi' |

---

## Further Reading

- **Next Lesson**: Python Lists - Ordered collections of data
- **Practice**: Complete all exercises above
- **Challenge**: Write a simple text adventure game that processes user commands
- **Explore**: Try reading and analyzing a real text file
