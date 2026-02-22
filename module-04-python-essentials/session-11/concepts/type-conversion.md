# Type Conversion: Changing Data Types in Python

## Why Type Conversion?

Different operations require different data types. Type conversion allows you to change a value from one type to another, enabling flexible programming.

## Implicit vs Explicit Conversion

### Implicit Conversion (Automatic)
Python automatically converts types when safe:
```python
# Numeric promotion
result = 5 + 3.2  # 8.2 (int + float = float)

# Boolean contexts
if []:           # Empty list → False
    print("Never executes")

if [1, 2, 3]:    # Non-empty list → True
    print("Executes")
```

### Explicit Conversion (Manual)
You explicitly convert using built-in functions:
```python
# String to number
age = int("25")        # 25
price = float("19.99") # 19.99

# Number to string
count = str(42)        # "42"

# Collection conversions
numbers = list("123")  # ['1', '2', '3']
unique = set([1, 2, 2, 3])  # {1, 2, 3}
```

## Numeric Conversions

### Integer Conversions
```python
# From string
int("42")         # 42
int("1010", 2)    # 10 (binary string)
int("2A", 16)     # 42 (hexadecimal string)
int("52", 8)      # 42 (octal string)

# From float
int(3.14)         # 3 (truncates)
int(3.9)          # 3 (truncates toward zero)

# From boolean
int(True)         # 1
int(False)        # 0

# Errors
# int("hello")   # ValueError
```

### Float Conversions
```python
# From string
float("3.14")     # 3.14
float("42")       # 42.0
float("1e-3")     # 0.001 (scientific notation)

# From integer
float(42)         # 42.0

# From boolean
float(True)       # 1.0
float(False)      # 0.0

# Special values
float("inf")      # inf
float("-inf")     # -inf
float("nan")      # nan
```

### Complex Conversions
```python
# From numbers
complex(2, 3)     # (2+3j)
complex(5)        # (5+0j)
complex(0, 1)     # 1j

# From strings (limited)
complex("2+3j")   # (2+3j)
# complex("2, 3") # Doesn't work
```

## String Conversions

### From Numbers
```python
# Integers
str(42)           # "42"
str(-15)          # "-15"

# Floats
str(3.14)         # "3.14"
str(1e-6)         # "1e-06"

# Booleans
str(True)         # "True"
str(False)        # "False"
```

### From Collections
```python
# Lists
str([1, 2, 3])    # "[1, 2, 3]"

# Tuples
str((1, 2, 3))    # "(1, 2, 3)"

# Dictionaries
str({"a": 1, "b": 2})  # "{'a': 1, 'b': 2}"

# Sets
str({1, 2, 3})    # "{1, 2, 3}"
```

### Formatting Strings
```python
# f-strings (Python 3.6+)
name = "Alice"
age = 25
message = f"My name is {name} and I'm {age} years old."

# format() method
message = "My name is {} and I'm {} years old.".format(name, age)

# % formatting
message = "My name is %s and I'm %d years old." % (name, age)
```

## Collection Conversions

### List Conversions
```python
# From string
list("hello")     # ['h', 'e', 'l', 'l', 'o']

# From tuple
list((1, 2, 3))   # [1, 2, 3]

# From set
list({1, 2, 3})   # [1, 2, 3] (order not guaranteed)

# From range
list(range(5))    # [0, 1, 2, 3, 4]

# From dictionary
list({"a": 1, "b": 2})  # ['a', 'b'] (keys only)
```

### Tuple Conversions
```python
# From list
tuple([1, 2, 3])  # (1, 2, 3)

# From string
tuple("hello")    # ('h', 'e', 'l', 'l', 'o')

# From range
tuple(range(3))   # (0, 1, 2)
```

### Set Conversions
```python
# From list (removes duplicates)
set([1, 2, 2, 3]) # {1, 2, 3}

# From tuple
set((1, 2, 3))    # {1, 2, 3}

# From string
set("hello")      # {'h', 'e', 'l', 'o'} (no duplicates)
```

### Dictionary Conversions
```python
# From list of pairs
dict([("a", 1), ("b", 2)])  # {'a': 1, 'b': 2}

# From keyword arguments
dict(a=1, b=2, c=3)  # {'a': 1, 'b': 2, 'c': 3}

# From zip
keys = ["a", "b", "c"]
values = [1, 2, 3]
dict(zip(keys, values))  # {'a': 1, 'b': 2, 'c': 3}
```

## Boolean Conversions

### Truthy/Falsy Values
```python
# Numbers
bool(0)        # False
bool(1)        # True
bool(-1)       # True
bool(3.14)     # True

# Strings
bool("")       # False (empty string)
bool("hello")  # True

# Collections
bool([])       # False (empty list)
bool([1, 2])   # True
bool({})       # False (empty dict)
bool({"a": 1}) # True
bool(set())    # False (empty set)

# None
bool(None)     # False
```

