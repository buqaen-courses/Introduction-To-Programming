# Loop Control: Break, Continue, and Else

## What You'll Learn
- How to exit loops early with `break`
- How to skip iterations with `continue`
- How to use the `else` clause with loops
- Common patterns for loop control
- Practical examples of controlled loops

---

## Main Concept: Controlling Your Loops

Sometimes you need to change the normal flow of a loop:
- **Stop early** when you find what you're looking for (`break`)
- **Skip items** that don't meet certain conditions (`continue`)
- **Do something special** when a loop completes normally (`else`)

**Analogy: Searching a Library**
- `break`: When you find the book, stop looking
- `continue`: Skip the damaged books and check the next one
- `else`: If you search the whole library and don't find it, order it online

---

## The `break` Statement: Exit Immediately

`break` immediately stops the current loop and continues with the code after the loop.

### Finding an Item and Stopping

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
target = "cherry"

for fruit in fruits:
    print(f"Checking: {fruit}")
    
    if fruit == target:
        print(f"Found it!")
        break  # Stop immediately

print("Search ended")

# Output:
# Checking: apple
# Checking: banana
# Checking: cherry
# Found it!
# Search ended
```

### Search with User Confirmation

```python
items = ["pen", "pencil", "eraser", "ruler", "marker"]

while True:
    search = input("What are you looking for? (or 'quit'): ")
    
    if search == "quit":
        break
    
    found = False
    for item in items:
        if item == search:
            print(f"Found: {item}")
            found = True
            break  # Stop searching
    
    if not found:
        print("Not in stock")
```

### Finding First Match

```python
numbers = [4, 2, 7, 1, 9, 5]

# Find first number greater than 5
for num in numbers:
    if num > 5:
        print(f"First number > 5: {num}")
        break
else:
    print("No number found greater than 5")
```

---

## The `continue` Statement: Skip and Continue

`continue` skips the rest of the current iteration and moves to the next one.

### Skip Even Numbers

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Odd numbers only:")
for num in numbers:
    if num % 2 == 0:  # If even
        continue  # Skip even numbers
    print(num)

# Output: 1, 3, 5, 7, 9
```

### Skip Empty or Invalid Input

```python
lines = [
    "Hello world",
    "",
    "   ",
    "Python is fun",
    "",
    "Continue learning"
]

print("Valid lines only:")
for line in lines:
    if line.strip() == "":  # Skip empty lines
        continue
    print(f"→ {line}")

# Output:
# → Hello world
# → Python is fun
# → Continue learning
```

### Process Valid Data Only

```python
data = [10, "x", 20, "y", 30, "z"]

total = 0
for item in data:
    if not isinstance(item, int):
        print(f"Skipping non-number: {item}")
        continue
    
    total += item
    print(f"Added {item}, total now: {total}")

print(f"Final total: {total}")
```

---

## The `else` Clause with Loops

The `else` runs when a loop completes **normally** (not by `break`).

### Using `else` for "Not Found"

```python
fruits = ["apple", "banana", "cherry"]
search = "date"

for fruit in fruits:
    if fruit == search:
        print(f"Found: {fruit}")
        break
else:
    # This runs only if loop didn't hit break
    print(f"{search} not found in the list!")

# Output: date not found in the list!
```

### Validating Prime Numbers

```python
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} = {i} × {n//i}")
            return False
    
    return True

# Test
for num in [7, 10, 13, 15]:
    if is_prime(num):
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")
```

### Password Validation

```python
password = input("Enter password: ")
attempts = 3

for attempt in range(attempts):
    if password == "secret":
        print("Access granted!")
        break
    
    remaining = attempts - attempt - 1
    if remaining > 0:
        password = input(f"Wrong! {remaining} tries left: ")
    else:
        password = ""
else:
    # Loop completed without breaking
    print("Access denied - too many failed attempts")
```

---

## Common Patterns

### Pattern 1: Find and Process First Match

