# Session 11: Variables and Basic Data Types (int, float, bool, str)

## Session Overview

Last session you ran Python and printed things. Now we give those values names,
and we ask what kind of thing each name is holding. This session introduces
variables as labels bound to values, the four data types you will use constantly
(`int`, `float`, `bool`, `str`), and type conversion — including the reason
`input()` hands you a string no matter what you typed.

## Key Learning Objectives

By the end of this session, you will be able to:

- **Create** variables and assign values with `=`
- **Use** `int`, `float`, `bool`, and `str` correctly
- **Inspect** a value's type with `type()`
- **Convert** between types explicitly and predict the result
- **Avoid** the most common beginner errors, including reusing built-in names

## A Variable Is a Label, Not a Box

The most common early misconception is that a variable is a container that
holds a value. A better model is a label attached to a value that already
exists:

```python
age = 25
```

Read this as "the name `age` points at the value 25". Assigning again
*repoints* the label; it does not modify a box:

```python
age = 25        # age points at 25
age = 30        # age now points at 30; 25 is untouched elsewhere
```

This is why two variables can point at the same value, and why mutating one
list later affects the other (you will meet this properly in Session 16).

## The Four Types You Need Now

```
    ┌──────────────────────────────────────────────────────────────┐
    │  TYPE      EXAMPLE      NOTES                               │
    ├──────────────────────────────────────────────────────────────┤
    │  int      25, -7, 0     Whole numbers. No decimal point.    │
    │  float    3.14, -0.5    Decimal numbers. Any point → float. │
    │  bool     True, False   Exactly two values. Capital letters.│
    │  str      "Ali", 'hi'    Text in quotes. Can hold anything.  │
    └──────────────────────────────────────────────────────────────┘
```

Note the capital letters on `True` and `False`. They are not `true` and
`false`. This is one of the most common first-week errors.

## Inspecting Types

`type()` tells you what a value is. It is a debugging tool you will use
constantly:

```python
print(type(25))        # <class 'int'>
print(type(25.0))      # <class 'float'>
print(type(True))      # <class 'bool'>
print(type("25"))      # <class 'str'>
```

Look at that last one carefully. `25` and `"25"` look almost identical printed,
but they are completely different kinds of thing. This is the seed of the type
errors in Session 12.

## Type Conversion Is Explicit

To change a type, call the type like a function:

```python
age_text = "25"          # str
age_number = int(age_text)   # int

print(age_number + 5)   # 30      works
print(age_text + "5")   # 255     concatenates!
```

The second line is the trap. `"25" + "5"` is `255`, because for strings `+`
means join. `25 + 5` is `30`, because for numbers `+` means add. Same operator,
different data types, different meaning.

## 📖 Detailed Concepts

| Topic | Description |
|-------|-------------|
| **📦 [Python Variables](concepts/python-variables.md)** | Creating, updating, and naming variables, plus what `=` really does |
| **🔢 [Python Data Types](concepts/python-data-types.md)** | `int`, `float`, `bool`, `str` and how to check them |
| **🔄 [Type Conversion](concepts/type-conversion.md)** | Explicit and implicit conversion, safe patterns, common scenarios |

Both English and Persian versions of all three are available. Read in order.

## Main Concepts

- **Assignment**: `name = value` binds a name to a value
- **Dynamic typing**: you do not declare a type; the value carries it
- **`type()`**: reveals what a value actually is
- **Explicit conversion**: `int()`, `float()`, `str()`, `bool()` as functions
- **`bool()` truthiness**: zero, empty string, and empty collections are `False`
- **Naming rules**: letters, digits, underscores; cannot start with a digit
- **Shadowing**: overwriting a built-in like `list` or `str` breaks things later

## Common Beginner Mistakes

| Mistake | What happens |
|---------|--------------|
| `true` instead of `True` | `NameError`. Python is case-sensitive. |
| Reassigning `list` or `str` | Your code breaks in confusing ways much later |
| `input()` result used in arithmetic | `TypeError`. It is always a `str` |
| `age = age + 1` "not working" | It works; `age` still points at the old value if you typo the name |
| Using `=` where `==` belongs | `=` assigns, it does not compare |

## Workshop Activities

1. **Personal data card.** Create variables for name, age, height, and whether
   you like programming. Print them one per line, then print all four with a
   single `print()`.
2. **Type guessing.** Your partner shows you ten literals. Before running
   anything, write down `type()` for each. Then check. Revisit any you got
   wrong.
3. **The string trap.** Try to make `"20"` and `20` fail. Then find the two
   different things that work.
4. **Conversion clinic.** Take three strings from `input()` and build a small
   program that does arithmetic on them without crashing.

## Homework

- **Variable exercises**: three small scripts describing a product, a movie, and
  a city, each with at least five variables of different types.
- **Predict the output**: given six short snippets, write down exactly what each
  prints. Then run them and mark the ones you got wrong.
- **Type challenge**: deliberately write code that adds a string to a number,
  read the `TypeError` carefully, and fix it two different ways.
- **Reflection**: one paragraph explaining in your own words what `=` does.

## Key Takeaways

- A variable is a name bound to a value, and rebinding replaces the binding.
- Python does not need type declarations; values carry their own type.
- `type()` is your first debugging tool.
- Conversion is explicit: you must ask for it.
- `+` means different things for strings and numbers, which is why `input()`
  needs conversion before arithmetic.

## Connection to Next Session

You can now store values. [Session 12: Input, Output and
Expressions](../session-12/README.md) puts them to work: reading from the user,
building arithmetic expressions, and understanding precedence so you can predict
what `2 + 3 * 4` actually evaluates to.

**Required Reading**: the three concept articles listed above. Start with
[Python Variables](concepts/python-variables.md).