# Binary Number System: How Computers Count with Just Two Digits

## Introduction: Why Do Computers Use Only 0 and 1?

Imagine you had to count using only your two hands - not ten fingers, just "hand up" or "hand down." It would be slow, right? But what if you had billions of hands that could flip up or down instantly? That's exactly how computers work!

Computers use the **binary number system** because:
- They're made of electronic switches (transistors)
- Each switch can only be ON or OFF
- ON = 1, OFF = 0
- This two-state system is extremely reliable

---

## Understanding Number Systems

### Decimal: The System We Know (Base 10)

We humans use decimal because we have 10 fingers:
- **Digits**: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
- **Base**: 10
- **Place values**: ones, tens, hundreds, thousands...

**Example: The number 4,237**
```
  4     2     3     7
thousands hundreds tens ones
│      │      │      │
4×1000 + 2×100 + 3×10 + 7×1
│      │      │      │
4000 + 200 + 30 + 7 = 4,237
```

### Binary: The Computer's Language (Base 2)

Computers use binary with just two digits:
- **Digits**: 0 and 1
- **Base**: 2
- **Place values**: ones, twos, fours, eights, sixteens...

**Key insight**: Instead of powers of 10, we use powers of 2!

---

## Binary Place Values

### The Pattern of Powers of 2

Each position in a binary number represents a power of 2:

| Position | Power of 2 | Decimal Value |
|----------|------------|---------------|
| 0 | 2⁰ | 1 |
| 1 | 2¹ | 2 |
| 2 | 2² | 4 |
| 3 | 2³ | 8 |
| 4 | 2⁴ | 16 |
| 5 | 2⁵ | 32 |
| 6 | 2⁶ | 64 |
| 7 | 2⁷ | 128 |
| 8 | 2⁸ | 256 |

**Pattern**: Each number is double the previous one!

### Visual: An 8-Bit Binary Number

```
Position:   7    6    5    4    3    2    1    0
Bit:        1    0    1    0    1    0    1    0
Value:    128   64   32   16    8    4    2    1
          ─────────────────────────────────────────
Calculation:
128 + 0 + 32 + 0 + 8 + 0 + 2 + 0 = 170

So: 10101010₂ = 170₁₀
```

---

## Converting Binary to Decimal

### The Simple Method

1. Write down the place values
2. Where there's a 1, add that place value
3. Where there's a 0, skip it
4. Sum the values

### Practice Examples

**Example 1: Convert 00001101 to decimal**
```
Position:  7   6   5   4   3   2   1   0
Bit:       0   0   0   0   1   1   0   1
Value:   128  64  32  16   8   4   2   1

Add the 1s: 8 + 4 + 1 = 13
```

**Example 2: Convert 10000001 to decimal**
```
Position:  7   6   5   4   3   2   1   0
Bit:       1   0   0   0   0   0   0   1
Value:   128  64  32  16   8   4   2   1

Add the 1s: 128 + 1 = 129
```

**Example 3: Convert 11111111 to decimal**
```
Position:  7   6   5   4   3   2   1   0
Bit:       1   1   1   1   1   1   1   1
Value:   128  64  32  16   8   4   2   1

Add all: 128+64+32+16+8+4+2+1 = 255
```

---

## Converting Decimal to Binary

### Method 1: Subtraction (Easy for Beginners)

Find the largest power of 2 that fits, subtract, repeat:

**Example: Convert 45 to binary**
```
Step 1: Largest power of 2 ≤ 45 is 32 (2⁵)
        45 - 32 = 13 → put 1 in position 5

Step 2: Largest power of 2 ≤ 13 is 8 (2³)
        13 - 8 = 5 → put 1 in position 3

Step 3: Largest power of 2 ≤ 5 is 4 (2²)
        5 - 4 = 1 → put 1 in position 2

Step 4: Largest power of 2 ≤ 1 is 1 (2⁰)
        1 - 1 = 0 → put 1 in position 0

Result:    0  0  1  0  1  1  0  1
Position:  7  6  5  4  3  2  1  0
          (fill 0s where we didn't use)

45₁₀ = 00101101₂
```

### Method 2: Division by 2 (Traditional Method)

Divide by 2 repeatedly, note the remainders, read bottom-up:

**Example: Convert 42 to binary**
```
42 ÷ 2 = 21 remainder 0 ↑ (read up)
21 ÷ 2 = 10 remainder 1 ↑
10 ÷ 2 = 5  remainder 0 ↑
5  ÷ 2 = 2  remainder 1 ↑
2  ÷ 2 = 1  remainder 0 ↑
1  ÷ 2 = 0  remainder 1 ↑ (start here)

Reading from bottom: 101010

42₁₀ = 101010₂
```

---

## Counting in Binary

### Binary Counting Table (0-15)

| Decimal | Binary | Decimal | Binary |
|---------|--------|---------|--------|
| 0 | 0000 | 8 | 1000 |
| 1 | 0001 | 9 | 1001 |
| 2 | 0010 | 10 | 1010 |
| 3 | 0011 | 11 | 1011 |
| 4 | 0100 | 12 | 1100 |
| 5 | 0101 | 13 | 1101 |
| 6 | 0110 | 14 | 1110 |
| 7 | 0111 | 15 | 1111 |

**Pattern to notice:**
- The rightmost bit flips every number (0,1,0,1,0,1...)
- The next bit flips every 2 numbers
- The next bit flips every 4 numbers
- The next bit flips every 8 numbers

### How High Can 8 Bits Count?

With 8 bits (one byte), the maximum number is:
```
11111111₂ = 128+64+32+16+8+4+2+1 = 255
```

