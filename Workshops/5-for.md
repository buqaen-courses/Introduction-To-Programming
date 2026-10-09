# Python Tutorial: The `for` Loop

Welcome! This tutorial covers Python's powerful `for` loop – your go‑to tool for iterating over sequences and collections. We'll explore:

- What `for` loops are and when to use them
- Iterating over lists, strings, tuples, sets, dictionaries, and ranges
- The `break` and `continue` statements inside `for`
- The `else` clause with `for` loops
- Nested `for` loops
- Useful patterns: `enumerate`, `zip`, and more
- Practice questions to test your understanding

Let's get looping!

---

## 1. Introduction to `for` Loops

A `for` loop is used to iterate over a sequence (like a list, tuple, string, or range) or any iterable object. It executes a block of code once for each item in the sequence.

Unlike a `while` loop that runs as long as a condition is true, a `for` loop runs a **fixed number of times** – once for each element in the collection. This makes it ideal when you know the items you want to process.

---

## 2. Basic Syntax

```python
for item in iterable:
    # code block to execute for each item
```

- `item` is a variable that takes the value of the current element in each iteration.
- `iterable` is any object that can return its elements one at a time (list, string, tuple, dictionary, set, range, etc.).

### Example 1: Iterating over a list

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")
```

Output:
```
I like apple
I like banana
I like cherry
```

### Example 2: Iterating over a string (characters)

```python
word = "Python"
for letter in word:
    print(letter)
```

Output:
```
P
y
t
h
o
n
```

### Example 3: Iterating over a tuple

```python
colors = ("red", "green", "blue")
for color in colors:
    print(color)
```

---

## 3. The `range()` Function

Often you need to repeat an action a specific number of times, or loop with an index. Python's `range()` function generates a sequence of numbers.

### Syntax

```python
range(stop)              # numbers from 0 to stop-1
range(start, stop)       # numbers from start to stop-1
range(start, stop, step) # numbers with custom step
```

### Example 4: Print numbers 0 to 4

```python
for i in range(5):
    print(i)
```

Output:
```
0
1
2
3
4
```

### Example 5: Print numbers 2 to 8

```python
for i in range(2, 9):
    print(i)
```

### Example 6: Count down from 10 to 1

```python
for i in range(10, 0, -1):
    print(i)
print("Blast off!")
```

### Example 7: Even numbers from 0 to 10

```python
for i in range(0, 11, 2):
    print(i)
```

---

## 4. Iterating Over Dictionaries

Dictionaries store key‑value pairs. You can iterate over keys, values, or both.

### Example 8: Iterating over dictionary keys

```python
person = {"name": "Alice", "age": 30, "city": "New York"}
for key in person:
    print(key, ":", person[key])
```

Better: use `.items()` to get both key and value.

### Example 9: Using `.items()`

```python
for key, value in person.items():
    print(f"{key}: {value}")
```

### Example 10: Just keys with `.keys()`, just values with `.values()`

```python
for k in person.keys():
    print(k)

for v in person.values():
    print(v)
```

---

## 5. Iterating Over Sets

Sets are unordered, but you can still iterate over them.

```python
numbers = {1, 2, 3, 4, 5}
for n in numbers:
    print(n)
```

(Note: order is not guaranteed.)

---

## 6. `break` and `continue` in `for` Loops

Just like in `while` loops, `break` exits the loop entirely, and `continue` skips to the next iteration.

### Example 11: `break` – stop when a condition is met

```python
for num in range(10):
    if num == 5:
        break
    print(num)
```

Output:
```
0
1
2
3
4
```

### Example 12: `continue` – skip even numbers

```python
for num in range(10):
    if num % 2 == 0:
        continue
    print(num)
```

Output:
```
1
3
5
7
9
```

### Example 13: Find first vowel in a word

```python
word = "Python"
vowels = "aeiouAEIOU"
for letter in word:
    if letter in vowels:
        print(f"First vowel: {letter}")
        break
else:
    print("No vowel found")  # executes if loop completes without break
