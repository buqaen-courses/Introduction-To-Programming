# ورودی-پردازش-خروجی (IPO): بنیان محاسبات

## مقدمه: هر سیستمی از این الگو پیروی می‌کند

برنامه صبحگاهی خود را در نظر بگیرید:
1. **ورودی**: زنگ ساعت به صدا در می‌آید، نور خورشید از پنجره می‌تابد
2. **پردازش**: مغز شما بیدار می‌شود، تصمیم می‌گیرد که وقت بلند شدن است
3. **خروجی**: شما از تخت بیرون می‌آیید

این الگوی ساده - **ورودی → پردازش → خروجی** - بنیان تمام محاسبات است. هر برنامه، هر اپلیکیشن، هر سیستمی از آن پیروی می‌کند.

---

## IPO چیست؟

### سه مؤلفه

```
┌─────────┐      ┌──────────┐      ┌──────────┐
│  INPUT  │  →   │ PROCESS  │  →   │  OUTPUT  │
└─────────┘      └──────────┘      └──────────┘

Input:   داده یا اطلاعاتی که وارد سیستم می‌شود
Process: کاری که روی آن داده انجام می‌شود
Output:  نتایجی که از سیستم خارج می‌شود
```

### مثال‌های دنیای واقعی

#### مثال ۱: دستگاه قهوه‌ساز
```
INPUT:  دانه‌های قهوه، آب، برق، فشار دادن دکمه
PROCESS: آسیاب کردن دانه‌ها → گرم کردن آب → مخلوط کردن → دم کردن
OUTPUT:  قهوه داغ در فنجان شما
```

#### مثال ۲: ماشین حساب
```
INPUT:  ۵، +، ۳، = (فشردن دکمه‌ها)
PROCESS: جمع کردن ۵ و ۳
OUTPUT: صفحه نمایش "۸" را نشان می‌دهد
```

#### مثال ۳: جستجوی گوگل
```
INPUT:  عبارت جستجوی شما "بهترین پیتزا نزدیک من"
PROCESS: جستجوی پایگاه داده → رتبه‌بندی نتایج → قالب‌بندی صفحه
OUTPUT:  لیستی از پیتزا فروشی‌ها روی صفحه شما
```

---

## درک هر مؤلفه

### ۱. ورودی: دریافت داده به سیستم

#### انواع ورودی

| نوع | توضیحات | مثال‌ها |
|------|-------------|----------|
| **ورودی کاربر** | از افراد | تایپ کردن، کلیک کردن، صحبت کردن |
| **ورودی فایل** | از حافظه | خواندن اسناد، تصاویر |
| **ورودی سنسور** | از دستگاه‌ها | دما، GPS، دوربین |
| **ورودی شبکه** | از اینترنت | فراخوانی API، دانلود |
| **ورودی پایگاه داده** | از حافظه | نتایج پرس‌وجو |

#### مثال‌های ورودی در برنامه‌نویسی

```python
# ورودی کاربر - پرسیدن یک سوال
name = input("What is your name? ")
# کاربر تایپ می‌کند: "Alice"
# name now contains: "Alice"

# ورودی فایل - خواندن داده
with open("data.txt", "r") as file:
    content = file.read()
# content now has the file's text

# ورودی سنسور (شبیه‌سازی شده)
temperature = 72.5  # From temperature sensor
```

#### اصول خوب ورودی

1. **درخواست واضح** - به کاربران بگویید چه می‌خواهید
2. **اعتبارسنجی** - بررسی کنید ورودی منطقی باشد
3. **مدیریت خطا** - با ورودی نامعتبر به‌خوبی برخورد کنید

```python
# خوب: درخواست واضح و اعتبارسنجی
while True:
    age_str = input("Enter your age (0-120): ")
    
    # اعتبارسنجی
    if age_str.isdigit():
        age = int(age_str)
        if 0 <= age <= 120:
            break
    
    print("Invalid age. Please try again.")
```

---

### ۲. پردازش: تبدیل داده

#### در پردازش چه اتفاقی می‌افتد؟

