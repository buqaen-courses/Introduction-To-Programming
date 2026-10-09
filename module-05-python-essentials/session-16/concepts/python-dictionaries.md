# Python Dictionaries: Key-Value Pairs

## What is a Dictionary?

A **dictionary** is like a real dictionary or a phone book - it stores information as pairs of keys and values. You look up information using a **key** (like a word) and get back a **value** (like the definition).

```python
# Simple dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Access by key, not by position!
print(person["name"])   # "Alice"
print(person["age"])    # 25
```

### Why Dictionaries Matter

Dictionaries are incredibly useful:
- **Fast lookups** - Find information instantly by key
- **Meaningful data** - Keys tell you what the data means
- **Flexible** - Store any type of data
- **Real-world modeling** - Perfect for representing objects

### Dictionary vs List

| Feature | List | Dictionary |
|---------|------|------------|
| Access by | Position (0, 1, 2...) | Key ("name", "age") |
| Order | Maintained | Maintained (Python 3.7+) |
| Lookups | Slow (search through list) | Fast (direct access) |
| Use case | Ordered sequences | Labelled data |

---

## Creating Dictionaries

### Basic Creation

```python
# Empty dictionary
empty = {}
empty = dict()   # Alternative

# With initial values
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Using dict() with keyword arguments
person = dict(name="Alice", age=25, city="New York")

# From list of pairs
pairs = [("name", "Alice"), ("age", 25)]
person = dict(pairs)

# From two lists using zip()
keys = ["name", "age", "city"]
values = ["Alice", 25, "NYC"]
person = dict(zip(keys, values))
```

### Nested Dictionaries

```python
# Dictionaries can contain other dictionaries!
student = {
    "name": "Alice",
    "age": 20,
    "grades": {
        "math": 95,
        "science": 88,
        "history": 92
    },
    "contact": {
        "email": "alice@example.com",
        "phone": "555-1234"
    }
}

# Access nested data
math_grade = student["grades"]["math"]      # 95
email = student["contact"]["email"]         # "alice@example.com"
```

---

## Accessing Dictionary Values

### Direct Access (Careful!)

```python
person = {"name": "Alice", "age": 25}

# Direct access with []
name = person["name"]    # "Alice"

# Trying to access missing key raises error!
# salary = person["salary"]  # KeyError!
```

### Safe Access with get()

```python
person = {"name": "Alice", "age": 25}

# get() returns None if key not found
salary = person.get("salary")       # None (no error!)

# Provide default value
salary = person.get("salary", 0)    # 0 (default)
city = person.get("city", "Unknown") # "Unknown"

# Still works for existing keys
name = person.get("name")            # "Alice"
```

### Checking if Key Exists

```python
person = {"name": "Alice", "age": 25}

# Using in operator
has_name = "name" in person      # True
has_salary = "salary" in person  # False

# Safe access pattern
if "age" in person:
    age = person["age"]
    print(f"Age: {age}")
else:
    print("Age not specified")
```

### Using setdefault()

```python
person = {"name": "Alice"}

# If key exists, return value
age = person.setdefault("age", 18)   # Sets age=18, returns 18
print(person)  # {"name": "Alice", "age": 18}

# If key exists, return existing value (doesn't change)
age = person.setdefault("age", 99)   # Still 18, returns 18
```

---

## Modifying Dictionaries

### Adding and Updating

```python
person = {"name": "Alice", "age": 25}

# Add new key-value pair
person["city"] = "New York"
# Now: {"name": "Alice", "age": 25, "city": "New York"}

# Update existing value
person["age"] = 26
# Now: {"name": "Alice", "age": 26, "city": "New York"}

# Update multiple values at once
person.update({"age": 27, "job": "Engineer", "city": "Boston"})
# Now includes job, age updated, city changed
```

### Removing Items