```

---

## 7. The `else` Clause with `for` Loops

Just like with `while`, a `for` loop can have an `else` block that runs **only if the loop completes normally** (i.e., without hitting a `break`).

### Example 14: Search loop with `else`

```python
numbers = [2, 4, 6, 8, 10]
target = 7

for n in numbers:
    if n == target:
        print("Found!")
        break
else:
    print("Not found.")
```

### Example 15: Prime number checker using `for`-`else`

```python
num = 17
for i in range(2, num):
    if num % i == 0:
        print(f"{num} is not prime (divisible by {i})")
        break
else:
    print(f"{num} is prime")
```

---

## 8. Nested `for` Loops

You can put one `for` loop inside another. This is common for working with 2D data (matrices, tables) or generating patterns.

### Example 16: Multiplication table (up to 5)

```python
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j:2}", end="  ")
    print()   # newline after each row
```

### Example 17: Print a rectangle of stars

```python
rows = 4
cols = 6
for i in range(rows):
    for j in range(cols):
        print("*", end="")
    print()
```

### Example 18: Print a triangle

```python
n = 5
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()
```

---

## 9. Useful Patterns and Built‑ins

### Pattern A: Looping with Index – `enumerate`

When you need both the element and its index, use `enumerate()`.

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

Output:
```
0: apple
1: banana
2: cherry
```

### Pattern B: Iterating Multiple Lists – `zip`

Use `zip()` to loop over two or more sequences in parallel.

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

### Pattern C: List Comprehensions (Advanced Preview)

Though not a loop statement, list comprehensions are a concise way to create lists using a `for`-like syntax.

```python
squares = [x**2 for x in range(10)]
print(squares)   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

We'll cover comprehensions in a future tutorial.

### Pattern D: Reversing a Sequence – `reversed()`

```python
for i in reversed(range(1, 6)):
    print(i)
```

### Pattern E: Sorting a Sequence – `sorted()`

```python
words = ["banana", "apple", "cherry"]
for word in sorted(words):
    print(word)
```

---

## 10. Common Pitfalls and Tips

### Pitfall 1: Modifying a List While Iterating

Changing a list you're looping over can lead to unexpected behavior. Instead, iterate over a copy.

```python
# BAD – skipping elements
nums = [1, 2, 3, 4, 5]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)   # modifies list while iterating
print(nums)  # unexpected result

# GOOD – iterate over a copy
nums = [1, 2, 3, 4, 5]
for n in nums[:]:   # slice copy
    if n % 2 == 0:
        nums.remove(n)
print(nums)
```

### Pitfall 2: Using `range(len(seq))` unnecessarily

If you don't need the index, iterate directly over the sequence. It's cleaner and more Pythonic.

```python
# Not Pythonic
fruits = ["apple", "banana"]
for i in range(len(fruits)):
    print(fruits[i])

# Pythonic
for fruit in fruits:
    print(fruit)
```

### Pitfall 3: Forgetting that `range(stop)` excludes stop

```python
for i in range(5):
    print(i)  # prints 0..4, not 5
```

### Tip 1: Use `_` for unused loop variable

If you don't need the loop variable, use `_` to indicate it's intentionally unused.

```python
for _ in range(3):
    print("Hello")
```

### Tip 2: Combine `enumerate` with a custom start

```python
for idx, fruit in enumerate(fruits, start=1):
    print(f"{idx}. {fruit}")
```

### Tip 3: Use `for` when the number of iterations is known

`for` is more readable and less error‑prone than `while` for fixed iterations.

---

## 11. `for` vs `while`

| Feature         | `for`                                  | `while`                                |
| --------------- | -------------------------------------- | -------------------------------------- |
| Best for        | Iterating over sequences (known items) | Repeating until a condition changes    |
| Iteration count | Known in advance (length of sequence)  | Unknown; depends on condition          |
| Risk            | Fewer infinite loop risks              | Infinite loop if condition never false |
| Typical use     | Processing list items, ranges, strings | User input loops, game loops, flags    |

Choose the one that makes your intention clearest.

---

## 12. Practice Questions / Quiz

Test your understanding of `for` loops.

### Part A: Predict the Output

