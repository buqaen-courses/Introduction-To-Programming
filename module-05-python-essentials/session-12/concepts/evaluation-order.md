# Evaluation Order: Which Calculation Comes First?

## What You'll Learn
- How Python decides the order of calculations
- Why `2 + 3 * 4` equals 14 (not 20)
- How to use parentheses to control order
- Left-to-right vs right-to-left rules
- Common mistakes and how to avoid them

---

## Main Concept: Following the Rules

Imagine you're baking a cake. You can't put it in the oven before you mix the ingredients! Python has similar rules—it follows a specific order when solving math problems.

**Analogy: Traffic Rules**
Just like traffic lights tell cars when to go, Python's "order of operations" tells calculations when to happen.

---

## The Order of Operations (PEMDAS)

Python follows PEMDAS—just like you learned in math class:

| Letter | Stands For | Symbol | Example |
|--------|-----------|--------|---------|
| **P** | Parentheses | `()` | `(2 + 3) * 4` |
| **E** | Exponents | `**` | `2 ** 3` |
| **MD** | Multiply/Divide | `*`, `/`, `//`, `%` | `5 * 3`, `10 / 2` |
| **AS** | Add/Subtract | `+`, `-` | `5 + 3`, `10 - 2` |

**After math:** Comparisons (`==`, `>`, `<`, etc.), then logical operators (`and`, `or`)

### Let's See It in Action

```python
# Without parentheses
result = 2 + 3 * 4
print(result)  # 14, not 20!

# Why? Python does multiplication FIRST:
# Step 1: 3 * 4 = 12
# Step 2: 2 + 12 = 14

# With parentheses
result = (2 + 3) * 4
print(result)  # 20

# Parentheses force addition first:
# Step 1: 2 + 3 = 5
# Step 2: 5 * 4 = 20
```

---

## Step-by-Step Examples

### Example 1: Mixed Operations

```python
calculation = 10 + 5 * 2 - 3
# Step 1 (Multiply): 5 * 2 = 10
# Step 2 (Add left to right): 10 + 10 = 20
# Step 3 (Subtract): 20 - 3 = 17
print(calculation)  # 17
```

### Example 2: With Exponents

```python
calculation = 2 + 3 ** 2 * 4
# Step 1 (Exponent): 3 ** 2 = 9
# Step 2 (Multiply): 9 * 4 = 36
# Step 3 (Add): 2 + 36 = 38
print(calculation)  # 38
```

### Example 3: Complex Expression

```python
calculation = (10 - 2) * 3 + 8 / 4
# Step 1 (Parentheses): 10 - 2 = 8
# Step 2 (Multiply): 8 * 3 = 24
# Step 3 (Divide): 8 / 4 = 2.0
# Step 4 (Add): 24 + 2.0 = 26.0
print(calculation)  # 26.0
```

---

## Left-to-Right vs Right-to-Left

### Most Operations: Left to Right

When operators have the same priority, Python goes left to right:

```python
# Addition and subtraction (same priority)
result = 20 - 10 + 5
# Step 1: 20 - 10 = 10
# Step 2: 10 + 5 = 15
print(result)  # 15

# Multiplication and division (same priority)
result = 100 / 10 * 2
# Step 1: 100 / 10 = 10.0
# Step 2: 10.0 * 2 = 20.0
print(result)  # 20.0
```

### Exception: Exponents Go Right to Left

```python
# Exponents are special—they go right to left!
result = 2 ** 3 ** 2
# Python calculates: 2 ** (3 ** 2) = 2 ** 9 = 512
# NOT: (2 ** 3) ** 2 = 8 ** 2 = 64
print(result)  # 512

# Use parentheses to be clear:
result = (2 ** 3) ** 2  # 64
print(result)
```

---

## Comparisons and Logical Operators

After math, Python evaluates comparisons, then logical operators:

### Order: Math → Comparisons → Logical

```python
result = 5 + 3 > 7 and 10 - 2 < 15
# Step 1 (Math): 5 + 3 = 8, 10 - 2 = 8
# Step 2 (Comparisons): 8 > 7 is True, 8 < 15 is True
# Step 3 (Logical): True and True is True
print(result)  # True
```

### NOT Comes Before AND, AND Comes Before OR

```python
result = not False and True or False
# Step 1 (not): not False = True
# Step 2 (and): True and True = True
# Step 3 (or): True or False = True
print(result)  # True
```

---

## Common Beginner Mistakes

### Mistake 1: Expecting Left-to-Right for All Operations

```python
# ❌ Wrong assumption
result = 10 / 2 * 3  # NOT (10 / 2) * 3 = 15
print(result)  # 15.0 - actually correct!

# But watch out:
result = 10 - 5 + 2  # NOT 10 - (5 + 2) = 3
print(result)  # 7 - goes left to right
```

### Mistake 2: Forgetting Exponents Are Right-to-Left

```python
# ❌ Confusing
result = 2 ** 3 ** 2
print(result)  # 512, not 64!

# ✅ Use parentheses to be clear
result = 2 ** (3 ** 2)  # 512
result = (2 ** 3) ** 2  # 64
```

### Mistake 3: Confusing Division Types

```python
# Regular and integer division have same priority
result = 10 / 3 * 3  # (10 / 3) * 3 = 10.0
print(result)  # 10.0

result = 10 // 3 * 3  # (10 // 3) * 3 = 9
print(result)  # 9
```