```python
person = {
    "name": "Alice",
    "age": 27,
    "city": "Boston",
    "job": "Engineer"
}

# pop() - removes and returns value
removed_city = person.pop("city")    # Returns "Boston"
# Now: {"name": "Alice", "age": 27, "job": "Engineer"}

# pop() with default (safe)
removed_hobby = person.pop("hobby", "No hobby")  # Returns "No hobby"

# popitem() - removes and returns last item (Python 3.7+)
last_item = person.popitem()    # Returns ("job", "Engineer")

# del - removes but doesn't return
del person["age"]
# Now: {"name": "Alice"}

# clear() - removes everything
person.clear()
# Now: {}
```

---

## Working with Dictionary Views

### Getting Keys, Values, and Items

```python
person = {"name": "Alice", "age": 25, "city": "NYC"}

# Get all keys
keys = person.keys()
print(keys)        # dict_keys(['name', 'age', 'city'])
print(list(keys))  # ['name', 'age', 'city']

# Get all values
values = person.values()
print(values)      # dict_values(['Alice', 25, 'NYC'])

# Get all key-value pairs
items = person.items()
print(items)       # dict_items([('name', 'Alice'), ('age', 25), ('city', 'NYC')])

# Convert to list of tuples
pairs = list(person.items())
# [('name', 'Alice'), ('age', 25), ('city', 'NYC')]
```

### Iterating Over Dictionaries

```python
person = {"name": "Alice", "age": 25, "city": "NYC"}

# Iterate over keys (default)
for key in person:
    print(f"{key}: {person[key]}")

# Iterate over keys explicitly
for key in person.keys():
    print(key)

# Iterate over values
for value in person.values():
    print(value)

# Iterate over key-value pairs (most common!)
for key, value in person.items():
    print(f"{key} = {value}")

# Output:
# name = Alice
# age = 25
# city = NYC
```

---

## Dictionary Methods and Operations

### Copying Dictionaries

```python
original = {"a": 1, "b": [2, 3]}

# Shallow copy
shallow = original.copy()
shallow = dict(original)   # Alternative

# Modify copy - nested objects are shared!
shallow["b"].append(4)
print(original)   # {"a": 1, "b": [2, 3, 4]} - nested list changed!

# Deep copy (completely independent)
import copy
deep = copy.deepcopy(original)
deep["b"].append(5)
print(original)   # {"a": 1, "b": [2, 3, 4]} - unchanged!
```

### Dictionary Size

```python
person = {"name": "Alice", "age": 25, "city": "NYC"}

# Count items
size = len(person)   # 3

# Check if empty
if not person:       # True if empty
    print("Dictionary is empty")

if len(person) == 0:  # Same thing
    print("Dictionary is empty")
```

### Merging Dictionaries (Python 3.9+)

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}  # Note: b exists in both

# Merge with | operator (dict2 values win conflicts)
merged = dict1 | dict2
# Result: {"a": 1, "b": 3, "c": 4}

# Update in place with |=
dict1 |= dict2
# dict1 is now: {"a": 1, "b": 3, "c": 4}
```

---

## Dictionary Comprehensions

Just like list comprehensions, but for dictionaries!

### Basic Syntax

```python
# Regular way
squares = {}
for x in range(1, 6):
    squares[x] = x ** 2

# Dictionary comprehension
squares = {x: x ** 2 for x in range(1, 6)}
# Result: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### With Conditions

```python
# Only even numbers
even_squares = {x: x ** 2 for x in range(1, 11) if x % 2 == 0}
# Result: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# Transform existing dictionary
original = {"a": 1, "b": 2, "c": 3}
doubled = {k: v * 2 for k, v in original.items()}
# Result: {"a": 2, "b": 4, "c": 6}

# Swap keys and values
swapped = {v: k for k, v in original.items()}
# Result: {1: "a", 2: "b", 3: "c"}
```

---

## Practical Examples

### Example 1: Word Frequency Counter

```python
def count_words(text):
    """Count how many times each word appears."""
    words = text.lower().split()
    frequency = {}

    for word in words:
        # Remove punctuation (simple way)
        word = word.strip(".,!?;:'\"")

        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency

# Usage
text = "the quick brown fox jumps over the lazy dog"
freq = count_words(text)

# Find most common word
most_common = max(freq.items(), key=lambda x: x[1])
print(f"Most common: '{most_common[0]}' ({most_common[1]} times)")

# Print all frequencies sorted
for word, count in sorted(freq.items(), key=lambda x: -x[1]):
    print(f"{word}: {count}")
```