1. What will this code print?
   ```python
   for i in range(3):
       print(i, end=' ')
   ```

2. What is the output?
   ```python
   word = "code"
   for ch in word:
       print(ch * 2)
   ```

3. What will this print?
   ```python
   total = 0
   for n in [2, 4, 6, 8]:
       if n > 5:
           break
       total += n
   print(total)
   ```

4. What is the output?
   ```python
   for i in range(2, 5):
       for j in range(1, i):
           print(j, end='')
       print()
   ```

5. What does this print?
   ```python
   data = {"a": 1, "b": 2}
   for key, value in data.items():
       print(key, value)
   ```

### Part B: Fill in the Blanks

6. Complete the loop to print each character of `text`:
   ```python
   text = "Python"
   for ch in ________:
       print(ch)
   ```

7. Fill in to print numbers 0, 2, 4, 6, 8:
   ```python
   for i in range(________):
       print(i)
   ```

8. Use `enumerate` to print index and fruit:
   ```python
   fruits = ["apple", "banana"]
   for ________:
       print(index, fruit)
   ```

9. Write a `for` loop that breaks if the number 7 is found in the list `nums`:
   ```python
   nums = [3, 5, 7, 9]
   for n in nums:
       if ________:
           ________
   ```

10. Add an `else` clause that prints "All numbers are even" if no odd number is found:
    ```python
    numbers = [2, 4, 6, 8]
    for n in numbers:
        if n % 2 != 0:
            print("Odd found")
            break
    ________:
        print("All numbers are even")
    ```

### Part C: Write Code

11. Write a `for` loop that prints the square of each number in the list `[1, 2, 3, 4, 5]`.

12. Write a program that asks the user for 5 numbers (using a loop) and prints their sum.

13. Use a `for` loop to print all keys and values from the dictionary `grades = {"Alice": 85, "Bob": 92, "Charlie": 78}`.

14. Write nested `for` loops to print the following pattern:
    ```
    1
    2 2
    3 3 3
    4 4 4 4
    ```

15. Write a program that takes a list of words and prints the longest word (if multiple, print the first longest). (Use a loop, no `max` function.)

16. Use `zip` to print corresponding elements from `names = ["Anna", "Ben"]` and `ages = [20, 25]`.

17. Write a loop that counts how many vowels are in a string `s = "Hello World"`.

---

## 13. Answers

### Part A
1. `0 1 2 `
2. 
   ```
   cc
   oo
   dd
   ee
   ```
3. `6` (stops when `n=6`? Wait loop: [2,4,6,8]; first n=2 (<5) total=2; n=4 (<5) total=6; n=6 (>5) break, so total=6)
4. 
   ```
   1
   12
   123
   ```
   (i=2: j in range(1,2) prints 1; i=3: j=1,2 prints 12; i=4: j=1,2,3 prints 123)
5. 
   ```
   a 1
   b 2
   ```

### Part B
6. `text`
7. `0, 10, 2` (or `0, 10, 2` – but better `0, 9, 2`? Actually to get 0,2,4,6,8 you need `range(0, 9, 2)` or `range(0, 10, 2)`. The blank should be `0, 10, 2` to include 8.
8. `index, fruit in enumerate(fruits)`
9. `n == 7` and `break`
10. `else`

### Part C (Sample Solutions)

11. 
```python
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n ** 2)
```

12. 
```python
total = 0
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    total += num
print(f"Sum = {total}")
```

13. 
```python
grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
for name, score in grades.items():
    print(f"{name}: {score}")
```

14. 
```python
for i in range(1, 5):
    for j in range(i):
        print(i, end=" ")
    print()
```

15. 
```python
words = ["cat", "elephant", "dog", "butterfly"]
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print(f"Longest word: {longest}")
```

16. 
```python
names = ["Anna", "Ben"]
ages = [20, 25]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

17. 
```python
s = "Hello World"
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print(f"Vowel count: {count}")
```

---

Congratulations! You've learned the ins and outs of `for` loops in Python. Practice by modifying the examples and creating your own loops. Next, you might explore list comprehensions or dive into more advanced iteration techniques. Happy coding!