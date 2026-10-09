# Python Tutorial: Dictionary Operations and JSON Manipulation

Welcome! This tutorial focuses on the **fundamental operations** you can perform on dictionaries – the building blocks of JSON data. While the previous tutorial showed you how to fetch JSON from an API, it assumed you already knew how to manipulate dictionaries. Here we'll cover all the essential dictionary operations with plenty of examples, so you can confidently work with JSON data.

**What you'll learn:**
- Creating and accessing dictionaries
- Safe access with `.get()`
- Adding, updating, and deleting keys
- Merging dictionaries
- Working with nested structures
- Copying dictionaries correctly
- Dictionary comprehensions
- Practical examples using JSON from randomuser.me

Let's dive in!

---

## 1. Dictionary Basics (Quick Recap)

A dictionary stores data in **key-value pairs**. Keys must be immutable (strings, numbers, tuples), values can be anything.

```python
# Creating a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
```

---

## 2. Accessing Values

### Direct Access with `[]`
```python
print(person["name"])   # Alice
# But if key doesn't exist, you get a KeyError
# print(person["country"])  # KeyError!
```

### Safe Access with `.get()`
The `.get()` method returns the value if the key exists, otherwise it returns `None` (or a default you provide).

```python
print(person.get("name"))          # Alice
print(person.get("country"))       # None (no error)
print(person.get("country", "USA")) # USA (default value)
```

This is **essential** when working with JSON data where some fields might be missing.

---

## 3. Adding or Updating Keys

Simply assign a value to a key. If the key exists, it updates; if not, it adds.

```python
# Add a new key
person["email"] = "alice@example.com"
print(person)  # now includes email

# Update an existing key
person["age"] = 31
print(person["age"])  # 31
```

---

## 4. Deleting Keys

### Using `del`
```python
del person["city"]   # removes the key "city"
# If key doesn't exist, del raises KeyError
```

### Using `.pop()`
`.pop()` removes the key and returns its value. You can provide a default to avoid errors.

```python
age = person.pop("age")          # removes "age" and returns 31
email = person.pop("email", None) # safe: returns None if "email" missing
```

### Using `.popitem()`
Removes and returns the last inserted key-value pair (useful for LIFO processing).

```python
last_item = person.popitem()  # returns (key, value)
```

### Clearing all items
```python
person.clear()   # empties the dictionary
```

---

## 5. Checking if a Key Exists

Use the `in` operator.

```python
if "name" in person:
    print("Name exists")
```

---

## 6. Merging Dictionaries

### Using `update()` (modifies the original)
```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d1.update(d2)   # d1 becomes {"a": 1, "b": 3, "c": 4}
```

### Using `|` (Python 3.9+) – creates a new dictionary
```python
merged = d1 | d2   # leaves d1 and d2 unchanged
```

### Using `|=` (Python 3.9+) – updates in place
```python
d1 |= d2   # same as d1.update(d2)
```

---

## 7. Iterating Over Dictionaries

### Keys only
```python
for key in person:
    print(key, person[key])
```

### Keys and values together
```python
for key, value in person.items():
    print(f"{key}: {value}")
```

### Values only
```python
for value in person.values():
    print(value)
```

---

## 8. Working with Nested Dictionaries

JSON data is often nested. Here's how to navigate and modify it.

### Accessing nested values
```python
user = {
    "name": {
        "first": "John",
        "last": "Doe"
    },
    "location": {
        "city": "Paris",
        "country": "France"
    }
}

print(user["name"]["first"])   # John
```

### Modifying nested values
```python
user["location"]["city"] = "Lyon"
```

### Adding a new nested key
```python
user["name"]["middle"] = "Michael"
```

### Safe access with `.get()` for nested keys
```python
city = user.get("location", {}).get("city", "Unknown")
```

---

## 9. Copying Dictionaries

Be careful: assignment does **not** create a copy.

```python
original = {"a": 1, "b": [2, 3]}
copy = original          # both refer to the same dictionary!
copy["a"] = 99
print(original["a"])     # 99 – oops!
```

### Shallow copy with `.copy()`
```python
copy = original.copy()   # new dict, but inner objects are still shared
copy["b"].append(4)
print(original["b"])     # [2, 3, 4] – because list is shared!
```

### Deep copy with `copy.deepcopy()`
To completely separate all nested structures, use `deepcopy`.

```python
import copy
deep_copy = copy.deepcopy(original)
deep_copy["b"].append(5)
print(original["b"])     # [2, 3, 4] – unchanged
```

---

## 10. Dictionary Comprehensions

A concise way to build dictionaries.

