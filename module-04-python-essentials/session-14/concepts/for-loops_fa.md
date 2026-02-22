# حلقه‌های for در پایتون

## آنچه خواهید آموخت
- چگونه کد را بارها و بارها اجرا کنید
- نحوه کار با مجموعه‌ای از داده‌ها
- روش‌های مختلف استفاده از حلقه for

---

## حلقه‌ها چه هستند؟

**حلقه** راهی برای اجرای کد چندین بار است. به جای نوشتن کد تکراری، از حلقه استفاده می‌کنید.

### تشبیه: کار تکراری

```
❌ بدون حلقه (خسته‌کننده):
    چاپ "سلام"
    چاپ "سلام"
    چاپ "سلام"
    ... (۱۰۰ بار)

✅ با حلقه:
    تکرار ۱۰۰ بار:
        چاپ "سلام"
```

در برنامه‌نویسی:
- نمایش همه آیتم‌ها در یک لیست
- پردازش هر خط در یک فایل
- تلاش تا موفقیت
- انجام محاسبات روی یک بازه

---

## حلقه for پایه

### نحو

```python
for variable in sequence:
    # کدی که برای هر item اجرا می‌شود
    # (با تورفتگی!)
```

### مثال ساده

```python
# چاپ اعداد ۱ تا ۵
for number in [1, 2, 3, 4, 5]:
    print(number)

# خروجی:
# 1
# 2
# 3
# 4
# 5
```

### حلقه روی رشته

```python
# هر حرف را چاپ کن
for letter in "Hello":
    print(letter)

# خروجی:
# H
# e
# l
# l
# o
```

### حلقه روی لیست

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}")

# خروجی:
# I like apple
# I like banana
# I like cherry
```

---

## تابع range()

### range پایه

```python
# اعداد ۰ تا ۴ (نه ۵!)
for i in range(5):
    print(i)

# خروجی:
# 0
# 1
# 2
# 3
# 4
```

### range با شروع و پایان

```python
# اعداد ۵ تا ۹
for i in range(5, 10):
    print(i)

# خروجی: 5, 6, 7, 8, 9
```

### range با گام

```python
# اعداد زوج ۰ تا ۸
for i in range(0, 10, 2):
    print(i)

# خروجی: 0, 2, 4, 6, 8

# اعداد ۱۰ تا ۱ (برعکس)
for i in range(10, 0, -1):
    print(i)

# خروجی: 10, 9, 8, ..., 1
```

### خلاصه range

| دستور | نتیجه |
|---------|--------|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(2, 5)` | 2, 3, 4 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 |
| `range(5, 0, -1)` | 5, 4, 3, 2, 1 |

---

## الگوهای رایج

### شمارش

```python
# چاپ اعداد ۱ تا ۱۰
for i in range(1, 11):
    print(i)
```

### شمارش با گام

```python
# شمارش ۵ تا ۵۰، هر ۵ تا
for i in range(5, 51, 5):
    print(i)

# خروجی: 5, 10, 15, ..., 50
```

### حلقه روی لیست با اندیس

```python
fruits = ["apple", "banana", "cherry"]

# با enumerate
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# خروجی:
# 0: apple
# 1: banana
# 2: cherry

# شروع از ۱
for index, fruit in enumerate(fruits, 1):
    print(f"{index}. {fruit}")

# خروجی:
# 1. apple
# 2. banana
# 3. cherry
```

### حلقه روی دیکشنری

```python
person = {"name": "Alice", "age": 25, "city": "NYC"}

# فقط کلیدها
for key in person:
    print(key)

# کلید و مقدار
for key, value in person.items():
    print(f"{key}: {value}")

# خروجی:
# name: Alice
# age: 25
# city: NYC
```

---

## حلقه‌های تو در تو

### حلقه درون حلقه

```python
# جدول ضرب
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("---")

# خروجی:
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# ---
# 2 x 1 = 2
# ...
```

### الگوها با حلقه‌های تو در تو

```python
# مثلث
for i in range(1, 6):
    print("*" * i)

# خروجی:
# *
# **
# ***
# ****
# *****

# مربع
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()

# خروجی:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
```

---

## کار با چندین لیست

### zip

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# خروجی:
# Alice is 25 years old
# Bob is 30 years old
# Charlie is 35 years old
```

### zip با سه لیست

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, from {city}")
```

---

## کاربردهای عملی

### مثال ۱: جمع اعداد

```python
# جمع اعداد ۱ تا ۱۰۰
total = 0
for i in range(1, 101):
    total = total + i

print(f"Sum: {total}")   # 5050

# یا با sum() (راه بهتر)
total = sum(range(1, 101))
print(f"Sum: {total}")
```

### مثال ۲: یافتن بزرگ‌ترین عدد

```python
numbers = [23, 56, 12, 89, 34, 67]

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print(f"Largest: {largest}")  # 89

# یا با max() (راه بهتر)
print(f"Largest: {max(numbers)}")
```

