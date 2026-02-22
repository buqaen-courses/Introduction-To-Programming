# For Loops: Repeating Code Made Easy

## What You'll Learn
- How to repeat code multiple times with for loops
- Looping over lists, strings, and ranges
- Using `range()` for counting
- Common loop patterns
- Common mistakes to avoid

---

## Main Concept: Do It Again (and Again)

A **for loop** lets you repeat a block of code for each item in a sequence. Instead of writing the same code 10 times, you write it once and tell Python to run it 10 times.

**Analogy: A Recipe**
- "For each egg in the carton, crack it into the bowl"
- You don't say: "Crack egg 1, crack egg 2, crack egg 3..."
- The loop handles the repetition!

---

## Basic For Loop Syntax

### Looping Over a List

```python
fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    print(f"I like {fruit}")

# Output:
# I like apple
# I like banana
# I like cherry
# I like date
```

**How it works:**
1. The loop takes the first item (`"apple"`) and stores it in `fruit`
2. Runs the indented code (prints the message)
3. Takes the next item (`"banana"`) and repeats
4. Continues until all items are processed

### Looping Over a String

```python
message = "Hello"

for char in message:
    print(char)

# Output:
# H
# e
# l
# l
# o
```

---

## The range() Function

### Counting with range()

```python
# Count from 0 to 4 (stops before 5)
for i in range(5):
    print(f"Count: {i}")

# Output:
# Count: 0
# Count: 1
# Count: 2
# Count: 3
# Count: 4
```

### Starting from a Different Number

```python
# Count from 1 to 5
for i in range(1, 6):
    print(f"Number: {i}")

# Output:
# Number: 1
# Number: 2
# Number: 3
# Number: 4
# Number: 5
```

### Counting by Steps

```python
# Even numbers from 2 to 10
for i in range(2, 11, 2):
    print(f"Even: {i}")

# Output:
# Even: 2
# Even: 4
# Even: 6
# Even: 8
# Even: 10
```

### Counting Backwards

```python
# Count down from 5 to 1
for i in range(5, 0, -1):
    print(f"Countdown: {i}")

print("Blast off!")
```

---

## Practical Loop Patterns

### Pattern 1: Accumulator (Adding Things Up)

```python
# Calculate the sum of numbers
numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total = total + num
    # or: total += num

print(f"Total: {total}")  # 150
```

### Pattern 2: Counter (Counting Matches)

```python
# Count how many items pass a test
grades = [85, 92, 78, 95, 88, 70]
passing_count = 0

for grade in grades:
    if grade >= 70:
        passing_count += 1

print(f"Students passing: {passing_count}")
```

### Pattern 3: Finding Maximum/Minimum

```python
# Find the highest score
scores = [85, 92, 78, 95, 88, 70]
highest = scores[0]  # Start with first score

for score in scores[1:]:  # Check the rest
    if score > highest:
        highest = score

print(f"Highest score: {highest}")
```

### Pattern 4: Building a New List

```python
# Create a new list from an existing one
names = ["alice", "bob", "charlie"]
upper_names = []

for name in names:
    upper_names.append(name.upper())

print(upper_names)  # ['ALICE', 'BOB', 'CHARLIE']
```

---

## Using enumerate() for Index

### Getting Both Index and Value

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Output:
# 0: apple
# 1: banana
# 2: cherry
```

### Starting from 1 Instead of 0

```python
# For numbered lists (like rankings)
for rank, fruit in enumerate(fruits, start=1):
    print(f"{rank}. {fruit}")

# Output:
# 1. apple
# 2. banana
# 3. cherry
```

---

## Common Beginner Mistakes

### Mistake 1: Modifying a List While Looping Over It

```python
# ❌ Wrong - don't do this!
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:  # If even
        numbers.remove(num)  # Skip some items!

print(numbers)  # [1, 3, 5] - but 4 was skipped!

# ✅ Correct - create a new list
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
```

### Mistake 2: Forgetting the Colon

```python
# ❌ Wrong
for i in range(5)
    print(i)

# ✅ Correct
for i in range(5):
    print(i)
```

### Mistake 3: Indentation Error

```python
# ❌ Wrong
for i in range(5):
print(i)  # Not indented!

