# Session 13: Decision Making with if, elif, else

## Session Overview

Every program so far runs the same way every time. This session is where a
program starts behaving differently depending on its data. We translate the
selection control structure from Session 9 into Python, meet Python's boolean
logic (`and`, `or`, `not`) and its truthiness rules, and then nest conditionals
to handle decisions that depend on other decisions.

## Key Learning Objectives

By the end of this session, you will be able to:

- **Write** `if`, `if/else`, and `if/elif/else` statements correctly
- **Use** comparison operators to build conditions
- **Combine** conditions with `and`, `or`, and `not`
- **Predict** which branch runs for a given input
- **Nest** conditionals and know when to stop nesting
- **Debug** indentation and logic errors in conditionals

## Two-Way Then Many-Way

The basic shape, then the extension:

```python
# one way
if score >= 60:
    print("Pass")

# two ways
if score >= 60:
    print("Pass")
else:
    print("Fail")

# many ways
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```

`elif` is short for "else if". Only the **first** matching branch runs, then
Python skips straight past the rest. That is why the order matters: put the
strictest condition first, or a score of 95 will match `>= 60` and never reach
the `A` branch.

## Python Is Not Indented by Accident

The indentation after `:` is not style. It is syntax. It defines the block.

```python
if score >= 60:
    print("Pass")
    print("Congratulations")   # same block, both run
print("Done")                  # different block, always runs
```

Mixing tabs and spaces, or indenting one line of a block differently, gives you
an `IndentationError` or silently changes which lines are in the block.

## Truthiness: Python's Rules

Conditions do not have to be `True` or `False`. Any value can be a condition,
and Python decides by these rules:

```
    FALSY  (treated as False)              TRUTHY  (treated as True)

    0                zero                  1            nonzero number
    0.0              zero float            -1           any nonzero number
    ""              empty string          "hi"         nonempty string
    ''              empty string          " "          whitespace string
    []              empty list            [0]          nonempty list
    {}              empty dict            {"k": None}  dict with a None value
    None            no value

    NOTE:  [0] is TRUTHY. A list containing zero is still a list,
           and the list is not empty.
```

That last row surprises people. `[0]` is a non-empty list, so it is truthy, even
though the item inside it is falsy.

## Combining Conditions

```
    and    both sides must be true
    or     at least one side must be true
    not    flips the truth value

    age >= 18 and has_id          both required
    score > 90 or bonus > 50      either is enough
    not is_expired               inverts
```

A common bug is writing `18 <= age <= 65` — which is valid and correct — versus
`18 <= age and age <= 65`, which is the same but easier to read aloud. Both
work. Pick the one that matches how you would say it.

## 📖 Detailed Concepts

| Topic | Description |
|-------|-------------|
| **🔀 [Boolean Logic](concepts/boolean-logic.md)** | `True`/`False`, logical operators, truth tables, and truthiness |
| **🔀 [Conditional Statements](concepts/conditional-statements.md)** | `if`, `if/else`, `elif` chains, and choosing the right structure |
| **🪆 [Nested Conditionals](concepts/nested-conditionals.md)** | Decisions inside decisions, and when to stop nesting |

All three have Persian translations. Read in order.

## Main Concepts

- **`if` runs a block when a condition is true**
- **`else` catches everything else**
- **`elif` chains alternatives; only the first match runs**
- **Block definition by indentation**, not by braces
- **Truthiness**: any value can be a condition
- **`and`, `or`, `not`** combine and negate conditions
- **Guard clauses**: checking and exiting early is usually clearer than nesting

## Common Beginner Mistakes

| Mistake | Why it fails |
|---------|--------------|
| Missing the colon after `if` | `SyntaxError` |
| Inconsistent indentation inside the block | `IndentationError`, or a block that ends too early |
| Using `=` instead of `==` | Assigns `True` to the variable; the condition is then truthy |
| Putting a weaker condition first in an `elif` chain | Later branches become unreachable |
| Testing `if x == True:` | Works, but `if x:` is clearer |
| Trusting `[0]` as falsy | It is truthy. An empty list is falsy, a list holding zero is not. |

## Workshop Activities

1. **Pass/fail checker.** Read a score and print `Pass` or `Fail`. Then extend
   it to distinguish `Excellent`, `Good`, `Needs Work`, and `Fail`.
2. **Sign of a number.** Print whether the input is positive, negative, or
   zero. This forces you to think about the zero case instead of forgetting it.
3. **Discount logic.** Write an `if/elif` chain: no discount under 50, 5% under
   100, 10% under 200, 15% above.
4. **Deliberate bug hunt.** Swap programs with a partner. Find three bugs in
   their conditional code without running it. Then run it and see how many you
   caught.

## Homework

- **Condition exercises**: day/night message, voting eligibility, and leap year
  detection.
- **Predict the branch**: given five snippets and their inputs, write down which
  branch runs. Then run them.
- **Rewrite pseudocode**: convert three decision algorithms from
  [Session 9](../../module-03-algorithmic-thinking/session-09/README.md) into
  Python conditionals.
- **Refactor**: take a nested conditional you wrote in the workshop and rewrite
  it using guard clauses. Compare which is easier to read.

## Key Takeaways

- Indentation defines the block; Python has no braces.
- Only the first matching `elif` runs, so order conditions from strict to loose.
- Any value works as a condition; Python decides via truthiness.
- `[0]` is truthy. An empty list is falsy.
- Nested conditionals are fine, but a flat `elif` chain is usually clearer.

## Connection to Next Session

A program can now choose a path, but it still runs each step exactly once.
[Session 14: Loops](../session-14/README.md) adds iteration: `while` for
condition-controlled repetition, `for` for sequence traversal, and `break` and
`continue` for leaving the middle of a loop.

**Required Reading**: the three concept articles listed above. Start with
[Boolean Logic](concepts/boolean-logic.md), since everything else depends on
it.