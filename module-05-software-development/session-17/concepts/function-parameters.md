# Function Parameters: Flexible Input Handling

## Introduction: Beyond Basic Parameters

We've learned how to create functions with simple parameters. Now let's explore more flexible ways to handle function inputs, making your functions more powerful and easier to use.

### What We'll Cover

- Positional vs keyword arguments
- Default values with gotchas to avoid
- Variable number of arguments
- Unpacking collections as arguments

---

## Positional vs Keyword Arguments

### Positional Arguments (Order Matters)

```python
def create_user(username, email, age):
    """Create a user with positional arguments."""
    return {
        "username": username,
        "email": email,
        "age": age
    }

# Must be in exact order
user1 = create_user("alice123", "alice@email.com", 25)
user2 = create_user("bob456", "bob@email.com", 30)
```

**Key Point**: With positional arguments, order is everything!

### Keyword Arguments (Order Doesn't Matter)

```python
# Same function, called with keyword arguments
user3 = create_user(
    username="charlie789",
    email="charlie@email.com",
    age=35
)

# Order doesn't matter with keywords
user4 = create_user(
    age=28,
    username="diana101",
    email="diana@email.com"
)

# Mix positional and keyword (positional first!)
user5 = create_user("eve202", email="eve@email.com", age=32)
```

### Why Use Keywords?

```python
def send_email(to, subject, body, priority="normal"):
    """Send an email."""
    print(f"To: {to}")
    print(f"Subject: {subject}")
    print(f"Priority: {priority}")
    print(f"Body: {body}")

# Without keywords - what does each value mean?
send_email("boss@company.com", "Meeting", "Hi...", "high")
# Hard to tell which is which!

# With keywords - crystal clear!
send_email(
    to="boss@company.com",
    subject="Meeting tomorrow",
    body="Hi, can we meet tomorrow at 2pm?",
    priority="high"
)
```

**Best Practice**: Use keyword arguments when:
- Function has many parameters
- Some parameters are optional
- You want code to be self-documenting

---

## Default Parameters

### Basic Default Values

```python
def greet(name, greeting="Hello", punctuation="!"):
    """Greet someone with customizable message."""
    print(f"{greeting}, {name}{punctuation}")

# Use all defaults
greet("Alice")                           # Hello, Alice!

# Override some defaults
greet("Bob", greeting="Hi")              # Hi, Bob!
greet("Charlie", punctuation=".")        # Hello, Charlie.

# Override all
greet("Dave", "Howdy", "...")            # Howdy, Dave...
```

### Important Default Parameter Rules

**Rule 1: Defaults go at the end**

```python
# WRONG - SyntaxError!
def wrong(a="default", b):
    pass

# RIGHT
def right(b, a="default"):
    pass
```

**Rule 2: Don't use mutable defaults!** (Very Important!)

```python
# DANGER - mutable default argument
def add_item_bad(item, shopping_list=[]):
    """This has a subtle bug!"""
    shopping_list.append(item)
    return shopping_list

# First call
list1 = add_item_bad("apples")
print(list1)        # ['apples'] - looks good

# Second call
list2 = add_item_bad("bananas")
print(list2)        # ['apples', 'bananas'] - Wait, what?!

# list1 changed too!
print(list1)        # ['apples', 'bananas'] - Surprise!
```

**The Problem**: The default list is created ONCE when the function is defined, not each time it's called. So all calls share the same list!

**The Solution**: Use None as default

```python
# SAFE - use None as default
def add_item_safe(item, shopping_list=None):
    """Correct version - no shared list."""
    if shopping_list is None:
        shopping_list = []    # Create new list each time
    shopping_list.append(item)
    return shopping_list

# Each call gets its own list
list1 = add_item_safe("apples")
print(list1)        # ['apples']

list2 = add_item_safe("bananas")
print(list2)        # ['bananas'] - separate list!
```

**Always use None as default for mutable types (lists, dicts, sets)!**

---

## Variable Number of Arguments

### *args - Any Number of Positional Arguments

```python
def sum_all(*numbers):
    """Sum any number of arguments."""
    total = 0
    for num in numbers:
        total += num
    return total

# Call with any number of arguments
print(sum_all(1, 2, 3))              # 6
print(sum_all(10, 20, 30, 40))       # 100
print(sum_all())                     # 0 (no arguments)
print(sum_all(5))                    # 5 (single argument)

# Inside the function, 'numbers' is a tuple
print(type(numbers))   # <class 'tuple'>
```

### **kwargs - Any Number of Keyword Arguments

```python
def create_profile(**info):
    """Create a profile from any keyword arguments."""
    profile = {
        "created": True,
        "active": True
    }
    profile.update(info)  # Add all provided info
    return profile

# Call with any keywords
user1 = create_profile(name="Alice", age=25, city="NYC")
user2 = create_profile(name="Bob", profession="Engineer")

print(user1)
# {'created': True, 'active': True, 'name': 'Alice', 'age': 25, 'city': 'NYC'}

print(user2)
# {'created': True, 'active': True, 'name': 'Bob', 'profession': 'Engineer'}
```

