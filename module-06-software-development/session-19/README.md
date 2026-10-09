# Session 19: Working with Files – Reading and Writing Text Files

## Session Overview

Everything you have written so far forgets itself the moment it closes. Files
are how programs keep data: reading a configuration, writing a log, saving a
gradebook, remembering a high score. This session covers the `open()` call, the
three file modes you need, the `with` statement that guarantees files get
closed, and how to process file contents line by line.

## Key Learning Objectives

By the end of this session, you will be able to:

- **Explain** what a file path is and how paths differ across systems
- **Open** files in read, write, and append modes
- **Use** `with` so files always close
- **Read** a file whole, line by line, or into a list
- **Write** and **append** to a text file
- **Handle** `FileNotFoundError` and other file errors gracefully

## Three Modes You Need

```
    MODE     MEANING                    IF FILE EXISTS
    ----     -------                    ---------------
    'r'      read (default)             read from the start
    'w'      write                      ERASE, then write
    'a'      append                     write to the end

    ALWAYS pair with 'with'. Always.
```

The `'w'` trap: it truncates. If you open an existing file in write mode, its
contents are gone before you write a single character. This has destroyed more
student assignments than any other Python behaviour.

## Always Use `with`

```python
with open("data.txt", "r") as f:
    content = f.read()
# f is closed here automatically, even if read() raised
```

The `with` block closes the file when the block ends, whether it ended normally
or via an exception. This is called a context manager, and it removes an entire
category of bugs:

```python
# don't do this
f = open("data.txt", "r")
content = f.read()
f.close()        # runs only if nothing above raised
```

If `read()` fails, that last line never runs and the file stays open.

## Reading

```python
# whole file as one string
content = f.read()

# one line at a time - the memory-friendly way
for line in f:
    print(line, end="")      # end="" avoids double newlines

# all lines as a list
lines = f.readlines()

# a fixed number of characters
first_100 = f.read(100)
```

Iterating the file object directly, rather than calling `readlines()`, is
preferable for large files: it uses constant memory instead of loading
everything at once.

## Writing

```python
with open("output.txt", "w") as f:
    f.write("first line\n")
    f.write("second line\n")

with open("output.txt", "a") as f:
    f.write("appended later\n")
```

The `\n` is a newline character. Without it everything lands on one line.
Note also that `write()` returns the number of characters written, not the text
itself — so do not write `f.write(f.write("x"))`.

## Paths

```python
open("notes.txt")                  # relative to the current directory
open("data/scores.txt")            # subdirectory, if it exists
open("/home/user/notes.txt")       # absolute, Unix
open("C:\\Users\\me\\notes.txt")   # absolute, Windows
```

Windows uses `\` and Unix uses `/`. Python's `pathlib` and `os.path.join()` let
you write one path expression that works on both:

```python
from pathlib import Path

p = Path("data") / "scores.txt"
if p.exists():
    print("found it")
```

## 📖 Detailed Concepts

| Topic | Description |
|-------|-------------|
| **📄 [File Handling Basics](concepts/file-handling-basics.md)** | Paths, read and write modes, `with`, and handling file errors |

> **Note**: this article has no Persian translation yet. The English version is
> complete.

## Main Concepts

- **`open(path, mode)`** is the entry point to every file operation
- **`'r'` read, `'w'` write and truncate, `'a'` append**
- **`'w'` destroys existing content** before you write anything
- **`with` guarantees closing**, even when an exception is raised
- **`for line in f`** streams the file; `readlines()` loads it all
- **`\n`** is the newline you must write yourself
- **`pathlib.Path`** handles path separators portably
- **`FileNotFoundError`** is the error to expect on every read

## Common Beginner Mistakes

| Mistake | Consequence |
|---------|-------------|
| Opening with `'w'` when you meant to read | File is erased |
| Forgetting `with` | File stays open if an error occurs midway |
| Forgetting `\n` in `write()` | All output on one line |
| Using `read()` on a huge file | Loads it entirely into memory |
| Assuming a path exists | `FileNotFoundError` |
| Hardcoding a Windows path | Breaks on every other machine |
| `f.write(...)` result used as if it were text | It returns an integer count |

## Workshop Activities

1. **Journal program.** Ask for a journal entry and append it to a text file,
   with a date line before it. Run it three times and inspect the file.
2. **Word counter, v2.** Write a file with several paragraphs, then read it back
   and report lines, words, and characters. Do it streaming, not with `read()`.
3. **Copy file.** Read one file and write its contents to another, character
   count matching as you go.
4. **Missing file drill.** Try to open a file that does not exist. Catch the
   error, print a friendly message, and exit cleanly instead of crashing.

## Homework

- **Log creator**: a program that appends login times to a log file, one per
  run. Run it several times and show the file growing.
- **File stats**: given a text file, print its line count, word count, and
  character count.
- **Safeguard**: take any earlier program that writes a file and add a check
  that warns before overwriting, using `os.path.exists()`.
- **Reflection**: one short paragraph on when file-based programs are the right
  tool, and when they are overkill.

## Key Takeaways

- `'w'` truncates. That is the single most important fact in this session.
- Always use `with`. It closes the file no matter what.
- Stream with `for line in f` when the file might be large.
- `\n` does not appear on its own in `write()`.
- Handle `FileNotFoundError`; it is not an edge case, it is the default.

## Connection to Next Session

One file is a start. [Session 20: Modules and Multi-File
Programs](../session-20/README.md) splits a program across several files and
shows how `import` lets each one use the others.

**Required Reading**: [File Handling Basics](concepts/file-handling-basics.md).