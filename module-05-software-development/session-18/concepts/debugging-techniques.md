# Debugging: Finding and Fixing Bugs

## Introduction: What is Debugging?

Debugging is the process of finding and fixing errors (bugs) in your programs. Think of it like being a detective: something went wrong, and you need to investigate to find out why.

### Why Do We Call It "Debugging"?

The term originated from an actual bug! In 1947, Grace Hopper found a moth stuck in a computer relay, causing it to malfunction. She taped the moth in the logbook with the note: "First actual case of bug being found."

### Types of Errors

| Type | Description | Example |
|------|-------------|---------|
| **Syntax Error** | Code breaks Python's grammar rules | `print("Hello` (missing quote) |
| **Runtime Error** | Code runs but crashes during execution | `10 / 0` (division by zero) |
| **Logic Error** | Code runs but produces wrong results | Adding instead of subtracting |

### The Debugging Mindset

**Don't panic!** Everyone has bugs. Even experienced programmers spend time debugging.

**The Scientific Method of Debugging**:
1. **Observe** - What is happening?
2. **Hypothesize** - What might be causing it?
3. **Test** - Try to prove or disprove your hypothesis
4. **Fix** - Correct the problem
5. **Verify** - Make sure it's actually fixed

---

## Technique 1: Print Debugging

The simplest and most common debugging technique: add `print()` statements to see what's happening inside your code.

### Basic Print Debugging

```python
def calculate_average(numbers):
    """Calculate average with debugging."""
    print(f"DEBUG: Input received: {numbers}")
    print(f"DEBUG: Number of items: {len(numbers)}")

    if not numbers:
        print("DEBUG: Empty list! Returning 0")
        return 0

    total = 0
    for i, num in enumerate(numbers):
        print(f"DEBUG: Adding item {i}: {num}")
        total += num
        print(f"DEBUG: Running total is now: {total}")

    average = total / len(numbers)
    print(f"DEBUG: Final average: {average}")
    return average

# Run it
result = calculate_average([10, 20, 30])
print(f"Result: {result}")

# Output:
# DEBUG: Input received: [10, 20, 30]
# DEBUG: Number of items: 3
# DEBUG: Adding item 0: 10
# DEBUG: Running total is now: 10
# DEBUG: Adding item 1: 20
# DEBUG: Running total is now: 30
# DEBUG: Adding item 2: 30
# DEBUG: Running total is now: 60
# DEBUG: Final average: 20.0
# Result: 20.0
```

### Smart Print Debugging

**Show variable types**:
```python
def process_data(data):
    print(f"DEBUG: data = {data}")
    print(f"DEBUG: type(data) = {type(data)}")
    print(f"DEBUG: len(data) = {len(data) if hasattr(data, '__len__') else 'N/A'}")
    # ... rest of function
```

**Show function entry and exit**:
```python
def complex_function(a, b, c):
    print(f"\n=== ENTER complex_function ===")
    print(f"Parameters: a={a}, b={b}, c={c}")

    result = a + b * c

    print(f"=== EXIT complex_function ===")
    print(f"Returning: {result}\n")
    return result
```

**Show conditional branches**:
```python
def grade_score(score):
    print(f"DEBUG: score = {score}")

    if score >= 90:
        print("DEBUG: Branch: score >= 90")
        return "A"
    elif score >= 80:
        print("DEBUG: Branch: score >= 80")
        return "B"
    elif score >= 70:
        print("DEBUG: Branch: score >= 70")
        return "C"
    else:
        print("DEBUG: Branch: else (below 70)")
        return "F"
```

### When to Use Print Debugging

**✅ Good for**:
- Quick checks
- Understanding code flow
- Seeing variable values at specific points
- Simple programs

**❌ Limitations**:
- Must remove before production
- Can clutter output
- Hard to turn on/off
- Doesn't pause execution

---

## Technique 2: Assertions (Built-in Checks)

