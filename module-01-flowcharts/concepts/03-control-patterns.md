# The Three Control Patterns

> **Lesson 3 of 9** — Sequence, selection, iteration. The complete grammar of
> computation.

---

Every algorithm ever written is a braid of exactly three patterns. In 1966 Böhm and
Jacopini proved that **sequence, selection, and iteration** are sufficient to
compute anything computable. You are learning the whole language — there are only
three words.

## Pattern nº1 — sequence

Steps in a row. One at a time, in order. No surprises — the default temperament of
a program.

```mermaid
flowchart TD
    ST(["START"]) --> A["step A"]
    A --> B["step B"]
    B --> C["step C"]
    C --> SP(["STOP"])
```

Three tiny programs, all pure sequence:

**Hello, flow** — three symbols, each doing honest work: the door in, the single
act, the door out.

```mermaid
flowchart TD
    ST(["START"]) --> WR[/"WRITE 'Hello, World!'"/]
    WR --> SP(["STOP"])
```

```
IN — nothing · DO — nothing · OUT "Hello, World!"
```

**A name worth greeting** — our first input. Note the chart says nothing about
*how* to greet: fonts, punctuation, language. That is presentation, and it belongs
to the code. The chart is only concerned with the flow of data — it comes in, it
goes out.

```python
name = input("Your name? ")
print("Hello,", name)
```

**The IPO rhythm** — Input, Process, Output. Say it out loud; it is the heartbeat
of every program ever written. A parallelogram, a rectangle, a parallelogram.

```
IN  a, b · DO  sum ← a + b · OUT  sum
```

```mermaid
flowchart TD
    ST(["START"]) --> R1[/"READ a"/]
    R1 --> R2[/"READ b"/]
    R2 --> ADD["sum ← a + b"]
    ADD --> W1[/"WRITE sum"/]
    W1 --> SP(["STOP"])
```

From a pocket calculator to a tax filing system, the skeleton never changes — only
the number of boxes between the parallelograms grows.

## Pattern nº2 — selection

The diamond picks a lane. One branch runs; the other costs nothing.

```mermaid
flowchart TD
    ST(["START"]) --> D{"condition ?"}
    D -->|yes| A["act"]
    D -->|no| B["act differently"]
    A --> SP(["STOP"])
    B --> SP

    style D fill:#fef7e0,stroke:#f9ab00
```

**Selection** is the program choosing. In a plain `if`, one branch is "do
nothing" — the flow simply flows around the box:

```mermaid
flowchart TD
    ST(["START"]) --> D{"condition ?"}
    D -->|yes| A["act"]
    D -->|no| SP(["STOP"])
    A --> SP

    style D fill:#fef7e0,stroke:#f9ab00
```

Two facts about the skipped branch:

1. It isn't slow, hidden, or lazy — it **does not execute**. Free.
2. **`elif` chains** are just decisions in a row: each "no" feeds the next
   question. Remember this when you meet FizzBuzz in
   [Lesson 7: Classic Algorithms](07-classic-algorithms.md).

> A decision with only one labelled exit is a **half-answered question**. Always
> show where the other road goes, even if it goes nowhere.

### Fork and join — the first real program

**Program nº4 — odd or even.** Two new ideas at once.

```mermaid
flowchart TD
    ST(["START"]) --> RD[/"READ N"/]
    RD --> D{"N mod 2 = 0 ?"}
    D -->|yes| EV[/"WRITE 'even'"/]
    D -->|no| OD[/"WRITE 'odd'"/]
    EV --> SP(["STOP"])
    OD --> SP

    style D fill:#fef7e0,stroke:#f9ab00
```

```
IN  N · DO  N mod 2 ? · OUT  "even" / "odd"
```

- The **fork**: the diamond sends the flow down one of two roads.
- The **join**: both roads meet again before STOP — two paths, one destination.

The question itself is the whole trick: `mod` gives the remainder after division.
A number is even exactly when the remainder after dividing by two is zero.

```python
n = int(input("n = "))
if n % 2 == 0:
    print("even")
else:
    print("odd")
```

**Your turn — the pass/fail machine.** Read a student's mark. Print "Pass" if the
mark is 50 or more, otherwise print "Fail".

```
IN  mark · DO  mark ≥ 50 ? · OUT  "Pass" / "Fail"
```

- [ ] Draw it on paper before checking anything
- [ ] Check: fork, two labelled exits, one join, one STOP
- [ ] Watch out: is the boundary mark **≥ 50** or **> 50**? Off-by-one bugs are
      born exactly here

<details>
<summary>Answer</summary>

```mermaid
flowchart TD
    ST(["START"]) --> RD[/"READ mark"/]
    RD --> D{"mark ≥ 50 ?"}
    D -->|yes| P[/"WRITE 'Pass'"/]
    D -->|no| F[/"WRITE 'Fail'"/]
    P --> SP(["STOP"])
    F --> SP

    style D fill:#fef7e0,stroke:#f9ab00
```

```python
mark = int(input("mark = "))
if mark >= 50:
    print("Pass")
else:
    print("Fail")
```

If your drawing matches the shape — fork, join, stop — you've understood
selection. The labels are details; the shape is the idea.

</details>

### Real-world selection examples

**Grade classification** — a multi-stage `if/elif/else` chain. Each "no"
feeds the next question, exactly like the `elif` chain described above.

