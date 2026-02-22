# Binary Addition and Subtraction: How Computers Do Math

## Introduction: Binary Math is Like Regular Math

If you can add and subtract regular numbers, you can do it in binary too! The rules are actually simpler because you only work with 0s and 1s.

Think of binary math like working with light switches:
- **0** = Switch OFF
- **1** = Switch ON
- **Carry** = When you have too many ON switches, you pass the overflow to the next position

---

## Binary Addition: The Four Rules

### Basic Addition Table

Adding two bits gives us four possible combinations:

| A | B | Sum | Carry | Explanation |
|---|---|-----|-------|-------------|
| 0 | 0 | 0 | 0 | Nothing + Nothing = Nothing |
| 0 | 1 | 1 | 0 | Nothing + One = One |
| 1 | 0 | 1 | 0 | One + Nothing = One |
| 1 | 1 | 0 | 1 | One + One = Two (which is 10 in binary) |

### The "1 + 1" Rule

The tricky one is 1 + 1:
```
In decimal: 1 + 1 = 2
In binary:  1 + 1 = 10 (which means "two")

  1
+ 1
---
 10  (0 here, carry 1 to next column)
```

**Think of it like coins:**
- You have 2 one-dollar bills
- You exchange them for 1 two-dollar bill
- That's a "carry" to the next higher position!

---

## Adding Two Binary Numbers

### Example 1: 5 + 3

```
Convert to binary:
5 = 101
3 = 011

    ¹ ¹    (carries)
      1 0 1   (5)
    + 0 1 1   (3)
    ---------
    1 0 0 0   (8)

Let's do it column by column (right to left):

Column 0 (rightmost): 1 + 1 = 0, carry 1
Column 1: 0 + 1 + 1(carry) = 0, carry 1  
Column 2: 1 + 0 + 1(carry) = 0, carry 1
Column 3: 0 + 0 + 1(carry) = 1

Result: 1000₂ = 8₁₀ ✓ (5 + 3 = 8)
```

### Example 2: 6 + 7

```
Convert to binary:
6 = 110
7 = 111

    ¹ ¹ ¹  (carries)
      1 1 0   (6)
    + 1 1 1   (7)
    ---------
    1 1 0 1   (13)

Column 0: 0 + 1 = 1, no carry
Column 1: 1 + 1 = 0, carry 1
Column 2: 1 + 1 + 1 = 1, carry 1  (because 3 = 11 in binary)
Column 3: 0 + 0 + 1 = 1

Result: 1101₂ = 13₁₀ ✓ (6 + 7 = 13)
```

### Example 3: 10 + 5

```
10 = 1010
5  = 0101

      1 0 1 0   (10)
    + 0 1 0 1   (5)
    ---------
      1 1 1 1   (15)

Column 0: 0 + 1 = 1
Column 1: 1 + 0 = 1
Column 2: 0 + 1 = 1
Column 3: 1 + 0 = 1

Result: 1111₂ = 15₁₀ ✓ (10 + 5 = 15)
```

---

## Binary Subtraction: The Four Rules

### Basic Subtraction Table

| A | B | Result | Borrow | Explanation |
|---|---|--------|--------|-------------|
| 0 | 0 | 0 | 0 | Nothing - Nothing = Nothing |
| 1 | 0 | 1 | 0 | One - Nothing = One |
| 1 | 1 | 0 | 0 | One - One = Nothing |
| 0 | 1 | 1 | 1 | Nothing - One = One (but we need to borrow!) |

### The "0 - 1" Rule (Borrowing)

This is like regular subtraction when the top number is smaller:
```
  2  (after borrowing, becomes 1)
 10
-  1
----
   1
```

**The borrowing process:**
1. Find the nearest 1 to the left
2. That 1 becomes 0
3. All 0s between become 1s (they received 2)
4. The rightmost position gets 2 (which is 10 in binary)

---

## Subtracting Two Binary Numbers

### Example 1: 5 - 3

```
5 = 101
3 = 011

    Borrow:  0  10 (after borrowing)
      1 0 1   (5)
    - 0 1 1   (3)
    ---------
      0 1 0   (2)

Column 0: 1 - 1 = 0
Column 1: 0 - 1 (can't do, need to borrow)
          Borrow from column 2
          Column 2: 1→0, Column 1: 0→10 (binary for 2)
          Now: 10 - 1 = 1
Column 2: 0 - 0 = 0

Result: 010₂ = 2₁₀ ✓ (5 - 3 = 2)
```

### Example 2: 13 - 6

```
13 = 1101
6  = 0110

    Borrows:  0 10  0 10
      1 1 0 1   (13)
    - 0 1 1 0   (6)
    ---------
      0 1 1 1   (7)

Column 0: 1 - 0 = 1
Column 1: 0 - 1 (need to borrow)
          Borrow from column 2
          0→10 (2), 1→0
          Now: 10 - 1 = 1
Column 2: Now it's 0, need 0 - 1
          Borrow from column 3
          1→0, 0→10
          Now: 10 - 1 = 1
Column 3: 0 - 0 = 0

Result: 0111₂ = 7₁₀ ✓ (13 - 6 = 7)
```

---

## Two's Complement: The Smart Way Computers Do Subtraction

### The Big Idea