```python
# Squares of numbers 1 to 5
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filtering: only even numbers
even_squares = {x: x**2 for x in range(1, 6) if x % 2 == 0}
print(even_squares)  # {2: 4, 4: 16}
```

---

## 11. Practical JSON Examples with randomuser.me

Let's combine everything with data from the randomuser.me API.

### Fetch and explore a user
```python
import requests

response = requests.get("https://randomuser.me/api/")
user = response.json()["results"][0]

# Safely get name
first = user.get("name", {}).get("first", "Unknown")
last = user.get("name", {}).get("last", "Unknown")
print(f"Name: {first} {last}")

# Get email, or a default if missing
email = user.get("email", "No email provided")
print(f"Email: {email}")

# Update a field – e.g., add a note
user["note"] = "Fetched from API"
```

### Remove a key safely
```python
# Remove login info if present
if "login" in user:
    login_data = user.pop("login")  # removes and returns
    print("Login info removed")
```

### Merge with additional data
```python
extra_info = {"source": "randomuser.me", "timestamp": "2025-01-01"}
user.update(extra_info)   # now user has source and timestamp
```

### Build a list of user emails from multiple results
```python
response = requests.get("https://randomuser.me/api/?results=5")
users = response.json()["results"]

emails = [user["email"] for user in users]   # list comprehension
print(emails)
```

---

## 12. Common Pitfalls and Tips

- **Keys must be immutable**: lists cannot be keys, but tuples can.
- **Order**: Since Python 3.7, dictionaries preserve insertion order.
- **Default values with `.get()`**: always use it when you're unsure if a key exists.
- **Be careful with mutable values**: if a dictionary value is a list or another dict, modifying it affects all references unless you deepcopy.
- **Pretty printing JSON**: use `json.dumps(data, indent=2)` for readability.

---

## 13. Practice Exercises

### Exercise 1: Safe Access
Given the nested dictionary below, write code to safely extract the `"city"` without raising an error, defaulting to `"Unknown"` if missing.
```python
data = {
    "user": {
        "name": "Alice",
        # "address" key is missing
    }
}
```

### Exercise 2: Update and Delete
Start with `inventory = {"apples": 5, "bananas": 3}`. Perform:
- Add 2 more apples (update the value)
- Remove bananas
- Add a new item "oranges" with quantity 4
- Print the final dictionary.

### Exercise 3: Merge Two Dictionaries
Given `defaults = {"theme": "light", "font": "Arial"}` and `user_prefs = {"font": "Helvetica", "font_size": 12}`, merge them so that `user_prefs` overrides `defaults`. The result should be `{"theme": "light", "font": "Helvetica", "font_size": 12}`.

### Exercise 4: Nested Update
Using the user dictionary from randomuser.me, update the user's location to add a `"timezone"` field with value `"UTC+1"`.

### Exercise 5: Copying
Create a dictionary `original = {"items": [1, 2, 3]}`. Make a shallow copy and a deep copy. Modify the list inside each copy and observe the changes in the original.

---

## 14. Answers

### Exercise 1
```python
city = data.get("user", {}).get("address", {}).get("city", "Unknown")
print(city)  # Unknown
```

### Exercise 2
```python
inventory = {"apples": 5, "bananas": 3}
inventory["apples"] += 2           # update
del inventory["bananas"]            # delete
inventory["oranges"] = 4            # add
print(inventory)  # {'apples': 7, 'oranges': 4}
```

### Exercise 3
```python
defaults = {"theme": "light", "font": "Arial"}
user_prefs = {"font": "Helvetica", "font_size": 12}
merged = defaults | user_prefs   # Python 3.9+
# Or: merged = {**defaults, **user_prefs}
print(merged)
```

### Exercise 4
```python
# Assuming user is already fetched
user["location"]["timezone"] = "UTC+1"
```

### Exercise 5
```python
import copy
original = {"items": [1, 2, 3]}

shallow = original.copy()
deep = copy.deepcopy(original)

shallow["items"].append(4)
deep["items"].append(5)

print(original["items"])  # [1, 2, 3, 4] (shallow affected it)
print(deep["items"])      # [1, 2, 3, 5] (deep separate)
```

---

## Summary

You now have a complete toolkit for dictionary manipulation in Python – from basic CRUD operations to safe access, merging, and handling nested structures. These skills are essential for working with JSON data from APIs like randomuser.me. Remember to always use `.get()` when you're not sure a key exists, and understand the difference between shallow and deep copies when dealing with nested data.

Practice with real APIs, experiment, and you'll soon be a dictionary pro! Happy coding! 🐍