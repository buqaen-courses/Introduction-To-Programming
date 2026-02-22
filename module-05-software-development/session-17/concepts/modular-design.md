# Modular Design: Building Code Like LEGO

## Introduction

Just like how LEGO bricks can be combined in countless ways to build anything from simple houses to complex spaceships, modular code consists of small, independent pieces that work together.

### Why Modular Design Matters

**Without Modules (Messy Code)**:
```python
# Everything in one giant function
def process_user_request():
    # Read from database
    # Validate 50 different inputs
    # Calculate taxes
    # Send 3 different emails
    # Update 5 different tables
    # Log to 2 different systems
    # Generate report
    # Handle 20 different error cases
    pass
```

**With Modules (Clean Code)**:
```python
def process_user_request():
    """High-level orchestration - easy to understand!"""
    user = get_user_data()
    order = create_order(user)
    process_payment(order)
    send_confirmation(user, order)
    update_inventory(order)
    log_transaction(order)
```

**Benefits of Modular Design**:
- **Easier to understand** - Each piece does one thing
- **Easier to test** - Test small functions independently
- **Easier to maintain** - Fix bugs in isolated parts
- **Easier to reuse** - Use the same function in multiple places
- **Easier to collaborate** - Different people work on different modules

---

## The Single Responsibility Principle

### One Function = One Job

Think of functions like kitchen appliances:
- Toaster = toast bread only
- Blender = blend things only
- Coffee maker = make coffee only

Each appliance (function) does one thing really well.

### Bad Example: Swiss Army Knife Function

```python
def handle_user_data(data):
    """
    Does everything - hard to understand, test, and maintain!
    """
    # Step 1: Validate
    if not data.get('email'):
        return "Email required"
    if '@' not in data['email']:
        return "Invalid email"
    if not data.get('age'):
        return "Age required"
    if data['age'] < 18:
        return "Must be 18+"

    # Step 2: Clean
    data['email'] = data['email'].lower().strip()
    data['name'] = data['name'].title()

    # Step 3: Save to database
    import sqlite3
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users VALUES (?, ?, ?)",
                   (data['name'], data['email'], data['age']))
    conn.commit()
    conn.close()

    # Step 4: Send email
    import smtplib
    # ... 20 lines of email code ...

    # Step 5: Log
    with open('log.txt', 'a') as f:
        f.write(f"User created: {data['email']}\n")

    return "Success"
```

**Problems**:
- 60+ lines - hard to read
- Does 5 different things
- If database code breaks, the whole function fails
- Impossible to test email sending without database
- Can't reuse just the validation part

### Good Example: Separate, Focused Functions

```python
# ============ validation.py ============

def validate_user_data(data):
    """Validate user data - returns error message or None."""
    if not data.get('email'):
        return "Email required"
    if '@' not in data['email']:
        return "Invalid email"
    if not data.get('age'):
        return "Age required"
    if data['age'] < 18:
        return "Must be 18+"
    return None  # No errors


# ============ cleaning.py ============

def clean_user_data(data):
    """Clean and normalize user data."""
    cleaned = {}
    cleaned['email'] = data['email'].lower().strip()
    cleaned['name'] = data['name'].title()
    cleaned['age'] = int(data['age'])
    return cleaned


# ============ database.py ============

def save_user(data):
    """Save user to database."""
    import sqlite3
    conn = sqlite3.connect('users.db')
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
            (data['name'], data['email'], data['age'])
        )
        conn.commit()
        return True
    finally:
        conn.close()


# ============ email_service.py ============

def send_welcome_email(user):
    """Send welcome email to new user."""
    # Email logic here
    print(f"Welcome email sent to {user['email']}")
    return True


# ============ logger.py ============

def log_user_creation(user):
    """Log user creation event."""
    from datetime import datetime
    with open('log.txt', 'a') as f:
        f.write(f"[{datetime.now()}] User created: {user['email']}\n")


# ============ main.py ============

def register_user(data):
    """
    Register a new user - orchestrates all the steps.
    This high-level function is easy to understand!
    """
    # Step 1: Validate
    error = validate_user_data(data)
    if error:
        return {"success": False, "error": error}

    # Step 2: Clean
    clean_data = clean_user_data(data)

    # Step 3: Save
    save_user(clean_data)

    # Step 4: Notify
    send_welcome_email(clean_data)

    # Step 5: Log
    log_user_creation(clean_data)

    return {"success": True, "user": clean_data}


# Usage
result = register_user({
    "name": "alice smith",
    "email": "ALICE@EMAIL.COM",
    "age": 25
})
print(result)
```

