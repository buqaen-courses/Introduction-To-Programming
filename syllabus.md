## High-level course outline

This 22‑session course gently introduces complete beginners to how computers work, how data is represented, how to think algorithmically, and finally how to write, run, and debug Python programs. It emphasizes understanding concepts first (computer model, bits, algorithms), then pseudocode, and only then Python syntax and small projects, so that students learn to think like programmers, not just copy code.

- **Theme 1 – Computer & programming fundamentals**: What computers are, how they execute programs, CPU, memory, source vs machine code, compilers vs interpreters.
- **Theme 2 – Data representation & number systems**: Bits and bytes, how text and numbers are stored, binary/decimal/hex, conversions, simple binary arithmetic, ASCII vs Unicode.
- **Theme 3 – Algorithms & pseudocode**: What an algorithm is, input–process–output, designing step‑by‑step solutions, basic algorithms written in natural language and pseudocode.
- **Theme 4 – Python language fundamentals**: Python environment, REPL and scripts, variables and types, I/O, expressions and operators, conditionals, loops, strings, collections.
- **Theme 5 – Practical programming & mini‑projects**: Functions, modules, basic error handling, working with files, small end‑to‑end programs that integrate all topics.

---

## Session-by-session syllabus (22 sessions)

### Session 1: What Is a Computer? How Programs Run

**Learning objectives**

- **Describe** what a computer is and its main components (CPU, memory, storage, I/O).
- **Explain** at a high level how a program runs on a computer.
- **Distinguish** between hardware and software.
- **Identify** examples of programs in everyday life.

**Main concepts (`README.md`)**

- **Computer components**: CPU, RAM, storage, input/output devices.
- **Hardware vs software**: Operating system, applications, utilities.
- **What a program is**: Instructions for the computer.
- **From human idea to running program**: Very high‑level pipeline.

**Tutorial content summary**

- **Tour of a computer**: Diagrams/photos of CPU, RAM, disk, keyboard, monitor.
- **Everyday examples**: Phone apps, web browsers, games as “programs”.
- **Execution story**: “When you click an app, what happens?” – OS loads program, CPU executes instructions, uses RAM and storage.
- **Discussion**: Why computers follow instructions exactly; what happens if instructions are wrong.

**Workshop ideas**

- **Label the diagram**: Students label a blank diagram of a computer with CPU/RAM/storage/I/O.
- **Program hunt**: In pairs, list as many programs they used in the last 24 hours and what each does.
- **Mini role-play**: One student is “CPU”, others give them step‑by‑step instructions (e.g., move 3 steps, turn left).

**Homework suggestions**

- **Short reflection**: Write a short paragraph describing the parts of a computer and their roles.
- **Everyday programs list**: List 5 programs you use and describe what inputs and outputs they have.
- **Concept check quiz**: Simple multiple choice / short answer about CPU vs memory vs storage.

**Connection**

- **From previous**: First session, no prerequisites.
- **To next**: Sets the stage for understanding how source code becomes something a CPU can execute.

---

### Session 2: From Source Code to Machine Code

**Learning objectives**

- **Define** source code and machine code.
- **Explain** why computers need machine code (0s and 1s).
- **Compare** compilers and interpreters at a high level.
- **Recognize** that Python is typically interpreted.

**Main concepts**

- **Source code**: Human‑readable instructions.
- **Machine code**: CPU‑readable instructions.
- **Compilation vs interpretation**: Two main ways to get from source to execution.
- **High‑level vs low‑level languages**.

**Tutorial content summary**

- **Story of a program**: Human writes source → compiler/interpreter → machine code → CPU executes.
- **Visual pipeline diagram**: Show arrows from `.py` file to Python interpreter to machine instructions.
- **Compilers vs interpreters**: Analogies (translator who translates entire book vs simultaneous interpreter).
- **Python**: Where it fits; REPL, interpreter.

**Workshop ideas**

- **Match the terms**: Cards with “source code”, “machine code”, “compiler”, “interpreter” and definitions to match.
- **Language examples**: Show same simple algorithm in pseudocode vs C vs Python; ask which is more readable.
- **Explain to a friend**: In pairs, explain the difference between compiler and interpreter using your own analogy.

**Homework suggestions**

- **Short essay**: Explain to a non‑technical friend what “source code” is in 5–7 sentences.
- **Compare tools**: Look up an example compiled language and an interpreted language; write 2–3 differences.
- **Concept questions**: Few questions on why we don’t write machine code directly.

**Connection**

- **From previous**: Builds on what a program is and how it runs.
- **To next**: Prepares for understanding what bits and bytes actually are in memory.

---

