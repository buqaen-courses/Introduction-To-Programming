# Session 9 Concepts: Expressing Algorithms

This folder contains articles about expressing algorithms visually (flowcharts) and textually (pseudocode), plus the control structures that form the building blocks of all algorithms. These concepts build on Sessions 7 (IPO analysis) and 8 (FIDEO definition), showing you how to formally describe algorithms.

## Table of Contents

### Visual Algorithm Design ⭐ START HERE
- **📊 [Flowchart Fundamentals](flowchart-fundamentals.md)** - Visual algorithm representation with standard symbols
  - Sum Numbers
  - Find Maximum
  - Find Minimum
  - Simple Sort

### Textual Algorithm Expression
- **📝 [Pseudocode Fundamentals](pseudocode-fundamentals.md)** - Writing structured algorithm descriptions
- **🔧 [Control Structures](control-structures.md)** - Sequence, selection, and iteration

### Implementation Bridge
- **💻 [Pseudocode to Code](pseudocode-to-code.md)** - Translating to actual programming languages

## Persian Translations

For Persian speakers:
- **📝 [مبانی شبه‌کد](pseudocode-fundamentals_fa.md)** - Pseudocode fundamentals in Persian
- **🔧 [ساختارهای کنترلی](control-structures_fa.md)** - Control structures in Persian
- **💻 [از شبه‌کد به کد](pseudocode-to-code_fa.md)** - Pseudocode to code in Persian

## Recommended Reading Order

### For Visual Learners
1. **Flowchart Fundamentals** - See algorithms visually
2. **Pseudocode Fundamentals** - Learn the textual equivalent
3. **Control Structures** - Understand the building blocks
4. **Pseudocode to Code** - Make the leap to actual programming

### For Textual Learners
1. **Pseudocode Fundamentals** - Start with structured text
2. **Control Structures** - Master the three fundamental structures
3. **Flowchart Fundamentals** - Add visual understanding
4. **Pseudocode to Code** - Translate to real code

## Detailed Article Descriptions

### 📊 [Flowchart Fundamentals](flowchart-fundamentals.md) ⭐ PRIMARY READING
**Start here for visual understanding of algorithms.**

Learn to express algorithms using standard symbols:
- ⬭ **Terminator** (Oval): Start and End
- ⬜ **Process** (Rectangle): Actions and calculations
- 🔷 **Decision** (Diamond): Yes/No questions
- 🗄️ **Input/Output** (Parallelogram): Reading and displaying
- ➡️ **Flow Line** (Arrow): Direction of execution

**Four Complete Algorithm Examples:**
1. **Sum Numbers**: Adding a list of numbers step-by-step
2. **Find Maximum**: Tracking the largest value seen
3. **Find Minimum**: Tracking the smallest value seen
4. **Simple Sort (Bubble Sort)**: Arranging numbers in order

Each includes:
- ASCII art flowcharts
- Step-by-step thinking process
- Matching pseudocode
- Trace tables showing execution
- Practice exercises

**Why read this?** Flowcharts make algorithm logic visible. You can see the flow, spot errors, and trace execution easily.

### 📝 [Pseudocode Fundamentals](pseudocode-fundamentals.md) ⭐ PRIMARY READING
**The bridge between thinking and coding.**

Master structured English for algorithms:

**Basic Elements:**
- Variables and assignment: `SET x TO 5` or `x ← 5`
- Input/Output: `READ x`, `WRITE "Result: " + x`
- Math operations: `+`, `-`, `×`, `/`, `MOD`

**Program Structure:**
- Algorithm headers and declarations
- Sequential structure
- Modular design (functions/procedures)
- Comments and documentation

**Data Structures:**
- Arrays and indexing
- Records/structures
- Lists and collections

**Why read this?** Pseudocode is language-independent. It describes the logic without getting bogged down in syntax details.

