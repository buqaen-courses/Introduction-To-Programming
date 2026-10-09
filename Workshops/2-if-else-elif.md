# Python Tutorial: Conditional Statements (`if`/`elif`/`else`) and Logical Expressions

Welcome! This tutorial covers decision-making in Python. You'll learn how to make your programs respond differently depending on conditions. We'll explore:

- Boolean values and logical expressions
- Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- Logical operators (`and`, `or`, `not`)
- The `if` statement
- `else` and `elif` clauses
- Nested conditionals
- Many practical examples
- Quizzes to test your understanding

Let's get started!

---

## 1. Introduction to Conditional Statements

In programming, we often need to execute different code based on certain conditions. For example:

- If a user is logged in, show a welcome message; otherwise, show a login button.
- If a number is positive, print "Positive"; if negative, print "Negative".
- If a student's score is above 90, give an A; if above 80, give a B; and so on.

Python uses **`if`**, **`elif`** (else if), and **`else`** statements to handle these decisions. They rely on **Boolean expressions** – expressions that evaluate to either `True` or `False`.

---

## 2. Boolean Values and Expressions

### Boolean Values

Python has two Boolean constants: `True` and `False`. They are of type `bool`.

```python
print(True)
print(False)
print(type(True))   # <class 'bool'>
```

### Comparison Operators

Comparison operators compare two values and return a Boolean.

| Operator | Meaning                  | Example  | Result |
| -------- | ------------------------ | -------- | ------ |
| `==`     | equal to                 | `5 == 5` | `True` |
| `!=`     | not equal to             | `5 != 3` | `True` |
| `<`      | less than                | `3 < 5`  | `True` |
| `>`      | greater than             | `5 > 3`  | `True` |
| `<=`     | less than or equal to    | `5 <= 5` | `True` |
| `>=`     | greater than or equal to | `5 >= 3` | `True` |

Examples:

```python
a = 10
b = 5

print(a == b)   # False
print(a != b)   # True
print(a > b)    # True
print(a < b)    # False
print(a >= 10)  # True
print(b <= 4)   # False
```

You can also compare strings (lexicographically):

```python
print("apple" < "banana")   # True (because 'a' comes before 'b')
print("hello" == "hello")   # True
```

### Logical Operators

Logical operators combine Boolean expressions.

| Operator | Meaning                      | Example                 | Result  |
| -------- | ---------------------------- | ----------------------- | ------- |
| `and`    | True if both are true        | `(5 > 3) and (10 < 20)` | `True`  |
| `or`     | True if at least one is true | `(5 > 10) or (3 < 4)`   | `True`  |
| `not`    | Negates the Boolean          | `not (5 > 3)`           | `False` |

Examples:

```python
x = 7
print(x > 5 and x < 10)   # True (both conditions true)
print(x > 10 or x < 5)    # False (neither true)
print(not (x == 7))       # False (x==7 is True, so not True is False)
```

### Truthiness and Falsiness

In Python, every value can be treated as Boolean in a condition. Values that are considered `False` in a Boolean context are called **falsy**. All other values are **truthy**.

Common falsy values:
- `None`
- `False`
- Zero of any numeric type: `0`, `0.0`, `0j`
- Empty sequences/collections: `""` (empty string), `[]` (empty list), `()` (empty tuple), `{}` (empty dict), `set()` (empty set)

All other values are truthy (e.g., non-zero numbers, non-empty strings, non-empty lists, etc.).

Examples:

```python
if 0:
    print("This won't print")   # 0 is falsy
if 42:
    print("This will print")    # 42 is truthy
if "":
    print("Empty string is falsy")   # won't print
if "Hello":
    print("Non-empty string is truthy")   # will print
```

This is useful for checking if a list is empty, if a string has content, etc., without explicit comparisons.

---

## 3. The `if` Statement

The simplest conditional: execute a block only if a condition is true.

### Syntax

```python
if condition:
    # indented block of code
    # runs only if condition is True
```

- The condition is a Boolean expression.
- The colon `:` is required.
- The indented block must be consistent (usually 4 spaces).

### Example 1: Basic if

```python
age = 18
if age >= 18:
    print("You are an adult.")
```

### Example 2: Multiple statements in the block

```python
temperature = 25
if temperature > 20:
    print("It's warm outside.")
    print("Maybe wear a t-shirt.")
```

### Example 3: Using logical operators

```python
score = 85
if score >= 70 and score <= 100:
    print("Passing grade!")
```

---

## 4. The `else` Clause

The `else` clause catches everything that doesn't satisfy the `if` condition.

### Syntax

```python
if condition:
    # runs if condition is True
else:
    # runs if condition is False
```

### Example 1: If-else

```python
age = 16
if age >= 18:
    print("You can vote.")
else:
    print("You are too young to vote.")
```

### Example 2: Even or odd

```python
number = 7
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
```

### Example 3: Using truthiness

```python
name = input("Enter your name: ")
if name:   # true if name is not empty
    print(f"Hello, {name}!")
else:
    print("You didn't enter a name.")
```

---

## 5. The `elif` Clause

When you have multiple conditions to check, use `elif` (short for "else if").

