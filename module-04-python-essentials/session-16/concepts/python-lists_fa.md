# فهرست‌های پایتون: نخستین ساختار داده شما

## فهرست چیست؟

**فهرست** مثل فهرست خرید یا فهرست کار است: مجموعه‌ای مرتب از آیتم‌ها که می‌توانید به آن اضافه کنید، از آن حذف کنید و تغییرش دهید. برخلاف رشته‌ها، فهرست‌ها می‌توانند هر نوع داده‌ای را نگه دارند و **می‌توانید** تغییرشان دهید!

```python
# فهرست‌ها می‌توانند هر نوع داده‌ای را نگه دارند
fruits = ["apple", "banana", "cherry"]          # رشته‌ها
numbers = [1, 2, 3, 4, 5]                        # اعداد
mixed = [1, "hello", 3.14, True]                 # انواع مخلوط
empty = []                                        # فهرست خالی
```

### چرا فهرست‌ها مهم‌اند

فهرست یکی از پرکاربردترین ابزارهای پایتون است:
- نگه‌داری مجموعه‌ای از داده‌های مرتبط
- حفظ ترتیب آیتم‌ها
- اضافه یا حذف آسان
- پردازش چند آیتم با حلقه
- ساخت ساختارهای داده پیچیده‌تر

---

## ساخت فهرست

### ساخت پایه

```python
# فهرست خالی
shopping_list = []
shopping_list = list()   # جایگزین

# فهرست با آیتم
colors = ["red", "green", "blue"]

# فهرست از یک بازه
numbers = list(range(1, 6))
# Result: [1, 2, 3, 4, 5]

# فهرست از یک رشته
letters = list("Hello")
# Result: ['H', 'e', 'l', 'l', 'o']

# فهرست از آیتم‌های تکراری
zeros = [0] * 5
# Result: [0, 0, 0, 0, 0]
```

### فهرست از فهرست (فهرست تودرتو)

```python
# یک فهرست می‌تواند شامل فهرست‌های دیگر هم باشد!
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# دسترسی به آیتم‌های تودرتو
first_row = matrix[0]        # [1, 2, 3]
center = matrix[1][1]        # 5 (ردیف دوم، ستون دوم)
```

---

## دسترسی به عناصر فهرست

### با اندیس (موقعیت)

درست مثل رشته‌ها، اندیس فهرست از صفر شروع می‌شود:

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# دسترسی بر اساس موقعیت
first = fruits[0]          # "apple"
second = fruits[1]         # "banana"
last = fruits[4]           # "elderberry"

# اندیس منفی (از انتها)
last = fruits[-1]          # "elderberry"
second_to_last = fruits[-2]  # "date"

# چند آیتم داریم؟
count = len(fruits)        # 5
```

**نمایش بصری:**
```
Index:    0        1         2        3          4
         ↓        ↓         ↓        ↓          ↓
List: ["apple", "banana", "cherry", "date", "elderberry"]
         ↑                 ↑                    ↑
       fruits[0]        fruits[2]          fruits[-1]
```

### اشتباه رایج مبتدی

```python
fruits = ["apple", "banana", "cherry"]

# اشتباه - اندیس ۳ وجود ندارد (فقط ۰، ۱، ۲ هست)
last = fruits[3]   # IndexError!

# درست
last = fruits[2]      # "cherry"
last = fruits[-1]     # "cherry" (امن‌تر!)
last = fruits[len(fruits) - 1]  # "cherry" (صریح)
```

---

## برش فهرست

### گرفتن زیرمجموعه

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# برش پایه: list[start:end] (پایان شامل نمی‌شود!)
subset = numbers[2:5]      # [2, 3, 4] (اندیس‌های ۲، ۳، ۴)

# از ابتدا
beginning = numbers[:4]     # [0, 1, 2, 3]

# تا انتها
ending = numbers[6:]        # [6, 7, 8, 9]

# هر N آیتم یکی
every_second = numbers[::2]    # [0, 2, 4, 6, 8]
every_third = numbers[::3]     # [0, 3, 6, 9]

# معکوس
to_back = numbers[::-1]        # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

### نمونه‌های برش

```python
# گرفتن N آیتم آخر
tasks = ["email", "meeting", "lunch", "coding", "review"]
last_three = tasks[-3:]         # ["lunch", "coding", "review"]

