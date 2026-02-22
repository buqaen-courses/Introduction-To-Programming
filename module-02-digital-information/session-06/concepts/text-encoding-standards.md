# Text Encoding Standards: The Rules of Digital Text

## Introduction: Why Standards Matter

Imagine if every country used different rules for writing addresses. One puts the street first, another puts the city first. Chaos! 

Text encoding standards exist so that when you save a document on your computer, someone else can open it on theirs and see exactly what you wrote. Without standards, digital text would be a mess of incomprehensible symbols.

---

## The Evolution of Text Encoding

### Timeline of Major Standards

```
1963: ASCII (7-bit, 128 characters)
  ↓
1980s: Extended ASCII variants (8-bit, 256 characters, different per region)
  ↓
1991: Unicode 1.0 (16-bit, 65,536 characters planned)
  ↓
1992: UTF-8 invented (variable-length encoding)
  ↓
2008: UTF-8 becomes dominant web encoding
  ↓
Today: UTF-8 is used by 98% of web pages
```

---

## ASCII: The Foundation (1963)

### What Made ASCII Revolutionary

Before ASCII, every computer manufacturer used their own encoding:
- IBM had EBCDIC
- CDC had their own system
- Teletypes had different codes

**ASCII unified them all.**

### ASCII Structure (7-bit = 128 characters)

```
Codes 0-31:   Control characters (non-printable)
Code 32:      Space
Codes 33-47:  !"#$%&'()*+,-./
Codes 48-57:  0-9
Codes 58-64:  :;<=>?@
Codes 65-90:  A-Z
Codes 91-96:  [\]^_`
Codes 97-122: a-z
Codes 123-126: {|}~
Code 127:     DEL (Delete)
```

### Control Characters (Important Ones)

| Code | Abbreviation | Name | Purpose |
|------|--------------|------|---------|
| 0 | NUL | Null | End of string in C |
| 7 | BEL | Bell | Make a beep sound |
| 8 | BS | Backspace | Delete previous character |
| 9 | TAB | Horizontal Tab | Indent text |
| 10 | LF | Line Feed | New line (Unix) |
| 13 | CR | Carriage Return | Return to start of line |
| 27 | ESC | Escape | Start escape sequences |
| 127 | DEL | Delete | Delete character |

### ASCII Limitations

- **Only English**: No accented characters (é, ñ, ü)
- **No currency**: No €, ¥, £ (well, £ is there at 163 in some variants)
- **No math symbols**: No ±, ×, ÷
- **No box drawing**: No lines and corners

---

## Extended ASCII: The Tower of Babel (1980s)

### The Problem

Everyone wanted more characters, but the 8th bit gave only 128 more slots. Different regions chose differently.

### Major Extended ASCII Variants

| Name | Region | Year | Notable Features |
|------|--------|------|------------------|
| ISO-8859-1 (Latin-1) | Western Europe | 1987 | Covers most Western European languages |
| ISO-8859-2 (Latin-2) | Central Europe | 1987 | Polish, Czech, Hungarian |
| ISO-8859-5 | Cyrillic | 1988 | Russian, Bulgarian |
| ISO-8859-6 | Arabic | 1987 | Arabic script |
| ISO-8859-7 | Greek | 1987 | Greek alphabet |
| ISO-8859-8 | Hebrew | 1988 | Hebrew alphabet |
| Windows-1252 | Windows Western | 1992 | Microsoft's variant of Latin-1 |
| KOI8-R | Russia | 1993 | Popular in Russian internet |
| Shift-JIS | Japan | 1997 | Japanese characters |
| GB2312/GBK | China | 1980/1995 | Chinese characters |

### ISO-8859-1 (Latin-1) Character Ranges

```
0x00-0x7F:   Same as ASCII
0x80-0x9F:   Control characters (rarely used)
0xA0-0xFF:   Extended characters

Examples:
0xA1 = ¡ (inverted exclamation)
0xA9 = © (copyright)
0xC0 = À (A with grave)
0xE9 = é (e with acute)
0xF1 = ñ (n with tilde)
0xFC = ü (u with umlaut)
```

### The Encoding Nightmare

**Scenario 1: The Email Problem**
```
Sender in France uses ISO-8859-1
Writes: "déjeuner" (lunch)
Bytes: 64 E9 6A 65 75 6E 65 72

Receiver in USA opens with ASCII:
Sees: "d□jeuner" (box instead of é)

Receiver in Russia opens with KOI8-R:
Sees: "dжjeuner" (Russian letter instead of é)
```

**Scenario 2: The Web Page Problem**
```
Web developer saves HTML as Windows-1252
Includes: "smart quotes" (curly quotes)
Bytes: 93 ... 94

Browser assumes ISO-8859-1:
Shows: "smart quotes" works (both have same bytes)

