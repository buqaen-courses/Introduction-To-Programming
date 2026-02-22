# لیست‌ها در پایتون: مجموعه‌های تغییرپذیر

## آنچه خواهید آموخت
- چگونه لیست ایجاد و دستکاری کنید
- دسترسی، اضافه کردن، حذف، و تغییر آیتم‌ها
- برش و جستجو در لیست‌ها
- لیست‌تفسیری (List Comprehensions)

---

## لیست چیست؟

یک **لیست** مجموعه‌ای از آیتم‌هاست که:
- **مرتب** است (ترتیب حفظ می‌شود)
- **تغییرپذیر** است (می‌توانید تغییر دهید)
- می‌تواند **انواع مختلف** داشته باشد

```python
# لیست‌های نمونه
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, 3.14, True]
```

---

## ایجاد لیست‌ها

### لیست literals

```python
# با براکت‌ها
empty = []
fruits = ["apple", "banana", "cherry"]
```

### با تابع list()

```python
# از رشته
chars = list("hello")   # ['h', 'e', 'l', 'l', 'o']

# از محدوده
numbers = list(range(5))  # [0, 1, 2, 3, 4]

# از تاپل
items = list((1, 2, 3))   # [1, 2, 3]
```

---

## دسترسی به آیتم‌ها

### با ایندکس

```python
fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])    # apple (اولین)
print(fruits[1])    # banana
print(fruits[-1])   # date (آخرین)
print(fruits[-2])   # cherry (دوم از آخر)
```

### برش (Slicing)

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(fruits[1:3])   # ['banana', 'cherry']
print(fruits[:2])    # ['apple', 'banana']
print(fruits[2:])    # ['cherry', 'date', 'elderberry']
print(fruits[::2])   # ['apple', 'cherry', 'elderberry']
print(fruits[::-1])  # معکوس
```

---

## تغییر لیست‌ها

### اضافه کردن آیتم

```python
fruits = ["apple", "banana"]

# append - اضافه به انتها
fruits.append("cherry")   # ['apple', 'banana', 'cherry']

# insert - اضافه در موقعیت
fruits.insert(0, "apricot")  # ['apricot', 'apple', 'banana', 'cherry']

# extend - اضافه کردن چندین آیتم
fruits.extend(["date", "elderberry"])
```

### حذف آیتم

```python
fruits = ["apple", "banana", "cherry", "banana"]

# remove - حذف اولین تطابق
fruits.remove("banana")   # ['apple', 'cherry', 'banana']

# pop - حذف و برگرداندن (پیش‌فرض: آخرین)
last = fruits.pop()       # 'banana', ['apple', 'cherry']
first = fruits.pop(0)     # 'apple', ['cherry']

# del - حذف با ایندکس
del fruits[0]             # []

# clear - حذف همه
fruits.clear()            # []
```

### تغییر آیتم‌ها

```python
fruits = ["apple", "banana", "cherry"]

# تغییر یک آیتم
fruits[1] = "blueberry"   # ['apple', 'blueberry', 'cherry']

# تغییر یک برش
fruits[1:3] = ["blackberry", "boysenberry"]
```

---

## متدهای مفید

### جستجو و اطلاعات

```python
fruits = ["apple", "banana", "cherry", "banana"]

# یافتن ایندکس
print(fruits.index("banana"))   # 1 (اولین تطابق)

# شمارش تکرار
print(fruits.count("banana"))   # 2

# بررسی وجود
print("apple" in fruits)        # True
print("grape" in fruits)        # False

# طول
print(len(fruits))              # 4
```

### مرتب‌سازی

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# sort - تغییر درجا
numbers.sort()              # [1, 1, 2, 3, 4, 5, 6, 9]
numbers.sort(reverse=True)  # [9, 6, 5, 4, 3, 2, 1, 1]

# sorted - لیست جدید
new_list = sorted(numbers)  # اصلی تغییر نمی‌کند

# sort با کلید
words = ["banana", "pie", "Washington", "book"]
words.sort(key=len)         # ['pie', 'book', 'banana', 'Washington']
```

