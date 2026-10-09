# String Formatting: Creating Professional Output

## What You'll Learn
- How to use f-strings to insert variables into text
- How to format numbers (decimals, currency, percentages)
- How to align text in columns
- How to create clean, readable output

## What is String Formatting? (The Mad Libs Analogy)

Remember Mad Libs? You have a story with blanks like "My name is ______ and I am ______ years old." String formatting is like filling in those blanks with your own values.

### The Problem: Messy String Building

```python
# The old, hard-to-read way (don't do this!)
name = "Alice"
age = 25
message = "My name is " + name + ", I am " + str(age) + " years old."
# Hard to read, easy to make mistakes!
```

### The Solution: F-Strings

```python
# Clean, readable, professional!
name = "Alice"
age = 25
message = f"My name is {name}, I am {age} years old."
# Much better!
```

---

## F-Strings: The Modern Way

**F-strings** (formatted string literals) are the easiest way to format strings in Python. They're the best choice for beginners!

### Basic F-String Usage

```python
# Put 'f' before the string, use {variables} inside
name = "Alice"
age = 25

message = f"Hello, my name is {name} and I am {age} years old."
# Result: "Hello, my name is Alice and I am 25 years old."
```

### Doing Math in F-Strings

```python
a, b = 10, 3
result = f"{a} + {b} = {a + b}"
# Result: "10 + 3 = 13"

price = 50
discount = 10
final = f"Price: ${price}, Discount: ${discount}, Total: ${price - discount}"
# Result: "Price: $50, Discount: $10, Total: $40"
```

---

## Formatting Numbers

### Controlling Decimal Places

```python
pi = 3.14159265359

# Show 2 decimal places
print(f"Pi: {pi:.2f}")      # "Pi: 3.14"

# Show 4 decimal places
print(f"Pi: {pi:.4f}")      # "Pi: 3.1416"
```

### Formatting Currency

```python
price = 29.99

# Basic currency format
print(f"Price: ${price:.2f}")      # "Price: $29.99"

# Large numbers with commas
big_price = 1234.50
print(f"Price: ${big_price:,.2f}")  # "Price: $1,234.50"
```

### Formatting Percentages

```python
ratio = 0.856

# Convert to percentage
print(f"Success rate: {ratio:.1%}")  # "Success rate: 85.6%"

# Percentage with 0 decimals
print(f"Completed: {ratio:.0%}")     # "Completed: 86%"
```

---

## Aligning Text

### Creating Simple Tables

```python
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]

# Create a nice table
print(f"{'Name':<10} {'Score':>6}")
print("-" * 18)
for name, score in zip(names, scores):
    print(f"{name:<10} {score:>6}")

# Output:
# Name       Score
# ------------------
# Alice          95
# Bob            87
# Charlie        92
```

Alignment options:
- `<` Left align
- `>` Right align
- `^` Center

### More Alignment Examples

```python
text = "Hi"

print(f"[{text:<10}]")   # [Hi        ] - left aligned
print(f"[{text:>10}]")   # [        Hi] - right aligned
print(f"[{text:^10}]")   # [    Hi    ] - centered
```

---

## Multi-Line F-Strings

```python
name = "Alice"
age = 25
city = "New York"

message = f"""
Name:   {name}
Age:    {age}
City:   {city}
Next year, I'll be {age + 1}!
"""

print(message)
# Output:
# Name:   Alice
# Age:    25
# City:   New York
# Next year, I'll be 26!
```

---

## Common Beginner Mistakes

### Mistake 1: Forgetting the 'f' Prefix

```python
# ❌ Wrong - missing 'f'
name = "Alice"
message = "Hello, {name}"   # Result: "Hello, {name}"

# ✅ Correct
message = f"Hello, {name}"  # Result: "Hello, Alice"
```

### Mistake 2: Using Quotes Inside Quotes

```python
# ❌ Wrong - causes syntax error
message = f"He said "Hello""   # Syntax error!

# ✅ Correct - use different quote types
message = f'He said "Hello"'   # Single quotes outside
message = f"He said 'Hello'"   # Double quotes outside
message = f"He said \"Hello\"" # Escaped quotes
```

### Mistake 3: Wrong Format Specifier

```python
# ❌ Wrong - trying to format text as number
text = "Hello"
print(f"{text:.2f}")   # Error! Can't format string as float

# ✅ Correct
number = 3.14159
print(f"{number:.2f}")  # "3.14"
```

---

## Try It Yourself: Exercises

### Exercise 1: Simple Receipt
Create a formatted receipt for a purchase.

```python
def print_receipt(item, price, quantity):
    total = price * quantity
    print("=" * 30)
    print(f"{'RECEIPT':^30}")
    print("=" * 30)
    print(f"{'Item:':<15} {item}")
    print(f"{'Price:':<15} ${price:.2f}")
    print(f"{'Quantity:':<15} {quantity}")
    print("-" * 30)
    print(f"{'Total:':<15} ${total:.2f}")
    print("=" * 30)

# Test
print_receipt("Coffee", 3.50, 2)
```

### Exercise 2: Grade Report
Create a formatted grade report.

```python
def grade_report(name, grades):
    average = sum(grades) / len(grades)
    print(f"\n{'='*30}")
    print(f"{'GRADE REPORT':^30}")
    print(f"{'='*30}")
    print(f"Student: {name}")
    print(f"{'-'*30}")
    for i, grade in enumerate(grades, 1):
        print(f"Test {i}: {grade:>20}")
    print(f"{'-'*30}")
    print(f"Average: {average:>19.1f}")
    print(f"{'='*30}")

# Test
grade_report("Alice", [85, 92, 78, 96])
```

### Exercise 3: Temperature Converter
Format temperature conversions nicely.

```python
def format_temperature(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return f"{celsius:.1f}°C = {fahrenheit:.1f}°F"

# Test
print(format_temperature(0))      # 0.0°C = 32.0°F
print(format_temperature(100))    # 100.0°C = 212.0°F
print(format_temperature(37))     # 37.0°C = 98.6°F
```

---

## Quick Reference

| What You Want | How to Do It | Example | Result |
|--------------|--------------|---------|--------|
| Insert variable | `f"{var}"` | `f"{name}"` | value of name |
| 2 decimals | `f"{n:.2f}"` | `f"{3.14159:.2f}"` | 3.14 |
| Percentage | `f"{n:.1%}"` | `f"{0.85:.1%}"` | 85.0% |
| Thousands separator | `f"{n:,}"` | `f"{1234567:,}"` | 1,234,567 |
| Left align (10 chars) | `f"{s:<10}"` | `f"{'Hi':<10}"` | 'Hi        ' |
| Right align (10 chars) | `f"{s:>10}"` | `f"{'Hi':>10}"` | '        Hi' |
| Center (10 chars) | `f"{s:^10}"` | `f"{'Hi':^10}"` | '    Hi    ' |
| Currency | `f"${n:.2f}"` | `f"${29.99:.2f}"` | $29.99 |

---

## Key Takeaways

1. **F-strings are the best choice** - put `f` before quotes and use `{variable}` inside
2. **Format numbers with `:.2f`** - controls decimal places (2 in this example)
3. **Align text with `<`, `>`, `^`** - left, right, and center alignment
4. **Use `:.1%` for percentages** - converts decimals to percentages
5. **You can do math inside f-strings** - `{age + 1}` works perfectly

## What's Next?

In the next lesson, you'll learn about **Text Processing** - how to search, split, and manipulate strings to analyze and transform text data. You'll build practical programs like word counters and text cleaners.
