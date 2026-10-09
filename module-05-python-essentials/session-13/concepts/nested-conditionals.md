# Nested Conditionals: Decisions Inside Decisions

## What You'll Learn
- How to put if statements inside other if statements
- When to use nested conditionals vs. logical operators
- How to avoid getting lost in "indentation hell"
- Common patterns for nested decisions
- Practical examples

---

## Main Concept: Questions Lead to More Questions

Sometimes one decision leads to another. You check one condition, and if it's true, you need to check another condition. This is called **nesting**.

**Analogy: A Choose Your Own Adventure Book**
- Turn to page 5 if you want to enter the cave
- On page 5: Turn to page 10 if you have a torch, or page 15 if you don't
- Each choice leads to more choices!

---

## Basic Nesting: If Inside If

### Simple Two-Level Nesting

```python
age = 20
has_id = True

if age >= 18:
    print("You are an adult.")
    
    if has_id:
        print("You can enter the club!")
    else:
        print("You need ID to enter.")
        
else:
    print("You are too young to enter.")
```

**What happens:**
1. Check if age >= 18 → Yes
2. Print "You are an adult"
3. Check if has_id → Yes
4. Print "You can enter the club!"

### Three Levels of Nesting

```python
temperature = 75
weather = "sunny"
is_weekend = True

if temperature > 70:
    print("It's warm outside.")
    
    if weather == "sunny":
        print("Perfect weather!")
        
        if is_weekend:
            print("Go to the beach!")
        else:
            print("Have a nice day at work.")
            
    else:
        print("Warm but cloudy.")
        
else:
    print("It's cool outside.")
```

---

## When to Use Nesting vs. Logical Operators

### Use Logical Operators for Simple AND Conditions

```python
# ✅ Good - simple condition
if age >= 18 and has_id:
    print("You can enter!")
else:
    print("Cannot enter.")
```

### Use Nesting for Different Messages

```python
# ✅ Good - different messages for different failures
if age >= 18:
    if has_id:
        print("Welcome to the club!")
    else:
        print("Sorry, you need ID to enter.")
else:
    print("Sorry, you must be 18 or older.")
    print(f"Come back in {18 - age} years!")
```

---

## Common Patterns

### Pattern 1: Check Prerequisites First

```python
# Check if user exists before checking other things
username = "alice"
password = "secret123"
account_active = True

# Simulated database
database = {
    "alice": {"password": "secret123", "active": True}
}

if username in database:
    user = database[username]
    
    if password == user["password"]:
        
        if user["active"]:
            print("Login successful!")
        else:
            print("Account is deactivated.")
            
    else:
        print("Wrong password.")
        
else:
    print("Username not found.")
```

### Pattern 2: Categorize Then Decide

```python
score = 85
attendance = 90

# First categorize by score
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D or F"

# Then check attendance
if attendance >= 90:
    attendance_bonus = "+"
else:
    attendance_bonus = ""

print(f"Final grade: {grade}{attendance_bonus}")
```

### Pattern 3: Menu System

```python
print("=== Food Ordering System ===")
print("1. Pizza")
print("2. Burger")
print("3. Salad")

choice = input("Choose (1-3): ")

if choice == "1":
    print("Pizza options:")
    print("  a. Pepperoni")
    print("  b. Cheese")
    print("  c. Veggie")
    
    topping = input("Choose topping (a-c): ")
    
    if topping == "a":
        print("You ordered pepperoni pizza!")
    elif topping == "b":
        print("You ordered cheese pizza!")
    elif topping == "c":
        print("You ordered veggie pizza!")
    else:
        print("Invalid topping choice.")
        
elif choice == "2":
    print("You ordered a burger!")
    
elif choice == "3":
    print("You ordered a salad!")
    
else:
    print("Invalid choice.")
```

---

## Avoiding "Indentation Hell"

### Too Many Levels = Hard to Read

```python
# ❌ Hard to follow (the "arrow" pattern)
if user_exists:
    if user.is_active:
        if user.has_permission:
            if user.quota > 0:
                if not user.is_banned:
                    do_something()
                else:
                    print("User is banned")
            else:
                print("No quota left")
        else:
            print("No permission")
    else:
        print("User inactive")
else:
    print("User not found")
```

### Better: Flatten with Return or Logical Operators

```python
# ✅ Better - check negatives first and return early
if not user_exists:
    print("User not found")
elif not user.is_active:
    print("User inactive")
elif not user.has_permission:
    print("No permission")
elif user.quota <= 0:
    print("No quota left")
elif user.is_banned:
    print("User is banned")
else:
    do_something()
```

---

## Common Beginner Mistakes

### Mistake 1: Wrong Indentation Level

```python
# ❌ Wrong - else doesn't match the right if
if age >= 18:
    if has_id:
        print("Can enter")
    else:  # This matches the inner if!
        print("Need ID")
else:  # This matches the outer if
    print("Too young")
```

