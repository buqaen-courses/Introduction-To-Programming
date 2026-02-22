# دیکشنری‌ها در پایتون: ذخیره‌سازی key-value

## آنچه خواهید آموخت
- چگونه دیکشنری ایجاد و استفاده کنید
- دسترسی، اضافه کردن، و حذف آیتم‌ها
- متدها و عملیات دیکشنری
- دیکشنری‌تفسیری

---

## دیکشنری چیست؟

یک **دیکشنری** مجموعه‌ای از جفت‌های **key-value** است:
- **کلیدها (Keys)** منحصر به فرد و تغییرناپذیر هستند
- **مقدارها (Values)** می‌توانند هر چیزی باشند
- **مرتب** (Python 3.7+) - ترتیب درج حفظ می‌شود
- **تغییرپذیر** - می‌توانید اضافه، حذف، و تغییر دهید

```python
# دیکشنری نمونه
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "CS", "Physics"]
}
```

---

## ایجاد دیکشنری‌ها

### با آکولادها

```python
# خالی
empty = {}

# با آیتم‌ها
person = {
    "name": "Bob",
    "age": 30,
    "city": "New York"
}
```

### با تابع dict()

```python
# از آرگومان‌های کلیدواژه
person = dict(name="Bob", age=30, city="New York")

# از لیست تاپل‌ها
person = dict([("name", "Bob"), ("age", 30), ("city", "New York")])

# با zip
keys = ["name", "age", "city"]
values = ["Bob", 30, "New York"]
person = dict(zip(keys, values))
```

---

## دسترسی به آیتم‌ها

### با کلید

```python
student = {"name": "Alice", "age": 20, "grade": "A"}

# با براکت‌ها
print(student["name"])   # Alice
print(student["age"])    # 20

# ⚠️ اگر کلید وجود نداشته باشد، خطا می‌دهد!
# print(student["gpa"])   # KeyError!
```

### با get() (امن‌تر)

```python
# get - بدون خطا اگر وجود نداشته باشد
print(student.get("name"))    # Alice
print(student.get("gpa"))     # None
print(student.get("gpa", 0))   # 0 (پیش‌فرض)
```

### بررسی وجود کلید

```python
if "name" in student:
    print(f"Name: {student['name']}")

if "gpa" not in student:
    print("GPA not recorded")
```

---

## تغییر دیکشنری‌ها

### اضافه یا تغییر آیتم

```python
student = {"name": "Alice", "age": 20}

# اضافه کردن جدید
student["grade"] = "A"          # {'name': 'Alice', 'age': 20, 'grade': 'A'}

# تغییر موجود
student["age"] = 21             # {'name': 'Alice', 'age': 21, 'grade': 'A'}

# update - چندین آیتم
student.update({"gpa": 3.8, "major": "CS"})
```

### حذف آیتم

```python
student = {"name": "Alice", "age": 20, "grade": "A"}

# pop - حذف و برگرداندن
age = student.pop("age")        # 20, student اکنون {'name': 'Alice', 'grade': 'A'}

# popitem - حذف و برگرداندن آخرین (LIFO)
last = student.popitem()        # ('grade', 'A')

# del - حذف
student = {"name": "Alice", "age": 20}
del student["age"]              # {'name': 'Alice'}

# clear - حذف همه
student.clear()                 # {}
```

---

## متدها و ویژگی‌ها

### دسترسی به کلیدها، مقادیر، و آیتم‌ها

```python
student = {"name": "Alice", "age": 20, "grade": "A"}

# کلیدها
print(student.keys())      # dict_keys(['name', 'age', 'grade'])

# مقادیر
print(student.values())    # dict_values(['Alice', 20, 'A'])

# آیتم‌ها (key-value pairs)
print(student.items())     # dict_items([('name', 'Alice'), ('age', 20), ('grade', 'A')])

# می‌توان به عنوان لیست تبدیل کرد
print(list(student.keys()))   # ['name', 'age', 'grade']
```

### ست کردن پیش‌فرض

```python
# setdefault - اگر وجود ندارد، مقدار پیش‌فرض را ست می‌کند
counts = {}
counts.setdefault("apple", 0)   # 0 را برمی‌گرداند و ست می‌کند
counts["apple"] += 1

# یا با defaultdict (از collections)
from collections import defaultdict
counts = defaultdict(int)  # 0 برای int
counts["apple"] += 1       # بدون خطا، 0 + 1 = 1
```

---

## حلقه‌زنی روی دیکشنری‌ها

### روی کلیدها (پیش‌فرض)

```python
student = {"name": "Alice", "age": 20, "grade": "A"}

for key in student:
    print(f"{key}: {student[key]}")
```

### روی مقادیر

```python
for value in student.values():
    print(value)
```

