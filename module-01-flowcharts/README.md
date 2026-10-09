# Section 0: Flowcharts — The Flow of Thought

> **A zero-indexed primer.** This section sits *before* Session 1 and exists so that
> the rest of the course has somewhere to stand. Read it once, at the start, before
> you write a single line of Python.

---

## Why This Section Exists

Most beginner courses start with syntax: variables, `print`, loops. That order
teaches you to type before you can think, and it is why so many beginners can
read a line of Python but cannot say *what the program does*.

This section reverses it. You will **draw first**. Every program in this course
was designed as a chart long before it was typed, and the charts are the part
that transfers. Syntax changes — Python 3.14 will replace something you learned
this month. The shape of a solution does not.

By the end of this primer you will be able to read a flowchart, draw one for a
small problem, trace it on paper, and convert it into code.

## Learning Objectives

After completing this section you will be able to:

- **Name** the six standard flowchart symbols and explain the job of each
- **Draw** a valid flowchart obeying the five laws
- **Recognise** the three control patterns — sequence, selection, iteration —
  inside any algorithm
- **Identify** the four organs of a loop: init, test, body, step
- **Trace** an algorithm by hand with a table and find its bugs on paper
- **Apply** the five-move design method to turn a wordy problem into a chart
- **Convert** chart → pseudocode → code as a mechanical, boring step
- **Analyse** problems using the IPO framework and track state
- **Evaluate** procedures against the FIDEO algorithm characteristics
- **Implement** ten classic algorithms with flowcharts and pseudocode

## How This Section Is Structured

Nine lessons, roughly **2–3 hours at reading pace**. Each one builds on the last.

| # | Lesson | What it gives you |
|---|--------|-------------------|
| 1 | [Why Draw Before You Code](concepts/01-why-draw-before-you-code.md) | The case for designing on paper |
| 2 | [The Six Symbols](concepts/02-flowchart-symbols.md) | Terminator, process, I/O, decision, flow line, connector |
| 3 | [The Three Control Patterns](concepts/03-control-patterns.md) | Sequence, selection, iteration — the whole grammar |
| 4 | [Loops and Trace Tables](concepts/04-loops-and-trace-tables.md) | The four organs of a loop, counters, and dry running |
| 5 | [Design Method and Review Checklist](concepts/05-design-method-and-review.md) | Problem → chart in five moves, plus the four ways charts break |
| 6 | [Workshop: Three Briefs](concepts/06-workshop-briefs.md) | Practice with an answer key |
| 7 | [Classic Algorithms](concepts/07-classic-algorithms.md) | Ten classic algorithms with flowcharts and pseudocode |
| 8 | [IPO and State](concepts/08-ipo-and-state.md) | Input-Process-Output framework and state management |
| 9 | [Algorithm Characteristics](concepts/09-algorithm-characteristics.md) | FIDEO: what makes a procedure a valid algorithm |

> **Read them in order.** Lesson 3 assumes Lesson 2's symbols, and Lesson 4
> assumes you can draw a fork. Skipping ahead is possible but will cost you.

## Where This Section Ends and the Course Begins

This is a **primer** that now covers the core of algorithmic thinking alongside
flowchart design. The classic algorithms — FizzBuzz, prime test, GCD, Fibonacci,
linear and binary search, bubble sort — are taught here in Lesson 7.

## Prerequisites

**None.** You need paper, a pen, and the willingness to trace a table by hand.

That last part is not optional. Students who try to dry-run a chart "in their
head" skip the step that teaches the step. Students who write the table learn it.

You will also want a way to render the Mermaid diagrams in these files. GitHub
renders them natively; on other platforms see
[Mermaid Live Editor](https://mermaid.js.org/intro/).

## The Whole Section on One Page

Six symbols, three patterns, five moves. That is the entire art — the rest is
practice.

**The six symbols**

| Symbol | Name | Purpose |
|--------|------|---------|
| ⬭ | Terminator | One door in, doors out |
| ⬜ | Process | One box, one job — `←` means *becomes* |
| 🗄️ | I/O parallelogram | Data leaning in or out |
| 🔷 | Decision | One yes/no question, labelled exits |
| ➡️ | Flow line | Down and right, or carry an arrowhead |
| ◯ | Connector | Splices the long jumps |

**The three patterns**

```
sequence   A → B → C          do this, then that, then the other thing
selection  ◇ yes → ...        choose a lane; the other lane costs nothing
iteration  → back             repeat while a condition holds
```

**The five moves**

1. **Restate** — what comes in, what must come out
2. **Spill** — the steps in plain words, unpolished
3. **Shape** — mark each step as sequence, selection, or iteration
4. **Draw** — boxes, diamonds, arrows; one action per box
5. **Dry-run** — trace a small input with a table

## The One-Sheet Review Checklist

Before any chart earns the right to become code:

- [ ] Exactly one START, and every path reaches a STOP
- [ ] Every decision's exits are labelled yes / no
- [ ] One arrow enters each symbol — never more
- [ ] Arrows flow down or right; anything else carries an arrowhead
- [ ] No line crosses, touches, or cuts through a symbol
- [ ] Every loop has a step that can make its test false
- [ ] One action per rectangle; one question per diamond
- [ ] It has been dry-run on paper, with a table

## Where to Go Next

1. Finish [Session 1: What Is a Computer?](../module-02-computers-and-programs/session-01/README.md)
2. Work through the rest of the course modules
3. When you reach the Python modules, translate your Section 0 charts into
   Python and notice how boring the last step is

---

*First you shape the flow. Then the flow shapes you.*

## Persian

این بخش به فارسی هم موجود است: [مقدمه فلوچارت — جریان اندیشه](README_FA.md)