### Syntax

```python
if condition1:
    # runs if condition1 is True
elif condition2:
    # runs if condition1 is False and condition2 is True
elif condition3:
    # runs if condition1 and condition2 are False and condition3 is True
else:
    # runs if all above conditions are False
```

- You can have any number of `elif` clauses.
- The `else` is optional.
- Only the first true condition's block executes.

### Example 1: Grading system

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is {grade}.")
```

### Example 2: Positive, negative, or zero

```python
num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

### Example 3: Simple menu

```python
print("1. Say Hello")
print("2. Say Goodbye")
print("3. Exit")

choice = input("Enter your choice: ")

if choice == "1":
    print("Hello!")
elif choice == "2":
    print("Goodbye!")
elif choice == "3":
    print("Exiting...")
else:
    print("Invalid choice.")
```

---

## 6. Nested Conditionals

You can place `if` statements inside other `if` statements. This is called **nesting**.

### Example 1: Nested if

```python
x = 10
y = 5

if x > 0:
    print("x is positive")
    if y > 0:
        print("y is also positive")
    else:
        print("y is not positive")
else:
    print("x is not positive")
```

### Example 2: Checking login

```python
username = "admin"
password = "secret"

if username == "admin":
    if password == "secret":
        print("Access granted")
    else:
        print("Wrong password")
else:
    print("Unknown user")
```

**Note:** Deep nesting can make code hard to read. Often you can simplify using logical operators (like `and`). The above could be rewritten as:

```python
if username == "admin" and password == "secret":
    print("Access granted")
elif username == "admin":
    print("Wrong password")
else:
    print("Unknown user")
```

---

## 7. Common Patterns and Tips

### Avoid Deep Nesting

Too many nested levels can be confusing. Consider refactoring using `elif` or combining conditions.

### Use `in` for Multiple Comparisons

Instead of:

```python
if color == "red" or color == "green" or color == "blue":
```

Use:

```python
if color in ("red", "green", "blue"):
```

### Short-Circuit Evaluation

Logical operators `and` and `or` evaluate from left to right and stop as soon as the result is determined.

- With `and`: if the left operand is `False`, the right is never evaluated (because the whole expression is already `False`).
- With `or`: if the left operand is `True`, the right is never evaluated.

This can prevent errors:

```python
x = 0
if x != 0 and 10 / x > 2:   # safe: x != 0 is False, so division never happens
    print("OK")
```

### Chaining Comparisons

Python allows chaining comparisons like in mathematics:

```python
if 0 < x < 10:   # equivalent to x > 0 and x < 10
    print("x is between 0 and 10")
```

### Ternary Conditional Expression (One-liner)

For simple if-else, you can use a **conditional expression**:

```python
value = x if condition else y
```

Example:

```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)   # adult
```

---

## 8. Many Examples

Let's look at a variety of examples to solidify understanding.

### Example A: Leap Year Checker

A year is a leap year if:
- It is divisible by 4, and
- If divisible by 100, it must also be divisible by 400.

```python
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
```

### Example B: Maximum of Three Numbers

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    max_num = a
elif b >= a and b >= c:
    max_num = b
else:
    max_num = c

print(f"The maximum is {max_num}.")
```

### Example C: Simple Calculator (without functions/loops)

```python
print("Simple Calculator")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operator"

print(f"Result: {result}")
```

### Example D: Age Group Classifier

```python
age = int(input("How old are you? "))

if age < 0:
    print("Invalid age.")
elif age <= 12:
    print("You are a child.")
elif age <= 19:
    print("You are a teenager.")
elif age <= 64:
    print("You are an adult.")
else:
    print("You are a senior.")
```

### Example E: Rock-Paper-Scissors Logic

Assume `player1` and `player2` are strings like `"rock"`, `"paper"`, or `"scissors"`.

```python
p1 = input("Player 1 (rock/paper/scissors): ").lower()
p2 = input("Player 2 (rock/paper/scissors): ").lower()

if p1 == p2:
    print("It's a tie!")
elif (p1 == "rock" and p2 == "scissors") or \
     (p1 == "paper" and p2 == "rock") or \
     (p1 == "scissors" and p2 == "paper"):
    print("Player 1 wins!")
else:
    print("Player 2 wins!")
```

### Example F: Simple Password Check

```python
password = input("Enter password: ")

if len(password) < 8:
    print("Password too short.")
elif password.isalpha():
    print("Password should contain numbers.")
elif password.isdigit():
    print("Password should contain letters.")
else:
    print("Password is strong enough.")
```

### Example G: Day of the Week

```python
day_num = int(input("Enter a day number (1-7): "))

if day_num == 1:
    day = "Monday"
elif day_num == 2:
    day = "Tuesday"
elif day_num == 3:
    day = "Wednesday"
elif day_num == 4:
    day = "Thursday"
elif day_num == 5:
    day = "Friday"
elif day_num == 6:
    day = "Saturday"
elif day_num == 7:
    day = "Sunday"
else:
    day = "Invalid day number"