### Session 3: Bits, Bytes, and Representing Information

**Learning objectives**

- **Define** bit and byte.
- **Explain** how bits can represent yes/no, true/false, and numbers.
- **Describe** how larger data is built from bits and bytes.
- **Recognize** that all digital data is ultimately bits.

**Main concepts**

- **Bit**: 0 or 1.
- **Byte**: Group of 8 bits.
- **Representing information**: On/off switches, true/false, tiny memory cells.
- **Examples**: Images, text, audio as huge collections of bits.

**Tutorial content summary**

- **Physical analogy**: Light switches or beads representing bits.
- **From bits to numbers**: How different bit patterns correspond to different numbers.
- **Scale**: 1 KB, 1 MB, 1 GB (intuitive comparisons).
- **Everyday example**: File sizes and why they matter.

**Workshop ideas**

- **Human bits game**: 8 students stand in a line, each is a bit (raising hand=1, down=0); interpret pattern as a number.
- **Estimate sizes**: Guess how many bytes a short text file vs a photo might have, then verify on a computer.
- **Bit patterns**: Given some patterns (e.g., 00000000, 00000001, 11111111), ask what numbers they might represent.

**Homework suggestions**

- **Terminology sheet**: Define “bit”, “byte”, “kilobyte”, “megabyte”, “gigabyte” in your own words.
- **File inspection**: On your computer/phone, find sizes of 3 different files (image, song, document) and record them.
- **Mini problems**: If you have 3 bits, how many different patterns? What about 4 bits?

**Connection**

- **From previous**: Moves from abstract “machine code” to concrete 0s and 1s.
- **To next**: Sets up number systems (binary, decimal, hex) built on bits.

---

### Session 4: Number Bases – Binary, Decimal, Hexadecimal

**Learning objectives**

- **Explain** what a number base is.
- **Convert** small numbers between decimal and binary.
- **Recognize** hexadecimal notation and its purpose.
- **Relate** binary numbers to bits and bytes.

**Main concepts**

- **Base 10 (decimal)**: Our usual system.
- **Base 2 (binary)**: Using digits 0 and 1.
- **Base 16 (hexadecimal)**: Using digits 0–9 and A–F.
- **Place value**: Ones, twos, fours, eights… vs ones, tens, hundreds.

**Tutorial content summary**

- **Review decimal**: Place values 1,10,100.
- **Introduce binary**: Place values 1,2,4,8,16…; examples converting small numbers.
- **Introduce hex**: Why it’s useful (compact representation of bits/bytes).
- **Step‑by‑step conversions**: Decimal → binary and binary → decimal exercises.

**Workshop ideas**

- **Convert in groups**: In pairs, convert given decimal numbers (0–31) to binary.
- **Binary blocks**: Use blocks labeled 1,2,4,8 to build numbers physically.
- **Hex practice**: Convert a byte (e.g., 10101100) to hex and vice versa.

**Homework suggestions**

- **Conversion drills**: 10–15 small numbers to convert between binary and decimal.
- **Explain in words**: Describe how you would convert 13 (decimal) to binary.
- **Challenge**: Convert some small decimals to hex (with guidance).

**Connection**

- **From previous**: Extends bits/bytes into number systems.
- **To next**: Prepares for simple binary arithmetic and understanding how computers add numbers.

---

### Session 5: Simple Binary Arithmetic

**Learning objectives**

- **Perform** simple binary addition of small numbers.
- **Understand** carries in binary addition.
- **Explain** at a high level how computers add numbers.
- **Recognize** limits of fixed‑size binary numbers (overflow conceptually).

**Main concepts**

- **Binary addition rules**: 0+0, 0+1, 1+0, 1+1.
- **Carrying**: When a sum exceeds 1.
- **Overflow**: When result doesn’t fit in fixed bits (conceptual only).
- **Relation to hardware**: Very high‑level view of adders.

**Tutorial content summary**

- **Addition table** for two bits.
- **Column‑wise addition** examples: adding 2‑bit, 3‑bit, 4‑bit numbers.
- **Visuals**: Comparing to decimal addition with carries.
- **Demo**: Show a simple online visualization of binary adders (optional).

**Workshop ideas**

- **Practice problems**: Students add binary numbers (e.g., 0011 + 0101).
- **Group explanation**: In small groups, explain to each other how binary addition works.
- **Overflow examples**: Show a few additions where the result would need more bits.

**Homework suggestions**

- **Binary addition sheet**: 10–15 binary additions.
- **Reflection**: Write 3–4 sentences on how binary and decimal addition are similar and different.
- **Optional challenge**: Simple binary subtraction with hints.

