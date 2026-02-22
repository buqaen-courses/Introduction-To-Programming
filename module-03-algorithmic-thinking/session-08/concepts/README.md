# Session 8 Concepts: What Is an Algorithm?

This folder contains articles defining what makes a valid algorithm and exploring different algorithm types. These concepts build on Session 7's IPO analysis, showing you how to turn problem analysis into valid algorithmic solutions.

## Table of Contents

### Algorithm Fundamentals
- **📊 [Algorithm Characteristics](algorithm-characteristics.md)** - The FIDEO framework: what makes a valid algorithm

### Algorithm Classification
- **🗂️ [Algorithm Types](algorithm-types.md)** - Different categories of algorithms (search, sort, calculation, decision)

### Advanced Analysis (Optional)
- **🔍 [Algorithm Analysis](algorithm-analysis.md)** - Efficiency and performance analysis (for deeper understanding)

## Persian Translations

For Persian speakers:
- **📊 [ویژگی‌های الگوریتم](algorithm-characteristics_fa.md)** - Algorithm characteristics in Persian
- **🗂️ [انواع الگوریتم](algorithm-types_fa.md)** - Algorithm types in Persian
- **🔍 [تحلیل الگوریتم](algorithm-analysis_fa.md)** - Algorithm analysis in Persian

## Detailed Article Descriptions

### 📊 [Algorithm Characteristics](algorithm-characteristics.md) ⭐ PRIMARY READING
**The most important article in this module.**

Learn the FIDEO framework - the five essential characteristics every algorithm must have:
- **F** - Finiteness: Must end (no infinite loops)
- **I** - Input: Needs defined data (can be zero inputs)
- **D** - Definiteness: Clear, precise steps
- **E** - Effectiveness: Each step must be doable
- **O** - Output: Must produce a result

Includes:
- Recipe Test (algorithm vs. regular instructions)
- Real-world analogies (bus routes, vending machines, directions)
- Code examples in Python
- Common beginner mistakes
- Practice exercises

**Why read this?** This is the foundation. You cannot design valid algorithms without understanding FIDEO.

### 🗂️ [Algorithm Types](algorithm-types.md) ⭐ PRIMARY READING
Learn the different categories of algorithms and when to use each:

**Basic Algorithm Types:**
- **Search Algorithms**: Find data that matches criteria (find maximum, linear search)
- **Sort Algorithms**: Arrange data in order (bubble sort, selection sort)
- **Calculation Algorithms**: Perform mathematical operations (sum, average, factorial)
- **Decision Algorithms**: Make choices based on conditions (grade calculator, eligibility checker)

**Problem-Solving Approaches:**
- **Brute Force**: Try everything (simple but may be slow)
- **Greedy**: Make locally optimal choices
- **Divide and Conquer**: Break into smaller subproblems
- **Dynamic Programming**: Remember past results to avoid recalculation

**Why read this?** Understanding types helps you choose the right approach and recognize patterns in problems.

### 🔍 [Algorithm Analysis](algorithm-analysis.md) ADVANCED TOPIC
For students wanting deeper understanding:

- Big O notation
- Time complexity (how long algorithms take)
- Space complexity (how much memory they use)
- Comparing algorithm efficiency

**Why read this?** Optional for beginners, essential for advanced students planning to work on performance-critical systems.

## How to Use These Articles

### For Beginners (Recommended Path)
1. **Read Algorithm Characteristics** - Master FIDEO first
2. **Study Algorithm Types** - Learn to categorize algorithms
3. **Practice identifying** - Check procedures against FIDEO criteria
4. **Write natural language** - Describe algorithms before formal notation

### For Advanced Students
1. Complete beginner path above
2. Read Algorithm Analysis for efficiency understanding
3. Study different problem-solving approaches
4. Compare algorithm trade-offs

## Key Themes

### FIDEO Defines Validity
Not every set of instructions is an algorithm. FIDEO provides clear criteria to evaluate whether a solution is a valid algorithm.

### Types Guide Approach
Understanding algorithm types helps you:
- Choose the right strategy for a problem
- Recognize familiar patterns
- Apply known solutions to new problems
- Design more efficient solutions

### Multiple Solutions Exist
Many problems have multiple valid algorithmic solutions. Different approaches have different trade-offs (simplicity vs. efficiency).

## Prerequisites

These articles assume you've completed Session 7:
- Understanding of IPO framework
- Ability to analyze problems into input/process/output
- Knowledge of state management

## Connection to Session 9

Session 8 defines WHAT an algorithm is. Session 9 shows HOW to express it:

```
Problem → IPO Analysis (Session 7)
              ↓
     FIDEO-Compliant Algorithm (Session 8)
              ↓
     Natural Language Description
              ↓
     Flowchart (Visual) - Session 9
     Pseudocode (Textual) - Session 9
              ↓
     Python Code - Module 4
```

## Learning Outcomes

After reading these articles, you'll be able to:

1. **Define algorithm** precisely using FIDEO criteria
2. **Evaluate procedures** to determine if they're valid algorithms
3. **Fix invalid algorithms** by addressing FIDEO violations
4. **Classify algorithms** by type (search, sort, calculation, decision)
5. **Describe algorithms** in natural language
6. **Recognize multiple solutions** to the same problem

## Practice Exercises

### Exercise 1: FIDEO Check
Analyze these procedures. Which FIDEO criteria do they meet? Which do they violate?

**Procedure A:**
```
1. Set x = 1
2. While x > 0:
   - Print x
   - x = x + 1
```
*Analysis: Violates FINITENESS (infinite loop)*

**Procedure B:**
```
1. Get temperature
2. If temp > 30, print "Hot"
3. If temp < 10, print "Cold"
4. Else print "Mild"
```
*Analysis: Valid algorithm (passes all FIDEO)*

**Procedure C:**
```
1. Add ingredients until it tastes good
2. Cook until done
3. Serve
```
*Analysis: Violates DEFINITENESS ("tastes good", "done" are vague)*

### Exercise 2: Fix the Algorithm
Fix these violations:

**Problem**: Infinite loop
```
# Original
while x > 0:
    print(x)
    x = x + 1

# Fixed
while x <= 100:
    print(x)
    x = x + 1
```

**Problem**: Missing output
```
# Original
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    # No return!

# Fixed
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average  # Added output
```

### Exercise 3: Algorithm Classification
Classify these by type:

1. **Find the cheapest product in a catalog**
   - Type: Search Algorithm

2. **Arrange student names alphabetically**
   - Type: Sort Algorithm

3. **Calculate sales tax on a purchase**
   - Type: Calculation Algorithm

4. **Determine if a student passes based on grades**
   - Type: Decision Algorithm

5. **Find the shortest path between two cities**
   - Type: Search Algorithm (optimization variant)

### Exercise 4: Multiple Solutions
Find two different algorithms for: **"Count even numbers in a list"**

**Solution A (Direct Count):**
```
count = 0
for each number:
    if number is even:
        count = count + 1
return count
```

**Solution B (Filter then Count):**
```
even_numbers = filter(list, is_even)
return length(even_numbers)
```

Both are valid! Different approaches, same result.

## Quick Reference: FIDEO

| Letter | Characteristic | Test Question | Common Violation |
|--------|----------------|---------------|------------------|
| **F** | Finiteness | "Will it stop?" | Infinite loops |
| **I** | Input | "What data is needed?" | Undefined requirements |
| **D** | Definiteness | "Is every step clear?" | Vague instructions |
| **E** | Effectiveness | "Can each step be done?" | Impossible operations |
| **O** | Output | "What do we get?" | No result produced |

## Common Algorithm Types for Beginners

| Type | Purpose | Examples | Difficulty |
|------|---------|----------|------------|
| **Search** | Find data | Find max, find min, find specific | ⭐ Beginner |
| **Sort** | Arrange data | Bubble sort, selection sort | ⭐ Beginner |
| **Calculation** | Math operations | Sum, average, factorial | ⭐ Beginner |
| **Decision** | Make choices | Grade calculator, eligibility | ⭐ Beginner |
| **Count** | Tally matches | Count even, count passing | ⭐ Beginner |

## Assessment Checklist

Before moving to Session 9, ensure you can:
- [ ] Define "algorithm" in your own words
- [ ] List and explain all 5 FIDEO characteristics
- [ ] Identify whether a procedure is an algorithm
- [ ] Fix common FIDEO violations (infinite loops, vague steps)
- [ ] Classify algorithms by type (search, sort, calculation, decision)
- [ ] Describe a simple algorithm in natural language
- [ ] Explain why FINITENESS is the most critical characteristic

## Next Steps

After mastering FIDEO and algorithm types:
1. Move to Session 9 to learn flowcharts (visual expression)
2. Learn pseudocode (textual expression)
3. Practice translating between forms
4. Get ready for Module 4: Python implementation

---

*Session 8 provides the theoretical foundation. Session 9 provides the practical tools. Together they enable you to design and express valid algorithms.*
