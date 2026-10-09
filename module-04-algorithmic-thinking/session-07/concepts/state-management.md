# State Management: How Programs Remember

## Introduction: Programs with Memory

Think about a calculator app. When you press:
1. **5** - Display shows "5"
2. **+** - Calculator remembers you want to add
3. **3** - Display shows "3"
4. **=** - Calculator shows "8" (5 + 3)

How does the calculator remember the 5 while you enter the 3? It uses **state**.

**State** is the information a program remembers between actions.

---

## What is State?

### Definition

**State** = All the data a program is currently tracking and remembering.

### Analogy: A Chef in the Kitchen

A chef maintains "state" while cooking:
- **Current temperature** of the stove
- **Which ingredients** have been added
- **How long** the food has been cooking
- **What step** of the recipe they're on

Without remembering these things, the chef couldn't cook properly!

### State in a Program

```python
# Shopping cart state
cart_state = {
    "items": ["apple", "banana"],
    "total": 3.50,
    "user_id": "user123",
    "logged_in": True
}
```

---

## Types of State

### 1. Application State

**What the program knows about itself.**

```python
# Game application state
game_state = {
    "score": 1500,
    "level": 3,
    "lives": 2,
    "paused": False,
    "sound_on": True
}
```

### 2. User State

**Information about the current user.**

```python
# User session state
user_state = {
    "username": "alice",
    "logged_in": True,
    "last_activity": "2024-01-15 10:30:00",
    "permissions": ["read", "write"],
    "shopping_cart": ["item1", "item2"]
}
```

### 3. UI State

**What the interface currently shows.**

```python
# UI state
ui_state = {
    "current_page": "dashboard",
    "sidebar_open": True,
    "modal_visible": False,
    "selected_items": ["doc1", "doc2"],
    "sort_column": "date"
}
```

### 4. Data State

**The actual information being worked with.**

```python
# Document editor state
document_state = {
    "filename": "report.txt",
    "content": "This is my report...",
    "cursor_position": 45,
    "selection_start": None,
    "selection_end": None,
    "modified": True,
    "saved": False
}
```

---

## Stateful vs Stateless Systems

### Stateful System (Remembers Things)

**Example: Online Shopping Cart**
```
User Action → System Response
─────────────────────────────────────
"Add apple" → Cart now has: [apple]
"Add banana" → Cart now has: [apple, banana]
"View cart" → Shows: [apple, banana], Total: $2.50
"Remove apple" → Cart now has: [banana]
```

The system **remembers** the cart contents between actions.

### Stateless System (Forgets Everything)

**Example: Calculator (basic mode)**
```
User Action → System Response
─────────────────────────────────────
"5" → Display: 5
"+ 3" → Display: 8 (forgets the 5 after showing result)
"+ 2" → Display: 2 (forgets everything!)
```

The system **forgets** everything after each calculation.

### Comparison Table

| Feature | Stateful | Stateless |
|---------|----------|-----------|
| **Memory** | Remembers data | Starts fresh each time |
| **Complexity** | More complex | Simpler |
| **Examples** | Shopping carts, games | Basic calculators, math functions |
| **Scalability** | Harder to scale | Easier to scale |
| **Recovery** | Can recover state | Must restart |

---

## Managing State in Programs

### Method 1: Variables

Simple state using variables:

```python
def simple_counter():
    count = 0  # State variable
    
    while True:
        action = input("Enter 'add', 'sub', or 'quit': ")
        
        if action == "add":
            count += 1  # Update state
            print(f"Count: {count}")
        
        elif action == "sub":
            count -= 1  # Update state
            print(f"Count: {count}")
        
        elif action == "quit":
            break
    
    return count
```

### Method 2: Dictionaries

Organized state using dictionaries:

```python
def bank_account():
    account = {
        "balance": 1000.00,
        "transactions": [],
        "account_number": "ACC123"
    }
    
    while True:
        print(f"\nBalance: ${account['balance']:.2f}")
        action = input("Deposit, Withdraw, or History? ").lower()
        
        if action == "deposit":
            amount = float(input("Amount: $"))
            account["balance"] += amount
            account["transactions"].append(f"+${amount:.2f}")
            
        elif action == "withdraw":
            amount = float(input("Amount: $"))
            if amount <= account["balance"]:
                account["balance"] -= amount
                account["transactions"].append(f"-${amount:.2f}")
            else:
                print("Insufficient funds!")
                
        elif action == "history":
            print("\nTransaction History:")
            for trans in account["transactions"]:
                print(f"  {trans}")
                
        elif action == "quit":
            break
    
    return account
```

### Method 3: Classes (Object-Oriented)

Advanced state using classes:

