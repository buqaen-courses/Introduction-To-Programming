# Sets and Tuples: Specialized Collections

## Introduction: When to Use What

Python gives us several built-in collection types. Here's when to use each:

| Type | Use When... | Example |
|------|-------------|---------|
| **List** | Order matters, duplicates OK | Shopping list with multiple apples |
| **Dictionary** | Need key-value pairs | Student grades by name |
| **Tuple** | Data shouldn't change | Coordinates (x, y) |
| **Set** | Only care about unique items, order doesn't matter | Unique website visitors |

---

## Tuples: Immutable Sequences

### What is a Tuple?

A **tuple** is like a list that cannot be changed after creation. Think of it as a sealed container - you can look inside, but you can't modify the contents.

```python
# Creating tuples
coordinates = (10, 20)
person = ("Alice", 25, "Engineer")
```

### Why Use Tuples?

1. **Protection**: Data that shouldn't be accidentally modified
2. **Performance**: Tuples are slightly faster than lists
3. **Dictionary keys**: Tuples can be dictionary keys (lists can't!)
4. **Function returns**: Returning multiple values

### Creating Tuples

```python
# Empty tuple
empty = ()
empty = tuple()

# Single element tuple (REQUIRES COMMA!)
single = (42,)   # ← Note the comma!
not_a_tuple = (42)  # This is just the number 42 in parentheses

# Multiple elements
point = (3, 4)
colors = ("red", "green", "blue")

# Without parentheses (tuple packing)
values = 1, 2, 3   # Same as (1, 2, 3)

# From other iterables
letters = tuple("hello")   # ('h', 'e', 'l', 'l', 'o')
numbers = tuple([1, 2, 3]) # (1, 2, 3)
```

### Accessing Tuple Elements

```python
point = (3, 4, 5)

# Same as lists - use indexing
x = point[0]        # 3
y = point[1]        # 4
last = point[-1]    # 5

# Slicing works too
first_two = point[:2]    # (3, 4)
```

### Tuple Operations

```python
t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Concatenation (creates new tuple)
combined = t1 + t2      # (1, 2, 3, 4, 5, 6)

# Repetition
repeated = t1 * 3       # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Length
size = len(t1)          # 3

# Membership
two_in_t1 = 2 in t1     # True

# Count and index (same as lists)
count = t1.count(2)     # 1
position = t1.index(2)  # 1
```

### Important: Tuples Are Immutable

```python
point = (3, 4)

# WRONG - cannot modify!
point[0] = 5   # TypeError!

# RIGHT - create new tuple
new_point = (5, point[1])   # (5, 4)
```

### Tuple Unpacking

```python
# Assign tuple values to multiple variables
point = (10, 20)
x, y = point
print(x)    # 10
print(y)    # 20

# Extended unpacking
first, *middle, last = (1, 2, 3, 4, 5)
print(first)    # 1
print(middle)   # [2, 3, 4]
print(last)     # 5

# Ignore unwanted values
name, _, age = ("Alice", "female", 25)
print(name, age)    # Alice 25

# Swap values (Pythonic!)
a, b = 1, 2
a, b = b, a
print(a, b)    # 2 1
```

### Multiple Return Values

```python
def get_min_max(numbers):
    """Return both min and max."""
    return min(numbers), max(numbers)

# Unpack the returned tuple
minimum, maximum = get_min_max([3, 1, 4, 1, 5])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 5

# Or receive as tuple
result = get_min_max([3, 1, 4, 1, 5])
print(result)   # (1, 5)
```

---

## Sets: Collections of Unique Elements

### What is a Set?

A **set** is an unordered collection of unique items. Think of it like a bag where you can't have duplicates and you can't rely on the order.

```python
# Creating sets
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
```

### Why Use Sets?

1. **Automatic duplicates removal**: Sets only keep unique items
2. **Fast membership testing**: Checking if an item exists is very fast
3. **Mathematical operations**: Unions, intersections, differences
4. **Removing duplicates from lists**: Easy conversion

### Creating Sets

```python
# Empty set (NOT {} - that's an empty dictionary!)
empty = set()

# Set with values
fruits = {"apple", "banana", "cherry"}

# From list (removes duplicates!)
numbers = set([1, 2, 2, 3, 3, 3, 4])
# Result: {1, 2, 3, 4}

# From string (unique characters)
unique_chars = set("hello")
# Result: {'h', 'e', 'l', 'o'}
```

### Important: Sets Are Unordered

```python
my_set = {3, 1, 4, 1, 5}
print(my_set)
# Might print: {1, 3, 4, 5} (order not guaranteed!)

# Can't access by index
my_set[0]   # TypeError!
```

### Set Operations

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union - elements in either set
union = set1 | set2              # {1, 2, 3, 4, 5, 6}
union = set1.union(set2)         # Same thing

# Intersection - elements in both sets
intersection = set1 & set2       # {3, 4}
intersection = set1.intersection(set2)

# Difference - in set1 but not set2
diff = set1 - set2               # {1, 2}
diff = set1.difference(set2)

# Symmetric difference - in either but not both
sym_diff = set1 ^ set2           # {1, 2, 5, 6}
sym_diff = set1.symmetric_difference(set2)
```

### Set Methods

```python
fruits = {"apple", "banana"}

# Add single element
fruits.add("cherry")      # {"apple", "banana", "cherry"}

# Add multiple elements
fruits.update(["date", "elderberry", "fig"])

# Remove (raises error if not found)
fruits.remove("banana")

# Remove (no error if not found)
fruits.discard("grape")   # No error even if "grape" isn't there

# Remove and return arbitrary element
removed = fruits.pop()

# Check membership
"apple" in fruits         # True

# Clear all
fruits.clear()            # set()
```

### Set Comprehensions

```python
# Like list comprehensions but for sets
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Even numbers
evens = {x for x in numbers if x % 2 == 0}
# Result: {2, 4, 6, 8, 10}

# Squares
squares = {x ** 2 for x in range(1, 6)}
# Result: {1, 4, 9, 16, 25}
```

---

## Practical Examples

### Example 1: Remove Duplicates from List

```python
def remove_duplicates(items):
    """Remove duplicates while preserving order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Usage
original = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = remove_duplicates(original)
print(unique)   # [1, 2, 3, 4]

# Quick way (loses order)
unique_fast = list(set(original))
```

### Example 2: Find Common Friends

```python
def find_common_friends(user1_friends, user2_friends):
    """Find friends that both users have."""
    set1 = set(user1_friends)
    set2 = set(user2_friends)
    return set1 & set2

# Usage
alice_friends = ["Bob", "Charlie", "Diana", "Eve"]
bob_friends = ["Alice", "Charlie", "Eve", "Frank"]

common = find_common_friends(alice_friends, bob_friends)
print(f"Common friends: {common}")  # {'Charlie', 'Eve'}

# Find unique to each
alice_only = set(alice_friends) - set(bob_friends)
bob_only = set(bob_friends) - set(alice_friends)
```

### Example 3: Validate User Input

```python
def validate_selection(user_selection, valid_options):
    """Check if user selected valid options."""
    user_set = set(user_selection)
    valid_set = set(valid_options)

    # Find invalid selections
    invalid = user_set - valid_set

    # Find missing required
    missing = valid_set - user_set

    return {
        "valid": not invalid,
        "invalid": invalid,
        "all_selected": not missing,
        "missing": missing
    }

# Usage
valid_colors = ["red", "green", "blue", "yellow"]
user_picked = ["red", "purple", "green"]

result = validate_selection(user_picked, valid_colors)
print(f"Invalid colors: {result['invalid']}")  # {'purple'}
```

### Example 4: Configuration as Tuples

```python
# Use tuples for configuration that shouldn't change
DATABASE_CONFIG = (
    "localhost",  # host
    5432,         # port
    "myapp",      # database
    "user",       # username
    "password"    # password
)

# Unpack for use
host, port, dbname, user, password = DATABASE_CONFIG

# Can't accidentally modify
# DATABASE_CONFIG[0] = "other"  # TypeError!
```

### Example 5: Word Analysis

```python
def analyze_vocab(text1, text2):
    """Compare vocabulary between two texts."""
    # Extract words (simplified)
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())

    # Remove punctuation (simple)
    punctuation = ".,!?;:'\""
    for p in punctuation:
        words1 = {w.replace(p, "") for w in words1}
        words2 = {w.replace(p, "") for w in words2}

    # Remove empty strings
    words1 = {w for w in words1 if w}
    words2 = {w for w in words2 if w}

    return {
        "unique_to_text1": words1 - words2,
        "unique_to_text2": words2 - words1,
        "common": words1 & words2,
        "total_unique": words1 | words2
    }

# Usage
text_a = "Python is great for data science"
text_b = "Python is also great for web development"

analysis = analyze_vocab(text_a, text_b)
print(f"Common words: {analysis['common']}")
print(f"Unique to text A: {analysis['unique_to_text1']}")
```

---

## Common Beginner Mistakes

### Mistake 1: Creating Empty Set Wrong

```python
# WRONG - this creates an empty dictionary!
empty = {}
type(empty)   # <class 'dict'>

# RIGHT
empty = set()
type(empty)   # <class 'set'>
```

### Mistake 2: Forgetting Tuple Comma

```python
# WRONG - not a tuple!
single = (5)
type(single)   # <class 'int'>

# RIGHT
single = (5,)
type(single)   # <class 'tuple'>
```

### Mistake 3: Trying to Access Set by Index

```python
my_set = {1, 2, 3}

# WRONG
first = my_set[0]   # TypeError!

# RIGHT - convert to list or iterate
first = list(my_set)[0]   # Works but order not guaranteed
# Or better:
for item in my_set:
    print(item)
    break
```

### Mistake 4: Modifying Tuple Elements

```python
point = (3, 4)

# WRONG
point[0] = 5   # TypeError!

# RIGHT - create new tuple
new_point = (5, point[1])
# Or convert to list and back
temp = list(point)
temp[0] = 5
new_point = tuple(temp)
```

---

## Comparing Collection Types

### When to Use Each

```python
# LIST - Ordered, changeable, allows duplicates
shopping = ["milk", "eggs", "milk"]  # Can have two milks
shopping.append("bread")              # Can add items

# TUPLE - Ordered, unchangeable, allows duplicates
coordinates = (40.7128, -74.0060)    # Fixed coordinates
color_rgb = (255, 128, 0)             # Fixed color

# SET - Unordered, changeable, unique only
unique_visitors = {"alice", "bob", "alice"}  # Only one "alice"
unique_visitors.add("charlie")              # Can add

# DICT - Key-value pairs, ordered, changeable
student = {"name": "Alice", "grade": "A"}
student["age"] = 20                  # Can add new keys
```

### Performance Comparison

```python
# Membership testing (checking if item exists)
large_list = list(range(10000))
large_set = set(range(10000))

# Set is MUCH faster for checking if item exists
9999 in large_list   # Slow - checks each item one by one
9999 in large_set    # Fast - uses hash table

# But lists are better for ordered access
large_list[5000]     # Fast - direct index access
# large_set[5000]    # Error! Sets don't support indexing
```

---

## Practice Exercises

### Exercise 1: Find Missing Numbers
Find which numbers from 1 to N are missing from a list.

```python
def find_missing(numbers, n):
    """Return set of missing numbers from 1 to n."""
    # Your code here
    pass

# Test
print(find_missing([1, 2, 4, 6], 6))
# Should return: {3, 5}
```

### Exercise 2: Anagram Checker
Check if two words are anagrams (contain same letters).

```python
def is_anagram(word1, word2):
    """Return True if word1 and word2 are anagrams."""
    # Your code here
    pass

# Test
print(is_anagram("listen", "silent"))   # True
print(is_anagram("hello", "world"))      # False
```

### Exercise 3: Stock Portfolio
Track stock purchases and calculate average cost.

```python
def add_purchase(portfolio, stock, price, shares):
    """Add stock purchase to portfolio."""
    # Your code here
    pass

def get_average_cost(portfolio, stock):
    """Calculate average cost per share for a stock."""
    # Your code here
    pass

# Test
portfolio = {}
add_purchase(portfolio, "AAPL", 150.00, 10)
add_purchase(portfolio, "AAPL", 155.00, 5)
add_purchase(portfolio, "GOOGL", 2800.00, 2)

print(get_average_cost(portfolio, "AAPL"))   # Should be ~151.67
```

### Exercise 4: Tuple Sorting
Sort a list of tuples by second element.

```python
def sort_by_second(items):
    """Sort list of tuples by second element."""
    # Your code here
    pass

# Test
data = [(1, 5), (2, 3), (3, 8), (4, 1)]
result = sort_by_second(data)
# Should return: [(4, 1), (2, 3), (1, 5), (3, 8)]
```

---

## Key Takeaways

1. **Tuples are immutable** - Use when data shouldn't change
2. **Sets are for unique items** - Automatically removes duplicates
3. **Sets are unordered** - Can't rely on position or order
4. **Sets are fast** - O(1) membership testing vs O(n) for lists
5. **Use `set()` not `{}`** - Empty brackets make a dictionary!
6. **Tuple comma matters** - `(x,)` is a tuple, `(x)` is not

## Quick Reference Card

| Operation | Tuple | Set |
|-----------|-------|-----|
| Create | `(1, 2, 3)` or `tuple()` | `{1, 2, 3}` or `set()` |
| Empty | `()` | `set()` (not `{}`) |
| Access | `t[0]` | Can't access by index |
| Check membership | `x in t` | `x in s` (faster!) |
| Add element | Can't (immutable) | `s.add(x)` |
| Remove | Can't | `s.remove(x)` or `s.discard(x)` |
| Length | `len(t)` | `len(s)` |
| Unique elements | N/A (can have duplicates) | Automatic |
| Union | N/A | `s1 \| s2` or `s1.union(s2)` |
| Intersection | N/A | `s1 & s2` or `s1.intersection(s2)` |
| Difference | N/A | `s1 - s2` or `s1.difference(s2)` |

---

## Further Reading

- **Next Lesson**: Function Definition - Creating reusable code blocks
- **Practice**: Complete all exercises above
- **Challenge**: Build a simple spell checker using a set of valid words
- **Explore**: Try `frozenset` - an immutable version of set that can be dictionary keys
