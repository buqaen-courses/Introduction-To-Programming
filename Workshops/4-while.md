# Python Tutorial: The `while` Loop

Welcome! This tutorial covers one of Python's most fundamental looping mechanisms – the **`while` loop**. You'll learn how to repeat code as long as a condition holds true. We'll explore:

- Basic `while` loop syntax
- Infinite loops and how to avoid them
- The `break` statement to exit early
- The `continue` statement to skip iterations
- The `else` clause with loops
- Common patterns and practical examples
- Quizzes to test your understanding

Let's dive in!

---

## 1. Introduction to Loops

Often in programming, you need to repeat a block of code multiple times. Python provides two main looping constructs:

- **`for` loops** – iterate over a sequence (list, tuple, string, etc.)
- **`while` loops** – repeat as long as a condition is `True`

A `while` loop is ideal when you don't know in advance how many iterations you need – you keep going until some condition changes.

---

## 2. Basic `while` Loop Syntax

```python
while condition:
    # code block to repeat
    # update something that eventually makes condition False
```

- The `condition` is a Boolean expression (or any value that can be treated as Boolean).
- The indented block executes repeatedly **while** the condition is `True`.
- It's crucial that something inside the loop eventually makes the condition `False`; otherwise, you get an **infinite loop**.

### Example 1: Count from 1 to 5

```python
count = 1
while count <= 5:
    print(count)
    count = count + 1   # increment
```

Output:
```
1
2
3
4
5
```

### Example 2: Sum of numbers until user stops

```python
total = 0
num = float(input("Enter a number (0 to stop): "))
while num != 0:
    total += num
    num = float(input("Enter a number (0 to stop): "))
print(f"Total = {total}")
```

---

## 3. Infinite Loops and How to Avoid Them

An **infinite loop** occurs when the condition never becomes `False`. This can crash your program or make it unresponsive.

### Example of an infinite loop (don't run!):
```python
# BAD: x never changes
x = 5
while x > 0:
    print("Forever...")
```

To avoid infinite loops:
- Ensure the condition eventually becomes `False`.
- Update at least one variable involved in the condition inside the loop.
- Use `break` if necessary (see next section).

Sometimes infinite loops are intentional (e.g., game loops, server listeners). In those cases, you include a `break` condition inside.

### Intentional infinite loop with break:
```python
while True:
    response = input("Type 'quit' to exit: ")
    if response == 'quit':
        break
    print(f"You said: {response}")
```

---

## 4. The `break` Statement

`break` immediately exits the loop, regardless of the condition. Execution continues with the first statement after the loop.

### Example: Find first number divisible by 7

```python
num = 1
while num <= 100:
    if num % 7 == 0:
        print(f"First multiple of 7 is {num}")
        break
    num += 1
```

### Example: Menu system

```python
while True:
    print("\n1. Say Hello")
    print("2. Say Goodbye")
    print("3. Quit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        print("Hello!")
    elif choice == '2':
        print("Goodbye!")
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice")
```

---

## 5. The `continue` Statement

`continue` skips the rest of the current iteration and jumps back to the top of the loop (checking the condition again).

### Example: Print odd numbers only

```python
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print(num)
```

Output:
```
1
3
5
7
9
```

### Example: Ignore negative inputs

```python
total = 0
count = 0
while count < 5:
    num = int(input("Enter a positive number: "))
    if num <= 0:
        print("Ignored, not positive.")
        continue
    total += num
    count += 1
print(f"Sum of 5 positive numbers: {total}")
```

---

## 6. The `else` Clause with Loops

Python allows an `else` block after a loop. The `else` executes **only if the loop terminated normally** (i.e., without hitting a `break`). If the loop exits due to `break`, the `else` is skipped.

### Example: Search loop with else

```python
numbers = [2, 4, 6, 8, 10]
target = 7
i = 0

while i < len(numbers):
    if numbers[i] == target:
        print(f"Found {target} at index {i}")
        break
    i += 1
else:
    print(f"{target} not found in the list")
```

Output:
```
7 not found in the list
```

