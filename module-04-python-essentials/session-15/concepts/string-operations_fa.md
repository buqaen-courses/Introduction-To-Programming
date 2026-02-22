# عملیات رشته در پایتون: دستکاری متن

## آنچه خواهید آموخت
- چگونه رشته‌ها را ایجاد و دستکاری کنید
- دسترسی به کاراکترها و برش (slicing)
- متدهای رایج رشته
- عملیات اصلی روی رشته‌ها

---

## ایجاد رشته‌ها

### کوتیشن‌ها

```python
# تک کوتیشن
name = 'Alice'

# جفت کوتیشن
city = "Paris"

# سه‌تایی (برای چند خط)
poem = """Roses are red,
Violets are blue,
Python is awesome,
And so are you!"""
```

**توجه:** رشته‌های پایتون **تغییرناپذیر** هستند - نمی‌توانید پس از ایجاد تغییر دهید!

---

## دسترسی به کاراکترها

### ایندکسینگ

```python
text = "Python"

# دسترسی با ایندکس
print(text[0])   # P (اولین)
print(text[1])   # y
print(text[5])   # n (آخرین)

# ایندکس منفی (از انتها)
print(text[-1])  # n (آخرین)
print(text[-2])  # o (دوم از آخر)
```

### برش (Slicing)

```python
text = "Hello World"

# برش [start:end] - end شامل نمی‌شود
print(text[0:5])   # Hello
print(text[6:11])  # World

# کوتاه‌نویسی‌ها
print(text[:5])    # Hello (از ابتدا)
print(text[6:])    # World (تا انتها)
print(text[:])     # Hello World (همه)

# با step
print(text[::2])   # HloWrd (هر 2 تایی)
print(text[::-1])  # dlroW olleH (معکوس!)
```

---

## متدهای اصلی رشته

### تغییر حروف

```python
text = "Hello World"

print(text.upper())      # HELLO WORLD
print(text.lower())      # hello world
print(text.title())      # Hello World
print(text.capitalize()) # Hello world
print(text.swapcase())   # hELLO wORLD
```

### جستجو

```python
text = "Hello World"

print(text.find("World"))     # 6 (ایندکس یا -1)
print(text.index("World"))    # 6 (ایندکس یا ارور)
print(text.count("l"))        # 3 (تعداد تکرار)
print(text.startswith("Hello")) # True
print(text.endswith("World"))     # True
```

### جایگزینی و تقسیم

```python
text = "Hello World"

# جایگزینی
new_text = text.replace("World", "Python")  # Hello Python

# تقسیم
words = text.split()          # ['Hello', 'World']
words = text.split("l")       # ['He', '', 'o Wor', 'd']

# اتصال
text = " ".join(words)        # Hello World
text = "-".join(words)        # Hello-World
```

### تمیز کردن

```python
text = "  Hello World  "

print(text.strip())    # "Hello World" (هر دو طرف)
print(text.lstrip())   # "Hello World  " (چپ)
print(text.rstrip())   # "  Hello World" (راست)

# حذف کاراکترهای خاص
text = "...Hello..."
print(text.strip("."))  # Hello
```

---

## عملیات رشته

### اتصال (Concatenation)

```python
first = "Hello"
second = "World"

print(first + " " + second)  # Hello World
```

### تکرار

```python
print("Hi! " * 3)   # Hi! Hi! Hi!
print("-" * 20)     # --------------------
```

### عضویت

```python
text = "Hello World"

print("Hello" in text)    # True
print("Python" in text)   # False
print("Python" not in text) # True
```

### طول

```python
text = "Hello"
print(len(text))   # 5
```

---

## اشتباهات رایج

### اشتباه 1: تلاش برای تغییر رشته

```python
# ❌ رشته‌ها تغییرناپذیر هستند!
text = "Hello"
text[0] = "h"   # TypeError!

# ✅ یک رشته جدید بسازید
text = "h" + text[1:]   # hello
```

### اشتباه 2: فراموش کردن اینکه slice رشته جدید می‌دهد

```python
# ❌ این کاری انجام نمی‌دهد!
text = "Hello"
text.upper()   # "HELLO" را برمی‌گرداند اما ذخیره نمی‌کند!

# ✅ نتیجه را ذخیره کنید
text = text.upper()   # "HELLO"
```

---

## مرجع سریع

| متد | استفاده | مثال | نتیجه |
|-----|---------|------|-------|
| `upper()` | حروف بزرگ | `"hi".upper()` | `"HI"` |
| `lower()` | حروف کوچک | `"HI".lower()` | `"hi"` |
| `title()` | اول هر کلمه بزرگ | `"hi there".title()` | `"Hi There"` |
| `find()` | یافتن زیررشته | `"hello".find("l")` | `2` |
| `replace()` | جایگزینی | `"hi".replace("i", "o")` | `"ho"` |
| `split()` | تقسیم به لیست | `"a,b".split(",")` | `["a", "b"]` |
| `join()` | اتصال لیست | `" ".join(["a", "b"])` | `"a b"` |
| `strip()` | حذف فاصله | `"  hi  ".strip()` | `"hi"` |
| `len()` | طول | `len("hi")` | `2` |

---

## نکات کلیدی

1. **رشته‌ها تغییرناپذیر هستند** - متدها رشته جدید می‌دهند
2. **ذخیره نتایج** - `text = text.upper()`
3. **برش قدرتمند است** - `[start:end:step]`
4. **join برای لیست‌ها** - از رشته جدا کننده استفاده کنید
5. **find vs index** - find -1 می‌دهد، index ارور

---

## قدم بعدی چیست؟

اکنون می‌توانید رشته‌ها را دستکاری کنید! بعدی، ما یاد می‌گیریم:
- پردازش متن پیشرفته
- اعتبارسنجی و پاکسازی داده‌ها
- الگوهای رایج پردازش متن
