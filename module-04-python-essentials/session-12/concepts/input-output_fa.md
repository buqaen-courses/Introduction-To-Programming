# ورودی و خروجی در پایتون

## آنچه خواهید آموخت
- چگونه اطلاعات را از کاربر بگیرید
- چگونه داده را روی صفحه نمایش دهید
- روش‌های مختلف نمایش خروجی

---

## چرا ورودی/خروجی اهمیت دارد؟

برنامه‌های کامپیوتری نیاز دارند:
- **ورودی** - گرفتن اطلاعات از کاربر، فایل‌ها، یا سایر منابع
- **خروجی** - نمایش نتایج، ذخیره در فایل‌ها، یا ارسال به جای دیگر

بدون ورودی/خروجی، برنامه‌ها جعبه‌های سیاه هستند که نمی‌توانید با آنها تعامل داشته باشید!

---

## خروجی: تابع print()

### نحو پایه

```python
print(value1, value2, ...)
```

### مثال‌های ساده

```python
# یک مقدار
print("Hello, World!")

# چند مقدار
print("Hello", "World")    # با فاصله بین آنها

# اعداد
print(42)
print(3.14)

# متغیرها
name = "Alice"
print(name)
```

### چاپ چندین مقدار

```python
# جدا کردن با فاصله (پیش‌فرض)
print("Hello", "World", "!")    # Hello World !

# تغییر جداکننده
print("Hello", "World", sep="-") # Hello-World
print("Hello", "World", sep="")  # HelloWorld

# تغییر پایان (پیش‌فرض: newline)
print("Hello", end=" ")
print("World")                 # Hello World (در یک خط)
```

### کنترل فرمت خروجی

```python
# پیش‌فرض
print(1, 2, 3)                 # 1 2 3

# بدون فاصله
print(1, 2, 3, sep="")         # 123

# با کاما
print(1, 2, 3, sep=", ")       # 1, 2, 3

# در یک خط
print("Loading", end="")
print("...", end="")
print("Done!")                 # Loading...Done!
```

---

## رشته‌های f (f-strings)

بهترین روش برای ترکیب متن و متغیرها.

### نحو

```python
f"text {variable} more text"
```

### مثال‌های پایه

```python
name = "Alice"
age = 25

# جاسازی متغیرها
print(f"Hello, {name}!")
print(f"{name} is {age} years old")

# عبارات
print(f"Next year, {name} will be {age + 1}")

# محاسبات
price = 19.99
quantity = 3
print(f"Total: ${price * quantity}")
```

### قالب‌بندی اعداد

```python
pi = 3.14159265359

# تعداد اعشار
print(f"Pi = {pi:.2f}")        # Pi = 3.14
print(f"Pi = {pi:.4f}")        # Pi = 3.1416

# عرض
number = 42
print(f"Number: {number:5}")   # Number:    42

# صفر اضافه کردن
print(f"Number: {number:05}")  # Number: 00042
```

### فرمت‌های پیشرفته

```python
# درصد
progress = 0.85
print(f"Progress: {progress:.1%}")  # Progress: 85.0%

# هزارگان
big_number = 1234567
print(f"{big_number:,}")       # 1,234,567

# چپ‌چین و راست‌چین
text = "Hi"
print(f"[{text:<10}]")         # [Hi        ] (چپ‌چین)
print(f"[{text:>10}]")         # [        Hi] (راست‌چین)
print(f"[{text:^10}]")         # [    Hi    ] (وسط‌چین)
```

---

## روش‌های قدیمی‌تر (بدانید اما از f-strings استفاده کنید)

### روش % (قالب‌بندی قدیمی)

```python
name = "Alice"
age = 25

# %s برای رشته، %d برای عدد صحیح
print("Hello, %s! You are %d years old." % (name, age))

# %.2f برای اعشار
price = 19.99
print("Price: $%.2f" % price)
```

### روش .format()

```python
name = "Alice"
age = 25

# موقعیتی
print("Hello, {}! You are {} years old.".format(name, age))

# با شماره
print("Hello, {0}! You are {1} years old.".format(name, age))

# با نام
print("Hello, {name}! You are {age} years old.".format(name=name, age=age))
```

**نتیجه:** از f-strings استفاده کنید - تمیزتر و سریع‌تر هستند!

---

## ورودی: تابع input()

### نحو پایه

```python
variable = input("Prompt message: ")
```

### مثال‌های ساده

```python
# گرفتن نام
name = input("Enter your name: ")
print(f"Hello, {name}!")

# گرفتن ورودی خام
response = input("Continue? (yes/no): ")
print(f"You said: {response}")
```

### ⚠️ مهم: ورودی همیشه رشته است!

```python
# ❌ این کار نمی‌کند
age = input("Enter your age: ")
next_year = age + 1        # TypeError!

# ✅ تبدیل به عدد
age = int(input("Enter your age: "))
next_year = age + 1
print(f"Next year you'll be {next_year}")
```

### گرفتن اعداد

```python
# عدد صحیح
age = int(input("Enter your age: "))

# عدد اعشاری
height = float(input("Enter your height in meters: "))

# استفاده
print(f"You are {age} years old and {height}m tall")
```

### گرفتن چندین مقدار

```python
# روش ۱: جداگانه
first = input("First number: ")
second = input("Second number: ")
x = int(first)
y = int(second)

# روش ۲: در یک خط
x, y = input("Enter two numbers: ").split()
x = int(x)
y = int(y)

print(f"Sum: {x + y}")
```

---

## برنامه‌های تعاملی کامل

### مثال ۱: ماشین حساب ساده

