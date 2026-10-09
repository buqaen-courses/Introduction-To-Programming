# Session 10 Homework: Python Environment and First Scripts

## Homework Overview

Today you set up your Python environment and wrote your first programs! This homework gives you practice with the Python REPL and basic scripting.

## Assignment 1: Environment Check (10 minutes)

**Objective**: Confirm your Python setup works correctly

**Instructions**:
1. Open your Python environment (REPL or IDLE)
2. Run these commands and record what they output:
   - `python --version` (or check version in REPL)
   - `print("Hello from Python!")`
   - `2 + 3 * 4`
   - `type("hello")`
   - `type(42)`

3. Create and run a simple script that prints your name and favorite color

**What to submit**:
- Screenshot or copy of the version check
- Screenshot or copy of the REPL outputs
- Your name-color script file

## Assignment 2: Personal Profile Script (20 minutes)

**Objective**: Create a script that introduces yourself using variables and print statements

**Requirements**:
Create a script called `profile.py` that:
- Defines variables for your name, age, favorite color, and hobby
- Prints a nice introduction using these variables
- Includes at least 3 different print statements
- Uses comments to explain what each part does

**Example output**:
```
Hello! My name is Alex.
I am 25 years old.
My favorite color is blue.
I enjoy reading and hiking.
Nice to meet you!
```

**Hints**:
- Use descriptive variable names
- Combine strings with variables using `+`
- Add comments with `#` to explain your code

## Assignment 3: Interactive Calculator (30 minutes)

**Objective**: Build a simple calculator that interacts with the user

**Requirements**:
Create a script called `simple_calculator.py` that:
1. Asks the user for two numbers
2. Asks what operation they want (+, -, *, /)
3. Performs the calculation and shows the result
4. Handles basic input validation (numbers only)

**Sample interaction**:
```
Welcome to Simple Calculator!
Enter first number: 15
Enter second number: 7
Enter operation (+, -, *, /): *
Result: 15 * 7 = 105
```

**Hints**:
- Use `input()` to get user input
- Convert strings to numbers with `int()` or `float()`
- Use `if` statements to handle different operations
- Test with different numbers and operations

## Assignment 4: Reflection and Troubleshooting (15 minutes)

**Objective**: Reflect on your first programming experience

**Instructions**:
Answer these questions in 2-3 sentences each:

1. What was the most surprising thing about writing your first Python program?
2. Did you encounter any errors? What were they and how did you fix them?
3. How does Python feel different from the pseudocode we wrote in Session 9?
4. What do you think will be the hardest part of learning Python?
5. What are you most excited to build next?

## Bonus Challenge: Temperature Converter (Optional)

Create a script that converts between Celsius and Fahrenheit:

- Ask user for temperature value and unit (C or F)
- Convert to the other unit
- Display the result

**Formula**: F = (C × 9/5) + 32, C = (F - 32) × 5/9

## Submission Guidelines

- Submit all script files (.py files)
- Include comments in your code explaining what each part does
- Test your programs with different inputs
- If something doesn't work, include a note about what you tried

## Testing Your Code

Before submitting:
- Run each script at least twice with different inputs
- Check for error messages in the console
- Make sure the output looks correct and readable

## Common Issues to Watch For

- Forgetting quotes around strings
- Not converting input strings to numbers
- Case sensitivity in operation checks
- Division by zero (if you implement division)

## Time Estimate

- Assignment 1: 10 minutes
- Assignment 2: 20 minutes
- Assignment 3: 30 minutes
- Assignment 4: 15 minutes
- **Total**: ~75 minutes

## Next Session Connection

This homework prepares you for Session 11, where we'll explore variables and data types in more depth. You'll learn about different types of values (integers, strings, booleans) and how to work with them effectively.