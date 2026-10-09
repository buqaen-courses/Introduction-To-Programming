# Session 9: Expressing Algorithms - Flowcharts and Pseudocode

## Session Overview

Now that we understand what algorithms are (Session 8), we need to learn how to express them clearly. This session covers two fundamental ways to describe algorithms: **flowcharts** (visual diagrams) and **pseudocode** (structured text). We'll also learn the three basic control structures that form the building blocks of all algorithms.

## Key Learning Objectives

By the end of this session, you will be able to:

- **Create** flowcharts using standard symbols for visual algorithm representation
- **Write** clear pseudocode that describes algorithm logic precisely
- **Translate** between flowcharts, pseudocode, and natural language descriptions
- **Apply** the three control structures: sequence, selection, and iteration
- **Trace** algorithm execution step-by-step using both representations
- **Design** simple algorithms using both visual and textual approaches

## Why Two Ways to Express Algorithms?

Different representations serve different purposes:

| Representation | Best For | Strengths |
|----------------|----------|-----------|
| **Flowchart** | Visual learners, seeing flow | Easy to trace execution, spot logic errors |
| **Pseudocode** | Detailed logic, implementation | Precise, language-independent, easy to modify |
| **Natural Language** | Initial understanding | Accessible to everyone |

**The Process**: Natural Language → Flowchart → Pseudocode → Actual Code

## Session Structure

### Part 1: Flowcharts - Visual Algorithm Design (45 minutes)

#### Flowchart Symbols

Every flowchart uses standard symbols:

| Symbol | Name | Purpose |
|--------|------|---------|
| ⬭ | **Terminator** (Oval) | Start and End points |
| ⬜ | **Process** (Rectangle) | Actions, calculations, assignments |
| 🔷 | **Decision** (Diamond) | Yes/No questions, conditions |
| 🗄️ | **Input/Output** (Parallelogram) | Reading input or displaying output |
| ➡️ | **Flow Line** (Arrow) | Direction of execution |

#### Four Fundamental Algorithms with Flowcharts

**Algorithm 1: Sum Numbers**
```
Problem: Given a list of numbers, calculate their total.

Flowchart Logic:
START → Read List → Set sum=0 → For each number: Add to sum → Display sum → END
```

**Algorithm 2: Find Maximum**
```
Problem: Find the largest number in a list.

Flowchart Logic:
START → Read List → Set max=first number → For each remaining:
            ↓ Is current > max? → YES: update max
            ↓ NO: continue
Display max → END
```

**Algorithm 3: Find Minimum**
```
Problem: Find the smallest number in a list.

Flowchart Logic:
Similar to Maximum, but checks "Is current < min?"
```

**Algorithm 4: Simple Sort (Bubble Sort)**
```
Problem: Arrange numbers from smallest to largest.

Flowchart Logic:
START → Read List → Repeat until no swaps:
            ↓ For each adjacent pair:
            ↓ Is left > right? → YES: swap them
Display sorted list → END
```

#### Flowchart Best Practices
1. **Keep it simple**: One flowchart per algorithm
2. **Use standard symbols**: Don't invent new shapes
3. **Clear flow direction**: Generally top-to-bottom
4. **Label decision exits**: Always Yes/No or True/False
5. **Trace before finalizing**: Test with sample data

### Part 2: Pseudocode - Structured Text (45 minutes)

#### What is Pseudocode?
Pseudocode is a detailed description of an algorithm using a mix of natural language and programming-like constructs. It's designed to be readable by humans while precise enough to translate into any programming language.

#### Basic Pseudocode Elements

**Variables and Assignment:**
```
SET variable_name TO value
sum ← 0
count ← count + 1
```

**Input/Output:**
```
READ variable_name
WRITE "message" OR variable_name
DISPLAY result
```

**Mathematical Operations:**
```
result ← a + b
product ← x × y
quotient ← a / b
remainder ← a MOD b
```

#### Control Structures in Pseudocode

**1. Sequence (Do things in order):**
```
Step 1: Read number1
Step 2: Read number2
Step 3: sum ← number1 + number2
Step 4: WRITE "Sum is: " + sum
```

**2. Selection (Make decisions):**
```
IF condition THEN
    statement(s)
ELSE
    statement(s)
END IF
```

**3. Iteration (Repeat actions):**
```
WHILE condition DO
    statement(s)
END WHILE

FOR counter FROM start TO end DO
    statement(s)
END FOR
```

#### Pseudocode Examples

**Example 1: Sum Numbers**
```
ALGORITHM SumNumbers
    DECLARE numbers AS ARRAY OF INTEGER
    DECLARE sum, i AS INTEGER
    
    sum ← 0
    
    FOR i FROM 0 TO LENGTH(numbers) - 1 DO
        sum ← sum + numbers[i]
    END FOR
    
    WRITE "Sum is: " + sum
END ALGORITHM
```