```python
class TodoList:
    """A todo list that maintains state."""
    
    def __init__(self):
        self.tasks = []  # State: list of tasks
        self.completed_count = 0  # State: tracking
    
    def add_task(self, task):
        """Add a new task."""
        self.tasks.append({
            "text": task,
            "done": False,
            "created": "now"
        })
    
    def complete_task(self, index):
        """Mark a task as complete."""
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            self.completed_count += 1
    
    def get_stats(self):
        """Return current statistics."""
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t["done"])
        pending = total - completed
        
        return {
            "total": total,
            "completed": completed,
            "pending": pending
        }

# Usage
my_todos = TodoList()  # Create with empty state
my_todos.add_task("Buy groceries")
my_todos.add_task("Finish report")
my_todos.complete_task(0)

print(my_todos.get_stats())
# {'total': 2, 'completed': 1, 'pending': 1}
```

---

## State Transitions

### What is a State Transition?

Changing from one state to another based on an event or action.

### Example: Traffic Light

```
States: [RED] → [RED-YELLOW] → [GREEN] → [YELLOW] → [RED]

Current State    Event           Next State
────────────────────────────────────────────────
RED              Timer expires   GREEN
GREEN            Timer expires   YELLOW  
YELLOW           Timer expires   RED
(any)            Emergency       FLASHING
```

### Example: User Login State Machine

```
States: [LOGGED_OUT] → [LOGGING_IN] → [LOGGED_IN] → [LOGGED_OUT]

Current State     Event              Next State
────────────────────────────────────────────────────
LOGGED_OUT        User clicks login  LOGGING_IN
LOGGING_IN        Valid credentials  LOGGED_IN
LOGGING_IN        Invalid password   LOGGED_OUT (error)
LOGGED_IN         User logs out      LOGGED_OUT
LOGGED_IN         Session expires    LOGGED_OUT
```

### Code Example: State Machine

```python
class LoginSystem:
    def __init__(self):
        self.state = "LOGGED_OUT"
        self.username = None
    
    def login(self, username, password):
        if self.state != "LOGGED_OUT":
            return "Already logged in or processing"
        
        self.state = "LOGGING_IN"
        
        # Check credentials
        if self._validate(username, password):
            self.state = "LOGGED_IN"
            self.username = username
            return f"Welcome, {username}!"
        else:
            self.state = "LOGGED_OUT"
            return "Invalid credentials"
    
    def logout(self):
        if self.state != "LOGGED_IN":
            return "Not logged in"
        
        self.state = "LOGGED_OUT"
        self.username = None
        return "Logged out successfully"
    
    def get_status(self):
        return {
            "state": self.state,
            "user": self.username
        }
    
    def _validate(self, username, password):
        # Simplified validation
        return username == "admin" and password == "secret"

# Usage
system = LoginSystem()
print(system.get_status())  # {'state': 'LOGGED_OUT', 'user': None}

print(system.login("admin", "secret"))  # Welcome!
print(system.get_status())  # {'state': 'LOGGED_IN', 'user': 'admin'}

print(system.logout())  # Logged out
print(system.get_status())  # {'state': 'LOGGED_OUT', 'user': None}
```

---

## Common State Management Patterns

### Pattern 1: Current State Storage

Keep track of "where we are now":

```python
def wizard_signup():
    current_step = 1  # State: current step
    user_data = {}    # State: collected data
    
    while current_step <= 3:
        if current_step == 1:
            user_data["name"] = input("Enter name: ")
            current_step = 2  # State transition
            
        elif current_step == 2:
            user_data["email"] = input("Enter email: ")
            current_step = 3  # State transition
            
        elif current_step == 3:
            print(f"Confirm: {user_data}")
            confirm = input("Confirm? (yes/no): ")
            if confirm == "yes":
                save_user(user_data)
                current_step = 4  # Done!
            else:
                current_step = 1  # Start over
    
    print("Signup complete!")
```

### Pattern 2: History/Undo

Keep history to allow undo:

```python
class TextEditor:
    def __init__(self):
        self.content = ""
        self.history = []  # State: history
        self.history_index = -1  # State: current position in history
    
    def type_text(self, text):
        # Save current state to history
        self.history = self.history[:self.history_index + 1]
        self.history.append(self.content)
        self.history_index += 1
        
        # Update content
        self.content += text
    
    def undo(self):
        if self.history_index >= 0:
            self.content = self.history[self.history_index]
            self.history_index -= 1
    
    def redo(self):
        if self.history_index < len(self.history) - 1:
            self.history_index += 1
            self.content = self.history[self.history_index]
```

### Pattern 3: Caching/Memoization

Remember results to avoid recalculation:

```python
# Without caching
def fibonacci_slow(n):
    if n <= 1:
        return n
    return fibonacci_slow(n-1) + fibonacci_slow(n-2)
    # Very slow for large n!

# With caching (state management)
def fibonacci_fast(n, cache={}):
    if n in cache:  # Check state first
        return cache[n]
    
    if n <= 1:
        result = n
    else:
        result = fibonacci_fast(n-1, cache) + fibonacci_fast(n-2, cache)
    
    cache[n] = result  # Save to state
    return result
```

---

## Persisting State (Saving State)

### Why Persist State?

