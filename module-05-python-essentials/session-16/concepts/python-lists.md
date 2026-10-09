# Python Lists: Your First Data Structure

## What is a List?

A **list** is like a shopping list or a to-do list - it's an ordered collection of items that you can add to, remove from, and change. Unlike strings, lists can hold any type of data and you CAN change them!

```python
# Lists can hold any type of data
fruits = ["apple", "banana", "cherry"]          # Strings
numbers = [1, 2, 3, 4, 5]                        # Numbers
mixed = [1, "hello", 3.14, True]                 # Mixed types
empty = []                                        # Empty list
```

### Why Lists Matter

Lists are one of the most useful tools in Python:
- Store collections of related data
- Keep items in order
- Easily add or remove items
- Process multiple items with loops
- Build more complex data structures

---

## Creating Lists

### Basic Creation

```python
# Empty list
shopping_list = []
shopping_list = list()   # Alternative

# List with items
colors = ["red", "green", "blue"]

# List from a range
numbers = list(range(1, 6))
# Result: [1, 2, 3, 4, 5]

# List from a string
letters = list("Hello")
# Result: ['H', 'e', 'l', 'l', 'o']

# List of repeated items
zeros = [0] * 5
# Result: [0, 0, 0, 0, 0]
```

### List of Lists (Nested Lists)

```python
# A list can contain other lists!
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access nested items
first_row = matrix[0]        # [1, 2, 3]
center = matrix[1][1]        # 5 (second row, second column)
```

---

## Accessing List Elements

### By Index (Position)

Just like strings, list indices start at 0:

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Access by position
first = fruits[0]          # "apple"
second = fruits[1]         # "banana"
last = fruits[4]           # "elderberry"

# Negative indices (from the end)
last = fruits[-1]          # "elderberry"
second_to_last = fruits[-2]  # "date"

# How many items?
count = len(fruits)        # 5
```

**Visual Representation:**
```
Index:    0        1         2        3          4
         ↓        ↓         ↓        ↓          ↓
List: ["apple", "banana", "cherry", "date", "elderberry"]
         ↑                 ↑                    ↑
       fruits[0]        fruits[2]          fruits[-1]
```

### Common Beginner Mistake

```python
fruits = ["apple", "banana", "cherry"]

# WRONG - index 3 doesn't exist (only 0, 1, 2)
last = fruits[3]   # IndexError!

# RIGHT
last = fruits[2]      # "cherry"
last = fruits[-1]     # "cherry" (safer!)
last = fruits[len(fruits) - 1]  # "cherry" (explicit)
```

---

## Slicing Lists

### Getting Subsets

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing: list[start:end] (end is NOT included!)
subset = numbers[2:5]      # [2, 3, 4] (indices 2, 3, 4)

# From start
beginning = numbers[:4]     # [0, 1, 2, 3]

# To end
ending = numbers[6:]        # [6, 7, 8, 9]

# Every Nth item
every_second = numbers[::2]    # [0, 2, 4, 6, 8]
every_third = numbers[::3]     # [0, 3, 6, 9]

# Reverse
to_back = numbers[::-1]        # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

### Slicing Examples

```python
# Get last N items
tasks = ["email", "meeting", "lunch", "coding", "review"]
last_three = tasks[-3:]         # ["lunch", "coding", "review"]

# Skip first and last
grades = [65, 70, 85, 90, 95]
middle = grades[1:-1]           # [70, 85, 90]

# Copy entire list
copy = numbers[:]               # Same as list(numbers) or numbers.copy()
```

---

## Modifying Lists (Lists Are Mutable!)

Unlike strings, you CAN change lists in place!

### Changing Items

```python
fruits = ["apple", "banana", "cherry"]

# Change one item
fruits[1] = "blueberry"
# Result: ["apple", "blueberry", "cherry"]

# Change a slice
fruits[1:3] = ["blackberry", "cranberry"]
# Result: ["apple", "blackberry", "cranberry"]

