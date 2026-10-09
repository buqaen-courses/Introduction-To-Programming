# دیکشنری‌های پایتون: جفت‌های کلید-مقدار

## دیکشنری چیست؟

**دیکشنری** مثل یک فرهنگ لغت یا دفترچه تلفن واقعی است: اطلاعات را به شکل جفت کلید و مقدار نگه می‌دارد. برای پیدا کردن اطلاعات از یک **کلید** استفاده می‌کنید (مثل یک کلمه) و یک **مقدار** می‌گیرید (مثل تعریف آن).

```python
# دیکشنری ساده
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# دسترسی با کلید، نه با موقعیت!
print(person["name"])   # "Alice"
print(person["age"])    # 25
```

### چرا دیکشنری‌ها مهم‌اند

دیکشنری‌ها بسیار پرکاربرد هستند:
- **جست‌وجوی سریع**: اطلاعات را بی‌درنگ با کلید پیدا کنید
- **داده معنادار**: کلیدها می‌گویند داده چه معنایی دارد
- **انعطاف‌پذیر**: هر نوع داده‌ای را نگه می‌دارند
- **مدل‌سازی دنیای واقعی**: برای نمایش اشیا عالی‌اند

### دیکشنری در برابر فهرست

| ویژگی | فهرست | دیکشنری |
|-------|-------|---------|
| دسترسی با | موقعیت (۰، ۱، ۲...) | کلید ("name"، "age") |
| ترتیب | حفظ می‌شود | حفظ می‌شود (پایتون ۳.۷+) |
| جست‌وجو | کند (پیمایش فهرست) | سریع (دسترسی مستقیم) |
| کاربرد | دنباله‌های مرتب | داده برچسب‌دار |

---

## ساخت دیکشنری

### ساخت پایه

```python
# دیکشنری خالی
empty = {}
empty = dict()   # جایگزین

# با مقادیر اولیه
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# استفاده از dict() با آرگومان کلیدی
person = dict(name="Alice", age=25, city="New York")

# از فهرستی از جفت‌ها
pairs = [("name", "Alice"), ("age", 25)]
person = dict(pairs)

# از دو فهرست با zip()
keys = ["name", "age", "city"]
values = ["Alice", 25, "NYC"]
person = dict(zip(keys, values))
```

### دیکشنری تودرتو

```python
# دیکشنری‌ها می‌توانند شامل دیکشنری‌های دیگر باشند!
student = {
    "name": "Alice",
    "age": 20,
    "grades": {
        "math": 95,
        "science": 88,
        "history": 92
    },
    "contact": {
        "email": "alice@example.com",
        "phone": "555-1234"
    }
}

# دسترسی به داده تودرتو
math_grade = student["grades"]["math"]      # 95
email = student["contact"]["email"]         # "alice@example.com"
```

---

## دسترسی به مقادیر دیکشنری

### دسترسی مستقیم (با احتیاط!)

```python
person = {"name": "Alice", "age": 25}

# دسترسی مستقیم با []
name = person["name"]    # "Alice"

# تلاش برای دسترسی به کلید ناشناخته خطا می‌دهد!
# salary = person["salary"]  # KeyError!
```

### دسترسی امن با get()

```python
person = {"name": "Alice", "age": 25}

# get() اگر کلید پیدا نشود None برمی‌گرداند
salary = person.get("salary")       # None (بدون خطا!)

# دادن مقدار پیش‌فرض
salary = person.get("salary", 0)    # 0 (پیش‌فرض)
city = person.get("city", "Unknown") # "Unknown"

# برای کلیدهای موجود هم کار می‌کند
name = person.get("name")            # "Alice"
```

### بررسی وجود کلید

```python
person = {"name": "Alice", "age": 25}

# با عملگر in
has_name = "name" in person      # True
has_salary = "salary" in person  # False

# الگوی دسترسی امن
if "age" in person:
    age = person["age"]
    print(f"Age: {age}")
else:
    print("Age not specified")
```

### استفاده از setdefault()