### Example 2: Simple Phone Book

```python
def phone_book_app():
    contacts = {}

    while True:
        print("\nPhone Book:")
        for name, number in contacts.items():
            print(f"  {name}: {number}")

        print("\nOptions: (a)dd, (l)ookup, (d)elete, (q)uit")
        choice = input("Choice: ").lower()

        if choice == 'a':
            name = input("Name: ")
            number = input("Number: ")
            contacts[name] = number
            print(f"Added {name}")

        elif choice == 'l':
            name = input("Name to look up: ")
            number = contacts.get(name)
            if number:
                print(f"{name}: {number}")
            else:
                print(f"{name} not found")

        elif choice == 'd':
            name = input("Name to delete: ")
            if name in contacts:
                del contacts[name]
                print(f"Deleted {name}")
            else:
                print(f"{name} not found")

        elif choice == 'q':
            print("Goodbye!")
            break

# Uncomment to run:
# phone_book_app()
```

### Example 3: Student Grade Manager

```python
def create_student(name, grades):
    """Create a student dictionary with grades."""
    return {
        "name": name,
        "grades": grades,
        "average": sum(grades) / len(grades) if grades else 0
    }

def add_grade(student, subject, grade):
    """Add a grade for a subject."""
    if "grades_by_subject" not in student:
        student["grades_by_subject"] = {}

    student["grades_by_subject"][subject] = grade

    # Update all grades list and average
    student["grades"] = list(student["grades_by_subject"].values())
    student["average"] = sum(student["grades"]) / len(student["grades"])

def get_report(student):
    """Generate a formatted report."""
    report = f"\nReport for {student['name']}\n"
    report += "=" * 30 + "\n"

    if "grades_by_subject" in student:
        for subject, grade in student["grades_by_subject"].items():
            report += f"{subject:12}: {grade:3}\n"

    report += "-" * 30 + "\n"
    report += f"{'Average':12}: {student['average']:.1f}\n"

    return report

# Usage
alice = create_student("Alice Johnson", [])
add_grade(alice, "Math", 95)
add_grade(alice, "Science", 88)
add_grade(alice, "History", 92)

print(get_report(alice))
```

### Example 4: Configuration Manager

```python
def create_default_config():
    """Create default application configuration."""
    return {
        "app": {
            "name": "MyApp",
            "version": "1.0.0",
            "debug": False
        },
        "database": {
            "host": "localhost",
            "port": 5432,
            "name": "myapp_db"
        },
        "features": {
            "notifications": True,
            "dark_mode": False,
            "auto_save": True
        }
    }

def get_config_value(config, path, default=None):
    """Safely get nested config value using dot notation."""
    keys = path.split(".")
    current = config

    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default

    return current

def set_config_value(config, path, value):
    """Set nested config value using dot notation."""
    keys = path.split(".")
    current = config

    for key in keys[:-1]:
        if key not in current:
            current[key] = {}
        current = current[key]

    current[keys[-1]] = value

# Usage
config = create_default_config()

# Get values
app_name = get_config_value(config, "app.name")        # "MyApp"
db_port = get_config_value(config, "database.port")    # 5432
missing = get_config_value(config, "cache.enabled", False)  # False (default)

# Set values
set_config_value(config, "app.debug", True)
set_config_value(config, "cache.enabled", True)
```

---

## Common Beginner Mistakes

### Mistake 1: Using Lists as Dictionary Keys

```python
# WRONG - lists cannot be keys (they're mutable)
my_dict = {["a", "b"]: "value"}  # TypeError!

# RIGHT - use tuples (immutable)
my_dict = {("a", "b"): "value"}  # Works!

# Lists can be values though
my_dict = {"items": ["a", "b", "c"]}  # This is fine!
```

### Mistake 2: Modifying Dictionary While Iterating