**Connection**

- **From previous**: Uses binary notation to do real operations.
- **To next**: Leads into representing characters/text (ASCII/Unicode) and then to algorithms.

---

### Session 6: Text Representation – ASCII and Unicode

**Learning objectives**

- **Explain** how characters are stored using numbers.
- **Differentiate** between ASCII and Unicode.
- **Describe** why Unicode is needed (beyond English).
- **Give** everyday examples of encodings (emojis, accented letters).

**Main concepts**

- **Character → number**: Code points.
- **ASCII**: 7/8‑bit basic Latin set.
- **Unicode**: Much larger system covering many scripts and symbols.
- **Encodings (UTF‑8, etc.)** at a conceptual level.

**Tutorial content summary**

- **ASCII table snippet**: Show a few letters and their codes.
- **Unicode overview**: Many scripts/symbols, emojis.
- **Why Unicode**: Need to handle many languages and symbols.
- **Examples**: Show a string as bytes in an editor or online tool.

**Workshop ideas**

- **Decode exercise**: Given a few ASCII codes, students write letters; and vice versa.
- **Name encoding**: Look up the Unicode code points for characters in their name.
- **Language diversity**: Show text in multiple languages and discuss how computers handle it.

**Homework suggestions**

- **Short answers**: Questions on why ASCII alone isn’t enough.
- **Code lookup**: Find Unicode code points for 5 emojis and record them.
- **Reflection**: 1–2 paragraphs on why encoding standards matter in software.

**Connection**

- **From previous**: Extends bits and numbers to characters and text.
- **To next**: Completes “data representation” foundation, paving the way to algorithmic thinking.

---

### Session 7: From Data to Problems – Inputs, Outputs, and State

**Learning objectives**

- **Identify** inputs, outputs, and internal state in everyday systems.
- **Describe** program behavior as transforming input data into output data.
- **Relate** stored data (bits) to problem‑solving.
- **Prepare** to express solutions as algorithms.

**Main concepts**

- **Input–process–output** model.
- **Examples**: Calculator, ATM, login system.
- **State**: Memory contents that change over time.
- **From representation to behavior**: Data + rules → programs.

**Tutorial content summary**

- **IPO diagrams**: Draw simple input–process–output boxes for real systems.
- **State examples**: Variables like balance, score, position.
- **Thinking in terms of data**: What information is needed to solve a problem?
- **Transition to algorithms**: How we will soon describe processes step by step.

**Workshop ideas**

- **System breakdown**: In groups, choose a familiar app and identify its inputs, outputs, and key internal data.
- **IPO practice**: Draw IPO for making tea, ordering food, etc.
- **State changes**: Track score changes in a simple game scenario.

**Homework suggestions**

- **IPO worksheets**: 3–5 real‑world scenarios to model.
- **Short reflection**: Why is it helpful to think in terms of input/process/output?
- **Prep**: Write, in natural language, how you would find the largest number in a list.

**Connection**

- **From previous**: Uses knowledge of data to think about behavior.
- **To next**: Natural bridge into algorithms and pseudocode.

---

### Session 8: What Is an Algorithm? Natural Language Descriptions

**Learning objectives**

- **Define** what an algorithm is in programming.
- **Describe** simple algorithms in plain language.
- **Identify** inputs, outputs, and steps in an algorithm.
- **Appreciate** that the same problem can have multiple algorithms.

**Main concepts**

- **Algorithm**: Step‑by‑step procedure to solve a problem.
- **Properties**: Clear, finite, effective.
- **Everyday algorithms**: Recipes, directions, to‑do lists.
- **Algorithm vs program**: Concept vs specific code.

**Tutorial content summary**

- **Examples**: Recipe for making a sandwich, steps to log into an account.
- **Formalizing steps**: Discuss precision/ambiguity in everyday instructions.
- **Algorithm features**: Input, output, definiteness, finiteness.
- **Examples of simple data algorithms**: Find max, sum numbers.

**Workshop ideas**

- **Sandwich algorithm**: Students write sandwich‑making steps; teacher acts them out literally to show ambiguity.
- **Clarify algorithms**: Improve vague instructions collaboratively.
- **Problem breakdown**: Students outline steps for “count how many times a word appears in a sentence”.

**Homework suggestions**

- **Write algorithms**: In natural language, for (a) summing list of 5 numbers, (b) finding largest of 3 numbers.
- **Identify algorithms**: Describe an algorithm used in a favorite app or website.
- **Reflection**: 1–2 paragraphs on why precision matters in algorithms.

**Connection**

- **From previous**: Builds on IPO thinking.
- **To next**: Leads into pseudocode as a more structured way to write algorithms.

