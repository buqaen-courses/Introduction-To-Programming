# Input and Output: Talking to Your Program

## What You'll Learn
- How to get information from users (input)
- How to show information to users (output)
- How to format text nicely
- Common mistakes beginners make

---

## What is Input and Output?

Think of your program like a conversation:
- **Input** = The user speaks to the program (typing information)
- **Output** = The program speaks to the user (displaying text)

```
User: "What's your name?"  ← This is what the user types (input)
Program: "Hello, Alice!"  ← This is what the program shows (output)
```

---

## Basic Output: The print() Function

The `print()` function is how your program talks to the user.

### Simple Printing

```python
print("Hello, World!")
print("I am learning Python")
```

**Output:**
```
Hello, World!
I am learning Python
```

### Printing Multiple Things

```python
name = "Alice"
age = 25

# Print multiple items
print("Name:", name)
print("Age:", age)
print("Name:", name, "Age:", age)
```

**Output:**
```
Name: Alice
Age: 25
Name: Alice Age: 25
```

### Customizing print()

```python
# Stay on the same line (no newline)
print("Hello", end=" ")
print("World")  # Output: Hello World

# Use a custom separator
print("apple", "banana", "cherry", sep=", ")
# Output: apple, banana, cherry
```

---

## Basic Input: The input() Function

The `input()` function lets your program ask questions and get answers.

### Simple Input

```python
name = input("What's your name? ")
print("Hello, " + name + "!")
```

**How it works:**
1. Program shows: "What's your name? "
2. User types: Alice
3. Program stores "Alice" in the variable `name`
4. Program prints: "Hello, Alice!"

### Input Always Returns Text (Strings)

```python
age = input("How old are you? ")
print(type(age))  # Shows: <class 'str'> (text, not a number!)
```

**Important:** Even if the user types a number, `input()` gives you text.

### Converting Input to Numbers

```python
# Get a whole number (integer)
age = int(input("How old are you? "))
print("Next year you'll be", age + 1)

# Get a decimal number (float)
height = float(input("Your height in meters: "))
print("You are", height, "meters tall")
```

| Function | Use For | Example |
|----------|---------|---------|
| `int()` | Whole numbers | `int("25")` → `25` |
| `float()` | Decimal numbers | `float("1.75")` → `1.75` |
| `str()` | Convert to text | `str(25)` → `"25"` |

---

## String Formatting: Making Output Pretty

### f-strings (Recommended)

The easiest way to format text in Python 3.6+:

```python
name = "Alice"
age = 25
height = 1.65

# Put variables inside curly braces
print(f"Hello, {name}!")
print(f"You are {age} years old")
print(f"Your height is {height} meters")

# Do calculations inside the braces
print(f"Next year you'll be {age + 1}")
print(f"Double your age is {age * 2}")
```

**Output:**
```
Hello, Alice!
You are 25 years old
Your height is 1.65 meters
Next year you'll be 26
Double your age is 50
```

### Formatting Numbers

```python
pi = 3.14159265359
price = 19.99

# Round to 2 decimal places
print(f"Pi is approximately {pi:.2f}")  # 3.14

# Show currency
print(f"Price: ${price:.2f}")  # $19.99

# Add commas for large numbers
population = 8000000000
print(f"World population: {population:,}")  # 8,000,000,000
```

---

## ASCII Diagram: How Input/Output Works

```
┌─────────────────────────────────────────────────────────┐
│                      USER                              │
│  Types: "Alice"          Sees: "Hello, Alice!"        │
└──────────┬──────────────────────▲────────────────────────┘
           │                      │
           │ input()              │ print()
           │                      │
           ▼                      │
┌─────────────────────────────────────────────────────────┐
│                    YOUR PROGRAM                         │
│  1. Ask for name: input("Name? ")                       │
│  2. Store: name = "Alice"                               │
│  3. Respond: print(f"Hello, {name}!")                  │
└─────────────────────────────────────────────────────────┘
```

---

## Common Beginner Mistakes

### Mistake 1: Forgetting to Convert Input

```python
# ❌ Wrong - trying to add text to a number
age = input("How old are you? ")
next_year = age + 1  # ERROR! Can't add text + number

# ✅ Correct
age = int(input("How old are you? "))
next_year = age + 1  # Works!
```

### Mistake 2: Mismatched Quotes

```python
# ❌ Wrong - mixing quote types
print("Hello')

# ✅ Correct
print("Hello")
print('Hello')
```

### Mistake 3: Forgetting f-string Prefix

```python
name = "Alice"

# ❌ Wrong - missing the 'f'
print("Hello, {name}!")  # Shows: Hello, {name}!

# ✅ Correct
print(f"Hello, {name}!")  # Shows: Hello, Alice!
```

### Mistake 4: Spaces in Input

```python
# The space after the question makes output look better
name = input("What's your name?")   # User types right next to ?
name = input("What's your name? ")  # Better - space before input
```

### Mistake 5: NameError - Using Wrong Variable Name

```python
# ❌ Wrong - 'Age' is different from 'age'
Age = input("How old? ")
print(f"You are {age} years old")  # ERROR - 'age' not defined

# ✅ Correct
age = input("How old? ")
print(f"You are {age} years old")
```

---

## Try It Yourself: Exercises

### Exercise 1: Personal Greeting

Create a program that asks for the user's name and age, then prints a greeting.

```python
name = input("What's your name? ")
age = int(input("How old are you? "))
print(f"Hello, {name}! You are {age} years old.")
```

### Exercise 2: Simple Calculator

Create a program that adds two numbers.

```python
print("=== Simple Addition Calculator ===")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
total = num1 + num2
print(f"{num1} + {num2} = {total}")
```

### Exercise 3: Rectangle Calculator

Calculate the area and perimeter of a rectangle.

```python
print("=== Rectangle Calculator ===")
width = float(input("Enter width: "))
height = float(input("Enter height: "))

area = width * height
perimeter = 2 * (width + height)

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
```

### Exercise 4: Fix the Bugs

This program has 4 errors. Can you find and fix them?

```python
# Buggy program
name = input("What's your name? )
Age = int(input("How old are you? "))
print("Hello " + name + , you are", age, "years old")
```

<details>
<summary>Click to see the answer</summary>

```python
# Fixed program
name = input("What's your name? ")  # Added missing quote
age = int(input("How old are you? "))  # Changed Age to age
print("Hello " + name + ", you are", age, "years old")  # Fixed syntax error
# Or better with f-string:
print(f"Hello {name}, you are {age} years old")
```
</details>

---

## Quick Reference

| Task | Code Example |
|------|--------------|
| Print text | `print("Hello")` |
| Get text input | `name = input("Name? ")` |
| Get number input | `age = int(input("Age? "))` |
| Format with f-string | `print(f"Hello, {name}")` |
| Format number | `print(f"{price:.2f}")` |
| Convert to text | `str(42)` |
| Convert to integer | `int("42")` |
| Convert to float | `float("3.14")` |

---

## Key Takeaways

1. **`print()`** shows output to the user
2. **`input()`** gets text from the user
3. **`input()` always returns text** - use `int()` or `float()` for numbers
4. **f-strings** (`f"Hello, {name}"`) make formatting easy
5. **Variables store values** for later use

---

## What's Next?

Now you know how to communicate with your program! Next, we'll learn:
- How to do calculations (operators and expressions)
- How to make decisions (if/else)
- How to repeat actions (loops)