**Example 2: Find Maximum**
```
ALGORITHM FindMaximum
    DECLARE numbers AS ARRAY OF INTEGER
    DECLARE max, i AS INTEGER
    
    max ← numbers[0]
    
    FOR i FROM 1 TO LENGTH(numbers) - 1 DO
        IF numbers[i] > max THEN
            max ← numbers[i]
        END IF
    END FOR
    
    WRITE "Maximum is: " + max
END ALGORITHM
```

### Part 3: Control Structures Deep Dive (30 minutes)

#### The Three Fundamental Structures

All algorithms, no matter how complex, are built from three basic structures:

**1. Sequence (Straight Line)**
- Execute steps in order, one after another
- No branching or repetition
- Foundation of all algorithms

```
Flowchart:     Pseudocode:
⬭             BEGIN
 ↓              READ name
⬜              READ age
 ↓              year ← 2024 - age
⬜              WRITE name + " was born around " + year
 ↓            END
⬭
```

**2. Selection (Decision Making)**
- Choose between paths based on conditions
- Types: Simple IF, IF-ELSE, Multiple IF-ELSEIF

```
Flowchart:               Pseudocode:
    🔷 IF score >= 90 THEN
   /  \    grade ← "A"
 YES  NO ELSE IF score >= 80 THEN
  ↓    ↓     grade ← "B"
⬜   ⬜  ELSE IF score >= 70 THEN
            grade ← "C"
  \  /    ELSE
   ↓         grade ← "F"
        END IF
```

**3. Iteration (Looping)**
- Repeat actions multiple times
- Types: WHILE (pre-test), REPEAT-UNTIL (post-test), FOR (counted)

```
Flowchart:               Pseudocode:
   ⬜ counter ← 1
    ↓
   🔷 WHILE counter <= 10 DO
   /  \    WRITE counter
  YES  NO   counter ← counter + 1
  ↓        END WHILE
⬜
↓ (loop back)
```

#### Combining Structures

Real algorithms combine all three:

**Example: Calculate Average of Positive Numbers Only**
```
ALGORITHM AveragePositive
    DECLARE numbers AS ARRAY OF INTEGER
    DECLARE sum, count, i AS INTEGER
    DECLARE average AS REAL
    
    sum ← 0
    count ← 0
    
    FOR i FROM 0 TO LENGTH(numbers) - 1 DO
        IF numbers[i] > 0 THEN          // Selection inside Iteration
            sum ← sum + numbers[i]
            count ← count + 1
        END IF
    END FOR
    
    IF count > 0 THEN                   // Selection for output
        average ← sum / count
        WRITE "Average of positive numbers: " + average
    ELSE
        WRITE "No positive numbers found"
    END IF
END ALGORITHM
```

### Part 4: Translation Practice (30 minutes)

#### Natural Language → Flowchart

**Natural Language:**
```
Find the largest of three numbers:
1. Get three numbers
2. Assume first is largest
3. Compare with second, update if larger
4. Compare with third, update if larger
5. Display the largest
```

**Flowchart Steps:**
- Oval (Start)
- Parallelogram (Input: num1, num2, num3)
- Rectangle (max ← num1)
- Diamond (num2 > max?) → Rectangle or bypass
- Diamond (num3 > max?) → Rectangle or bypass
- Parallelogram (Output: max)
- Oval (End)

#### Flowchart → Pseudocode

Trace the flowchart and write matching pseudocode:
- Terminators → BEGIN/END
- Rectangles → Assignment statements
- Diamonds → IF statements
- Parallelograms → READ/WRITE
- Arrows → Sequential flow

#### Pseudocode → Code

The structure is nearly identical across languages:

| Pseudocode | Python | JavaScript |
|------------|--------|------------|
| `IF x > y THEN` | `if x > y:` | `if (x > y) {` |
| `WHILE n < 10 DO` | `while n < 10:` | `while (n < 10) {` |
| `FOR i FROM 1 TO 5` | `for i in range(1, 6):` | `for (let i = 1; i <= 5; i++) {` |
| `sum ← sum + x` | `sum = sum + x` | `sum = sum + x;` |

## The Complete Algorithm Design Process

