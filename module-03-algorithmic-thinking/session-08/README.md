# Session 8: What Is an Algorithm?

## Session Overview

Now that we understand how to analyze problems using IPO (Session 7), it's time to learn what makes a solution an **algorithm**. We'll define what an algorithm is, learn the FIDEO characteristics that every algorithm must have, and explore different types of algorithms and their applications.

## Key Learning Objectives

By the end of this session, you will be able to:

- **Define** what an algorithm is in the context of computing
- **Apply** the FIDEO framework to evaluate algorithm quality
- **Describe** simple algorithms in natural language
- **Identify** different algorithm types (search, sort, etc.)
- **Distinguish** between an algorithm and regular instructions
- **Recognize** multiple valid solutions to the same problem

## What Is an Algorithm?

### Simple Definition
An **algorithm** is a **finite set of clear, step-by-step instructions** to solve a problem or accomplish a task.

### Algorithm vs. Regular Instructions

**Regular Instructions (NOT an algorithm):**
```
How to Make Tea:
1. Boil some water
2. Add tea leaves
3. Wait a bit
4. Drink when ready
```
*Problems: "some" is vague, "a bit" is unclear, "when ready" is subjective*

**Algorithm Version:**
```
Algorithm: Make Black Tea
───────────────────────────
Input: 2 cups water, 1 tea bag, 1 teaspoon sugar (optional)

1. Pour 2 cups water into kettle
2. Heat water until it reaches 100°C (boiling)
3. Place tea bag in cup
4. Pour boiling water over tea bag
5. Wait exactly 3 minutes
6. Remove tea bag
7. If sugar desired, add 1 teaspoon and stir
8. Serve immediately

Output: 1 cup of brewed tea
```

### Key Differences
| Regular Instructions | Algorithm |
|---------------------|-----------|
| Vague descriptions | Precise steps |
| Subjective timing | Exact measurements |
| Assumes knowledge | Complete details |
| Missing inputs/outputs | Clearly defined |

## The FIDEO Framework

Every algorithm must satisfy **5 essential characteristics**. Remember **FIDEO**:

```
┌─────────────────────────────────────────────────────┐
│                    FIDEO CHECKLIST                  │
├─────────────────────────────────────────────────────┤
│                                                     │
│  F - FINITE      → Does it end?                    │
│  I - INPUT       → What data does it need?         │
│  D - DEFINITE    → Is every step crystal clear?    │
│  E - EFFECTIVE   → Can each step actually be done? │
│  O - OUTPUT      → What result does it produce?    │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### F - Finite (It Must End)
An algorithm must complete after a specific, finite number of steps.

**Good (Finite):**
```
Count from 1 to 10:
1. Set n = 1
2. Print n
3. If n = 10, stop
4. Set n = n + 1
5. Go back to step 2
```

**Bad (Infinite):**
```
Count forever:
1. Set n = 1
2. Print n
3. Set n = n + 1
4. Go back to step 2  ← Never stops!
```

### I - Input (It Accepts Data)
An algorithm clearly defines what data it works with (can be zero inputs).

**Examples:**
- **With Input**: Calculate area of rectangle (needs width and height)
- **Zero Input**: Get current time (reads from system clock)

### D - Definite (Every Step Is Clear)
Each step must be so precise that anyone (or any computer) can follow it without guessing.

**Vague:** "Add ingredients until it tastes good"
**Definite:** "Add 2 cups flour, 1 cup sugar, 2 eggs"

### E - Effective (Every Step Is Doable)
Each operation must be simple enough to be performed exactly.

**Ineffective:** "Read the user's mind"
**Effective:** "Ask the user to type their name"

### O - Output (It Produces a Result)
An algorithm must produce at least one well-defined output.

**Good:** Returns a calculated value, displays a result, saves data
**Bad:** Performs calculations but produces nothing usable

## Session Structure

### Part 1: Understanding Algorithms (30 minutes)

#### The Recipe Test
Convert these regular instructions into algorithms:

1. **Morning Routine**
   - Regular: "Wake up, get ready, leave"
   - Algorithm: Specific steps with times and measurements

2. **Finding the Largest Number**
   - Regular: "Look at numbers and pick the biggest"
   - Algorithm: Step-by-step comparison process

#### Algorithm Identification Practice
Determine if these are algorithms (check against FIDEO):

**Example 1:**
```
1. Set x = 1
2. While x > 0:
   - Print x
   - x = x + 1