---

### Session 9: Pseudocode and Basic Control Structures

**Learning objectives**

- **Write** simple algorithms in structured pseudocode.
- **Use** sequence, decision (if), and repetition (loops) in pseudocode.
- **Express** classic simple algorithms (max, linear search) in pseudocode.
- **Prepare** to map pseudocode ideas to Python.

**Main concepts**

- **Pseudocode**: Language‑like structured description, not real code.
- **Control structures**: Sequence, selection (IF), iteration (loops).
- **Example algorithms**: Max in list, linear search, counting, sum.

**Tutorial content summary**

- **Pseudocode style**: Simple conventions (e.g., IF/ELSE, WHILE, FOR EACH).
- **Examples**: Turn earlier natural‑language algorithms into pseudocode.
- **Control structures**: Illustrate with flowcharts or indentation.
- **Trace examples**: Walk through pseudocode with sample inputs.

**Workshop ideas**

- **Rewrite exercises**: Convert earlier natural‑language homework algorithms into pseudocode.
- **Max and search**: Write pseudocode for finding max and for searching a target in a list.
- **Tracing**: Given pseudocode, step through on sample data and record outputs.

**Homework suggestions**

- **Pseudocode practice**: Write pseudocode for (a) counting how many numbers in a list are positive, (b) computing average.
- **Trace tasks**: Trace given pseudocode line by line and show resulting output.
- **Concept questions**: Identify where input, process, and output appear in given pseudocode.

**Connection**

- **From previous**: Moves from natural descriptions to structured algorithm notation.
- **To next**: Now ready to see Python as a concrete language that implements these pseudocode ideas.

---

### Session 10: Getting Started with Python – Environment and First Steps

**Learning objectives**

- **Install or access** a Python environment (local or online).
- **Use** the Python REPL to run simple expressions.
- **Run** a basic Python script from a file.
- **Relate** simple Python statements to pseudocode steps.

**Main concepts**

- **Python interpreter & REPL**.
- **Scripts vs interactive mode**.
- **Printing output (`print`)**.
- **Comment lines for explanations**.

**Tutorial content summary**

- **Environment setup**: Show how to open Python (or use an online environment).
- **REPL demo**: Simple arithmetic, strings, `print`.
- **First script**: Create a `.py` file that prints a greeting; run it.
- **Connecting to pseudocode**: Simple sequence of steps as Python statements.

**Workshop ideas**

- **Hello program**: Everyone writes a script that prints their name and a short message.
- **Calculator REPL**: Use Python as a calculator (add, subtract, multiply, divide).
- **Comment practice**: Add explanations as comments above lines.

**Homework suggestions**

- **Environment check**: Confirm Python works at home (or note issues).
- **Tiny scripts**: Write a script that prints a short “about me” and your favorite number.
- **Reflection**: Short paragraph on how Python feels compared to pseudocode.

**Connection**

- **From previous**: Implements algorithmic thinking in a real language for the first time.
- **To next**: Prepares to introduce variables and data types.

---

### Session 11: Variables and Basic Data Types (int, float, bool, str)

**Learning objectives**

- **Define** what a variable is in programming.
- **Use** integers, floats, booleans, and strings in Python.
- **Assign** values to variables and print them.
- **Recognize** type‑related errors conceptually.

**Main concepts**

- **Variables**: Names pointing to values.
- **Data types**: `int`, `float`, `bool`, `str`.
- **Simple operations** on these types.
- **Type conversion basics** (`int()`, `str()`, etc., conceptually).

**Tutorial content summary**

- **Variable examples**: `age = 20`, `price = 4.99`, `is_sunny = True`, `name = "Ali"`.
- **Printing variables**: Using `print(name, age)`.
- **Type introspection**: `type()` for curiosity.
- **Primitive examples**: How these relate to data representation (numbers, text, true/false).

**Workshop ideas**

- **Personal data**: Students create variables for name, age, height, likes_programming.
- **Mini profile**: Script that prints a short profile using variables.
- **Type guessing**: Show literals and ask students to guess their types.

**Homework suggestions**

- **Variable exercises**: Create a few scripts that define and print variables describing a product, a movie, etc.
- **Predict output**: Given small code snippets, predict what will be printed.
- **Type challenge**: Error‑spotting tasks (e.g., trying to add a string and number without conversion).

**Connection**

- **From previous**: Moves from bare expressions to named data.
- **To next**: Leads into user input and more complex expressions and operators.

---

### Session 12: Input/Output and Expressions & Operators

**Learning objectives**

