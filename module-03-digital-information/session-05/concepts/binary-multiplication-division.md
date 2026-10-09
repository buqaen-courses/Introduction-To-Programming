# Binary Multiplication and Division: Advanced Binary Arithmetic

## Introduction: Building on Addition and Subtraction

Just like in decimal math, binary multiplication is repeated addition, and division is repeated subtraction. But because we only work with 0s and 1s, the process is actually simpler!

---

## Binary Multiplication

### The Multiplication Table (Much Simpler Than Decimal!)

| × | 0 | 1 |
|---|---|---|
| **0** | 0 | 0 |
| **1** | 0 | 1 |

**This is it!** Four rules instead of 100.

### How It Works

Binary multiplication follows the same pattern as decimal multiplication:
1. Multiply each digit of the second number by the first number
2. Shift each partial result left based on position
3. Add all partial results

### Example 1: 5 × 3

```
Decimal: 5 × 3 = 15

Binary:
  1 0 1   (5)
× 0 1 1   (3)
---------

Step 1: Multiply by rightmost bit (1)
  1 0 1 × 1 = 1 0 1
  
Step 2: Multiply by middle bit (1), shift left by 1
  1 0 1 × 1 = 1 0 1, then shift → 1 0 1 0
  
Step 3: Multiply by leftmost bit (0), shift left by 2
  1 0 1 × 0 = 0 0 0, then shift → 0 0 0 0 0
  
Step 4: Add all partial results
    0 0 1 0 1   (5)
  + 0 1 0 1 0   (10, shifted)
  + 0 0 0 0 0   (0, shifted)
  -----------
    0 1 1 1 1   (15)

Answer: 1111₂ = 15₁₀ ✓
```

### Example 2: 6 × 5

```
  1 1 0   (6)
× 1 0 1   (5)
---------

Partial products:
  1 1 0 × 1 = 0 0 1 1 0   (position 0)
  1 1 0 × 0 = 0 0 0 0 0   (position 1, shifted)
  1 1 0 × 1 = 0 1 1 0 0   (position 2, shifted)

Add:
    0 0 1 1 0
  + 0 0 0 0 0
  + 0 1 1 0 0
  -----------
    1 0 0 0 1 1  (6 + 24 = 30, but wait...)
    
Let me recheck: 6 × 5 = 30
1 0 0 0 1 1 = 32 + 2 + 1 = 35... Error!

Correction:
    0 0 1 1 0   (6)
  + 0 0 0 0 0   (0)
  + 1 1 0 0 0   (24)
  -----------
    1 1 1 1 0   (30)
    
30 = 16 + 8 + 4 + 2 = 11110 ✓
```

### The Shift-and-Add Method (How Computers Do It)

Computers use a clever trick:
- If the current bit is 1, add the multiplicand
- If the current bit is 0, add nothing
- Always shift left

```
Algorithm for A × B:
result = 0
for each bit in B (from right to left):
    if current bit is 1:
        result = result + A
    A = A << 1  (shift A left by 1)
return result
```

---

## Binary Division

### Long Division in Binary

Binary division is like decimal long division but simpler (only 0 or 1 for each digit).

### Example 1: 15 ÷ 3

```
Decimal: 15 ÷ 3 = 5

Binary:
    1 0 1  (quotient = 5)
   ------
1 1 ) 1 1 1 1  (15 ÷ 3)
      1 1      (3 × 1 = 3, subtract)
      ---
        0 1    (bring down next bit)
          0    (3 doesn't fit in 1, put 0)
          --
          0 11 (bring down next bits)
           1 1 (3 × 1 = 3, subtract)
           ---
             0 (remainder = 0)

Answer: 101₂ = 5₁₀ ✓
```

### Example 2: 20 ÷ 4

```
    1 0 1  (quotient = 5)
   ------
1 0 0 ) 1 0 1 0 0  (20 ÷ 4)
        1 0 0      (4 × 1 = 4, subtract)
        -----
          1 0 0    (bring down)
          1 0 0    (4 × 1 = 4, subtract)
          -----
              0    (remainder = 0)

Wait, that's 20 ÷ 4 = 5, not right...

Let me redo:
    0 0 0 0 1 0 1  (20 = 10100, 4 = 100)

Actually, 20 ÷ 4:
20 = 10100
4  = 00100

    0 0 1 0 1  (5)
   ------
1 0 0 ) 1 0 1 0 0
        1 0 0      (can't subtract from 1, move to 10)
        
Let's try aligned properly:
        1 0 1
       ------
      1 0 0 ) 1 0 1 0 0
            - 1 0 0    (bit 2)
            ------
              0 0 1 0  (remainder, bring down 0)
                - 0    (can't subtract, bit 1 = 0)
              -----
                0 1 0 0 (bring down 0)
              -   1 0 0  (bit 0)
              -------
                    0

Quotient: 101 = 5 ✓
```

### Example 3: 21 ÷ 5 (With Remainder)

