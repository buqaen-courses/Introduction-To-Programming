# Session 16: Collections – Lists, Tuples, Dictionaries, Sets

## Session Overview

A single string holds one piece of text. Real programs hold *many* things at
once, and the type you choose for them changes how your code works and how fast
it runs. This session introduces Python's four core collections — lists,
dictionaries, tuples, and sets — what each is good for, and how to choose. It
also introduces list comprehensions, which replace most of the loops you wrote
last session.

## Key Learning Objectives

By the end of this session, you will be able to:

- **Describe** when to use each of the four collection types
- **Create**, **index**, and **modify** lists and dictionaries
- **Iterate** over collections with `for` loops
- **Write** list and dictionary comprehensions
- **Use** tuples for fixed groups and sets for uniqueness
- **Choose** a collection based on the access pattern you need

## Choosing a Collection

This is the decision that matters most:

```
    ┌──────────────┬────────────────────┬───────────┬──────────────┐
    │  TYPE        │  ORDERED?          │ MUTABLE?  │  LOOKUP BY   │
    ├──────────────┼────────────────────┼───────────┼──────────────┤
    │  list        │  yes               │ yes       │  position    │
    │  tuple       │  yes               │ no        │  position    │
    │  dict        │  yes (insertion)   │ yes       │  key         │
    │  set         │  no                │ yes       │  membership  │
    └──────────────┴────────────────────┴───────────┴──────────────┘
```

In plain terms: a **list** is an ordered, changeable row of items. A **tuple**
is the same but locked. A **dictionary** is a lookup table keyed by name. A
**set** is a bag of unique values where order does not matter.

## Lists: The Workhorse

```python
fruits = ["apple", "banana", "cherry"]

fruits[0]          # "apple"
fruits[-1]         # "cherry"
fruits[1:3]        # ["banana", "cherry"]
len(fruits)        # 3

fruits.append("date")          # add to the end
fruits.insert(0, "fig")        # add at the front
fruits.remove("banana")        # remove by value
fruits.pop()                   # remove last, return it
fruits.sort()                  # in place
```

Note the asymmetry: `sort()` changes the list and returns `None`.
`sorted(fruits)` returns a **new** sorted list and leaves the original alone.

## Dictionaries: Name to Value

When your data has labels rather than positions, use a dictionary:

```python
student = {"name": "Sara", "age": 21, "gpa": 3.8}

student["name"]              # "Sara"
student["major"] = "CS"      # adds a key
student.get("major", "N/A")  # safe access, no KeyError
"age" in student             # True

for key, value in student.items():
    print(key, value)
```

`student["major"]` raises `KeyError` if the key is missing. `.get()` with a
default does not. This is the same defensive habit you will formalize with
exceptions in Session 18.

## Tuples and Sets

A **tuple** is immutable, which means it is safe to use as a dictionary key and
cannot be accidentally changed:

```python
point = (3, 5)
x, y = point              # unpacking
colors = ("red", "green", "blue")   # this will not change
```

A **set** holds only unique values and answers "is this in here?" instantly:

```python
visitors = ["Ali", "Sara", "Ali", "Reza"]
unique = set(visitors)    # {"Ali", "Sara", "Reza"}  <- Ali collapsed
"Ali" in unique           # True, fast even for huge sets

a = {1, 2, 3}
b = {2, 3, 4}
a & b     # {2, 3}     intersection
a | b     # {1, 2, 3, 4}  union
a - b     # {1}        difference
```

Sets trade order for uniqueness and lookup speed. That is the whole bargain.

## Comprehensions

A comprehension builds a collection in one expression. It is shorter and
usually faster than the equivalent loop:

```python
# the loop you would write
squares = []
for n in range(10):
    squares.append(n * n)

# the comprehension
squares = [n * n for n in range(10)]

# with a condition
evens = [n for n in range(20) if n % 2 == 0]

# dictionary comprehension
lengths = {word: len(word) for word in ["cat", "dog", "horse"]}
```

## 📖 Detailed Concepts

| Topic | Description |
|-------|-------------|
| **📋 [Python Lists](concepts/python-lists.md)** | The workhorse collection: creation, slicing, methods, comprehensions |
| **🔑 [Python Dictionaries](concepts/python-dictionaries.md)** | Key-value storage, safe access, views, and comprehension syntax |
| **🔗 [Sets and Tuples](concepts/sets-tuples.md)** | Immutable sequences and unique collections, and how to choose |

> **Note**: none of these three has a Persian translation yet. The English
> articles are complete; the Persian versions are a known gap.

## Main Concepts

- **List**: ordered, mutable, indexed by position
- **Tuple**: ordered, immutable; usable as a dictionary key
- **Dictionary**: key-value mapping with O(1) lookup by key
- **Set**: unique elements, unordered, fast membership test
- **`sort()` vs `sorted()`**: one mutates, one returns a new object
- **`.get()` with a default** avoids `KeyError`
- **Comprehensions**: build a collection from an iterable in one expression
- **Unpacking**: `x, y = point` reads better than `point[0]`, `point[1]`

## Common Beginner Mistakes

| Mistake | Result |
|---------|--------|
| `x = mylist.sort()` | `x` becomes `None`. Use `x = sorted(mylist)` |
| `d["key"]` when the key may be missing | `KeyError`. Use `.get()` or check `in` |
| Modifying a list while iterating over it | Skipped or duplicated elements. Iterate over a copy |
| Expecting sets to preserve order | They do not. Use a list if order matters |
| Using `tuple.append()` | `AttributeError`. Tuples cannot change |
| Nested `for` loops instead of a comprehension | Works, but verbose. Comprehensions are clearer |

## Workshop Activities

1. **Shopping list.** Build a list of items, let the user add and remove
   entries, then print the whole list sorted.
2. **Phone book.** A dictionary mapping names to numbers. Add three contacts,
   look one up by name, and handle the case where the name is not found.
3. **Unique words.** Take a sentence, split it into words, and use a set to
   report how many distinct words it contains. Compare that to the raw count.
4. **Set operations survey.** Given two lists of student IDs, print who is in
   both, who is only in the first, and who is in neither.

## Homework

- **List exercises**: build small lists and exercise `insert`, `remove`, `pop`,
  `sort`, slicing, and iteration.
- **Dictionary tasks**: a country-to-capital mapping, then look up five of them.
  Add a `.get()` fallback for an unknown key.
- **Membership**: check whether an item appears in a list, a set, and a
  dictionary. Time each with a large collection and explain the difference.
- **Comprehension drill**: rewrite five loops from Session 14 as comprehensions.
  If one does not convert cleanly, say why.

## Key Takeaways

- Choose a collection by how you will *look things up*, not by what it holds.
- `sort()` mutates; `sorted()` returns new.
- `.get()` with a default is the safe dictionary read.
- Tuples are for things that should not change; sets are for uniqueness.
- Comprehensions replace most collection-building loops.

## Connection to Next Session

You can now store and organise data. [Module 5: Software
Development](../../module-05-software-development/README.md) changes the
question from *what data do I have* to *how do I turn repeated work into named,
reusable units*. [Session 17](../../module-05-software-development/session-17/README.md)
introduces functions.

**Required Reading**: the three concept articles listed above, in order. Begin
with [Python Lists](concepts/python-lists.md).