- **Use** `input()` to read user input.
- **Convert** input strings to numbers as needed.
- **Build** expressions using arithmetic and comparison operators.
- **Write** small programs combining input, processing, and output.

**Main concepts**

- **Input**: `input()` and returning strings.
- **Output**: `print()` with variables and expressions.
- **Operators**: `+`, `-`, `*`, `/`, `//`, `%`, `**`, `==`, `!=`, `<`, `>`, `<=`, `>=`.
- **Expression evaluation**: Order of operations.

**Tutorial content summary**

- **Simple I/O program**: Ask for name and age; greet user and show age next year.
- **Numeric input**: Use `int()`/`float()` on input.
- **Operators practice**: Evaluate expressions and predict results.
- **Link to algorithms**: Implement “sum of two numbers” as a program.

**Workshop ideas**

- **Age calculator**: Ask for current year and birth year; compute age.
- **Rectangle calculator**: Ask for width/height; compute area/perimeter.
- **Comparison demo**: Ask for two numbers; print which is larger.

**Homework suggestions**

- **Mini calculators**: Programs for currency conversion, temperature conversion, etc.
- **Expression puzzles**: Simplify and predict results of given expressions.
- **I/O story**: Write a simple dialogue program that asks a few questions and replies.

**Connection**

- **From previous**: Adds user interaction and richer expressions to variables.
- **To next**: Sets up the need for decision‑making via `if`, `elif`, `else`.

---

### Session 13: Decision Making with `if`, `elif`, `else`

**Learning objectives**

- **Write** simple conditional statements in Python.
- **Use** `if`, `elif`, and `else` for branching logic.
- **Translate** decision‑making pseudocode into Python conditionals.
- **Debug** common indentation and logic mistakes.

**Main concepts**

- **Conditionals**: Evaluating boolean expressions.
- **Indentation**: Code blocks in Python.
- **Nested and chained conditionals**.
- **Simple decision problems**: Grade classifier, sign of a number, etc.

**Tutorial content summary**

- **Basic `if`**: Run code only when a condition is true.
- **Adding `else`**: Two‑way decisions.
- **`elif` chains**: Multiple conditions.
- **Examples**: Age‑based messages, simple grading, number comparison.

**Workshop ideas**

- **Pass/fail checker**: Program that reads a score and prints pass/fail.
- **Number sign**: Program that says if a number is positive, negative, or zero.
- **Discount logic**: Simple discount based on purchase amount (if/elif).

**Homework suggestions**

- **Condition exercises**: Write conditionals for day/night messages, voting eligibility, etc.
- **Predict branches**: Given code and inputs, indicate which branch will run.
- **Rewrite pseudocode**: Convert 2–3 pseudocode decision algorithms into Python.

**Connection**

- **From previous**: Uses operators and expressions in decisions.
- **To next**: Leads into repetition with loops, often combined with conditionals.

---

### Session 14: Loops – `while` and `for`

**Learning objectives**

- **Explain** why loops are needed (repetition).
- **Use** `while` loops for condition‑controlled repetition.
- **Use** `for` loops with `range()` and over simple sequences.
- **Avoid** common infinite loop mistakes.

**Main concepts**

- **`while` loops**: Repeat while a condition is true.
- **`for` loops**: Iterating over ranges and sequences.
- **Loop variables and updates**.
- **Combining loops with conditionals**.

**Tutorial content summary**

- **Counting loops**: Print numbers 1–10 with both `while` and `for`.
- **Summation loop**: Sum of numbers 1–n.
- **Input loops**: Ask repeatedly until user enters a valid value.
- **Tracing loops**: Hand‑simulate loop iterations.

**Workshop ideas**

- **Multiplication table**: Print table for a chosen number using a loop.
- **Guessing game (simple)**: User guesses a number with limited tries (basic version).
- **List processing preview**: Use a loop over a small predefined list.

**Homework suggestions**

- **Loop patterns**: Print even numbers, count down to 0, etc.
- **Trace exercises**: Given loop code, show sequence of values.
- **Small programs**: Sum of first N squares, simple factorial (conceptually).

**Connection**

- **From previous**: Adds repetition to decision‑making.
- **To next**: Prepares for working with collections like strings and lists more naturally in loops.

---

### Session 15: Working with Strings

**Learning objectives**

- **Create** and manipulate strings in Python.
- **Use** basic string methods (`len`, `.lower()`, `.upper()`, slicing).
- **Iterate** over characters in a string.
- **Solve** simple text‑processing tasks.

**Main concepts**

- **String literals** and concatenation.
- **Indexing and slicing**.
- **Common methods**: `.strip()`, `.replace()`, etc. (beginner level).
- **Relation to Unicode/encoding** (conceptual link).