```python
person = {"name": "Alice"}

# اگر کلید وجود داشته باشد، مقدار آن برمی‌گردد
age = person.setdefault("age", 18)   # مقدار age را ۱۸ می‌گذارد و ۱۸ برمی‌گرداند
print(person)  # {"name": "Alice", "age": 18}

# اگر کلید وجود داشته باشد، مقدار موجود برمی‌گردد (تغییری نمی‌کند)
age = person.setdefault("age", 99)   # هنوز ۱۸، و ۱۸ برمی‌گرداند
```

---

## تغییر دیکشنری‌ها

### افزودن و به‌روزرسانی

```python
person = {"name": "Alice", "age": 25}

# افزودن جفت کلید-مقدار تازه
person["city"] = "New York"
# الان: {"name": "Alice", "age": 25, "city": "New York"}

# به‌روزرسانی مقدار موجود
person["age"] = 26
# الان: {"name": "Alice", "age": 26, "city": "New York"}

# به‌روزرسانی چند مقدار هم‌زمان
person.update({"age": 27, "job": "Engineer", "city": "Boston"})
# حالا job دارد، age به‌روز شد، city تغییر کرد
```

### حذف آیتم‌ها

```python
person = {
    "name": "Alice",
    "age": 27,
    "city": "Boston",
    "job": "Engineer"
}

# pop() - حذف و بازگرداندن مقدار
removed_city = person.pop("city")    # "Boston" را برمی‌گرداند
# الان: {"name": "Alice", "age": 27, "job": "Engineer"}

# pop() با پیش‌فرض (امن)
removed_hobby = person.pop("hobby", "No hobby")  # "No hobby" را برمی‌گرداند

# popitem() - آخرین آیتم را حذف و بازمی‌گرداند (پایتون ۳.۷+)
last_item = person.popitem()    # ("job", "Engineer") را برمی‌گرداند

# del - حذف می‌کند ولی بازگرداندن نمی‌کند
del person["age"]
# الان: {"name": "Alice"}

# clear() - همه را حذف می‌کند
person.clear()
# الان: {}
```

---

## کار با viewهای دیکشنری

### گرفتن کلیدها، مقدارها و آیتم‌ها

```python
person = {"name": "Alice", "age": 25, "city": "NYC"}

# گرفتن همه کلیدها
keys = person.keys()
print(keys)        # dict_keys(['name', 'age', 'city'])
print(list(keys))  # ['name', 'age', 'city']

# گرفتن همه مقدارها
values = person.values()
print(values)      # dict_values(['Alice', 25, 'NYC'])

# گرفتن همه جفت‌های کلید-مقدار
items = person.items()
print(items)       # dict_items([('name', 'Alice'), ('age', 25), ('city', 'NYC')])

# تبدیل به فهرستی از تاپل‌ها
pairs = list(person.items())
# [('name', 'Alice'), ('age', 25), ('city', 'NYC')]
```

### پیمایش روی دیکشنری

```python
person = {"name": "Alice", "age": 25, "city": "NYC"}

# پیمایش روی کلیدها (پیش‌فرض)
for key in person:
    print(f"{key}: {person[key]}")

# پیمایش روی کلیدها به‌صورت صریح
for key in person.keys():
    print(key)

# پیمایش روی مقدارها
for value in person.values():
    print(value)

# پیمایش روی جفت‌های کلید-مقدار (رایج‌ترین حالت!)
for key, value in person.items():
    print(f"{key} = {value}")

# Output:
# name = Alice
# age = 25
# city = NYC
```

---

## متدها و عملیات دیکشنری

### کپی کردن دیکشنری

```python
original = {"a": 1, "b": [2, 3]}

# کپی کم‌عمق
shallow = original.copy()
shallow = dict(original)   # جایگزین

# تغییر کپی - اشیای تودرتو مشترک‌اند!
shallow["b"].append(4)
print(original)   # {"a": 1, "b": [2, 3, 4]} - فهرست تودرتو تغییر کرد!

# کپی عمیق (کاملاً مستقل)
import copy
deep = copy.deepcopy(original)
deep["b"].append(5)
print(original)   # {"a": 1, "b": [2, 3, 4]} - بدون تغییر!
```