پردازش جایی است که "فکر کردن" اتفاق می‌افتد:
- **محاسبات**: عملیات ریاضی
- **تصمیم‌گیری**: اگر این، آن‌گاه آن
- **تبدیلات**: تغییر قالب، فیلتر کردن
- **حلقه‌ها**: انجام کاری به صورت تکراری
- **ذخیره‌سازی**: به خاطر سپردن اطلاعات

#### مثال‌های پردازش

```python
# فرآیند محاسبه
def calculate_area(length, width):
    area = length * width  # عملیات ریاضی
    return area

# فرآیند تصمیم‌گیری
def check_grade(score):
    if score >= 60:       # تصمیم
        return "Pass"
    else:
        return "Fail"

# فرآیند تبدیل
def clean_phone_number(phone):
    # حذف کاراکترهای غیرعددی
    digits_only = "".join(c for c in phone if c.isdigit())
    return digits_only

# فرآیند حلقه
def calculate_average(scores):
    total = 0
    for score in scores:  # حلقه
        total += score
    return total / len(scores)
```

#### الگوهای پردازش

| الگو | توضیحات | مثال |
|---------|-------------|---------|
| **اعتبارسنجی** | بررسی صحت ورودی | آیا قالب ایمیل درست است؟ |
| **تبدیل** | تغییر قالب | تبدیل به حروف بزرگ |
| **تجمیع** | ترکیب مقادیر چندگانه | محاسبه میانگین |
| **جستجو** | یافتن داده خاص | جستجوی کاربر با شناسه |
| **فیلتر** | نگه داشتن بعضی، حذف بقیه | فقط بزرگسالان |
| **مرتب‌سازی** | قرار دادن به ترتیب | لیست الفبایی |

---

### ۳. خروجی: تولید نتایج

#### انواع خروجی

| نوع | توضیحات | مثال‌ها |
|------|-------------|----------|
| **خروجی صفحه** | نمایش روی مانیتور | متن، گرافیک، ویدیو |
| **خروجی فایل** | ذخیره در حافظه | اسناد، صفحات گسترده |
| **خروجی شبکه** | ارسال روی اینترنت | ایمیل، پاسخ API |
| **خروجی فیزیکی** | عمل واقعی در دنیای واقعی | چاپ، صدا، حرکت ربات |

#### مثال‌های خروجی در برنامه‌نویسی

```python
# خروجی صفحه
print("Hello, World!")
print(f"Your score is: {score}")

# خروجی فایل
with open("results.txt", "w") as file:
    file.write("Processing complete\n")

# خروجی‌های چندگانه
def analyze_data(data):
    result = process(data)
    print(f"Result: {result}")        # خروجی صفحه
    save_to_file(result)               # خروجی فایل
    return result                      # بازگشت به فراخوان
```

#### اصول خوب خروجی

1. **واضح باشد** - کاربران باید خروجی را درک کنند
2. **کامل باشد** - شامل تمام اطلاعات لازم
3. **قالب‌بندی زیبا** - خوانا باشد

```python
# قالب‌بندی خوب خروجی
def generate_report(name, scores):
    average = sum(scores) / len(scores)
    
    print("=" * 40)
    print(f"REPORT CARD")
    print("=" * 40)
    print(f"Student: {name}")
    print(f"Scores: {scores}")
    print(f"Average: {average:.1f}")
    print("=" * 40)

# استفاده
generate_report("Alice", [85, 92, 78, 96])
```

خروجی:
```
========================================
REPORT CARD
========================================
Student: Alice
Scores: [85, 92, 78, 96]
Average: 87.8
========================================
```

---

## IPO در برنامه‌نویسی

### مثال کامل برنامه

```python
def main():
    # ========== فاز ورودی ==========
    print("Welcome to the Grade Calculator")
    name = input("Enter student name: ")
    
    # دریافت نمرات چندگانه
    scores = []
    for i in range(3):
        while True:
            score_str = input(f"Enter score {i+1}: ")
            if score_str.isdigit():
                score = int(score_str)
                if 0 <= score <= 100:
                    scores.append(score)
                    break
            print("Invalid score. Enter 0-100.")
    
    # ========== فاز پردازش ==========
    # محاسبه میانگین
    average = sum(scores) / len(scores)
    
    # تعیین نمره
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
    
    # تعیین قبول/مردود
    status = "Pass" if average >= 60 else "Fail"
    
    # ========== فاز خروجی ==========
    print("\n" + "=" * 40)
    print(f"RESULTS FOR: {name}")
    print("=" * 40)
    print(f"Scores: {scores}")
    print(f"Average: {average:.1f}")
    print(f"Grade: {grade}")
    print(f"Status: {status}")
    print("=" * 40)

# اجرای برنامه
main()
```