# رد کردن اول و آخر
grades = [65, 70, 85, 90, 95]
middle = grades[1:-1]           # [70, 85, 90]

# کپی کردن کل فهرست
copy = numbers[:]               # مثل list(numbers) یا numbers.copy()
```

---

## تغییر فهرست‌ها (فهرست تغییرپذیر است!)

برخلاف رشته‌ها، شما **می‌توانید** فهرست‌ها را درجا تغییر دهید!

### تغییر آیتم‌ها

```python
fruits = ["apple", "banana", "cherry"]

# تغییر یک آیتم
fruits[1] = "blueberry"
# Result: ["apple", "blueberry", "cherry"]

# تغییر یک برش
fruits[1:3] = ["blackberry", "cranberry"]
# Result: ["apple", "blackberry", "cranberry"]

# جایگزینی با تعداد آیتم متفاوت
fruits[1:2] = ["kiwi", "mango"]
# Result: ["apple", "kiwi", "mango", "cranberry"]
```

### اضافه کردن آیتم‌ها

```python
fruits = ["apple", "banana"]

# اضافه کردن به انتها (رایج‌ترین)
fruits.append("cherry")
# Result: ["apple", "banana", "cherry"]

# درج در موقعیت مشخص
fruits.insert(1, "avocado")
# Result: ["apple", "avocado", "banana", "cherry"]

# اضافه کردن چند آیتم از فهرست دیگر
fruits.extend(["date", "elderberry"])
# Result: ["apple", "avocado", "banana", "cherry", "date", "elderberry"]

# می‌توانید از + هم برای ترکیب فهرست‌ها استفاده کنید (فهرست تازه می‌سازد)
more_fruits = fruits + ["fig", "grape"]
```

### حذف آیتم‌ها

```python
fruits = ["apple", "banana", "cherry", "banana"]

# حذف بر اساس مقدار (فقط اولین مورد!)
fruits.remove("banana")
# Result: ["apple", "cherry", "banana"]

# حذف بر اساس اندیس
del fruits[0]
# Result: ["cherry", "banana"]

# حذف و بازگرداندن آخرین آیتم
last = fruits.pop()
# last = "banana", fruits = ["cherry"]

# حذف و بازگرداندن اندیس مشخص
first = fruits.pop(0)
# Removes and returns the first item

# خالی کردن کل فهرست
fruits.clear()
# Result: []
```

**مهم**: `remove()` فقط اولین تطبیقی را که پیدا کند حذف می‌کند!

```python
# برای حذف همه موارد یک مقدار
numbers = [1, 2, 3, 2, 4, 2, 5]
while 2 in numbers:
    numbers.remove(2)
# Result: [1, 3, 4, 5]
```

---

## متدهای مفید فهرست

### پیدا کردن و شمردن

```python
numbers = [1, 2, 3, 2, 4, 2, 5]

# پیدا کردن موقعیت (اندیس یا خطا برمی‌گرداند)
position = numbers.index(3)       # 2

# پیدا کردن از موقعیت ۳ به بعد
position = numbers.index(2, 3)    # 5 (دومین ۲ در اندیس ۳)

# شمردن تکرارها
count = numbers.count(2)          # 3 (۳ بار آمده)

# بررسی حضور (True/False)
has_three = 3 in numbers          # True
has_ten = 10 in numbers           # False
```

### مرتب‌سازی

```python
scores = [85, 92, 78, 96, 88, 91]

# مرتب‌سازی درجا (فهرست اصلی را تغییر می‌دهد)
scores.sort()
# Result: [78, 85, 88, 91, 92, 96]