**Tutorial content summary**

- **Indexing examples**: Get first/last character.
- **Slicing**: Substrings like first 3 characters.
- **Case conversion** and basic cleaning.
- **Simple patterns**: Count occurrences of a letter, reverse a string (with loops or slicing).

**Workshop ideas**

- **Name formatter**: Ask first and last name; print in different formats (all caps, etc.).
- **Word counter (simple)**: Count spaces to approximate word count.
- **Character counter**: Count how many times a chosen character appears.

**Homework suggestions**

- **String tasks**: Check if a string starts/ends with certain characters, simple censorship (replace word with `***`).
- **Slicing practice**: Given a string, extract parts with slices.
- **Mini challenge**: Reverse a string (using slicing or loop).

**Connection**

- **From previous**: Uses loops and decision logic on text.
- **To next**: Extends to collections like lists, tuples, dictionaries, sets.

---

### Session 16: Collections – Lists, Tuples, Dictionaries, Sets (Beginner Level)

**Learning objectives**

- **Describe** when to use lists, tuples, dictionaries, and sets at a basic level.
- **Create** and access elements in lists and dictionaries.
- **Iterate** over lists with `for` loops.
- **Use** simple collection operations (append, membership checks).

**Main concepts**

- **Lists**: Ordered, mutable sequences.
- **Tuples**: Ordered, often used for fixed groups.
- **Dictionaries**: Key–value mappings.
- **Sets**: Unordered unique elements (brief introduction).

**Tutorial content summary**

- **Basic list operations**: Create, index, append, iterate.
- **Dictionaries**: Create small dictionary, access by key.
- **Use cases**: Storing scores, mapping names to phone numbers.
- **Simple set use**: Remove duplicates from a list (conceptually).

**Workshop ideas**

- **Shopping list**: List of items; add/remove items, print all.
- **Phone book**: Simple dictionary mapping names to numbers; look up entries.
- **Unique words**: Basic example using set to find unique words in a sentence (guided).

**Homework suggestions**

- **List exercises**: Build and manipulate small lists (insert, remove, slice).
- **Dictionary tasks**: Create a dictionary of countries to capitals; access them.
- **Membership**: Check if an item is in a list or set.

**Connection**

- **From previous**: Builds on loops and strings to store many values.
- **To next**: Prepares for functions that operate on these data structures.

---

### Session 17: Functions – Reusable Blocks of Code

**Learning objectives**

- **Define** and call simple Python functions.
- **Use** parameters and return values.
- **Differentiate** between local variables and global variables conceptually.
- **Write** functions that encapsulate small algorithms.

**Main concepts**

- **Function definitions** with `def`.
- **Parameters and arguments**.
- **Return values** and `return` statement.
- **Reusability and modularity**.

**Tutorial content summary**

- **Simple functions**: `greet(name)`, `add(a, b)`.
- **Return vs print**: Clarify difference.
- **Refactoring**: Turn part of a longer script into a function.
- **Scope overview**: Where variables “live” (basic notion).

**Workshop ideas**

- **Math functions**: Write functions to compute area of shapes.
- **Utility functions**: Write `is_even(n)`, `max_of_three(a, b, c)`.
- **Refactor**: Take a prior homework script and split into functions.

**Homework suggestions**

- **Function library**: Create 3–5 small functions and a script that calls them.
- **Predict output**: For given function definitions and calls, show results.
- **Rewrite pseudocode**: Turn a pseudocode algorithm (e.g., linear search) into a function.

**Connection**

- **From previous**: Uses data structures and loops inside modular units.
- **To next**: Leads into handling errors and debugging functions and programs.

---

### Session 18: Basic Error Handling and Debugging

**Learning objectives**

- **Recognize** common Python error messages (syntax, runtime).
- **Use** `try`/`except` for simple error handling.
- **Apply** basic debugging strategies (print statements, reasoning).
- **Develop** a mindset that errors are normal and helpful.

**Main concepts**

- **Types of errors**: Syntax, runtime, logical.
- **Reading tracebacks** at a beginner level.
- **`try`/`except`** blocks for safe operations (e.g., input conversion).
- **Debugging habits**: Isolate, simplify, test small pieces.

**Tutorial content summary**

- **Intentional errors**: Show code with errors; read messages together.
- **Simple `try`/`except`**: Wrap `int(input())` to catch invalid input.
- **Debugging checklist**: Steps to find problems.
- **Link to algorithms**: Re‑check algorithm logic when code seems fine.

**Workshop ideas**

