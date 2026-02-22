# Bitwise Operations: The Power of Working with Individual Bits

## Introduction: Thinking Like a Computer

Imagine you have 8 light switches, each labeled 0 to 7. Instead of treating them all the same, you want to:
- Turn on only switch #3
- Check if switch #5 is on
- Flip the state of all switches

This is exactly what **bitwise operations** do! They let you manipulate individual bits - the smallest pieces of data in a computer.

---

## Why Learn Bitwise Operations?

### Real-World Uses

| Use Case | How Bitwise Helps |
|----------|-------------------|
| **Graphics** | Change colors, apply filters |
| **Game Development** | Store multiple flags (is player jumping? shooting? invincible?) |
| **Networking** | Check IP addresses, port numbers |
| **File Permissions** | Set read/write/execute permissions |
| **Compression** | Pack data efficiently |
| **Encryption** | Scramble data for security |
| **Performance** | Faster than regular arithmetic |

### Analogy: A Row of Light Switches

Think of an 8-bit number as 8 light switches:
```
Bit position:  7   6   5   4   3   2   1   0
Switch:       [ ] [ ] [ ] [ ] [X] [ ] [ ] [ ]
Binary:        0   0   0   0   1   0   0   0   = 8

Only switch #3 (position 3) is ON
```

---

## The Six Basic Bitwise Operations

### 1. AND (&): Both Must Be ON

**Rule:** The result is 1 only if **both** bits are 1.

| A | B | A & B |
|---|---|-------|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

**Think of it like:** Two people both need to approve something.

**Example:**
```
  11001100    (204)
& 10101010    (170)
----------
  10001000    (136)
  
Only positions where BOTH have 1 stay as 1
```