Without persistence, state is lost when the program ends!

### Method 1: File Storage

```python
import json

def save_state(state, filename="state.json"):
    """Save state to a file."""
    with open(filename, "w") as f:
        json.dump(state, f)
    print(f"State saved to {filename}")

def load_state(filename="state.json"):
    """Load state from a file."""
    try:
        with open(filename, "r") as f:
            state = json.load(f)
        print(f"State loaded from {filename}")
        return state
    except FileNotFoundError:
        print("No saved state found, starting fresh")
        return {}

# Usage
app_state = {
    "user": "alice",
    "preferences": {"theme": "dark"},
    "last_opened": "document.txt"
}

save_state(app_state)
loaded_state = load_state()
print(loaded_state)
```

### Method 2: Database Storage

```python
# Conceptual example using SQLite
import sqlite3

def save_to_database(user_id, state):
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT OR REPLACE INTO user_states (user_id, data)
        VALUES (?, ?)
    ''', (user_id, json.dumps(state)))
    
    conn.commit()
    conn.close()

def load_from_database(user_id):
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT data FROM user_states WHERE user_id = ?
    ''', (user_id,))
    
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return json.loads(result[0])
    return None
```

---

## State Management Best Practices

### 1. Keep State Minimal

Only store what you need:

```python
# Good - minimal state
game_state = {
    "player_position": (10, 20),
    "health": 100,
    "inventory": ["sword", "potion"]
}

# Bad - too much redundant state
game_state = {
    "player_position": (10, 20),
    "health": 100,
    "max_health": 100,
    "health_percentage": 100.0,  # Can calculate from health/max_health
    "inventory": ["sword", "potion"],
    "inventory_count": 2,  # Can calculate from inventory
    "last_position": (10, 20),  # Same as current position!
}
```

### 2. Immutable State Updates

Don't modify state directly - create new state:

```python
# Good - immutable update
def add_item(current_state, item):
    new_inventory = current_state["inventory"] + [item]
    return {
        **current_state,
        "inventory": new_inventory
    }

# Bad - mutating state directly
def add_item_bad(current_state, item):
    current_state["inventory"].append(item)  # Mutates!
    return current_state
```

### 3. Single Source of Truth

Don't duplicate state:

```python
# Bad - duplicated state
user_state = {
    "name": "Alice",
    "profile": {
        "name": "Alice"  # Duplicated!
    }
}

# Good - single source
user_state = {
    "name": "Alice",  # Only here
    "profile": {
        "bio": "Software developer",
        "location": "NYC"
    }
}
```

### 4. Clear State Transitions

Make it obvious how state changes:

```python
# Good - explicit transitions
def process_order(order_state, action):
    if action == "submit":
        return {**order_state, "status": "PENDING"}
    elif action == "pay":
        return {**order_state, "status": "PAID"}
    elif action == "ship":
        return {**order_state, "status": "SHIPPED"}
    else:
        return order_state  # No change
```

---

## Practice Exercises

### Exercise 1: Identify State

For each application, list 3-5 pieces of state:

1. Music player app
2. E-commerce shopping cart
3. Video game
4. Chat application

### Exercise 2: Design State Management

Design state management for a **simple game**:

```python
game_state = {
    # What state do you need?
    
}

def initialize_game():
    # Set up initial state
    pass

def update_game(state, action):
    # Update state based on action
    pass
```

### Exercise 3: State Machine

Create a state machine for a **traffic light**:

- States: RED, GREEN, YELLOW
- Events: TIMER_EXPIRED, EMERGENCY_VEHICLE
- Transitions: Define what happens for each event in each state

### Exercise 4: Undo Functionality

Implement undo functionality for a simple text editor:

```python
class SimpleEditor:
    def __init__(self):
        self.content = ""
        # Add history state here
    
    def type_text(self, text):
        # Add text and save to history
        pass
    
    def undo(self):
        # Restore previous state
        pass
```

---

## Key Takeaways

1. **State is remembered data**: What the program knows right now
2. **Stateful vs Stateless**: Systems that remember vs systems that forget
3. **State transitions**: How state changes over time
4. **State management patterns**: Variables, dictionaries, classes
5. **Persistence**: Saving state so it's not lost

## Remember

```
┌─────────────────────────────────────────┐
│         STATE MANAGEMENT                │
├─────────────────────────────────────────┤
│                                         │
│  INPUT → [UPDATE STATE] → OUTPUT       │
│              ↑                          │
│         [REMEMBER FOR                  │
│          NEXT TIME]                     │
│                                         │
└─────────────────────────────────────────┘
```

### Key Questions for State Design

1. **What needs to be remembered?** (Identify state)
2. **When does it change?** (Identify transitions)
3. **Who can change it?** (Access control)
4. **Should it persist?** (Save to disk/database?)

---

## Next Steps

- Learn about global state vs local state
- Study Redux/Flux architecture (for web apps)
- Explore database design for state persistence
- Understand concurrent state access (threading)
