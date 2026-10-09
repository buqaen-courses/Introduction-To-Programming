# Conditional Statements: Making Decisions in Code

## What You'll Learn
- How to make your program make decisions
- Using `if`, `else`, and `elif` statements
- Comparing values to make choices
- Combining multiple conditions
- Common mistakes to avoid

---

## Main Concept: The Program Chooses Its Path

Think of a conditional statement like a crossroads. Your program reaches a decision point and chooses which path to take based on a condition.

**Analogy: A Traffic Light**
- Green light? → Go!
- Red light? → Stop!
- Yellow light? → Slow down and prepare to stop.

---

## The Basic if Statement

### Simple Decision Making

```python
age = 20

if age >= 18:
    print("You are an adult!")
    print("You can vote.")

print("This always prints (outside the if)")
```

**How it works:**
1. Check if `age >= 18` is `True`
2. If yes, run the indented code
3. The last line runs no matter what

### The if-else Structure

```python
temperature = 85

if temperature > 80:
    print("It's hot outside!")
    print("Wear shorts.")
else:
    print("It's not too hot.")
    print("Regular clothes are fine.")
```

**Key point:** One of these will ALWAYS run—either the `if` part or the `else` part.

### Multiple Choices with elif

```python
score = 85

if score >= 90:
    grade = "A"
    message = "Excellent work!"
elif score >= 80:
    grade = "B"
    message = "Good job!"
elif score >= 70:
    grade = "C"
    message = "Fair performance."
elif score >= 60:
    grade = "D"
    message = "Needs improvement."
else:
    grade = "F"
    message = "Failed."

print(f"Your grade: {grade} - {message}")
```

**How elif works:**
- Python checks each condition in order
- When it finds a `True` condition, it runs that block and skips the rest
- `else` catches anything that didn't match

---

## Comparison Operators in Conditions

### Basic Comparisons

```python
# Check if equal
name = "Alice"
if name == "Alice":
    print("Hello, Alice!")

# Check if not equal
password = "secret123"
if password != "admin":
    print("Password is not the default. Good!")

# Greater than and less than
age = 25
if age > 18:
    print("Adult")
if age < 13:
    print("Child")

# Greater/less than or equal
items = 5
if items >= 5:
    print("You have enough items")
```

### Checking if Something is "Truthy"

```python
# Non-empty strings are "truthy"
name = input("Enter your name: ")
if name:  # Same as: if name != ""
    print(f"Hello, {name}!")
else:
    print("You didn't enter a name.")

# Non-zero numbers are "truthy"
count = 0
if count:
    print(f"You have {count} messages")
else:
    print("No messages")
```

---

## Combining Conditions with Logical Operators

### Using AND (Both must be true)

```python
age = 20
has_license = True

# Both conditions must be true
if age >= 18 and has_license:
    print("You can drive!")
else:
    print("You cannot drive.")
```

### Using OR (At least one must be true)

```python
day = "Saturday"
is_holiday = False

# Either condition can be true
if day == "Saturday" or day == "Sunday" or is_holiday:
    print("It's a day off!")
else:
    print("It's a work day.")
```

### Using NOT (Reverse the condition)

```python
is_raining = False

if not is_raining:
    print("No umbrella needed!")
else:
    print("Take an umbrella.")

# Another example
logged_in = False
if not logged_in:
    print("Please log in first.")
```

### Combining All Three

```python
age = 25
has_ticket = True
is_vip = False

# Complex condition
if (age >= 18 and has_ticket) or is_vip:
    print("Welcome to the concert!")
else:
    print("Cannot enter.")
```

---

## Common Beginner Mistakes

### Mistake 1: Using `=` Instead of `==`

```python
# ❌ Wrong - this tries to assign a value
age = 25
if age = 18:  # SyntaxError!
    print("You're 18")

# ✅ Correct - compare values
if age == 18:
    print("You're exactly 18")
```

### Mistake 2: Forgetting the Colon

```python
# ❌ Wrong - missing colon
if age > 18
    print("Adult")

# ✅ Correct
if age > 18:
    print("Adult")
```

### Mistake 3: Wrong Indentation

