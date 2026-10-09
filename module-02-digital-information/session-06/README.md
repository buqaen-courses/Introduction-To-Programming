# Session 6: Text Representation – ASCII and Unicode

## Session Overview

A computer cannot store the letter `A`. It can store a number. Somewhere
between the character you type and the bits on disk, an encoding system decides
which number means `A`. This session makes that step visible, shows why the
7-bit ASCII system that English fits inside cannot hold a Persian or Chinese
sentence, and introduces Unicode and UTF-8 as the answer. It is also the first
session where a real encoding bug can corrupt your data irreversibly, so we look
at what happens when the wrong encoding is assumed.

## Key Learning Objectives

By the end of this session, you will be able to:

- **Explain** that characters are stored as numbers, not as letter shapes
- **Differentiate** between ASCII and Unicode
- **Describe** why Unicode was necessary, and what problem it solved
- **Recognize** UTF-8 and UTF-16 by their byte patterns
- **Identify** mojibake, and state what caused it
- **Convert** a short string to bytes and back, by hand

## Characters Are Numbers

The letter `A` on your keyboard is a key. Pressing it produces something the
operating system turns into a number, using an agreed table:

```
    What you type          What the computer stores          What comes back

        A                       65  (0b01000001)                  A
        B                       66  (0b01000010)                  B
        a                       97  (0b01100001)                  a
        b                       98  (0b01100010)                  b
        0                       48  (0b00110000)                  0
        1                       49  (0b00110001)                  1
```

Notice how the numbers jump. `a` is 97 but `A` is 65. The 32-number gap is
exactly the difference between upper and lower case, and it is not a coincidence.

## Why 7 Bits Was Not Enough

ASCII allocates 7 bits, which covers 128 code points:

```
    7 bits = 128 possible values
    ASCII uses them for:
      0-31    control characters (newline, tab, backspace)
      32-126  printable English: space, digits, punctuation, A-Z, a-z
      127     delete

    That is the entire ASCII world. English, plus punctuation.
```

Now consider what a Persian or Chinese sentence needs. Each of those languages
has thousands of characters. Three consequences follow:

1. One byte per character cannot work.
2. Languages need to share the number space without colliding.
3. A single byte cannot signal how long the following character is.

## Unicode Solves the Number Space Problem

Unicode assigns every character in every written language a single unique
number, called a **code point**:

```
    'A'    U+0041        Persian 'ا'    U+0627
    'a'    U+0061        Persian 'ب'    U+0628
    '0'    U+0030        Chinese '中'   U+4E2D
    '€'    U+20AC        Emoji '🎉'      U+1F389
```

The `U+` prefix and four hex digits are the notation. Unicode itself defines
the *numbers*. It does not define how those numbers become bytes. That second
job belongs to the UTF encodings, and this is where most real-world confusion
lives.

## Unicode vs UTF-8: Two Different Things

```
    Unicode          = the code point table      (a dictionary)
    UTF-8            = one encoding of that table (a spelling)

    '€' has code point U+20AC.

    Encoded as UTF-8:    E2 82 AC        (3 bytes)
    Encoded as UTF-16:   20 AC           (2 bytes)
    Encoded as UTF-32:   00 00 20 AC     (4 bytes)

    Same character. Different bytes. Same meaning.
```

UTF-8 is the practical default: it uses 1 byte for ASCII, so existing English
data is unchanged, and it grows only for non-ASCII characters.

## Mojibake: A Symptom Worth Recognizing

You have seen this. `café` becomes `cafÃ©`. Here is exactly what happened:

```
    The original text            café
    Encoded as UTF-8             63 61 66 C3 A9
    Decoded as Latin-1 (wrong)   c a f Ã ©
```

Two bytes (`C3 A9`) were each read as one separate Latin-1 character. Nothing
was lost; the bytes are intact. But a reader can no longer tell whether it was
meant as UTF-8 or Latin-1. This is the encoding bug you will debug at least once.

## 📖 Detailed Concepts

| Topic | Description |
|-------|-------------|
| **🔤 [Character Encoding](concepts/character-encoding.md)** | How characters become numbers: code points, ASCII tables, byte sequences |
| **📝 [Text Encoding Standards](concepts/text-encoding-standards.md)** | From ASCII through the UTF family, and choosing an encoding safely |
| **🔧 [String Operations](concepts/string-operations.md)** | Working with text as data: indexing, slicing, searching, transforming |

All three have Persian translations. Read them in the order listed.

## Main Concepts

- **Code point**: the number assigned to a character by Unicode
- **ASCII**: a 7-bit, 128-value standard for English
- **Unicode**: one code point space covering all written languages
- **UTF-8, UTF-16, UTF-32**: encodings of that space, differing in byte width
- **Variable-width**: UTF-8 uses 1 to 4 bytes depending on the code point
- **Mojibake**: text decoded with the wrong encoding
- **BOM**: an optional leading marker, now discouraged for UTF-8

## Workshop Activities

1. **Decode by hand.** You are given the ASCII codes `72 101 108 108 111`.
   Write down the letters. Then verify with `print(bytes([72, 101, 108, 108,
   111]).decode("ascii"))`.
2. **Your name in code points.** Find the Unicode code point of every character
   in your own name using `ord()`. Record them. Notice how many code points a
   name takes versus how many letters it appears to have.
3. **Round-trip a Persian string.** In Python, take a Persian sentence, call
   `.encode("utf-8")`, print the bytes, then `.decode("utf-8")` back. Do it
   again with `.encode("ascii")` and read the error carefully.
4. **Break it deliberately.** Encode text as UTF-8, decode as Latin-1, then as
   cp1256. Compare the damage. Which one is recoverable?

## Homework

- **Short answers**: why is ASCII not enough? What problem does Unicode solve
  that ASCII could not?
- **Code lookup**: find the code points for five emojis and record them along
  with their UTF-8 byte sequences.
- **Encoding survey**: find one real file on your computer that is not UTF-8,
  or write a short program that produces mojibake on purpose and explain what
  went wrong.
- **Reflection**: one or two paragraphs on why an encoding standard matters
  more than it looks like it should.

## Key Takeaways

- Computers store numbers. Encoding tables map numbers to characters.
- ASCII is 128 values, and English uses nearly all of them.
- Unicode is a shared number space, not a byte format.
- UTF-8 is the encoding. Most of the time you want it, everywhere.
- Mojibake is a decoding mistake, not data loss, and it is easy to diagnose once
  you know the pattern.

## Connection to Next Session

Module 2 is complete. You understand bits, bytes, arithmetic on both, and how
text becomes data. [Module 3: Algorithmic Thinking](../../module-03-algorithmic-thinking/README.md)
starts asking a different question: given data, what should a program *do* with
it?

**Required Reading**: the three concept articles listed above, in order. Both
English and Persian versions are available.