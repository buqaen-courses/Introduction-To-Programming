# Session 5: Simple Binary Arithmetic

## Session Overview

Now that you can write numbers in binary (Session 4), it is time to do math
with them. The good news: binary arithmetic is *easier* than decimal, because
there are only four cases instead of a hundred. This session builds the mental
model of what a CPU actually does when it executes `a + b`, and introduces the
one consequence of fixed-width storage that bites every programmer eventually:
overflow.

## Key Learning Objectives

By the end of this session, you will be able to:

- **Perform** binary addition and subtraction on small numbers by hand
- **Explain** carries and why `1 + 1` produces `10`
- **Describe** at a high level how hardware adders work
- **Recognize** overflow as a consequence of fixed bit width
- **Multiply and divide** small binary numbers using shift-and-add

## Addition Is Simpler, Not Harder

There are only four combinations of two bits. Memorize the table and you have
learned all of binary addition:

| A | B | Sum | Carry | Why |
|---|---|-----|-------|-----|
| 0 | 0 | 0 | 0 | nothing + nothing = nothing |
| 0 | 1 | 1 | 0 | nothing + one = one |
| 1 | 0 | 1 | 0 | one + nothing = one |
| 1 | 1 | 0 | 1 | one + one = two, which is `10` |

The fourth row is the only interesting one. In decimal, `1 + 1 = 2` and you
write `2`. In binary there is no `2`, so the digit is `0` and the leftover
value moves one position left. That leftover is the **carry**.

## Carries in Action

Adding column by column, right to left, exactly like decimal addition:

```
    1   1   0   1        (13)
+   1   0   1   1        (11)
  ─────────────────
  1   0   1   0   0     (24)

  Step 1:  1 + 1 = 10   → write 0, carry 1
  Step 2:  0 + 1 + 1 = 10 → write 0, carry 1
  Step 3:  1 + 0 + 1 = 10 → write 0, carry 1
  Step 4:  1 + 1 + 1 = 11 → write 1, carry 1
  Step 5:  carry 1 goes to a new leading position
```

A carry is not a special case. It is the same rule every single time.

## Overflow: Why Bit Width Matters

A CPU does not have infinite space. If a register holds 4 bits, it holds 4
bits. When the answer needs a fifth, the answer is wrong:

```
    4-bit arithmetic                      what "correct" needs

        1 1 1 1   (15)                         1 1 1 1 1   (31)
    +   0 0 0 1   (1)                      +   0 0 0 0 1   (1)
    ─────────────────                    ─────────────────
      1 0 0 0 0   ← WRONG (0)              1 0 0 0 0 0   (32)

    The extra bit had nowhere to go.
```

This is not a bug in your arithmetic. It is a property of the storage. In real
code, Python's arbitrary-precision integers mean this never bites at the Python
level, but it absolutely happens in C, in embedded systems, and in network
protocols.

## 📖 Detailed Concepts

| Topic | Description |
|-------|-------------|
| **➕ [Binary Addition and Subtraction](concepts/binary-addition-subtraction.md)** | The four rules, carries, borrowing, and worked column-by-column examples |
| **✖️ [Binary Multiplication and Division](concepts/binary-multiplication-division.md)** | Shift-and-add multiplication and shift-based division |
| **🔀 [Bitwise Operations](concepts/bitwise-operations.md)** | AND, OR, XOR, NOT, and shifts on individual bits |

Start with addition. Multiplication and division reuse the carry logic.

## Main Concepts

- **Four rules**: `0+0`, `0+1`, `1+0`, `1+1` cover every possible addition
- **Carry**: the leftover value when a column's sum exceeds 1
- **Borrowing**: the subtraction mirror of a carry
- **Overflow**: the result does not fit in the available bits
- **Shift and add**: multiplication as repeated addition, with shifts instead
  of place-value columns
- **Hardware adders**: gates wired to implement exactly those four rules

## Workshop Activities

1. **Add ten pairs.** Work through ten binary additions of two 4-bit numbers.
   Include at least three that produce a carry out of the top position.
2. **Explain in pairs.** Take turns explaining binary addition to each other
   without using the words "one" and "zero". Use light switches or coins.
3. **Overflow hunt.** Your teacher gives you pairs that overflow 4 bits. For
   each, state what the answer should have been and what the machine returns.
4. **Decimal cross-check.** Add five pairs in binary, then convert both
   operands and the result to decimal and add normally. Confirm they agree.

## Homework

- **Addition sheet**: fifteen binary additions, mixed widths (3, 4, and 8 bits).
- **Overflow sheet**: six additions that overflow their stated width.
- **Reflection**: three or four sentences on how binary and decimal addition are
  alike and how they differ.
- **Optional challenge**: binary subtraction of four pairs, including one that
  requires borrowing.

## Key Takeaways

- Binary addition has four cases; decimal addition has a hundred.
- The carry is the only mechanism you need to memorize.
- Overflow comes from storage width, not from a mistake in your method.
- Shift-and-add is how multiplication reduces to addition.
- The hardware is not doing anything clever. It is applying these four rules.

## Connection to Next Session

We can now do arithmetic on numbers, but we still cannot store *text*.
[Session 6: Text Representation](../session-06/README.md) asks how a computer
encodes the letter `A`, and why one ASCII byte cannot hold a Persian or Chinese
character.

**Required Reading**: the three concept articles listed above. Start with
[Binary Addition and Subtraction](concepts/binary-addition-subtraction.md).