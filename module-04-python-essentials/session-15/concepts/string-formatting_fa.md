# قالب‌بندی رشته‌ها: ایجاد خروجی حرفه‌ای

## چه چیزی یاد خواهید گرفت
- نحوه استفاده از f-string برای درج متغیرها در متن
- نحوه قالب‌بندی اعداد (اعشار، ارز، درصد)
- نحوه تراز کردن متن در ستون‌ها
- نحوه ایجاد خروجی تمیز و خوانا

---

## قالب‌بندی رشته چیست؟ (مثال کتاب‌های Mad Libs)

آیا کتاب‌های Mad Libs را به خاطر دارید؟ یک داستان با جاهای خالی مثل "اسم من ______ است و من ______ سال دارم." قالب‌بندی رشته دقیقاً شبیه پر کردن این جاهای خالی با مقادیر شماست.

### مشکل: ساختن رشته به روش قدیمی و نامرتب

```python
# روش قدیمی و سخت‌خوان (این کار را نکنید!)
name = "Alice"
age = 25
message = "My name is " + name + ", I am " + str(age) + " years old."
# خواندن سخت، خطا زدن آسان!
```

### راه‌حل: F-String‌ها

```python
# تمیز، خوانا و حرفه‌ای!
name = "Alice"
age = 25
message = f"My name is {name}, I am {age} years old."
# خیلی بهتر!
```

---

## F-String‌ها: روش مدرن

**F-String‌ها** (رشته‌های لغوی قالب‌بندی‌شده) ساده‌ترین راه برای قالب‌بندی رشته در پایتون هستند. بهترین انتخاب برای مبتدی‌ها!

### استفاده پایه F-String

```python
# قبل از رشته 'f' بگذارید، از {متغیرها} داخل استفاده کنید
name = "Alice"
age = 25

message = f"Hello, my name is {name} and I am {age} years old."
# Result: "Hello, my name is Alice and I am 25 years old."
```

### انجام ریاضی در F-String‌ها

```python
a, b = 10, 3
result = f"{a} + {b} = {a + b}"
# Result: "10 + 3 = 13"

price = 50
discount = 10
final = f"Price: ${price}, Discount: ${discount}, Total: ${price - discount}"
# Result: "Price: $50, Discount: $10, Total: $40"
```

---

## قالب‌بندی اعداد

### کنترل اعشار

```python
pi = 3.14159265359

# نمایش 2 رقم اعشار
print(f"Pi: {pi:.2f}")      # "Pi: 3.14"

# نمایش 4 رقم اعشار
print(f"Pi: {pi:.4f}")      # "Pi: 3.1416"
```

### قالب‌بندی ارز

```python
price = 29.99

# فرمت ارز پایه
print(f"Price: ${price:.2f}")      # "Price: $29.99"

# اعداد بزرگ با کاما
big_price = 1234.50
print(f"Price: ${big_price:,.2f}")  # "Price: $1,234.50"
```

### قالب‌بندی درصد

```python
ratio = 0.856

# تبدیل به درصد
print(f"Success rate: {ratio:.1%}")  # "Success rate: 85.6%"

# درصد با 0 اعشار
print(f"Completed: {ratio:.0%}")     # "Completed: 86%"
```

---

## تراز کردن متن

### ایجاد جداول ساده

```python
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]

# ایجاد یک جدول زیبا
print(f"{'Name':<10} {'Score':>6}")
print("-" * 18)
for name, score in zip(names, scores):
    print(f"{name:<10} {score:>6}")

# Output:
# Name       Score
# ------------------
# Alice          95
# Bob            87
# Charlie        92
```

گزینه‌های تراز:
- `<` چپ‌چین
- `>` راست‌چین
- `^` وسط‌چین

### مثال‌های بیشتر تراز

```python
text = "Hi"

print(f"[{text:<10}]")   # [Hi        ] - چپ‌چین
print(f"[{text:>10}]")   # [        Hi] - راست‌چین
print(f"[{text:^10}]")   # [    Hi    ] - وسط‌چین
```

---

## F-String‌های چندخطی

```python
name = "Alice"
age = 25
city = "New York"

message = f"""
Name:   {name}
Age:    {age}
City:   {city}
Next year, I'll be {age + 1}!
"""

print(message)
# Output:
# Name:   Alice
# Age:    25
# City:   New York
# Next year, I'll be 26!
```

---

## اشتباهات رایج مبتدی‌ها

### اشتباه 1: فراموش کردن پیشوند 'f'

```python
# ❌ اشتباه - 'f' ندارد
name = "Alice"
message = "Hello, {name}"   # Result: "Hello, {name}"

# ✅ درست
message = f"Hello, {name}"  # Result: "Hello, Alice"
```