- **Fix the code**: Provide broken snippets; students fix them.
- **Robust input**: Extend a previous input program to handle bad input gracefully.
- **Error reading**: Given tracebacks, identify the line and probable issue.

**Homework suggestions**

- **Debug tasks**: 3–5 short buggy code fragments to correct.
- **Error log**: While doing other homework, note any error messages and how they fixed them.
- **Simple `try`/`except`**: Program that keeps asking for a number until a valid one is given.

**Connection**

- **From previous**: Builds on writing non‑trivial code; now learning to handle when things go wrong.
- **To next**: Prepares for reading and writing files, where errors are common.

---

### Session 19: Working with Files – Reading and Writing Text Files

**Learning objectives**

- **Open** and close text files in Python.
- **Read** contents of a file line by line.
- **Write** text to a new or existing file.
- **Use** basic patterns to process file data.

**Main concepts**

- **File paths** (basic).
- **`open()`**, context managers (`with`).
- **Reading methods**: `.read()`, `.readline()`, `.readlines()` (conceptual).
- **Writing**: `write()` and appending.

**Tutorial content summary**

- **Simple write**: Create a text file with some lines.
- **Simple read**: Print file contents to screen.
- **Line processing**: Count lines or words.
- **Safety**: Emphasize `with` blocks to ensure closing.

**Workshop ideas**

- **Journal program**: Append a new journal entry to a text file.
- **Word counter v2**: Read a file and count lines or words.
- **Copy file**: Simple script that copies contents from one file to another.

**Homework suggestions**

- **Log creator**: Program that logs user actions (e.g., login times) to a file.
- **File stats**: Script to print number of lines and characters in a file.
- **Reflection**: Short explanation on when file processing is useful in real life.

**Connection**

- **From previous**: Uses functions, error handling when files are missing or unreadable.
- **To next**: Leads into organizing code into multiple files/modules and a small project.

---

### Session 20: Organizing Code – Modules and a Small Multi-File Program

**Learning objectives**

- **Import** functions from one Python file into another.
- **Organize** code into simple modules based on purpose.
- **Structure** a small project with multiple files.
- **Understand** basic `__main__` usage (conceptual).

**Main concepts**

- **Modules**: Python files as reusable units.
- **Imports**: `import`, `from ... import ...`.
- **Project structure**: Grouping related functionality.
- **Simple main script** that ties it all together.

**Tutorial content summary**

- **Create utility module**: `utils.py` with a couple of functions.
- **Import and use**: Call these functions from `main.py`.
- **Explain structure**: How splitting code improves clarity.
- **Mini project example**: Simple text‑based application using multiple files.

**Workshop ideas**

- **Two‑file project**: One file for functions, one for user interaction.
- **Utility library**: In groups, build a small module of helper functions.
- **Refactor**: Take a previous larger script and split it into 2–3 files.

**Homework suggestions**

- **Module practice**: Create a simple math utilities module and a script that uses it.
- **Directory layout**: Draw a diagram of your project’s files and explain each.
- **Reflection**: Short writing on why organizing code matters.

**Connection**

- **From previous**: Builds on functions and files to make more realistic programs.
- **To next**: Sets up for integrated mini‑projects drawing on the whole course.

---

### Session 21: Mini-Project 1 – Data Processing Script

**Learning objectives**

- **Plan** and implement a small end‑to‑end Python program.
- **Apply** variables, control structures, collections, functions, and files together.
- **Test** and debug a complete script.
- **Reflect** on the development process.

**Main concepts**

- **Project planning**: Requirements, inputs, outputs.
- **Incremental development**: Build in small steps and test.
- **Integrating features**: Loops, conditionals, functions, file I/O.
- **User experience**: Simple prompts and messages.

**Tutorial content summary**

- **Project choice**: Teacher proposes a concrete small project (e.g., student gradebook, expense tracker, simple log analyzer).
- **Requirements breakdown**: List features, inputs, outputs.
- **Step‑by‑step build**: Start with core functionality, then add features.
- **Testing**: Try various inputs, fix bugs.

**Workshop ideas**

- **Group project building**: In small teams, implement the chosen project with guidance.
- **Feature extension**: Each group adds one extra feature.
- **Peer demo**: Groups briefly show their program to others.

**Homework suggestions**

- **Project polish**: Clean up and document code (comments, clearer variable names).
- **User guide**: Write a short README‑style description of what the program does and how to run it.
- **Optional extension**: Add one more feature or robustness improvement.

**Connection**

- **From previous**: Combines all skills from Python fundamentals and file handling.
- **To next**: Prepares for final review and a second capstone‑style mini‑project or individual project.

---