### Combining All Parameter Types

```python
def complex_function(required, *args, default="value", **kwargs):
    """
    Function demonstrating all parameter types.

    required: Must be provided
    *args: Variable positional arguments (tuple)
    default: Optional with default value
    **kwargs: Variable keyword arguments (dict)
    """
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Default: {default}")
    print(f"Kwargs: {kwargs}")

# Usage examples
complex_function("hello")
# Required: hello
# Args: ()
# Default: value
# Kwargs: {}

complex_function("hello", 1, 2, 3)
# Required: hello
# Args: (1, 2, 3)
# Default: value
# Kwargs: {}

complex_function("hello", 1, 2, 3, default="changed", extra="data")
# Required: hello
# Args: (1, 2, 3)
# Default: changed
# Kwargs: {'extra': 'data'}
```

**Order Matters**: `def func(regular, *args, default="val", **kwargs)`

---

## Unpacking Arguments

### Unpacking Lists/Tuples as Arguments

```python
def greet(first, middle, last):
    """Greet with full name."""
    print(f"Hello, {first} {middle} {last}!")

# Direct call
greet("John", "Quincy", "Adams")

# Unpack from tuple
name_parts = ("John", "Quincy", "Adams")
greet(*name_parts)   # Same as greet("John", "Quincy", "Adams")

# Unpack from list
name_list = ["Jane", "Marie", "Doe"]
greet(*name_list)    # Same as greet("Jane", "Marie", "Doe")
```

### Unpacking Dictionaries as Arguments

```python
def create_user(name, email, age, city="Unknown"):
    """Create a user with required and optional fields."""
    return {
        "name": name,
        "email": email,
        "age": age,
        "city": city
    }

# Unpack dictionary
user_data = {
    "name": "Alice",
    "email": "alice@example.com",
    "age": 25,
    "city": "NYC"
}

user = create_user(**user_data)
# Same as: create_user(name="Alice", email="alice@example.com", age=25, city="NYC")
```

### Practical Use: Merging Function Calls

```python
def configure_server(host, port, debug=False, ssl=True, timeout=30):
    """Configure server with various options."""
    return {
        "host": host,
        "port": port,
        "debug": debug,
        "ssl": ssl,
        "timeout": timeout
    }

# Base configuration
base_config = {
    "host": "localhost",
    "port": 8080,
    "debug": False
}

# Development environment (override debug)
dev_config = {**base_config, "debug": True}
server1 = configure_server(**dev_config)

# Production environment (add SSL)
prod_config = {**base_config, "ssl": True, "timeout": 60}
server2 = configure_server(**prod_config)
```

---

## Practical Examples

### Example 1: Flexible Logger

```python
def log(message, level="INFO", timestamp=None, **metadata):
    """
    Flexible logging function.

    Args:
        message: The log message
        level: Log level (DEBUG, INFO, WARNING, ERROR)
        timestamp: Optional timestamp (defaults to now)
        **metadata: Any additional key-value pairs
    """
    import datetime

    if timestamp is None:
        timestamp = datetime.datetime.now()

    # Build log entry
    entry = f"[{timestamp:%Y-%m-%d %H:%M:%S}] {level}: {message}"

    # Add metadata if any
    if metadata:
        meta_str = ", ".join(f"{k}={v}" for k, v in metadata.items())
        entry += f" | {meta_str}"

    print(entry)

# Usage
log("Application started")
# [2024-01-15 10:30:00] INFO: Application started

log("Error occurred", level="ERROR", file="data.txt", line=42)
# [2024-01-15 10:30:00] ERROR: Error occurred | file=data.txt, line=42

log("User login", user="alice", ip="192.168.1.1")
# [2024-01-15 10:30:00] INFO: User login | user=alice, ip=192.168.1.1
```

### Example 2: HTML Tag Builder

```python
def tag(name, *children, **attributes):
    """
    Build an HTML tag with children and attributes.

    Args:
        name: Tag name (div, span, p, etc.)
        *children: Child elements or text
        **attributes: HTML attributes (class, id, style, etc.)
    """
    # Build attributes string
    attrs = " ".join(f'{k}="{v}"' for k, v in attributes.items())
    if attrs:
        attrs = " " + attrs

    # Build content
    content = "".join(str(child) for child in children)

    # Build tag
    return f"<{name}{attrs}>{content}</{name}>"

# Usage
print(tag("p", "Hello, World!"))
# <p>Hello, World!</p>

print(tag("div", "Content", class_="container", id="main"))
# <div class="container" id="main">Content</div>

# Note: 'class' is reserved word, use 'class_' instead
print(tag("span", "Important", class_="highlight"))
# <span class="highlight">Important</span>
```

### Example 3: Database Query Builder

