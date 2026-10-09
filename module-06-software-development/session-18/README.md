# Session 18: Error Handling and Debugging

## Session Overview

Everything so far assumes your program receives sensible input. Real programs
do not. This session reframes errors as information rather than failure: what
the three error categories mean, how to read a traceback, how to catch the
errors you expect with `try/except` while letting the ones you do not expect
crash loudly, and how to debug systematically instead of guessing.

## Key Learning Objectives

By the end of this session, you will be able to:

- **Distinguish** syntax, runtime, and logic errors
- **Read** a traceback from the bottom up and find the real failing line
- **Handle** expected failures with `try/except/else/finally`
- **Choose** which exceptions to catch, and which to let propagate
- **Debug** using print statements, assertions, logging, and `pdb`
- **Recognise** that a logic error is the hardest kind, because nothing complains

## Three Kinds of Error

```
    SYNTAX ERROR       Python cannot parse the code at all.
                       Nothing runs. Usually a missing colon,
                       unbalanced bracket, or typo.

    RUNTIME ERROR     The code parsed, started, and then failed.
                       Python stops and shows a traceback.

    LOGIC ERROR        The code ran perfectly and produced
                       the wrong answer. Nothing complains.
                       This is the dangerous one.
```

The third category is why testing matters. A program that crashes is telling
you something. A program that quietly computes the wrong average is not.

## Reading a Traceback

Tracebacks read **bottom-up**. The last line is the error; the lines above show
the call chain that led there.

```
Traceback (most recent call last):
  File "grades.py", line 42, in <module>
    report = generate_report(students)
  File "grades.py", line 58, in generate_report
    average = sum(scores) / len(scores)
ZeroDivisionError: division by zero
```

Read it like this: the program started at line 42, called `generate_report`,
which died at line 58 trying to divide by zero. That is where you look — not at
line 42.

## try/except, and Its Limits

```python
try:
    age = int(input("How old are you? "))
except ValueError:
    print("Please enter a number.")
```

The full form has four parts:

```python
try:
    result = risky_operation()
except ValueError as e:
    print(f"Bad value: {e}")
except KeyError:
    print("Missing key")
else:
    print("No error - this only runs on success")
finally:
    cleanup()          # runs no matter what
```

Two rules keep this from becoming a code smell:

1. **Catch specific exceptions, not bare `except:`.** A bare `except:` swallows
   your own typos too, and you will spend an afternoon wondering why a variable
   is `None`.
2. **Do not use `try` to hide bugs.** Use it for failures you genuinely expect,
   like user input or a missing file. A `TypeError` from your own logic bug
   should crash so you notice.

## Debugging Techniques

In rough order of usefulness:

```
    1. READ THE ERROR MESSAGE   It usually names the problem exactly.

    2. REPRODUCE IT             Find the smallest input that fails.
       Every time, the same way.

    3. BISECT                   Comment out half the code.
       Which half still fails?

    4. PRINT THE STATE          print(repr(x)) not print(x).
       repr() shows quotes, so an
       empty string is visible.

    5. ASSERT                   assert 0 <= score <= 100, "score out of range"
       Fires at the moment the
       assumption breaks.

    6. pdb                      python -m pdb broken.py
       Step line by line, inspect
       variables, continue.

    7. RUBBER DUCK              Explain it out loud, line by line,
       to an object that cannot
       help. You will find the bug
       mid-sentence.
```

## 📖 Detailed Concepts

| Topic | Description |
|-------|-------------|
| **⚠️ [Common Python Errors](concepts/common-errors.md)** | Syntax, runtime, and logic errors, and what each message means |
| **🐛 [Debugging Techniques](concepts/debugging-techniques.md)** | Print debugging, assertions, logging, `pdb`, and bisecting |
| **🛡️ [Exception Handling](concepts/exception-handling.md)** | `try/except/else/finally`, raising your own, and context managers |

All three have Persian translations. Read in order.

## Main Concepts

- **Syntax, runtime, logic** — three categories with three different remedies
- **Tracebacks read bottom-up**; the last line is the error
- **`try/except/else/finally`**: `else` on success, `finally` always
- **Catch specific exceptions**; a bare `except:` hides your own bugs
- **Don't use `try` to mask logic errors**; let them crash
- **`repr()`** reveals invisible problems like an empty string
- **`assert`** documents and checks an assumption
- **`pdb`** steps through real execution

## Common Beginner Mistakes

| Mistake | Consequence |
|---------|-------------|
| Bare `except:` | Hides typos, `NameError`, everything. The program silently misbehaves |
| Catching an exception then printing nothing | The failure is invisible and will resurface later |
| `print(x)` to debug an empty string | Looks like nothing printed. Use `print(repr(x))` |
| Reading only the first traceback line | That is the *cause*, not the *location*. Read upward |
| Wrapping the whole program in `try/except` | Every bug becomes "something went wrong" |
| Assuming no error means correct | Logic errors produce no error at all |

## Workshop Activities

1. **Fix the code.** Five broken snippets. Find the errors, say which of the
   three categories each is, then fix them.
2. **Robust input.** Take your Session 12 input program and make it keep asking
   until it receives a valid integer, using a `while` loop with `try/except`.
3. **Traceback practice.** Three tracebacks. For each, write down the exact file,
   line number, exception type, and what the program was trying to do.
4. **Find the logic error.** A program that runs without crashing but returns
   the wrong average. Use `print(repr(...))` to find out why.

## Homework

- **Debug tasks**: five short buggy code fragments. For each, name the error
  category, explain the cause, and provide the fix.
- **Error log**: while doing your other homework, record every error message
  you hit and how you resolved it. This becomes a personal reference.
- **Safe conversion**: write a function `read_number(prompt)` that keeps asking
  until it gets a valid number, then returns it. Use it in a small program.
- **Prediction**: given three `try/except` blocks, write down exactly what
  happens for inputs that raise, do not raise, and raise something uncaught.

## Key Takeaways

- Syntax errors stop you before running. Runtime errors stop you during.
  Logic errors do not stop you at all.
- Tracebacks read bottom-up; the bottom line is where to look.
- Catch specific exceptions. A bare `except:` is a trap.
- Use `try/except` for expected failures, not to conceal bugs.
- `repr()` and `assert` catch what `print` cannot.

## Connection to Next Session

Your programs now survive bad input. [Session 19: Working with
Files](../session-19/README.md) makes them survive restarts by reading and
writing data that outlives the process.

**Required Reading**: the three concept articles listed above, in order. Start
with [Common Python Errors](concepts/common-errors.md) so the vocabulary is
fresh.