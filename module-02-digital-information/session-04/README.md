# Session 4: Number Bases – Binary, Decimal, Hexadecimal

## Session Overview

Every number you have ever written assumes ten fingers. Computers assume a
different number. Once you see that a "base" is just a choice about how many
digits a counting system has, binary and hexadecimal stop being strange and
start being convenient. This session builds directly on the bits and bytes from
Session 3: those bits are grouped into positions, and each position carries a
weight in whatever base you are using.

## Key Learning Objectives

By the end of this session, you will be able to:

- **Explain** what a number base is and why computers use base 2
- **Convert** small numbers between decimal and binary by hand
- **Recognize** hexadecimal notation and state why it exists
- **Relate** a 4-bit binary group to one hexadecimal digit
- **Read** a byte written in hex and unpack it into bits

## Why Bases Matter

The digits `0` through `9` are not the numbers themselves. They are *symbols*
for ten different quantities. Change the symbols to `0` and `1` and you get a
system that counts the same quantities differently.

```
                  THE SAME QUANTITY, THREE BASES

    Decimal            Binary             Hexadecimal
    ───────            ───────            ───────────
        0                  0                    0
        1                  1                    1
        2                 10                    2
        3                 11                    3
        4                100                    4
        5                101                    5
        6                110                    6
        7                111                    7
        8               1000                    8
        9               1001                    9
       10               1010                    A
       11               1011                    B
       12               1100                    C
       13               1101                    D
       14               1110                    E
       15               1111                    F
       16              10000                   10
```

Note the rightmost column: after `9`, decimal and binary both need a new
symbol, but hex jumps straight to `A`. That is the whole reason hex exists.

## Place Value Is the Mechanism

In any base `b`, each position multiplies by `b`:

```
        Decimal            Binary            Hexadecimal
        ───────            ───────            ───────────
    1s  10⁰ = 1          2⁰ = 1             16⁰ =  1
   10s  10¹ = 10         (does not exist)   (does not exist)
  100s  10² = 100        (does not exist)   (does not exist)
 1000s  10³ = 1000       2³ = 8             16³ = 4096
        ───────          ───────             ───────
        base 10           base 2              base 16
```

Binary has no second column because `2¹ = 2` is already "ten" in that system.
Hex skips straight from `16⁰` to `16³` because it borrows the missing columns
from decimal.

## The Four-Bit Bridge

This is the single most useful fact in the session:

```
    4 binary bits  =  1 hexadecimal digit     (because 2⁴ = 16)

    ┌────┬────┬────┬────┐        ┌────┬────┬────┬────┐
    │  8 │  4 │  2 │  1 │        │  8 │  4 │  2 │  1 │   <- bit weights
    └────┴────┴────┴────┘        └────┴────┴────┴────┘

     Binary        Hex      Binary        Hex      Binary        Hex
     0000           0        0100           4        1000           8
     0001           1        0101           5        1001           9
     0010           2        0110           6        1010           A
     0011           3        0111           7        1011           B
                    ... and on to 1111 = F
```

A byte is two of these groups. That is why you will meet byte patterns like
`10101100` and their hex form `AC` throughout the rest of the course.

## 📖 Detailed Concepts

| Topic | Description |
|-------|-------------|
| **🔢 [Binary Number System](concepts/binary-number-system.md)** | How counting with only 0 and 1 works, and why computers chose it |
| **🔄 [Decimal-Binary Conversion](concepts/decimal-binary-conversion.md)** | Step-by-step methods for converting in both directions |
| **🔡 [Hexadecimal System](concepts/hexadecimal-system.md)** | Binary's shorthand, and how to read a byte at a time |

Start with the binary number system, then conversion, then hexadecimal. Each
one assumes the previous.

## Main Concepts

- **Base 10 (decimal)**: the digits `0`–`9`, place values 1, 10, 100, 1000
- **Base 2 (binary)**: the digits `0` and `1`, place values 1, 2, 4, 8, 16
- **Base 16 (hexadecimal)**: digits `0`–`9` plus `A`–`F`, place values 1, 16, 256
- **Place value**: the rule that makes `101` mean one-hundred-and-one in
  decimal but five in binary
- **The 4-bit bridge**: four binary positions equal exactly one hex digit

## Workshop Activities

1. **Physical place-value blocks.** Using cards or coins labelled 8, 4, 2, 1,
   build the number 13 in binary. Then rebuild the same quantity in decimal
   with blocks labelled 10, 1. Notice how the physical objects are the same
   and only the block sizes changed.
2. **Convert in pairs.** Convert the decimal numbers 0–31 to binary. Time each
   other. Then reverse the task for eight of the numbers.
3. **Bytes to hex.** Convert these bytes to hexadecimal and back:
   `10101100`, `11110000`, `01010101`, `00001111`.
4. **Spot the odd one.** A classmate writes a number in binary. Without
   converting it, predict whether it is larger or smaller than 1000 in decimal.
   Then check.

## Homework

- **Conversion drills**: fifteen numbers to convert between binary and decimal,
  and five between binary and hexadecimal.
- **Explain in words**: write four sentences describing how you would convert
  13 from decimal to binary. Assume the reader has never seen the method.
- **Challenge**: convert `11010110₂` to decimal and to hexadecimal, showing
  each intermediate step.
- **Reflection**: one paragraph on why a computer programmer would ever want
  hexadecimal instead of just binary.

## Key Takeaways

- A base is a counting convention, not a different set of numbers.
- Base 2 exists because electronic circuits are cheapest with two states.
- Base 16 exists because 2⁴ = 16, so four bits collapse into one digit.
- Place value is the single rule that makes every conversion mechanical.
- Converting by hand now saves you guessing later when a value looks wrong.

## Connection to Next Session

You can now *write* numbers in binary, but you cannot yet *do math* with them.
[Session 5: Simple Binary Arithmetic](../session-05/README.md) adds the four
addition rules, carries, and overflow — how a CPU actually adds.

**Required Reading**: the three concept articles listed above. Start with
[Binary Number System](concepts/binary-number-system.md).