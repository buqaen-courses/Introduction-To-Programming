# Character Encoding: How Computers Understand Text

## Introduction: The Translation Problem

Imagine you receive a message in a language you don't understand. You need a translator! That's exactly what happens when computers work with text.

Humans use **letters, numbers, and symbols** (A, B, C, 1, 2, 3, @, #, etc.)
Computers only understand **numbers** (stored as binary)

**Character encoding** is the "translator" that converts between human text and computer numbers.

---

## Why Do We Need Encoding?

### The Computer's Challenge

A computer stores everything as numbers. To store text, we need to answer:
1. **Which number** represents each letter?
2. **How many numbers** do we need?
3. **How do we handle** different languages?

### The Solution: A Code Book

Just like a spy code book where:
- "A" might mean "Attack at dawn"
- "B" might mean "Retreat immediately"

Character encoding creates a code book where:
- 65 means "A"
- 66 means "B"
- 97 means "a"

---

## ASCII: The First Universal Code

### What is ASCII?

**ASCII** (American Standard Code for Information Interchange) was created in the 1960s as a standard way for computers to represent text.

**Key Facts:**
- Uses **7 bits** per character (128 possible characters)
- Covers: English alphabet, numbers, punctuation, control codes
- First 32 codes (0-31): Control characters (newline, tab, etc.)
- Codes 32-126: Printable characters
- Code 127: Delete character

### ASCII Table (Key Characters)

```
32 = Space      48-57 = 0-9      65-90 = A-Z      97-122 = a-z

Special symbols:
33-47: !"#$%&'()*+,-./
58-64: :;<=>?@
91-96: [\]^_`
123-126: {|}~
```

### How ASCII Works

**Example: Encoding "Hello"**
```
Letter    ASCII Code    Binary
H              65        1000001
e             101        1100101
l             108        1101100
l             108        1101100
o             111        1101111

"Hello" = 5 bytes = 40 bits
```

### The Problem with ASCII

**English-only**: Only 128 characters, mostly English.

**What about:**
- Arabic? مرحبا
- Chinese? 你好  
- Russian? Привет
- Japanese? こんにちは
- Emoji? 😀🎉

ASCII can't handle these!

---

## Extended ASCII: A Temporary Fix

### 8-Bit ASCII (256 Characters)

**Idea:** Use the 8th bit to double the characters from 128 to 256.

**The Catch:** Different regions created different versions:
- **ISO-8859-1 (Latin-1)**: Western European languages
- **Windows-1252**: Windows version with extra symbols
- **KOI8-R**: Russian/Cyrillic
- **Shift-JIS**: Japanese

### The Problem

**Document created in Russia** using KOI8-R:
```
Original: "Привет" (Hello)
```

**Opened on American computer** using ASCII:
```
Shows as: "Ð¿ÑÐ¸Ð²ÐµÑ" (garbage!)
```

**Mojibake:** When text is displayed using the wrong encoding.

---

## Unicode: One Code to Rule Them All

### The Big Idea

Create ONE standard that includes **every character** from **every language** that has ever existed.

### Unicode Code Points

Each character gets a unique **code point** (a number written as U+XXXX):

| Character | Code Point | Name |
|-----------|------------|------|
| A | U+0041 | Latin Capital Letter A |
| a | U+0061 | Latin Small Letter A |
| ا | U+0627 | Arabic Letter Alef |
| 你 | U+4F60 | CJK Unified Ideograph |
| 😀 | U+1F600 | Grinning Face Emoji |
| 🚀 | U+1F680 | Rocket |

### The Scope of Unicode

**Version 15.1 (2023):**
- **149,000+ characters**
- Covers **161 modern and historic scripts**
- Includes **emojis, symbols, mathematical notation**
- Even has **Egyptian hieroglyphics**!

### How Unicode is Organized

Unicode divides characters into **planes** (groups of 65,536 characters):

| Plane | Range | Contents |
|-------|-------|----------|
| **Basic Multilingual Plane (BMP)** | U+0000 to U+FFFF | Most common characters |
| **Supplementary Multilingual Plane** | U+10000 to U+1FFFF | Historic scripts |
| **Supplementary Ideographic Plane** | U+20000 to U+2FFFF | Additional CJK |
| **Tertiary Ideographic Plane** | U+30000 to U+3FFFF | More CJK |
| **Supplementary Special-purpose Plane** | U+E0000 to U+EFFFF | Specials |
| **Private Use Planes** | U+F0000 to U+10FFFF | Private/custom |

**95% of text uses only the BMP (first 65,536 characters).**

---

## UTF-8: Storing Unicode Efficiently

### The Challenge

Unicode needs up to 21 bits per character (for code points up to U+10FFFF). But:
- English text would waste space
- Old ASCII files should still work
- We need different sizes for different characters

### The Solution: UTF-8

**UTF-8** (Unicode Transformation Format - 8-bit) is a clever encoding:
- Uses **1 to 4 bytes** per character
- **1 byte** for ASCII characters (backward compatible!)
- **2-4 bytes** for other characters as needed

### UTF-8 Encoding Scheme

| Code Point Range | Bytes | Binary Pattern |
|------------------|-------|----------------|
| U+0000 to U+007F | 1 | 0xxxxxxx |
| U+0080 to U+07FF | 2 | 110xxxxx 10xxxxxx |
| U+0800 to U+FFFF | 3 | 1110xxxx 10xxxxxx 10xxxxxx |
| U+10000 to U+10FFFF | 4 | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx |

**The x's are filled with the actual character bits.**

### UTF-8 Examples

```
'A' (U+0041):
  Code point: 00000000 01000001
  Fits in: 0xxxxxxx range
  UTF-8:    01000001 (1 byte)

'é' (U+00E9):
  Code point: 00000000 11101001 (233)
  Fits in: 2-byte range
  UTF-8:    11000011 10101001 (0xC3 0xA9)

'中' (U+4E2D):
  Code point: 01001110 00101101 (20,013)
  Fits in: 3-byte range
  UTF-8:    11100100 10111000 10101101 (0xE4 0xB8 0xAD)

'😀' (U+1F600):
  Code point: 0001 11110110 00000000 (128,512)
  Fits in: 4-byte range
  UTF-8:    11110000 10011111 10011000 10000000 (0xF0 0x9F 0x98 0x80)
```

### Why UTF-8 Won

| Feature | Benefit |
|---------|---------|
| **Backward compatible** | Old ASCII files work without changes |
| **Self-synchronizing** | Can find character boundaries anywhere |
| **Compact for English** | Most web content is 1 byte/character |
| **Supports all Unicode** | Can encode every character |
| **No byte order issues** | Same on all computers |

**Today, 98% of web pages use UTF-8!**

---

## Other Unicode Encodings

### UTF-16

- Uses 2 or 4 bytes per character
- Common characters (BMP): 2 bytes
- Rare characters: 4 bytes (surrogate pairs)
- Used by: Windows, Java, JavaScript internally

### UTF-32

- Always uses 4 bytes per character
- Simple but wasteful
- Used when: Fixed-size characters needed

### Comparison Table

| Encoding | 'A' | 'é' | '中' | '😀' | Size vs UTF-8 |
|----------|-----|-----|------|------|-----------------|
| UTF-8 | 1 | 2 | 3 | 4 | Baseline |
| UTF-16 | 2 | 2 | 2 | 4 | 2× for ASCII |
| UTF-32 | 4 | 4 | 4 | 4 | 4× always |

**UTF-8 is almost always the best choice!**

---

## Common Encoding Problems

### Problem 1: Mojibake (Garbled Text)

**When it happens:** File encoded in UTF-8, opened as Latin-1.

**Example:**
```
Original (UTF-8): "café"
Bytes: c3 a9 (UTF-8 for é)

Opened as Latin-1:
  c3 = Ã
  a9 = ©
Result: "cafÃ©" (garbage!)
```

**Fix:** Open with correct encoding.

### Problem 2: The Byte Order Mark (BOM)

Some UTF-8 files start with invisible bytes (`EF BB BF`) to identify themselves as UTF-8.

**When good:** Helps programs detect encoding automatically.

**When bad:** Can cause problems in programming if not handled.

### Problem 3: Truncated Multi-Byte Characters

**When it happens:** Cutting a string at a specific byte count.

**Example:**
```
"café" in UTF-8: c3 a9 (2 bytes for é)
Cut after 4 bytes: "caf" + "c3"
"c3" alone is invalid UTF-8 → causes errors!
```

**Fix:** Cut at character boundaries, not byte boundaries.

---

## Programming with Encodings

### Python Examples

```python
# Encoding: String to Bytes
text = "Hello, 世界"
utf8_bytes = text.encode('utf-8')
print(utf8_bytes)  # b'Hello, \xe4\xb8\x96\xe7\x95\x8c'

# Decoding: Bytes to String
decoded = utf8_bytes.decode('utf-8')
print(decoded)  # "Hello, 世界"

# Get Unicode code point
char = 'A'
code_point = ord(char)  # 65
print(f"U+{code_point:04X}")  # U+0041

# Get character from code point
char = chr(65)  # 'A'
char = chr(0x4E2D)  # '中'

# Check encoding of a file
with open('file.txt', 'rb') as f:
    raw = f.read()
    # Try UTF-8 first
    try:
        text = raw.decode('utf-8')
    except UnicodeDecodeError:
        # Try other encodings
        text = raw.decode('latin-1')
```

### File I/O Best Practices

```python
# ALWAYS specify encoding when opening files!

# Writing with UTF-8
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write("Hello, مرحبا, 你好")

# Reading with UTF-8
with open('input.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# BAD - uses system default (could be anything!)
with open('file.txt', 'r') as f:  # Don't do this!
    content = f.read()
```

---

## Best Practices

### 1. Always Use UTF-8

```python
# Good - explicit UTF-8
with open('file.txt', 'w', encoding='utf-8') as f:
    f.write(content)

# Bad - system dependent
with open('file.txt', 'w') as f:
    f.write(content)
```

### 2. Handle Encoding Errors Gracefully

```python
try:
    with open('file.txt', 'r', encoding='utf-8') as f:
        content = f.read()
except UnicodeDecodeError:
    # Try another encoding
    with open('file.txt', 'r', encoding='latin-1') as f:
        content = f.read()
```

### 3. Declare Encoding in Source Files

```python
# At the top of Python files
# -*- coding: utf-8 -*-
```

### 4. Use UTF-8 for Databases and APIs

- Database connections: specify `charset=utf8mb4`
- HTTP headers: `Content-Type: text/html; charset=utf-8`
- HTML meta tag: `<meta charset="UTF-8">`

---

## Key Takeaways

1. **ASCII was the beginning**: 128 characters, English only
2. **Unicode solves the language problem**: 149,000+ characters for all languages
3. **UTF-8 is the modern standard**: Efficient, backward compatible, universal
4. **Always specify encoding**: Prevents mojibake and errors
5. **UTF-8 is everywhere**: 98% of web pages use it

## Remember

| Era | Encoding | Characters | Status |
|-----|----------|------------|--------|
| 1960s | ASCII | 128 | Legacy |
| 1980s | Extended ASCII | 256 | Legacy |
| 1990s | Unicode | 149,000+ | Current |
| Today | UTF-8 | All of Unicode | Standard |

---

## Next Steps

- Learn about string handling in your programming language
- Understand text normalization (NFC, NFD)
- Explore collation (sorting rules for different languages)
- Study bidirectional text (mixing left-to-right and right-to-left)