**Benefits**:
- Each function is 10 lines or less
- Each does exactly one thing
- Can test validation without touching database
- Can reuse validation in other parts of the app
- Easy to find and fix bugs
- Multiple people can work on different files

---

## Function Composition: Building Bigger from Smaller

### The Building Block Approach

Just like building with LEGO:
1. Make small bricks (simple functions)
2. Combine bricks into walls (intermediate functions)
3. Combine walls into houses (complex functions)

### Example: Word Frequency Counter

```python
# Level 1: Basic building blocks
def read_file(filename):
    """Read text from file."""
    with open(filename, 'r') as f:
        return f.read()

def clean_text(text):
    """Clean and normalize text."""
    return text.lower()

def extract_words(text):
    """Split text into words."""
    return text.split()

def count_words(words):
    """Count frequency of each word."""
    from collections import Counter
    return Counter(words)

# Level 2: Combine into workflow
def analyze_text(text):
    """Analyze text - combine cleaning, extracting, counting."""
    clean = clean_text(text)
    words = extract_words(clean)
    frequencies = count_words(words)
    return frequencies

# Level 3: Full workflow with file
def analyze_file(filename):
    """Analyze entire file - the main function."""
    text = read_file(filename)
    frequencies = analyze_text(text)
    return frequencies.most_common(10)

# Usage
top_words = analyze_file("book.txt")
print("Most common words:", top_words)
```

### Visual Composition

```
Input: filename "book.txt"
    |
    v
┌──────────────┐
│  read_file   │ → "Once upon a time..."
└──────────────┘
    |
    v
┌──────────────┐
│  clean_text  │ → "once upon a time..."
└──────────────┘
    |
    v
┌──────────────┐
│extract_words │ → ["once", "upon", "a", "time"]
└──────────────┘
    |
    v
┌──────────────┐
│  count_words │ → {"once": 5, "upon": 3, ...}
└──────────────┘
    |
    v
Output: [("once", 42), ("upon", 38), ...]
```

---

## Organizing Code by Purpose

### Separation of Concerns

Keep different types of work in different places:

```
my_project/
├── data/               # Data files
│   ├── users.csv
│   └── products.csv
│
├── database/           # Database code
│   ├── connection.py   # Connect to database
│   ├── users.py       # User table operations
│   └── products.py    # Product table operations
│
├── services/           # Business logic
│   ├── auth.py        # Login, signup, passwords
│   ├── email.py       # Send emails
│   └── reporting.py   # Generate reports
│
├── validation/        # Input checking
│   ├── users.py       # Validate user data
│   └── products.py    # Validate product data
│
├── utils/             # Helper functions
│   ├── formatting.py  # Format numbers, dates
│   ├── files.py       # File operations
│   └── logging.py     # Logging utilities
│
└── main.py            # The main application
```

### Example: Clear Module Structure

```python
# ============ database/users.py ============
"""All database operations for users table."""

def get_user(user_id):
    """Get user by ID."""
    pass

def create_user(data):
    """Insert new user."""
    pass

def update_user(user_id, data):
    """Update existing user."""
    pass

def delete_user(user_id):
    """Delete user."""
    pass

# ============ services/auth.py ============
"""All authentication-related business logic."""

def register_user(data):
    """Register a new user."""
    # Uses database/users.py
    # Uses validation/users.py
    # Uses services/email.py
    pass

def login(email, password):
    """Authenticate user login."""
    pass

def reset_password(email):
    """Handle password reset."""
    pass

# ============ validation/users.py ============
"""All user data validation rules."""

def validate_email(email):
    """Check if email is valid."""
    pass

def validate_password(password):
    """Check if password is strong enough."""
    pass

def validate_registration_data(data):
    """Check all registration fields."""
    pass
```

---

## Abstraction Levels: Different Zoom Levels

### Think Like an Elevator

- **Floor 10**: High-level overview (CEO perspective)
- **Floor 5**: Mid-level operations (Manager perspective)
- **Floor 1**: Detailed implementation (Worker perspective)

### Code Abstraction Levels