# مرتب‌سازی نزولی
scores.sort(reverse=True)
# Result: [96, 92, 91, 88, 85, 78]

# ساخت کپی مرتب‌شده (اصلی تغییر نمی‌کند)
original = [3, 1, 4, 1, 5]
sorted_copy = sorted(original)
# original: [3, 1, 4, 1, 5]
# sorted_copy: [1, 1, 3, 4, 5]

# مرتب‌سازی رشته‌ها (پیش‌فرض حساس به بزرگی و کوچکی حروف)
names = ["alice", "Bob", "ALICE", "bob"]
names.sort()
# Result: ["ALICE", "Bob", "alice", "bob"] (حروف بزرگ اول!)

# مرتب‌سازی بدون حساسیت به بزرگی و کوچکی حروف
names.sort(key=str.lower)
# Result: ["alice", "ALICE", "Bob", "bob"]
```

### معکوس کردن

```python
numbers = [1, 2, 3, 4, 5]

# معکوس درجا
numbers.reverse()
# Result: [5, 4, 3, 2, 1]

# ساخت کپی معکوس
original = [1, 2, 3, 4, 5]
reversed_copy = list(reversed(original))
# original: [1, 2, 3, 4, 5]
# reversed_copy: [5, 4, 3, 2, 1]
```

### کپی کردن فهرست

```python
original = [1, 2, [3, 4]]

# کپی کم‌عمق (آیتم‌های تودرتو مشترک‌اند)
copy1 = original.copy()
copy2 = list(original)
copy3 = original[:]

# تغییر کپی - فهرست تودرتوی اصلی هم تغییر می‌کند!
copy1[2][0] = 999
# original becomes: [1, 2, [999, 4]]

# کپی عمیق (کاملاً مستقل)
import copy
deep = copy.deepcopy(original)
deep[2][0] = 777
# original stays: [1, 2, [999, 4]]
```

---

## عملیات فهرست با حلقه

### پیمایش پایه

```python
fruits = ["apple", "banana", "cherry"]

# پیمایش روی آیتم‌ها
for fruit in fruits:
    print(f"I like {fruit}")

# Output:
# I like apple
# I like banana
# I like cherry
```

### حلقه با اندیس

```python
grades = [85, 92, 78, 96]

# استفاده از enumerate
for index, grade in enumerate(grades):
    print(f"Student {index + 1}: {grade}")

# Output:
# Student 1: 85
# Student 2: 92
# Student 3: 78
# Student 4: 96
```

### ساخت یک فهرست

```python
# از خالی شروع کنید، آیتم اضافه کنید
squares = []
for number in range(1, 6):
    squares.append(number ** 2)
# Result: [1, 4, 9, 16, 25]

# list comprehension (راه کوتاه‌تر!)
squares = [x ** 2 for x in range(1, 6)]
```

### فیلتر کردن یک فهرست

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# فقط اعداد زوج
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
# Result: [2, 4, 6, 8, 10]

# list comprehension (پایتونی‌تر!)
evens = [num for num in numbers if num % 2 == 0]
```

---

## List Comprehension (روش پایتونی)

List comprehension روشی فشرده برای ساخت فهرست است.

### نحو پایه

```python
# روش معمولی
squares = []
for x in range(1, 6):
    squares.append(x ** 2)

# روش list comprehension
squares = [x ** 2 for x in range(1, 6)]
# Result: [1, 4, 9, 16, 25]
```

### با شرط

```python
numbers = range(1, 21)

# فقط اعداد زوج
evens = [x for x in numbers if x % 2 == 0]
# Result: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# فقط مربع اعداد فرد
odd_squares = [x ** 2 for x in numbers if x % 2 == 1]
# Result: [1, 9, 25, 49, 81, 121, 169, 225, 289, 361]
```

### تبدیل داده

