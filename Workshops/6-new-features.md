# Python New Features Tutorial (3.8 to 3.14)

Welcome! This tutorial covers the most useful new features added to Python from version 3.8 through 3.14. Each section explains a feature in simple terms with examples you can try yourself.

---

## Python 3.8 (October 2019)

### The Walrus Operator `:=` 

The walrus operator lets you assign a value to a variable **at the same time** you use it in an expression. It looks like a walrus lying down (eyes and tusks).

**Without walrus (old way):**
```python
items = [10, 20, 30]
n = len(items)
if n <= 3:
    print(f"Only {n} items")
```

**With walrus (new way):**
```python
items = [10, 20, 30]
if (n := len(items)) <= 3:
    print(f"Only {n} items")
```

### F-String Debugging 

Add `=` inside f-strings to print both the expression and its value – perfect for debugging!

```python
name = "Alice"
age = 30
print(f"{name=}, {age=}")  # Output: name='Alice', age=30
```

### Positional-Only Parameters 

Use `/` in function definitions to force certain parameters to be positional (not keyword arguments).

```python
def greet(name, /, greeting="Hello"):
    return f"{greeting}, {name}!"

# Valid calls:
print(greet("Bob"))           # Works
print(greet("Bob", "Hi"))     # Works

# Invalid call:
print(greet(name="Bob"))      # Error! name must be positional
```

---

## Python 3.9 (October 2020)

### Dictionary Merge and Update Operators 

Merge dictionaries using `|` (merge) and `|=` (update in-place).

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Merge (creates new dictionary)
merged = dict1 | dict2
print(merged)  # {'a': 1, 'b': 3, 'c': 4}

# Update in-place
dict1 |= dict2
print(dict1)   # {'a': 1, 'b': 3, 'c': 4}
```

### New String Methods 

Remove prefixes and suffixes easily without complex slicing.

```python
filename = "python_3.9_document.txt"

# Remove prefix
print(filename.removeprefix("python_"))  # '3.9_document.txt'

# Remove suffix
print(filename.removesuffix(".txt"))     # 'python_3.9_document'
```

### Type Hints with Built-in Collections 

Use built-in types directly in type hints – no more importing from `typing`.

```python
# Old way (Python 3.8):
from typing import List
def process(items: List[int]) -> List[str]: ...

# New way (Python 3.9):
def process(items: list[int]) -> list[str]: ...
```

---

## Python 3.10 (October 2021)

### Structural Pattern Matching (`match`/`case`) 

Python's version of switch/case – much more powerful!

```python
def describe_value(value):
    match value:
        case 0:
            return "Zero"
        case 1 | 2 | 3:
            return "Small number"
        case int(x) if x > 100:
            return "Large number"
        case str(s):
            return f"Text: {s}"
        case _:
            return "Something else"

print(describe_value(2))        # Small number
print(describe_value(200))      # Large number
print(describe_value("hello"))  # Text: hello
```

### Better Error Messages 

Python 3.10 gives more helpful error messages with suggestions.

```python
# Instead of just "invalid syntax"...
# Python 3.10 suggests: "Did you forget parentheses?"

# Instead of "NameError"...
# Python 3.10 suggests: "Did you mean: existing_variable?"
```

### Union Types with `|` 

Use `|` to specify multiple possible types.

```python
# Old way:
from typing import Union
def process(item: Union[int, str]): ...

# New way:
def process(item: int | str): ...
```

---

## Python 3.11 (October 2022)

### Exception Groups and `except*` 

Handle multiple exceptions at once with ExceptionGroup.

```python
try:
    raise ExceptionGroup("Multiple errors",
        [ValueError("Bad value"),
         TypeError("Bad type")])
except* ValueError as e:
    print(f"Value errors: {e.exceptions}")
except* TypeError as e:
    print(f"Type errors: {e.exceptions}")
```

### `add_note()` to Exceptions 

Add extra information to exceptions after they're created.

```python
try:
    x = 1 / 0
except ZeroDivisionError as e:
    e.add_note("This happened during calculation")
    raise  # Re-raise with note attached
