# Session 17: Functions – Reusable Blocks of Code

## Session Overview

You now have all the pieces of a program: variables, conditions, loops,
collections. What you lack is a way to name a piece of behaviour and reuse it.
Functions are that mechanism. This session covers defining functions,
passing parameters, returning values, and the scope rules that determine where a
variable lives. It also introduces the habit that separates working scripts from
maintainable code: giving each function exactly one job.

## Key Learning Objectives

By the end of this session, you will be able to:

- **Define** and **call** functions with `def`
- **Pass** parameters, positionally and by keyword
- **Return** values and distinguish `return` from `print`
- **Explain** local versus global scope
- **Write** docstrings for every function you create
- **Refactor** a long script into named functions

## Defining and Calling

```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Sara")     # call
print(message)              # Hello, Sara!
```

A function is defined with `def`, then called by writing its name with
parentheses. The `name` in the definition is a **parameter**; `"Sara"` at the
call site is an **argument**.

## return vs print

This distinction trips up nearly everyone once:

```python
def add_print(a, b):
    print(a + b)            # prints, returns None

result = add_print(2, 3)
print(result)               # None
```

```python
def add_return(a, b):
    return a + b            # hands a value back

result = add_return(2, 3)
print(result)               # 5
```

The rule: `print` sends something to the screen for a human. `return` sends a
value back to the code that called you. A function that computes something must
`return` it. `return` also exits the function immediately.

## Scope: Where Variables Live

A variable created inside a function is local to it and disappears when the
function ends:

```python
count = 0

def increment():
    count = count + 1        # UnboundLocalError!
```

Python sees `count` on the left of the assignment and treats it as local for
the whole function, then finds no value assigned to it yet. The rule of thumb:
**pass values in, return values out**. Do not reach for `global`.

```python
def increment(n):
    return n + 1

count = increment(count)
```

## Defaults and Flexible Parameters

```python
def greet(name, greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"

greet("Sara")                        # Hello, Sara!
greet("Sara", "Hi")                  # Hi, Sara!
greet("Sara", punctuation="?")       # Hello, Sara?
greet(greeting="Welcome", name="Ali") # Welcome, Ali!
```

Note that parameters with defaults must come *after* those without. Also note
the last call: keyword arguments can be given in any order.

```python
def total(*args):        # any number of positional arguments
    return sum(args)

def describe(**kwargs):  # any number of keyword arguments
    return kwargs

def strict(a, b, *args, **kwargs):  # both
    ...
```

## One Job Per Function

A function that does one thing is easy to name, test, and reuse. A function that
parses input, validates, calculates, formats, and prints is none of those. This
idea has a name — single responsibility — and it is the difference between code
you can change next month and code you are afraid to touch.

```
    GOOD                          BAD
    ────                          ────
    def calculate_average(s):     def process_student(name, scores):
        return sum(s)/len(s)          validate(scores)
                                         compute(scores)
                                         print_report(scores)
                                         save_to_file(scores)
```

The left version can be tested in one line and reused anywhere. The right
version cannot be tested without touching the filesystem.

## 📖 Detailed Concepts

| Topic | Description |
|-------|-------------|
| **📝 [Function Definition](concepts/function-definition.md)** | `def`, parameters, return values, scope, and docstrings |
| **🎛️ [Function Parameters](concepts/function-parameters.md)** | Positional vs keyword arguments, defaults, `*args`, `**kwargs` |
| **🧱 [Modular Design](concepts/modular-design.md)** | Single responsibility, composing functions, and organising code |

All three have Persian translations. Read in order.

## Main Concepts

- **`def` defines; parentheses call**
- **Parameter** is the name in the definition; **argument** is the value passed
- **`return` hands a value back and exits**; `print` only displays
- **Local scope**: variables inside a function die with it
- **Pass in, return out** — avoid `global`
- **Defaults** must come after non-default parameters
- **Keyword arguments** make call sites readable and order-independent
- **Docstrings** explain what a function does, not how

## Common Beginner Mistakes

| Mistake | Result |
|---------|--------|
| Using `print` instead of `return` | Callers get `None` and cannot compute with the result |
| Reaching for `global` to modify a variable | Works, but couples the function to everything around it |
| A mutable default argument (`items=[]`) | That list persists across calls and accumulates. Use `items=None` |
| Default parameter before a non-default one | `SyntaxError` |
| Forgetting that `return` exits immediately | Code after it never runs |
| Writing a docstring that restates the name | `"""Get the name."""` adds nothing. Say what it returns |

The mutable default is worth calling out because it is genuinely surprising:

```python
def add_item(item, basket=[]):   # the list is created ONCE
    basket.append(item)
    return basket

add_item("apple")   # ['apple']
add_item("pear")    # ['apple', 'pear']  <- the previous call leaked in
```

## Workshop Activities

1. **Shape functions.** Write `area_rectangle(w, h)`, `area_circle(r)`, and
   `area_triangle(b, h)`. Each takes numbers and returns a number. Nothing
   prints.
2. **Utility belt.** Write `is_even(n)`, `is_positive(n)`, `max_of_three(a, b, c)`,
   and `count_digits(n)`.
3. **Refactor.** Take a long script from your earlier homework and split it into
   at least four functions. Give each one a name that describes what it does,
   not how.
4. **Docstring drill.** Add a docstring to every function you wrote today that
   states the parameters, what it returns, and any assumption it makes.

## Homework

- **Function library**: write five small functions with docstrings, and a
  script that calls all of them.
- **Predict the output**: given six function definitions and calls, write down
  exactly what each prints. Include at least one function that returns a value
  it never prints.
- **Pseudocode to function**: take the linear search algorithm from
  [Session 9](../../module-03-algorithmic-thinking/session-09/README.md) and
  turn it into a function that takes a list and a target and returns the index
  or `-1`.
- **Refactor**: pick your longest program from the course so far and reduce it
  to functions with no function longer than about ten lines.

## Key Takeaways

- `return` is for the code; `print` is for the human. They are not the same.
- Local variables die with the function. Pass values in, get values out.
- Parameters with defaults must come last.
- A mutable default argument is created once and shared. Avoid it.
- One job per function; everything else follows from that.

## Connection to Next Session

Functions let you organise code, but a program can still crash on bad input.
[Session 18: Error Handling and
Debugging](../session-18/README.md) covers exceptions, `try/except`, reading
tracebacks, and the debugging techniques that turn a crash into information.

**Required Reading**: the three concept articles listed above, in order. Start
with [Function Definition](concepts/function-definition.md).