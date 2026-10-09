# Session 14: Loops – while and for

## Session Overview

A program that runs each line exactly once can only do so much. Loops let a
block of code run many times, which is what turns a script into something that
can process a list of a thousand items instead of one. This session covers
`for` for walking a sequence, `while` for repeating until a condition changes,
and the two keywords that let you leave a loop early: `break` and `continue`.

## Key Learning Objectives

By the end of this session, you will be able to:

- **Write** `for` loops over ranges and sequences
- **Write** `while` loops with a guaranteed terminating condition
- **Use** `break` and `continue` to control loop flow
- **Choose** between `for` and `while` deliberately
- **Avoid** infinite loops and off-by-one errors
- **Trace** a loop iteration by iteration on paper

## Two Loops, Two Purposes

```
    for      "do this once per item in this sequence"
              knows ahead of time how many times

    while    "keep doing this while something is true"
              you do not know the count in advance
```

That is the whole distinction. If you know what you are iterating over, use
`for`. If you are repeating until the world changes, use `while`.

## The for Loop

```python
for i in range(5):
    print(i)
# 0 1 2 3 4      <- note: starts at 0, stops BEFORE 5

for name in ["Sara", "Ali", "Reza"]:
    print(name)
# Sara Ali Reza

for char in "Python":
    print(char)
# P y t h o n
```

`range(5)` produces five values: 0 through 4. This off-by-one behaviour is the
most common beginner surprise. `range(1, 6)` gives you 1 through 5.

## The while Loop

```python
count = 0
while count < 3:
    print(count)
    count += 1
# 0 1 2
```

The condition is checked **before** each iteration. If it is never false, the
loop never ends. This is the single most dangerous thing about `while`:

```python
# NEVER ENDS - count never changes
count = 0
while count < 3:
    print(count)
```

Fix it by making sure something inside the loop moves toward the condition
becoming false. If you are not sure how a `while` loop ends, use a `for` loop
instead.

## break and continue

```python
for i in range(10):
    if i == 5:
        break          # leave the loop entirely
    print(i)
# 0 1 2 3 4

for i in range(5):
    if i == 2:
        continue       # skip this iteration, keep going
    print(i)
# 0 1 3 4
```

One nuance worth knowing: `break` inside a loop that is inside another loop
only breaks the *inner* one.

## 📖 Detailed Concepts

| Topic | Description |
|-------|-------------|
| **🔁 [While Loops](concepts/while-loops.md)** | Condition-controlled repetition, and how to guarantee termination |
| **🔂 [For Loops](concepts/for-loops.md)** | `range()`, sequences, `enumerate()`, and common loop patterns |
| **🎛️ [Loop Control](concepts/loop-control.md)** | `break`, `continue`, the loop `else` clause, and nested loops |

All three have Persian translations. Read in order.

## Main Concepts

- **`for` iterates a sequence** a known number of times
- **`range(n)` yields 0 to n-1**, which is the off-by-one source
- **`while` repeats while a condition holds** and depends on you updating state
- **`break` exits the loop**; **`continue` skips to the next iteration**
- **`enumerate()`** gives you index and value together
- **Nested loops** multiply: two loops over 10 items means 100 iterations
- **Accumulator pattern**: initialise before the loop, update inside it

## Common Beginner Mistakes

| Mistake | Result |
|---------|--------|
| `while` condition that never changes | Infinite loop, or a frozen program |
| Forgetting `count += 1` | Same infinite loop, different code |
| `range(1, 10)` when you meant 1 through 10 | Misses the last item |
| Indenting the update line outside the loop | Infinite loop |
| Using `continue` when you meant `break` | Skips one item instead of exiting |
| Expecting a `for` over a `range` to include the upper bound | Off-by-one |

## Workshop Activities

1. **Multiplication table.** Ask for a number, print its 1-through-10 table using
   a `for` loop. Then rewrite the same output with a `while` loop and compare.
2. **Guessing game.** Pick a secret number 1 through 10. Loop until the user
   guesses correctly, and tell them after each attempt whether they were high
   or low.
3. **Repeat-until-valid input.** Ask for a number, and keep asking until the
   user actually types one. This is a `while` loop with a `try/except` inside —
   you will formalize it in Session 18.
4. **Trace by hand.** Take three loops from the board, write a table of the loop
   variable's value on each iteration, then run them to check.

## Homework

- **Loop patterns**: print even numbers, count down to zero, and print a
  triangle of stars.
- **Trace exercises**: for four loops, show the value of every variable at each
  iteration as a table.
- **Small programs**: sum the first N squares, compute a factorial, and find
  the first number divisible by both 3 and 7 above 100.
- **Conversion challenge**: rewrite three of your Session 12 programs using a
  loop instead of repetition.

## Key Takeaways

- `for` when you know the sequence, `while` when you do not.
- `range(n)` stops before `n`. This is not an error.
- Every `while` loop must change something that moves toward termination.
- `break` exits; `continue` skips. Choosing the wrong one is easy and quiet.
- Nested loops multiply, so a small mistake becomes an expensive one.

## Connection to Next Session

You can now repeat work over a fixed count. [Session 15: Working with
Strings](../session-15/README.md) applies all of this to text: indexing,
slicing, methods, and building formatted output you would be happy to show
someone.

**Required Reading**: the three concept articles listed above. Start with
[While Loops](concepts/while-loops.md), since infinite loops are the concept
worth understanding before you write any of them.

Also see the standalone loop workshop notes in
[`Workshops/`](../../Workshops/README.md) for extra practice problems.