```
┌─────────────────────────────────────────────────────────────────┐
│                     ALGORITHM DESIGN FLOW                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. PROBLEM UNDERSTANDING                                       │
│     └─ Read and understand what needs to be solved              │
│                                                                 │
│  2. IPO ANALYSIS (Session 7)                                    │
│     ├─ Input: What data do we need?                             │
│     ├─ Process: What operations?                              │
│     └─ Output: What result?                                     │
│                                                                 │
│  3. NATURAL LANGUAGE DESCRIPTION (Session 8)                    │
│     └─ Write steps in plain English                             │
│         "1. Get the numbers. 2. Add them up. 3. Show result."   │
│                                                                 │
│  4. CREATE FLOWCHART (Session 9 - This Session!)                │
│     └─ Draw visual diagram with symbols                         │
│                                                                 │
│  5. WRITE PSEUDOCODE (Session 9 - This Session!)                │
│     └─ Convert to structured text                               │
│                                                                 │
│  6. IMPLEMENT IN CODE (Module 4)                                │
│     └─ Translate to Python or other language                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Practice Exercises

### Exercise 1: Flowchart Creation
Draw flowcharts for these problems:

1. **Calculate Rectangle Area**
   - Input: Width and height
   - Process: Multiply width × height
   - Output: Area

2. **Check Even or Odd**
   - Input: A number
   - Process: Check if divisible by 2
   - Output: "Even" or "Odd"

3. **Countdown from 10**
   - Input: None
   - Process: Count from 10 down to 1
   - Output: Each number, then "Blast off!"

### Exercise 2: Pseudocode Writing
Write pseudocode for:

1. **Find Minimum** (similar to maximum but find smallest)
2. **Calculate Average** of a list of numbers
3. **Simple Search** - check if a number exists in a list

### Exercise 3: Translation Practice

**Given this flowchart logic:**
```
START → Read score → Is score >= 60? → YES: "Pass" → END
                              ↓
                              NO: "Fail" → END
```

**A)** Write the pseudocode
**B)** Trace through with score = 75
**C)** Trace through with score = 45

### Exercise 4: Complete Algorithm Design

**Problem**: "Given a list of test scores, find how many are passing (>= 60)."

**Do all steps:**
1. IPO analysis
2. Natural language description
3. Flowchart (draw or describe)
4. Pseudocode
5. Trace with: [85, 55, 92, 60, 45, 78]

### Exercise 5: Control Structures Identification

Identify which control structures are used in:

**A)** Making a sandwich
**B)** Washing dishes until all are clean
**C)** Choosing what to wear based on weather
**D)** Counting attendance in a classroom

## Required Reading

1. **[Flowchart Fundamentals](./concepts/flowchart-fundamentals.md)** - Visual algorithm representation with 4 complete examples
2. **[Pseudocode Fundamentals](./concepts/pseudocode-fundamentals.md)** - Structured text syntax and examples
3. **[Control Structures](./concepts/control-structures.md)** - Deep dive into sequence, selection, and iteration
4. **[Pseudocode to Code](./concepts/pseudocode-to-code.md)** - Translating to actual programming languages

## Key Takeaways

1. **Two ways to express algorithms**: Flowcharts (visual) and Pseudocode (textual)
2. **Three control structures**: Sequence, Selection, Iteration - all algorithms use these
3. **Process**: Natural Language → Flowchart → Pseudocode → Code
4. **Trace before coding**: Test your algorithm with sample data first
5. **Symbols matter**: Learn and use standard flowchart symbols consistently

## Assessment Checklist

Before moving to Module 4 (Python), ensure you can:
- [ ] Draw flowcharts using standard symbols correctly
- [ ] Write pseudocode for simple algorithms
- [ ] Translate between flowcharts and pseudocode
- [ ] Identify sequence, selection, and iteration in algorithms
- [ ] Trace through an algorithm step-by-step
- [ ] Describe the complete algorithm design process
- [ ] Create both flowchart and pseudocode for: Sum, Max, Min, Sort, Search

## Quick Reference

### Flowchart Symbols
- ⬭ Oval: Start/End
- ⬜ Rectangle: Process/Action
- 🔷 Diamond: Decision (Yes/No)
- 🗄️ Parallelogram: Input/Output
- ➡️ Arrow: Flow direction

### Pseudocode Keywords
- `READ`, `WRITE`, `DISPLAY` - I/O
- `←` or `SET` - Assignment
- `IF...THEN...ELSE...END IF` - Decision
- `WHILE...DO...END WHILE` - Pre-test loop
- `FOR...FROM...TO...DO...END FOR` - Counted loop
- `BEGIN`/`END` or `ALGORITHM`/`END ALGORITHM` - Program boundaries

### Common Algorithm Patterns
| Task | Pattern |
|------|---------|
| Sum | Start at 0, add each item |
| Count | Start at 0, increment when condition met |
| Max/Min | Track current best, update when better found |
| Search | Check each item, stop when found |
| Sort | Compare and swap adjacent items |