```python
# WRONG - can't change size while iterating
prices = {"apple": 1.00, "banana": 0.50, "cherry": 2.00}
for fruit in prices:
    if prices[fruit] < 1.00:
        del prices[fruit]  # RuntimeError!

# RIGHT - create list of keys first
for fruit in list(prices.keys()):
    if prices[fruit] < 1.00:
        del prices[fruit]

# Or use dictionary comprehension
prices = {k: v for k, v in prices.items() if v >= 1.00}
```

### Mistake 3: Assuming Key Exists

```python
person = {"name": "Alice"}

# WRONG - KeyError if key doesn't exist
age = person["age"]   # KeyError!

# RIGHT - use get()
age = person.get("age", 0)  # Returns 0

# Or check first
if "age" in person:
    age = person["age"]
else:
    age = 0
```

### Mistake 4: Not Understanding Shallow Copy

```python
original = {"data": [1, 2, 3]}

# WRONG - both reference same nested list
copy = original.copy()
copy["data"].append(4)
print(original["data"])   # [1, 2, 3, 4] - original changed!

# RIGHT - deep copy for nested structures
import copy
copy = copy.deepcopy(original)
```

---

## Practice Exercises

### Exercise 1: Character Counter
Count how many times each character appears in a string.

```python
def count_characters(text):
    # Your code here
    pass

# Test
result = count_characters("hello")
# Should return: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

### Exercise 2: Inventory Manager
Create functions to manage a store inventory.

```python
def add_item(inventory, item, quantity):
    """Add quantity to item in inventory."""
    # Your code here
    pass

def remove_item(inventory, item, quantity):
    """Remove quantity from item."""
    # Your code here
    pass

def get_inventory_report(inventory):
    """Print formatted inventory report."""
    # Your code here
    pass

# Test
inv = {}
add_item(inv, "apple", 50)
add_item(inv, "banana", 30)
remove_item(inv, "apple", 10)
get_inventory_report(inv)
```

### Exercise 3: Group by Length
Group words by their length.

```python
def group_by_length(words):
    """Return dictionary with lengths as keys, lists of words as values."""
    # Your code here
    pass

# Test
words = ["cat", "dog", "elephant", "bird", "fish"]
result = group_by_length(words)
# Should return something like: {3: ['cat', 'dog'], 8: ['elephant'], 4: ['bird', 'fish']}
```

### Exercise 4: Merge Dictionaries
Merge two dictionaries, with values from dict2 taking priority.

```python
def merge_dicts(dict1, dict2):
    """Merge dict2 into dict1, dict2 values win conflicts."""
    # Your code here
    pass

# Test
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
result = merge_dicts(d1, d2)
# Should return: {"a": 1, "b": 3, "c": 4}
```

---

## Key Takeaways

1. **Dictionaries store key-value pairs** - like a real dictionary or phone book
2. **Keys must be unique and immutable** - strings, numbers, or tuples
3. **Values can be anything** - any type, including other dictionaries
4. **Use `get()` for safe access** - avoids KeyError for missing keys
5. **Check with `in`** - `if "key" in dict:` before accessing
6. **Iterate with `.items()`** - `for key, value in dict.items():`

## Quick Reference Card

| Operation | How To Do It | Example |
|-----------|--------------|---------|
| Create empty | `{}` or `dict()` | `d = {}` |
| Add/Update | `d[key] = value` | `d["x"] = 10` |
| Access | `d[key]` or `d.get(key)` | `d["x"]` → 10 |
| Safe access | `d.get(key, default)` | `d.get("y", 0)` → 0 |
| Check key | `key in d` | `"x" in d` → True |
| Remove | `d.pop(key)` | `d.pop("x")` → 10 |
| Get keys | `d.keys()` | All keys |
| Get values | `d.values()` | All values |
| Get items | `d.items()` | All (key, value) pairs |
| Merge | `d1 \| d2` or `d1.update(d2)` | Combine dictionaries |
| Copy | `d.copy()` | Shallow copy |
| Clear | `d.clear()` | Remove all items |

---

## Further Reading

- **Next Lesson**: Sets and Tuples - Other useful collection types
- **Practice**: Complete all exercises above
- **Challenge**: Build a simple database using nested dictionaries
- **Explore**: Try using `collections.defaultdict` for automatic default values