**Formula:** Maximum value with n bits = 2ⁿ - 1
- 8 bits: 2⁸ - 1 = 255
- 16 bits: 2¹⁶ - 1 = 65,535
- 32 bits: 2³² - 1 = 4,294,967,295

---

## Binary Addition

### The Four Rules

| A | B | Sum | Carry |
|---|---|-----|-------|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

**Remember:** 1 + 1 = 10 in binary (which is "2" in decimal)

### Example: 5 + 3
```
    1 0 1  (5)
  + 0 1 1  (3)
  ---------
  
  Step 1: Right column: 1 + 1 = 0, carry 1
  Step 2: Middle: 0 + 1 + 1(carry) = 0, carry 1
  Step 3: Left: 1 + 0 + 1(carry) = 0, carry 1
  Step 4: Write the final carry
  
    ¹ ¹ ¹  (carries)
      1 0 1
    + 0 1 1
    -------
    1 0 0 0  (8)
    
  5 + 3 = 8 ✓
```

### Example: 7 + 5
```
    ¹ ¹ ¹
      1 1 1  (7)
    + 1 0 1  (5)
    ---------
    1 1 0 0  (12)
    
  7 + 5 = 12 ✓
```

---

## Binary Subtraction

### The Four Rules

| A | B | Result | Borrow |
|---|---|--------|--------|
| 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 (from next column) |

**Remember:** When you see 0 - 1, you must borrow from the left!

### Example: 5 - 3
```
    1 0 1  (5)
  - 0 1 1  (3)
  ---------
  
  Right: 1 - 1 = 0
  Middle: 0 - 1 (need to borrow) → 10 - 1 = 1
  Left: 1 became 0, 0 - 0 = 0
  
  Result: 0 1 0 = 2
  
  5 - 3 = 2 ✓
```

---

## Real-World: Where You See Binary

### 1. File Sizes (Bytes)
```
1 KB = 1024 bytes = 1024 × 8 bits = 8,192 bits
```

### 2. Display Colors
```
RGB values are stored as binary:
- Red: 255 = 11111111
- Green: 128 = 10000000
- Blue: 0 = 00000000
```

### 3. IP Addresses
```
IP address: 192.168.1.1
In binary:  11000000.10101000.00000001.00000001
```

### 4. Permissions (Unix/Linux)
```
Read (4) + Write (2) + Execute (1) = Permissions
111 = 7 = rwx (read, write, execute)
101 = 5 = r-x (read, no write, execute)
```

---

## Hexadecimal: Binary's Shorthand

### Why Hexadecimal?

Binary numbers get very long. **Hexadecimal (base 16)** makes them shorter and easier to read.

| Hex | Decimal | Binary |
|-----|---------|--------|
| 0 | 0 | 0000 |
| 1 | 1 | 0001 |
| 2 | 2 | 0010 |
| 3 | 3 | 0011 |
| 4 | 4 | 0100 |
| 5 | 5 | 0101 |
| 6 | 6 | 0110 |
| 7 | 7 | 0111 |
| 8 | 8 | 1000 |
| 9 | 9 | 1001 |
| A | 10 | 1010 |
| B | 11 | 1011 |
| C | 12 | 1100 |
| D | 13 | 1101 |
| E | 14 | 1110 |
| F | 15 | 1111 |

### Conversion: Binary to Hex

**Key rule:** Every 4 bits = 1 hex digit

**Example:** Convert 10101101 to hex
```
Binary:  1010  1101
         ↓     ↓
Hex:      A     D

10101101₂ = AD₁₆
```

**Example:** Convert 111100001111 to hex
```
Binary:  1111  0000  1111
         ↓     ↓     ↓
Hex:      F     0     F

111100001111₂ = F0F₁₆
```

### Where You See Hexadecimal

1. **Color codes in web design**
   ```
   Red: #FF0000
   Blue: #0000FF
   Purple: #FF00FF
   ```

2. **Memory addresses**
   ```
   0x7FFF_A000 (a typical memory address)
   ```

3. **MAC addresses**
   ```
   00:1A:2B:3C:4D:5E
   ```

---

## Practice Exercises

### Exercise 1: Binary to Decimal
Convert these binary numbers to decimal:

1. 00001111 = _______
2. 00110011 = _______
3. 10000001 = _______
4. 11110000 = _______
5. 01010101 = _______

### Exercise 2: Decimal to Binary
Convert these decimal numbers to 8-bit binary:

1. 25 = _______
2. 100 = _______
3. 200 = _______
4. 127 = _______
5. 1 = _______

### Exercise 3: Binary Addition
Add these binary numbers:

1. 0011 + 0101 = _______
2. 0111 + 0001 = _______
3. 1010 + 0110 = _______

### Exercise 4: Binary to Hex
Convert these binary numbers to hexadecimal:

1. 11110000 = _______
2. 10101010 = _______
3. 00001111 = _______

---

## Key Takeaways

1. **Binary uses only 0 and 1**: Matches computer hardware
2. **Each position is a power of 2**: 1, 2, 4, 8, 16, 32, 64, 128...
3. **Converting is a learned skill**: Practice makes it easy!
4. **8 bits = 1 byte**: Standard unit for storing one character
5. **Hexadecimal is binary's shorthand**: Every 4 bits = 1 hex digit

## Remember These Patterns

| Binary | Decimal | Pattern |
|--------|---------|---------|
| 0001 | 1 | 2⁰ |
| 0010 | 2 | 2¹ |
| 0100 | 4 | 2² |
| 1000 | 8 | 2³ |
| 1111 | 15 | All bits on |
| 0000 | 0 | All bits off |

---

## Next Steps

- Practice converting numbers daily
- Learn binary subtraction and multiplication
- Understand how negative numbers are stored
- Explore hexadecimal in color codes and memory addresses