```mermaid
flowchart TD
    ST(["START"]) --> RD[/"READ score"/]
    RD --> D1{"score ≥ 90 ?"}
    D1 -->|yes| A[/"WRITE 'A'"/]
    D1 -->|no| D2{"score ≥ 80 ?"}
    D2 -->|yes| B[/"WRITE 'B'"/]
    D2 -->|no| D3{"score ≥ 70 ?"}
    D3 -->|yes| C[/"WRITE 'C'"/]
    D3 -->|no| D4{"score ≥ 60 ?"}
    D4 -->|yes| D[/"WRITE 'D'"/]
    D4 -->|no| F[/"WRITE 'F'"/]
    A --> SP(["STOP"])
    B --> SP
    C --> SP
    D --> SP
    F --> SP

    style D1 fill:#fef7e0,stroke:#f9ab00
    style D2 fill:#fef7e0,stroke:#f9ab00
    style D3 fill:#fef7e0,stroke:#f9ab00
    style D4 fill:#fef7e0,stroke:#f9ab00
```

```
IN  score · DO  compare against 90, 80, 70, 60 · OUT  "A" / "B" / "C" / "D" / "F"
```

**Shipping cost calculator** — a small business charges by weight, with a
surcharge for express delivery.

```mermaid
flowchart TD
    ST(["START"]) --> R1[/"READ weight"/]
    R1 --> R2[/"READ express?"/]
    R2 --> D1{"weight ≤ 1 ?"}
    D1 -->|yes| C1["cost ← 5"]
    D1 -->|no| D2{"weight ≤ 5 ?"}
    D2 -->|yes| C2["cost ← 10"]
    D2 -->|no| D3{"weight ≤ 20 ?"}
    D3 -->|yes| C3["cost ← 20"]
    D3 -->|no| C4["cost ← 20 + 2/kg over 20"]
    C1 --> D4{"express ?"}
    C2 --> D4
    C3 --> D4
    C4 --> D4
    D4 -->|yes| SUR["cost ← cost + 8"]
    D4 -->|no| W[/"WRITE cost"/]
    SUR --> W
    W --> SP(["STOP"])

    style D1 fill:#fef7e0,stroke:#f9ab00
    style D2 fill:#fef7e0,stroke:#f9ab00
    style D3 fill:#fef7e0,stroke:#f9ab00
    style D4 fill:#fef7e0,stroke:#f9ab00
```

**Game level progression** — unlock the next level only if the player has
enough stars *and* has completed the previous level.

```mermaid
flowchart TD
    ST(["START"]) --> R1[/"READ stars"/]
    R1 --> R2[/"READ prev_complete?"/]
    R2 --> D1{"prev_complete ?"}
    D1 -->|no| LOCK[/"WRITE 'Locked'"/]
    D1 -->|yes| D2{"stars ≥ 3 ?"}
    D2 -->|yes| UNLOCK[/"WRITE 'Level 2 unlocked!'"/]
    D2 -->|no| D3{"stars ≥ 1 ?"}
    D3 -->|yes| PART[/"WRITE 'Partial — replay for more stars'"/]
    D3 -->|no| LOCK
    LOCK --> SP(["STOP"])
    UNLOCK --> SP
    PART --> SP

    style D1 fill:#fef7e0,stroke:#f9ab00
    style D2 fill:#fef7e0,stroke:#f9ab00
    style D3 fill:#fef7e0,stroke:#f9ab00
```

## Pattern nº3 — iteration

A path that bends back on itself. Steps repeat while a condition holds.

```mermaid
flowchart TD
    ST(["START"]) --> D{"condition ?"}
    D -->|yes| A["act"]
    A --> D
    D -->|no| SP(["STOP"])

    style D fill:#e6f4ea,stroke:#34a853
```

Covered in depth in [Loops and Trace Tables](04-loops-and-trace-tables.md), since a
loop is the one pattern you cannot get right by eye alone — it needs a table.

## The three patterns side by side

```mermaid
flowchart LR
    subgraph SEQ["sequence — steps in a row"]
        S0(["START"]) --> S1["A"] --> S2["B"] --> S3(["STOP"])
    end

    subgraph SEL["selection — a fork in the road"]
        L0(["START"]) --> L1{"?"}
        L1 -->|yes| L2["act"]
        L1 -->|no| L3(["STOP"])
        L2 --> L3
    end

    subgraph ITR["iteration — the roundabout"]
        I0(["START"]) --> I1{"?"}
        I1 -->|yes| I2["act"]
        I2 --> I1
        I1 -->|no| I3(["STOP"])
    end
```

## Recognising patterns in the wild

Take any instruction you are given and sort it into one of the three buckets. This
is the "shape" step of the design method, and it is the highest-value habit in
this section.

| Instruction | Pattern | Why |
|-------------|---------|-----|
| "Read the name, then greet them" | sequence | Two steps, no condition |
| "If the mark is below 50, fail them" | selection | One condition, two outcomes |
| "Add each of these ten numbers" | iteration | The same action, repeatedly |
| "Keep asking until the answer is right" | iteration | A test that depends on progress |
| "Sort the list, then save it" | sequence | Two steps, each complex |
| "For each student, if absent, skip" | iteration + selection | A loop wrapping a fork |

Note the last two rows. Patterns **nest**. That is the point — you are not
learning three templates, you are learning three moves you can combine.

## Quick Reference

| Pattern | Shape | Cost |
|---------|-------|------|
| **Sequence** | Straight line, no branching | One pass, in order |
| **Selection** | One fork, paths rejoin | Chosen branch only; the other costs nothing |
| **Iteration** | A path returning to an earlier test | Zero, one, or many times |

## What to take away

- Three patterns. Sequence, selection, iteration. That is the whole language
- Böhm and Jacopini proved in 1966 this is *sufficient*, not merely convenient
- A fork splits; a join reunites. Both must exist
- The skipped branch of a selection costs nothing — it does not execute
- Patterns nest; you are learning moves, not templates

## Next

**[Loops and Trace Tables](04-loops-and-trace-tables.md)** — the pattern you cannot
verify by eye, and the table that lets you verify it anyway.

---

## Persian

[سه الگوی کنترلی](03-control-patterns_fa.md)