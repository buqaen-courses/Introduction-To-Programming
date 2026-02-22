# Basic Python Syntax: Writing Your First Code

## What You'll Learn
- How to write a simple Python program
- Basic Python rules (syntax)
- Common beginner mistakes to avoid

---

## Your First Python Program

Let's start with the classic "Hello, World!" program:

```python
print("Hello, World!")
```

**What this does:** It displays the text "Hello, World!" on the screen.

Try it yourself! Open your Python interpreter or create a `.py` file and run it.

---

## Python's Special Rule: Indentation Matters

Python is unique because it uses **indentation** (spaces at the beginning of lines) to organize code.

### Good Example (Correct Indentation)

```python
if age >= 18:
    print("You are an adult")
    print("You can vote")
```

### Bad Example (Wrong Indentation)

```python
if age >= 18:
print("You are an adult")      # ❌ Wrong! Missing spaces
    print("You can vote")       # ❌ Wrong! Inconsistent spacing
```

### The Rule
- Use **4 spaces** for each level of indentation (most editors do this automatically)
- Always be consistent with your spacing

---

## Comments: Notes for Humans

Comments are text that Python ignores. Use them to explain your code.

```python
# This is a comment - Python ignores this line
print("Hello")  # This comment is at the end of a line

# You can have multiple comments
# Like this
# To explain something longer
```

**Why use comments?**
- To explain what your code does
- To remind yourself later
- To temporarily disable code without deleting it

---

## Variables: Storing Data

Variables are like **labeled boxes** where you store information.

### Creating Variables

```python
name = "Alice"      # A box labeled "name" containing "Alice"
age = 25            # A box labeled "age" containing 25
height = 1.65       # A box labeled "height" containing 1.65
is_student = True   # A box labeled "is_student" containing True
```

### Variable Naming Rules

**✅ Good names:**
```python
user_name = "Bob"
total_count = 100
favorite_color = "blue"
```

**❌ Invalid names (will cause errors):**
```python
2nd_place = "silver"      # Can't start with a number
my-name = "Alice"         # Can't use hyphens
my name = "Bob"           # Can't use spaces
class = "Python"          # Can't use reserved words
```

### Tips for Good Names
- Use descriptive names (`total_price` is better than `tp`)
- Use lowercase with underscores (`snake_case`)
- Be consistent

---

## Data Types: Different Kinds of Information

### 1. Strings (Text)

```python
# Use single or double quotes
greeting = "Hello"
name = 'Alice'

# Both work the same!
message = "It's a nice day"
quote = 'He said "Hello"'
```

### 2. Numbers

```python
# Integers (whole numbers)
age = 25
year = 2024

# Floats (decimal numbers)
price = 19.99
pi = 3.14159
```

### 3. Booleans (True/False)

```python
is_sunny = True
is_raining = False
```

---

## Basic Math Operations

```python
# Addition
result = 5 + 3      # 8

# Subtraction
result = 10 - 4     # 6

# Multiplication
result = 6 * 7      # 42

# Division
result = 15 / 3     # 5.0

# Combining operations
result = (5 + 3) * 2    # 16
```

**Try these in the interactive mode!**

---

## Getting Input from Users

The `input()` function lets your program ask the user for information:

```python
name = input("What's your name? ")
print(f"Hello, {name}!")
```

**Important:** `input()` always gives you text (a string). If you want numbers:

```python
# Convert string to integer
age = int(input("How old are you? "))

# Convert string to float
height = float(input("Your height in meters: "))
```

---

## Common Beginner Mistakes

### Mistake 1: Mismatched Quotes

```python
# ❌ Wrong
print("Hello')
print('Hello")

# ✅ Correct
print("Hello")
print('Hello')
```

### Mistake 2: Wrong Indentation

```python
# ❌ Wrong
if age > 18:
print("Adult")

# ✅ Correct
if age > 18:
    print("Adult")
```

### Mistake 3: Using = Instead of == for Comparison

```python
# ❌ Wrong (= is for assignment)
if x = 5:
    print("x is 5")

# ✅ Correct (== is for comparison)
if x == 5:
    print("x is 5")
```

### Mistake 4: Forgetting Parentheses

```python
# ❌ Wrong
print "Hello"

# ✅ Correct
print("Hello")
```

### Mistake 5: Case Sensitivity

```python
# ❌ Wrong
Print("Hello")
PRINT("Hello")

# ✅ Correct
print("Hello")
```

Python is case-sensitive! `print` and `Print` are different.

---

## Try It Yourself: Exercises

### Exercise 1: Simple Greeting

Create a program that:
1. Asks for the user's name
2. Asks for their age
3. Prints a greeting with both pieces of information

```python
name = input("What's your name? ")
age = input("How old are you? ")
print(f"Hello {name}! You are {age} years old.")
```

### Exercise 2: Simple Calculator

Create a program that:
1. Asks for two numbers
2. Adds them together
3. Shows the result

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1 + num2
print(f"The sum is: {result}")
```

### Exercise 3: Fix the Errors

This program has 3 errors. Can you find and fix them?

```python
# Original (with errors)
name = input("What's your name? )
Age = input("How old are you? )
print("Hello " + name + you are " + age + " years old")
```

<details>
<summary>Click to see the answer</summary>

```python
# Fixed version
name = input("What's your name? ")  # Added missing quote
age = input("How old are you? ")   # Fixed 'Age' to 'age' and added quote
print("Hello " + name + ", you are " + age + " years old")  # Added missing quote
```
</details>

---

## Quick Reference

| Concept | Example | Description |
|---------|---------|-------------|
| Print | `print("Hello")` | Shows text on screen |
| Variable | `x = 5` | Stores a value |
| Input | `name = input("Name? ")` | Gets user input |
| String | `"Hello"` or `'Hello'` | Text data |
| Integer | `42` | Whole number |
| Float | `3.14` | Decimal number |
| Comment | `# This is a note` | Ignored by Python |

---

## Key Takeaways

1. **Python is readable** - It looks almost like English
2. **Indentation matters** - Use 4 spaces for code blocks
3. **Variables store data** - Like labeled boxes
4. **Different data types** - Text, numbers, true/false
5. **Input/Output** - Use `input()` and `print()` to communicate
6. **Comments explain code** - Start with `#`

---

## What's Next?

Now you know the basics! Next, we'll learn:
- More about variables and data types
- How to make decisions in code (if/else)
- How to repeat actions (loops)