### 🔧 [Control Structures](control-structures.md) ⭐ PRIMARY READING
**The three building blocks of all algorithms.**

Understand the fundamental structures that control program flow:

**1. Sequence (Straight Line)**
```
BEGIN
    Step 1: Do this
    Step 2: Do that
    Step 3: Do next
END
```
- Execute steps in order
- Foundation of all algorithms

**2. Selection (Decision Making)**
```
IF condition THEN
    Do something
ELSE
    Do something else
END IF
```
- Simple IF
- IF-ELSE
- Nested IF
- Multiple selection (IF-ELSEIF)

**3. Iteration (Looping)**
```
WHILE condition DO
    Repeat this
END WHILE

FOR i FROM 1 TO 10 DO
    Repeat this
END FOR
```
- Pre-test loops (WHILE)
- Post-test loops (REPEAT-UNTIL)
- Counted loops (FOR)
- Loop control (BREAK, CONTINUE)

**Includes:**
- Examples in pseudocode, Python, and JavaScript
- Common pitfalls and how to avoid them
- Nested structures
- Best practices

**Why read this?** Every algorithm, no matter how complex, is built from these three structures.

### 💻 [Pseudocode to Code](pseudocode-to-code.md) - BRIDGE TO PROGRAMMING
**Making the leap from design to implementation.**

Learn to translate pseudocode into actual programming languages:

**Translation Process:**
1. Understand the pseudocode logic
2. Choose target language (Python, JavaScript, etc.)
3. Map constructs: pseudocode → language syntax
4. Handle language-specific details
5. Test and verify

**Examples Include:**
- IF statements in Python, JavaScript, Java, C++
- Loops in multiple languages
- Variable declarations
- Function definitions
- Error handling

**Why read this?** This article bridges the gap between algorithm design and actual programming.

## Key Themes

### Visual + Textual = Complete Understanding
- **Flowcharts** help you see the algorithm structure
- **Pseudocode** provides precise details
- **Together** they give complete understanding
- **Practice**: Convert between the two forms

### The Three Control Structures
Every algorithm uses only three basic patterns:
1. **Sequence**: Do A, then B, then C
2. **Selection**: If X is true, do Y, else do Z
3. **Iteration**: While condition is true, repeat action

**Important**: Even the most complex programs (Google Search, operating systems, games) are built from these three structures combined in sophisticated ways.

### Translation is a Skill
Learning to translate between forms:
- Natural Language → Flowchart
- Flowchart → Pseudocode
- Pseudocode → Actual Code

This skill is essential for moving from design to implementation.

## Prerequisites

These articles assume you've completed:
- **Session 7**: IPO analysis (understand what goes in and out)
- **Session 8**: FIDEO characteristics (understand what makes a valid algorithm)

## Connection to Module 4 (Python)

Session 9 prepares you for actual programming:

| Session 9 Concept | Python Equivalent |
|-------------------|-------------------|
| Flowchart diamond | `if/else` statement |
| `WHILE condition DO` | `while condition:` |
| `FOR i FROM 1 TO 10` | `for i in range(1, 11):` |
| `READ x` | `x = input()` |
| `WRITE result` | `print(result)` |
| `x ← 5` | `x = 5` |

## Learning Outcomes

After reading these articles, you'll be able to:

1. **Create flowcharts** using standard symbols correctly
2. **Write pseudocode** that is clear and structured
3. **Identify control structures** in any algorithm
4. **Translate** between flowcharts, pseudocode, and natural language
5. **Trace execution** step-by-step through algorithms
6. **Design algorithms** using both visual and textual approaches
7. **Prepare for coding** by having clear algorithm designs

## Practice Exercises

### Exercise 1: Flowchart Creation
Draw flowcharts for:
1. Calculate rectangle area (input: width, height; output: area)
2. Check if number is even or odd
3. Count from 10 down to 1, then say "Blast off!"
4. Find the minimum of three numbers