### Example: Prime number checker using else

```python
num = 17
divisor = 2

while divisor < num:
    if num % divisor == 0:
        print(f"{num} is not prime (divisible by {divisor})")
        break
    divisor += 1
else:
    print(f"{num} is prime")
```

---

## 7. Common Patterns and Examples

### Pattern 1: User Input Validation

Keep asking until the user provides valid input.

```python
age = -1
while age <= 0:
    try:
        age = int(input("Enter your age (positive number): "))
        if age <= 0:
            print("Age must be positive.")
    except ValueError:
        print("Invalid input. Please enter a number.")
print(f"Your age is {age}")
```

### Pattern 2: Countdown Timer

```python
import time
seconds = 5
while seconds > 0:
    print(f"T-minus {seconds}")
    time.sleep(1)
    seconds -= 1
print("Liftoff!")
```

### Pattern 3: Guessing Game

```python
import random
secret = random.randint(1, 100)
guess = None
attempts = 0

while guess != secret:
    guess = int(input("Guess the number (1-100): "))
    attempts += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
print(f"Correct! You guessed it in {attempts} attempts.")
```

### Pattern 4: Fibonacci Sequence

Generate Fibonacci numbers up to a limit.

```python
limit = 100
a, b = 0, 1
while a <= limit:
    print(a, end=' ')
    a, b = b, a + b
print()
```

### Pattern 5: Process a List Until Condition Met

Remove elements from a list until a certain value is found.

```python
items = [3, 7, 2, 9, 1, 8, 4]
while items and items[0] != 9:
    print(f"Removing {items.pop(0)}")
print(f"Remaining: {items}")
```

---

## 8. Nested `while` Loops

You can put one `while` loop inside another. This is useful for working with tables, matrices, or generating patterns.

### Example: Multiplication table

```python
i = 1
while i <= 5:
    j = 1
    while j <= 5:
        print(f"{i} x {j} = {i*j:2}", end="  ")
        j += 1
    print()  # new line after each row
    i += 1
```

### Example: Simple number pyramid

```python
rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1
```

---

## 9. Common Pitfalls and Tips

### Pitfall 1: Forgetting to Update the Loop Variable

```python
# Infinite loop – x never changes
x = 1
while x < 10:
    print(x)
    # forgot x += 1
```

### Pitfall 2: Off-by-One Errors

Make sure your loop runs the correct number of times. Test with boundary values.

### Pitfall 3: Using `break` When `while` Condition Would Suffice

Sometimes beginners use `while True` with a break when a proper condition would be clearer.

### Tip 1: Use `while` When Number of Iterations Is Unknown

If you know exactly how many times to loop, a `for` loop is usually better.

### Tip 2: Avoid Infinite Loops by Double-Checking Exit Conditions

Always ensure that something in the loop body can change the condition.

### Tip 3: `else` Can Make Code More Expressive

Use `else` to handle "not found" or "successful completion" cases without extra flags.

---

## 10. Comparison with `for` Loops

| Feature   | `while`                                          | `for`                                                 |
| --------- | ------------------------------------------------ | ----------------------------------------------------- |
| Use case  | When number of iterations unknown                | When iterating over a sequence or known range         |
| Condition | Loop continues while condition is `True`         | Loop runs for each item in iterable                   |
| Risk      | Infinite loop if condition never becomes `False` | Finite (unless you modify the iterable in weird ways) |
| Typical   | User input, game loops, until a flag changes     | Processing lists, strings, ranges                     |

Sometimes you can choose either; clarity matters more.

---

## 11. Practice Questions / Quiz

Test your understanding of `while` loops.

### Part A: Predict the Output

1. What does this code print?
   ```python
   i = 3
   while i > 0:
       print(i)
       i -= 1
   print("Done")
   ```

2. What is the output?
   ```python
   x = 5
   while x < 10:
       print(x, end=' ')
       x += 2
   ```

3. What will this print?
   ```python
   count = 0
   while count < 5:
       count += 1
       if count == 3:
           continue
       print(count)
   ```

