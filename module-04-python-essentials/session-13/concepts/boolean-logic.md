# Boolean Logic: True or False?

## What You'll Learn
- What True and False mean in programming
- How to use AND, OR, and NOT
- Truth tables for logical operations
- When values are considered "true" or "false"
- Practical examples and common mistakes

---

## Main Concept: The World is Binary

In programming, every question has a simple answer: **Yes** or **No**, **True** or **False**. Boolean logic is the foundation of all decision-making in code.

**Analogy: Light Switches**
- A switch can only be **ON** or **OFF**
- There are no "maybe" positions!
- Boolean values work the same way: **True** (ON) or **False** (OFF)

---

## Boolean Values in Python

### True and False

```python
# These are the only two boolean values
is_active = True
is_deleted = False

# Check the type
print(type(True))   # <class 'bool'>
print(type(False))  # <class 'bool'>
```

### Converting to Boolean

```python
# Non-zero numbers are True
print(bool(1))      # True
print(bool(-5))     # True (any non-zero!)
print(bool(0))      # False

# Non-empty strings are True
print(bool("hello"))  # True
print(bool(""))       # False (empty)

# Non-empty collections are True
print(bool([1, 2, 3]))  # True
print(bool([]))         # False (empty list)
```

---

## Logical Operators

### AND: Both Must Be True

Think of AND like a two-key lock—both keys must turn.

```python
# AND examples
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

# Real-world: Can enter club?
has_ticket = True
is_adult = True
can_enter = has_ticket and is_adult
print(f"Can enter: {can_enter}")  # True
```

### OR: At Least One Must Be True

Think of OR like having two doors—either one gets you in.

```python
# OR examples
print(True or True)     # True
print(True or False)    # True
print(False or True)   # True
print(False or False)  # False

# Real-world: Can get discount?
is_student = False
is_senior = True
gets_discount = is_student or is_senior
print(f"Gets discount: {gets_discount}")  # True
```

### NOT: Reverse the Answer

NOT flips True to False and False to True.

```python
# NOT examples
print(not True)   # False
print(not False)  # True

# Real-world: Is it safe to go out?
is_raining = False
should_go_out = not is_raining
print(f"Should go out: {should_go_out}")  # True

# Another example
is_logged_in = False
if not is_logged_in:
    print("Please log in!")  # This prints
```

---

## Truth Tables

### AND Truth Table

| A | B | A AND B |
|---|---|---------|
| True | True | **True** |
| True | False | **False** |
| False | True | **False** |
| False | False | **False** |

### OR Truth Table

| A | B | A OR B |
|---|---|--------|
| True | True | **True** |
| True | False | **True** |
| False | True | **True** |
| False | False | **False** |

### NOT Truth Table

| A | NOT A |
|---|-------|
| True | **False** |
| False | **True** |

---

## Combining Logical Operators

### Complex Conditions

```python
age = 25
has_license = True
is_sober = True

# All three must be true
can_drive = age >= 18 and has_license and is_sober
print(f"Can drive: {can_drive}")  # True

# Weekend check
day = "Saturday"
is_holiday = False
is_weekend = (day == "Saturday") or (day == "Sunday")
can_relax = is_weekend or is_holiday
print(f"Can relax: {can_relax}")  # True
```

### Using NOT with AND/OR

```python
# NOT with AND
is_banned = False
has_permission = True
can_post = not is_banned and has_permission
print(f"Can post: {can_post}")  # True

# NOT with OR
is_sleeping = True
is_away = False
is_available = not (is_sleeping or is_away)
print(f"Is available: {is_available}")  # False
```

---

## Truthy and Falsy Values

### What Python Considers "True"

These values are treated as `True` in conditions:

```python
# Numbers (any non-zero)
if 5:
    print("5 is truthy")  # Prints

# Non-empty strings
if "hello":
    print("Non-empty string is truthy")  # Prints

# Non-empty collections
if [1, 2, 3]:
    print("Non-empty list is truthy")  # Prints

if {"key": "value"}:
    print("Non-empty dict is truthy")  # Prints
```

### What Python Considers "False"

These values are treated as `False` in conditions:

```python
# Zero
if not 0:
    print("0 is falsy")  # Prints

# Empty string
if not "":
    print("Empty string is falsy")  # Prints

# Empty collections
if not []:
    print("Empty list is falsy")  # Prints

if not {}:
    print("Empty dict is falsy")  # Prints

# None
if not None:
    print("None is falsy")  # Prints
```

### Practical Use Cases

```python
# Check if user entered a name
name = input("Enter your name: ")
if name:  # True if not empty
    print(f"Hello, {name}!")
else:
    print("You didn't enter a name.")

# Check if list has items
shopping_list = ["apples", "milk"]
if shopping_list:  # True if not empty
    print("You need to go shopping!")
else:
    print("Your list is empty.")
```

---

## Common Beginner Mistakes

### Mistake 1: Confusing `=` with `==`

