# Flowchart Fundamentals: Visual Algorithm Design

## What is a Flowchart?

A flowchart is a visual representation of an algorithm using standard symbols connected by arrows. It shows the flow of execution from start to finish, making it easy to understand the logic at a glance.

### Why Use Flowcharts?

- **Visual clarity**: See the algorithm's structure immediately
- **Easy to follow**: Follow the arrows to trace execution
- **Spot errors quickly**: Visual representation reveals logic flaws
- **Universal language**: Symbols are understood worldwide
- **Planning tool**: Design before writing code

---

## Flowchart Symbols

| Symbol | Name | Purpose |
|--------|------|---------|
| ⬭ | Oval (Terminator) | Start and End points |
| ⬜ | Rectangle (Process) | Actions, calculations, assignments |
| 🔷 | Diamond (Decision) | Yes/No questions, conditions |
| 🗄️ | Parallelogram (Input/Output) | Reading input or displaying output |
| ➡️ | Arrow (Flow Line) | Direction of execution |
| ○ | Circle (Connector) | Links to another part of the flowchart |

---

## Algorithm 1: Sum a List of Numbers

### The Problem
Given a list of numbers, calculate their total sum.

### Step-by-Step Thinking
1. Start the program
2. Get the list of numbers
3. Start with sum = 0 (we haven't added anything yet)
4. Look at each number one by one
5. Add each number to our running sum
6. When all numbers are processed, display the result
7. End the program

### Flowchart (ASCII Representation)

```
                    +-------------+
                    |    START    |
                    +------+------+
                           |
                           v
                    +-------------+
                    |  Read list  |
                    | of numbers  |
                    +------+------+
                           |
                           v
                    +-------------+
                    | Set sum = 0 |
                    +------+------+
                           |
                           v
                    +-------------+
                    | Set index   |
                    |    = 0      |
                    +------+------+
                           |
                           v
              +----------------------+
              |  Are there more      |----NO---->
              |  numbers to check?   |          |
              +----------+-----------+          |
                         | YES                  |
                         v                      |
                  +-------------+                |
                  | Add current |                |
                  | number to   |                |
                  |    sum      |                |
                  +------+------+                |
                         |                       |
                         v                       |
                  +-------------+                |
                  | Move to     |                |
                  | next number |                |
                  +------+------+                |
                         |                       |
                         +-----------------------+
                                                 |
                                                 v
                                          +-------------+
                                          |  Display  |
                                          |  sum      |
                                          +------+------+
                                                 |
                                                 v
                                          +-------------+
                                          |    END     |
                                          +-------------+
```

### Pseudocode
```
ALGORITHM SumNumbers
    // Calculate sum of a list of numbers
    
    DECLARE numbers AS ARRAY OF INTEGER
    DECLARE sum, i AS INTEGER
    
    sum ← 0
    
    FOR each number IN numbers DO
        sum ← sum + number
    END FOR
    
    WRITE "Sum is: " + sum
END ALGORITHM
```

### Example Walkthrough
**Input**: [5, 3, 8, 2]

| Step | Action | sum value |
|------|--------|-----------|
| 1 | Start with sum = 0 | 0 |
| 2 | Add 5 | 5 |
| 3 | Add 3 | 8 |
| 4 | Add 8 | 16 |
| 5 | Add 2 | 18 |
| 6 | Display result | 18 |

**Output**: 18

---

## Algorithm 2: Find the Maximum Number

### The Problem
Given a list of numbers, find the largest one.

### Step-by-Step Thinking
1. Start the program
2. Get the list of numbers
3. Assume the first number is the maximum (it's the largest we've seen so far)
4. Look at each remaining number
5. If a number is bigger than our current maximum, update maximum
6. When all numbers are checked, display the maximum
7. End the program

### Flowchart (ASCII Representation)

```
                    +-------------+
                    |    START    |
                    +------+------+
                           |
                           v
                    +-------------+
                    |  Read list  |
                    | of numbers  |
                    +------+------+
                           |
                           v
                    +-------------+
                    | Set max =   |
                    | first number|
                    +------+------+
                           |
                           v
                    +-------------+
                    | Set index   |
                    |   = 1       |
                    +------+------+
                           |
                           v
              +----------------------+
              |  Are there more      |----NO---->
              |  numbers to check?   |          |
              +----------+-----------+          |
                         | YES                  |
                         v                      |
              +----------------------+          |
              | Is current number    |            |
              | > max?               |---NO------>|
              +----------+-----------+            |
                         | YES                  |
                         v                      |
                  +-------------+               |
                  | Update max  |               |
                  | to current  |               |
                  |   number    |               |
                  +------+------+               |
                         |                      |
                         +----------------------
                                                 |
                                                 v
                                          +-------------+
                                          |  Display  |
                                          |    max    |
                                          +------+------+
                                                 |
                                                 v
                                          +-------------+
                                          |    END     |
                                          +-------------+
```

### Pseudocode
```
ALGORITHM FindMaximum
    // Find the largest number in a list
    
    DECLARE numbers AS ARRAY OF INTEGER
    DECLARE max, i AS INTEGER
    
    max ← numbers[0]  // Assume first is largest
    
    FOR i FROM 1 TO LENGTH(numbers) - 1 DO
        IF numbers[i] > max THEN
            max ← numbers[i]  // Found a bigger one!
        END IF
    END FOR
    
    WRITE "Maximum is: " + max
END ALGORITHM
```

### Example Walkthrough
**Input**: [12, 5, 27, 8, 15]

| Step | Action | max value |
|------|--------|-----------|
| 1 | Start with max = 12 | 12 |
| 2 | 5 > 12? No, keep 12 | 12 |
| 3 | 27 > 12? Yes! Update | 27 |
| 4 | 8 > 27? No, keep 27 | 27 |
| 5 | 15 > 27? No, keep 27 | 27 |
| 6 | Display result | 27 |

**Output**: 27

---

## Algorithm 3: Find the Minimum Number

### The Problem
Given a list of numbers, find the smallest one.

### Step-by-Step Thinking
1. Start the program
2. Get the list of numbers
3. Assume the first number is the minimum (it's the smallest we've seen so far)
4. Look at each remaining number
5. If a number is smaller than our current minimum, update minimum
6. When all numbers are checked, display the minimum
7. End the program

### Flowchart (ASCII Representation)

```
                    +-------------+
                    |    START    |
                    +------+------+
                           |
                           v
                    +-------------+
                    |  Read list  |
                    | of numbers  |
                    +------+------+
                           |
                           v
                    +-------------+
                    | Set min =   |
                    | first number|
                    +------+------+
                           |
                           v
                    +-------------+
                    | Set index   |
                    |   = 1       |
                    +------+------+
                           |
                           v
              +----------------------+
              |  Are there more      |----NO---->
              |  numbers to check?   |          |
              +----------+-----------+          |
                         | YES                  |
                         v                      |
              +----------------------+          |
              | Is current number    |            |
              | < min?               |---NO------>|
              +----------+-----------+            |
                         | YES                  |
                         v                      |
                  +-------------+               |
                  | Update min  |               |
                  | to current  |               |
                  |   number    |               |
                  +------+------+               |
                         |                      |
                         +----------------------
                                                 |
                                                 v
                                          +-------------+
                                          |  Display  |
                                          |    min    |
                                          +------+------+
                                                 |
                                                 v
                                          +-------------+
                                          |    END     |
                                          +-------------+
```

### Pseudocode
```
ALGORITHM FindMinimum
    // Find the smallest number in a list
    
    DECLARE numbers AS ARRAY OF INTEGER
    DECLARE min, i AS INTEGER
    
    min ← numbers[0]  // Assume first is smallest
    
    FOR i FROM 1 TO LENGTH(numbers) - 1 DO
        IF numbers[i] < min THEN
            min ← numbers[i]  // Found a smaller one!
        END IF
    END FOR
    
    WRITE "Minimum is: " + min
END ALGORITHM
```

### Example Walkthrough
**Input**: [34, 12, 56, 8, 23]

| Step | Action | min value |
|------|--------|-----------|
| 1 | Start with min = 34 | 34 |
| 2 | 12 < 34? Yes! Update | 12 |
| 3 | 56 < 12? No, keep 12 | 12 |
| 4 | 8 < 12? Yes! Update | 8 |
| 5 | 23 < 8? No, keep 8 | 8 |
| 6 | Display result | 8 |

**Output**: 8

---

## Algorithm 4: Simple Sort (Bubble Sort)

### The Problem
Given a list of numbers, arrange them from smallest to largest.

### The Idea
Compare adjacent numbers. If they're in the wrong order, swap them. Repeat until no more swaps are needed.

### Step-by-Step Thinking
1. Start the program
2. Get the list of numbers
3. Look at each pair of adjacent numbers
4. If a pair is out of order (bigger first), swap them
5. Repeat the process until no swaps happen in a complete pass
6. The list is now sorted
7. Display the sorted list
8. End the program

### Flowchart (ASCII Representation)

```
                    +-------------+
                    |    START    |
                    +------+------+
                           |
                           v
                    +-------------+
                    |  Read list  |
                    | of numbers  |
                    +------+------+
                           |
                           v
              +----------------------+
              |  Set swapped = true  |
              +----------+-----------+
                         |
                         v
              +----------------------+
              | swapped = true?      |----NO---->
              +----------+-----------+          |
                         | YES                 |
                         v                     |
              +----------------------+         |
              | Set swapped = false  |         |
              +----------+-----------+         |
                         |                    |
                         v                    |
              +----------------------+         |
              | Set index = 0      |         |
              +----------+-----------+         |
                         |                    |
                         v                    |
    +--------------------+-----------------+   |
    | index < length - 1?                |   |
    +----------+-------------+-------------+   |
               | NO              | YES       |
               |                 v           |
               |    +--------------------+  |
               |    | Is numbers[index]  |  |
               |    | > numbers[index+1]?|  |
               |    +--------+-----------+  |
               |              | YES  | NO   |
               |              v       |      |
               |    +-------------+  |      |
               |    | Swap the two|  |      |
               |    |  numbers    |  |      |
               |    |             |  |      |
               |    | Set swapped |  |      |
               |    |   = true    |  |      |
               |    +------+------+  |      |
               |           |         |      |
               |           +---------+      |
               |                 |         |
               |                 v         |
               |    +----------------+    |
               |    | index = index + 1|    |
               |    +--------+-----------+   |
               |              |             |
               +--------------+             |
                                            |
                                            v
                                     +-------------+
                                     |  Display  |
                                     |  sorted   |
                                     |   list    |
                                     +------+------+
                                            |
                                            v
                                     +-------------+
                                     |    END     |
                                     +-------------+
```

### Pseudocode
```
ALGORITHM SimpleSort
    // Sort numbers from smallest to largest
    
    DECLARE numbers AS ARRAY OF INTEGER
    DECLARE i, temp AS INTEGER
    DECLARE swapped AS BOOLEAN
    DECLARE n AS INTEGER
    
    n ← LENGTH(numbers)
    swapped ← TRUE
    
    WHILE swapped = TRUE DO
        swapped ← FALSE
        
        FOR i FROM 0 TO n-2 DO
            IF numbers[i] > numbers[i+1] THEN
                // Swap the two numbers
                temp ← numbers[i]
                numbers[i] ← numbers[i+1]
                numbers[i+1] ← temp
                swapped ← TRUE
            END IF
        END FOR
    END WHILE
    
    WRITE "Sorted list: " + numbers
END ALGORITHM
```

### Example Walkthrough
**Input**: [5, 2, 8, 1]

**Pass 1:**
- Compare 5 and 2: 5 > 2? Yes! Swap → [2, 5, 8, 1]
- Compare 5 and 8: 5 > 8? No → [2, 5, 8, 1]
- Compare 8 and 1: 8 > 1? Yes! Swap → [2, 5, 1, 8]

**Pass 2:**
- Compare 2 and 5: 2 > 5? No → [2, 5, 1, 8]
- Compare 5 and 1: 5 > 1? Yes! Swap → [2, 1, 5, 8]
- Compare 5 and 8: 5 > 8? No → [2, 1, 5, 8]

**Pass 3:**
- Compare 2 and 1: 2 > 1? Yes! Swap → [1, 2, 5, 8]
- Compare 2 and 5: 2 > 5? No → [1, 2, 5, 8]
- Compare 5 and 8: 5 > 8? No → [1, 2, 5, 8]

**Pass 4:**
- No swaps! The list is sorted.

**Output**: [1, 2, 5, 8]

---

## Flowchart Best Practices

### 1. Keep It Simple
- One flowchart per algorithm
- Clear, simple labels
- Avoid clutter

### 2. Standard Symbols
- Use proper symbols consistently
- Don't invent new shapes
- Follow the convention

### 3. Flow Direction
- Generally top to bottom
- Left to right for branches
- Clear arrow directions

### 4. Decision Diamonds
- Always two exits (Yes/No, True/False)
- Label the exits clearly
- Only one question per diamond

### 5. Testing Your Flowchart
- Trace through with sample data
- Check all paths (Yes and No branches)
- Verify the output is correct

---

## Common Mistakes to Avoid

| Mistake | Why It's Wrong | How to Fix |
|---------|---------------|------------|
| Missing START/END | Every algorithm needs them | Always include ovals at both ends |
| Unclear arrows | Don't know the flow direction | Label arrows or use clear paths |
| Missing decisions | Logic errors | Add diamonds for all conditions |
| Too much in one box | Makes it confusing | Break into smaller steps |
| No input/output | Don't know what goes in/out | Use parallelograms for I/O |

---

## Practice Exercises

### Exercise 1: Count Numbers
Create a flowchart that counts how many numbers are in a list.

**Hint**: Similar to sum, but increment a counter instead of adding.

### Exercise 2: Find Average
Create a flowchart that calculates the average of a list of numbers.

**Hint**: Sum the numbers first, then divide by the count.

### Exercise 3: Check If Number Exists
Create a flowchart that checks if a specific number exists in a list.

**Hint**: Stop early if you find it (this is called a linear search).

---

## From Flowchart to Code

### Flowchart → Pseudocode → Python

**Flowchart Step**: Rectangle "Set sum = 0"

**Pseudocode**: `sum ← 0`

**Python**: `sum = 0`

**Flowchart Step**: Diamond "Is number > max?"

**Pseudocode**: 
```
IF number > max THEN
    max ← number
END IF
```

**Python**:
```python
if number > max:
    max = number
```

---

## Summary

### Key Takeaways

1. **Flowcharts are visual algorithms**: Pictures that show program logic
2. **Standard symbols**: Ovals, rectangles, diamonds, parallelograms
3. **Three basic patterns**:
   - **Sequence**: Steps in order (rectangle after rectangle)
   - **Decision**: Yes/No branches (diamond with two exits)
   - **Loop**: Repeat steps (arrow back to earlier step)
4. **Always trace through**: Test with sample data before coding
5. **Flowchart → Pseudocode → Code**: A three-step design process

### Algorithm Patterns You Learned

| Algorithm | Core Idea |
|-----------|-----------|
| Sum | Start at 0, add each number |
| Max | Track the biggest seen so far |
| Min | Track the smallest seen so far |
| Sort | Compare neighbors, swap if wrong order |

---

## Quick Reference Card

```
SYMBOLS:
⬭  Start / End
⬜  Process (do something)
🔷  Decision (yes/no question)
🗄️  Input / Output
➡️  Flow direction

LOOP PATTERN:
    ⬭
    |
    v
   ⬜ (initialize)
    |
    v
   🔷 <--< (check condition)
   /  \
 YES    NO
  |      |
  v      v
 ⬜      ⬜ (end)
  |      |
  +------+
  (loop back)

DECISION PATTERN:
       🔷
      /  \
   YES    NO
    |      |
    v      v
   ⬜      ⬜
    |      |
    +------+
       |
       v
```

Remember: **Think first, draw second, code third!**