```python
# ============ HIGH LEVEL (Main Application) ============
# "What does the app do?"

def process_order(order_data):
    """Process customer order - top level workflow."""
    validated_order = validate_order(order_data)
    payment_result = process_payment(validated_order)
    if payment_result.success:
        fulfillment_id = create_fulfillment(validated_order)
        send_confirmation(validated_order, fulfillment_id)
        update_inventory(validated_order)
    return payment_result

# ============ MID LEVEL (Service Functions) ============
# "How does each step work?"

def validate_order(order_data):
    """Validate order data."""
    check_customer_exists(order_data['customer_id'])
    check_products_available(order_data['items'])
    check_payment_method(order_data['payment'])
    return sanitize_order(order_data)

def process_payment(order):
    """Process payment."""
    payment_method = load_payment_method(order['payment_id'])
    transaction = charge_payment_method(payment_method, order['total'])
    return transaction

def create_fulfillment(order):
    """Create fulfillment request."""
    warehouse = select_warehouse(order)
    fulfillment_id = warehouse.create_pick_list(order)
    schedule_shipping(fulfillment_id, order['shipping_address'])
    return fulfillment_id

# ============ LOW LEVEL (Implementation Details) ============
# "How does each sub-step actually work?"

def check_products_available(items):
    """Check database for product availability."""
    for item in items:
        stock = database.query(
            "SELECT quantity FROM inventory WHERE product_id = ?",
            item['product_id']
        )
        if stock < item['quantity']:
            raise OutOfStockError(item['product_id'])

def charge_payment_method(method, amount):
    """Make API call to payment processor."""
    response = requests.post(
        PAYMENT_API_URL,
        json={
            'token': method['token'],
            'amount': amount,
            'currency': 'USD'
        }
    )
    return PaymentResult(response.json())
```

**Rule**: When reading code, start at high level. Only dive deeper when needed.

---

## Function Interfaces: Clear Contracts

### What is a Function Contract?

A "contract" defines:
1. **What inputs are expected** (parameters)
2. **What output is returned** (return value)
3. **What errors might happen** (exceptions)
4. **How to use it** (examples)

### Good Function Documentation

```python
def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index (BMI).

    Args:
        weight_kg: Weight in kilograms (must be positive number)
        height_m: Height in meters (must be positive number)

    Returns:
        BMI value as float

    Raises:
        ValueError: If weight or height is not positive
        TypeError: If inputs are not numbers

    Example:
        >>> calculate_bmi(70, 1.75)
        22.86
        >>> calculate_bmi(50, 1.60)
        19.53
    """
    # Type checking
    if not isinstance(weight_kg, (int, float)):
        raise TypeError(f"Weight must be a number, got {type(weight_kg)}")
    if not isinstance(height_m, (int, float)):
        raise TypeError(f"Height must be a number, got {type(height_m)}")

    # Value checking
    if weight_kg <= 0:
        raise ValueError(f"Weight must be positive, got {weight_kg}")
    if height_m <= 0:
        raise ValueError(f"Height must be positive, got {height_m}")

    # Calculation
    return weight_kg / (height_m ** 2)

# Usage examples
print(calculate_bmi(70, 1.75))      # 22.86
print(calculate_bmi(50, 1.60))      # 19.53

# Error cases
# calculate_bmi("70", 1.75)        # TypeError
# calculate_bmi(-70, 1.75)         # ValueError
```

### Simple Interface Design

```python
# GOOD: Simple, clear interface
def get_weather(city):
    """
    Get current weather for a city.

    Args:
        city: City name as string

    Returns:
        Dictionary with 'temperature', 'humidity', 'condition'
    """
    # Implementation...
    return {"temperature": 72, "humidity": 45, "condition": "sunny"}

# BAD: Too many parameters
def get_weather(
    city,
    include_temperature=True,
    include_humidity=True,
    include_wind=False,
    include_forecast=False,
    days_of_forecast=5,
    temperature_unit="fahrenheit",
    wind_speed_unit="mph",
    use_cache=True,
    cache_duration_minutes=10
):
    """Too complicated!"""
    pass

# BETTER: Group related options
def get_weather(city, options=None):
    """
    Get weather with options.

    Args:
        city: City name
        options: Dictionary of display options
                 (temperature, humidity, wind, forecast, etc.)
    """
    options = options or {}
    # ...

# Usage
weather = get_weather("NYC", options={
    "include_wind": True,
    "temperature_unit": "celsius"
})
```

---

## Testing Modular Code

### Why Modular Code is Easier to Test

```python
# ============ calculator.py ============

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def calculate(expression):
    """Parse and calculate simple expression like '10 + 5'."""
    parts = expression.split()
    a, operator, b = float(parts[0]), parts[1], float(parts[2])

    if operator == "+":
        return add(a, b)
    elif operator == "-":
        return subtract(a, b)
    elif operator == "*":
        return multiply(a, b)
    elif operator == "/":
        return divide(a, b)

# ============ test_calculator.py ============
"""Test each function independently."""

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2

def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5
    try:
        divide(10, 0)
        assert False, "Should have raised error"
    except ValueError:
        pass  # Expected

def test_calculate():
    assert calculate("10 + 5") == 15
    assert calculate("10 - 5") == 5
    assert calculate("10 * 5") == 50
    assert calculate("10 / 5") == 2

# Run tests
test_add()
test_subtract()
test_multiply()
test_divide()
test_calculate()
print("All tests passed!")
```