4. What is the output?
   ```python
   n = 10
   while n > 0:
       n -= 2
       if n == 4:
           break
   print(n)
   ```

5. What does this print?
   ```python
   i = 1
   while i <= 3:
       j = 1
       while j <= i:
           print('*', end='')
           j += 1
       print()
       i += 1
   ```

### Part B: Fill in the Blanks

6. Complete the loop to print numbers from 1 to 10:
   ```python
   num = 1
   while ________:
       print(num)
       ________
   ```

7. Fill in the missing parts to keep asking until the user enters 'yes' or 'no':
   ```python
   answer = ""
   while ________:
       answer = input("Enter yes or no: ").lower()
   print(f"You entered {answer}")
   ```

8. Complete the code to sum positive numbers until a negative number is entered:
   ```python
   total = 0
   num = 0
   while ________:
       num = int(input("Enter a number (negative to stop): "))
       if num < 0:
           ________
       total += num
   print(f"Sum = {total}")
   ```

9. Add a `continue` to skip printing even numbers:
   ```python
   n = 0
   while n < 10:
       n += 1
       if ________:
           ________
       print(n)
   ```

10. Write a `while` loop that uses `else` to print "Not found" if a number 5 is not in the list `[1, 2, 3, 4]`.

### Part C: Write Code

11. Write a program that repeatedly asks the user for a number and prints its square. Stop when the user enters 0.

12. Write a program that prints all even numbers between 1 and 20 using a `while` loop.

13. Write a program that simulates a simple ATM: start with balance = 1000. Keep asking for withdraw amount; if amount <= balance, subtract and show new balance; if amount > balance, print "Insufficient funds". Stop when user enters 0.

14. Write a program that finds the largest number entered by the user. The user can enter numbers until they type 'done'.

15. Write a nested `while` loop to print a pattern:
    ```
    1
    1 2
    1 2 3
    1 2 3 4
    ```

---

## 12. Answers

### Part A
1. 
   ```
   3
   2
   1
   Done
   ```
2. `5 7 9 ` (space at end)
3. 
   ```
   1
   2
   4
   5
   ```
4. `4`
5. 
   ```
   *
   **
   ***
   ```

### Part B
6. `num <= 10` and `num += 1` (or `num = num + 1`)
7. `answer not in ('yes', 'no')` or `answer != 'yes' and answer != 'no'`
8. `True` (or `num >= 0` if you want to stop on negative), `break`
9. `n % 2 == 0` and `continue`
10. 
    ```python
    numbers = [1, 2, 3, 4]
    i = 0
    while i < len(numbers):
        if numbers[i] == 5:
            print("Found")
            break
        i += 1
    else:
        print("Not found")
    ```

### Part C (Sample Solutions)

11. 
```python
while True:
    num = float(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    print(f"Square: {num * num}")
```

12. 
```python
n = 2
while n <= 20:
    print(n)
    n += 2
```

13. 
```python
balance = 1000
while True:
    print(f"Balance: ${balance}")
    amount = float(input("Enter withdrawal amount (0 to exit): "))
    if amount == 0:
        break
    if amount <= balance:
        balance -= amount
        print(f"Withdrawn ${amount}. New balance: ${balance}")
    else:
        print("Insufficient funds")
```

14. 
```python
largest = None
while True:
    user_input = input("Enter a number (or 'done'): ")
    if user_input.lower() == 'done':
        break
    try:
        num = float(user_input)
        if largest is None or num > largest:
            largest = num
    except ValueError:
        print("Invalid input, please enter a number.")
if largest is not None:
    print(f"Largest number: {largest}")
else:
    print("No numbers entered.")
```

15. 
```python
i = 1
while i <= 4:
    j = 1
    while j <= i:
        print(j, end=' ')
        j += 1
    print()
    i += 1
```

---

Congratulations! You've mastered the `while` loop in Python. Practice by modifying the examples and writing your own programs. Loops are essential for automation and handling repetitive tasks. Next, you might explore `for` loops to see how they complement `while`. Happy coding!