### Exercise 2: Pseudocode Writing
Write pseudocode for:
1. Calculate average of a list of numbers
2. Count how many positive numbers in a list
3. Simple search: check if a number exists in a list
4. Temperature converter (Fahrenheit to Celsius)

### Exercise 3: Translation Practice

**A) Natural Language → Flowchart**
```
Find the largest of three numbers:
1. Get three numbers
2. Assume first is largest
3. Compare with second, update if larger
4. Compare with third, update if larger
5. Display the largest
```
Draw the flowchart.

**B) Flowchart → Pseudocode**
Take the flowchart you drew and write the pseudocode.

**C) Pseudocode → Python**
```
IF score >= 60 THEN
    WRITE "Pass"
ELSE
    WRITE "Fail"
END IF
```
Convert to Python:
```python
if score >= 60:
    print("Pass")
else:
    print("Fail")
```

### Exercise 4: Control Structure Identification

Identify which structures are used:

**Recipe for making tea:**
- Boil water (sequence)
- Steep tea bag for 3 minutes (sequence with time)
- Add sugar if desired (selection)
- Serve (sequence)

**Washing dishes:**
- While there are dirty dishes (iteration)
  - Wash one dish (sequence)
- Put away clean dishes (sequence)

### Exercise 5: Complete Algorithm Design

**Problem**: "Find how many students passed (score >= 60) in a list of scores."

Do all steps:
1. IPO analysis (Session 7)
2. FIDEO check (Session 8)
3. Flowchart (Session 9)
4. Pseudocode (Session 9)
5. Trace with: [85, 55, 92, 60, 45, 78]

## Quick Reference

### Flowchart Symbols
| Symbol | Meaning | Use For |
|--------|---------|---------|
| ⬭ | Start/End | Beginning and termination |
| ⬜ | Process | Calculations, assignments |
| 🔷 | Decision | Yes/No questions |
| 🗄️ | Input/Output | Reading, displaying |
| ➡️ | Arrow | Flow direction |

### Pseudocode Keywords
| Keyword | Purpose | Example |
|---------|---------|---------|
| `BEGIN`/`END` | Program boundaries | `BEGIN ... END` |
| `READ` | Get input | `READ age` |
| `WRITE` | Display output | `WRITE "Hello"` |
| `←` | Assignment | `sum ← 0` |
| `IF...THEN` | Decision | `IF x > 0 THEN...` |
| `WHILE...DO` | Pre-test loop | `WHILE n < 10 DO...` |
| `FOR...TO` | Counted loop | `FOR i FROM 1 TO 5 DO...` |

### Common Patterns
| Task | Pattern |
|------|---------|
| Sum | `total ← 0`, then `total ← total + item` |
| Count | `count ← 0`, then `count ← count + 1` |
| Max | `max ← first`, then `IF item > max THEN max ← item` |
| Search | `FOR each item: IF item = target THEN found ← true` |
| Sort | Compare adjacent, swap if wrong order, repeat |

## Assessment Checklist

Before moving to Module 4 (Python), ensure you can:
- [ ] Draw a complete flowchart with all standard symbols
- [ ] Write clear pseudocode with proper structure
- [ ] Identify sequence, selection, and iteration in algorithms
- [ ] Translate a flowchart to pseudocode
- [ ] Translate pseudocode to Python
- [ ] Trace through an algorithm step-by-step
- [ ] Create both flowchart and pseudocode for: Sum, Max, Min, Sort, Search
- [ ] Explain when to use flowcharts vs. pseudocode

## Next Steps

After mastering flowcharts and pseudocode:
1. Review all exercises and ensure you can complete them independently
2. Practice with new problems not in the articles
3. Move to Module 4: Python Essentials
4. Translate your Session 9 algorithms into working Python code

---

*Session 9 provides the practical tools to express algorithms. Combined with Session 7 (analysis) and Session 8 (definition), you now have a complete algorithm design toolkit.*