```python
def build_query(table, columns="*", where=None, order_by=None, limit=None):
    """
    Build a SQL SELECT query.

    Args:
        table: Table name
        columns: Columns to select (default all)
        where: WHERE clause conditions (dict)
        order_by: ORDER BY column
        limit: LIMIT value

    Returns:
        SQL query string
    """
    query = f"SELECT {columns} FROM {table}"

    if where:
        conditions = " AND ".join(f"{k}='{v}'" for k, v in where.items())
        query += f" WHERE {conditions}"

    if order_by:
        query += f" ORDER BY {order_by}"

    if limit:
        query += f" LIMIT {limit}"

    return query

# Usage
print(build_query("users"))
# SELECT * FROM users

print(build_query("users", columns="name, email", where={"active": "true"}))
# SELECT name, email FROM users WHERE active='true'

print(build_query("products", where={"category": "electronics"}, order_by="price", limit=10))
# SELECT * FROM products WHERE category='electronics' ORDER BY price LIMIT 10
```

---

## Common Beginner Mistakes

### Mistake 1: Mutable Default Arguments (Again!)

```python
# DANGER
def append_timestamp(timestamps=[]):
    import time
    timestamps.append(time.time())
    return timestamps

# SAFE
def append_timestamp(timestamps=None):
    if timestamps is None:
        timestamps = []
    import time
    timestamps.append(time.time())
    return timestamps
```

### Mistake 2: Wrong Order of Arguments

```python
def process_data(data, format="json", validate=True):
    pass

# WRONG - keyword before positional
process_data(format="xml", my_data)  # SyntaxError!

# RIGHT
process_data(my_data, format="xml")
```

### Mistake 3: Forgetting to Unpack

```python
def add_three(a, b, c):
    return a + b + c

numbers = [1, 2, 3]

# WRONG - passes list as single argument
result = add_three(numbers)  # TypeError!

# RIGHT - unpack the list
result = add_three(*numbers)  # Returns 6
```

### Mistake 4: Confusing * and **

```python
def func(*args, **kwargs):
    pass

# WRONG
data = {"a": 1, "b": 2}
func(*data)     # Unpacks keys: func("a", "b")

# RIGHT - use ** for dictionaries
func(**data)    # func(a=1, b=2)

# Lists use *
nums = [1, 2, 3]
func(*nums)     # func(1, 2, 3)
```

---

## Practice Exercises

### Exercise 1: Flexible Average Calculator
Create a function that calculates averages with optional weights.

```python
def weighted_average(*values, weights=None):
    """
    Calculate average of values.
    If weights provided, calculate weighted average.
    """
    # Your code here
    pass

# Test
print(weighted_average(10, 20, 30))                    # 20.0
print(weighted_average(10, 20, 30, weights=[1, 2, 3]))  # 23.33
```

### Exercise 2: Format Function
Create a flexible string formatter.

```python
def format_line(template, *values, separator=" | ", align="left"):
    """
    Format values according to template.
    separator: string between values
    align: "left", "right", or "center"
    """
    # Your code here
    pass

# Test
print(format_line("Name: {}, Age: {}", "Alice", 25))
print(format_line("{} - {}", "Item", "$10.00", separator=" | "))
```

### Exercise 3: Decorator Builder
Create a function that builds print decorators.

```python
def make_box(*texts, padding=1, char="*"):
    """
    Create a text box with padding.
    Example: make_box("Title", "Subtitle", padding=2, char="#")
    """
    # Your code here
    pass

# Test
print(make_box("Welcome", padding=1, char="*"))
# Should print something like:
# ***********
# *         *
# * Welcome *
# *         *
# ***********
```

### Exercise 4: Function Combiner
Create a function that calls other functions with arguments.

```python
def apply_functions(value, *functions):
    """
    Apply each function to the value in sequence.
    Return the final result.
    """
    # Your code here
    pass

# Test
def double(x): return x * 2
def add_one(x): return x + 1
def square(x): return x ** 2

result = apply_functions(3, double, add_one, square)
# Should be: ((3 * 2) + 1) ** 2 = 49
```

---

## Key Takeaways

1. **Keyword arguments improve clarity** - Use them especially with many parameters
2. **Avoid mutable defaults** - Use `None` and check inside function
3. **`*args` captures extra positional arguments** - Becomes a tuple
4. **`**kwargs` captures extra keyword arguments** - Becomes a dictionary
5. **Unpacking with `*`** - Use `func(*list)` to pass list items as separate arguments
6. **Unpacking with `**`** - Use `func(**dict)` to pass dict items as keyword arguments

## Quick Reference Card

| Feature | Syntax | Inside Function |
|---------|--------|----------------|
| Regular parameter | `def f(a, b)` | Normal variables |
| Default value | `def f(a, b=1)` | b is 1 if not provided |
| Mutable default | `def f(a, b=None)` | Check `if b is None` |
| Variable positional | `def f(*args)` | `args` is a tuple |
| Variable keyword | `def f(**kwargs)` | `kwargs` is a dict |
| Unpack list | `f(*my_list)` | Passes as separate args |
| Unpack dict | `f(**my_dict)` | Passes as keyword args |

---

## Further Reading

- **Next Lesson**: Modular Design - Organizing functions into logical groups
- **Practice**: Complete all exercises above
- **Challenge**: Create a mini-framework for building command-line interfaces
- **Explore**: Learn about function decorators (`@decorator`)
