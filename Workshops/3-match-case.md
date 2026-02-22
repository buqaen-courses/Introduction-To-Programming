# Python Tutorial: Switch/Case Statements (`match`/`case`)

Welcome! This tutorial covers Python's modern approach to switch/case functionality. You'll learn:

- The history of switch statements in Python
- Python 3.10's **`match`/`case`** (structural pattern matching)
- Simple value matching
- Matching multiple patterns with OR (`|`)
- Using the wildcard `_` for default cases
- Pattern matching with sequences and data structures

Let's dive in!

---

## 1. Does Python Have Switch/Case?

**Short answer: Yes, since Python 3.10!**

Long answer: Before version 3.10, Python did **not** have a built-in switch/case statement like C, Java, or JavaScript. Programmers used alternatives:

- Long `if`/`elif`/`else` chains
- Dictionary mapping (functions or values)
- Class-based dispatching

But with Python 3.10, a new feature called **structural pattern matching** was introduced using the keywords `match` and `case` . This is more powerful than traditional switch statements because it can match not just values, but also patterns in data structures .

---

## 2. Basic Syntax of `match`/`case`

### Simple Syntax

```python
match expression:
    case pattern1:
        # code for pattern1
    case pattern2:
        # code for pattern2
    case pattern3:
        # code for pattern3
    case _:
        # default code (like 'else')
```

### Key Points

- `match` evaluates an expression
- `case` defines patterns to match against
- The **wildcard** `_` matches anything (like `default` in other languages) 
- No `break` needed – only the first matching case executes 

### Example 1: Basic Value Matching

```python
day_number = 3

match day_number:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day number")

# Output: Wednesday
```

### Example 2: User Command Handler

```python
command = input("Enter command (start/stop/pause): ")

match command:
    case "start":
        print("Starting system...")
    case "stop":
        print("Stopping system...")
    case "pause":
        print("Pausing system...")
    case _:
        print("Unknown command")

# If user enters "start": Starting system...
```

This is much cleaner than a long `if`/`elif` chain .

---

## 3. Matching Multiple Values with OR (`|`)

You can combine multiple patterns in one `case` using the pipe symbol (`|`).

### Example 3: Weekday vs Weekend

```python
day = input("Enter a day: ").lower()

match day:
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("Weekday")
    case "saturday" | "sunday":
        print("Weekend")
    case _:
        print("Invalid day")
```

### Example 4: HTTP Status Codes

```python
status = 404

match status:
    case 200 | 201 | 204:
        print("Success")
    case 400 | 401 | 403 | 404:
        print("Client Error")
    case 500 | 501 | 502 | 503:
        print("Server Error")
    case _:
        print("Unknown status")
```

### Example 5: Darts Game Scoring

In a darts game, scores are based on distance from center :

```python
from math import hypot, ceil

x = 2
y = 2
distance = ceil(hypot(x, y))  # calculates distance from center

match distance:
    case 0 | 1:
        score = 10
    case 2 | 3 | 4 | 5:
        score = 5
    case 6 | 7 | 8 | 9 | 10:
        score = 1
    case _:
        score = 0

print(f"Score: {score}")
```

---

## 4. Matching with Conditions (Guards)

You can add `if` conditions to cases for more complex logic .

### Example 6: Positive/Negative/Zero with Guards

```python
number = -5

match number:
    case n if n < 0:
        print("Negative")
    case n if n == 0:
        print("Zero")
    case n if n > 0:
        print("Positive")

# Output: Negative
```

### Example 7: Age Classifier with Guards

```python
age = 25

match age:
    case a if a < 0:
        print("Invalid age")
    case a if a < 13:
        print("Child")
    case a if a < 20:
        print("Teenager")
    case a if a < 65:
        print("Adult")
    case _:
        print("Senior")
```

---

## 5. Matching Sequences (Lists, Tuples)

This is where `match` becomes truly powerful. It can match against the structure of lists and tuples .

### Example 8: Matching Different Point Formats

```python
point = (5, 10)  # can be list or tuple

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"On Y-axis at y={y}")
    case (x, 0):
        print(f"On X-axis at x={x}")
    case (x, y):
        print(f"Point at ({x}, {y})")
    case _:
        print("Not a point")

# Output: Point at (5, 10)
```

### Example 9: Matching Lists of Different Lengths