Browser assumes UTF-8:
Shows: "smart quotes" (Mojibake!)
Because 93 and 94 are invalid UTF-8 sequences
```

---

## Unicode: The Universal Solution (1991)

### Unicode's Goals

1. **Universal**: Include every writing system
2. **Efficient**: Use space wisely
3. **Unambiguous**: One code point per character
4. **Stable**: Never change character assignments
5. **Plain text**: Just characters, no formatting

### How Unicode is Organized

**Code Points:** U+0000 to U+10FFFF (1,114,112 possible)

**17 Planes** (groups of 65,536 code points each):

| Plane | Range | Name | Purpose |
|-------|-------|------|---------|
| 0 | U+0000-U+FFFF | BMP | Most used characters |
| 1 | U+10000-U+1FFFF | SMP | Historic scripts, symbols |
| 2 | U+20000-U+2FFFF | SIP | More Chinese/Japanese/Korean |
| 3 | U+30000-U+3FFFF | TIP | Even more CJK |
| 14 | U+E0000-U+EFFFF | SSP | Specials (format controls) |
| 15-16 | U+F0000-U+10FFFF | PUP | Private use |

### Basic Multilingual Plane (BMP) - Plane 0

Contains 65,536 characters including:
- All modern alphabets (Latin, Cyrillic, Greek, Arabic...)
- Chinese, Japanese, Korean (first 20,000 CJK)
- Symbols (currency, math, arrows)
- Control characters

**95% of text uses only the BMP!**

### Unicode Character Categories

| Category | Code Range | Examples |
|----------|------------|----------|
| Lu (Letter, uppercase) | U+0041-U+005A | A-Z |
| Ll (Letter, lowercase) | U+0061-U+007A | a-z |
| Nd (Number, decimal) | U+0030-U+0039 | 0-9 |
| P (Punctuation) | Various | !@#$% |
| Z (Separators) | U+0020, U+00A0 | Space, NBSP |
| C (Control/Format) | U+0000-U+001F | TAB, newline |
| So (Symbol, other) | U+2600-U+26FF | ☀, ★, ♠ |
| Emojis | U+1F600+ | 😀, 🚀, ❤️ |

---

## UTF-8: The Encoding That Won the Internet

### Why UTF-8 Was Invented

**Problem with UTF-16 (the original Unicode encoding):**
- Every character takes 2 bytes minimum
- English text doubles in size
- Old ASCII files break

**Ken Thompson's brilliant solution (1992): UTF-8**

### UTF-8 Design Principles

1. **Backward compatible**: ASCII files are valid UTF-8
2. **Self-synchronizing**: Can find character boundaries anywhere
3. **Compact**: 1 byte for common characters
4. **Universal**: Can encode all Unicode

### UTF-8 Byte Patterns

| Bytes | First Byte | Continuation | Range | Capacity |
|-------|------------|--------------|-------|----------|
| 1 | 0xxxxxxx | None | U+0000-U+007F | 128 |
| 2 | 110xxxxx | 10xxxxxx | U+0080-U+07FF | 1,920 |
| 3 | 1110xxxx | 10xxxxxx × 2 | U+0800-U+FFFF | 61,440 |
| 4 | 11110xxx | 10xxxxxx × 3 | U+10000-U+10FFFF | 1,048,576 |

**The trick:** Continuation bytes always start with `10`, so you can always tell where a character starts!

### UTF-8 Encoding Examples

```
$ (U+0024):
  Binary: 00100100
  UTF-8:  00100100 (same as ASCII!)

¢ (U+00A2):
  Binary: 00000000 10100010
  Needs 2 bytes (above U+007F)
  UTF-8:  11000010 10100010 (0xC2 0xA2)

€ (U+20AC):
  Binary: 00100000 10101100
  Needs 3 bytes (above U+07FF)
  UTF-8:  11100010 10000010 10101100 (0xE2 0x82 0xAC)

𐍈 (U+10348):
  Binary: 0001 00000011 01001000
  Needs 4 bytes (above U+FFFF)
  UTF-8:  11110000 10010000 10001101 10001000 (0xF0 0x90 0x8D 0x88)