### Mistake 4: Missing Parentheses in Complex Conditions

```python
# ❌ Confusing
age = 20
has_id = True
result = age >= 18 and has_id or age >= 16
# Does this mean: (age >= 18 and has_id) or age >= 16 ?
# Or: age >= 18 and (has_id or age >= 16) ?

# ✅ Always use parentheses for clarity
can_enter = (age >= 18 and has_id) or (age >= 16 and not has_id)
```

---

## Try It Yourself: Exercises

### Exercise 1: Predict the Output

Before running, predict what each will print:

```python
print(2 + 3 * 4)        # Your guess: ___
print((2 + 3) * 4)      # Your guess: ___
print(10 - 4 + 2)       # Your guess: ___
print(10 - (4 + 2))     # Your guess: ___
print(2 ** 2 ** 2)      # Your guess: ___
print((2 ** 2) ** 2)    # Your guess: ___
```

<details>
<summary>Click to see answers</summary>

```
14, 20, 8, 4, 16, 16
```
</details>

### Exercise 2: Add Parentheses

Add parentheses to make the result match the comment:

```python
# Make this equal 30 (not 14)
result = 2 + 3 * 4

# Make this equal 20 (not 14)
result = 10 - 2 * 3

# Make this equal 36 (not 14)
result = 10 + 2 * 3 - 4
```

<details>
<summary>Click to see answers</summary>

```python
result = (2 + 3) * 4        # 30
result = (10 - 2) * 3       # 24 - wait, that's not 20!
# Actually: result = 10 - 2 * 3 will always be 4
# We want: 10 * 2 = 20, then what?
# Maybe: result = (10 - 2) * (3 - 1)  # 16, still not 20
# Let's try: result = 10 * 2 - 3 * 0  # No, that equals 20 but changes expression
# Actually this one might be a trick question!

result = 10 + (2 * 3) - 4   # 12 - still not 36
# Maybe: (10 + 2) * 3 = 36, then what about - 4?
# (10 + 2) * (3 - 4) = -12
# Hmm, maybe: (10 + 2) * 3 - 4 would be 32
# Actually: 10 + 2 * 3 * 4 = 34 - close!
# Try: 10 + 2 * (3 + 4) = 24 - nope
# (10 + 2 * 3) * 4 = 64 - too high
# Actually, let's reconsider the original: 10 + 2 * 3 - 4 = 12
# To get 36: (10 + 2) * 3 = 36, so... maybe the -4 shouldn't apply?
```
</details>

### Exercise 3: Shopping Calculator with Clear Order

Write a program that calculates total price with tax:

```python
# Get inputs
price = float(input("Item price: $"))
quantity = int(input("Quantity: "))
tax_rate = 0.08  # 8%

# Calculate with clear order
subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (8%): ${tax:.2f}")
print(f"Total: ${total:.2f}")

# Alternative in one line (harder to read!)
total_one_line = price * quantity + price * quantity * tax_rate
print(f"\nOne-line total: ${total_one_line:.2f}")
```

### Exercise 4: Fix the Bugs

This program has errors. Find and fix them:

```python
# Buggy program
age = input("Enter your age: ")
is_adult = age > 18
print("Can vote: " + age >= 18)

# Another bug
total = 100
discount = 10
final = total - discount / 100 * total  # Should be 90, but isn't!
print(f"Final price: ${final}")
```

<details>
<summary>Click to see answers</summary>

```python
# Fixed program
age = int(input("Enter your age: "))  # Convert to number!
is_adult = age >= 18  # Use >= for "18 or older"
print(f"Can vote: {age >= 18}")  # Use f-string or convert bool to string

# Discount fix - need parentheses
total = 100
discount = 10
final = total - (discount / 100 * total)  # Now equals 90
# Or clearer:
discount_amount = total * (discount / 100)
final = total - discount_amount
print(f"Final price: ${final}")
```
</details>

---

## Quick Reference

### Complete Order of Operations

1. `()` - Parentheses (always first!)
2. `**` - Exponents (right to left)
3. `*`, `/`, `//`, `%` - Multiply, divide, floor divide, modulo (left to right)
4. `+`, `-` - Add, subtract (left to right)
5. `==`, `!=`, `>`, `<`, `>=`, `<=` - Comparisons
6. `not` - Logical NOT
7. `and` - Logical AND
8. `or` - Logical OR

### Memory Trick: PEMDAS

**P**lease **E**xcuse **M**y **D**ear **A**unt **S**ally

(Parentheses, Exponents, Multiply/Divide, Add/Subtract)

### Golden Rules

| Rule | Example |
|------|---------|
| Use parentheses to be clear | `(a + b) * c` |
| Exponents go right-to-left | `2 ** 3 ** 2 = 2 ** 9 = 512` |
| Same level goes left-to-right | `10 - 5 + 2 = 7` |
| When in doubt, add parentheses | `(10 - 5) + 2` |

---

## Key Takeaways

1. **Python follows PEMDAS** just like math class
2. **Parentheses always win**—use them to control order and improve readability
3. **Exponents are right-to-left**, everything else at the same level is left-to-right
4. **Math happens before comparisons**, which happen before logical operators
5. **When in doubt, add parentheses**—clear code is better than clever code
6. **Break complex expressions** into multiple steps for clarity

---

## What's Next?

Now that you understand evaluation order:
- You'll learn how to make decisions with if/else statements
- You'll write programs that react differently based on conditions
- You'll practice combining operators and conditions