### توابع به عنوان سیستم‌های کوچک IPO

هر تابع از IPO پیروی می‌کند:

```python
def calculate_circle_area(radius):
    """
    ورودی: radius (یک عدد)
    پردازش: مساحت = π × r²
    خروجی: مساحت (یک عدد)
    """
    import math
    area = math.pi * radius ** 2
    return area

def format_name(first_name, last_name):
    """
    ورودی: first_name, last_name (دو رشته)
    پردازش: ترکیب با فاصله، بزرگ‌نویسی
    خروجی: نام قالب‌بندی شده (یک رشته)
    """
    full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
    return full_name
```

---

## الگوهای IPO در زندگی واقعی

### الگوی ۱: سیستم اعتبارسنجی داده

```
ورودی: داده خام کاربر
پردازش: بررسی قالب، بازه، کامل بودن
خروجی: داده معتبر یا پیام خطا
```

```python
def validate_email(email):
    # ورودی: رشته ایمیل
    # پردازش: بررسی قالب
    if "@" not in email:
        return False, "Email must contain @"
    if "." not in email.split("@")[1]:
        return False, "Email must contain domain"
    # خروجی: (is_valid, message)
    return True, "Email is valid"
```

### الگوی ۲: خط لوله تبدیل داده

```
ورودی: داده در قالب A
پردازش: تبدیل به قالب B (احتمالاً چند مرحله)
خروجی: داده در قالب B
```

```python
def process_customer_data(raw_data):
    # ورودی: رشته CSV خام
    # پردازش: تجزیه، پاکسازی، اعتبارسنجی، قالب‌بندی
    lines = raw_data.split("\n")
    customers = []
    for line in lines:
        fields = line.split(",")
        customer = {
            "id": clean_id(fields[0]),
            "name": clean_name(fields[1]),
            "email": validate_email(fields[2]),
            "phone": format_phone(fields[3])
        }
        customers.append(customer)
    # خروجی: لیستی از دیکشنری‌های مشتری
    return customers
```

### الگوی ۳: الگوی تجمیع

```
ورودی: مجموعه‌ای از آیتم‌ها
پردازش: پردازش هر آیتم، تجمیع نتایج
خروجی: خلاصه/نتیجه ترکیبی
```

```python
def calculate_class_statistics(all_scores):
    # ورودی: لیست تمام نمرات دانشجویان
    # پردازش: آمار تجمیعی
    total_score = sum(all_scores)
    count = len(all_scores)
    average = total_score / count
    highest = max(all_scores)
    lowest = min(all_scores)
    
    # خروجی: دیکشنری آمار
    return {
        "count": count,
        "average": average,
        "highest": highest,
        "lowest": lowest
    }
```

---

## مدیریت خطا در IPO

### خطاهای ورودی

```python
def safe_input_number(prompt, min_val, max_val):
    """دریافت عدد از کاربر با اعتبارسنجی."""
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}")
        except ValueError:
            print("That's not a valid number. Try again.")

# استفاده
temperature = safe_input_number("Enter temperature (0-100): ", 0, 100)
```

### خطاهای پردازش

```python
def safe_divide(a, b):
    """تقسیم دو عدد به‌صورت امن."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Both values must be numbers"

# استفاده
print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # پیام خطا
print(safe_divide(10, "a")) # پیام خطا
```

### مثال کامل مدیریت خطا

```python
def process_file(filename):
    """پردازش فایل با مدیریت خطای جامع."""
    try:
        # ورودی
        with open(filename, "r") as file:
            content = file.read()
        
        # پردازش
        lines = content.split("\n")
        word_count = sum(len(line.split()) for line in lines)
        
        # خروجی
        return f"File has {len(lines)} lines and {word_count} words"
        
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except PermissionError:
        return f"Error: No permission to read '{filename}'"
    except Exception as e:
        return f"Error: {str(e)}"
```

---

## نمودارهای IPO بصری