```python
# ❌ Wrong - inconsistent indentation
if age > 18:
    print("Adult")
     print("Can vote")  # Indentation error!

# ✅ Correct - use 4 spaces
if age > 18:
    print("Adult")
    print("Can vote")
```

### Mistake 4: Confusing elif with Multiple ifs

```python
# ❌ Wrong - multiple ifs (all might run)
score = 95
if score >= 60:
    print("Passing")
if score >= 80:
    print("Good")
if score >= 90:
    print("Excellent")
# This prints all three!

# ✅ Correct - elif (only one runs)
if score >= 90:
    print("Excellent")
elif score >= 80:
    print("Good")
elif score >= 60:
    print("Passing")
```

### Mistake 5: String Comparison Case Sensitivity

```python
# ❌ Wrong - case matters!
name = "alice"
if name == "Alice":
    print("Hello!")  # Won't print!

# ✅ Correct - check both cases or convert
if name == "Alice" or name == "alice":
    print("Hello!")

# Or better:
if name.lower() == "alice":
    print("Hello!")
```

---

## Try It Yourself: Exercises

### Exercise 1: Age Categorizer

Categorize people by age.

```python
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age!")
elif age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")
```

### Exercise 2: Simple Login System

Check username and password.

```python
# Stored credentials
correct_username = "admin"
correct_password = "secret123"

# Get user input
username = input("Username: ")
password = input("Password: ")

# Check credentials
if username == correct_username and password == correct_password:
    print("Login successful! Welcome!")
elif username != correct_username:
    print("Error: Username not found.")
elif password != correct_password:
    print("Error: Wrong password.")
```

### Exercise 3: Number Guessing Game

Give hints about a number.

```python
import random

secret = random.randint(1, 100)
guess = int(input("Guess a number (1-100): "))

if guess == secret:
    print("🎉 Correct! You win!")
elif guess < secret:
    print("Too low! Try again.")
else:
    print("Too high! Try again.")

print(f"The secret number was: {secret}")
```

### Exercise 4: Fix the Bugs

Find and fix the errors:

```python
# Buggy program
age = input("How old are you? ")

if age > 18
    print("Adult")
    print("You can vote")
else
    print("Minor")

if age = 18
    print("Exactly 18!")
```

<details>
<summary>Click to see the answer</summary>

```python
# Fixed program
age = int(input("How old are you? "))  # Convert to number!

if age > 18:  # Added colon
    print("Adult")
    print("You can vote")
else:  # Added colon
    print("Minor")

if age == 18:  # Use == and add colon
    print("Exactly 18!")
```
</details>

---

## Quick Reference

### Condition Structure

```python
# Simple if
if condition:
    # code

# If-else
if condition:
    # code if true
else:
    # code if false

# If-elif-else
if condition1:
    # code 1
elif condition2:
    # code 2
elif condition3:
    # code 3
else:
    # default code
```

### Common Comparisons

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `7 > 5` | `True` |
| `<` | Less than | `3 < 5` | `True` |
| `>=` | Greater or equal | `5 >= 5` | `True` |
| `<=` | Less or equal | `4 <= 5` | `True` |

### Logical Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `and` | Both true | `True and True` | `True` |
| `or` | At least one true | `True or False` | `True` |
| `not` | Reverse | `not True` | `False` |

### Key Rules

| Rule | Example |
|------|---------|
| Always use `==` for comparison | `if x == 5:` |
| Don't forget the colon | `if x > 5:` |
| Indent the code block | 4 spaces |
| `elif` means "else if" | `elif x > 3:` |
| `else` has no condition | `else:` |

---

## Key Takeaways

1. **`if` statements** let your program make decisions
2. **`else`** provides an alternative when the condition is false
3. **`elif`** (else if) lets you check multiple conditions in order
4. **Use `==`** for comparison, not `=` (which assigns values)
5. **Don't forget the colon** `:` at the end of if/elif/else lines
6. **Indentation matters**—Python uses it to know what code belongs to the condition
7. **Combine conditions** with `and`, `or`, and `not` for complex logic

---

## What's Next?

Now that you can make decisions:
- You'll learn about boolean logic (True/False values in detail)
- You'll write more complex decision trees (nested conditionals)
- You'll combine conditionals with loops for powerful programs