### معکوس کردن

```python
numbers = [1, 2, 3, 4, 5]

# reverse - تغییر درجا
numbers.reverse()           # [5, 4, 3, 2, 1]

# reversed - iterator جدید
for num in reversed(numbers):
    print(num)
```

---

## کپی کردن لیست‌ها

### مشکل: رفرنس به جای کپی

```python
# ❌ هر دو به یک لیست اشاره می‌کنند!
original = [1, 2, 3]
copy = original
copy.append(4)
print(original)   # [1, 2, 3, 4] - اصلی هم تغییر کرد!
```

### راه‌حل‌ها

```python
original = [1, 2, 3]

# روش 1: slice
copy1 = original[:]

# روش 2: list()
copy2 = list(original)

# روش 3: copy()
copy3 = original.copy()

# روش 4: copy عمیق (برای لیست‌های تو در تو)
import copy
deep = copy.deepcopy(nested_list)
```

---

## لیست‌تفسیری (List Comprehensions)

روش کوتاه برای ساختن لیست.

### ساختار پایه

```python
# فرم بلند
squares = []
for x in range(10):
    squares.append(x ** 2)

# فرم کوتاه (لیست‌تفسیری)
squares = [x ** 2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### با شرط

```python
# فقط اعداد زوج
evens = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# فقط کلمات طولانی
words = ["apple", "hi", "banana", "pie", "cherry"]
long_words = [w for w in words if len(w) > 4]
# ['apple', 'banana', 'cherry']
```

### تو در تو

```python
# جدول ضرب ( flatten )
pairs = [(x, y) for x in range(3) for y in range(3)]
# [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
```

---

## اشتباهات رایج

### اشتباه 1: تغییر لیست در حین حلقه‌زنی

```python
# ❌ رفتار غیرمنتظره!
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # گیج‌کننده!

# ✅ یک کپی بسازید
for num in numbers[:]:  # [:] کپی می‌سازد
    if num % 2 == 0:
        numbers.remove(num)

# یا بهتر:
numbers = [n for n in numbers if n % 2 != 0]
```

### اشتباه 2: ایندکس خارج از محدوده

```python
fruits = ["apple", "banana"]
print(fruits[5])   # IndexError!

# بررسی کنید
if len(fruits) > 5:
    print(fruits[5])
```

---

## مرجع سریع

| عملیات | کد | توضیح |
|--------|-----|-------|
| ایجاد | `[]` یا `list()` | لیست خالی |
| دسترسی | `list[i]` | آیتم در ایندکس i |
| برش | `list[i:j]` | آیتم‌ها از i تا j-1 |
| اضافه | `list.append(x)` | به انتها |
| درج | `list.insert(i, x)` | در ایندکس i |
| حذف | `list.remove(x)` | اولین x |
| pop | `list.pop(i)` | حذف و برگرداندن |
| جستجو | `x in list` | بررسی وجود |
| مرتب‌سازی | `list.sort()` | تغییر درجا |
| معکوس | `list.reverse()` | تغییر درجا |
| طول | `len(list)` | تعداد آیتم‌ها |

---

## نکات کلیدی

1. **لیست‌ها تغییرپذیر و مرتب هستند** - از تاپل‌ها و مجموعه‌ها متمایزند
2. **ایندکس از 0 شروع می‌شود** - و منفی از انتها می‌آید
3. **برش یک لیست جدید می‌دهد** - اصلی را تغییر نمی‌دهد
4. **تغییر در حین حلقه با احتیاط** - یا کپی بسازید یا لیست‌تفسیری استفاده کنید
5. **لیست‌تفسیری قدرتمند است** - `[x for x in items if condition]`
6. **کپی صحیح بسازید** - `[:]`، `list()`، یا `.copy()`

---

## قدم بعدی چیست؟

اکنون می‌توانید با لیست‌ها کار کنید! بعدی، ما یاد می‌گیریم:
- دیکشنری‌ها - ذخیره‌سازی key-value
- مجموعه‌ها و تاپل‌ها
- ساختارهای داده پیشرفته
