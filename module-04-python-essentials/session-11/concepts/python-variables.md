# Python Variables: Storing Information

## What You'll Learn
- What variables are and why we use them
- How to create and use variables
- Rules for naming variables
- How to update variable values

---

## What is a Variable?

A **variable** is like a **labeled container** that stores information your program needs.

Think of it like a box with a name tag:

```
┌─────────────────┐
│   Box: "age"    │  ← Label (variable name)
│                 │
│    Content:     │
│      25         │  ← Value stored inside
└─────────────────┘
```

### Real-World Analogy

Imagine you're organizing your room:
- You have a box labeled "Socks" containing your socks
- You have a box labeled "Books" containing your books
- You have a box labeled "Toys" containing your toys

In Python:
- `socks = "wool socks"` creates a "box" named socks
- `books = 15` creates a "box" named books with the number 15

---

## Creating Your First Variables

Creating a variable is simple: give it a name, use `=` (the assignment operator), and give it a value.

```python
# Creating variables
name = "Alice"
age = 25
height = 1.65
is_student = True

# Using the variables
print(name)        # Output: Alice
print(age)         # Output: 25
print(height)      # Output: 1.65
print(is_student)  # Output: True
```

### The Assignment Operator (=)

The `=` sign in Python doesn't mean "equals" like in math. It means **"assign the value on the right to the name on the left."**

```python
# Read this as: "x gets the value 10"
x = 10

# Read this as: "name gets the value 'Bob'"
name = "Bob"
```

---

## Variable Naming Rules

Python has rules for what you can name variables:

### ✅ Valid Names

```python
# These all work:
name = "Alice"
user_name = "Bob"      # Underscores are OK
age2 = 26              # Numbers are OK (just not at the start)
_total = 100           # Starting with underscore is OK
MAX_SIZE = 50          # All caps is OK (convention for constants)
```

### ❌ Invalid Names (Will Cause Errors)

```python
# These will NOT work:
2name = "Alice"        # Can't start with a number
my-name = "Bob"        # Can't use hyphens
my name = "Charlie"    # Can't use spaces
class = "Python"       # Can't use Python's reserved words
$price = 10            # Can't use special characters except _
```

### Reserved Words to Avoid

These words have special meaning in Python, so you can't use them as variable names:

```python
# Don't use these as variable names:
False, None, True, and, as, assert, async, await, break, class,
continue, def, del, elif, else, except, finally, for, from, global,
if, import, in, is, lambda, nonlocal, not, or, pass, raise, return,
try, while, with, yield
```

---

## Best Practices for Naming Variables

### Use Descriptive Names

**❌ Bad - unclear what the variable means:**
```python
x = 25
n = "Alice"
d = 3.14
```

**✅ Good - clear and descriptive:**
```python
age = 25
username = "Alice"
pi_value = 3.14
```

### Use snake_case (Lowercase with Underscores)

Python convention is to use lowercase letters with underscores between words:

```python
# ✅ Good (snake_case)
user_name = "Alice"
total_score = 100
is_valid = True

# ❌ Avoid these styles in Python
userName = "Alice"     # camelCase (common in other languages)
UserName = "Alice"     # PascalCase (used for classes)
username = "Alice"     # lowercase (OK for single words)
```

---

## Updating Variable Values

Variables can change their values. That's why they're called "variable" - they can vary!

### Simple Updates

```python
score = 0
print(score)      # Output: 0

score = 10
print(score)      # Output: 10

score = 25
print(score)      # Output: 25
```

### Using a Variable's Current Value

```python
counter = 5
print(counter)    # Output: 5

# Use the current value and add 1
counter = counter + 1
print(counter)    # Output: 6

# Shorthand version (does the same thing)
counter += 1    # Add 1 to counter
counter += 5    # Add 5 to counter
counter -= 2    # Subtract 2 from counter
```

### Common Shorthand Operators

```python
x = 10

x += 5      # Same as: x = x + 5      (x is now 15)
x -= 3      # Same as: x = x - 3      (x is now 12)
x *= 2      # Same as: x = x * 2      (x is now 24)
x /= 4      # Same as: x = x / 4      (x is now 6.0)
```