```
21 = 10101
5  = 00101

    0 0 1 0 0  (4, with remainder)
   ------
1 0 1 ) 1 0 1 0 1
        1 0 1
        -----
          0 0 0 0  (can't subtract)
            0 0 0 1 (can't subtract)
              0 0 1 (remainder = 1)

21 ÷ 5 = 4 remainder 1 ✓
```

---

## Special Case: Multiplying/Dividing by Powers of 2

### The Fast Way: Use Bit Shifts!

This is one of the most important tricks in computing.

**Multiplication by powers of 2:**
```
Multiply by 2:  x << 1   (shift left 1)
Multiply by 4:  x << 2   (shift left 2)
Multiply by 8:  x << 3   (shift left 3)
Multiply by 16: x << 4   (shift left 4)
```

**Example:**
```
13 × 8:
13 = 00001101
13 << 3 = 01101000 = 104 ✓
(13 × 8 = 104)
```

**Division by powers of 2:**
```
Divide by 2:  x >> 1   (shift right 1)
Divide by 4:  x >> 2   (shift right 2)
Divide by 8:  x >> 3   (shift right 3)
```

**Example:**
```
100 ÷ 4:
100 = 01100100
100 >> 2 = 00011001 = 25 ✓
(100 ÷ 4 = 25)
```

### Why Shifts Are Faster

- **Multiplication/division circuits** are complex and slow
- **Shift operations** are built into the hardware and execute in one cycle
- Compilers automatically replace `× 8` with `<< 3` when possible

---

## Practical Applications

### Application 1: Screen Resolution Calculations

Calculate memory needed for a screen:
```
1920 × 1080 pixels, 4 bytes per pixel

Fast calculation:
1920 × 1080 × 4
= 1920 × (1024 + 56) × 4  [1080 = 1024 + 56]
= 1920 × 1024 × 4 + 1920 × 56 × 4

Using shifts:
1920 << 10 = 1920 × 1024 = 1,966,080
1920 × 56 × 4 = 430,080
Total: ~2.4 MB per screen
```

### Application 2: Memory Address Calculation

Arrays in memory:
```
Base address: 0x1000
Each element: 4 bytes
Element index: n

Address = Base + (n × 4)
        = Base + (n << 2)  [faster!]
```

### Application 3: Converting Between Storage Units

```
1 KB = 1024 bytes = 2^10
1 MB = 1024 KB = 2^20
1 GB = 1024 MB = 2^30

To find how many KB in 5000 bytes:
5000 >> 10 = 5000 ÷ 1024 ≈ 4 KB
```

---

## Practice Exercises

### Exercise 1: Binary Multiplication
Calculate (show your work):

1. 4 × 3 = _______
2. 7 × 2 = _______
3. 5 × 5 = _______
4. 6 × 4 = _______

### Exercise 2: Binary Division
Calculate (show quotient and remainder):

1. 12 ÷ 4 = _______
2. 15 ÷ 2 = _______
3. 20 ÷ 6 = _______
4. 31 ÷ 5 = _______

### Exercise 3: Shift Operations
Calculate using bit shifts:

1. 16 × 4 = _______ (16 << ?)
2. 32 × 8 = _______ (32 << ?)
3. 64 ÷ 4 = _______ (64 >> ?)
4. 128 ÷ 8 = _______ (128 >> ?)

### Exercise 4: Real-World Problem

**Graphics Memory Calculation:**
A game needs to store a texture that is 512 × 512 pixels, with each pixel using 4 bytes (RGBA).

1. Calculate total memory needed (in bytes)
2. Convert to KB using bit shifts
3. If you have 8 textures like this, how much memory total?

---

## Common Mistakes and Tips

### Mistake 1: Forgetting to Shift

```
Wrong:
  101
× 011
----
  101  (forgot to shift!)
  101
----
 1010  (should be 1111 = 15)

Right:
  101
× 011
----
  101   (position 0, no shift)
 1010   (position 1, shift 1)
0000    (position 2, shift 2)
----
1111   (5 + 10 = 15) ✓
```

### Mistake 2: Misaligned Division

Always align the divisor properly under the dividend!

### Tip: Verify with Decimal

After doing binary arithmetic, convert back to decimal to check your answer.

---

## Key Takeaways

1. **Binary multiplication** is simpler than decimal (only 0 and 1 to multiply)
2. **Shift and add** is how computers multiply efficiently
3. **Long division** works the same way, just with binary digits
4. **Powers of 2 are special**: Use bit shifts for instant multiplication/division
5. **Always verify**: Convert to decimal to check your answers

## Remember

| Operation | Binary Method | Fast Method |
|-----------|---------------|-------------|
| × 2 | Multiply | << 1 |
| × 4 | Multiply | << 2 |
| × 8 | Multiply | << 3 |
| ÷ 2 | Divide | >> 1 |
| ÷ 4 | Divide | >> 2 |
| ÷ 8 | Divide | >> 3 |

---

## Next Steps

- Practice more multiplication and division problems
- Learn about binary floating-point arithmetic
- Understand how CPUs handle arithmetic operations
- Explore multiplication algorithms (Booth's algorithm, etc.)