### Mistake 2: Forgetting the Outer Condition

```python
# ❌ Wrong - this runs even if age < 18!
if age >= 18:
    print("Adult")
if has_id:  # This is NOT inside the age check!
    print("Can enter")
```

### Mistake 3: Over-Nesting Simple Logic

```python
# ❌ Overly complex
if temperature > 70:
    if weather == "sunny":
        if is_weekend:
            print("Go out!")
        else:
            print("Work day")
    else:
        print("Cloudy")
else:
    print("Cold")

# ✅ Simpler with logical operators
if temperature > 70 and weather == "sunny" and is_weekend:
    print("Go out!")
elif temperature > 70 and weather == "sunny":
    print("Work day")
elif temperature > 70:
    print("Cloudy")
else:
    print("Cold")
```

### Mistake 4: Not Handling All Cases

```python
# ❌ Missing cases
if choice == "1":
    if subchoice == "a":
        print("Option 1a")
    elif subchoice == "b":
        print("Option 1b")
    # What if subchoice is neither a nor b?
```

---

## Try It Yourself: Exercises

### Exercise 1: Club Entry System

Create a system that checks age, ID, and dress code:

```python
age = int(input("Enter your age: "))
has_id = input("Do you have ID? (yes/no): ").lower() == "yes"

if age >= 21:
    if has_id:
        dress_code = input("Are you wearing nice clothes? (yes/no): ").lower()
        if dress_code == "yes":
            print("Welcome to the VIP club!")
        else:
            print("Sorry, dress code required.")
    else:
        print("ID is required for entry.")
elif age >= 18:
    print("You can enter the regular area.")
else:
    print("You are too young to enter.")
```

### Exercise 2: Quiz Grading System

Grade a quiz based on multiple factors:

```python
score = int(input("Enter score (0-100): "))
attempts = int(input("How many attempts? "))

if score >= 70:
    if attempts == 1:
        print("Excellent! Passed on first try!")
    else:
        print(f"Passed after {attempts} attempts.")
else:
    if score >= 50:
        print("Close! Need more practice.")
    else:
        print("Failed. Please review the material.")
```

### Exercise 3: ATM Simulation

Simple ATM with balance check and withdrawal:

```python
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")

if entered_pin == pin:
    print("Access granted.")
    print(f"Your balance: ${balance}")
    
    action = input("Withdraw or Deposit? (w/d): ").lower()
    
    if action == "w":
        amount = int(input("Amount to withdraw: $"))
        if amount <= balance:
            balance = balance - amount
            print(f"Withdrew ${amount}. New balance: ${balance}")
        else:
            print("Insufficient funds!")
    elif action == "d":
        amount = int(input("Amount to deposit: $"))
        balance = balance + amount
        print(f"Deposited ${amount}. New balance: ${balance}")
    else:
        print("Invalid action.")
        
else:
    print("Incorrect PIN.")
```

### Exercise 4: Fix the Bugs

```python
# Buggy program
age = int(input("Age: "))
has_ticket = input("Has ticket? ") == "yes"

if age >= 18:
    print("Adult")
if has_ticket:
    print("Can enter")
else:
    print("Need ticket")
else:
    print("Minor")
```

<details>
<summary>Click to see the answer</summary>

```python
# Fixed program
age = int(input("Age: "))
has_ticket = input("Has ticket? ").lower() == "yes"

if age >= 18:
    print("Adult")
    if has_ticket:  # This must be INSIDE the age check
        print("Can enter")
    else:
        print("Need ticket")
else:
    print("Minor")
```
</details>

---

## Quick Reference

### Nesting Structure

```python
if condition1:
    # Code for condition1
    if condition2:
        # Code for both conditions
    else:
        # Condition1 true, condition2 false
else:
    # Condition1 false
```

### When to Use What

| Situation | Use |
|-----------|-----|
| Simple AND check | `if a and b:` |
| Different messages per check | Nested ifs |
| Multiple independent checks | Separate ifs (not nested) |
| Complex decision tree | Nested ifs with elif |

### Indentation Levels

```python
# Level 1: Outer if
if age >= 18:
    # Level 2: Inside first if
    if has_id:
        # Level 3: Inside second if
        print("Enter")
    else:
        # Level 3: Inside second if's else
        print("Need ID")
else:
    # Level 2: Inside first if's else
    print("Too young")
```

---

## Key Takeaways

1. **Nesting** means putting if statements inside other if statements
2. **Use nesting** when you need different messages for different checks
3. **Use logical operators** (`and`, `or`) for simple combined conditions
4. **Avoid too many levels**—it gets hard to read and debug
5. **Indentation is crucial**—it shows which code belongs to which if
6. **Flatten when possible**—check negative cases first and use `elif`

---

## What's Next?

Now that you understand nested conditionals:
- You'll learn about loops (repeating code)
- You'll combine conditionals with loops
- You'll write more interactive programs