```
*Answer: NOT an algorithm (infinite loop - fails FINITENESS)*

**Example 2:**
```
1. Get a number from user
2. If number > 0, print "positive"
3. If number < 0, print "negative"
4. Else print "zero"
```
*Answer: IS an algorithm (passes all FIDEO criteria)*

### Part 2: FIDEO Deep Dive (45 minutes)

#### Characteristic 1: Finiteness
**Test Question**: "Will this eventually stop on ALL possible inputs?"

**Common Mistake - Infinite Search:**
```
Find number in list:
1. Look at first item
2. If it's the target, done
3. Otherwise, look at next item
4. Go to step 2
```
*Problem: If target isn't in the list, never stops!*

**Fixed Version:**
```
Find number in list:
1. For each item in list:
   a. If item equals target, return "Found"
2. Return "Not found"  ← Now it always ends!
```

#### Characteristic 2: Input
**Test Question**: "What information does it need?"

**Zero Input Example:**
```
Algorithm: Get Current Day
Input: None (reads from system)
Process: Read system clock
Output: "Today is Monday"
```

**Multiple Input Example:**
```
Algorithm: Calculate Tip
Input: Bill amount ($50), Tip percentage (15%)
Process: Multiply bill by percentage/100
Output: Tip amount ($7.50)
```

#### Characteristic 3: Definiteness
**Test Question**: "Can a computer follow this exactly?"

**Indefinite**: "Sort the numbers somehow"
**Definite**: "Compare each pair, swap if out of order, repeat until sorted"

#### Characteristic 4: Effectiveness
**Test Question**: "Is each step possible?"

**Effective Operations:**
- Arithmetic: +, -, ×, ÷
- Comparisons: <, >, =
- Reading input, displaying output
- Basic data operations

**Ineffective Operations:**
- "Make everyone happy"
- "Solve world hunger"
- "Read the user's mind"

#### Characteristic 5: Output
**Test Question**: "What do we get at the end?"

**Good Output:**
- Single value (maximum number)
- Multiple values (min, max, average)
- Action result (file saved, email sent)
- Status message ("Login successful")

### Part 3: Types of Algorithms (30 minutes)

#### Search Algorithms
**Purpose**: Find data that matches criteria

**Example - Find Maximum:**
```
Algorithm: Find Maximum
Input: List of numbers
Process: Track largest seen, update when finding larger
Output: Maximum value
```

#### Sort Algorithms
**Purpose**: Arrange data in order

**Example - Simple Sort:**
```
Algorithm: Sort Numbers
Input: List of numbers
Process: Compare adjacent, swap if wrong order, repeat
Output: Sorted list (smallest to largest)
```

#### Calculation Algorithms
**Purpose**: Perform mathematical operations

**Example - Calculate Average:**
```
Algorithm: Calculate Average
Input: List of numbers
Process: Sum all numbers, divide by count
Output: Average value
```

#### Decision Algorithms
**Purpose**: Make choices based on conditions

**Example - Grade Calculator:**
```
Algorithm: Determine Grade
Input: Numeric score (0-100)
Process: Compare score to grade thresholds
Output: Letter grade (A, B, C, D, F)
```

### Part 4: Natural Language Descriptions (15 minutes)

#### Writing Algorithms in Plain English

Before using flowcharts or pseudocode, describe the algorithm naturally:

**Problem**: Find the oldest person in a group

**Natural Language Algorithm:**
```
1. Start with the first person's age as the "oldest so far"
2. Look at each remaining person's age one by one
3. If someone's age is greater than "oldest so far", update "oldest so far"
4. After checking everyone, "oldest so far" is the answer
5. Display the result
```

**Key Points:**
- Use clear, simple language
- Number the steps
- Be specific about actions
- Include input and output

## Practice Exercises

### Exercise 1: FIDEO Analysis
Analyze these procedures against the FIDEO criteria:

**A:**
```
1. Set total = 0
2. Add 5 to total
3. Add 3 to total
4. Display total
```

**B:**
```
1. Get a list of numbers
2. While there are numbers:
   - Add current number to sum