```python
data = [1, 2, 3, 4, 5]

match data:
    case []:
        print("Empty list")
    case [x]:
        print(f"Single element: {x}")
    case [x, y]:
        print(f"Two elements: {x} and {y}")
    case [x, y, z]:
        print(f"Three elements: {x}, {y}, {z}")
    case [x, y, z, *rest]:  # *rest captures remaining elements
        print(f"First three: {x}, {y}, {z}")
        print(f"Rest: {rest}")
```

### Example 10: Handling Different Data Formats

Imagine you have book data that could come in different formats :

```python
def process_book(data):
    match data:
        case (author, title, year):
            print(f"Book: {title} by {author} ({year})")
        case [author, title, year, price]:
            print(f"Book: {title} by {author} ({year}) - ${price}")
        case {"author": a, "title": t, "year": y}:
            print(f"Book: {t} by {a} ({y})")
        case _:
            print("Unknown format")

# Test with different formats
process_book(("Tolkien", "The Hobbit", 1937))
process_book(["Rowling", "Harry Potter", 1997, 24.99])
process_book({"author": "Orwell", "title": "1984", "year": 1949})
```

---

## 6. Matching Dictionaries

You can also match against dictionary patterns .

### Example 11: API Response Handling

```python
response = {"status": "success", "data": {"user": "alice", "id": 123}}

match response:
    case {"status": "success", "data": {"user": username, "id": user_id}}:
        print(f"Welcome back, {username} (ID: {user_id})")
    case {"status": "error", "message": error_msg}:
        print(f"Error: {error_msg}")
    case _:
        print("Unexpected response format")
```

### Example 12: Database Connection Configuration 

```python
config = {'server': '127.0.0.1', 'login': 'root', 'password': '1234'}

match config:
    case {'server': host, 'login': login, 'password': psw, 'port': port}:
        print(f"Connecting to {host}@{login}:{port}")
    case {'server': host, 'login': login, 'password': psw}:
        print(f"Connecting to {host}@{login}:22 (default port)")
    case _:
        print("Invalid configuration")
```

---

## 7. Matching Custom Objects

You can even match against custom class instances .

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

shapes = [Point(0, 0), Point(3, 4), Circle(Point(1, 1), 5)]

for shape in shapes:
    match shape:
        case Point(x=0, y=0):
            print("Origin point")
        case Point(x=x, y=y):
            print(f"Point at ({x}, {y})")
        case Circle(center=Point(x, y), radius=r):
            print(f"Circle centered at ({x}, {y}) with radius {r}")
        case _:
            print("Unknown shape")
```

---

## 8. When to Use `match` vs `if`/`elif`/`else`

### Use `match` when:
- You have many discrete values to check (like menu options, commands, status codes) 
- You need to match against the **structure** of data (lists, tuples, dictionaries, objects)
- Your code has deep nesting that would be hard to read with `if` statements
- You want to capture parts of the matched data (like extracting values from a dictionary)

### Use `if`/`elif`/`else` when:
- You have simple conditions (like `x > 5`) 
- You have range checks (`if 10 <= score <= 20`)
- You're working with Python versions before 3.10
- The logic is straightforward and doesn't benefit from pattern matching

---

## 9. Alternative Methods (For Older Python Versions)

If you're using Python before 3.10, here are common ways to simulate switch/case:

### Method A: Dictionary Mapping 

```python
# Map values to functions
def start():
    return "Starting..."

def stop():
    return "Stopping..."

commands = {
    "start": start,
    "stop": stop,
    "pause": lambda: "Pausing..."
}

# Usage
cmd = "start"
result = commands.get(cmd, lambda: "Unknown command")()
print(result)  # Starting...
```

### Method B: Dictionary with Values

```python
status_codes = {
    200: "OK",
    404: "Not Found",
    500: "Server Error"
}

code = 404
print(status_codes.get(code, "Unknown"))
```

### Method C: Class-based Dispatching 

```python
class Handler:
    def case_start(self):
        return "Starting..."
    def case_stop(self):
        return "Stopping..."
    def default(self):
        return "Unknown command"
    
    def handle(self, action):
        method = getattr(self, f"case_{action}", self.default)
        return method()

h = Handler()
print(h.handle("start"))  # Starting...
```

---

## 10. Common Pitfalls and Tips

### Tip 1: Always Include a Wildcard
Always use `case _:` to handle unexpected values .

### Tip 2: Order Matters
Cases are checked from top to bottom. Put more specific patterns first .

```python
# Bad: General case first
match value:
    case _:  # This catches everything!
        print("Default")
    case 42:  # Never reached
        print("Answer")