```python
def find_and_process(items, condition, process):
    """Find first item matching condition and process it."""
    for item in items:
        if condition(item):
            process(item)
            return True  # Found and processed
    return False  # Not found

# Example: Find first expensive item and apply discount
products = [
    {"name": "Pen", "price": 2},
    {"name": "Book", "price": 15},
    {"name": "Laptop", "price": 1000},
]

def is_expensive(p): return p["price"] > 100
def apply_discount(p): 
    p["price"] *= 0.9
    print(f"Applied discount to {p['name']}: ${p['price']:.2f}")

found = find_and_process(products, is_expensive, apply_discount)
if not found:
    print("No expensive items found")
```

### Pattern 2: Skip Invalid Items

```python
def process_valid_items(data, validator, processor):
    """Process only valid items, skip invalid ones."""
    results = []
    
    for item in data:
        if not validator(item):
            print(f"Skipping invalid: {item}")
            continue
        
        result = processor(item)
        results.append(result)
    
    return results

# Example: Process only positive numbers
def is_positive(x): return x > 0
def double(x): return x * 2

numbers = [5, -3, 8, -1, 10]
results = process_valid_items(numbers, is_positive, double)
print(f"Results: {results}")  # [10, 16, 20]
```

### Pattern 3: Menu with Loop Control

```python
def show_menu():
    print("\n=== Menu ===")
    print("1. Add item")
    print("2. View items")
    print("3. Exit")

items = []

while True:
    show_menu()
    choice = input("Choose: ")
    
    if choice == "3":
        print("Goodbye!")
        break
    
    if choice == "1":
        item = input("Enter item: ")
        if item.strip() == "":
            print("Cannot add empty item!")
            continue
        items.append(item)
        print(f"Added: {item}")
    
    elif choice == "2":
        if not items:
            print("No items yet!")
            continue
        print("Items:")
        for i, item in enumerate(items, 1):
            print(f"  {i}. {item}")
    
    else:
        print("Invalid choice!")
```

---

## Common Beginner Mistakes

### Mistake 1: Using `continue` or `break` Outside a Loop

```python
# ❌ Wrong - SyntaxError
def helper():
    if x < 0:
        continue  # 'continue' not properly in loop

# ✅ Correct
def helper():
    for x in items:
        if x < 0:
            continue
```

### Mistake 2: Forgetting That `break` Exits Only the Innermost Loop

```python
# ❌ Wrong - only breaks inner loop
found = False
for row in matrix:
    for cell in row:
        if cell == target:
            found = True
            break
    # Still in outer loop!

# ✅ Correct - use flag to exit both
found = False
for row in matrix:
    if found:
        break
    for cell in row:
        if cell == target:
            found = True
            break
```

### Mistake 3: Confusing Loop `else` with `if-else`

```python
# ❌ Wrong understanding
for x in items:
    if x > 10:
        print("Big!")
    else:  # This runs EVERY iteration!
        print("Not big")

# ✅ Correct - use for-else for search
for x in items:
    if x == target:
        print("Found!")
        break
else:  # This runs only if loop completed without break
    print("Not found")
```

### Mistake 4: Using `continue` to Skip the Last Iteration

```python
# ❌ Wrong - using continue when we should just loop differently
for i in range(10):
    if i == 9:
        continue  # Skip last iteration
    print(i)

# ✅ Correct - just loop to 9
for i in range(9):
    print(i)
```

### Mistake 5: Thinking `break` Returns from Function

```python
# ❌ Wrong - function returns None
def find_first_positive(numbers):
    for n in numbers:
        if n > 0:
            break  # Exits loop, not function!

# ✅ Correct
result = find_first_positive([-5, -3, 2, 8])
print(result)  # None! (not 2)

# ✅ Correct version
def find_first_positive(numbers):
    for n in numbers:
        if n > 0:
            return n  # Exit function with value
    return None  # Not found
```

---

## Try It Yourself: Exercises

### Exercise 1: Find and Stop

Find the first number divisible by both 3 and 5:

