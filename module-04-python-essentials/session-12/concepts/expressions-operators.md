# Expressions and Operators: Python's Calculator

## What You'll Learn
- How to do math in Python (arithmetic operators)
- How to compare values (comparison operators)
- How to combine conditions (logical operators)
- The order Python solves math problems (operator precedence)
- Common mistakes beginners make

---

## Main Concept: Python as a Calculator

Think of Python as a super-powered calculator. You can write **expressions**—combinations of numbers, variables, and operators—that Python evaluates to give you a result.

**Analogy: Following a Recipe**
Just like a recipe tells you what to do first (mix ingredients before baking), Python has rules about which operations to do first.

---

## Arithmetic Operators: Basic Math

### The Four Basic Operations

```python
# Addition (+)
apples = 5
oranges = 3
total_fruit = apples + oranges
print(f"Total fruit: {total_fruit}")  # 8

# Subtraction (-)
money = 100
spent = 35
remaining = money - spent
print(f"Remaining: {remaining}")  # 65

# Multiplication (*)
boxes = 4
items_per_box = 6
total_items = boxes * items_per_box
print(f"Total items: {total_items}")  # 24

# Division (/)
total_cookies = 12
people = 4
cookies_each = total_cookies / people
print(f"Cookies per person: {cookies_each}")  # 3.0
```

### Special Division Operators

```python
# Integer division (//) - drops the decimal
pizzas = 10
people = 3
whole_pizzas_each = pizzas // people
print(f"Whole pizzas each: {whole_pizzas_each}")  # 3

# Modulo (%) - gives the remainder
remaining_slices = pizzas % people
print(f"Leftover slices: {remaining_slices}")  # 1

# Exponentiation (**) - raising to a power
square = 5 ** 2  # 5 squared = 25
cube = 2 ** 3    # 2 cubed = 8
print(f"5 squared: {square}, 2 cubed: {cube}")
```

### Quick Reference: Math Operators

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `10 - 4` | `6` |
| `*` | Multiplication | `6 * 7` | `42` |
| `/` | Division | `15 / 4` | `3.75` |
| `//` | Integer Division | `15 // 4` | `3` |
| `%` | Modulo (remainder) | `15 % 4` | `3` |
| `**` | Exponentiation | `2 ** 3` | `8` |

---

## Comparison Operators: Making Comparisons

### Basic Comparisons

```python
age = 25

# Equal to (==)
is_twenty_five = (age == 25)  # True

# Not equal to (!=)
is_not_thirty = (age != 30)  # True

# Greater than (>)
is_adult = (age > 18)  # True

# Less than (<)
is_child = (age < 13)  # False

# Greater than or equal (>=)
can_vote = (age >= 18)  # True

# Less than or equal (<=)
gets_discount = (age <= 12)  # False

print(f"Can vote: {can_vote}")
```

### Comparing Text (Strings)

```python
name = "Alice"

# Check if equal (case-sensitive!)
is_alice = (name == "Alice")  # True
is_alice_lower = (name == "alice")  # False (case matters!)

# Check if not empty
has_name = bool(name)  # True (non-empty string)
empty = ""
is_empty = bool(empty)  # False
```

---

## Logical Operators: Combining Conditions

### AND, OR, and NOT

Think of logical operators like questions you ask:

```python
has_ticket = True
is_adult = True

# AND - both must be true (like "Do you have a ticket AND are you an adult?")
can_enter = has_ticket and is_adult
print(f"Can enter: {can_enter}")  # True

# OR - at least one must be true (like "Do you have a ticket OR a membership?")
has_membership = False
can_enter_alt = has_ticket or has_membership  # True (has ticket)

# NOT - reverses the answer
is_raining = False
should_go_out = not is_raining  # True (it's not raining)
```

### Real-World Examples

```python
# Checking if someone can drive
age = 20
has_license = True
is_sober = True

can_drive = age >= 18 and has_license and is_sober
print(f"Can drive: {can_drive}")  # True

# Weekend check
day = "Saturday"
is_weekend = (day == "Saturday") or (day == "Sunday")
print(f"Is weekend: {is_weekend}")  # True
```

### Truth Table (Quick Reference)

| Condition 1 | Condition 2 | AND Result | OR Result |
|-------------|-------------|------------|-----------|
| True | True | True | True |
| True | False | False | True |
| False | True | False | True |
| False | False | False | False |

---

## Operator Precedence: Order of Operations

### Python Follows PEMDAS (Like Math Class!)

Just like in math class, Python does operations in a specific order:

1. **P**arentheses `()` - Always first!
2. **E**xponents `**` - Powers and roots
3. **M**ultiplication `*` and **D**ivision `/` (left to right)
4. **A**ddition `+` and **S**ubtraction `-` (left to right)
5. **C**omparisons `==`, `>`, `<`, etc.
6. **L**ogical operators `not`, `and`, `or`

```python
# Without parentheses
result = 2 + 3 * 4
print(result)  # 14 (multiplication first: 3*4=12, then 2+12)

# With parentheses
result = (2 + 3) * 4
print(result)  # 20 (parentheses first: 2+3=5, then 5*4)

# More complex example
total = 10 + 5 * 2 ** 2
# Step 1: 2 ** 2 = 4
# Step 2: 5 * 4 = 20
# Step 3: 10 + 20 = 30
print(total)  # 30
```

### When in Doubt, Use Parentheses!

```python
# Clear and safe
result = (price * quantity) + (shipping * 0.1)

# Confusing
result = price * quantity + shipping * 0.1
# (Same result, but harder to read)
```

