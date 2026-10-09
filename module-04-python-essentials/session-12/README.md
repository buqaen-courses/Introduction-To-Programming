# Session 12: Input, Output, Expressions and Operators

## Session Overview

We now have variables holding values. This session makes programs interactive:
read something from the user, compute something with it, print a result. Along
the way we build the arithmetic and comparison operators, and — critically —
the precedence rules that decide what `2 + 3 * 4` actually means. Getting
precedence wrong is the most common source of silent logic bugs in early
Python, so this session spends real time on it.

## Key Learning Objectives

By the end of this session, you will be able to:

- **Read** input with `input()` and convert it to the right type
- **Print** values and format output clearly
- **Use** arithmetic operators including `//`, `%`, and `**`
- **Use** comparison operators to produce booleans
- **Apply** operator precedence correctly, and use parentheses deliberately
- **Build** small programs that combine input, processing, and output

## input() Always Returns a String

This single fact causes most first-week errors:

```python
age = input("How old are you? ")
print(type(age))    # <class 'str'>  -- always
```

So this fails:

```python
print(age + 1)      # TypeError
```

And this works:

```python
age = int(input("How old are you? "))
print(age + 1)
```

Wrap the `input()` call in the conversion you need. This is the single most
common line you will write in this course.

## The Operators

```
    ARITHMETIC                    COMPARISON
    ---------                     ----------
    +   addition                  ==   equal
    -   subtraction               !=   not equal
    *   multiplication            <    less than
    /   true division (→ float)   >    greater than
    //  floor division (no rem.)  <=   less or equal
    %   remainder / modulo        >=   greater or equal
    **  power

    LOGICAL (detailed in Session 13)
    --------
    and   or   not
```

Three of these deserve a note:

- `/` always produces a float. `10 / 2` is `5.0`, not `5`.
- `//` rounds down and discards the remainder. `10 // 3` is `3`.
- `%` gives just the remainder. `10 % 3` is `1`.

The last two are how you get "how many full boxes" and "how many left over".

## Precedence: What Happens First

Python evaluates in a defined order. Reading top to bottom:

```
    1. ()                      parentheses — highest, and always explicit
    2. **                      exponent
    3. +x  -x                  unary sign
    4. *  /  //  %             multiplicative
    5. +  -                    additive
    6. <  <=  >  >=  ==  !=    comparison
    7. not                     logical not
    8. and                     logical and
    9. or                      logical or
```

So:

```python
2 + 3 * 4        # 14, not 20  (multiplication first)
(2 + 3) * 4      # 20
```

The same rule governs comparison:

```python
1 + 2 == 3       # True  (compares after the addition)
1 + 2 == 4       # False
```

## When Precedence Surprises You

Multiplication and division are **left-to-right**, and so are addition and
subtraction. The surprise is that they are *different groups*:

```python
100 / 10 / 2      # 5.0    ( (100/10) / 2 )
2 ** 3 ** 2       # 512    right-to-left! (2 ** (3 ** 2) )
```

That second line catches experienced programmers too. Whenever the intended
order is not obvious to a reader, add parentheses. Clarity beats brevity.

## 📖 Detailed Concepts

| Topic | Description |
|-------|-------------|
| **💬 [Input and Output](concepts/input-output.md)** | `input()`, `print()`, and formatting output readably |
| **🔧 [Expressions and Operators](concepts/expressions-operators.md)** | Arithmetic, comparison, and logical operators with examples |
| **📐 [Evaluation Order](concepts/evaluation-order.md)** | Precedence, associativity, and tracing expressions by hand |

All three have Persian translations. Read in order.

## Main Concepts

- **`input()` returns a string**, always
- **Type conversion**: wrap `input()` in `int()` or `float()`
- **Arithmetic operators**: `+ - * / // % **`
- **Comparison operators**: produce `True` or `False`
- **Precedence**: the order operations are evaluated in
- **Associativity**: left-to-right for `* /` and `+ -`; right-to-left for `**`
- **Parentheses**: your clearest tool for removing doubt

## Common Beginner Mistakes

| Mistake | Result |
|---------|--------|
| `input()` used directly in arithmetic | `TypeError` |
| `=` used instead of `==` | Assigns a boolean instead of comparing |
| Assuming `/` gives an integer | `5.0` where you expected `5` |
| Mixing up `//` and `/` | Wrong results, no error message |
| Forgetting that `**` is right-to-left | `2 ** 3 ** 2` is 512, not 64 |
| Chained comparison written as `1 < x < 10` with `and` | Correct as written; just know `and` binds looser than `==` |

## Workshop Activities

1. **Age calculator.** Ask for the current year and the user's birth year.
   Print their age, and their age next year. Handle the conversion properly.
2. **Rectangle calculator.** Ask for width and height. Print the area and the
   perimeter, each on its own line with a label.
3. **Which is larger?** Ask for two numbers and print which is larger. Then
   extend it to handle the case where they are equal.
4. **Predict, then run.** Take five expressions from the board, write down the
   results, then check with Python. Any you missed, trace by hand again.

## Homework

- **Mini calculators**: currency conversion, temperature conversion, and a
  seconds-to-hours-minutes converter.
- **Expression puzzles**: fifteen expressions to simplify and evaluate. Show
  your working, including where you applied precedence.
- **I/O story**: write a short dialogue program that asks three questions and
  responds to each answer differently.
- **Reflection**: three sentences on why `input()` returning a string is a
  design decision rather than a flaw.

## Key Takeaways

- `input()` gives you a string; convert before arithmetic.
- `/` gives a float, `//` and `%` split the quotient and remainder.
- Precedence decides order; parentheses remove all doubt.
- `**` is right-to-left, unlike `* /` and `+ -`.
- Parentheses are not clutter. They are documentation.

## Connection to Next Session

You can now read, compute, and print. But every program so far runs the same
way every time. [Session 13: Decision Making](../session-13/README.md) adds
choice: `if`, `elif`, `else`, and the boolean logic that decides which path runs.

**Required Reading**: the three concept articles listed above. If precedence
feels shaky, read [Evaluation Order](concepts/evaluation-order.md) twice.