3. Display average
```

**C:**
```
1. Ask user for temperature
2. Convert to other scale
3. Show result
```

For each, identify which FIDEO criteria are met and which are violated.

### Exercise 2: Fix the Algorithm
Fix these non-algorithms to satisfy FIDEO:

**Problem 1:**
```
1. Keep adding numbers until you're done
2. Show the total
```

**Problem 2:**
```
1. Set x = 10
2. While x is not 0:
   - Print x
   - x = x + 1  // Oops!
```

### Exercise 3: Multiple Solutions
Find two different algorithms for this problem:

**"Given a list of numbers, find how many are positive."**

**Solution A (Count-up approach):**
- Start count at 0
- For each number, if positive, add 1 to count

**Solution B (Filter approach):**
- Remove all non-positive numbers
- Count how many remain

Both are valid algorithms - different approaches, same result!

### Exercise 4: Algorithm Classification
Classify these by type (Search, Sort, Calculation, Decision):

1. Find the cheapest product in a catalog
2. Arrange names alphabetically
3. Calculate sales tax on a purchase
4. Determine if a number is prime
5. Find the shortest route between two cities

## Required Reading

1. **[Algorithm Characteristics](./concepts/algorithm-characteristics.md)** - Complete FIDEO framework with examples and exercises
2. **[Algorithm Types](./concepts/algorithm-types.md)** - Different categories of algorithms and their uses
3. **[Algorithm Analysis](./concepts/algorithm-analysis.md)** - Understanding efficiency and correctness

## Key Takeaways

1. **FIDEO defines algorithms** - Finite, Input, Definite, Effective, Output
2. **Not all instructions are algorithms** - Must be precise and complete
3. **Multiple solutions exist** - Different algorithms can solve the same problem
4. **Natural language first** - Describe algorithms simply before formal notation
5. **Types matter** - Understanding categories helps choose the right approach

## Connection to Next Session

Session 8 answered: **"What is an algorithm and what makes it valid?"**

Session 9 will answer: **"How do we express algorithms clearly?"**

We'll learn two formal ways to describe algorithms:
1. **Flowcharts** - Visual diagrams (for seeing the flow)
2. **Pseudocode** - Structured text (for precise description)

## Assessment Checklist

Before moving to Session 9, ensure you can:
- [ ] Define "algorithm" in your own words
- [ ] List and explain all 5 FIDEO characteristics
- [ ] Identify whether a procedure is an algorithm
- [ ] Fix common FIDEO violations
- [ ] Describe a simple algorithm in natural language
- [ ] Identify algorithm types (search, sort, calculation, decision)
- [ ] Explain why FINITENESS is crucial

## Quick Reference

| Letter | Characteristic | Simple Definition | Test Question |
|--------|----------------|-------------------|---------------|
| **F** | Finiteness | It must end | "Will it eventually stop?" |
| **I** | Input | Accepts data | "What information does it need?" |
| **D** | Definiteness | Crystal clear | "Can a computer follow this exactly?" |
| **E** | Effectiveness | Actually doable | "Is each step possible?" |
| **O** | Output | Produces result | "What do we get at the end?" |

## Common Mistakes to Avoid

| Mistake | Why It's Wrong | How to Fix |
|---------|---------------|------------|
| Missing end condition | Infinite loop | Add clear stopping criteria |
| Vague steps | Can't be followed exactly | Use precise measurements |
| No output | No result produced | Always return/display something |
| Impossible steps | Can't actually be done | Break down into basic operations |
| Undefined inputs | Don't know what data is needed | List all inputs clearly |