### ماشین حساب ساده

```
┌─────────────────────────────────────────────┐
│                   ورودی                      │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐      │
│  │ Number 1│  │ Operator│  │ Number 2│      │
│  │   10    │  │    +    │  │    5    │      │
│  └─────────┘  └─────────┘  └─────────┘      │
└─────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────┐
│                  پردازش                      │
│                                             │
│   IF operator is "+":                       │
│      result = 10 + 5 = 15                  │
│                                             │
└─────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────┐
│                   خروجی                      │
│                                             │
│           ┌──────────────┐                  │
│           │  Result: 15  │                  │
│           └──────────────┘                  │
│                                             │
└─────────────────────────────────────────────┘
```

### سیستم ورود

```
ورودی                       پردازش                    خروجی
─────────────────────────────────────────────────────────────
Username: "alice"  →    Check database       →   Success:
Password: "secret"       Verify password          "Welcome!"
                         Match found

                                                    یا

                                              Failure:
                                                 "Invalid
                                                  login"
```

---

## تمرین‌های عملی

### تمرین ۱: شناسایی مؤلفه‌های IPO

برای هر سناریو، ورودی، پردازش و خروجی را مشخص کنید:

1. **برداشت از خودپرداز**
2. **سفارش غذای آنلاین**
3. **فیلتر اسپم ایمیل**
4. **اپلیکیشن تبدیل دما**

### تمرین ۲: طراحی یک سیستم IPO

یک سیستم IPO برای **امانت کتاب از کتابخانه** طراحی کنید:

```
ورودی:  
_________________________________
_________________________________

پردازش:
_________________________________
_________________________________
_________________________________

خروجی:
_________________________________
_________________________________
```

### تمرین ۳: نوشتن یک برنامه IPO کامل

یک برنامه پایتون بنویسید که:
- **ورودی**: لیستی از اعداد را از کاربر دریافت کند
- **پردازش**: مجموع، میانگین، حداقل، حداکثر را محاسبه کند
- **خروجی**: گزارشی قالب‌بندی شده نمایش دهد

### تمرین ۴: مدیریت خطا

مدیریت خطا را به برنامه خود اضافه کنید برای:
- ورودی خالی
- اعداد نامعتبر
- تقسیم بر صفر (هنگام محاسبه میانگین لیست خالی)

---

## نکات کلیدی

1. **IPO جهانی است**: هر سیستمی از ورودی → پردازش → خروجی پیروی می‌کند
2. **ورودی می‌تواند از منابع زیادی بیاید**: کاربران، فایل‌ها، سنسورها، شبکه‌ها
3. **پردازش جایی است که کار انجام می‌شود**: محاسبات، تصمیم‌گیری، تبدیلات
4. **خروجی باید واضح و مفید باشد**: برای مخاطب خود قالب‌بندی کنید
5. **مدیریت خطا حیاتی است**: برای ورودی نامعتبر و خطاهای پردازش برنامه‌ریزی کنید

## به خاطر بسپارید

```
┌─────────────────────────────────────────────────────┐
│                    الگوی IPO                      │
├─────────────────────────────────────────────────────┤
│                                                     │
│   ورودی → [اعتبارسنجی] → پردازش → [قالب‌بندی]   │
│                                                     │
│   ↓                                              →  │
│   داده وارد     تبدیل داده    نتایج خارج       │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### سوالات برای پرسیدن هنگام طراحی

1. **چه ورودی‌هایی نیاز دارم؟** (کاربر چه داده‌ای باید ارائه دهد؟)
2. **چه پردازشی لازم است؟** (چگونه داده را تبدیل کنم؟)
3. **چه خروجی باید تولید کنم؟** (کاربر چه چیزی خواهد دید؟)
4. **چه چیزی می‌تواند اشتباه شود؟** (چگونه خطاها را مدیریت کنم؟)

---

## گام‌های بعدی

- درباره روش‌های مختلف ورودی بیاموزید (GUI، فایل I/O، APIها)
- مدیریت وضعیت در پردازش را مطالعه کنید
- فرمت‌های مختلف خروجی را بررسی کنید (گزارش‌ها، تجسم‌سازی)
- ورودی مبتنی بر رویداد (اقدامات کاربر) را درک کنید