print(day)
```

---

## 9. Quiz / Practice Questions

Test your understanding with these questions. Try to answer without running the code.

### Part A: True or False (Predict the output)

1. What is the output?
   ```python
   x = 5
   if x > 3:
       print("A")
   print("B")
   ```

2. What is the output?
   ```python
   x = 10
   if x > 15:
       print("A")
   else:
       print("B")
   print("C")
   ```

3. What is the output?
   ```python
   x = 0
   if x:
       print("A")
   else:
       print("B")
   ```

4. What is the output?
   ```python
   name = ""
   if name:
       print("Hello")
   else:
       print("Goodbye")
   ```

5. What is the output?
   ```python
   a = 5
   b = 10
   if a < b and b > 8:
       print("Yes")
   else:
       print("No")
   ```

6. What is the output?
   ```python
   score = 75
   if score >= 90:
       grade = "A"
   elif score >= 80:
       grade = "B"
   elif score >= 70:
       grade = "C"
   else:
       grade = "F"
   print(grade)
   ```

7. What is the output?
   ```python
   x = 3
   y = 5
   if x == 3:
       if y == 4:
           print("A")
       else:
           print("B")
   else:
       print("C")
   ```

8. What is the output?
   ```python
   x = 7
   if x % 2 == 0:
       print("Even")
   else:
       print("Odd")
   ```

9. What is the output?
   ```python
   a = 2
   b = 3
   c = 1
   if a > b and a > c:
       print(a)
   elif b > a and b > c:
       print(b)
   else:
       print(c)
   ```

10. What is the output?
    ```python
    x = 10
    y = 20
    z = 30
    if x < y < z:
        print("Increasing")
    else:
        print("Not increasing")
    ```

### Part B: Fill in the Blanks

11. Write an `if` statement that prints "Positive" if the variable `num` is greater than 0.
    ```python
    if ________:
        print("Positive")
    ```

12. Fill in the condition to check if a number is even.
    ```python
    if ________:
        print("Even")
    else:
        print("Odd")
    ```

13. Fill in the missing parts to print "Adult" if age is 18 or older, else "Minor".
    ```python
    if age >= 18:
        ________
    ________:
        print("Minor")
    ```

14. Use a logical operator to check if `x` is between 10 and 20 (inclusive).
    ```python
    if ________:
        print("In range")
    ```

15. Write a conditional expression (ternary) that sets `status` to "pass" if `score >= 60` else "fail".
    ```python
    status = ________
    ```

### Part C: Write Code

16. Write a program that asks the user for a number and prints whether it's positive, negative, or zero.

17. Write a program that asks the user for two numbers and prints the larger one. If they are equal, print "Equal".

18. Write a program that asks the user for a letter and prints whether it's a vowel (a, e, i, o, u) or a consonant. Assume lowercase input.

19. Write a program that asks for the current temperature in Celsius and prints:
    - "Freezing" if below 0
    - "Cold" if between 0 and 15
    - "Warm" if between 16 and 25
    - "Hot" if above 25

20. Write a program that simulates a simple login: ask for username and password. If username is "admin" and password is "1234", print "Login successful". If only username is correct, print "Wrong password". If username is wrong, print "User not found".

---

## 10. Answers to Quiz

### Part A

1. `A` (then `B` on next line)
   Output:
   ```
   A
   B
   ```

2. `B` then `C`
   Output:
   ```
   B
   C
   ```

3. `B` (since 0 is falsy)

4. `Goodbye` (empty string is falsy)

5. `Yes` (both conditions true)

6. `C` (score=75 meets the third condition)

7. `B` (x==3 true, but y==4 false, so inner else executes)

8. `Odd` (7 % 2 = 1, not 0)

9. `1` (a=2, b=3, c=1; the largest is c? Actually a=2, b=3, c=1, so largest is b=3. Wait code: if a>b and a>c: print(a); elif b>a and b>c: print(b); else: print(c). Here a>b? 2>3 false, so skip first. b>a and b>c? 3>2 true and 3>1 true, so print b: 3. So output is 3. I need to correct my mental. The code prints b=3. So answer: 3.

10. `Increasing` (10 < 20 < 30 is true)

### Part B

11. `num > 0`

12. `num % 2 == 0`

13. `print("Adult")` and `else:`

14. `x >= 10 and x <= 20` or `10 <= x <= 20`

15. `"pass" if score >= 60 else "fail"`

### Part C (Sample Solutions)

16. 
```python
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

17. 
```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print("Equal")
```

18. 
```python
letter = input("Enter a letter: ").lower()
if letter in ('a', 'e', 'i', 'o', 'u'):
    print("Vowel")
else:
    print("Consonant")
```

19. 
```python
temp = float(input("Enter temperature in Celsius: "))
if temp < 0:
    print("Freezing")
elif temp <= 15:
    print("Cold")
elif temp <= 25:
    print("Warm")
else:
    print("Hot")
```

20. 
```python
username = input("Username: ")
password = input("Password: ")
if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("User not found")
```

---

Congratulations! You've learned how to make decisions in Python. Practice by modifying the examples and writing your own programs. Conditional statements are fundamental – mastering them opens the door to more complex logic. Happy coding!