### مثال ۳: فیلتر کردن

```python
# اعداد زوج را پیدا کن
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)      # [2, 4, 6, 8, 10]
```

### مثال ۴: پردازش لیست خرید

```python
cart = [
    {"item": "Apple", "price": 1.50, "qty": 3},
    {"item": "Banana", "price": 0.75, "qty": 6},
    {"item": "Cherry", "price": 2.00, "qty": 2}
]

total = 0
for product in cart:
    subtotal = product["price"] * product["qty"]
    total = total + subtotal
    print(f"{product['item']}: ${subtotal:.2f}")

print(f"Total: ${total:.2f}")

# خروجی:
# Apple: $4.50
# Banana: $4.50
# Cherry: $4.00
# Total: $13.00
```

---

## اشتباهات رایج

### اشتباه ۱: تغییر لیست در حین حلقه

```python
# ⚠️ خطرناک
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # مشکل‌ساز!

print(numbers)  # نتیجه غیرمنتظره: [1, 3, 5] یا [1, 3, 4]?

# ✅ صحیح - کپی بسازید
numbers = [1, 2, 3, 4, 5]
for num in numbers[:]:  # کپی با [:]
    if num % 2 == 0:
        numbers.remove(num)

print(numbers)  # [1, 3, 5]

# ✅ یا از list comprehension استفاده کنید
numbers = [num for num in numbers if num % 2 != 0]
```

### اشتباه ۲: فراموش کردن تورفتگی

```python
# ❌ اشتباه
for i in range(5):
print(i)                # IndentationError!

# ✅ صحیح
for i in range(5):
    print(i)
```

### اشتباه ۳: اصلاح متغیر حلقه

```python
# ⚠️ کار می‌کند اما گیج‌کننده است
for i in range(5):
    print(i)            # 0, 1, 2, 3, 4
    i = i + 10        # این i را در حلقه تغییر نمی‌دهد!

# i در حلقه هنوز 0, 1, 2, 3, 4 است
```

### اشتباه ۴: range با اعداد float

```python
# ❌ خطا
for i in range(0, 1, 0.1):  # TypeError!

# ✅ از numpy یا حلقه while استفاده کنید
import numpy as np
for i in np.arange(0, 1, 0.1):
    print(i)
```

### اشتباه ۵: فراموش کردن تبدیل ورودی

```python
# ❌ اشتباه
numbers = input("Enter numbers: ")  # "1 2 3 4 5"
total = 0
for num in numbers:  # این روی کاراکترها حلقه می‌زند!
    total = total + num

# ✅ صحیح
numbers = input("Enter numbers: ").split()
total = 0
for num in numbers:
    total = total + int(num)
```

---

## خودتان امتحان کنید: تمرین‌ها

### تمرین ۱: جدول ضرب

کدی بنویسید که جدول ضرب ۱ تا ۱۰ را چاپ کند:

```
1 x 1 = 1   1 x 2 = 2   ...   1 x 10 = 10
2 x 1 = 2   2 x 2 = 4   ...   2 x 10 = 20
...
10 x 1 = 10  10 x 2 = 20  ...  10 x 10 = 100
```

### تمرین ۲: یافتن اعداد اول

کدی بنویسید که همه اعداد اول تا ۱۰۰ را پیدا و چاپ کند.

**راهنمایی:** عدد اول فقط بر ۱ و خودش بخش‌پذیر است.

### تمرین ۳: ماشین حساب میانگین

کدی بنویسید که:
۱. از کاربر ۵ نمره بگیرد
۲. میانگین را محاسبه کند
۳. نتیجه را با یک رقم اعشار نمایش دهد

### تمرین ۴: الگوی مثلث

کدی بنویسید که این الگو را چاپ کند:

```
    *
   ***
  *****
 *******
*********
```

---

## مرجع سریع

### نحو for

```python
# پایه
for item in sequence:
    # code

# با range
for i in range(10):
for i in range(5, 10):
for i in range(0, 10, 2):

# با enumerate
for index, value in enumerate(list):
for index, value in enumerate(list, start=1):

# با items
for key, value in dict.items():

# با zip
for a, b in zip(list1, list2):
```

### دستورات مفید در حلقه

```python
break       # خروج از حلقه
continue    # رفتن به تکرار بعدی
else:       # اگر حلقه کامل اجرا شود (بدون break)
pass        # هیچ کاری نکن
```

---

## نکات کلیدی

۱. **for** برای تکرار روی مجموعه‌ها استفاده می‌شود
۲. **range()** برای حلقه روی اعداد استفاده می‌شود
۳. **enumerate()** برای گرفتن اندیس و مقدار
۴. **zip()** برای حلقه روی چندین لیست همزمان
۵. از **items()** برای حلقه روی دیکشنری‌ها استفاده کنید

---

## گام بعدی چیست؟

حالا که با حلقه for آشنا شدید، بیایید درباره کنترل حلقه‌ها یاد بگیریم:
- **کنترل حلقه** - break، continue، else