---

## Common Beginner Mistakes

### Mistake 1: Using `=` Instead of `==`

```python
# ❌ Wrong - this tries to assign, not compare
if age = 18:  # SyntaxError!
    print("You're 18")

# ✅ Correct - compare values
if age == 18:
    print("You're exactly 18")
```

### Mistake 2: String vs Number Comparison

```python
# ❌ Wrong - comparing string to number
age = "25"  # String from input()
if age == 25:  # Never true!
    print("Adult")

# ✅ Correct - convert first
age = int("25")
if age == 25:
    print("Adult")
```

### Mistake 3: Forgetting Operator Precedence

```python
# ❌ Wrong - might not be what you expect
result = 10 / 2 * 5  # 25.0 (not 1.0)
# Division happens before multiplication (left to right)

# ✅ Correct - use parentheses for clarity
discount = total * (percent / 100)
```

### Mistake 4: Confusing `/` and `//`

```python
# Regular division gives decimal
result1 = 10 / 3  # 3.333...

# Integer division gives whole number
result2 = 10 // 3  # 3

# Be careful when you need exact values!
```

### Mistake 5: Modulo with Negative Numbers

```python
# Modulo can be confusing with negatives
# Stick to positive numbers as a beginner
remainder = 17 % 5  # 2 (easy to understand)
```

---

## Try It Yourself: Exercises

### Exercise 1: Simple Calculator

Create a program that calculates the area of a rectangle.

```python
# Get dimensions
width = float(input("Enter width: "))
height = float(input("Enter height: "))

# Calculate area and perimeter
area = width * height
perimeter = 2 * (width + height)

# Display results
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
```

### Exercise 2: Temperature Converter

Convert Celsius to Fahrenheit.

```python
# Formula: F = (C × 9/5) + 32
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")
```

### Exercise 3: Shopping Calculator

Calculate the total with tax and discount.

```python
price = float(input("Item price: $"))
quantity = int(input("Quantity: "))
tax_rate = 0.08  # 8% tax
discount_threshold = 100  # $100 for discount
discount_rate = 0.10  # 10% discount

subtotal = price * quantity

# Apply discount if over threshold
if subtotal > discount_threshold:
    discount = subtotal * discount_rate
    subtotal = subtotal - discount
    print(f"Discount applied: ${discount:.2f}")

tax = subtotal * tax_rate
total = subtotal + tax

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
```

### Exercise 4: Fix the Bugs

This program has errors. Can you find and fix them?

```python
# Buggy program
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
sum = num1 + num2
print("The sum is: " sum)

average = sum / 2
if average = 10:
    print("Average is exactly 10")
```

<details>
<summary>Click to see the answer</summary>

```python
# Fixed program
num1 = float(input("Enter first number: "))  # Convert to number
num2 = float(input("Enter second number: "))  # Convert to number
sum_result = num1 + num2  # Can't use 'sum' (built-in function)
print("The sum is:", sum_result)  # Added missing comma

average = sum_result / 2
if average == 10:  # Use == for comparison
    print("Average is exactly 10")
```
</details>

---

## Quick Reference

| Category | Operator | What It Does | Example |
|----------|----------|--------------|---------|
| **Math** | `+` | Add | `5 + 3 = 8` |
| **Math** | `-` | Subtract | `10 - 4 = 6` |
| **Math** | `*` | Multiply | `6 * 7 = 42` |
| **Math** | `/` | Divide | `15 / 4 = 3.75` |
| **Math** | `//` | Integer divide | `15 // 4 = 3` |
| **Math** | `%` | Remainder | `15 % 4 = 3` |
| **Math** | `**` | Power | `2 ** 3 = 8` |
| **Compare** | `==` | Equal to | `5 == 5` is `True` |
| **Compare** | `!=` | Not equal to | `5 != 3` is `True` |
| **Compare** | `>` | Greater than | `7 > 5` is `True` |
| **Compare** | `<` | Less than | `3 < 8` is `True` |
| **Compare** | `>=` | Greater or equal | `5 >= 5` is `True` |
| **Compare** | `<=` | Less or equal | `4 <= 6` is `True` |
| **Logic** | `and` | Both true | `True and True` is `True` |
| **Logic** | `or` | At least one true | `True or False` is `True` |
| **Logic** | `not` | Reverse | `not True` is `False` |

### Precedence Order (Highest to Lowest)

1. `()` - Parentheses
2. `**` - Exponentiation
3. `*`, `/`, `//`, `%` - Multiply/Divide
4. `+`, `-` - Add/Subtract
5. `==`, `!=`, `>`, `<`, `>=`, `<=` - Comparisons
6. `not` - Logical NOT
7. `and` - Logical AND
8. `or` - Logical OR

---

## Key Takeaways

1. **Arithmetic operators** (`+`, `-`, `*`, `/`, `//`, `%`, `**`) do math calculations
2. **Comparison operators** (`==`, `!=`, `>`, `<`, `>=`, `<=`) compare values and return True/False
3. **Logical operators** (`and`, `or`, `not`) combine multiple conditions
4. **Operator precedence** determines which operation happens first—use parentheses to be clear
5. **Always use `==`** for comparison, not `=` (which is for assignment)
6. **Convert input** to numbers with `int()` or `float()` before doing math

---

## What's Next?

Now that you know how to do calculations and comparisons, you'll learn:
- How Python decides which operations to do first (evaluation order in detail)
- How to make decisions in your programs (if/else statements)
- How to repeat actions (loops)
- How to work with collections of data (lists)