### اندازه دیکشنری

```python
person = {"name": "Alice", "age": 25, "city": "NYC"}

# شمردن آیتم‌ها
size = len(person)   # 3

# بررسی خالی بودن
if not person:       # اگر خالی باشد True است
    print("Dictionary is empty")

if len(person) == 0:  # همان چیزی است که می‌شود گفت
    print("Dictionary is empty")
```

### ادغام دیکشنری‌ها (پایتون ۳.۹+)

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}  # توجه: b در هر دو وجود دارد

# ادغام با عملگر | (مقادیر dict2 برنده می‌شوند)
merged = dict1 | dict2
# Result: {"a": 1, "b": 3, "c": 4}

# به‌روزرسانی درجا با |=
dict1 |= dict2
# dict1 حالا: {"a": 1, "b": 3, "c": 4}
```

---

## Dict Comprehension

دقیق مثل list comprehension، ولی برای دیکشنری!

### نحو پایه

```python
# روش معمولی
squares = {}
for x in range(1, 6):
    squares[x] = x ** 2

# Dict comprehension
squares = {x: x ** 2 for x in range(1, 6)}
# Result: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### با شرط

```python
# فقط اعداد زوج
even_squares = {x: x ** 2 for x in range(1, 11) if x % 2 == 0}
# Result: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# تبدیل دیکشنری موجود
original = {"a": 1, "b": 2, "c": 3}
doubled = {k: v * 2 for k, v in original.items()}
# Result: {"a": 2, "b": 4, "c": 6}

# جابه‌جایی کلیدها و مقدارها
swapped = {v: k for k, v in original.items()}
# Result: {1: "a", 2: "b", 3: "c"}
```

---

## مثال‌های کاربردی

### مثال ۱: شمارنده فراوانی کلمات

```python
def count_words(text):
    """Count how many times each word appears."""
    words = text.lower().split()
    frequency = {}

    for word in words:
        # حذف نقطه‌گذاری (روش ساده)
        word = word.strip(".,!?;:'\"")

        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency

# Usage
text = "the quick brown fox jumps over the lazy dog"
freq = count_words(text)

# پیدا کردن پرتکرارترین کلمه
most_common = max(freq.items(), key=lambda x: x[1])
print(f"Most common: '{most_common[0]}' ({most_common[1]} times)")

# چاپ همه فراوانی‌ها به ترتیب
for word, count in sorted(freq.items(), key=lambda x: -x[1]):
    print(f"{word}: {count}")
```

### مثال ۲: دفترچه تلفن ساده

```python
def phone_book_app():
    contacts = {}

    while True:
        print("\nPhone Book:")
        for name, number in contacts.items():
            print(f"  {name}: {number}")

        print("\nOptions: (a)dd, (l)ookup, (d)elete, (q)uit")
        choice = input("Choice: ").lower()

        if choice == 'a':
            name = input("Name: ")
            number = input("Number: ")
            contacts[name] = number
            print(f"Added {name}")

        elif choice == 'l':
            name = input("Name to look up: ")
            number = contacts.get(name)
            if number:
                print(f"{name}: {number}")
            else:
                print(f"{name} not found")

        elif choice == 'd':
            name = input("Name to delete: ")
            if name in contacts:
                del contacts[name]
                print(f"Deleted {name}")
            else:
                print(f"{name} not found")

        elif choice == 'q':
            print("Goodbye!")
            break

# Uncomment to run:
# phone_book_app()
```

### مثال ۳: مدیر نمرات دانشجو