Assertions are like "sanity checks" that stop your program if something is clearly wrong.

### Basic Assertions

```python
def divide(a, b):
    """Divide a by b with built-in checks."""
    # "I assert that b is not zero"
    assert b != 0, "Cannot divide by zero!"

    # "I assert that both a and b are numbers"
    assert isinstance(a, (int, float)), f"Expected number, got {type(a)}"
    assert isinstance(b, (int, float)), f"Expected number, got {type(b)}"

    return a / b

# Works fine
print(divide(10, 2))   # 5.0

# Fails assertion
# print(divide(10, 0))   # AssertionError: Cannot divide by zero!
# print(divide("10", 2)) # AssertionError: Expected number, got <class 'str'>
```

### Assertions in Action

```python
def get_element(items, index):
    """Get element from list with checks."""
    # Check that items is actually a list
    assert isinstance(items, list), f"Expected list, got {type(items)}"

    # Check that index is valid
    assert isinstance(index, int), f"Index must be integer, got {type(index)}"
    assert 0 <= index < len(items), f"Index {index} out of range (0-{len(items)-1})"

    return items[index]

# Good calls
print(get_element([1, 2, 3], 0))   # 1

# Bad calls (would raise AssertionError)
# get_element("hello", 0)     # Not a list
# get_element([1, 2, 3], 5)   # Index out of range
# get_element([1, 2, 3], -1)  # Negative index
```

### When to Use Assertions

**Use assertions for**:
- Internal consistency checks
- Catching programming errors early
- Documenting assumptions in your code

**Don't use assertions for**:
- Validating user input (use proper error handling)
- Checking for external errors (file not found, network down)
- Things that might happen during normal use

### Important Note About Assertions

Assertions can be disabled when Python runs with optimizations (`python -O`). So never use assertions for critical safety checks!

---

## Technique 3: Logging (The Professional Way)

Logging is like print debugging, but better organized and can be turned on/off.

### Setting Up Logging

```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,     # Show all messages of this level and above
    format='%(asctime)s - %(levelname)s - %(message)s'
)
# Output looks like:
# 2024-01-15 10:30:00 - INFO - Starting up

# Different log levels (from most to least important)
logging.critical("Critical error! System may crash!")
logging.error("Error occurred, but system can continue")
logging.warning("Something unexpected happened, but not serious")
logging.info("General information about program operation")
logging.debug("Detailed information for debugging")
```

### Logging in Practice

```python
import logging

# Setup
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

def process_order(order):
    """Process an order with logging."""
    logging.info(f"Processing order for {order['customer']}")

    # Validate
    if not order.get('items'):
        logging.warning("Order has no items!")
        return False

    # Calculate total
    total = 0
    for i, item in enumerate(order['items']):
        logging.debug(f"Item {i}: {item['name']} - ${item['price']}")
        total += item['price']

    logging.info(f"Order total: ${total}")

    # Simulate saving
    try:
        save_to_database(order)
        logging.info("Order saved successfully")
        return True
    except Exception as e:
        logging.error(f"Failed to save order: {e}")
        return False

def save_to_database(order):
    """Placeholder for database save."""
    # Simulating a potential error
    if order['total'] > 10000:
        raise ValueError("Amount exceeds limit")

# Example usage
order = {
    "customer": "Alice",
    "items": [
        {"name": "T-Shirt", "price": 25.00},
        {"name": "Jeans", "price": 50.00}
    ],
    "total": 75.00
}

process_order(order)
```

### Log Level Guide

| Level | When to Use | Example |
|-------|-------------|---------|
| **CRITICAL** | Program might crash | Database connection lost |
| **ERROR** | Something went wrong | File failed to save |
| **WARNING** | Unexpected but OK | User entered weird input |
| **INFO** | Normal operation | Starting server, request received |
| **DEBUG** | Development details | Variable values, code flow |

---

## Technique 4: The Interactive Debugger (pdb)

