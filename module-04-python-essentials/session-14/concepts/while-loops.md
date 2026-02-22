# While Loops: Repeat While a Condition is True

## What You'll Learn
- How to use while loops for unknown repetition
- The difference between for and while loops
- Common while loop patterns
- How to avoid infinite loops
- Input validation with while loops

---

## Main Concept: Keep Going While...

A **while loop** keeps repeating code as long as a condition stays `True`. Unlike for loops that go through a list, while loops continue until something changes.

**Analogy: Washing Your Hands**
- While hands are dirty: keep washing
- When hands are clean: stop
- You don't know how many washes it will take!

---

## Basic While Loop Syntax

### Simple Counter

```python
count = 1

while count <= 5:
    print(f"Count: {count}")
    count = count + 1  # Or: count += 1

print("Done!")

# Output:
# Count: 1
# Count: 2
# Count: 3
# Count: 4
# Count: 5
# Done!
```

**How it works:**
1. Check if `count <= 5` → True (1 <= 5)
2. Run the indented code
3. Increase count by 1
4. Check again → True (2 <= 5)
5. Repeat until count becomes 6
6. 6 <= 5 is False, so the loop ends

### Boolean Condition

```python
keep_going = True

while keep_going:
    answer = input("Continue? (yes/no): ").lower()
    
    if answer == "no":
        keep_going = False
    else:
        print("Continuing...")

print("Goodbye!")
```

---

## Common While Loop Patterns

### Pattern 1: Input Validation

Get valid input from the user:

```python
# Keep asking until user enters a positive number
number = 0  # Start with invalid value

while number <= 0:
    try:
        number = float(input("Enter a positive number: "))
        if number <= 0:
            print("That wasn't positive! Try again.")
    except ValueError:
        print("That's not a number! Try again.")
        number = 0  # Reset to keep looping

print(f"Thank you! You entered: {number}")
```

### Pattern 2: Sentinel Value (Special Stop Value)

```python
# Keep reading numbers until user enters 0
total = 0

print("Enter numbers to sum (enter 0 to stop):")

while True:
    num = int(input("Number: "))
    
    if num == 0:
        break  # Exit the loop
    
    total = total + num
    print(f"Added. Current total: {total}")

print(f"Final total: {total}")
```

### Pattern 3: Menu System

```python
def show_menu():
    print("\n=== Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Choose (1-5): ")
    
    if choice == "5":
        print("Goodbye!")
        break
    
    if choice in ["1", "2", "3", "4"]:
        try:
            a = float(input("First number: "))
            b = float(input("Second number: "))
            
            if choice == "1":
                print(f"Result: {a + b}")
            elif choice == "2":
                print(f"Result: {a - b}")
            elif choice == "3":
                print(f"Result: {a * b}")
            elif choice == "4":
                if b != 0:
                    print(f"Result: {a / b}")
                else:
                    print("Cannot divide by zero!")
        except ValueError:
            print("Invalid number!")
    else:
        print("Invalid choice!")
```

---

## Infinite Loops and How to Avoid Them

### The Accidental Infinite Loop

```python
# ❌ WRONG - This runs forever!
count = 1

while count <= 5:
    print(count)
    # Forgot to increase count!

# Output: 1, 1, 1, 1, 1... forever
```

### How to Fix It

```python
# ✅ CORRECT - This stops properly
count = 1

while count <= 5:
    print(count)
    count += 1  # Don't forget this!
```

### Intentional Infinite Loop with Break

```python
# Sometimes infinite loops are useful
while True:
    command = input("Enter command (quit to exit): ")
    
    if command.lower() == "quit":
        print("Thanks for playing!")
        break  # Exit the loop
    
    print(f"Executing: {command}")
```

---

## For Loops vs While Loops

### Use For Loops When You Know the Count

```python
# ✅ Good - we know exactly 10 iterations
for i in range(10):
    print(f"Item {i}")

# ✅ Good - we have a list to process
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)
```

### Use While Loops When You Don't Know the Count

```python
# ✅ Good - we don't know how many tries
password = ""
while password != "secret":
    password = input("Enter password: ")

# ✅ Good - depends on user input
lines = []
line = input("Enter line (blank to finish): ")
while line != "":
    lines.append(line)
    line = input("Enter line (blank to finish): ")
```

---

## Common Beginner Mistakes

### Mistake 1: Forgetting to Update the Condition Variable