## Safe Conversion Techniques

### Try-Except for Error Handling
```python
def safe_int_conversion(value):
    """Safely convert value to integer."""
    try:
        return int(value)
    except ValueError:
        print(f"Cannot convert '{value}' to integer")
        return None
    except TypeError:
        print(f"Invalid type for conversion: {type(value)}")
        return None

# Usage
print(safe_int_conversion("42"))     # 42
print(safe_int_conversion("hello"))  # None
print(safe_int_conversion([1, 2]))   # None
```

### Default Values
```python
def get_port(config):
    """Get port number with default."""
    port = config.get("port", "8080")
    try:
        return int(port)
    except ValueError:
        print(f"Invalid port '{port}', using default")
        return 8080

config = {"port": "invalid"}
port = get_port(config)  # 8080
```

### Validation Functions
```python
def is_valid_number(text):
    """Check if text represents a valid number."""
    try:
        float(text)
        return True
    except ValueError:
        return False

def parse_number(text, default=0):
    """Parse text to number with fallback."""
    try:
        return float(text)
    except ValueError:
        print(f"Using default value: {default}")
        return default
```

## Advanced Conversion Patterns

### Custom Conversion Functions
```python
def str_to_bool(text):
    """Convert string to boolean with various formats."""
    text = text.lower().strip()
    if text in ("true", "yes", "1", "on"):
        return True
    elif text in ("false", "no", "0", "off"):
        return False
    else:
        raise ValueError(f"Cannot convert '{text}' to boolean")

# Usage
print(str_to_bool("yes"))    # True
print(str_to_bool("no"))     # False
print(str_to_bool("maybe"))  # ValueError
```

### Type Dispatcher
```python
def convert_value(value, target_type):
    """Convert value to specified type."""
    converters = {
        int: lambda x: int(float(x)) if isinstance(x, str) else int(x),
        float: float,
        str: str,
        bool: lambda x: bool(x) if not isinstance(x, str) else str_to_bool(x),
        list: lambda x: list(x) if hasattr(x, '__iter__') else [x],
    }

    converter = converters.get(target_type)
    if converter:
        return converter(value)
    else:
        raise ValueError(f"Unsupported type: {target_type}")

# Usage
print(convert_value("3.14", float))  # 3.14
print(convert_value("yes", bool))    # True
print(convert_value(42, str))        # "42"
```

### Serialization/Deserialization
```python
import json

# Convert Python objects to JSON strings
data = {"name": "Alice", "age": 25, "scores": [95, 87, 92]}
json_string = json.dumps(data)
# '{"name": "Alice", "age": 25, "scores": [95, 87, 92]}'

# Convert JSON strings back to Python objects
parsed_data = json.loads(json_string)
# {'name': 'Alice', 'age': 25, 'scores': [95, 87, 92]}
```

## Common Conversion Scenarios

### User Input Processing
```python
def get_user_info():
    """Get validated user information."""
    name = input("Name: ").strip()
    if not name:
        raise ValueError("Name cannot be empty")

    try:
        age = int(input("Age: "))
        if age < 0 or age > 150:
            raise ValueError("Age must be between 0 and 150")
    except ValueError as e:
        raise ValueError(f"Invalid age: {e}")

    return {"name": name, "age": age}

user = get_user_info()
```

### Data File Processing
```python
def parse_csv_line(line):
    """Parse a CSV line into appropriate types."""
    parts = line.strip().split(',')
    try:
        name = parts[0].strip()
        age = int(parts[1].strip())
        score = float(parts[2].strip())
        active = parts[3].strip().lower() == 'true'
        return {"name": name, "age": age, "score": score, "active": active}
    except (IndexError, ValueError) as e:
        raise ValueError(f"Invalid CSV line: {line}") from e

# Usage
line = "Alice, 25, 95.5, true"
student = parse_csv_line(line)
```

### API Data Handling
```python
import requests

def fetch_user_data(user_id):
    """Fetch user data from API."""
    response = requests.get(f"https://api.example.com/users/{user_id}")
    data = response.json()

    # Convert API strings to appropriate types
    return {
        "id": int(data["id"]),
        "name": str(data["name"]),
        "age": int(data["age"]),
        "active": bool(data["active"]),
        "score": float(data["score"])
    }

user = fetch_user_data(123)
```

## Key Takeaways

1. **Type conversion** enables working with different data types
2. **Explicit conversion** uses built-in functions like `int()`, `str()`, `float()`
3. **Implicit conversion** happens automatically in safe cases
4. **Error handling** prevents crashes from invalid conversions
5. **Custom conversion functions** provide flexible data processing

## Further Reading
- Python's data model and type system
- Internationalization and locale-specific conversions
- Advanced serialization formats (pickle, msgpack)
- Type hints and static type checking