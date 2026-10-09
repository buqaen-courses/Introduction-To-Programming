# Session 15: Working with Strings

## Session Overview

Strings are sequences of characters, and almost everything a user types arrives
as one. This session treats text as data you can index, slice, search, and
transform. It also introduces f-strings, which are the modern way to build
output, and text-processing patterns — splitting, joining, cleaning — that turn
a messy string into structured data you can work with.

## Key Learning Objectives

By the end of this session, you will be able to:

- **Index** and **slice** strings to extract characters and substrings
- **Use** the essential string methods for searching and transforming
- **Format** output with f-strings, including numbers and alignment
- **Split and join** text to convert between strings and lists
- **Clean** user input with `strip()`, `lower()`, and friends
- **Build** a small text analysis program

## Strings Are Sequences

A string is a sequence, so it behaves like a list of characters that you cannot
modify in place:

```python
word = "Python"

print(word[0])      # P
print(word[-1])     # n
print(word[1:4])    # yth      (start inclusive, end exclusive)
print(word[::2])    # Pto      (step of 2)
print(len(word))    # 6
```

The `start:end` rule is worth memorising now because it applies to lists in
Session 16 too: the start is included, the end is not.

## The Methods You Will Actually Use

```
    CLEANING                  FINDING                 TRANSFORMING
    --------                  -------                 ------------
    .strip()   trim spaces    .find(x)    position    .upper()   to upper
    .lstrip()  trim left      .index(x)   position    .lower()   to lower
    .rstrip()  trim right     x in s      yes/no      .replace() swap text
    .split()   cut to list    s.startswith()          .title()
    .splitlines() by lines    s.endswith()
```

`.find()` returns `-1` when nothing matches. `.index()` raises an error
instead. For beginner code where a missing substring is normal, `in` or
`.find()` is usually what you want.

## f-Strings: Put the Expression Inside

Concatenation with `+` works but gets unwieldy:

```python
# the old way
name = "Sara"
print("Hello " + name + ", you are " + str(25) + " years old")

# the modern way
print(f"Hello {name}, you are {25} years old")
```

You can also format numbers directly inside the braces:

```python
price = 1234.5678
print(f"{price:.2f}")        # 1234.57    two decimal places
print(f"{price:,.2f}")       # 1,234.57   with thousands separator
print(f"{42:5d}")            #    42      right-aligned, width 5
print(f"{42:<5}|")           # 42   |     left-aligned
print(f"{42:^7}|")           #   42   |   centred
```

This replaces `str.format()` and `%` formatting for anything new you write.

## Split and Join

Two methods that convert between the string world and the list world:

```python
words = "the quick brown fox".split()
# ['the', 'quick', 'brown', 'fox']

line = ",".join(words)
# 'the,quick,brown,fox'

lines = """first
second
third""".splitlines()
# ['first', 'second', 'third']
```

`split()` with no argument splits on any whitespace and drops empties.
`split(",")` splits on the literal comma. Remember this pair — it is the single
most useful text-processing idiom in the language.

## 📖 Detailed Concepts

| Topic | Description |
|-------|-------------|
| **✂️ [String Operations](concepts/string-operations.md)** | Indexing, slicing, essential methods, and immutable-string consequences |
| **🎨 [String Formatting](concepts/string-formatting.md)** | f-strings, number formats, alignment, and multi-line output |
| **🔍 [Text Processing](concepts/text-processing.md)** | Searching, splitting and joining, cleaning, and text analysis |

> **Note**: `string-operations.md` also exists in
> [Session 6](../../module-02-digital-information/session-06/concepts/README.md),
> where the focus is on encoding and bytes. This session's version is about
> manipulating text in Python. The Persian translation of the Session 15 article
> is not yet available.

## Main Concepts

- **Strings are immutable sequences**; slicing returns a new string
- **`s[start:end]`** with the end excluded
- **`.strip()`, `.lower()`, `.upper()`** for cleaning user input
- **`.find()` returns `-1`**; `.index()` raises; `in` returns a boolean
- **f-strings** `f"{value:.2f}"` for inline formatting
- **`.split()` and `.join()`** convert between text and lists
- **`enumerate()` over `split()`** is the standard line-by-line pattern

## Common Beginner Mistakes

| Mistake | Result |
|---------|--------|
| `word[0] = "X"` | `TypeError`. Strings cannot be modified |
| `s.find()` result used directly in `if` | `-1` is truthy, so the check always passes. Test `!= -1` |
| Mixing `str` and `int` in `+` | `TypeError`. Convert explicitly |
| Using `%` formatting when the string contains `%` | Confusing behaviour. Prefer f-strings |
| `.split(" ")` on input with double spaces | Empty strings in the result. Use `.split()` |
| Assuming `.splitlines()` handles `\r\n` | It does, but `.split("\n")` does not |

## Workshop Activities

1. **Name formatter.** Ask for a first and last name. Print the name in caps,
   lowercase, title case, and as an initial-style form (`Ali R.`).
2. **Word counter.** Count words in a sentence using `.split()`, then count
   characters using `len()`. Find the longest word with a loop.
3. **Character counter.** Ask for a character and count how many times it
   appears in a sentence.
4. **Vowel report.** For a given sentence, print how many of each vowel
   (`a e i o u`) appear. Use `.lower()` first so you only handle one case.

## Homework

- **String tasks**: check whether a string starts or ends with certain
  characters, and write a simple censorship function that replaces a word with
  `***`.
- **Slicing practice**: given ten strings, extract the first three characters,
  the last three, every other character, and the string reversed.
- **Mini challenge**: reverse a string. Do it once with slicing and once with a
  loop, then say which you prefer and why.
- **Formatter**: build a receipt printer using f-strings with right-aligned
  item names and two-decimal prices.

## Key Takeaways

- Strings are sequences, so indexing and slicing work as they do for lists.
- Strings are immutable; every method returns a new string.
- `.find()` gives `-1`, which is truthy. Test the result, do not trust it.
- f-strings are the clear way to build output.
- `.split()` and `.join()` are the bridge between text and structured data.

## Connection to Next Session

You can now work with one string well. [Session 16: Collections](../session-16/README.md)
scales that up to lists, tuples, dictionaries, and sets, and shows how to choose
the right structure for the job.

**Required Reading**: the three concept articles listed above, in order.