### اشتباه 2: استفاده از کوتیشن داخل کوتیشن

```python
# ❌ اشتباه - خطای syntax
message = f"He said "Hello""   # Syntax error!

# ✅ درست - از نوع کوتیشن متفاوت استفاده کنید
message = f'He said "Hello"'   # کوتیشن تک بیرون
message = f"He said 'Hello'"   # کوتیشن دوبل بیرون
message = f"He said \"Hello\"" # کوتیشن فرار شده
```

### اشتباه 3: مشخصه قالب‌بندی اشتباه

```python
# ❌ اشتباه - تلاش برای قالب‌بندی متن به عنوان عدد
text = "Hello"
print(f"{text:.2f}")   # Error! Can't format string as float

# ✅ درست
number = 3.14159
print(f"{number:.2f}")  # "3.14"
```

---

## تمرین‌های عملی

### تمرین 1: رسید ساده

ایجاد یک رسید قالب‌بندی‌شده برای خرید.

```python
def print_receipt(item, price, quantity):
    total = price * quantity
    print("=" * 30)
    print(f"{'RECEIPT':^30}")
    print("=" * 30)
    print(f"{'Item:':<15} {item}")
    print(f"{'Price:':<15} ${price:.2f}")
    print(f"{'Quantity:':<15} {quantity}")
    print("-" * 30)
    print(f"{'Total:':<15} ${total:.2f}")
    print("=" * 30)

# Test
print_receipt("Coffee", 3.50, 2)
```

### تمرین 2: کارنامه نمرات

ایجاد یک کارنامه نمرات قالب‌بندی‌شده.

```python
def grade_report(name, grades):
    average = sum(grades) / len(grades)
    print(f"\n{'='*30}")
    print(f"{'GRADE REPORT':^30}")
    print(f"{'='*30}")
    print(f"Student: {name}")
    print(f"{'-'*30}")
    for i, grade in enumerate(grades, 1):
        print(f"Test {i}: {grade:>20}")
    print(f"{'-'*30}")
    print(f"Average: {average:>19.1f}")
    print(f"{'='*30}")

# Test
grade_report("Alice", [85, 92, 78, 96])
```

### تمرین 3: تبدیل‌کننده دما

قالب‌بندی تمیز تبدیل دما.

```python
def format_temperature(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return f"{celsius:.1f}°C = {fahrenheit:.1f}°F"

# Test
print(format_temperature(0))      # 0.0°C = 32.0°F
print(format_temperature(100))    # 100.0°C = 212.0°F
print(format_temperature(37))     # 37.0°C = 98.6°F
```

---

## مرجع سریع

| آنچه می‌خواهید | نحوه انجام | مثال | نتیجه |
|--------------|----------|-------|--------|
| درج متغیر | `f"{var}"` | `f"{name}"` | value of name |
| 2 رقم اعشار | `f"{n:.2f}"` | `f"{3.14159:.2f}"` | 3.14 |
| درصد | `f"{n:.1%}"` | `f"{0.85:.1%}"` | 85.0% |
| جداکننده هزارگان | `f"{n:,}"` | `f"{1234567:,}"` | 1,234,567 |
| چپ‌چین (10 کاراکتر) | `f"{s:<10}"` | `f"{'Hi':<10}"` | 'Hi        ' |
| راست‌چین (10 کاراکتر) | `f"{s:>10}"` | `f"{'Hi':>10}"` | '        Hi' |
| وسط‌چین (10 کاراکتر) | `f"{s:^10}"` | `f"{'Hi':^10}"` | '    Hi    ' |
| ارز | `f"${n:.2f}"` | `f"${29.99:.2f}"` | $29.99 |

---

## نکات کلیدی

1. **F-String‌ها بهترین انتخاب هستند** - `f` قبل از کوتیشن بگذارید و از `{variable}` داخل استفاده کنید
2. **قالب‌بندی اعداد با `:.2f`** - اعشار را کنترل می‌کند (2 در این مثال)
3. **تراز متن با `<`, `>`, `^`** - چپ، راست و وسط
4. **استفاده از `:.1%` برای درصد** - اعشار را به درصد تبدیل می‌کند
5. **می‌توانید ریاضی داخل f-string انجام دهید** - `{age + 1}` کاملاً کار می‌کند

---

## بعدی چیست؟

در درس بعدی، شما درباره **پردازش متن** یاد خواهید گرفت - چگونه متن را جستجو، تقسیم و دستکاری کنید تا داده‌های متنی را تحلیل و تبدیل کنید. برنامه‌های عملی مثل شمارنده کلمات و تمیزکننده متن خواهید ساخت.
