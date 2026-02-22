# Control Structures: Directing Program Flow

## What Are Control Structures?

Control structures determine the order in which statements are executed in a program. They allow programs to make decisions, repeat actions, and respond to different conditions.

## The Three Fundamental Control Structures

### 1. Sequence
**Definition**: Execute statements in order, one after another.

**Flowchart Symbol**: Rectangle

**Pseudocode:**
```
statement1
statement2
statement3
```

**Real Code Examples:**
```python
# Python
name = "Alice"
greeting = "Hello, " + name
print(greeting)

# JavaScript
let name = "Alice";
let greeting = "Hello, " + name;
console.log(greeting);

# Java
String name = "Alice";
String greeting = "Hello, " + name;
System.out.println(greeting);
```

### 2. Selection (Decision Making)
**Definition**: Choose between different paths based on conditions.

**Flowchart Symbol**: Diamond

#### Simple IF
```
IF condition THEN
    statements
END IF
```

```python
# Check if number is positive
if number > 0:
    print("Number is positive")
```

#### IF-ELSE
```
IF condition THEN
    true_statements
ELSE
    false_statements
END IF
```

```python
# Check pass/fail
if score >= 60:
    print("Pass")
else:
    print("Fail")
```

#### Multiple Selection (IF-ELSEIF)
```
IF condition1 THEN
    statements1
ELSE IF condition2 THEN
    statements2
ELSE
    default_statements
END IF
```

```python
# Grade calculator
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

#### Nested IF Statements
```
IF outer_condition THEN
    IF inner_condition THEN
        statements
    END IF
END IF
```

```python
# Complex condition
if age >= 18:
    if has_license:
        print("Can drive")
    else:
        print("Needs license")
else:
    print("Too young")
```

### 3. Iteration (Looping)
**Definition**: Repeat statements multiple times.

**Flowchart Symbol**: Rectangle with curved bottom

#### Pre-test Loop (WHILE)
```
WHILE condition DO
    statements
END WHILE
```

```python
# Count to 5
count = 1
while count <= 5:
    print(count)
    count += 1
```

#### Post-test Loop (DO-WHILE/REPEAT-UNTIL)
```
REPEAT
    statements
UNTIL condition
```

```python
# Python implementation (using while True)
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break
    print(f"You entered: {user_input}")
```

#### Counted Loop (FOR)
```
FOR counter FROM start TO end DO
    statements
END FOR
```

```python
# Loop 5 times
for i in range(1, 6):
    print(i)

# Loop through collection
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

## Advanced Control Structures

### Loop Control Statements

#### BREAK
Exit loop immediately:
```python
# Find first even number
numbers = [1, 3, 5, 6, 8, 9]
for num in numbers:
    if num % 2 == 0:
        print(f"First even: {num}")
        break
```

#### CONTINUE
Skip to next iteration:
```python
# Print odd numbers only
for num in range(10):
    if num % 2 == 0:
        continue
    print(num)
```

#### ELSE in Loops
Execute when loop completes normally:
```python
# Search with result indication
def find_item(items, target):
    for item in items:
        if item == target:
            print(f"Found {target}")
            break
    else:
        print(f"{target} not found")
```

### Switch/Case (in some languages)
Multiple selection based on value:
```javascript
// JavaScript
switch (grade) {
    case 'A':
        console.log("Excellent");
        break;
    case 'B':
        console.log("Good");
        break;
    case 'C':
        console.log("Average");
        break;
    default:
        console.log("Needs improvement");
}
```

## Control Structure Patterns

### Input Validation Loop
```python
# Keep asking until valid input
while True:
    try:
        age = int(input("Enter age: "))
        if age >= 0 and age <= 120:
            break
        else:
            print("Age must be between 0 and 120")
    except ValueError:
        print("Please enter a valid number")

print(f"Valid age: {age}")
```

### Menu System
```python
def show_menu():
    print("1. Add item")
    print("2. Remove item")
    print("3. List items")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose option: ")

    if choice == "1":
        # Add item logic
        pass
    elif choice == "2":
        # Remove item logic
        pass
    elif choice == "3":
        # List items logic
        pass
    elif choice == "4":
        break
    else:
        print("Invalid choice")
```

