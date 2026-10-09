# Workshops — Supplemental Python Tutorials

These are standalone, self-contained tutorials that go deeper than the session
material on a single topic. Each one can be read on its own, out of order, and
each ends with practice questions and answers.

They are **supplemental**. Every session already has its own concepts,
workshop activities, and homework. Use these when you want more examples of
one thing, or when a topic deserves a second pass.

## How These Relate to the Sessions

| Workshop | Covers | Main session |
|----------|--------|--------------|
| [1. Python Basics](01-Python-Basics.md) | Variables, `print()`, types, lists, tuples, sets, strings, file I/O | Sessions 10–16, 19 |
| [2. if / elif / else](2-if-else-elif.md) | Conditionals in depth, nesting, patterns | [Session 13](../module-04-python-essentials/session-13/README.md) |
| [3. `match` / `case`](3-match-case.md) | Structural pattern matching, and when to prefer `if` | Extension of Session 13 |
| [4. `while`](4-while.md) | Infinite loops, `break` / `continue`, loop `else`, nesting | [Session 14](../module-04-python-essentials/session-14/README.md) |
| [5. `for`](5-for.md) | `range()`, iterating dicts and sets, nested loops | [Session 14](../module-04-python-essentials/session-14/README.md) |
| [6. New Features](6-new-features.md) | What changed in Python 3.8 → 3.14 | Reference material |
| [7. Dictionaries & JSON](7-json-dicts-intro.md) | Dictionary operations and JSON structure | [Session 16](../module-04-python-essentials/session-16/README.md) |
| [8. Dictionaries & APIs](7-json-dicts-workshop.md) | Calling a web API and parsing the JSON response | Extension of Session 16 |

> **Note on numbering**: the JSON API workshop is filed as `7-json-dicts-workshop.md`
> but covers different ground from `7-json-dicts-intro.md` — the first is a
> crash course on the data structure, the second on fetching it over the
> network. Read them in that order. The filename is unchanged to avoid breaking
> any existing links.

## Runnable Examples

[`Section1/`](Section1) holds three small scripts used in the early sessions.
They are meant to be edited and run, not just read:

- [`1-hello-world.py`](Section1/1-hello-world.py) — your first program
- [`2-variables.py`](Section1/2-variables.py) — variables and `type()`
- [`3-print-function.py`](Section1/3-print-function.py) — concatenation vs f-strings

```bash
python Section1/1-hello-world.py
```

## Requirements

Everything here runs on the Python 3 standard library, except
[the API workshop](7-json-dicts-workshop.md), which needs one package:

```bash
pip install requests
```

## PDF

`01-Python-Basics.pdf` is a print-ready version of the Python Basics tutorial,
for students who prefer to work from paper.

## A Suggested Order

If you are working through the course and want the workshops alongside it:

1. Sessions 10–12, then [Workshop 1](01-Python-Basics.md) for extra practice
2. [Workshop 2](2-if-else-elif.md) after Session 13
3. [Workshops 4 and 5](4-while.md) after Session 14
4. [Workshop 3](3-match-case.md) once `if`/`elif` is comfortable
5. [Workshops 7 and 8](7-json-dicts-intro.md) after Session 16
6. [Workshop 6](6-new-features.md) whenever a new Python version lands

## Contributing

If you add a workshop here, keep the `N-topic-name.md` naming, give it a
numbered section structure, and end it with practice questions and answers. Add
a row to the table above.