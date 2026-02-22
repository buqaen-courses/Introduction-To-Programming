# جملات شرطی در پایتون

## آنچه خواهید آموخت
- چگونه برنامه شما تصمیم بگیرد
- چگونه کد را بر اساس شرایط اجرا کنید
- نحوه مدیریت سناریوهای مختلف

---

## چرا جملات شرطی نیاز داریم؟

برنامه‌های کامپیوتری باید **تصمیم بگیرند**. بسته به شرایط، کارهای مختلفی انجام می‌دهند.

### تشبیه: چراغ راهنمایی

```
┌─────────────────────────────────────┐
│           چراغ راهنمایی            │
├─────────────────────────────────────┤
│  اگر قرمز: توقف                    │
│  اگر زرد: آماده شوید               │
│  اگر سبز: حرکت کنید                │
└─────────────────────────────────────┘
```

در برنامه‌نویسی هم همینطور است:
- اگر کاربر وارد شده: داشبورد را نشان بده
- اگر نه: صفحه ورود را نشان بده

---

## if (اگر)

ساده‌ترین شکل تصمیم‌گیری: "اگر این شرط درست است، این کار را انجام بده."

### نحو

```python
if condition:
    # کدی که اگر شرط True باشد اجرا می‌شود
    # (با تورفتگی!)
```

### مثال‌های پایه

```python
# بررسی سن
age = 20

if age >= 18:
    print("You are an adult.")

# بررسی رمز
password = "secret123"

if password == "secret123":
    print("Access granted!")

# بررسی موجودی
balance = 100
withdrawal = 50

if balance >= withdrawal:
    print("Withdrawal successful!")
    balance = balance - withdrawal
    print(f"New balance: ${balance}")
```

### نکته مهم: تورفتگی

در پایتون، **تورفتگی مهم است**!

```python
# ✅ صحیح - تورفتگی ۴ فاصله
if age >= 18:
    print("Adult")         # این در if است
    print("Welcome")       # این هم در if است
print("Done")              # این بیرون if است

# ❌ اشتباه - بدون تورفتگی
if age >= 18:
print("Adult")            # IndentationError!
```

---

## else (وگرنه)

"اگر شرط درست نیست، این کار دیگر را انجام بده."

### نحو

```python
if condition:
    # اگر شرط True باشد
else:
    # اگر شرط False باشد
```

### مثال‌ها

```python
# بررسی سن
age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# بررسی زوج/فرد
number = 7

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

# بررسی ورود
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "secret":
    print("Login successful!")
else:
    print("Invalid credentials.")
```

---

## elif (وگرنه اگر)

بررسی چندین شرط به ترتیب.

### نحو

```python
if condition1:
    # اگر condition1 True باشد
elif condition2:
    # اگر condition1 False و condition2 True باشد
elif condition3:
    # اگر همه قبلی False و condition3 True باشد
else:
    # اگر همه False باشند
```

### مثال: درجه حرارت

```python
temperature = 25

if temperature > 30:
    print("It's hot! ☀️")
    print("Drink water.")
elif temperature > 20:
    print("It's warm. 😊")
elif temperature > 10:
    print("It's cool. 🍂")
else:
    print("It's cold! ❄️")
    print("Wear a jacket.")
```

### مثال: نمره

```python
score = 85

if score >= 90:
    grade = "A"
    message = "Excellent!"
elif score >= 80:
    grade = "B"
    message = "Good job!"
elif score >= 70:
    grade = "C"
    message = "Satisfactory."
elif score >= 60:
    grade = "D"
    message = "Need improvement."
else:
    grade = "F"
    message = "Failed."

print(f"Score: {score}, Grade: {grade}")
print(message)
```

### مثال: ساعت روز

```python
hour = 14  # 2 PM

if hour < 6:
    time_of_day = "Night"
elif hour < 12:
    time_of_day = "Morning"
elif hour < 18:
    time_of_day = "Afternoon"
else:
    time_of_day = "Evening"

print(f"It's {time_of_day}.")
```

---

## شرایط پیچیده

### ترکیب شرایط

```python
age = 25
has_license = True
is_sober = True

if age >= 18 and has_license and is_sober:
    print("You can drive.")
else:
    print("You cannot drive.")
```

### بررسی محدوده

```python
age = 65

# روش ۱
if age >= 18 and age <= 65:
    print("You are in the working age group.")

# روش ۲ (خواناتر)
if 18 <= age <= 65:
    print("You are in the working age group.")
```

### چندین else-if

```python
day = "Saturday"

if day == "Monday":
    activity = "Work meeting"
elif day == "Tuesday":
    activity = "Gym"
elif day == "Wednesday":
    activity = "Project work"
elif day == "Thursday":
    activity = "Team lunch"
elif day == "Friday":
    activity = "Happy hour"
elif day in ["Saturday", "Sunday"]:
    activity = "Weekend fun!"
else:
    activity = "Invalid day"

print(f"{day}: {activity}")
```

---

## ifهای کوتاه (عملگر سه‌گانه)

برای شرایط ساده، از این روش استفاده کنید.

### نحو

```python
value_if_true if condition else value_if_false
```

### مثال‌ها

```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)            # "adult"

# یا در تابع
number = 7
parity = "even" if number % 2 == 0 else "odd"
print(f"{number} is {parity}")

# برای مقدار پیش‌فرض
name = input("Enter name: ") or "Guest"
print(f"Hello, {name}!")
```

