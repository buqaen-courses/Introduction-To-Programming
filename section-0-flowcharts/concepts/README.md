# Section 0 Concepts: Flowcharts

Six lessons that teach you to design algorithms visually before you write them in
code. This is a primer for the whole course, not a substitute for
[Session 9](../../module-03-algorithmic-thinking/session-09/README.md).

## Table of Contents

| # | Lesson | Covers |
|---|--------|--------|
| 1 | **[Why Draw Before You Code](why-draw-before-you-code.md)** | Separating logic from syntax; the standard; cheaper bugs |
| 2 | **[The Six Symbols](flowchart-symbols.md)** | Terminator, process, I/O, decision, flow lines, connectors, the five laws |
| 3 | **[The Three Control Patterns](control-patterns.md)** | Sequence, selection, iteration; fork and join; the whole grammar |
| 4 | **[Loops and Trace Tables](loops-and-trace-tables.md)** | Four organs of a loop; counters and accumulators; dry running |
| 5 | **[Design Method and Review Checklist](design-method-and-review.md)** | Five moves; four ways charts break; the checklist |
| 6 | **[Workshop: Three Briefs](workshop-briefs.md)** | Three exercises with hints and an answer key |

## Reading Order

Read 1 → 6 in order. Lesson 3 needs Lesson 2's symbols; Lesson 4 needs you to be
able to draw a fork; Lesson 5 assumes you have broken a chart at least once.

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

- 📈 [چرا قبل از کدنویسی رسم می‌کنیم](why-draw-before-you-code_fa.md)
- 📊 [شش نماد فلوچارت](flowchart-symbols_fa.md)
- 🔀 [سه الگوی کنترلی](control-patterns_fa.md)
- 🔁 [حلقه‌ها و جدول ردیابی](loops-and-trace-tables_fa.md)
- ✅ [روش طراحی و چک‌لیست بازبینی](design-method-and-review_fa.md)
- 📝 [کارگاه: سه تمرین](workshop-briefs_fa.md)

## Prerequisites

None. Paper, a pen, and a tolerance for tracing tables by hand.

## Learning Outcomes

After these six lessons you should be able to:

1. Draw a valid flowchart obeying the five laws
2. Recognise the three patterns inside an unfamiliar algorithm
3. Spot the four organs of any loop you meet
4. Trace an algorithm on paper and find its bugs before they reach a screen
5. Turn a wordy problem into a chart using the five moves
6. Convert chart → pseudocode → code without thinking hard

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

- **Module 3, Session 9** extends this material with pseudocode and algorithm
  analysis. The ten classic algorithms — FizzBuzz, prime test, GCD, binary
  search, bubble sort — are taught there, not here.
- **Module 4** turns these charts into Python. The translation is meant to be
  mechanical. If it feels hard, the chart was not finished.