# Replace with different number of items
fruits[1:2] = ["kiwi", "mango"]
# Result: ["apple", "kiwi", "mango", "cranberry"]
```

### Adding Items

```python
fruits = ["apple", "banana"]

# Add to end (most common)
fruits.append("cherry")
# Result: ["apple", "banana", "cherry"]

# Insert at specific position
fruits.insert(1, "avocado")
# Result: ["apple", "avocado", "banana", "cherry"]

# Add multiple items from another list
fruits.extend(["date", "elderberry"])
# Result: ["apple", "avocado", "banana", "cherry", "date", "elderberry"]

# You can also use + to combine lists (creates new list)
more_fruits = fruits + ["fig", "grape"]
```

### Removing Items

```python
fruits = ["apple", "banana", "cherry", "banana"]

# Remove by value (first occurrence only!)
fruits.remove("banana")
# Result: ["apple", "cherry", "banana"]

# Remove by index
del fruits[0]
# Result: ["cherry", "banana"]

# Remove and return last item
last = fruits.pop()
# last = "banana", fruits = ["cherry"]

# Remove and return specific index
first = fruits.pop(0)
# Removes and returns the first item

# Clear entire list
fruits.clear()
# Result: []
```

**Important**: `remove()` only removes the first match it finds!

```python
# To remove ALL occurrences of a value
numbers = [1, 2, 3, 2, 4, 2, 5]
while 2 in numbers:
    numbers.remove(2)
# Result: [1, 3, 4, 5]
```

---

## Useful List Methods

### Finding and Counting

```python
numbers = [1, 2, 3, 2, 4, 2, 5]

# Find position (returns index or error)
position = numbers.index(3)       # 2

# Find starting from position 3
position = numbers.index(2, 3)    # 5 (second '2' at index 3)

# Count occurrences
count = numbers.count(2)          # 3 (appears 3 times)

# Check membership (True/False)
has_three = 3 in numbers          # True
has_ten = 10 in numbers           # False
```

### Sorting

```python
scores = [85, 92, 78, 96, 88, 91]

# Sort in place (modifies original list)
scores.sort()
# Result: [78, 85, 88, 91, 92, 96]

# Sort descending
scores.sort(reverse=True)
# Result: [96, 92, 91, 88, 85, 78]

# Create sorted copy (original unchanged)
original = [3, 1, 4, 1, 5]
sorted_copy = sorted(original)
# original: [3, 1, 4, 1, 5]
# sorted_copy: [1, 1, 3, 4, 5]

# Sort strings (case-sensitive by default)
names = ["alice", "Bob", "ALICE", "bob"]
names.sort()
# Result: ["ALICE", "Bob", "alice", "bob"] (uppercase first!)

# Case-insensitive sort
names.sort(key=str.lower)
# Result: ["alice", "ALICE", "Bob", "bob"]
```

### Reversing

```python
numbers = [1, 2, 3, 4, 5]

# Reverse in place
numbers.reverse()
# Result: [5, 4, 3, 2, 1]

# Create reversed copy
original = [1, 2, 3, 4, 5]
reversed_copy = list(reversed(original))
# original: [1, 2, 3, 4, 5]
# reversed_copy: [5, 4, 3, 2, 1]
```

### Copying Lists

```python
original = [1, 2, [3, 4]]

# Shallow copy (shares nested items)
copy1 = original.copy()
copy2 = list(original)
copy3 = original[:]

# Modify copy - original's nested list changes too!
copy1[2][0] = 999
# original becomes: [1, 2, [999, 4]]

# Deep copy (completely independent)
import copy
deep = copy.deepcopy(original)
deep[2][0] = 777
# original stays: [1, 2, [999, 4]]
```

---

## List Operations with Loops

### Basic Looping

```python
fruits = ["apple", "banana", "cherry"]

# Loop through items
for fruit in fruits:
    print(f"I like {fruit}")

