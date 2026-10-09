# Section 0 Concepts: Flowcharts

Nine lessons that teach you to design algorithms visually before you write them in
code. This is a primer for the whole course, covering flowchart design, classic
algorithms, IPO analysis, and algorithm characteristics.

## Table of Contents

| # | Lesson | Covers |
|---|--------|--------|
| 1 | **[Why Draw Before You Code](01-why-draw-before-you-code.md)** | Separating logic from syntax; the standard; cheaper bugs |
| 2 | **[The Six Symbols](02-flowchart-symbols.md)** | Terminator, process, I/O, decision, flow lines, connectors, the five laws |
| 3 | **[The Three Control Patterns](03-control-patterns.md)** | Sequence, selection, iteration; fork and join; the whole grammar |
| 4 | **[Loops and Trace Tables](04-loops-and-trace-tables.md)** | Four organs of a loop; counters and accumulators; dry running |
| 5 | **[Design Method and Review Checklist](05-design-method-and-review.md)** | Five moves; four ways charts break; the checklist |
| 6 | **[Workshop: Three Briefs](06-workshop-briefs.md)** | Three exercises with hints and an answer key |
| 7 | **[Classic Algorithms](07-classic-algorithms.md)** | Ten classic algorithms with flowcharts and pseudocode |
| 8 | **[IPO and State](08-ipo-and-state.md)** | Input-Process-Output framework and state management |
| 9 | **[Algorithm Characteristics](09-algorithm-characteristics.md)** | FIDEO: what makes a procedure a valid algorithm |

## Reading Order

Read 1 → 9 in order. Lesson 3 needs Lesson 2's symbols; Lesson 4 needs you to be
able to draw a fork; Lesson 5 assumes you have broken a chart at least once.
Lesson 7 assumes you can trace a loop; Lessons 8–9 build on all previous lessons.

## The Three Patterns at a Glance

Every algorithm ever written is a braid of exactly three patterns. Böhm and
Jacopini proved in 1966 that sequence, selection, and iteration are the complete
grammar of computation — you are learning the whole language, and it has three
words.

```
sequence    A → B → C
            steps in a row, one at a time, in order

selection   START → ◇ ──yes──▶ act ──┐
                  │                ├──▶ STOP
                  └───no───▶ (skip) ┘
            the diamond picks a lane

iteration   START → ◇ ──yes──▶ act ──┐
                  ▲                  │
                  └──────────────────┘
                  │                  │
                  └───no───▶ STOP ◀──┘
            a path that bends back on itself
```

## Persian Translations

Every lesson has a Persian version with identical content. Read either language,
or both.

- 📈 [چرا قبل از کدنویسی رسم می‌کنیم](01-why-draw-before-you-code_fa.md)
- 📊 [شش نماد فلوچارت](02-flowchart-symbols_fa.md)
- 🔀 [سه الگوی کنترلی](03-control-patterns_fa.md)
- 🔁 [حلقه‌ها و جدول ردیابی](04-loops-and-trace-tables_fa.md)
- ✅ [روش طراحی و چک‌لیست بازبینی](05-design-method-and-review_fa.md)
- 📝 [کارگاه: سه تمرین](06-workshop-briefs_fa.md)
- 🧮 [الگوریتم‌های کلاسیک](07-classic-algorithms_fa.md)
- 🔄 [ورودی، پردازش، خروجی و حالت](08-ipo-and-state_fa.md)
- ✔️ [ویژگی‌های الگوریتم](09-algorithm-characteristics_fa.md)

## Prerequisites

None. Paper, a pen, and a tolerance for tracing tables by hand.

## Learning Outcomes

After these nine lessons you should be able to:

1. Draw a valid flowchart obeying the five laws
2. Recognise the three patterns inside an unfamiliar algorithm
3. Spot the four organs of any loop you meet
4. Trace an algorithm on paper and find its bugs before they reach a screen
5. Turn a wordy problem into a chart using the five moves
6. Convert chart → pseudocode → code without thinking hard
7. Implement ten classic algorithms with flowcharts and pseudocode
8. Analyse problems using the IPO framework and track state
9. Evaluate procedures against the FIDEO algorithm characteristics

## Common Patterns Reference

Keep this table nearby while you draw.

| Task | Pattern | Skeleton |
|------|---------|----------|
| Greet a user | sequence | read → write |
| Add two numbers | sequence | read, read, add, write |
| Odd or even | selection | read → `N mod 2 = 0 ?` → write |
| Count to N | iteration | init → test → write → step → back |
| Sum a range | iteration + accumulator | `sum ← 0` → loop → `sum ← sum + i` |
| Password with retries | iteration + selection + counter | loop → check → granted / retry / denied |

## Prerequisites for Later

Section 0 assumes nothing, and everything later assumes it. In particular:

- **Module 4** turns these charts into Python. The translation is meant to be
  mechanical. If it feels hard, the chart was not finished.
- **Module 5** builds complete programs using the algorithms and patterns
  you have learned here.
