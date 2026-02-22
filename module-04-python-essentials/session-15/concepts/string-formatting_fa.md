# قالب‌بندی رشته در پایتون

## آنچه خواهید آموخت
- چگونه متن و اعداد را زیبا نمایش دهید
- f-strings - روش مدرن پایتون
- قالب‌بندی اعداد، ارز، و درصد
- ترازبندی و عرض فیلد

---

## چرا قالب‌بندی؟

بدون قالب‌بندی:
```python
price = 19.99999
print("Price: $" + str(price))  # Price: $19.99999
```

با قالب‌بندی:
```python
print(f"Price: ${price:.2f}")   # Price: $20.00
```

**مزایا:**
- خواناتر
- کنترل بیشتر
- کد کمتر

---

## f-strings (توصیه می‌شود!)

f-strings راه آسان برای ترکیب متن و متغیرها هستند.

### ساختار پایه

```python
# f قبل از کوتیشن
name = "Alice"
print(f"Hello, {name}!")
```

### عبارات در داخل آکولادها

```python
age = 25
print(f"Next year you'll be {age + 1}")  # Next year you'll be 26

a, b = 10, 3
print(f"{a} divided by {b} is {a / b:.2f}")  # 10 divided by 3 is 3.33
```

---

## قالب‌بندی اعداد

### رقم اعشار

```python
pi = 3.14159265359

print(f"Pi: {pi:.2f}")    # Pi: 3.14
print(f"Pi: {pi:.4f}")    # Pi: 3.1416 (گرد می‌کند!)
print(f"Pi: {pi:.0f}")    # Pi: 3
```

**کدها:**
- `f` = اعشاری (float)
- `.2` = 2 رقم اعشار
- گرد کردن خودکار

### اعداد صحیح

```python
number = 42

print(f"Number: {number:d}")   # Number: 42
print(f"Number: {number:5d}")  # Number:    42 (عرض 5)
```

### جداکننده هزارگان

```python
large = 1234567890

print(f"{large:,}")       # 1,234,567,890
print(f"${large:,.2f}")   # $1,234,567,890.00
```

---

## قالب‌بندی ارز

### الگوی استاندارد

```python
price = 19.99
discount = 0.15
total = price * (1 - discount)

print(f"Price: ${price:.2f}")      # Price: $19.99
print(f"Discount: {discount:.0%}")  # Discount: 15%
print(f"Total: ${total:.2f}")      # Total: $16.99
```

### ستون ارز

```python
items = [
    ("Apple", 1.50),
    ("Banana", 0.75),
    ("Cherry", 2.00)
]

print("Item        Price")
print("-" * 20)
for item, price in items:
    print(f"{item:<12} ${price:>6.2f}")

# خروجی:
# Item        Price
# --------------------
# Apple        $  1.50
# Banana       $  0.75
# Cherry       $  2.00
```

---

## قالب‌بندی درصد

### ساختار

```python
rate = 0.8567

print(f"Success rate: {rate:.1%}")   # Success rate: 85.7%
print(f"Success rate: {rate:.2%}")   # Success rate: 85.67%
print(f"Success rate: {rate:.0%}")   # Success rate: 86%
```

**کد `%`** - ضرب در 100 و افزودن علامت %

---

## ترازبندی و عرض

### ترازبندی

```python
text = "Hi"

# چپ (پیش‌فرض)
print(f"|{text:<10}|")   # |Hi        |

# راست
print(f"|{text:>10}|")   # |        Hi|

# مرکز
print(f"|text:^10}|")   # |    Hi    |
```

**کدها:**
- `<` = چپ
- `>` = راست
- `^` = مرکز
- `10` = عرض کل

### ترکیب با اعداد

```python
# جدول نمرات
scores = [
    ("Alice", 95),
    ("Bob", 87),
    ("Carol", 92)
]

print(f"{'Name':<10} {'Score':>6}")
print("-" * 17)
for name, score in scores:
    print(f"{name:<10} {score:>6}")

# خروجی:
# Name       Score
# -----------------
# Alice         95
# Bob           87
# Carol         92
```

---

## پیشرفته

### پد کردن با صفر

```python
number = 42

print(f"{number:05d}")   # 00042
print(f"{number:5d}")   #    42
```

### نمادهای علمی

```python
large = 1234567890

print(f"{large:.2e}")   # 1.23e+09
print(f"{large:.2E}")   # 1.23E+09
```

### ترکیب همه

```python
import datetime

name = "Alice"
balance = 1234.56
date = datetime.datetime.now()

print(f"""
Statement for: {name}
Date: {date:%Y-%m-%d}
Balance: ${balance:,.2f}
""")

# خروجی:
# Statement for: Alice
# Date: 2024-01-15
# Balance: $1,234.56
```

---

## مرجع سریع

### کدهای قالب‌بندی

| کد | معنی | مثال |
|-----|-------|---------|
| `:d` | عدد صحیح | `42` |
| `:f` | اعشاری | `3.14` |
| `:.2f` | 2 رقم اعشار | `3.14` |
| `:,` | هزارگان | `1,000` |
| `:.1%` | درصد | `85.7%` |
| `:<10` | چپ، عرض 10 | `text      ` |
| `:>10` | راست، عرض 10 | `      text` |
| `:^10` | مرکز، عرض 10 | `   text   ` |
| `:05d` | پد با صفر | `00042` |

---

## نکات کلیدی

1. **f-strings آسان‌ترین روش** - با Python 3.6+
2. **`{var:.2f}` برای اعشار** - 2 رقم اعشار
3. **`{var:,}` برای هزارگان** - جداکننده
4. **`{var:.1%}` برای درصد** - ضرب در 100
5. **`< > ^` برای تراز** - چپ، راست، مرکز
6. **عدد برای عرض** - فضای تخصیص یافته

---

## قدم بعدی چیست؟

اکنون می‌توانید خروجی زیبا بسازید! بعدی، ما یاد می‌گیریم:
- عملیات و متدهای رشته
- دستکاری و جستجوی متن
- پردازش متن
