# Session 20: Organizing Code – Modules and a Small Multi-File Program

## Session Overview

One file works until it does not. At some point a program grows past the point
where you can find anything, and the natural response is to split it across
several files. This session covers Python modules: how to create one, the three
ways to import from it, why `if __name__ == "__main__":` exists, and how to lay
out a small project so each file has one job.

## Key Learning Objectives

By the end of this session, you will be able to:

- **Create** a module and import from it
- **Distinguish** `import x`, `from x import y`, and `from x import y as z`
- **Explain** why `if __name__ == "__main__":` guards a file's entry point
- **Organise** a project into a sensible file layout
- **Use** the standard library's modules instead of reinventing them
- **Avoid** the circular import trap

## A Module Is Just a .py File

There is no special syntax. A module is a Python file, and anything you define
at the top level in it becomes available to importers:

```python
# utils.py
def add(a, b):
    return a + b

TAX_RATE = 0.09
```

```python
# main.py
import utils
print(utils.add(2, 3))        # 5
print(utils.TAX_RATE)         # 0.09
```

## Three Ways to Import

```
    import utils
        → use utils.add(...)
        → clear where things come from

    from utils import add
        → use add(...)
        → shorter, but ambiguous if two modules have `add`

    from utils import add as sum_two
        → use sum_two(...)
        → for renaming a clash

    from utils import *          <- avoid
        → pollutes your namespace
        → hides where names came from
```

The general advice: prefer `import module` at the top of the file. It makes the
dependency visible and avoids collisions.

## The __main__ Guard

This looks like ceremony until you write a project:

```python
# main.py
from calc import add

def main():
    print(add(1, 2))

if __name__ == "__main__":
    main()
```

When you run `main.py` directly, `__name__` is `"__main__"` and `main()` runs.
When `main.py` is *imported* by another file, `__name__` is `"main"` and the
block is skipped. Without the guard, importing a file runs everything in it —
which is why a file with `print("loading...")` at the top level prints that every
time anything imports it.

## A Sensible Project Layout

For a small application, this is enough:

```
    myapp/
    ├── main.py          entry point, user interaction, main()
    ├── calc.py          calculation logic
    ├── storage.py       reading and writing files
    └── data/
        └── sample.txt   data, kept out of the code
```

Two rules that keep this from tangling:

- **No circular imports.** `a.py` imports `b.py` which imports `a.py` fails. If
  you need shared code, put it in a third file that both import.
- **`main.py` imports; the others do not import it.** Dependencies point one
  way, like an arrow.

## The Standard Library

You do not need to write these yourself:

```
    random        random numbers, choices, shuffling
    datetime      dates and times
    math          sqrt, pi, floor, ceil
    json          read and write JSON
    collections   Counter, defaultdict, namedtuple
    pathlib       modern path handling
```

```python
import random
from datetime import datetime

print(datetime.now().strftime("%Y-%m-%d %H:%M"))
print(random.choice(["Ali", "Sara", "Reza"]))
```

If you are about to write a utility, check whether the standard library already
has it. For this course's file-processing project, `json` is almost always
better than a hand-rolled comma-separated format.

## 📖 Detailed Concepts

| Topic | Description |
|-------|-------------|
| **📦 [Python Modules](concepts/python-modules.md)** | Creating modules, import styles, search paths, `__main__`, and project layout |

> **Note**: this article has no Persian translation yet. The English version is
> complete.

## Main Concepts

- **A module is a `.py` file**; there is no special syntax
- **`import x`, `from x import y`, `as`** are the three styles
- **Avoid `from x import *`**; it hides where names came from
- **`if __name__ == "__main__":`** distinguishes running from importing
- **Dependencies point one way**; cycles fail at import time
- **`main.py` imports, everything else does not import it**
- **Check the standard library before writing a utility**

## Common Beginner Mistakes

| Mistake | Consequence |
|---------|-------------|
| Top-level code with no `__main__` guard | Runs again on every import |
| `from x import *` | Name collisions you cannot trace |
| File named `random.py` or `math.py` | Shadows the standard library; confusing errors |
| Circular imports between modules | `ImportError` at startup |
| Importing after code has started | Legal but confusing. Imports go at the top |
| All logic in `main.py` | The split happens later, messily, when it hurts most |

## Workshop Activities

1. **Two-file project.** Split one of your earlier scripts: functions in one
   file, user interaction in another, with `main.py` tying them together.
2. **Utility library.** In pairs, build a small `utils.py` with five helper
   functions. Trade files and use each other's module in a driver script.
3. **Refactor.** Take your longest program and split it into at least three
   files with distinct jobs. Add the `__main__` guard to each.
4. **Deliberate cycle.** Create two modules that import each other. Watch the
   `ImportError`. Then break the cycle with a third shared module.

## Homework

- **Module practice**: build a math utilities module (`add`, `subtract`,
  `multiply`, `divide` with zero-division handling, `power`, `factorial`) and a
  script that uses them.
- **Directory layout**: draw a diagram of your project's files, state what each
  one is responsible for, and mark the direction of each import.
- **Standard library**: pick three modules from the standard library, use each
  in a short script, and write two sentences on what they replace.
- **Reflection**: a short piece on why organising code matters, in terms of what
  it costs you when you do not.

## Key Takeaways

- A module is just a file. Splitting a program is mechanical once you know why.
- `if __name__ == "__main__":` is what stops imports from running everything.
- One-directional imports keep a project debuggable.
- The standard library already solves more problems than you think.
- Decide the file layout before the code gets big, not after.

## Connection to Next Session

You can now organise a project. [Session 21: Mini-Project 1](../session-21/README.md)
puts everything together: read data, process it, validate it, report on it, and
save the result.

**Required Reading**: [Python Modules](concepts/python-modules.md).