### Testing with Fake Dependencies

```python
# ============ user_service.py ============

def notify_user(user_id, message, email_service):
    """Send notification to user.

    Args:
        user_id: User to notify
        message: Message to send
        email_service: Object with send(email, message) method
    """
    # Get user's email from database
    email = database.get_user_email(user_id)

    # Use provided email service
    email_service.send(email, message)

# ============ test_user_service.py ============

class FakeEmailService:
    """Fake email service for testing."""
    def __init__(self):
        self.sent_emails = []

    def send(self, email, message):
        self.sent_emails.append({"email": email, "message": message})

def test_notify_user():
    # Create fake
    fake_email = FakeEmailService()

    # Call function with fake
    notify_user(user_id=123, message="Hello!", email_service=fake_email)

    # Check what happened
    assert len(fake_email.sent_emails) == 1
    assert fake_email.sent_emails[0]["message"] == "Hello!"
    print("Test passed - email would have been sent!")

# Run test
test_notify_user()
```

**Benefits**:
- Test without sending real emails
- Test without needing database
- Runs instantly
- No side effects

---

## Practical Examples

### Example 1: Shopping Cart System

```python
# ============ cart.py ============
"""Shopping cart operations."""

def create_cart():
    """Create empty shopping cart."""
    return {"items": [], "total": 0}

def add_item(cart, product, quantity=1):
    """Add item to cart."""
    cart["items"].append({
        "product": product,
        "quantity": quantity,
        "price": product["price"]
    })
    update_total(cart)

def remove_item(cart, product_id):
    """Remove item from cart by product ID."""
    cart["items"] = [
        item for item in cart["items"]
        if item["product"]["id"] != product_id
    ]
    update_total(cart)

def update_total(cart):
    """Recalculate cart total."""
    cart["total"] = sum(
        item["price"] * item["quantity"]
        for item in cart["items"]
    )

def get_cart_summary(cart):
    """Get printable cart summary."""
    lines = ["Shopping Cart:"]
    for item in cart["items"]:
        line_total = item["price"] * item["quantity"]
        lines.append(
            f"  {item['product']['name']} x {item['quantity']} = ${line_total:.2f}"
        )
    lines.append(f"Total: ${cart['total']:.2f}")
    return "\n".join(lines)

# Usage
product_a = {"id": 1, "name": "T-Shirt", "price": 19.99}
product_b = {"id": 2, "name": "Jeans", "price": 49.99}

cart = create_cart()
add_item(cart, product_a, quantity=2)
add_item(cart, product_b)

print(get_cart_summary(cart))
# Shopping Cart:
#   T-Shirt x 2 = $39.98
#   Jeans x 1 = $49.99
# Total: $89.97
```

### Example 2: Task Manager

```python
# ============ task_manager.py ============
"""Simple task management system."""

# Data storage
tasks = []
task_id_counter = 0

# ============ Core Functions ============

def add_task(title, description="", priority="medium"):
    """Add a new task."""
    global task_id_counter
    task_id_counter += 1

    task = {
        "id": task_id_counter,
        "title": title,
        "description": description,
        "priority": priority,
        "completed": False,
        "created": datetime.now()
    }
    tasks.append(task)
    return task["id"]

def complete_task(task_id):
    """Mark task as complete."""
    task = find_task(task_id)
    if task:
        task["completed"] = True
        return True
    return False

def delete_task(task_id):
    """Delete a task."""
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]

# ============ Helper Functions ============

def find_task(task_id):
    """Find task by ID."""
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

def filter_tasks(completed=None, priority=None):
    """Filter tasks by criteria."""
    result = tasks
    if completed is not None:
        result = [t for t in result if t["completed"] == completed]
    if priority:
        result = [t for t in result if t["priority"] == priority]
    return result

# ============ Display Functions ============

def format_task(task):
    """Format single task for display."""
    status = "✓" if task["completed"] else " "
    return f"[{status}] {task['id']}: {task['title']} ({task['priority']})"

def list_tasks(tasks_to_show=None):
    """Display list of tasks."""
    tasks_to_show = tasks_to_show or tasks
    if not tasks_to_show:
        print("No tasks found.")
        return

    for task in tasks_to_show:
        print(format_task(task))

# Usage
from datetime import datetime

add_task("Buy groceries", "Milk, eggs, bread", "high")
add_task("Call mom", "Weekly check-in", "medium")
add_task("Finish project", "Due Friday", "high")

print("All tasks:")
list_tasks()

print("\nHigh priority:")
list_tasks(filter_tasks(priority="high"))
```