---

## Variables Can Store Different Types

```python
# Text (strings)
message = "Hello, World!"

# Whole numbers (integers)
items = 42

# Decimal numbers (floats)
price = 19.99

# True/False values (booleans)
is_active = True
```

We'll learn more about data types in the next lesson!

---

## Common Beginner Mistakes

### Mistake 1: Using Undeclared Variables

```python
# ❌ Error: NameError
print(my_variable)   # Error! Variable doesn't exist yet

# ✅ Fix: Create the variable first
my_variable = "Hello"
print(my_variable)   # Works!
```

### Mistake 2: Confusing = with ==

```python
# ❌ Wrong: = is for assignment, not comparison
if x = 5:
    print("x is 5")

# ✅ Correct: == is for comparison
if x == 5:
    print("x is 5")
```

### Mistake 3: Misspelling Variable Names

```python
name = "Alice"

# ❌ Error: NameError (different spelling)
print(naem)   # Error! 'naem' is not defined

# ✅ Correct
print(name)   # Works!
```

### Mistake 4: Trying to Use Reserved Words

```python
# ❌ Error: SyntaxError
class = "Python 101"   # 'class' is a reserved word!

# ✅ Fix: Use a different name
course_name = "Python 101"
```

---

## Try It Yourself: Exercises

### Exercise 1: Create Your Own Variables

Create variables for:
- Your name
- Your age
- Your favorite number
- Whether you like pizza (True or False)

Then print each one!

```python
name = "Your Name"
age = 20
favorite_number = 7
likes_pizza = True

print(name)
print(age)
print(favorite_number)
print(likes_pizza)
```

### Exercise 2: Variable Update Challenge

Start with `score = 0`. Update it to:
1. Add 10
2. Add 25
3. Subtract 5
4. Double it (multiply by 2)

What's the final score?

```python
score = 0
score += 10
score += 25
score -= 5
score *= 2
print(score)   # What will this print?
```

### Exercise 3: Fix the Errors

Find and fix the errors in this code:

```python
# Original (with errors)
2nd_place = "Bob"
my-score = 100
my name = "Alice"
class = "Python"
Print(my name)
```

<details>
<summary>Click to see the answer</summary>

```python
# Fixed version
second_place = "Bob"        # Can't start with number
my_score = 100              # Can't use hyphens
my_name = "Alice"           # Can't use spaces
course = "Python"           # 'class' is reserved
print(my_name)              # 'Print' should be lowercase
```
</details>

### Exercise 4: Swapping Values

Can you swap the values of two variables without losing either value?

```python
a = 5
b = 10

# Your code here to swap a and b
# So that a becomes 10 and b becomes 5

print(a)  # Should print: 10
print(b)  # Should print: 5
```

**Hint:** You might need a temporary variable, or use Python's cool multiple assignment feature!

<details>
<summary>Click to see two solutions</summary>

**Solution 1 - Using a temporary variable:**
```python
a = 5
b = 10
temp = a
a = b
b = temp
print(a, b)  # 10 5
```

**Solution 2 - Python's cool way:**
```python
a = 5
b = 10
a, b = b, a   # Python magic!
print(a, b)   # 10 5
```
</details>

---

## Quick Reference

| Concept | Example | Meaning |
|---------|---------|---------|
| Create variable | `x = 5` | Store 5 in a container named x |
| Update variable | `x = 10` | Change x to hold 10 |
| Add to variable | `x += 3` | Add 3 to current value of x |
| Valid name | `my_var` | Letters, numbers, underscores |
| Invalid name | `2var`, `my-var` | Can't start with number, no hyphens |

---

## Key Takeaways

1. **Variables store information** - like labeled boxes
2. **Create with `=`** - name = value
3. **Names should be descriptive** - use `user_age` instead of `x`
4. **Follow naming rules** - no spaces, no starting with numbers
5. **Use snake_case** - lowercase with underscores
6. **Variables can change** - that's why they're called "variable"

---

## What's Next?

Now that you know how to store information, let's learn about:
- Different types of data (numbers, text, etc.)
- How to work with each type
- Converting between types