Python has a built-in debugger that lets you pause your program and inspect it interactively.

### Getting Started with pdb

```python
def calculate_something(x, y, z):
    """Function with a bug we want to investigate."""
    step1 = x + y
    step2 = step1 * z
    step3 = step2 / (x + y)  # This might be problematic!
    return step3

# Method 1: Insert this line where you want to pause
import pdb; pdb.set_trace()

result = calculate_something(2, 3, 4)
print(f"Result: {result}")
```

When the code hits `pdb.set_trace()`, you'll see:
```
> /path/to/file.py(10)calculate_something()
-> step1 = x + y
(Pdb)
```

### Essential pdb Commands

| Command | Shortcut | What It Does |
|---------|----------|--------------|
| `next` | `n` | Execute current line and move to next |
| `step` | `s` | Step into a function call |
| `continue` | `c` | Continue until next breakpoint |
| `quit` | `q` | Exit debugger |
| `print x` | `p x` | Show value of variable x |
| `list` | `l` | Show surrounding code |
| `where` | `w` | Show call stack |

### pdb Session Example

```python
def debug_example():
    data = [1, 2, 3, 4, 5]
    total = 0

    import pdb; pdb.set_trace()  # Pause here

    for num in data:
        total += num

    average = total / len(data)
    return average

# When pdb starts:
# (Pdb) p data          → [1, 2, 3, 4, 5]
# (Pdb) p total         → 0
# (Pdb) n               → execute next line, enter loop
# (Pdb) p num           → 1 (first iteration)
# (Pdb) c               → continue to end
```

### Python 3.7+: The `breakpoint()` Function

Modern Python makes it even easier:

```python
def modern_debug():
    x = 10
    y = 20

    breakpoint()  # Same as pdb.set_trace()

    result = x + y
    return result
```

---

## Technique 5: Systematic Debugging Process

Don't just guess! Use a systematic approach to find bugs efficiently.

### The Debugging Algorithm

```
1. REPRODUCE the bug
   ↓ Make it happen consistently
2. ISOLATE the problem
   ↓ Find the smallest code that triggers it
3. IDENTIFY the cause
   ↓ Understand why it's happening
4. FIX the bug
   ↓ Make the change
5. VERIFY the fix
   ↓ Test that it works
6. PREVENT recurrence
   ↓ Add a test case
```

### Example: Systematic Debugging

**Step 1: Reproduce**
```python
def remove_evens(numbers):
    """Remove even numbers from list."""
    for num in numbers:
        if num % 2 == 0:
            numbers.remove(num)
    return numbers

# Bug reproduction
print(remove_evens([1, 2, 3, 4, 5]))
# Expected: [1, 3, 5]
# Actual: [1, 3, 5]  ← Hmm, looks right?

print(remove_evens([1, 2, 3, 4, 5, 6]))
# Expected: [1, 3, 5]
# Actual: [1, 3, 5, 6]  ← Wait, 6 should be gone!
```

**Step 2: Isolate with Print Debugging**
```python
def remove_evens_debug(numbers):
    """Remove even numbers with debugging."""
    print(f"Starting with: {numbers}")

    for i, num in enumerate(numbers):
        print(f"  Index {i}, value {num}")

        if num % 2 == 0:
            print(f"    Removing {num}")
            numbers.remove(num)
            print(f"    List is now: {numbers}")

    return numbers

print(remove_evens_debug([1, 2, 3, 4, 5, 6]))

# Output reveals the problem:
# Starting with: [1, 2, 3, 4, 5, 6]
#   Index 0, value 1
#   Index 1, value 2
#     Removing 2
#     List is now: [1, 3, 4, 5, 6]  ← Everything shifted!
#   Index 2, value 4  ← Skipped 3! Index 2 is now 4
#     Removing 4
#     List is now: [1, 3, 5, 6]
#   Index 3, value 6
#   ... and so on
```

**Step 3: Identify the Cause**

