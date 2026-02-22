# عبارات و عملگرها در پایتون

## آنچه خواهید آموخت
- چه نوع عملیات‌هایی می‌توانید در پایتون انجام دهید
- چگونه محاسبات، مقایسه‌ها و عملیات منطقی انجام دهید
- عملگرهای خاص و نحوه استفاده از آنها

---

## عبارات چه هستند؟

**عبارات** قطعات کدی هستند که یک مقدار را تولید می‌کنند. آنها مثل **فرمول** یا **محاسبه** هستند.

```python
# همه اینها عبارات هستند
5 + 3                   # عبارت ریاضی: ۸
"Hello" + " World"      # عبارت رشته‌ای: "Hello World"
age > 18              # عبارت مقایسه‌ای: True یا False
```

**عبارت** = مقادیر + عملگرها

---

## عملگرهای ریاضی (حسابی)

### عملگرهای پایه

| عملگر | نام | مثال | نتیجه |
|---------|------|--------|--------|
| `+` | جمع | `5 + 3` | `8` |
| `-` | تفریق | `5 - 3` | `2` |
| `*` | ضرب | `5 * 3` | `15` |
| `/` | تقسیم | `5 / 2` | `2.5` |
| `//` | تقسیم صحیح | `5 // 2` | `2` |
| `%` | باقیمانده | `5 % 2` | `1` |
| `**` | توان | `2 ** 3` | `8` |

### مثال‌ها

```python
# جمع و تفریق
print(10 + 5)            # 15
print(10 - 5)            # 5

# ضرب و تقسیم
print(10 * 5)            # 50
print(10 / 5)            # 2.0 (همیشه float!)

# تقسیم صحیح (اعشار حذف می‌شود)
print(10 // 3)           # 3
print(7 // 2)            # 3

# باقیمانده (بسیار مفید!)
print(10 % 3)            # 1 (10 = 3*3 + 1)
print(15 % 4)            # 3 (15 = 4*3 + 3)

# توان
print(2 ** 3)            # 8 (2 به توان 3)
print(3 ** 2)            # 9 (3 به توان 2)
print(16 ** 0.5)         # 4.0 (جذر ۱۶)
```

### عملگرهای ترکیبی (تخصیص)

```python
x = 10

# روش طولانی
x = x + 5               # x حالا ۱۵ است

# روش کوتاه‌تر
x += 5                  # x حالا ۲۰ است

# بقیه عملگرها هم کار می‌کنند
x -= 3                  # x حالا ۱۷
x *= 2                  # x حالا ۳۴
x /= 2                  # x حالا ۱۷.۰
x //= 3                 # x حالا ۵.۰
x %= 3                  # x حالا ۲.۰
x **= 2                 # x حالا ۴.۰
```

---

## عملگرهای مقایسه‌ای (رابطه‌ای)

اینها دو مقدار را مقایسه کرده و `True` یا `False` برمی‌گردانند.

| عملگر | نام | مثال | نتیجه |
|---------|------|--------|--------|
| `==` | برابر | `5 == 5` | `True` |
| `!=` | نابرابر | `5 != 3` | `True` |
| `<` | کوچک‌تر | `3 < 5` | `True` |
| `>` | بزرگ‌تر | `5 > 3` | `True` |
| `<=` | کوچک‌تر یا برابر | `5 <= 5` | `True` |
| `>=` | بزرگ‌تر یا برابر | `5 >= 3` | `True` |

### مثال‌ها

```python
age = 25

# مقایسه اعداد
print(age == 25)         # True
print(age != 30)         # True
print(age < 30)          # True
print(age > 20)          # True
print(age <= 25)         # True
print(age >= 18)         # True

# مقایسه رشته‌ها
name = "Alice"
print(name == "Alice")   # True
print(name != "Bob")     # True
print(name < "Bob")      # True (ترتیب الفبایی)
```

**هشدار مهم:**
```python
# ❌ استفاده از = (تخصیص)
if age = 25:            # SyntaxError!

# ✅ استفاده از == (مقایسه)
if age == 25:           # صحیح
```

---

## عملگرهای منطقی (بولی)

اینها مقادیر `True` و `False` را ترکیب می‌کنند.

| عملگر | نام | مثال | نتیجه |
|---------|------|--------|--------|
| `and` | و | `True and False` | `False` |
| `or` | یا | `True or False` | `True` |
| `not` | نقیض | `not True` | `False` |

### جدول درستی

| A | B | A and B | A or B | not A |
|---|---|---------|--------|-------|
| True | True | True | True | False |
| True | False | False | True | False |
| False | True | False | True | True |
| False | False | False | False | True |