```python
names = ["alice", "bob", "charlie"]

# بزرگ کردن حرف اول همه نام‌ها
capitalized = [name.title() for name in names]
# Result: ["Alice", "Bob", "Charlie"]

# گرفتن طول‌ها
lengths = [len(name) for name in names]
# Result: [5, 3, 7]
```

---

## مثال‌های کاربردی

### مثال ۱: مدیریت فهرست خرید

```python
def shopping_list_app():
    shopping = []

    while True:
        print("\nShopping List:")
        for i, item in enumerate(shopping, 1):
            print(f"{i}. {item}")

        print("\nOptions: (a)dd, (r)emove, (q)uit")
        choice = input("Choice: ").lower()

        if choice == 'a':
            item = input("What to add: ")
            shopping.append(item)
            print(f"Added: {item}")

        elif choice == 'r':
            if shopping:
                item = shopping.pop()
                print(f"Removed: {item}")
            else:
                print("List is empty!")

        elif choice == 'q':
            print("Goodbye!")
            break

# Uncomment to run:
# shopping_list_app()
```

### مثال ۲: محاسبه‌گر نمرات

```python
def calculate_statistics(grades):
    """Calculate grade statistics."""
    if not grades:
        return None

    total = sum(grades)
    count = len(grades)
    average = total / count
    highest = max(grades)
    lowest = min(grades)

    return {
        "count": count,
        "total": total,
        "average": round(average, 2),
        "highest": highest,
        "lowest": lowest
    }

# Usage
grades = [85, 92, 78, 96, 88, 91]
stats = calculate_statistics(grades)

print(f"Grades: {grades}")
print(f"Count: {stats['count']}")
print(f"Average: {stats['average']}")
print(f"Highest: {stats['highest']}")
print(f"Lowest: {stats['lowest']}")
```

### مثال ۳: حذف تکراری‌ها

```python
def remove_duplicates(items):
    """Remove duplicates while preserving order."""
    seen = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return seen

# Usage
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = remove_duplicates(numbers)
print(unique)  # [1, 2, 3, 4]

# جایگزین با set (سریع‌تر، ولی ترتیب را از دست می‌دهد)
unique_fast = list(set(numbers))
```

### مثال ۴: پیدا کردن عناصر مشترک

```python
def find_common(list1, list2):
    """Find items present in both lists."""
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common

# Usage
class_a = ["Alice", "Bob", "Charlie", "Diana"]
class_b = ["Bob", "Diana", "Eve", "Frank"]

both = find_common(class_a, class_b)
print(f"In both classes: {both}")  # ['Bob', 'Diana']
```

---

## اشتباهات رایج مبتدی

### اشتباه ۱: تغییر فهرست هنگام پیمایش روی آن

```python
# اشتباه - آیتم‌ها جا می‌افتند!
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # خطرناک!

# درست - فهرست تازه بسازید
evens = [num for num in numbers if num % 2 == 0]

# یا روی یک کپی پیمایش کنید
for num in numbers[:]:
    if num % 2 == 0:
        numbers.remove(num)
```

### اشتباه ۲: ساخت چند ارجاع

```python
# اشتباه - هر دو به یک فهرست اشاره می‌کنند!
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1)  # [1, 2, 3, 4] - list1 هم تغییر کرد!

# درست - یک کپی بسازید
list1 = [1, 2, 3]
list2 = list1.copy()  # یا list1[:]
list2.append(4)
print(list1)  # [1, 2, 3] - بدون تغییر!
```

### اشتباه ۳: استفاده از `=` به‌جای `append()`

```python
# اشتباه
my_list = []
my_list = 5   # فهرست را با عدد ۵ جایگزین می‌کند!

# درست
my_list = []
my_list.append(5)   # فهرست الان [5] است
```

### اشتباه ۴: اندیس خارج از محدوده در حلقه