The problem: **Modifying a list while iterating over it!**

When we remove an element, everything shifts left, but the loop continues to the next index, skipping elements.

**Step 4: Fix the Bug**

```python
def remove_evens_fixed(numbers):
    """Remove even numbers correctly."""
    # Solution 1: Create a new list
    return [num for num in numbers if num % 2 != 0]

    # Solution 2: Iterate over a copy
    # for num in numbers[:]:  # [:] creates a copy
    #     if num % 2 == 0:
    #         numbers.remove(num)
    # return numbers
```

**Step 5: Verify with Multiple Test Cases**
```python
def test_remove_evens():
    """Test the fixed function thoroughly."""
    test_cases = [
        ([], []),                           # Empty list
        ([1, 3, 5], [1, 3, 5]),             # No evens
        ([2, 4, 6], []),                    # All evens
        ([1, 2, 3, 4, 5, 6], [1, 3, 5]),    # Mixed
        ([2, 1, 4, 3, 6, 5], [1, 3, 5]),    # Evens first
    ]

    for input_list, expected in test_cases:
        result = remove_evens_fixed(input_list[:])  # Copy to preserve original
        status = "✓" if result == expected else "✗"
        print(f"{status} {input_list} → {result}")

test_remove_evens()
```

---

## Technique 6: Rubber Duck Debugging

One of the most powerful techniques doesn't involve any tools!

### How It Works

1. Find a rubber duck (or any object, or a friend)
2. Explain your code to it, line by line
3. As you explain, you'll often spot the problem

### Example

```python
def find_max(numbers):
    """Find maximum number in list."""
    max_num = 0  # Bug: Should use numbers[0] or -infinity

    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num
```

**Explanation to Rubber Duck**:

"Okay duck, I'm finding the maximum number. First I set `max_num` to 0. Then I go through each number in the list... wait, what if all numbers are negative? Then `max_num` would stay 0, which isn't even in the list!"

**Fixed version**:
```python
def find_max_fixed(numbers):
    """Find maximum number in list."""
    if not numbers:
        return None

    max_num = numbers[0]  # Start with first number

    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num
```

---

## Technique 7: Binary Search Debugging

When you have a lot of code and don't know where the bug is, use binary search:

### The Concept

1. Comment out half your code
2. Run the remaining half
3. If bug still exists → bug is in this half
4. If bug gone → bug is in commented half
5. Repeat on the problematic half

### Example

```python
# Original problematic code:
def complex_function():
    step1()
    step2()  # Maybe bug here?
    step3()
    step4()  # Or here?
    step5()
    step6()  # Or here?
    step7()

# Binary search approach:
def debug_step1():
    step1()
    step2()
    step3()
    # Comment out rest
    # step4()
    # step5()
    # step6()
    # step7()

# Test... still has bug? Then bug is in steps 1-3
# If bug gone, uncomment half the remaining:
def debug_step2():
    # step1()
    # step2()
    # step3()
    step4()
    step5()  # Test first half of remaining
    # step6()
    # step7()
```

**This is especially useful for finding which code change introduced a bug.**

---

## Common Beginner Mistakes

### Mistake 1: Assuming the Bug is "Impossible"

```python
# "This can't possibly be wrong"
def calculate_total(items):
    total = 0
    for item in items:
        total += item['price']
    # ... more code ...
    # ... more code ...
    return total + tax  # Where did 'tax' come from?
```

**The computer is always right. If something is wrong, it's in your code.**

### Mistake 2: Changing Multiple Things at Once

```python
# Don't fix multiple things simultaneously
# You won't know which change fixed the bug!

# BAD: Changed 5 things at once
# GOOD: Change one thing, test, then change next
```

### Mistake 3: Not Checking Assumptions

