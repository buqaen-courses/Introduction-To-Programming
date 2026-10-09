# قالب‌بندی رشته: ساخت خروجی حرفه‌ای

## چه چیزی یاد می‌گیرید
- چگونه با f-string متغیرها را داخل متن قرار دهید
- چگونه اعداد را قالب‌بندی کنید (اعشار، واحد پول، درصد)
- چگونه متن را در ستون‌ها تراز کنید
- چگونه خروجی تمیز و خوانا بسازید

## قالب‌بندی رشته چیست؟ (تشبیه به Mad Libs)

Mad Libs را به یاد دارید؟ داستانی با جاهای خالی مثل «نام من ... است و ... سال سنم دارم». قالب‌بندی رشته یعنی پر کردن آن جاهای خالی با مقادیر خودتان.

### مسئله: ساخت رشته به شکل شلوغ

```python
# روش قدیمی و ناخوانا (این کار را نکنید!)
name = "Alice"
age = 25
message = "My name is " + name + ", I am " + str(age) + " years old."
# ناخوانا، و مستعد اشتباه!
```

### راه‌حل: f-string

```python
# تمیز، خوانا، حرفه‌ای!
name = "Alice"
age = 25
message = f"My name is {name}, I am {age} years old."
# خیلی بهتر!
```

---

## f-string: روش مدرن

**f-string** (رشته قالب‌بندی‌شده) ساده‌ترین راه قالب‌بندی رشته در پایتون است. برای مبتدی‌ها بهترین انتخاب است!

### کاربرد پایه f-string

```python
# پیش از رشته 'f' بگذارید، داخل آن از {متغیرها} استفاده کنید
name = "Alice"
age = 25

message = f"Hello, my name is {name} and I am {age} years old."
# Result: "Hello, my name is Alice and I am 25 years old."
```

### انجام حساب در f-string

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

### کنترل رقم‌های اعشار

```python
pi = 3.14159265359

# نمایش با 2 رقم اعشار
print(f"Pi: {pi:.2f}")      # "Pi: 3.14"

# نمایش با 4 رقم اعشار
print(f"Pi: {pi:.4f}")      # "Pi: 3.1416"
```

### قالب‌بندی واحد پول

```python
price = 29.99

# قالب پایه واحد پول
print(f"Price: ${price:.2f}")      # "Price: $29.99"

# اعداد بزرگ با جداکننده هزارگان
big_price = 1234.50
print(f"Price: ${big_price:,.2f}")  # "Price: $1,234.50"
```

### قالب‌بندی درصد

```python
ratio = 0.856

# تبدیل به درصد
print(f"Success rate: {ratio:.1%}")  # "Success rate: 85.6%"

# درصد بدون رقم اعشار
print(f"Completed: {ratio:.0%}")     # "Completed: 86%"
```

---

## تراز کردن متن

### ساخت جدول ساده

```python
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]

# ساخت یک جدول مرتب
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

### نمونه‌های بیشتر تراز

```python
text = "Hi"

print(f"[{text:<10}]")   # [Hi        ] - چپ‌چین
print(f"[{text:>10}]")   # [        Hi] - راست‌چین
print(f"[{text:^10}]")   # [    Hi    ] - وسط‌چین
```

---

## f-string چندخطی

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

## اشتباهات رایج مبتدی

### اشتباه ۱: فراموش کردن پیشوند 'f'

```python
# ❌ اشتباه - پیشوند 'f' جا افتاده
name = "Alice"
message = "Hello, {name}"   # Result: "Hello, {name}"

# ✅ درست
message = f"Hello, {name}"  # Result: "Hello, Alice"
```

### اشتباه ۲: گیومه داخل گیومه

```python
# ❌ اشتباه - خطای نحوی می‌دهد
message = f"He said "Hello""   # Syntax error!

# ✅ درست - از نوع گیومه متفاوت استفاده کنید
message = f'He said "Hello"'   # گیومه تکی بیرون
message = f"He said 'Hello'"   # گیومه دوتایی بیرون
message = f"He said \"Hello\"" # گیومه escape شده
```

### اشتباه ۳: مشخصه قالب نادرست

```python
# ❌ اشتباه - تلاش برای قالب‌بندی متن به‌عنوان عدد
text = "Hello"
print(f"{text:.2f}")   # Error! نمی‌توان رشته را float قالب‌بندی کرد

# ✅ درست
number = 3.14159
print(f"{number:.2f}")  # "3.14"
```

---

## تمرین کنید

### تمرین ۱: رسید ساده
برای یک خرید، رسیدی قالب‌بندی‌شده بسازید.

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

### تمرین ۲: کارنامه
یک کارنامه قالب‌بندی‌شده بسازید.

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

### تمرین ۳: مبدل دما
تبدیل دما را مرتب قالب‌بندی کنید.

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

| چه می‌خواهید | چگونه | مثال | نتیجه |
|--------------|-------|------|--------|
| درج متغیر | `f"{var}"` | `f"{name}"` | مقدار name |
| 2 رقم اعشار | `f"{n:.2f}"` | `f"{3.14159:.2f}"` | 3.14 |
| درصد | `f"{n:.1%}"` | `f"{0.85:.1%}"` | 85.0% |
| جداکننده هزارگان | `f"{n:,}"` | `f"{1234567:,}"` | 1,234,567 |
| چپ‌چین (۱۰ نویسه) | `f"{s:<10}"` | `f"{'Hi':<10}"` | 'Hi        ' |
| راست‌چین (۱۰ نویسه) | `f"{s:>10}"` | `f"{'Hi':>10}"` | '        Hi' |
| وسط‌چین (۱۰ نویسه) | `f"{s:^10}"` | `f"{'Hi':^10}"` | '    Hi    ' |
| واحد پول | `f"${n:.2f}"` | `f"${29.99:.2f}"` | $29.99 |

---

## نکات کلیدی

1. **f-string بهترین انتخاب است**: پیش از گیومه `f` بگذارید و داخلش از `{variable}` استفاده کنید
2. **اعداد را با `:.2f` قالب‌بندی کنید**: تعداد رقم اعشار را کنترل می‌کند (اینجا ۲)
3. **متن را با `<`، `>`، `^` تراز کنید**: چپ‌چین، راست‌چین، وسط‌چین
4. **برای درصد از `:.1%` استفاده کنید**: اعشار را به درصد تبدیل می‌کند
5. **داخل f-string می‌توانید حساب کنید**: `{age + 1}` بی‌نقص کار می‌کند

## قدم بعدی

در درس بعدی، **پردازش متن** را یاد می‌گیرید: چگونه رشته‌ها را جست‌وجو، تقسیم و دستکاری کنید تا داده‌های متنی را تحلیل و تبدیل کنید. برنامه‌های کاربردی مثل شمارنده کلمه و پاک‌کننده متن خواهید ساخت.