### Processing Collections
```python
# Process list with different actions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    elif num % 3 == 0:
        print(f"{num} is divisible by 3")
    else:
        print(f"{num} is odd and not divisible by 3")
```

## Control Flow in Different Languages

### Python Control Structures
```python
# IF statement
if condition:
    # code
elif another_condition:
    # code
else:
    # code

# FOR loop
for item in iterable:
    # code

# WHILE loop
while condition:
    # code
```

### JavaScript Control Structures
```javascript
// IF statement
if (condition) {
    // code
} else if (another_condition) {
    // code
} else {
    // code
}

// FOR loop
for (let i = 0; i < 10; i++) {
    // code
}

// WHILE loop
while (condition) {
    // code
}
```

### Java Control Structures
```java
// IF statement
if (condition) {
    // code
} else if (another_condition) {
    // code
} else {
    // code
}

// FOR loop
for (int i = 0; i < 10; i++) {
    // code
}

// WHILE loop
while (condition) {
    // code
}
```

## Common Control Structure Mistakes

### Off-by-One Errors
```python
# Wrong: loop runs 11 times instead of 10
for i in range(11):  # 0 to 10 inclusive
    print(i)

# Correct: loop runs 10 times
for i in range(10):  # 0 to 9
    print(i)

# Or more explicitly
for i in range(1, 11):  # 1 to 10
    print(i)
```

### Infinite Loops
```python
# Infinite loop - condition never becomes false
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break  # Without this, loop never ends

# Another infinite loop
counter = 0
while counter < 10:
    print(counter)
    # Forgot to increment counter!
```

### Dangling Else Problem
```python
# Which if does the else belong to?
if condition1:
    if condition2:
        statement1
else:  # Belongs to inner if, not outer if
    statement2

# Clarify with proper indentation and braces
if condition1:
    if condition2:
        statement1
    else:
        statement2
```

### Loop Variable Scope
```python
# In some languages, loop variables are scoped to the loop
for (int i = 0; i < 10; i++) {
    // i exists only in this loop
}
// i is not accessible here
```

## Nested Control Structures

### Nested Loops
```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i * j}")
    print()  # Empty line after each row
```

### Loop with Selection
```python
# Process student grades
grades = [85, 92, 78, 96, 88]
for grade in grades:
    if grade >= 90:
        print(f"{grade}: A")
    elif grade >= 80:
        print(f"{grade}: B")
    elif grade >= 70:
        print(f"{grade}: C")
    else:
        print(f"{grade}: F")
```

### Selection with Loops
```python
# Different processing based on user choice
choice = input("Choose: (1) Sum (2) Product: ")

if choice == "1":
    total = 0
    for num in numbers:
        total += num
    print(f"Sum: {total}")
elif choice == "2":
    product = 1
    for num in numbers:
        product *= num
    print(f"Product: {product}")
```

## Control Structure Best Practices

### Readability
- Use clear, descriptive variable names
- Add comments for complex conditions
- Consistent indentation
- Avoid deeply nested structures

### Maintainability
- Single responsibility principle
- Extract complex conditions to functions
- Use early returns to reduce nesting
- Limit loop depth to 2-3 levels

### Performance
- Avoid unnecessary work in loops
- Use appropriate loop types
- Consider loop unrolling for performance-critical code
- Break early when possible

### Error Handling
- Validate inputs before processing
- Handle edge cases in conditions
- Use try-catch for unexpected errors
- Provide meaningful error messages

## Key Takeaways

1. **Three fundamental structures**: Sequence, selection, and iteration cover all programming needs
2. **Selection controls decisions**: IF-ELSE structures handle different conditions
3. **Iteration enables repetition**: Loops process collections and repeat actions
4. **Control flow directs execution**: Programs can adapt to different situations
5. **Proper structure improves code**: Readable, maintainable, and correct programs

## Further Reading
- Study structured programming principles
- Learn about different control structures in various languages
- Explore advanced control flow patterns
- Understand control flow graphs and program analysis