Instead of actually subtracting, computers convert subtraction into addition:
```
A - B = A + (-B)
```

**Why?** Because computer circuits are simpler when they only need to add!

### How to Make a Number Negative (Two's Complement)

**Step-by-Step Process:**
1. Start with the positive number in binary
2. **Invert** all bits (0→1, 1→0) - This is called "one's complement"
3. **Add 1** to the result

### Example: Find -5 in 4-bit Two's Complement

```
Step 1: Positive 5 in 4 bits
        5 = 0101

Step 2: Invert all bits
        0101 → 1010
        
Step 3: Add 1
        1010 + 1 = 1011

Result: -5 = 1011₂ (in 4-bit two's complement)
```

### Verify: 5 + (-5) = 0

```
    0101   (5)
  + 1011   (-5)
  --------
   10000   (16, but we only have 4 bits!)
   
In 4 bits: 0000 = 0 ✓
(The overflow 1 is discarded in fixed-width arithmetic)
```

### Example: 7 - 3 Using Two's Complement

```
Step 1: Convert -3 to two's complement (4 bits)
        3 = 0011
        Invert: 1100
        Add 1: 1101
        So -3 = 1101

Step 2: Add 7 + (-3)
        7 = 0111
       -3 = 1101
        
          1111   (carries)
        0 1 1 1
      + 1 1 0 1
      ---------
       1 0 1 0 0
       
Keep only 4 bits: 0100 = 4 ✓

Result: 7 - 3 = 4 ✓
```

### Why Two's Complement is Brilliant

| Feature | Benefit |
|---------|---------|
| Single representation of zero | No +0 and -0 confusion |
| Simple negation | Invert and add 1 |
| Same addition circuit | No separate subtractor needed |
| Natural overflow | Discard extra bit, get correct result |
| Sign bit easy to check | Leftmost bit: 0=positive, 1=negative |

---

## Signed vs Unsigned Numbers

### In 8 Bits:

**Unsigned (positive only):**
```
00000000 = 0
00000001 = 1
...
11111111 = 255
Range: 0 to 255
```

**Signed (two's complement, positive and negative):**
```
00000000 = 0
00000001 = 1
...
01111111 = 127 (maximum positive)
10000000 = -128 (minimum negative)
...
11111111 = -1

Range: -128 to 127
```

**The Rule:** In signed numbers, the leftmost bit tells you the sign.
- **0** = Positive or zero
- **1** = Negative

---

## Overflow: When Numbers Get Too Big

### What is Overflow?

When the result of an operation is too large to fit in the available bits.

### Example: 8-Bit Overflow

```
Maximum 8-bit unsigned value: 255

Try: 200 + 100 = 300
     11001000   (200)
   + 01100100   (100)
   ----------
    100101100   (300)
    
In 8 bits: 00101100 = 44 (WRONG!)

We lost the carry bit, so we got 44 instead of 300.
This is overflow!
```

### Detecting Overflow

**In unsigned addition:**
- If there's a carry out of the leftmost bit → Overflow occurred

**In signed addition:**
- If adding two positives gives a negative → Overflow
- If adding two negatives gives a positive → Overflow

---

## Practice Exercises

### Exercise 1: Binary Addition
Add these binary numbers (show carries):

1. 0011 + 0101 = _______
2. 0110 + 0011 = _______
3. 1010 + 0110 = _______
4. 1111 + 0001 = _______ (What happens?)

### Exercise 2: Binary Subtraction
Subtract these binary numbers (show borrows):

1. 1000 - 0011 = _______
2. 1101 - 0110 = _______
3. 1010 - 0101 = _______

### Exercise 3: Two's Complement
Convert these to 8-bit two's complement:

1. -5 = _______
2. -10 = _______
3. -1 = _______

### Exercise 4: Verify with Addition
Use two's complement to check:

1. 10 - 4 = ?
   - Convert -4 to two's complement
   - Add 10 + (-4)
   - Verify the result

### Exercise 5: Real-World Thinking

1. If you're using 4-bit unsigned numbers, what's the largest number you can represent?
2. If you're using 4-bit signed numbers, what's the range?
3. Why do you think modern computers use 64-bit numbers?

---

## Key Takeaways

1. **Binary addition uses four simple rules**: 0+0=0, 0+1=1, 1+0=1, 1+1=10 (0 with carry 1)

2. **Binary subtraction involves borrowing**: Like decimal, but simpler (only 0 and 1)

3. **Two's complement is how computers store negatives**: Invert bits and add 1

4. **Subtraction becomes addition**: A - B = A + (-B), using two's complement

5. **Overflow happens when results are too big**: Important to detect and handle

## Remember

### Addition Cheat Sheet
```
0 + 0 = 0
0 + 1 = 1
1 + 0 = 1
1 + 1 = 10 (write 0, carry 1)
```

### Subtraction Cheat Sheet
```
0 - 0 = 0
1 - 0 = 1
1 - 1 = 0
0 - 1 = 1 (with borrow)
```

### Two's Complement Steps
```
1. Write positive number
2. Flip all bits (0→1, 1→0)
3. Add 1
```

---

## Next Steps

- Practice more addition and subtraction problems
- Learn binary multiplication and division
- Understand how CPUs perform these operations
- Explore binary-coded decimal (BCD)
