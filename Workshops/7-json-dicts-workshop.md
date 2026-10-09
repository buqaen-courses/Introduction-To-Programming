# Python Tutorial: Dictionaries (JSON) and Working with APIs

Welcome! In this tutorial, you'll learn how to work with **dictionaries** in Python and how to handle **JSON data** – the language of modern APIs. We'll use the free [randomuser.me](https://randomuser.me) API to fetch random user data and parse the results. This is a perfect real-world example because the API returns nicely structured JSON that you'll learn to navigate.

By the end, you'll be able to:
- Understand Python dictionaries (including nested ones)
- Make HTTP requests to an API using `requests`
- Parse JSON responses into Python dictionaries
- Extract specific pieces of information from complex nested data
- Handle API parameters to filter results

Let's dive in!

---

## 1. Dictionary Crash Course

Before we fetch data from the internet, let's quickly review Python dictionaries – they're the foundation for working with JSON.

### What is a Dictionary?

A dictionary stores data in **key-value pairs**. Think of it like a real dictionary: you look up a word (the key) and get its definition (the value).

```python
# A simple dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print(person["name"])  # Alice
print(person.get("age"))  # 30 (safer way, returns None if key missing)
```

### Nested Dictionaries

Values in a dictionary can themselves be dictionaries (or lists). This is crucial because APIs often return nested data.

```python
# A dictionary with nested structures
user = {
    "name": {
        "first": "John",
        "last": "Doe"
    },
    "location": {
        "city": "Paris",
        "country": "France"
    },
    "hobbies": ["reading", "cycling"]
}

# Access nested values
print(user["name"]["first"])     # John
print(user["location"]["city"])  # Paris
print(user["hobbies"][0])        # reading
```

---

## 2. JSON and APIs – What's the Connection?

**JSON** (JavaScript Object Notation) is a lightweight data format that looks almost identical to Python dictionaries. It's how most web APIs send and receive data .

When you request data from an API like randomuser.me, you get back a JSON string. Python's `json` module converts that string into a Python dictionary (or list of dictionaries) so you can work with it easily.

Here's a tiny sample of what randomuser.me returns:

```json
{
  "results": [
    {
      "gender": "male",
      "name": {
        "title": "Mr",
        "first": "John",
        "last": "Smith"
      },
      "location": {
        "street": {
          "number": 123,
          "name": "Main Street"
        },
        "city": "Springfield",
        "state": "Illinois",
        "country": "United States"
      },
      "email": "john.smith@example.com"
    }
  ]
}
```

Notice the structure: it's a dictionary with a key `"results"` whose value is a list. Each item in that list is a dictionary representing one user. This nesting is exactly what we'll learn to navigate.

---

## 3. Setting Up – Installing `requests`

To talk to an API, we need the `requests` library. It's not built into Python, so install it first:

```bash
pip install requests
```

Then import it along with `json` (which is built-in) :

```python
import requests
import json
```

---

## 4. Your First API Call to randomuser.me

Let's fetch a single random user and see what we get.

```python
import requests

# Make a GET request to the API
response = requests.get("https://randomuser.me/api/")

# Check if the request was successful
if response.status_code == 200:
    print("Success! Here's the raw JSON:")
    print(response.text)  # This is a JSON string
else:
    print(f"Oops, something went wrong. Status code: {response.status_code}")
```

**What's happening?**
- `requests.get()` sends an HTTP GET request to the URL .
- The server replies with a response object.
- `response.status_code` tells us if it worked (200 means OK) .
- `response.text` contains the raw JSON as a string.

---

## 5. Parsing JSON into a Python Dictionary

That JSON string is hard to work with directly. Let's convert it to a Python dictionary.

### Method 1: Using `json.loads()`

```python
import requests
import json

response = requests.get("https://randomuser.me/api/")
if response.status_code == 200:
    # Parse the JSON string into a Python dictionary
    data = json.loads(response.text)
    print(type(data))  # <class 'dict'>
```

### Method 2: Using `response.json()` (Even Easier!)

The `requests` library has a built-in shortcut :

```python
import requests

response = requests.get("https://randomuser.me/api/")
if response.status_code == 200:
    data = response.json()   # directly gives you a dictionary
    print(type(data))         # <class 'dict'>
```

We'll use `response.json()` from now on – it's cleaner.

---

## 6. Navigating the Random User Data Structure

Now that we have a Python dictionary, let's explore its structure and extract useful information.

First, let's see what keys the top-level dictionary has:

```python
import requests

response = requests.get("https://randomuser.me/api/")
data = response.json()

print(data.keys())  
# Output: dict_keys(['results', 'info'])
```

The API returns two main parts :
- `"results"`: a list containing the user(s) we requested.
- `"info"`: metadata about the request (seed, results count, version, etc.).

Since we asked for one user, `data["results"]` is a list with one item. Let's grab that user:

```python
user = data["results"][0]   # the first (and only) user
print(user.keys())
```

You'll see keys like `"gender"`, `"name"`, `"location"`, `"email"`, `"login"`, `"dob"`, `"registered"`, `"phone"`, `"cell"`, `"id"`, `"picture"`, `"nat"`. Many of these are themselves dictionaries.

### Extracting Basic Info

```python
# Get the full name
first = user["name"]["first"]
last = user["name"]["last"]
full_name = f"{first} {last}"
print(f"Name: {full_name}")

# Get email
email = user["email"]
print(f"Email: {email}")

# Get gender
gender = user["gender"]
print(f"Gender: {gender}")
```

### Digging into Location

The `"location"` field is a dictionary containing street, city, state, country, postcode, and coordinates. The street itself is a dictionary with number and name .

```python
location = user["location"]
city = location["city"]
state = location["state"]
country = location["country"]
postcode = location["postcode"]

# Street is nested
street_num = location["street"]["number"]
street_name = location["street"]["name"]
street = f"{street_num} {street_name}"

print(f"Address: {street}, {city}, {state}, {postcode}, {country}")
```

### Getting the Date of Birth

```python
dob = user["dob"]["date"]   # ISO format string
age = user["dob"]["age"]     # integer age
print(f"DOB: {dob}, Age: {age}")
```

### Profile Picture

```python
picture_url = user["picture"]["large"]   # also medium, thumbnail
print(f"Profile picture: {picture_url}")
```

### Login Credentials (if you need them)

```python
username = user["login"]["username"]
password = user["login"]["password"]
print(f"Username: {username}, Password: {password}")
```

---

## 7. Handling Multiple Results

You can ask for more than one user by adding a query parameter. For example, to get 5 users :

```python
response = requests.get("https://randomuser.me/api/?results=5")
data = response.json()
users = data["results"]   # this is a list of 5 users

print(f"Got {len(users)} users")

# Loop through them (yes, we're using a for loop!)
for i, user in enumerate(users, 1):
    name = f"{user['name']['first']} {user['name']['last']}"
    print(f"{i}. {name}")
```

Even though we haven't formally covered loops yet, this is a simple one to show how you'd process multiple records.

---

## 8. Filtering Results with Parameters

The randomuser.me API accepts many parameters to customize the results . You pass them as query string parameters.

### Get Only Female Users

```python
response = requests.get("https://randomuser.me/api/?gender=female")
data = response.json()
user = data["results"][0]
print(f"Gender: {user['gender']}")   # should be 'female'
```

### Get Users from a Specific Country (Nationality)

Use the `nat` parameter. For example, Canadian users:

```python
response = requests.get("https://randomuser.me/api/?nat=ca")
```

Multiple countries: `?nat=us,gb,fr`

### Combine Parameters

You can combine multiple parameters with `&`. For example, 3 female users from Australia:

```python
response = requests.get("https://randomuser.me/api/?results=3&gender=female&nat=au")
data = response.json()
for user in data["results"]:
    print(f"{user['name']['first']} from {user['location']['country']}")
```

---

## 9. Putting It All Together – A Complete Example

Here's a full program that fetches 5 random users and displays their names, emails, and countries in a formatted way:

```python
import requests

# Fetch 5 random users
url = "https://randomuser.me/api/?results=5"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    users = data["results"]
    
    print("=" * 50)
    print("RANDOM USER GENERATOR")
    print("=" * 50)
    
    for i, user in enumerate(users, 1):
        name = f"{user['name']['first']} {user['name']['last']}"
        email = user["email"]
        country = user["location"]["country"]
        
        print(f"{i}. {name}")
        print(f"   Email: {email}")
        print(f"   Country: {country}")
        print()
else:
    print(f"Request failed with status code {response.status_code}")
```

---

## 10. Common Pitfalls and Tips

### Always Check the Status Code

APIs can fail for many reasons. Always check `response.status_code == 200` before parsing.

### Use `.get()` for Safer Access

When navigating deep structures, some keys might be missing. Using `.get()` avoids `KeyError` .

```python
# Risky:
city = user["location"]["city"]

# Safer:
city = user.get("location", {}).get("city", "Unknown")
```

### Handle Empty Lists

If you request 0 results, `data["results"]` will be an empty list. Check its length before accessing elements.

### Pretty Print for Debugging

When exploring a new API, it's helpful to see the structure clearly:

```python
import json
print(json.dumps(data, indent=2))  # pretty-print the JSON
```

---

## 11. Practice Exercises

Now it's your turn! Try these exercises to reinforce what you've learned.

### Exercise 1: Basic Extraction
Fetch a single random user and print:
- Their full name
- Their phone number
- Their profile picture thumbnail URL

### Exercise 2: Age Calculator
Fetch a user, extract their date of birth, and calculate how many days old they are (approximately). (Hint: you'll need the `datetime` module.)

### Exercise 3: Multiple Users with Filtering
Fetch 10 male users from Germany (`nat=de`). Then print a list showing:
- Index number
- First name, last initial (e.g., "Hans M.")
- City they live in

### Exercise 4: Find the Oldest
Fetch 20 users and determine which one is the oldest (by `dob.age`). Print their name, age, and country.

### Exercise 5: Build a Mini Address Book
Fetch 15 users and create a simple address book. For each user, store their full name, email, and city. Then print the address book sorted by city.

---

## 12. Summary

Congratulations! You've learned:

- How to work with **nested dictionaries** in Python
- What **JSON** is and why it's important for APIs 
- How to use the **`requests`** library to make API calls 
- How to parse JSON responses into Python dictionaries 
- How to navigate complex nested data structures from the **randomuser.me** API 
- How to add **parameters** to filter API results 

These skills are fundamental for any Python developer working with web data. You can now fetch data from thousands of public APIs and integrate real-world information into your programs.

Keep experimenting – try different APIs, build small projects, and have fun!

**Happy coding!** 🐍