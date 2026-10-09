# Session 22: Review, Consolidation, and Capstone Projects

## Session Overview

The last session. This one has no new syntax, because the point is not new
syntax — it is checking whether the ideas have become available on demand. We
review the arc of the course, take stock of what you can now build unaided, and
then spend most of the session on your own project.

## Key Learning Objectives

By the end of this course, you will be able to:

- **Describe** how a computer represents data, from bits to text encoding
- **Design** an algorithm before writing code, using IPO and FIDEO
- **Write** Python using variables, control flow, collections, and functions
- **Handle** errors deliberately rather than accidentally
- **Organise** a program across files and read and write data
- **Identify** the next concrete step in your learning

## What You Have Built On

The course was sequenced deliberately. Each module answered the question the
previous one raised:

```
    M1  How does a computer work?      CPU, memory, processes, OS
        ↓
    M2  How is data stored?            bits, bytes, binary, encoding
        ↓
    M3  What should the program do?     IPO, FIDEO, pseudocode
        ↓
    M4  How do I say it in Python?     syntax, types, control flow, collections
        ↓
    M5  How do I make it maintainable? functions, errors, files, modules
```

You did not learn Python first and hope the concepts arrived later. You learned
what a computer is, and Python made sense immediately. That is the difference
this course was designed to produce.

## Your Toolkit

```
    CONCEPTS                      PYTHON
    --------                      ------
    binary, hex, encoding    →    str, bytes, .encode(), .decode()
    IPO model                 →    input, computation, print
    control structures        →    if / elif / else, while, for
    sequences                 →    list, tuple, dict, set
    algorithm                 →    def, parameters, return
    finite state              →    local variables, modules
    data persistence           →    open(), with, json
    error conditions           →    try / except / else / finally
    modular design            →    imports, __main__, project layout
```

If you can go from "the program must sum a list of numbers" to working code
without looking anything up, this course did its job.

## Self-Check

Try these without the notes. The answer is a concept name or a short snippet.

1. Why does `range(5)` produce five values starting at zero?
2. What does `input()` return, and what must you do before arithmetic?
3. When a list is modified while you iterate over it, what goes wrong?
4. Why does `x = my_list.sort()` leave `x` as `None`?
5. What is the difference between `except ValueError:` and a bare `except:`?
6. What does `'w'` mode do to an existing file?
7. Why does a file need `if __name__ == "__main__":`?
8. What does `s.find("x")` return when `"x"` is absent, and why is that
   dangerous in an `if`?

If you hesitated on several, revisit the module named in
[overview.md](../../overview.md) rather than moving on.

## Capstone Project

Pick something you actually want to exist. The requirement is not complexity,
it is **completion**: working, documented, and tested on data you did not
invent at the last minute.

Ideas that fit the skills you now have:

```
    text analyser      word counts, frequency, longest word, per-line stats
    expense tracker    read a file, categorise, summarise by month
    quiz engine        questions in a file, score, review wrong answers
    log analyser       parse a log, count error types, report busiest hour
    contact book       add, search, edit, delete, save to JSON
    number tool        convert between bases, as in Module 2
```

Whatever you choose, aim for these deliverables:

- [ ] Runs without errors on inputs you did not write
- [ ] Functions each doing one job, with docstrings
- [ ] Input validated, with helpful messages when it is wrong
- [ ] Data read from or written to a file
- [ ] A `README.md` explaining what it does and how to run it

That last item is worth more than you might expect. It is the difference
between code and a project, and it is the habit that makes your work legible to
yourself in a year.

## 📖 Detailed Concepts

| Topic | Description |
|-------|-------------|
| **🎓 [Course Review](concepts/course-review.md)** | A full recap of every module, what you can now build, and common mistakes to avoid |
| **🚀 [Next Steps](concepts/next-steps.md)** | Paths forward from here, project ideas by difficulty, and a 30-day challenge |

> **Note**: neither article has a Persian translation yet. Both English versions
> are complete.

## Key Takeaways

- The course ran bottom-up on purpose: hardware, then data, then thinking, then
  syntax, then engineering.
- You can now write, debug, organise, and persist a complete small program.
- A finished small project teaches more than a large unfinished one.
- Documenting your work is part of the work.
- The next step is decided by what you enjoy, not by what sounds impressive.

## Course Reflection

Before you leave, write one page answering:

1. Which concept was hardest, and what finally made it click?
2. Which session would you hand to a friend who was starting today?
3. What is the smallest program you could write today that you could not write
   at the start of Module 4?
4. What do you want to build next?

Question 3 is the real measure of the course. If you can name something
specific, you learned it.

**After this session**: [overview.md](../../overview.md) for the full course
map, and [next-steps.md](concepts/next-steps.md) for where to go from here.