```python
def create_student(name, grades):
    """Create a student dictionary with grades."""
    return {
        "name": name,
        "grades": grades,
        "average": sum(grades) / len(grades) if grades else 0
    }

def add_grade(student, subject, grade):
    """Add a grade for a subject."""
    if "grades_by_subject" not in student:
        student["grades_by_subject"] = {}

    student["grades_by_subject"][subject] = grade

    # به‌روزرسانی فهرست نمرات و میانگین
    student["grades"] = list(student["grades_by_subject"].values())
    student["average"] = sum(student["grades"]) / len(student["grades"])

def get_report(student):
    """Generate a formatted report."""
    report = f"\nReport for {student['name']}\n"
    report += "=" * 30 + "\n"

    if "grades_by_subject" in student:
        for subject, grade in student["grades_by_subject"].items():
            report += f"{subject:12}: {grade:3}\n"

    report += "-" * 30 + "\n"
    report += f"{'Average':12}: {student['average']:.1f}\n"

    return report

# Usage
alice = create_student("Alice Johnson", [])
add_grade(alice, "Math", 95)
add_grade(alice, "Science", 88)
add_grade(alice, "History", 92)

print(get_report(alice))
```

### مثال ۴: مدیر تنظیمات

```python
def create_default_config():
    """Create default application configuration."""
    return {
        "app": {
            "name": "MyApp",
            "version": "1.0.0",
            "debug": False
        },
        "database": {
            "host": "localhost",
            "port": 5432,
            "name": "myapp_db"
        },
        "features": {
            "notifications": True,
            "dark_mode": False,
            "auto_save": True
        }
    }

def get_config_value(config, path, default=None):
    """Safely get nested config value using dot notation."""
    keys = path.split(".")
    current = config

    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default

    return current

def set_config_value(config, path, value):
    """Set nested config value using dot notation."""
    keys = path.split(".")
    current = config

    for key in keys[:-1]:
        if key not in current:
            current[key] = {}
        current = current[key]

    current[keys[-1]] = value

# Usage
config = create_default_config()

# گرفتن مقادیر
app_name = get_config_value(config, "app.name")        # "MyApp"
db_port = get_config_value(config, "database.port")    # 5432
missing = get_config_value(config, "cache.enabled", False)  # False (پیش‌فرض)

# تنظیم مقادیر
set_config_value(config, "app.debug", True)
set_config_value(config, "cache.enabled", True)
```

---

## اشتباهات رایج مبتدی

### اشتباه ۱: استفاده از فهرست به‌عنوان کلید دیکشنری

```python
# اشتباه - فهرست نمی‌توانند کلید باشند (تغییرپذیرند)
my_dict = {["a", "b"]: "value"}  # TypeError!

# درست - از تاپل استفاده کنید (تغییرناپذیر)
my_dict = {("a", "b"): "value"}  # کار می‌کند!

# ولی فهرست می‌تواند مقدار باشد
my_dict = {"items": ["a", "b", "c"]}  # این اشکالی ندارد!
```

### اشتباه ۲: تغییر دیکشنری هنگام پیمایش روی آن

```python
# اشتباه - نمی‌توان اندازه را هنگام پیمایش تغییر داد
prices = {"apple": 1.00, "banana": 0.50, "cherry": 2.00}
for fruit in prices:
    if prices[fruit] < 1.00:
        del prices[fruit]  # RuntimeError!

# درست - اول فهرست کلیدها را بسازید
for fruit in list(prices.keys()):
    if prices[fruit] < 1.00:
        del prices[fruit]

# یا از dict comprehension استفاده کنید
prices = {k: v for k, v in prices.items() if v >= 1.00}
```

### اشتباه ۳: فرض کردن وجود کلید

```python
person = {"name": "Alice"}

# اشتباه - اگر کلید وجود نداشته باشد KeyError
age = person["age"]   # KeyError!

# درست - از get() استفاده کنید
age = person.get("age", 0)  # ۰ را برمی‌گرداند

# یا اول بررسی کنید
if "age" in person:
    age = person["age"]
else:
    age = 0
```

### اشتباه ۴: فهم نکردن کپی کم‌عمق

```python
original = {"data": [1, 2, 3]}

# اشتباه - هر دو به یک فهرست تودرتو اشاره دارند
copy = original.copy()
copy["data"].append(4)
print(original["data"])   # [1, 2, 3, 4] - اصل هم تغییر کرد!

# درست - برای ساختارهای تودرتو از کپی عمیق استفاده کنید
import copy
copy = copy.deepcopy(original)
```

---

## تمرین‌ها