```

### UTF-8 Statistics

| Website Type | % Using UTF-8 |
|--------------|---------------|
| All websites | 98.1% |
| English sites | 99.5% |
| Chinese sites | 99.9% |
| Japanese sites | 99.8% |
| Russian sites | 99.6% |

**UTF-8 is the de facto standard!**

---

## Other Unicode Encodings

### UTF-16

**Design:**
- BMP characters (U+0000-U+FFFF): 2 bytes
- Supplementary characters: 4 bytes (surrogate pairs)

**Used by:**
- Java, JavaScript, C# (internally)
- Windows (internally)
- Microsoft Office

**Pros:**
- Fixed 2-byte access for BMP
- Direct indexing into arrays

**Cons:**
- 2× space for ASCII
- Surrogate pairs complicate processing
- Byte order issues (BOM needed)

### UTF-32

**Design:** Always 4 bytes per character.

**Used when:**
- Character-by-character processing at fixed offsets
- Internal representation when memory isn't tight

**Pros:**
- Simple: every character is exactly 4 bytes
- Direct indexing: nth character at byte position n×4

**Cons:**
- 4× space for ASCII
- Wasteful for most text

### Comparison: Storing "Hello, 世界!"

| Encoding | Bytes | Hex Dump |
|----------|-------|----------|
| UTF-8 | 13 | `48 65 6C 6C 6F 2C 20 E4 B8 96 E7 95 8C 21` |
| UTF-16 | 20 | `48 00 65 00 6C 00 6C 00 6F 00 2C 00 20 00 16 4E 4C 75 21 00` |
| UTF-32 | 40 | `48 00 00 00 65 00 00 00 ...` |

**UTF-8 wins for mixed text!**

---

## Encoding Detection and Declaration

### The BOM (Byte Order Mark)

Some files start with special bytes to indicate encoding:

| Encoding | BOM Bytes | Hex |
|----------|-----------|-----|
| UTF-8 | EF BB BF | `0xEF 0xBB 0xBF` |
| UTF-16 BE | FE FF | `0xFE 0xFF` |
| UTF-16 LE | FF FE | `0xFF 0xFE` |
| UTF-32 BE | 00 00 FE FF | `0x00 0x00 0xFE 0xFF` |
| UTF-32 LE | FF FE 00 00 | `0xFF 0xFE 0x00 0x00` |

**UTF-8 BOM is optional** and sometimes causes problems. Many recommend not using it.

### Declaring Encoding in Documents

**HTML:**
```html
<!-- Method 1: HTTP header (best) -->
Content-Type: text/html; charset=utf-8

<!-- Method 2: Meta tag -->
<meta charset="UTF-8">

<!-- Method 3: Older style -->
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
```

**XML:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
```

**Python file:**
```python
# -*- coding: utf-8 -*-
```

**JSON:** Always UTF-8 (no declaration needed, it's in the spec)

---

## Common Encoding Problems and Solutions

### Problem 1: Mojibake

**Symptom:** Text shows wrong characters.

**Example:**
```
Should be: "Hello, café!"
Shows as: "Hello, cafÃ©!"

Cause: UTF-8 bytes interpreted as Latin-1
```

**Fix:** Open/save with correct encoding.

### Problem 2: Invalid Sequences

**Symptom:** Programs throw "invalid UTF-8" errors.

**Cause:** File contains bytes that don't form valid UTF-8.

**Fix:**
```python
# Replace invalid characters
text = bytes_data.decode('utf-8', errors='replace')
# Invalid bytes become (replacement character)

# Or ignore them
text = bytes_data.decode('utf-8', errors='ignore')
```

### Problem 3: Truncated Characters

**Symptom:** String cut mid-character.

**Cause:** Cutting byte arrays at wrong positions.

**Fix:** Cut at character boundaries, not byte boundaries.

---

## Best Practices for Developers

### 1. Always Specify Encoding

```python
# Good - explicit UTF-8
with open('file.txt', 'w', encoding='utf-8') as f:
    f.write(text)

# Bad - system dependent
with open('file.txt', 'w') as f:  # Don't do this!
    f.write(text)
```

### 2. Use UTF-8 for Everything

- Source code files
- Configuration files
- Database connections
- API responses
- Web pages
- Email

### 3. Handle Errors Gracefully

```python
try:
    text = data.decode('utf-8')
except UnicodeDecodeError:
    # Try fallback encodings
    for encoding in ['utf-8', 'latin-1', 'cp1252']:
        try:
            text = data.decode(encoding)
            break
        except UnicodeDecodeError:
            continue
```

### 4. Test with International Text

Always test your software with:
- Accented characters (café, naïve, résumé)
- Non-Latin scripts (مرحبا, 你好, Привет)
- Emoji (😀🎉🚀)
- Right-to-left text (Arabic, Hebrew)

### 5. Normalize Unicode When Comparing

```python
import unicodedata

# Some characters can be represented multiple ways
# é can be:
#   U+00E9 (single character - NFC)
#   U+0065 U+0301 (e + combining accent - NFD)

# Normalize before comparing
text1 = unicodedata.normalize('NFC', text1)
text2 = unicodedata.normalize('NFC', text2)
```

---

## Key Takeaways

1. **ASCII started it all**: Simple but limited to English
2. **Extended ASCII was a mess**: Different standards for different regions
3. **Unicode is the solution**: One standard for all characters
4. **UTF-8 is the standard encoding**: Universal, efficient, backward compatible
5. **Always be explicit**: Declare and specify encodings everywhere

## Summary Table

| Era | Standard | Year | Characters | Status |
|-----|----------|------|------------|--------|
| 1960s | ASCII | 1963 | 128 | Legacy |
| 1980s | Extended ASCII | 1987+ | 256 | Legacy |
| 1990s | Unicode | 1991 | 149,000+ | Current |
| Today | UTF-8 | 1992+ | All Unicode | Standard |

---

## Next Steps

- Learn Unicode normalization (NFC, NFD, NFKC, NFKD)
- Understand collation (locale-specific sorting)
- Study bidirectional text algorithms
- Explore Unicode security (homoglyph attacks)