### Session 22: Review, Consolidation, and Capstone Mini-Projects

**Learning objectives**

- **Review** key concepts from the entire course.
- **Complete** or present a small personal or group mini‑project.
- **Reflect** on learning progress and next steps.
- **Identify** areas for further study in programming.

**Main concepts**

- **Concept recap**: Computer model, data representation, algorithms, Python basics.
- **Project showcase**.
- **Feedback and reflection**.
- **Paths forward**: Further Python, web, data science, etc.

**Tutorial content summary**

- **Concept quiz/review**: Interactive recap of main ideas.
- **Q&A**: Address lingering questions.
- **Capstone guidance**: Suggestions for small personal projects (e.g., quiz game, simple to‑do list, text analyzer).
- **Next steps**: Introduce resources for continued learning.

**Workshop ideas**

- **Project work time**: Students build or finalize a small project (individually or in pairs).
- **Presentations**: Short demos to the class.
- **Peer feedback**: Simple feedback forms or informal comments.

**Homework suggestions**

- **Final reflection**: 1–2 pages describing what they learned, what was hardest, and what they enjoyed.
- **Future plan**: List 2–3 goals for the next 3–6 months of programming practice.
- **Optional**: Continue expanding the capstone project after the course ends.

**Connection**

- **From previous**: Builds directly on mini‑project skills.
- **To future**: Bridges this introductory course to more advanced topics and self‑study.

---

## Repository/folder structure description

**Top-level structure**

- **`overview.md`**: Brief description of the course, goals, themes, and how to use the repository.
- **`session-01/`** … **`session-22/`**: One folder per session, each containing:
  - **`README.md`**: Main concepts, explanations, and tutorial notes for that session.
  - **`workshop/`**: Subfolder with example starter code, skeletons, or prompts for in‑class exercises.
  - **`homeworks/`**: Subfolder with homework descriptions and (optionally) starter files or templates.

Example structure in text:

- **Root**
  - `overview.md`
  - `session-01/`
    - `README.md`
    - `workshop/`
    - `homeworks/`
  - `session-02/`
    - `README.md`
    - `workshop/`
    - `homeworks/`
  - …
  - `session-22/`
    - `README.md`
    - `workshop/`
    - `homeworks/`

---

### Sample `README.md` outline – Session 1

`session-01/README.md`:

- **Title**: What Is a Computer? How Programs Run
- **1. Session overview**: One paragraph summarizing goals (understand basic computer components and how programs run).
- **2. Key terms**: CPU, RAM, storage, input device, output device, program, software, hardware.
- **3. Computer components**: Short subsections describing CPU, memory, storage, and I/O with diagrams.
- **4. What is a program?**: Explanation of programs as instructions; everyday examples.
- **5. How a program runs**: High‑level narrative from clicking an icon to CPU executing instructions.
- **6. Everyday analogies**: Simple comparisons (kitchen, factory) to reinforce understanding.
- **7. Summary and checklist**: Quick recap and self‑check questions.

---

### Sample `README.md` outline – Session 10

`session-10/README.md`:

- **Title**: Getting Started with Python – Environment and First Steps
- **1. Session overview**: Goals of running Python interactively and via scripts.
- **2. What is the Python interpreter?**: Short explanation of interpreter and REPL.
- **3. Installing or accessing Python**: Instructions and screenshots/links for chosen environment.
- **4. Using the Python REPL**: Examples of entering expressions and seeing results.
- **5. Writing your first script**: Step‑by‑step guide: create file, add code, run it.
- **6. Connecting Python to pseudocode**: Compare a small pseudocode example with its Python version.
- **7. Common beginner issues**: Tips about saving files, path issues, and simple troubleshooting.
- **8. Summary and next steps**: What to practice before moving on to variables and types.

---

### Sample `README.md` outline – Session 20

`session-20/README.md`:

- **Title**: Organizing Code – Modules and a Small Multi-File Program
- **1. Session overview**: Why we split code into multiple files/modules.
- **2. What is a module?**: Python file as a reusable unit; examples.
- **3. Importing code**: `import` and `from … import …` with small examples.
- **4. Designing a simple project structure**: Example directory layout for a tiny app.
- **5. Step-by-step multi-file example**: Walkthrough of creating `utils.py` and `main.py`, and how they work together.
- **6. Common pitfalls**: Import errors, circular imports (brief warning), naming issues.
- **7. Summary and mini‑project ideas**: Ideas for small multi‑file projects and how to approach them.

This syllabus follows the required progression: conceptual computer foundations and data representation first, then algorithmic thinking and pseudocode, and only then Python syntax and practical programming, culminating in integrated mini‑projects.