### مثال‌ها

```python
# and - هر دو باید True باشند
print(True and True)     # True
print(True and False)    # False
print(False and True)    # False
print(False and False)   # False

# or - حداقل یکی باید True باشد
print(True or True)      # True
print(True or False)     # True
print(False or True)     # True
print(False or False)    # False

# not - معکوس می‌کند
print(not True)          # False
print(not False)         # True
```

### استفاده در شرایط واقعی

```python
age = 25
has_license = True

# هر دو شرط باید برقرار باشند
can_drive = age >= 18 and has_license
print(can_drive)         # True

# حداقل یک شرط
needs_id = age < 18 or age > 65
print(needs_id)          # False

# معکوس کردن
is_minor = not (age >= 18)
print(is_minor)          # False
```

---

## عملگرهای بیتی

اینها روی بیت‌های اعداد کار می‌کنند (پیشرفته‌تر).

| عملگر | نام | توضیح |
|---------|------|---------|
| `&` | AND | بیت ۱ اگر هر دو ۱ باشند |
| `\|` | OR | بیت ۱ اگر حداقل یکی ۱ باشد |
| `^` | XOR | بیت ۱ اگر فقط یکی ۱ باشد |
| `~` | NOT | همه بیت‌ها معکوس می‌شوند |
| `<<` | شیفت چپ | ضرب در ۲ |
| `>>` | شیفت راست | تقسیم بر ۲ |

### مثال‌های ساده

```python
# AND: فقط بیت‌های مشترک
print(5 & 3)             # 1 (0101 & 0011 = 0001)

# OR: همه بیت‌های ۱
print(5 | 3)             # 7 (0101 | 0011 = 0111)

# XOR: فقط یکی
print(5 ^ 3)             # 6 (0101 ^ 0011 = 0110)

# شیفت
print(8 << 1)            # 16 (8 * 2)
print(8 >> 1)            # 4 (8 / 2)
```

---

## عملگرهای عضویت

بررسی اینکه آیا چیزی در یک مجموعه وجود دارد.

| عملگر | نام | مثال | نتیجه |
|---------|------|--------|--------|
| `in` | عضو است | `"a" in "cat"` | `True` |
| `not in` | عضو نیست | `"z" not in "cat"` | `True` |

### مثال‌ها

```python
# در رشته‌ها
text = "Hello, World!"
print("H" in text)       # True
print("h" in text)       # False (حساس به بزرگی)
print("World" in text)   # True
print("Python" in text)  # False

# در لیست‌ها
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)         # True
print("orange" not in fruits)    # True

# در دیکشنری‌ها (فقط کلیدها بررسی می‌شوند)
person = {"name": "Alice", "age": 25}
print("name" in person)          # True
print("Alice" in person)         # False (مقدار نیست، کلید هست)
print("Alice" in person.values()) # True
```

---

## عملگرهای هویت

بررسی اینکه آیا دو متغیر به یک شیء اشاره می‌کنند.

| عملگر | نام | مثال |
|---------|------|--------|
| `is` | همان شیء است | `a is b` |
| `is not` | همان شیء نیست | `a is not b` |

### مثال‌ها

```python
# برای اعداد کوچک، پایتون آنها را بهینه می‌کند
a = 5
b = 5
print(a is b)            # True (معمولاً)

# برای اعداد بزرگ یا لیست‌ها، معمولاً False
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)            # True (مقادیر برابرند)
print(x is y)            # False (شیء متفاوت)

# None را با is بررسی کنید
value = None
print(value is None)     # True (این روش درست است)
print(value == None)     # True (اما is بهتر است)
```

---

## عملگرهای رشته‌ای

### الحاق (پیوند)

```python
first = "Hello"
second = "World"
result = first + " " + second
print(result)            # "Hello World"

# تکرار
line = "-" * 20
print(line)              # "--------------------"

# تبدیل به رشته
age = 25
text = "I am " + str(age) + " years old"
print(text)              # "I am 25 years old"

# یا بهتر
print(f"I am {age} years old")  # "I am 25 years old"
```

---

## عملگر سه‌گانه (شرطی)

یک **میان‌بر** برای if-else ساده.

```python
# نحو
# value_if_true if condition else value_if_false

# مثال
age = 20
status = "adult" if age >= 18 else "minor"
print(status)            # "adult"

# معادل با if-else معمولی
if age >= 18:
    status = "adult"
else:
    status = "minor"
```

### مثال‌های بیشتر