```python
fruits = ["apple", "banana", "cherry"]

# اشتباه
for i in range(5):  # تلاش برای دسترسی به fruits[3] و fruits[4]!
    print(fruits[i])

# درست
for i in range(len(fruits)):
    print(fruits[i])

# بهتر - مستقیم پیمایش کنید
for fruit in fruits:
    print(fruit)
```

---

## تمرین‌ها

### تمرین ۱: معکوس کردن فهرست
تابعی بنویسید که یک فهرست را بدون استفاده از متد `reverse()` معکوس کند.

```python
def reverse_list(items):
    # کد شما اینجا
    pass

# Test
print(reverse_list([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]
```

### تمرین ۲: پیدا کردن بیشینه
تابعی بنویسید که بیشترین مقدار یک فهرست را پیدا کند (بدون استفاده از `max()`).

```python
def find_maximum(numbers):
    # کد شما اینجا
    pass

# Test
print(find_maximum([3, 7, 2, 9, 1]))  # 9
```

### تمرین ۳: صاف کردن فهرست
تابعی بنویسید که فهرستی از فهرست‌ها را به یک فهرست تک تبدیل کند.

```python
def flatten(nested):
    # کد شما اینجا
    pass

# Test
print(flatten([[1, 2], [3, 4], [5, 6]]))  # [1, 2, 3, 4, 5, 6]
```

### تمرین ۴: چرخاندن فهرست
تابعی بنویسید که یک فهرست را N جایگاه بچرخاند.

```python
def rotate_list(items, n):
    # کد شما اینجا
    pass

# Test
print(rotate_list([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]
```

---

## نکات کلیدی

1. **فهرست‌ها مجموعه‌های مرتب‌اند**: آیتم‌ها به همان ترتیبی می‌مانند که اضافه می‌کنید
2. **فهرست‌ها تغییرپذیرند**: می‌توانید آیتم‌ها را تغییر، اضافه یا حذف کنید
3. **اندیس از صفر شروع می‌شود**: اولین آیتم در موقعیت ۰ است
4. **برش فهرست تازه می‌سازد**: `list[1:3]` یک کپی به شما می‌دهد
5. **از متدهای فهرست استفاده کنید** مثل `append()`، `sort()`، `reverse()`
6. **List comprehension** فشرده و پایتونی است: `[x**2 for x in range(5)]`

## کارت مرجع سریع

| عملیات | چگونه | مثال |
|---------|-------|------|
| ساخت فهرست خالی | `[]` یا `list()` | `my_list = []` |
| اضافه به انتها | `append(item)` | `list.append(5)` |
| درج در موقعیت | `insert(pos, item)` | `list.insert(0, 'first')` |
| حذف بر اساس مقدار | `remove(item)` | `list.remove('a')` |
| حذف بر اساس اندیس | `pop(index)` | `list.pop(0)` |
| گرفتن طول | `len(list)` | `len([1,2,3])` → 3 |
| مرتب‌سازی درجا | `sort()` | `list.sort()` |
| ساخت کپی مرتب‌شده | `sorted(list)` | `new = sorted(list)` |
| معکوس درجا | `reverse()` | `list.reverse()` |
| بررسی حضور | `item in list` | `3 in [1,2,3]` → True |
| پیدا کردن اندیس | `index(item)` | `[1,2,3].index(2)` → 1 |
| شمردن آیتم | `count(item)` | `[1,1,1].count(1)` → 3 |
| کپی فهرست | `copy()` یا `[:]` | `new = old.copy()` |
| خالی کردن همه | `clear()` | `list.clear()` |

---

## مطالعه بیشتر

- **درس بعدی**: دیکشنری‌های پایتون، جفت‌های کلید-مقدار برای جست‌وجوی کارآمد
- **تمرین**: همه تمرین‌های بالا را کامل کنید
- **چالش**: برنامه‌ای برای فهرست کارها با اولویت و مهلت بسازید
- **کاوش کنید**: سعی کنید با فهرست‌ها یک شبکه دوبعدی (مثل صفحه شطرنج) را نمایش دهید