**Practical Use:** Masking (hiding bits you don't care about)

---

### 2. OR (|): At Least One ON

**Rule:** The result is 1 if **either** bit is 1.

| A | B | A \| B |
|---|---|-------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

**Think of it like:** Either person can approve.

**Example:**
```
  11001100    (204)
| 10101010    (170)
----------
  11101110    (238)
  
Any position with at least one 1 stays as 1
```

**Practical Use:** Setting flags (turning bits ON)

---

### 3. XOR (^): Different Bits

**Rule:** The result is 1 if the bits are **different**.

| A | B | A ^ B |
|---|---|-------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

**Think of it like:** "Are these different?"

**Example:**
```
  11001100    (204)
^ 10101010    (170)
----------
  01100110    (102)
  
Positions where bits differ become 1
```

**Practical Use:**
- Toggling bits (flip on to off, off to on)
- Simple encryption (XOR with a key)
- Finding differences between two values

---

### 4. NOT (~): Flip All Bits

**Rule:** Turn every 0 to 1, and every 1 to 0.

| A | ~A |
|---|----|
| 0 | 1 |
| 1 | 0 |

**Example:**
```
~ 00001111    (15)
----------
  11110000    (240 in 8-bit unsigned)
  
All bits flipped
```

**Note:** In programming, the result depends on how many bits your number uses (8-bit, 16-bit, 32-bit, etc.)

---

### 5. Left Shift (<<): Move Bits Left

**Rule:** Shift all bits to the left, fill right with 0s.

**Effect:** Each left shift multiplies by 2!

**Example:**
```
00000101 (5)
<< 1
--------
00001010 (10)  = 5 × 2

00000101 (5)
<< 2
--------
00010100 (20)  = 5 × 4

00000101 (5)
<< 3
--------
00101000 (40)  = 5 × 8
```

**Practical Use:**
- Fast multiplication by powers of 2
- Setting up bit masks
- Creating flags

---

### 6. Right Shift (>>): Move Bits Right

**Rule:** Shift all bits to the right, fill left with 0s (or sign bit for signed numbers).

**Effect:** Each right shift divides by 2!

**Example (Unsigned):**
```
00010100 (20)
>> 1
--------
00001010 (10)  = 20 ÷ 2

00010100 (20)
>> 2
--------
00000101 (5)   = 20 ÷ 4
```

**Practical Use:**
- Fast division by powers of 2
- Extracting specific bits
- Unpacking compressed data

---

## Practical Applications

### Application 1: Checking if a Number is Even or Odd

**The Trick:** Look at the rightmost bit (bit 0)
- 0 = Even
- 1 = Odd

```python
# Check if number is even
def is_even(number):
    return (number & 1) == 0

# Check if number is odd  
def is_odd(number):
    return (number & 1) == 1

# Examples:
is_even(4)   # 4 & 1 = 0, returns True ✓
is_even(7)   # 7 & 1 = 1, returns False ✓
is_odd(7)    # 7 & 1 = 1, returns True ✓
```

**How it works:**
```
4 = 100
1 = 001
& = 000 = 0 → Even!

7 = 111
1 = 001
& = 001 = 1 → Odd!
```

---

### Application 2: Setting a Specific Bit

**Goal:** Turn ON a specific bit (position n)

```python
def set_bit(number, position):
    return number | (1 << position)

# Examples:
set_bit(0b0000, 2)   # Set bit 2
# 1 << 2 = 0b0100
# 0b0000 | 0b0100 = 0b0100 = 4

set_bit(0b1000, 0)   # Set bit 0
# 1 << 0 = 0b0001
# 0b1000 | 0b0001 = 0b1001 = 9
```

---

### Application 3: Clearing a Specific Bit

**Goal:** Turn OFF a specific bit (position n)

```python
def clear_bit(number, position):
    return number & ~(1 << position)

# Examples:
clear_bit(0b1111, 2)  # Clear bit 2
# 1 << 2 = 0b0100
# ~0b0100 = 0b1011 (in 4 bits)
# 0b1111 & 0b1011 = 0b1011 = 11
```

---

### Application 4: Toggling a Bit

**Goal:** Flip a bit (ON→OFF or OFF→ON)

```python
def toggle_bit(number, position):
    return number ^ (1 << position)

# Examples:
toggle_bit(0b1010, 0)  # Toggle bit 0
# 0b1010 ^ 0b0001 = 0b1011 = 11
# Was 0, now 1

toggle_bit(0b1011, 0)  # Toggle bit 0 again
# 0b1011 ^ 0b0001 = 0b1010 = 10
# Was 1, now 0
```

---

### Application 5: Checking if a Bit is Set

**Goal:** Is a specific bit ON?

```python
def is_bit_set(number, position):
    return (number & (1 << position)) != 0

# Examples:
is_bit_set(0b1010, 1)  # Check bit 1
# 0b1010 & 0b0010 = 0b0010 != 0 → True

is_bit_set(0b1010, 0)  # Check bit 0
# 0b1010 & 0b0001 = 0b0000 == 0 → False
```

---

### Application 6: File Permissions (Unix Style)

In Unix/Linux systems, file permissions use 3 bits for each of 3 groups:

```
Permissions format: rwx rwx rwx
                    │   │   │
                  owner group others

r = read    (4) = 100
w = write   (2) = 010
x = execute (1) = 001
```

**Common permission values:**
```
7 = 111 = rwx (read, write, execute)
6 = 110 = rw- (read, write, no execute)
5 = 101 = r-x (read, no write, execute)
4 = 100 = r-- (read only)
0 = 000 = --- (no permissions)

Permission 755 = rwxr-xr-x
  Owner:  7 = 111 = rwx
  Group:  5 = 101 = r-x
  Others: 5 = 101 = r-x
```

**Checking permissions with bitwise:**
```python
def can_read(permissions):
    return (permissions & 4) != 0  # Check read bit

def can_write(permissions):
    return (permissions & 2) != 0  # Check write bit

def can_execute(permissions):
    return (permissions & 1) != 0  # Check execute bit

# Example: Check if owner can write
owner_perms = 7  # rwx
if can_write(owner_perms):
    print("Can write!")
```

---

### Application 7: Storing Multiple Boolean Flags

Instead of using multiple boolean variables, pack them into one integer:

```python
# Define flags
IS_VISIBLE = 1 << 0    # Bit 0
IS_ENABLED = 1 << 1    # Bit 1  
IS_HOVERED = 1 << 2    # Bit 2
IS_CLICKED = 1 << 3    # Bit 3

# Set multiple flags
button_state = IS_VISIBLE | IS_ENABLED
# 0001 | 0010 = 0011

# Check if specific flag is set
if button_state & IS_VISIBLE:
    print("Button is visible")

# Add a flag
button_state |= IS_HOVERED
# 0011 | 0100 = 0111

# Remove a flag
button_state &= ~IS_ENABLED
# 0111 & 1101 = 0101
```

**Memory savings:**
- 4 separate booleans: 4 bytes (typically)
- 1 integer with 4 flags: 4 bytes
- But you can pack 32 flags into one 32-bit integer!

---

## Common Bit Masks

### What is a Mask?

A **mask** is a pattern of bits used to select or modify specific bits.

### Common Masks

| Purpose | Mask (8-bit) | Description |
|---------|--------------|-------------|
| Lower 4 bits | 00001111 | Keep only bits 0-3 |
| Upper 4 bits | 11110000 | Keep only bits 4-7 |
| Even bits | 01010101 | Keep bits 0, 2, 4, 6 |
| Odd bits | 10101010 | Keep bits 1, 3, 5, 7 |
| Single bit | 00001000 | Keep only bit 3 |

### Using Masks

```python
# Extract lower 4 bits
value = 0b10110101
lower_4 = value & 0b00001111
# Result: 0b00000101 = 5

# Extract upper 4 bits
upper_4 = (value & 0b11110000) >> 4
# Result: 0b00001011 = 11
```

---

## Practice Exercises

### Exercise 1: AND, OR, XOR
Calculate these by hand:

1. 1100 & 1010 = _______
2. 1100 | 1010 = _______
3. 1100 ^ 1010 = _______
4. ~1100 (4-bit) = _______

### Exercise 2: Shifts
Calculate:

1. 00001011 << 2 = _______
2. 00001011 >> 2 = _______
3. 00110000 >> 4 = _______

### Exercise 3: Bit Manipulation
For number = 0b10101100:

1. Set bit 1: _______
2. Clear bit 6: _______
3. Toggle bit 3: _______
4. Check if bit 4 is set: _______

### Exercise 4: Real-World Scenario

**Color Extraction:**
A pixel's color is stored as 0xFF5733 (orange). This is RGB format:
- Red: FF (bits 16-23)
- Green: 57 (bits 8-15)
- Blue: 33 (bits 0-7)

Extract each color component using bit shifts and masks.

---

## Key Takeaways

1. **AND (&)** keeps bits where both are 1 - used for masking
2. **OR (|)** keeps bits where either is 1 - used for setting
3. **XOR (^)** keeps bits where they're different - used for toggling
4. **NOT (~)** flips all bits - used for inverting
5. **Shifts (<<, >>)** move bits left/right - used for multiplication/division by 2
6. **Bitwise is fast** - operations happen at the hardware level

## Remember

| Operation | Symbol | Use When You Want To... |
|-----------|--------|------------------------|
| AND | & | Check if bits are both set, mask bits |
| OR | \| | Set bits to 1 |
| XOR | ^ | Toggle bits, find differences |
| NOT | ~ | Invert all bits |
| Left Shift | << | Multiply by 2, move bits left |
| Right Shift | >> | Divide by 2, move bits right |

---

## Next Steps

- Practice bit manipulation problems
- Learn about flags and masks in real code
- Explore bitwise operations in your programming language
- Study how graphics use bitwise for color manipulation