# Output:
# I like apple
# I like banana
# I like cherry
```

### Loop with Index

```python
grades = [85, 92, 78, 96]

# Using enumerate
for index, grade in enumerate(grades):
    print(f"Student {index + 1}: {grade}")

# Output:
# Student 1: 85
# Student 2: 92
# Student 3: 78
# Student 4: 96
```

### Building a List

```python
# Start empty, add items
squares = []
for number in range(1, 6):
    squares.append(number ** 2)
# Result: [1, 4, 9, 16, 25]

# List comprehension (shorter way!)
squares = [x ** 2 for x in range(1, 6)]
```

### Filtering a List

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get only even numbers
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
# Result: [2, 4, 6, 8, 10]

# List comprehension (more Pythonic!)
evens = [num for num in numbers if num % 2 == 0]
```

---

## List Comprehensions (Pythonic Way)

List comprehensions are a concise way to create lists.

### Basic Syntax

```python
# Regular way
squares = []
for x in range(1, 6):
    squares.append(x ** 2)

# List comprehension way
squares = [x ** 2 for x in range(1, 6)]
# Result: [1, 4, 9, 16, 25]
```

### With Conditions

```python
numbers = range(1, 21)

# Only even numbers
evens = [x for x in numbers if x % 2 == 0]
# Result: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Squares of odd numbers only
odd_squares = [x ** 2 for x in numbers if x % 2 == 1]
# Result: [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]
```

### Transforming Data

```python
names = ["alice", "bob", "charlie"]

# Capitalize all names
capitalized = [name.title() for name in names]
# Result: ["Alice", "Bob", "Charlie"]

# Get lengths
lengths = [len(name) for name in names]
# Result: [5, 3, 7]
```

---

## Practical Examples

### Example 1: Shopping List Manager

```python
def shopping_list_app():
    shopping = []

    while True:
        print("\nShopping List:")
        for i, item in enumerate(shopping, 1):
            print(f"{i}. {item}")

        print("\nOptions: (a)dd, (r)emove, (q)uit")
        choice = input("Choice: ").lower()

        if choice == 'a':
            item = input("What to add: ")
            shopping.append(item)
            print(f"Added: {item}")

        elif choice == 'r':
            if shopping:
                item = shopping.pop()
                print(f"Removed: {item}")
            else:
                print("List is empty!")

        elif choice == 'q':
            print("Goodbye!")
            break

# Uncomment to run:
# shopping_list_app()
```

### Example 2: Grade Calculator

```python
def calculate_statistics(grades):
    """Calculate grade statistics."""
    if not grades:
        return None

    total = sum(grades)
    count = len(grades)
    average = total / count
    highest = max(grades)
    lowest = min(grades)

    return {
        "count": count,
        "total": total,
        "average": round(average, 2),
        "highest": highest,
        "lowest": lowest
    }

# Usage
grades = [85, 92, 78, 96, 88, 91]
stats = calculate_statistics(grades)

print(f"Grades: {grades}")
print(f"Count: {stats['count']}")
print(f"Average: {stats['average']}")
print(f"Highest: {stats['highest']}")
print(f"Lowest: {stats['lowest']}")
```

### Example 3: Removing Duplicates

```python
def remove_duplicates(items):
    """Remove duplicates while preserving order."""
    seen = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return seen

# Usage
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = remove_duplicates(numbers)
print(unique)  # [1, 2, 3, 4]

# Alternative using set (faster, but loses order)
unique_fast = list(set(numbers))
```

### Example 4: Finding Common Elements

```python
def find_common(list1, list2):
    """Find items present in both lists."""
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common

# Usage
class_a = ["Alice", "Bob", "Charlie", "Diana"]
class_b = ["Bob", "Diana", "Eve", "Frank"]

both = find_common(class_a, class_b)
print(f"In both classes: {both}")  # ['Bob', 'Diana']
```

---

## Common Beginner Mistakes

### Mistake 1: Modifying List While Iterating