### تمرین ۱: شمارنده کاراکتر
بشمارید هر کاراکتر چند بار در یک رشته ظاهر می‌شود.

```python
def count_characters(text):
    # کد شما اینجا
    pass

# Test
result = count_characters("hello")
# Should return: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

### تمرین ۲: مدیر موجودی انبار
توابعی برای مدیریت موجودی یک فروشگاه بسازید.

```python
def add_item(inventory, item, quantity):
    """Add quantity to item in inventory."""
    # کد شما اینجا
    pass

def remove_item(inventory, item, quantity):
    """Remove quantity from item."""
    # کد شما اینجا
    pass

def get_inventory_report(inventory):
    """Print formatted inventory report."""
    # کد شما اینجا
    pass

# Test
inv = {}
add_item(inv, "apple", 50)
add_item(inv, "banana", 30)
remove_item(inv, "apple", 10)
get_inventory_report(inv)
```

### تمرین ۳: گروه‌بندی بر اساس طول
کلمات را بر اساس طولشان گروه‌بندی کنید.

```python
def group_by_length(words):
    """Return dictionary with lengths as keys, lists of words as values."""
    # کد شما اینجا
    pass

# Test
words = ["cat", "dog", "elephant", "bird", "fish"]
result = group_by_length(words)
# Should return something like: {3: ['cat', 'dog'], 8: ['elephant'], 4: ['bird', 'fish']}
```

### تمرین ۴: ادغام دیکشنری‌ها
دو دیکشنری را ادغام کنید، به‌گونه‌ای که مقادیر dict2 اولویت داشته باشند.

```python
def merge_dicts(dict1, dict2):
    """Merge dict2 into dict1, dict2 values win conflicts."""
    # کد شما اینجا
    pass

# Test
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
result = merge_dicts(d1, d2)
# Should return: {"a": 1, "b": 3, "c": 4}
```

---

## نکات کلیدی

1. **دیکشنری جفت‌های کلید-مقدار نگه می‌دارد**: مثل یک فرهنگ لغت یا دفترچه تلفن واقعی
2. **کلیدها باید یکتا و تغییرناپذیر باشند**: رشته، عدد یا تاپل
3. **مقدارها می‌توانند هرچیزی باشند**: هر نوعی، از جمله دیکشنری دیگر
4. **برای دسترسی امن از `get()` استفاده کنید**: از KeyError برای کلیدهای ناشناخته جلوگیری می‌کند
5. **با `in` بررسی کنید**: `if "key" in dict:` پیش از دسترسی
6. **با `.items()` پیمایش کنید**: `for key, value in dict.items():`

## کارت مرجع سریع

| عملیات | چگونه | مثال |
|--------|-------|------|
| ساخت خالی | `{}` یا `dict()` | `d = {}` |
| افزودن/به‌روزرسانی | `d[key] = value` | `d["x"] = 10` |
| دسترسی | `d[key]` یا `d.get(key)` | `d["x"]` → 10 |
| دسترسی امن | `d.get(key, default)` | `d.get("y", 0)` → 0 |
| بررسی کلید | `key in d` | `"x" in d` → True |
| حذف | `d.pop(key)` | `d.pop("x")` → 10 |
| گرفتن کلیدها | `d.keys()` | همه کلیدها |
| گرفتن مقدارها | `d.values()` | همه مقدارها |
| گرفتن آیتم‌ها | `d.items()` | همه جفت‌های (کلید, مقدار) |
| ادغام | `d1 \| d2` یا `d1.update(d2)` | ترکیب دیکشنری‌ها |
| کپی | `d.copy()` | کپی کم‌عمق |
| خالی کردن | `d.clear()` | حذف همه آیتم‌ها |

---

## مطالعه بیشتر

- **درس بعدی**: مجموعه‌ها و تاپل‌ها، دیگر انواع مجموعه مفید
- **تمرین**: همه تمرین‌های بالا را کامل کنید
- **چالش**: با دیکشنری‌های تودرتو یک پایگاه داده ساده بسازید
- **کاوش کنید**: سعی کنید از `collections.defaultdict` برای مقادیر پیش‌فرض خودکار استفاده کنید