```python
# گرفتن ورودی
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# انجام محاسبات
sum_result = num1 + num2
diff = num1 - num2
product = num1 * num2
quotient = num1 / num2

# نمایش نتایج
print(f"\nResults:")
print(f"Sum: {sum_result}")
print(f"Difference: {diff}")
print(f"Product: {product}")
print(f"Quotient: {quotient:.2f}")
```

### مثال ۲: فرم ثبت‌نام

```python
print("=== Registration Form ===\n")

# جمع‌آوری اطلاعات
first_name = input("First name: ")
last_name = input("Last name: ")
age = int(input("Age: "))
email = input("Email: ")

# نمایش خلاصه
print(f"\n=== Summary ===")
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
print(f"Email: {email}")
print(f"\nWelcome, {first_name}! Registration complete.")
```

### مثال ۳: تبدیل درجه حرارت

```python
print("Temperature Converter\n")

# گرفتن ورودی
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# تبدیل
celsius = (fahrenheit - 32) * 5 / 9
kelvin = celsius + 273.15

# نمایش نتایج
print(f"\n{fahrenheit}°F = {celsius:.2f}°C = {kelvin:.2f}K")
```

---

## گرفتن ورودی ایمن

### بررسی خطا

```python
# روش ساده با try-except
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old")
except ValueError:
    print("Please enter a valid number!")
```

### حلقه تا ورودی معتبر

```python
# تکرار تا ورودی صحیح
while True:
    try:
        age = int(input("Enter your age (1-120): "))
        if 1 <= age <= 120:
            break
        print("Please enter a valid age!")
    except ValueError:
        print("Please enter a number!")

print(f"Thank you! You are {age} years old.")
```

---

## اشتباهات رایج

### اشتباه ۱: فراموش کردن تبدیل ورودی

```python
# ❌ اشتباه
age = input("Age: ")
years_until_100 = 100 - age  # TypeError!

# ✅ صحیح
age = int(input("Age: "))
years_until_100 = 100 - age
```

### اشتباه ۲: جمع رشته به جای عدد

```python
# ❌ اشتباه
num1 = input("First: ")      # کاربر: "5"
num2 = input("Second: ")     # کاربر: "3"
result = num1 + num2         # "53" (نه 8!)

# ✅ صحیح
num1 = int(input("First: "))
num2 = int(input("Second: "))
result = num1 + num2         # 8
```

### اشتباه ۳: فرض کردن ورودی صحیح

```python
# ❌ ممکن است خطا دهد
number = int(input("Enter a number: "))  # کاربر: "abc"

# ✅ بررسی خطا
user_input = input("Enter a number: ")
if user_input.isdigit():
    number = int(user_input)
else:
    print("That's not a number!")
```

### اشتباه ۴: پرانتز اضافی در f-strings

```python
# ❌ اشتباه
print(f"Result: {len(text)}")  # این خوب است
print(f"Result: {len(text) + 1}")  # این هم خوب است

# اما این غیرضروری است
print(f"Result: {(x + y)}")    # پرانتز اضافی
```

---

## خودتان امتحان کنید: تمرین‌ها

### تمرین ۱: برنامه سلام

کدی بنویسید که:
۱. نام کاربر را بگیرد
۲. سن کاربر را به عنوان عدد بگیرد
۳. پیام خوش‌آمدگویی شخصی‌سازی شده چاپ کند

### تمرین ۲: ماشین حساب مساحت

کدی بنویسید که:
۱. طول و عرض یک مستطیل را بگیرد
۲. مساحت و محیط را محاسبه کند
۳. نتایج را با دو رقم اعشار نمایش دهد

### تمرین ۳: تبدیل واحد

کدی بنویسید که:
۱. سانتی‌متر را بگیرد
۲. به متر و اینچ تبدیل کند (۱ اینچ = ۲.۵۴ سانتی‌متر)
۳. همه مقادیر را نمایش دهد

### تمرین ۴: ماشین حساب BMI

کدی بنویسید که:
۱. وزن (کیلوگرم) و قد (متر) را بگیرد
۲. BMI را محاسبه کند: وزن / (قد ^ ۲)
۳. نتیجه را با یک رقم اعشار نمایش دهد

---

## مرجع سریع

### خروجی: print()

```python
print(value)                    # چاپ یک مقدار
print(a, b, c)                  # چاپ چند مقدار
print(a, b, sep="-")           # تغییر جداکننده
print(a, end=" ")              # تغییر پایان
print(f"Hello {name}")          # f-string
print(f"Value: {x:.2f}")       # قالب‌بندی
```

### ورودی: input()

```python
text = input("Prompt: ")        # گرفتن رشته
number = int(input("Prompt: ")) # گرفتن عدد صحیح
decimal = float(input("Prompt: ")) # گرفتن عدد اعشاری
```

### قالب‌بندی f-strings

```python
f"{value:.2f}"      # ۲ رقم اعشار
f"{value:05d}"      # ۵ رقم با صفر
f"{value:>10}"      # راست‌چین، عرض ۱۰
f"{value:<10}"      # چپ‌چین، عرض ۱۰
f"{value:,}"        # جداکننده هزارگان
f"{value:.1%}"      # درصد
```

---

## نکات کلیدی

۱. **`print()`** برای نمایش خروجی
۲. **`input()`** همیشه **رشته** برمی‌گرداند - آن را تبدیل کنید!
۳. **f-strings** بهترین روش برای ترکیب متن و متغیر هستند
۴. **`int()`** و **`float()`** برای تبدیل ورودی به عدد
۵. **بررسی خطا** هنگام گرفتن ورودی کاربر مهم است

---

## گام بعدی چیست؟

حالا که می‌دانید چگونه با کاربر تعامل داشته باشید، بیایید درباره تصمیم‌گیری یاد بگیریم:
- **جملات شرطی** - اجرای کد بر اساس شرایط