### روی آیتم‌ها

```python
for key, value in student.items():
    print(f"{key} = {value}")

# خروجی:
# name = Alice
# age = 20
# grade = A
```

---

## دیکشنری‌های تو در تو

```python
# دیکشنری‌های پیچیده
school = {
    "name": "High School",
    "students": {
        "Alice": {"age": 20, "grade": "A"},
        "Bob": {"age": 21, "grade": "B"}
    },
    "teachers": ["Mr. Smith", "Ms. Johnson"]
}

# دسترسی
print(school["students"]["Alice"]["grade"])  # A

# اضافه کردن
school["students"]["Charlie"] = {"age": 19, "grade": "A"}
```

---

## ادغام دیکشنری‌ها

### با update()

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

dict1.update(dict2)   # {'a': 1, 'b': 3, 'c': 4}
```

### با | (Python 3.9+)

```python
# | - ادغام و برگرداندن دیکشنری جدید
combined = dict1 | dict2   # {'a': 1, 'b': 3, 'c': 4}

# |= - ادغام درجا
dict1 |= dict2   # dict1 اکنون {'a': 1, 'b': 3, 'c': 4}
```

---

## دیکشنری‌تفسیری

### ساختار پایه

```python
# فرم بلند
squares = {}
for x in range(6):
    squares[x] = x ** 2

# فرم کوتاه
doubled = {x: x * 2 for x in range(6)}
# {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
```

### با شرط

```python
# فقط اعداد زوج
evens = {x: x ** 2 for x in range(10) if x % 2 == 0}
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

---

## کپی کردن دیکشنری‌ها

### کپی سطحی

```python
original = {"a": 1, "b": [2, 3]}

# کپی سطحی - لیست داخلی اشتراکی است!
copy1 = original.copy()
copy2 = dict(original)
copy3 = {**original}

original["b"].append(4)
print(copy1["b"])   # [2, 3, 4] - تغییر کرد!
```

### کپی عمیق

```python
import copy

deep = copy.deepcopy(original)
original["b"].append(5)
print(deep["b"])    # [2, 3, 4] - تغییر نکرد!
```

---

## اشتباهات رایج

### اشتباه 1: استفاده از کلید تغییرپذیر

```python
# ❌ لیست نمی‌تواند کلید باشد!
bad = {[1, 2]: "value"}   # TypeError!

# ✅ تاپل می‌تواند (اگر تغییرناپذیر باشد)
good = {(1, 2): "value"}   # کار می‌کند
```

### اشتباه 2: فراموش کردن get()

```python
# ❌ خطا اگر کلید وجود نداشته باشد
value = my_dict["missing_key"]   # KeyError!

# ✅ با get ایمن است
value = my_dict.get("missing_key", "default")
```

### اشتباه 3: فرض تغییر در حین حلقه‌زنی

```python
# ⚠️ با احتیاط - اندازه در حال تغییر است
for key in my_dict:
    if condition:
        del my_dict[key]   # RuntimeError!

# ✅ یک لیست از کلیدها بسازید
for key in list(my_dict.keys()):
    if condition:
        del my_dict[key]
```

---

## مرجع سریع

| عملیات | کد | توضیح |
|--------|-----|-------|
| ایجاد | `{}` یا `dict()` | دیکشنری خالی |
| دسترسی | `d[key]` | مقدار با کلید |
| get | `d.get(key, default)` | ایمن‌تر |
| اضافه/تغییر | `d[key] = value` | درج یا به‌روزرسانی |
| حذف | `d.pop(key)` | حذف و برگرداندن |
| کلیدها | `d.keys()` | تمام کلیدها |
| مقادیر | `d.values()` | تمام مقادیر |
| آیتم‌ها | `d.items()` | جفت‌های key-value |
| بررسی | `key in d` | وجود کلید |
| update | `d.update(other)` | ادغام دیکشنری‌ها |

---

## نکات کلیدی

1. **دیکشنری‌ها key-value هستند** - کلیدها منحصر به فرد و تغییرناپذیر
2. **از get() برای ایمنی استفاده کنید** - خطا نمی‌دهد
3. **کلیدها باید تغییرناپذیر باشند** - str، int، tuple (نه list)
4. **items() برای حلقه‌زنی** - هم کلید و مقدار
5. **کپی عمیق برای تو در تو** - copy.deepcopy()
6. **دیکشنری‌تفسیری قدرتمند است** - `{k: v for k, v in items}`

---

## قدم بعدی چیست؟

اکنون می‌توانید با دیکشنری‌ها کار کنید! بعدی، ما یاد می‌گیریم:
- مجموعه‌ها و تاپل‌ها
- تفاوت بین انواع داده
- انتخاب ساختار داده مناسب