---

## Common Beginner Mistakes

### Mistake 1: Creating "God Functions"

```python
# BAD: Does everything
def do_everything(data):
    # Validate
    # Clean
    # Save
    # Email
    # Log
    # Report
    # Notify
    pass

# GOOD: One function, one job
def validate_data(data): pass
def clean_data(data): pass
def save_data(data): pass
```

### Mistake 2: Too Many Dependencies

```python
# BAD: Depends on everything
def process_user(user_data):
    db.save(user_data)
    email.send(user_data)
    cache.update(user_data)
    logger.log(user_data)
    analytics.track(user_data)
    backup.store(user_data)
    # Too many responsibilities!

# GOOD: High-level orchestrates
def process_user(user_data):
    save_user_data(user_data)
    notify_user(user_data)
```

### Mistake 3: Unclear Module Names

```python
# BAD: What do these do?
def func1(): pass
def func2(): pass
def helper(): pass
def process(): pass

# GOOD: Clear, descriptive names
def validate_email(): pass
def calculate_tax(): pass
def format_currency(): pass
def generate_report(): pass
```

### Mistake 4: Deep Nesting

```python
# BAD: Deeply nested and complex
def process_data(data):
    if data:
        if data['items']:
            for item in data['items']:
                if item['active']:
                    if item['price'] > 0:
                        # Finally do something!
                        pass

# GOOD: Flatten with early returns
def process_data(data):
    if not data or not data.get('items'):
        return

    for item in data['items']:
        if not item.get('active'):
            continue
        if item.get('price', 0) <= 0:
            continue
        # Do something with valid item
```

---

## Practice Exercises

### Exercise 1: Refactor a Messy Function

Take this messy function and break it into smaller ones:

```python
def messy_function(data):
    """Clean data, validate it, save it, and log it."""
    # Clean the data
    cleaned = {}
    for key, value in data.items():
        if isinstance(value, str):
            cleaned[key] = value.strip()
        else:
            cleaned[key] = value

    # Validate the data
    if 'email' in cleaned and '@' not in cleaned['email']:
        return None
    if 'age' in cleaned and cleaned['age'] < 0:
        return None

    # Save to database
    import sqlite3
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO data VALUES (?, ?)",
                   (cleaned.get('name'), cleaned.get('email')))
    conn.commit()
    conn.close()

    # Log it
    with open('log.txt', 'a') as f:
        f.write(f"Saved: {cleaned}\n")

    return cleaned
```

### Exercise 2: Build a Calculator Module

Create a modular calculator with:
- `operations.py` - Basic math operations
- `validation.py` - Input checking
- `history.py` - Track calculations
- `display.py` - Format results
- `main.py` - Put it all together

### Exercise 3: Design a Library System

Design modules for a simple library:
- Book management (add, remove, search)
- User management (patrons, librarians)
- Checkout system (borrow, return)
- Due date tracking
- Late fee calculation

Draw the module structure and write key functions.

---

## Key Takeaways

1. **Single Responsibility** - One function = one job
2. **Function Composition** - Build complex from simple
3. **Separation of Concerns** - Group related functions together
4. **Clear Interfaces** - Document what functions need and return
5. **Testability** - Small functions are easy to test
6. **Reusability** - Well-designed functions can be used anywhere

## Quick Reference Card

| Principle | Description |
|-----------|-------------|
| Single Responsibility | Function does ONE thing well |
| Function Composition | Combine small functions into workflows |
| Abstraction Levels | High-level orchestrates, low-level implements |
| Clear Contracts | Document inputs, outputs, errors |
| Separation of Concerns | Group by purpose (data, validation, email) |
| Testability | Each function testable in isolation |

## Checklist for Good Functions

- [ ] Does one thing and does it well
- [ ] Has a clear, descriptive name
- [ ] Is 20 lines or less
- [ ] Has 3 or fewer parameters (ideally)
- [ ] Has no side effects (doesn't change global state)
- [ ] Is documented with docstring
- [ ] Handles errors gracefully
- [ ] Is easy to test independently

---

## Further Reading

- **Next**: Learn about modules and packages (Session 20)
- **Practice**: Complete all exercises above
- **Challenge**: Refactor one of your old projects using these principles
- **Explore**: Read about "Clean Code" by Robert Martin