```python
# بزرگ‌ترین عدد
a, b = 10, 20
max_value = a if a > b else b
print(max_value)         # 20

# مقدار مطلق
number = -5
abs_value = number if number >= 0 else -number
print(abs_value)         # 5
```

---

## اشتباهات رایج

### اشتباه ۱: = به جای ==

```python
# ❌ اشتباه
if x = 5:               # SyntaxError!
    print("x is 5")

# ✅ صحیح
if x == 5:
    print("x is 5")
```

### اشتباه ۲: تقسیم صحیح vs اعشاری

```python
# ❌ غافلگیرکننده در پایتون ۲ (در پایتون ۳ خوب است)
result = 5 / 2
print(result)            # 2.5 (در پایتون ۳)
print(5 // 2)            # 2 (تقسیم صحیح)
```

### اشتباه ۳: and/or اشتباهی

```python
# ❌ اشتباه رایج
if age > 18 and < 65:   # SyntaxError!

# ✅ صحیح
if age > 18 and age < 65:

# ✅ حتی بهتر
if 18 < age < 65:       # زنجیره‌سازی مقایسه
```

### اشتباه ۴: is به جای ==

```python
# ❌ معمولاً اشتباه
if x is 5:              # ممکن است کار کند، اما == بهتر است

# ✅ صحیح برای مقایسه مقادیر
if x == 5:

# ✅ صحیح برای None
if x is None:
```

### اشتباه ۵: فراموش کردن تبدیل نوع

```python
# ❌ خطا
age = input("Age: ")
if age > 18:            # TypeError! رشته با عدد مقایسه نمی‌شود

# ✅ صحیح
age = int(input("Age: "))
if age > 18:
```

---

## خودتان امتحان کنید: تمرین‌ها

### تمرین ۱: عملگرهای پایه

```python
# اینها را محاسبه کنید
a = 17
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

### تمرین ۲: عملگرهای مقایسه‌ای

```python
# اینها True یا False؟
x = 10
y = 20

print(x == y)
print(x != y)
print(x < y)
print(x >= 10)
print(x > 5 and y < 25)
```

### تمرین ۳: عملگرهای ترکیبی

```python
# از عملگرهای =+ و -= استفاده کنید
score = 100

# ۵۰ اضافه کنید
# ۲۵ کم کنید
# ۲ برابر کنید
```

### تمرین ۴: محاسبه ساعت و دقیقه

```python
# کل دقیقه را به ساعت و دقیقه تبدیل کنید
total_minutes = 145

hours = 
minutes = 

print(f"{hours} hours and {minutes} minutes")
```

### تمرین ۵: عملگر سه‌گانه

```python
# از عملگر سه‌گانه استفاده کنید
number = -10

# اگر number مثبت باشد "positive"، وگرنه "negative" یا "zero"
sign = 

print(sign)
```

---

## مرجع سریع

### عملگرهای ریاضی

```python
+   جمع
-   تفریق
*   ضرب
/   تقسیم (float)
//  تقسیم صحیح
%   باقیمانده
**  توان
```

### عملگرهای تخصیص ترکیبی

```python
x += y    # x = x + y
x -= y    # x = x - y
x *= y    # x = x * y
x /= y    # x = x / y
x //= y   # x = x // y
x %= y    # x = x % y
x **= y   # x = x ** y
```

### عملگرهای مقایسه‌ای

```python
==  برابر
!=  نابرابر
<   کوچک‌تر
>   بزرگ‌تر
<=  کوچک‌تر یا برابر
>=  بزرگ‌تر یا برابر
```

### عملگرهای منطقی

```python
and    هر دو True
or     حداقل یک True
not    معکوس
```

### سایر عملگرها

```python
in         عضویت
is         هویت
? :        عملگر سه‌گانه (در پایتون: a if cond else b)
```

---

## نکات کلیدی

۱. **عملگرها** نحوه ترکیب مقادیر را تعیین می‌کنند
۲. **تقسیم `/`** همیشه float برمی‌گرداند
۳. **تقسیم صحیح `//`** اعشار را حذف می‌کند
۴. **باقیمانده `%`** برای زوج/فرد بودن عالی است: `x % 2 == 0`
۵. **== برای مقایسه، = برای تخصیص**
۶. **is برای None، == برای مقایسه مقادیر**

---

## گام بعدی چیست؟

حالا که با عملگرها آشنا شدید، بیایید درباره ترتیب ارزیابی یاد بگیریم:
- **ترتیب ارزیابی** - کدام عملیات اول انجام می‌شود