```python
# ❌ Wrong
x = 5
if x = 5:  # SyntaxError!
    print("Five")

# ✅ Correct
if x == 5:
    print("Five")
```

### Mistake 2: Overly Complex Conditions

```python
# ❌ Hard to understand
if not (not has_ticket or not is_adult):
    print("Can enter")

# ✅ Simpler using De Morgan's law
if has_ticket and is_adult:
    print("Can enter")
```

### Mistake 3: Comparing Different Types

```python
# ❌ Wrong
age = "25"  # String
if age == 25:  # Never true!
    print("Adult")

# ✅ Correct
age = int("25")
if age == 25:
    print("Adult")
```

### Mistake 4: Using AND When You Mean OR

```python
# ❌ Wrong - very restrictive
day = "Saturday"
if day == "Saturday" and day == "Sunday":  # Always False!
    print("Weekend")

# ✅ Correct
if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

### Mistake 5: Forgetting NOT Affects Everything After It

```python
# ❌ Confusing
is_weekend = True
is_sunny = False
if not is_weekend and is_sunny:  # Means: (not is_weekend) AND is_sunny
    print("Go to the beach")  # Doesn't print

# ✅ Clear with parentheses
if not (is_weekend and is_sunny):  # Means: NOT (weekend AND sunny)
    print("Maybe stay home")  # Prints
```

---

## Try It Yourself: Exercises

### Exercise 1: Logic Puzzle

Figure out what each expression evaluates to:

```python
a = True
b = False

print(a and b)      # Your answer: ___
print(a or b)       # Your answer: ___
print(not a)        # Your answer: ___
print(not (a and b))  # Your answer: ___
print(not a or b)   # Your answer: ___
```

<details>
<summary>Click to see answers</summary>

```
False
True
False
True
False
```
</details>

### Exercise 2: Access Control System

Write a program that decides if someone can access a file:

```python
# User information
is_logged_in = True
is_admin = False
file_is_public = True

# Can access if: (logged in AND is admin) OR file is public
can_access = (is_logged_in and is_admin) or file_is_public

if can_access:
    print("Access granted!")
else:
    print("Access denied!")

# Try changing the values above to test different scenarios
```

### Exercise 3: Eligibility Checker

Check if someone is eligible for a student discount:

```python
age = int(input("Enter your age: "))
has_student_id = input("Do you have a student ID? (yes/no): ").lower() == "yes"

# Eligible if under 25 with ID OR under 18
is_eligible = (age < 25 and has_student_id) or (age < 18)

if is_eligible:
    print("You qualify for the student discount!")
else:
    print("Sorry, you don't qualify.")
```

### Exercise 4: Fix the Bugs

Find and fix the logic errors:

```python
# Buggy program
age = "20"
is_student = True

if age > 18 and is_student == True:
    print("College student")

day = "Saturday"
if day == "Saturday" and day == "Sunday":
    print("Weekend")

logged_in = True
if not logged_in or is_student:
    print("Special access")
```

<details>
<summary>Click to see answers</summary>

```python
# Fixed program
age = 20  # Convert to int!
is_student = True

if age > 18 and is_student:  # Don't need "== True"
    print("College student")

day = "Saturday"
if day == "Saturday" or day == "Sunday":  # Use OR, not AND
    print("Weekend")

logged_in = True
if not logged_in and is_student:  # Probably meant AND, not OR
    print("Special access")  # Or maybe: if logged_in or is_student:
```
</details>

---

## Quick Reference

### Logical Operators

| Operator | What It Does | Example | Result |
|----------|--------------|---------|--------|
| `and` | Both must be true | `True and False` | `False` |
| `or` | At least one true | `True or False` | `True` |
| `not` | Reverse | `not True` | `False` |

### Truthy Values (Count as True)

| Value | Boolean Result |
|-------|----------------|
| `1, 5, -10` (any non-zero) | `True` |
| `"hello"` (non-empty string) | `True` |
| `[1, 2]` (non-empty list) | `True` |
| `{"key": "val"}` (non-empty dict) | `True` |

### Falsy Values (Count as False)

| Value | Boolean Result |
|-------|----------------|
| `0` | `False` |
| `""` (empty string) | `False` |
| `[]` (empty list) | `False` |
| `{}` (empty dict) | `False` |
| `None` | `False` |

### Operator Precedence

1. `not` (highest)
2. `and`
3. `or` (lowest)

**Example:** `not a and b or c` means `((not a) and b) or c`

---

## Key Takeaways

1. **Boolean values** are only `True` or `False`
2. **AND** requires both conditions to be true
3. **OR** requires at least one condition to be true
4. **NOT** reverses True to False and vice versa
5. **Truthy values** (non-zero, non-empty) count as True in conditions
6. **Falsy values** (zero, empty, None) count as False in conditions
7. **Use parentheses** to make complex logic clear

---

## What's Next?

Now that you understand boolean logic:
- You'll learn about nested conditionals (conditions inside conditions)
- You'll combine boolean logic with loops
- You'll write more complex decision-making programs