```python
def calculate_discount(price, percent):
    # Assumption: percent is 0-100
    # But what if it's not?
    return price * (percent / 100)

# Test edge cases!
calculate_discount(100, 50)    # 50 ✓
calculate_discount(100, 0)       # 0 ✓
calculate_discount(100, 100)   # 100 ✓
calculate_discount(100, -10)   # -10 ???
calculate_discount(100, 150)   # 150 ???
```

### Mistake 4: Ignoring Error Messages

Error messages tell you exactly what's wrong! Read them carefully.

```python
# Error: "TypeError: unsupported operand type(s) for +: 'int' and 'str'"
# Translation: You tried to add a number and text

# Error: "IndexError: list index out of range"
# Translation: You asked for item 5 in a 3-item list

# Error: "KeyError: 'username'"
# Translation: You tried to access a dictionary key that doesn't exist
```

### Mistake 5: Not Simplifying Test Cases

```python
# BAD: Testing with complex real data
# GOOD: Create minimal example that shows the bug

# Instead of:
process_user_data(load_from_database(query=complex_query))

# Try:
process_user_data({"name": "Test"})  # Simplest possible input
```

---

## Practice Exercises

### Exercise 1: Find the Bug

This code has a bug. Use print debugging to find and fix it:

```python
def count_vowels(text):
    """Count vowels in text."""
    vowels = "aeiou"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Test
print(count_vowels("Hello World"))  # Should be 3, but what if it's not?
print(count_vowels("AEIOU"))        # Should be 5, but might be 0!
```

### Exercise 2: Add Assertions

Add appropriate assertions to this function:

```python
def calculate_circle_area(radius):
    """Calculate area of circle."""
    import math
    # Add assertions here
    return math.pi * radius * radius
```

### Exercise 3: Rubber Duck Debug

Explain this code to an imaginary rubber duck. Can you spot the bug?

```python
def find_average(numbers):
    total = 0
    for num in numbers:
        total = num  # Wait, what?
    return total / len(numbers)
```

### Exercise 4: Systematic Debugging

Use the systematic approach to fix this function:

```python
def get_unique_elements(items):
    """Return list with duplicates removed."""
    unique = []
    for item in items:
        if item not in items:  # Bug here
            unique.append(item)
    return unique

# Test
print(get_unique_elements([1, 2, 2, 3, 3, 3]))  # Should be [1, 2, 3]
```

---

## Key Takeaways

1. **Everyone has bugs** - It's normal, not a sign of bad programming
2. **Systematic approach beats guessing** - Follow the debugging algorithm
3. **Start simple** - Use print statements before advanced tools
4. **Assertions catch errors early** - Add sanity checks to your code
5. **Logging is print debugging for grown-ups** - Use it in real applications
6. **Explain your code** - Rubber duck debugging often reveals the issue
7. **Test thoroughly** - One fix might break something else

## Quick Reference Card

| Technique | When to Use | Pros | Cons |
|-----------|-------------|------|------|
| **Print** | Quick checks | Simple, fast | Must remove later |
| **Assertions** | Sanity checks | Self-documenting | Can be disabled |
| **Logging** | Real applications | Persistent, configurable | Slightly complex |
| **pdb** | Complex bugs | Interactive inspection | Learning curve |
| **Rubber Duck** | Logic errors | No tools needed | Requires explaining |
| **Binary Search** | Unknown location | Fast isolation | Time-consuming |

## Debugging Checklist

- [ ] Can I reproduce the bug consistently?
- [ ] Have I checked the error message carefully?
- [ ] Did I simplify the test case to the minimum?
- [ ] Have I added print/logging to understand the flow?
- [ ] Did I check my assumptions about the data?
- [ ] Have I explained the code line by line (rubber duck)?
- [ ] Did I test my fix with multiple cases?

---

## Further Reading

- **Next Lesson**: Common Errors (Session 18) - Learn about specific error types
- **Practice**: Debug 5 of your old programs
- **Tool**: Try IDE debuggers (PyCharm, VS Code have great ones)
- **Challenge**: Set up a logging system for a project