```python
# ❌ Wrong - infinite loop
count = 1
while count <= 5:
    print(count)
    # Forgot count += 1!

# ✅ Correct
count = 1
while count <= 5:
    print(count)
    count += 1
```

### Mistake 2: Wrong Comparison Direction

```python
# ❌ Wrong - never enters loop
num = 10
while num > 20:  # 10 > 20 is False immediately!
    print(num)
    num += 1

# ✅ Correct
num = 10
while num < 20:  # 10 < 20 is True
    print(num)
    num += 1
```

### Mistake 3: Off-by-One Errors

```python
# ❌ Wrong - prints 1 to 11 (11 times, not 10)
count = 1
while count <= 10:
    print(count)
count += 1  # This is OUTSIDE the loop!

# ✅ Correct - indent properly
count = 1
while count <= 10:
    print(count)
    count += 1  # This is inside the loop
```

### Mistake 4: Not Initializing the Variable

```python
# ❌ Wrong - what is count?
while count <= 5:  # NameError!
    print(count)
    count += 1

# ✅ Correct - initialize first
count = 1
while count <= 5:
    print(count)
    count += 1
```

---

## Try It Yourself: Exercises

### Exercise 1: Number Guessing Game

Keep guessing until correct:

```python
import random

secret = random.randint(1, 100)
guesses = 0

guess = 0  # Initialize with impossible value

while guess != secret:
    guess = int(input("Guess (1-100): "))
    guesses += 1
    
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")

print(f"🎉 Correct! You got it in {guesses} guesses!")
```

### Exercise 2: Password Attempts

Limit the number of tries:

```python
correct_password = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password: ")
    attempts += 1
    
    if password == correct_password:
        print("Access granted!")
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Wrong! {remaining} attempts remaining.")
        else:
            print("Account locked!")
```

### Exercise 3: Running Total with Sentinel

Add numbers until user enters -1:

```python
total = 0
count = 0

print("Enter numbers to average (enter -1 to finish):")

number = 0
while number != -1:
    number = float(input("Number: "))
    
    if number != -1:
        total += number
        count += 1

if count > 0:
    average = total / count
    print(f"You entered {count} numbers.")
    print(f"Sum: {total}")
    print(f"Average: {average:.2f}")
else:
    print("No numbers were entered.")
```

### Exercise 4: Fix the Bugs

```python
# Buggy program
count = 1
while count < 5
    print(count)
count += 1

password = ""
while password == "secret"
    password = input("Password: ")
print("Access granted")
```

<details>
<summary>Click to see the answer</summary>

```python
# Fixed program
count = 1
while count <= 5:  # Added colon
    print(count)
    count += 1  # Indent to be inside loop

password = ""
while password != "secret":  # Need : and != (not ==)
    password = input("Password: ")
print("Access granted")
```
</details>

---

## Quick Reference

### Basic While Loop

```python
while condition:
    # code to repeat
    # update condition variable
```

### Common Patterns

| Pattern | Code |
|---------|------|
| Input validation | `while not valid:`<br>`  get_input()`<br>`  validate()` |
| Menu loop | `while True:`<br>`  show_menu()`<br>`  if quit: break` |
| Count up | `count = 0`<br>`while count < max:`<br>`  do_something()`<br>`  count += 1` |
| Sentinel value | `while True:`<br>`  value = input()`<br>`  if value == sentinel: break` |

### For vs While

| Use | Loop Type |
|-----|-----------|
| Known number of iterations | `for` |
| Process a list/collection | `for` |
| Unknown iterations | `while` |
| Waiting for condition | `while` |
| User input until valid | `while` |

### Avoiding Infinite Loops

| Check | Example |
|-------|---------|
| Initialize variable | `count = 0` before `while count < 10` |
| Update in loop | `count += 1` inside the loop |
| Condition can become False | Make sure count will eventually reach 10 |
| Use break for intentional exit | `if done: break` |

---

## Key Takeaways

1. **While loops** run while a condition is `True`
2. **For loops** are for known iterations; **while loops** are for unknown
3. **Don't forget to update** your condition variable inside the loop
4. **Infinite loops** happen when the condition never becomes `False`
5. **Use `break`** to exit a loop early
6. **Input validation** is a classic use case for while loops
7. **Always initialize** variables before the while loop

---

## What's Next?

Now that you know both for and while loops:
- You'll learn about `break` and `continue` for fine-tuning loops
- You'll learn about `else` with loops
- You'll write more complex interactive programs