```python
# WRONG - skipping items!
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Dangerous!

# RIGHT - create new list
evens = [num for num in numbers if num % 2 == 0]

# Or iterate over a copy
for num in numbers[:]:
    if num % 2 == 0:
        numbers.remove(num)
```

### Mistake 2: Creating Multiple References

```python
# WRONG - both point to same list!
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1)  # [1, 2, 3, 4] - list1 changed too!

# RIGHT - create a copy
list1 = [1, 2, 3]
list2 = list1.copy()  # Or list1[:]
list2.append(4)
print(list1)  # [1, 2, 3] - unchanged!
```

### Mistake 3: Using `=` Instead of `append()`

```python
# WRONG
my_list = []
my_list = 5   # Replaces the list with the number 5!

# RIGHT
my_list = []
my_list.append(5)   # List is now [5]
```

### Mistake 4: Index Out of Range in Loops

```python
fruits = ["apple", "banana", "cherry"]

# WRONG
for i in range(5):  # Tries to access fruits[3] and fruits[4]!
    print(fruits[i])

# RIGHT
for i in range(len(fruits)):
    print(fruits[i])

# BETTER - just iterate directly
for fruit in fruits:
    print(fruit)
```

---

## Practice Exercises

### Exercise 1: Reverse a List
Write a function that reverses a list without using the `reverse()` method.

```python
def reverse_list(items):
    # Your code here
    pass

# Test
print(reverse_list([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]
```

### Exercise 2: Find Maximum
Write a function that finds the maximum value in a list (without using `max()`).

```python
def find_maximum(numbers):
    # Your code here
    pass

# Test
print(find_maximum([3, 7, 2, 9, 1]))  # 9
```

### Exercise 3: Flatten a List
Write a function that flattens a list of lists into a single list.

```python
def flatten(nested):
    # Your code here
    pass

# Test
print(flatten([[1, 2], [3, 4], [5, 6]]))  # [1, 2, 3, 4, 5, 6]
```

### Exercise 4: Rotate List
Write a function that rotates a list by N positions.

```python
def rotate_list(items, n):
    # Your code here
    pass

# Test
print(rotate_list([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]
```

---

## Key Takeaways

1. **Lists are ordered collections** - items stay in the order you add them
2. **Lists are mutable** - you can change, add, and remove items
3. **Index starts at 0** - the first item is at position 0
4. **Slicing creates new lists** - `list[1:3]` gives you a copy
5. **Use list methods** like `append()`, `sort()`, `reverse()`
6. **List comprehensions** are concise and Pythonic - `[x**2 for x in range(5)]`

## Quick Reference Card

| Operation | How To Do It | Example |
|-----------|--------------|---------|
| Create empty | `[]` or `list()` | `my_list = []` |
| Add to end | `append(item)` | `list.append(5)` |
| Insert at position | `insert(pos, item)` | `list.insert(0, 'first')` |
| Remove by value | `remove(item)` | `list.remove('a')` |
| Remove by index | `pop(index)` | `list.pop(0)` |
| Get length | `len(list)` | `len([1,2,3])` → 3 |
| Sort in place | `sort()` | `list.sort()` |
| Create sorted copy | `sorted(list)` | `new = sorted(list)` |
| Reverse in place | `reverse()` | `list.reverse()` |
| Check membership | `item in list` | `3 in [1,2,3]` → True |
| Find index | `index(item)` | `[1,2,3].index(2)` → 1 |
| Count items | `count(item)` | `[1,1,1].count(1)` → 3 |
| Copy list | `copy()` or `[:]` | `new = old.copy()` |
| Clear all | `clear()` | `list.clear()` |

---

## Further Reading

- **Next Lesson**: Python Dictionaries - Key-value pairs for efficient lookups
- **Practice**: Complete all exercises above
- **Challenge**: Create a to-do list application with priorities and due dates
- **Explore**: Try using lists to represent a 2D grid (like a chess board)
