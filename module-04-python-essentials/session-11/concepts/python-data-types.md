# Python Data Types: Kinds of Information

## What You'll Learn
- The main data types in Python
- When to use each type
- How to check what type something is
- How to convert between types

---

## What Are Data Types?

Just like in real life we categorize things (fruits, vehicles, animals), Python categorizes information into different **data types**.

Think of data types as different shapes of containers:
- A **string** container holds text
- An **integer** container holds whole numbers
- A **float** container holds decimal numbers
- A **boolean** container holds True or False

---

## The Four Main Data Types

### 1. Strings (str) - Text

Strings hold text - any sequence of characters like letters, numbers, symbols, and spaces.

```python
# Creating strings
name = "Alice"
message = 'Hello, World!'
greeting = "I'm learning Python!"

# You can use single or double quotes
quote = 'He said "Hello"'  # Single quotes outside, double inside
quote2 = "It's a nice day" # Double quotes outside, single inside

# Print the type
print(type(name))   # Output: <class 'str'>
```

#### String Tricks

```python
# Joining strings (concatenation)
first = "Hello"
second = "World"
message = first + " " + second   # "Hello World"

# Repeating strings
line = "-" * 20   # "--------------------"

# Getting the length
text = "Python"
print(len(text))   # Output: 6
```

---

### 2. Integers (int) - Whole Numbers

Integers are whole numbers - positive, negative, or zero, but no decimals.

```python
# Integers
age = 25
temperature = -5
year = 2024
items = 0

# They can be as big as you need!
big_number = 999999999999999999

print(type(age))   # Output: <class 'int'>
```

---

### 3. Floats (float) - Decimal Numbers

Floats are numbers with decimal points.

```python
# Floats
price = 19.99
height = 1.75
pi = 3.14159
temperature = -2.5

print(type(price))   # Output: <class 'float'>
```

**Why are they called "float"?** It's short for "floating point" - the decimal point can "float" to different positions.

---

### 4. Booleans (bool) - True or False

Booleans can only be one of two values: `True` or `False`.

```python
# Booleans
is_student = True
has_pet = False
is_raining = True

print(type(is_student))   # Output: <class 'bool'>
```

**Note:** In Python, `True` and `False` must be capitalized!

---

## Checking Data Types

Use the `type()` function to see what type something is:

```python
name = "Alice"
age = 25
height = 1.65
is_student = True

print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(height))      # <class 'float'>
print(type(is_student))  # <class 'bool'>
```

---

## Converting Between Types

Sometimes you need to change one type to another. This is called **type conversion**.

### String to Number

```python
# Getting input always gives you a string
age_string = "25"

# Convert string to integer
age_number = int(age_string)
print(age_number + 5)   # Output: 30

# Convert string to float
price_string = "19.99"
price_number = float(price_string)
print(price_number * 2)  # Output: 39.98
```

### Number to String

```python
age = 25

# Convert number to string
age_string = str(age)
print("I am " + age_string + " years old")   # "I am 25 years old"

# Or use f-strings (easier!)
print(f"I am {age} years old")   # "I am 25 years old"
```

### Number to Number

```python
# Integer to float (adds .0)
whole = 5
with_decimal = float(whole)
print(with_decimal)   # Output: 5.0

# Float to integer (cuts off decimal)
price = 19.99
whole_price = int(price)
print(whole_price)    # Output: 19 (not rounded!)
```

---

## Common Beginner Mistakes

### Mistake 1: Trying to Add Different Types

```python
# ❌ Error: Can't add string and number
age = 25
print("I am " + age + " years old")   # TypeError!

# ✅ Fix: Convert to string
print("I am " + str(age) + " years old")
# Or use f-string
print(f"I am {age} years old")
```

### Mistake 2: Input Always Returns a String

```python
# ❌ Wrong: Trying to do math with strings
age = input("How old are you? ")
next_year = age + 1   # Error! Can't add string and int

# ✅ Fix: Convert to number first
age = int(input("How old are you? "))
next_year = age + 1   # Works!
```

### Mistake 3: Confusing Float and Integer

```python
# Division always gives a float
total = 10 / 2
print(total)          # Output: 5.0 (not 5!)
print(type(total))    # <class 'float'>

# Use // for integer division
whole = 10 // 2
print(whole)          # Output: 5
print(type(whole))    # <class 'int'>
```

### Mistake 4: Forgetting Quotes

```python
# ❌ Without quotes, Python thinks it's a variable
print(Hello)   # Error! Variable 'Hello' not found

# ✅ With quotes, it's a string
print("Hello") # Works!
```

---

## Try It Yourself: Exercises

### Exercise 1: Type Detective

What type is each variable? Write down your answers, then check with `type()`.

```python
a = "Hello"
b = 42
c = 3.14
d = True
e = "123"
f = 0
```

<details>
<summary>Click to see answers</summary>

- a: `str` (string)
- b: `int` (integer)
- c: `float` (float)
- d: `bool` (boolean)
- e: `str` (string - quotes make it text, even though it looks like a number!)
- f: `int` (integer - zero is still an integer)
</details>

### Exercise 2: Fix the Calculator

This program has errors. Fix them!

```python
# Original (with errors)
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
sum = num1 + num2
print("The sum is: " + sum)
```

<details>
<summary>Click to see the answer</summary>

```python
# Fixed version
num1 = int(input("Enter first number: "))   # Convert to integer
num2 = int(input("Enter second number: "))   # Convert to integer
sum = num1 + num2
print("The sum is: " + str(sum))             # Convert back to string
# Or use f-string: print(f"The sum is: {sum}")
```
</details>

### Exercise 3: Create a Profile

Create variables for a user profile and print a summary:

```python
# Your code here
# Create variables for:
# - username (string)
# - age (integer)
# - height in meters (float)
# - is_member (boolean)

# Then print a profile like:
# "User: Alice, Age: 25, Height: 1.65m, Member: True"
```

### Exercise 4: Type Conversion Practice

Predict what each will output, then test:

```python
print(int(5.9))           # ?
print(float(5))           # ?
print(str(100))           # ?
print(int("50") + 10)     # ?
print("50" + "10")        # ?
```

<details>
<summary>Click to see answers</summary>

```python
print(int(5.9))           # 5 (truncates, doesn't round)
print(float(5))           # 5.0
print(str(100))           # "100" (but prints without quotes)
print(int("50") + 10)     # 60 (converts then adds)
print("50" + "10")        # "5010" (joins as text)
```
</details>

---

## Quick Reference

| Type | Use For | Example | Conversion |
|------|---------|---------|------------|
| `str` | Text | `"Hello"` | `str(x)` |
| `int` | Whole numbers | `42` | `int(x)` |
| `float` | Decimals | `3.14` | `float(x)` |
| `bool` | True/False | `True` | `bool(x)` |

---

## Key Takeaways

1. **Four main types**: `str` (text), `int` (whole numbers), `float` (decimals), `bool` (True/False)
2. **Strings use quotes** - text goes in single or double quotes
3. **Numbers don't use quotes** - 42 is a number, "42" is text
4. **Input gives strings** - remember to convert if you need numbers
5. **Use `type()`** to check what type something is
6. **Convert with functions** - `int()`, `float()`, `str()`, `bool()`

---

## What's Next?

Now you understand data types! Next, we'll learn:
- How to work with these types in more detail
- Type conversion in practice
- Operators for each type