---

## if در یک خط

برای دستورات ساده.

```python
# ✅ می‌تواند در یک خط باشد
if age >= 18: print("Adult")

# ✅ یا با else
print("Adult") if age >= 18 else print("Minor")

# ❌ چندین دستور باید تورفته شوند
if age >= 18:
    print("Adult")
    print("Welcome")
```

---

## کاربردهای عملی

### مثال ۱: ماشین حساب ساده

```python
num1 = float(input("First number: "))
operator = input("Operator (+, -, *, /): ")
num2 = float(input("Second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero!"
else:
    result = "Error: Invalid operator!"

print(f"Result: {result}")
```

### مثال ۲: تخفیف فروشگاه

```python
total = float(input("Total purchase: $"))
is_member = input("Are you a member? (yes/no): ").lower() == "yes"

if is_member and total > 100:
    discount = 0.20
    message = "20% member discount applied!"
elif is_member:
    discount = 0.10
    message = "10% member discount applied!"
elif total > 200:
    discount = 0.15
    message = "15% bulk discount applied!"
else:
    discount = 0
    message = "No discount applied."

final = total * (1 - discount)
print(message)
print(f"Final total: ${final:.2f}")
```

### مثال ۳: صدور گواهی سلامت

```python
age = int(input("Age: "))
has_symptoms = input("Any symptoms? (yes/no): ").lower() == "yes"
is_vaccinated = input("Vaccinated? (yes/no): ").lower() == "yes"

if has_symptoms:
    recommendation = "Stay home and rest. Consult a doctor."
elif age >= 65 and not is_vaccinated:
    recommendation = "Please get vaccinated. High risk group."
elif is_vaccinated:
    recommendation = "You're protected! Follow safety guidelines."
else:
    recommendation = "Consider getting vaccinated."

print(f"\nRecommendation: {recommendation}")
```

---

## اشتباهات رایج

### اشتباه ۱: == به جای =

```python
# ❌ اشتباه
if x = 5:               # SyntaxError! تخصیص، نه مقایسه

# ✅ صحیح
if x == 5:              # مقایسه
```

### اشتباه ۲: بدون تورفتگی

```python
# ❌ اشتباه
if x > 0:
print("Positive")       # IndentationError!

# ✅ صحیح
if x > 0:
    print("Positive")
```

### اشتباه ۳: elif بدون if

```python
# ❌ اشتباه
elif x > 0:             # SyntaxError! elif قبل از if نمی‌آید
    print("Positive")

# ✅ صحیح
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
```

### اشتباه ۴: شرط غیربولی

```python
# ⚠️ کار می‌کند اما مبهم است
if x:                   # True اگر x خالی/صفر نباشد

# ✅ صریح و واضح
if x != 0:
if len(items) > 0:
if name != "":
```

### اشتباه ۵: فراموش کردن شرایط لبه

```python
# ⚠️ ممکن است خطا دهد
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
# چه می‌شود اگر score دقیقاً ۷۹.۹ باشد؟
# باید else داشته باشید
```

---

## خودتان امتحان کنید: تمرین‌ها

### تمرین ۱: بررسی عدد

کدی بنویسید که یک عدد بگیرد و بگوید:
- مثبت است یا منفی یا صفر
- زوج است یا فرد

### تمرین ۲: ماشین حساب BMI

کدی بنویسید که BMI را محاسبه و طبقه‌بندی کند:
- زیر ۱۸.۵: کم‌وزن
- ۱۸.۵ تا ۲۴.۹: نرمال
- ۲۵ تا ۲۹.۹: اضافه‌وزن
- ۳۰ و بالاتر: چاق

### تمرین ۳: فصل‌ها

کدی بنویسید که ماه (۱-۱۲) را بگیرد و فصل را بگوید:
- بهار: ۳-۵
- تابستان: ۶-۸
- پاییز: ۹-۱۱
- زمستان: ۱۲، ۱-۲

### تمرین ۴: بازی حدس عدد

```python
import random

secret = random.randint(1, 100)
guess = int(input("Guess a number (1-100): "))

# کد را کامل کنید:
# اگر حدس درست بود: "Correct!"
# اگر حدس کم بود: "Too low!"
# اگر حدس زیاد بود: "Too high!"
```

---

## مرجع سریع

### نحو if-elif-else

```python
if condition:
    # کد
elif another_condition:
    # کد
else:
    # کد
```

### عملگر سه‌گانه

```python
result = value_if_true if condition else value_if_false
```

### الگوهای رایج

```python
# بررسی محدوده
if 18 <= age <= 65:

# بررسی عضویت
if item in list:

# بررسی وجود
if variable:
```

---

## نکات کلیدی

۱. **if** برای شرایط پایه، **elif** برای چندین شرط، **else** برای بقیه
۲. **تورفتگی** در پایتون اجباری است - معمولاً ۴ فاصله
۳. **==** برای مقایسه، **=** برای تخصیص
۴. از **elif** برای چک کردن چندین شرط به ترتیب استفاده کنید
۵. از **عملگر سه‌گانه** برای شرایط ساده استفاده کنید

---

## گام بعدی چیست؟

حالا که با شرایط آشنا شدید، بیایید درباره شرایط تودرتو یاد بگیریم:
- **شرایط تودرتو** - شرایط داخل شرایط