# ✅ Correct
for i in range(5):
    print(i)  # Properly indented
```

### Mistake 4: Wrong Range Parameters

```python
# ❌ Confusing
# range(end) - starts at 0, stops BEFORE end
for i in range(5):  # 0, 1, 2, 3, 4 (not 5!)
    print(i)

# range(start, end) - starts at start, stops BEFORE end
for i in range(1, 5):  # 1, 2, 3, 4 (not 5!)
    print(i)
```

### Mistake 5: Reusing the Loop Variable

```python
# ❌ Unexpected behavior
for i in range(5):
    print(i)

# i still exists after the loop!
print(f"Final value of i: {i}")  # Prints 4
```

---

## Try It Yourself: Exercises

### Exercise 1: Multiplication Table

Print a multiplication table for a number:

```python
number = int(input("Enter a number: "))

print(f"Multiplication table for {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} × {i} = {result}")
```

### Exercise 2: Shopping Total

Calculate the total of a shopping list:

```python
prices = [2.50, 3.75, 1.25, 8.99, 4.50]
total = 0

print("Your shopping list:")
for i, price in enumerate(prices, 1):
    print(f"  Item {i}: ${price:.2f}")
    total += price

print(f"\nTotal: ${total:.2f}")

# Add tax
tax = total * 0.08
final = total + tax
print(f"Tax (8%): ${tax:.2f}")
print(f"Final: ${final:.2f}")
```

### Exercise 3: Password Strength Checker

Check each character in a password:

```python
password = input("Enter a password: ")

has_digit = False
has_upper = False
has_lower = False

for char in password:
    if char.isdigit():
        has_digit = True
    elif char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True

# Check results
if len(password) >= 8 and has_digit and has_upper and has_lower:
    print("✅ Strong password!")
else:
    print("❌ Weak password!")
    if len(password) < 8:
        print("  - Too short (need 8+ characters)")
    if not has_digit:
        print("  - Add a number")
    if not has_upper:
        print("  - Add an uppercase letter")
    if not has_lower:
        print("  - Add a lowercase letter")
```

### Exercise 4: Fix the Bugs

```python
# Buggy program
numbers = [1, 2, 3, 4, 5]
for num in range(numbers):
    print(numbers)

total = 0
for i in range(1, 10)
    total = total + i
print(f"Sum 1-10: {total}")
```

<details>
<summary>Click to see the answer</summary>

```python
# Fixed program
numbers = [1, 2, 3, 4, 5]
for num in numbers:  # Loop over the list, not range(list)
    print(num)  # Print num, not numbers

total = 0
for i in range(1, 11):  # Need : and range goes UP TO the end number
    total = total + i
print(f"Sum 1-10: {total}")
```
</details>

---

## Quick Reference

### Basic For Loop

```python
# Loop over a list
for item in list:
    # code

# Loop with range
for i in range(5):      # 0, 1, 2, 3, 4
for i in range(1, 6):  # 1, 2, 3, 4, 5
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
```

### range() Function

| Syntax | Produces |
|--------|----------|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(2, 5)` | 2, 3, 4 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 |
| `range(5, 0, -1)` | 5, 4, 3, 2, 1 |

### Common Patterns

| Pattern | Code |
|---------|------|
| Sum items | `total = 0`<br>`for x in items: total += x` |
| Count matches | `count = 0`<br>`for x in items:`<br>`  if condition: count += 1` |
| Find maximum | `max_val = items[0]`<br>`for x in items[1:]:`<br>`  if x > max_val: max_val = x` |
| Build new list | `new = []`<br>`for x in old: new.append(transform(x))` |

---

## Key Takeaways

1. **For loops** repeat code for each item in a sequence
2. **`range(n)`** generates numbers from 0 to n-1
3. **`range(start, end)`** generates numbers from start to end-1
4. **`enumerate()`** gives you both index and value
5. **Don't modify a list** while looping over it
6. **Don't forget the colon** `:` at the end of the for line
7. **Indentation matters**—the indented code runs each iteration

---

## What's Next?

Now that you know for loops:
- You'll learn about while loops (loops that run while a condition is true)
- You'll learn to control loops with `break` and `continue`
- You'll combine loops with conditionals for powerful programs