```python
numbers = [4, 7, 10, 12, 15, 18, 20, 25]

for num in numbers:
    if num % 3 == 0 and num % 5 == 0:
        print(f"First divisible by both: {num}")
        break
else:
    print("No number found divisible by both 3 and 5")
```

### Exercise 2: Process Valid Only

Skip invalid email addresses:

```python
emails = [
    "user@example.com",
    "invalid-email",
    "another@domain.org",
    "not-an-email",
    "test@site.net"
]

valid = []
for email in emails:
    if "@" not in email or "." not in email:
        print(f"Invalid: {email}")
        continue
    valid.append(email)

print(f"Valid emails: {valid}")
```

### Exercise 3: Login with Limited Attempts

```python
correct = "secret123"
max_attempts = 3

for attempt in range(max_attempts):
    password = input(f"Attempt {attempt + 1}/{max_attempts}: ")
    
    if password == correct:
        print("Welcome!")
        break
else:
    print("Account locked!")
```

### Exercise 4: Fix the Bugs

```python
# Buggy program
def find_first_even(numbers):
    for n in numbers:
        if n % 2 == 0:
            print(f"Found: {n}")
            break
    else:
        return None
    return n

def process_data(data):
    total = 0
    for item in data:
        if item < 0:
            print("Skipping negative")
            continue
        total = total + item
    return total

# Test
result = find_first_even([1, 3, 5])
print(result)
```

<details>
<summary>Click to see the answer</summary>

```python
# Fixed program
def find_first_even(numbers):
    for n in numbers:
        if n % 2 == 0:
            print(f"Found: {n}")
            return n  # Return the found value
    return None  # Return None if not found

def process_data(data):
    total = 0
    for item in data:
        if item < 0:
            print("Skipping negative")
            continue
        total = total + item
    return total

# Test
result = find_first_even([1, 3, 5, 8, 10])
print(result)  # 8

result = find_first_even([1, 3, 5])
print(result)  # None
```
</details>

---

## Quick Reference

### Loop Control Statements

| Statement | What It Does | When to Use |
|-----------|--------------|-------------|
| `break` | Exit loop immediately | Found what you're looking for |
| `continue` | Skip to next iteration | Current item doesn't qualify |
| `else` (with loop) | Run if no `break` happened | Search/validation didn't find match |

### Common Patterns

| Pattern | Code Example |
|---------|--------------|
| Find first match | `for x in items:`<br>`  if match(x):`<br>`    process(x)`<br>`    break` |
| Skip invalid | `for x in items:`<br>`  if not valid(x):`<br>`    continue`<br>`  process(x)` |
| Search with else | `for x in items:`<br>`  if x == target:`<br>`    found = True`<br>`    break`<br>`else:`<br>`  print("Not found")` |
| Menu loop | `while True:`<br>`  show_menu()`<br>`  if quit: break` |

### Break vs Continue vs Else

| Scenario | break | continue | else |
|----------|-------|----------|------|
| Exit loop early | ✓ | ✗ | ✗ |
| Skip to next item | ✗ | ✓ | ✗ |
| Run after normal completion | ✗ | ✗ | ✓ |
| Works in for loops | ✓ | ✓ | ✓ |
| Works in while loops | ✓ | ✓ | ✓ |

---

## Key Takeaways

1. **`break`** exits the entire loop immediately
2. **`continue`** skips the rest of the current iteration and moves to the next
3. **Loop `else`** runs only if the loop completed normally (no `break`)
4. **`break` exits only the innermost loop** - use flags to exit nested loops
5. **`continue` and `break`** only work inside loops, not in functions
6. **Use `else` with loops** for "not found" or "no match" scenarios
7. **Use flags** (boolean variables) when you need to communicate between nested loops

---

## What's Next?

Now that you can control loops with break, continue, and else:
- You'll write more efficient search algorithms
- You'll handle edge cases and invalid data gracefully
- You'll build interactive programs with proper flow control
- You'll move on to more advanced data structures (lists, dictionaries)