```

---

## Python 3.12 (October 2023)

### Improved F-Strings

F-strings are now more flexible – you can reuse quotes and nest them.

```python
# Python 3.12 allows this:
print(f"Message: {"nested"}")
```

### `pathlib` Enhancements

Working with file paths gets easier.

```python
from pathlib import Path

# Walk directories more easily
for file in Path(".").walk():
    print(file)
```

---

## Python 3.13 (October 2024)

### Enhanced Pattern Matching 

Pattern matching gets more powerful with type checks and value extraction.

```python
def process(data):
    match data:
        # Match positive integers
        case int(value) if value > 0:
            return f"Positive: {value}"
        
        # Match lists with middle elements
        case [first, *middle, last]:
            return f"First: {first}, Last: {last}, Middle count: {len(middle)}"
        
        case _:
            return "No match"

print(process(42))              # Positive: 42
print(process([1,2,3,4,5]))     # First: 1, Last: 5, Middle count: 3
```

### Colorized REPL 

The interactive Python shell now has colors for better readability.

### Improved Error Messages 

Even smarter error messages with better suggestions.

### Pathlib Atomic Writes 

Write files safely without corruption risk.

```python
from pathlib import Path

p = Path("important.txt")
p.write_text_atomic("Safe write!", encoding="utf-8")
```

### Faster Performance 

Python 3.13 runs up to 30% faster for many operations.

---

## Python 3.14 (October 2025)

### Template Strings (T-strings) 

A new way to create strings with templates.

```python
name = "Alice"
items = ["book", "pen"]

# T-strings keep both template and values
template = t"Hello {name}, you have {len(items)} items"
print(template)  # Shows both template and evaluated result
```

### Enhanced REPL Experience 

The interactive shell gets even better with more features and better colors.

### Better Error Messages 

Continuing the trend of helpful error messages.

### Zstandard Compression 

Built-in support for modern compression.

```python
import zstandard as zstd

compressor = zstd.ZstdCompressor()
data = b"Some data to compress"
compressed = compressor.compress(data)
```

### Deferred Evaluation of Annotations 

Type hints now run faster by default.

---

## Practice Questions

### Python 3.8

1. Rewrite this code using the walrus operator:
   ```python
   data = input("Enter data: ")
   if data:
       print(f"You entered: {data}")
   ```

2. What will `print(f"{x=}, {y*2=}")` output if `x=5` and `y=3`?

### Python 3.9

3. Merge `d1 = {"a":1}` and `d2 = {"b":2}` using the new operator.

4. Remove the prefix "test_" from `filename = "test_file.txt"`.

### Python 3.10

5. Write a `match` statement that prints "Yes" for 1, 2, or 3, and "No" otherwise.

6. Write a function that accepts either `int` or `float` using the new union syntax.

### Python 3.11-3.14

7. What method lets you add extra info to an exception after it's created?

8. Which Python version introduced colorized REPL?

---

## Quick Reference Table

| Version | Key Features                                                 |
| ------- | ------------------------------------------------------------ |
| 3.8     | Walrus operator `:=`, f-string `=`, positional-only params `/` |
| 3.9     | Dictionary `\|` merge, `removeprefix()`/`removesuffix()`, built-in type hints |
| 3.10    | `match`/`case`, better errors, union types with `\|`         |
| 3.11    | Exception groups, `add_note()`                               |
| 3.12    | Improved f-strings, `pathlib.walk()`                         |
| 3.13    | Enhanced pattern matching, colorized REPL, atomic writes, faster performance |
| 3.14    | Template strings (t-strings), Zstandard compression          |

---

## Answers to Practice Questions

1. `if (data := input("Enter data: ")): print(f"You entered: {data}")`
2. `x=5, y*2=6`
3. `merged = d1 | d2` or `d1 |= d2`
4. `filename.removeprefix("test_")`
5. 
   ```python
   match value:
       case 1 | 2 | 3:
           print("Yes")
       case _:
           print("No")
   ```
6. `def func(value: int | float): ...`
7. `add_note()`
8. Python 3.13

Happy coding with modern Python! 🐍