# Good: Specific first
match value:
    case 42:
        print("Answer")
    case _:
        print("Default")
```

### Tip 3: Variable Names in Patterns
When you use a variable name in a pattern, it captures the value .

```python
point = (5, 10)
match point:
    case (x, y):  # x becomes 5, y becomes 10
        print(f"x={x}, y={y}")
```

### Tip 4: No Fall-Through
Unlike C or Java, Python doesn't need `break` statements. Only one case executes .

### Tip 5: Constants Need Dot Notation
If you want to match against constants, use dot notation :

```python
class Colors:
    RED = 1
    GREEN = 2
    BLUE = 3

color = 2
match color:
    case Colors.RED:
        print("Red")
    case Colors.GREEN:
        print("Green")
    case Colors.BLUE:
        print("Blue")
```

---

## 11. Quiz / Practice Questions

### Part A: Basic Matching

1. What will this code print?
   ```python
   x = 3
   match x:
       case 1:
           print("One")
       case 2:
           print("Two")
       case 3:
           print("Three")
       case _:
           print("Other")
   ```

2. Fill in the missing parts to create a simple calculator:
   ```python
   op = "+"
   a, b = 10, 5
   
   match op:
       case "+":
           result = a + b
       case "-":
           result = a - b
       case "*":
           result = a * b
       case "/":
           result = a / b
       case ________:
           result = "Invalid operator"
   
   print(result)
   ```

3. What's the output?
   ```python
   value = 7
   match value:
       case 1 | 2 | 3:
           print("Small")
       case 4 | 5 | 6:
           print("Medium")
       case 7 | 8 | 9:
           print("Large")
       case _:
           print("Unknown")
   ```

### Part B: Pattern Matching with Sequences

4. What will this print?
   ```python
   data = [1, 2, 3]
   match data:
       case [x, y]:
           print(f"Two: {x}, {y}")
       case [x, y, z]:
           print(f"Three: {x}, {y}, {z}")
       case _:
           print("Other")
   ```

5. Write a `match` statement that checks if a point `(x, y)` is on the X-axis, Y-axis, or elsewhere.

6. What's the output?
   ```python
   response = {"status": "error", "message": "Not found"}
   match response:
       case {"status": "success", "data": d}:
           print(f"Data: {d}")
       case {"status": "error", "message": msg}:
           print(f"Error: {msg}")
       case _:
           print("Unknown")
   ```

### Part C: Guards and Complex Patterns

7. What will this print?
   ```python
   num = 15
   match num:
       case n if n < 0:
           print("Negative")
       case n if n % 2 == 0:
           print("Even")
       case n if n % 2 == 1:
           print("Odd")
   ```

8. Write code that categorizes a person based on age and has_driving_license using pattern matching.

9. What's wrong with this code?
   ```python
   value = 42
   match value:
       case _:
           print("Default")
       case 42:
           print("Answer")
   ```

10. How would you match a list that starts with 1, has any second element, and then anything else?

---

## 12. Answers to Quiz

### Part A
1. `Three`
2. `_` (wildcard)
3. `Large`

### Part B
4. `Three: 1, 2, 3`
5. 
   ```python
   match (x, y):
       case (_, 0):
           print("On X-axis")
       case (0, _):
           print("On Y-axis")
       case (_, _):
           print("Elsewhere")
   ```
6. `Error: Not found`

### Part C
7. `Odd` (15 is positive and odd)
8. 
   ```python
   match (age, has_license):
       case (a, True) if a >= 18:
           print("Can drive")
       case (a, False) if a >= 18:
           print("Can get license")
       case (a, _) if a < 18:
           print("Too young")
   ```
9. The default case `_` comes before specific case 42, so it catches everything first. Order should be: specific first, general last.
10. `case [1, _, *rest]:` matches a list starting with 1, any second element, and the rest captured in `rest`.

---

Congratulations! You've learned Python's modern `match`/`case` statement. This powerful feature goes far beyond traditional switch statements and allows you to write cleaner, more expressive code when handling multiple conditions or complex data structures.

Remember: `match`/`case` requires **Python 3.10 or later**. If you're using an older version, stick with the alternative methods. Happy coding!