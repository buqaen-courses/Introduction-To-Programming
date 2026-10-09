# Session 10 Workshop: First Steps with Python

## Workshop Overview

Today we take our first steps writing and running Python code! We'll explore the REPL, create scripts, and connect our algorithmic thinking to actual Python syntax.

## Activity 1: Python REPL Exploration (15 minutes)

**Objective**: Get comfortable with the Python interactive environment

**Instructions**:
1. Open Python REPL (`python` in terminal or IDLE)
2. Try these expressions one by one:
```python
2 + 3
"Hello" + " World"
print("Welcome to programming!")
len("Python")
type(42)
type("hello")
```

**Experiment**:
- What happens with `2 + "hello"`?
- Try `print("Your name")` without quotes
- What does `5 * "ha"` produce?

**Questions to discuss**:
- What's the difference between an expression and a statement?
- Why does Python sometimes show quotes around output?

## Activity 2: Hello World Script (10 minutes)

**Objective**: Create and run your first Python script

**Instructions**:
1. Create a new file called `hello.py`
2. Add this code:
```python
print("Hello, World!")
print("Welcome to Python programming!")
print("Today is a great day to start coding!")
```

3. Save the file
4. Run it with `python hello.py` (or F5 in IDLE)

**Variations to try**:
- Add your name to the output
- Print the current date/time (we'll learn this later)
- Add comments explaining what each line does

## Activity 3: Interactive Greeting Program (15 minutes)

**Objective**: Combine input and output for interaction

**Instructions**:
Create a program that:
1. Asks for the user's name
2. Greets them personally
3. Asks for their favorite programming language (or "none yet")
4. Responds appropriately

**Sample code structure**:
```python
# Get user's name
name = input("What's your name? ")

# Greet them
print("Hello, " + name + "!")

# Ask about programming experience
language = input("What's your favorite programming language? ")

# Respond
if language.lower() == "python":
    print("Great choice! Python is awesome!")
elif language.lower() == "none" or language == "":
    print("That's okay! You're about to learn Python!")
else:
    print(language + " is cool too, but Python is pretty great!")
```

**Extension**: Add more personalized responses based on the language they mention.

## Activity 4: Pseudocode to Python Translation (15 minutes)

**Objective**: Convert algorithmic thinking to Python code

**Given pseudocode**:
```
DISPLAY "Calculator Program"
GET first_number FROM user
GET second_number FROM user
DISPLAY "Sum:" + (first_number + second_number)
DISPLAY "Difference:" + (first_number - second_number)
DISPLAY "Product:" + (first_number * second_number)
IF second_number != 0 THEN
    DISPLAY "Quotient:" + (first_number / second_number)
ELSE
    DISPLAY "Cannot divide by zero"
END IF
```

**Task**: Convert this to working Python code

**Hints**:
- Use `input()` for getting numbers
- Convert strings to numbers with `int()` or `float()`
- Use `if` for the division check
- Test with different number combinations

## Activity 5: Bug Hunt (10 minutes)

**Objective**: Practice debugging simple errors

**Instructions**:
Here are some broken code snippets. Find and fix the errors:

1. `print("Hello World")` - Missing something?
2. `Print("hello")` - Case sensitivity issue
3. `print("hello"` - Missing parenthesis
4. `name = input("Name: ") print(name)` - Missing line break
5. `print("Sum: " + 5 + 10)` - Type mismatch

**Discussion**: What error messages did you see? What do they tell you?

## Workshop Files

- `hello.py` - Starter hello world script
- `calculator.py` - Template for calculator activity
- `greeting.py` - Interactive greeting template
- `debugging-examples.py` - Code snippets with intentional errors

## Reflection

**What we learned today**:
- ✅ How to use the Python REPL
- ✅ Creating and running Python scripts
- ✅ Basic input/output operations
- ✅ Converting pseudocode to Python
- ✅ Common beginner errors and how to fix them

**Questions for next time**:
- How do we store values for later use?
- What other data types does Python have?
- How do we make decisions in code?