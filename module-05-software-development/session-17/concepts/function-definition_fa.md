# تعریف تابع: ایجاد کد قابل استفاده مجدد

## تابع چیست؟

**تابع** یک بلوک کد قابل استفاده مجدد است که یک کار مشخص را انجام می‌دهد. آن را مانند یک برنامه کوچک در داخل برنامه‌ی خود در نظر بگیرید - به آن ورودی می‌دهید، کار انجام می‌دهد و (در صورت نیاز) نتیجه را به شما برمی‌گرداند.

### تشبیه دنیای واقعی

توابع مانند لوازم خانگی آشپزخانه هستند:
- **توستر**: نان می‌گذارید → نان برشته می‌گیرید
- **مخلوط‌کن**: مواد می‌گذارید → اسموتی می‌گیرید
- **تابع**: داده می‌دهید → نتیجه می‌گیرید

### چرا از توابع استفاده کنیم؟

1. **قابلیت استفاده مجدد**: یک بار بنویسید، بارها استفاده کنید
2. **سازماندهی**: مسائل بزرگ را به قطعات کوچکتر تقسیم کنید
3. **خوانایی**: به عملیات پیچیده نام‌های معنادار بدهید
4. **تست‌پذیری**: قطعات کوچک را به صورت مستقل تست کنید
5. **همکاری**: افراد مختلف می‌توانند روی توابع مختلف کار کنند

---

## سینتکس پایه تابع

### تعریف یک تابع ساده

```python
# تعریف تابع
def say_hello():
    """این یک داک‌استرینگ است - توضیح می‌دهد تابع چه می‌کند."""
    print("Hello, World!")

# فراخوانی تابع (استفاده از تابع)
say_hello()
say_hello()
```

### آناتومی تابع

```
def function_name():
    """مستندات (اختیاری اما توصیه شده)"""
    # بدنه تابع
    # کدی که هنگام فراخوانی اجرا می‌شود
    return  # اختیاری - مقداری را برمی‌گرداند
```

| بخش | هدف | مثال |
|------|---------|---------|
| `def` | به پایتون می‌گوید در حال تعریف تابع هستید | `def` |
| `function_name` | نحوه فراخوانی تابع | `say_hello` |
| `()` | پارامترها (ورودی‌ها) را نگه می‌دارد | `(name, age)` |
| `:` | خط تعریف را تمام می‌کند | `:` |
| تورفتگی | کد داخل تابع را مشخص می‌کند | 4 فاصله |
| داک‌استرینگ | توضیح می‌دهد تابع چه می‌کند | `"""سلام می‌دهد"""` |
| `return` | نتیجه را برمی‌گرداند | `return 42` |

---

## توابع با پارامترها

### پارامتر تک

```python
def greet(name):
    """سلام به یک فرد بر اساس نام."""
    print(f"Hello, {name}!")

# فراخوانی با آرگومان
greet("Alice")    # Output: Hello, Alice!
greet("Bob")      # Output: Hello, Bob!
```

### پارامترهای چندگانه

```python
def introduce(first_name, last_name, age):
    """معرفی یک فرد."""
    print(f"This is {first_name} {last_name}, who is {age} years old.")

# فراخوانی با آرگومان‌های چندگانه (ترتیب مهم است!)
introduce("Alice", "Smith", 25)
# Output: This is Alice Smith, who is 25 years old.
```

**مهم**: آرگومان‌ها باید به همان ترتیب پارامترها ارائه شوند!

### پارامترهای پیش‌فرض

```python
def greet_with_time(name, time="morning"):
    """سلام به کسی با زمان روز."""
    print(f"Good {time}, {name}!")

# فراخوانی با هر دو آرگومان
greet_with_time("Alice", "evening")   # Good evening, Alice!

# فراخوانی فقط با آرگومان الزامی (از پیش‌فرض استفاده می‌کند)
greet_with_time("Bob")                 # Good morning, Bob!

# فراخوانی با آرگومان‌های کلیدی‌واژه‌ای
greet_with_time("Charlie", time="afternoon")  # Good afternoon, Charlie!
```

**بهترین تمرین**: پارامترهای پیش‌فرض را بعد از پارامترهای الزامی قرار دهید!

```python
# غلط
def wrong_order(time="morning", name):
    pass  # SyntaxError!

# درست
def correct_order(name, time="morning"):
    pass  # کار می‌کند!
```

---

## برگرداندن مقادیر

### برگرداندن یک مقدار

```python
def calculate_square(number):
    """مربع یک عدد را برمی‌گرداند."""
    result = number ** 2
    return result

# دریافت مقدار برگشتی
answer = calculate_square(5)
print(answer)        # 25

# استفاده مستقیم در عبارت
total = calculate_square(3) + calculate_square(4)
print(total)        # 9 + 16 = 25
```

### برگرداندن مقادیر چندگانه

```python
def get_circle_info(radius):
    """مساحت و محیط دایره را برمی‌گرداند."""
    import math
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

# باز کردن مقادیر برگشتی چندگانه
area, circumference = get_circle_info(5)
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")

# یا دریافت به صورت تاپل
result = get_circle_info(5)
print(result)        # (78.54..., 31.41...)
```

### بازگشت زودهنگام (Early Returns)

```python
def divide_safely(a, b):
    """تقسیم دو عدد با بررسی خطا."""
    # ابتدا بررسی تقسیم بر صفر
    if b == 0:
        return "Error: Cannot divide by zero"

    # بررسی انواع معتبر
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Error: Both must be numbers"

    # اگر به اینجا رسیدیم، ورودی‌ها معتبر هستند
    return a / b

# تست
print(divide_safely(10, 2))      # 5.0
print(divide_safely(10, 0))      # پیام خطا
print(divide_safely(10, "2"))    # پیام خطا
```

---

## دامنه متغیر: محلی در مقابل سراسری

### متغیرهای محلی (داخل تابع)

```python
def calculate_area(length, width):
    """محاسبه مساحت مستطیل."""
    area = length * width   # 'area' در این تابع محلی است
    return area

result = calculate_area(5, 3)
print(result)           # 15

# این باعث خطا می‌شود:
# print(area)           # NameError! 'area' اینجا تعریف نشده است
```

متغیرهای ایجاد شده داخل یک تابع فقط داخل آن تابع وجود دارند!

### متغیرهای سراسری (خارج تابع)

```python
# متغیر سراسری
counter = 0

def increment():
    """افزایش شمارنده سراسری."""
    global counter          # به پایتون می‌گوییم منظورمان متغیر سراسری است
    counter += 1
    print(f"Counter is now: {counter}")

increment()     # Counter is now: 1
increment()     # Counter is now: 2
print(counter)  # 2
```

**بهترین تمرین**: تا حد امکان از متغیرهای سراسلی اجتناب کنید. داده‌ها را به عنوان پارامتر منتقل کنید!

### جایگزین بهتر برای متغیرهای سراسلی

```python
# به جای حالت سراسلی، مقادیر را منتقل و برگردانید
def increment_counter(current):
    """برگرداندن شمارنده افزایش یافته."""
    return current + 1

# استفاده
counter = 0
counter = increment_counter(counter)   # 1
counter = increment_counter(counter)   # 2
```

---

## مستندسازی توابع

### داک‌استرینگ‌ها

```python
def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index (BMI).

    Parameters:
        weight_kg (float): وزن به کیلوگرم
        height_m (float): قد به متر

    Returns:
        float: مقدار BMI

    Raises:
        ValueError: اگر وزن یا قد مثبت نباشند

    Example:
        >>> calculate_bmi(70, 1.75)
        22.86
    """
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Weight and height must be positive")

    return weight_kg / (height_m ** 2)

# دسترسی به داک‌استرینگ
print(calculate_bmi.__doc__)
```

### تایپ هینت (اختیاری اما مفید)

```python
def greet(name: str, age: int) -> str:
    """
    ایجاد پیام خوش‌آمدگویی.

    Args:
        name: نام فرد
        age: سن فرد

    Returns:
        رشته خوش‌آمدگویی قالب‌بندی شده
    """
    return f"Hello {name}, you are {age} years old!"

# تایپ هینت‌ها انواع را اجبار نمی‌کنند، اما به:
# - مستندسازی
# - تکمیل خودکار IDE
# - خوانایی کد
# کمک می‌کنند
```

---

## مثال‌های کاربردی

### مثال ۱: اعتبارسنج ورودی

```python
def get_valid_number(prompt, min_value=None, max_value=None):
    """
    دریافت یک عدد معتبر از کاربر.

    Args:
        prompt: پیام برای نمایش به کاربر
        min_value: حداقل مقدار مجاز
        max_value: حداکثر مقدار مجاز

    Returns:
        عدد معتبر
    """
    while True:
        try:
            value = float(input(prompt))

            if min_value is not None and value < min_value:
                print(f"Please enter a value >= {min_value}")
                continue

            if max_value is not None and value > max_value:
                print(f"Please enter a value <= {max_value}")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")

# استفاده
age = get_valid_number("Enter your age: ", min_value=0, max_value=150)
```

### مثال ۲: محاسبه‌گر نمره

```python
def calculate_letter_grade(score):
    """
    تبدیل نمره عددی به نمره حرفی.

    Args:
        score: نمره عددی (۰-۱۰۰)

    Returns:
        نمره حرفی (A, B, C, D, F)
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def calculate_statistics(grades):
    """
    محاسبه آمار نمرات.

    Args:
        grades: لیست نمرات عددی

    Returns:
        دیکشنری با آمار
    """
    if not grades:
        return None

    return {
        "count": len(grades),
        "average": sum(grades) / len(grades),
        "highest": max(grades),
        "lowest": min(grades),
        "letter_grades": [calculate_letter_grade(g) for g in grades]
    }

# استفاده
scores = [85, 92, 78, 96, 88]
stats = calculate_statistics(scores)
print(f"Average: {stats['average']:.1f}")
print(f"Grades: {', '.join(stats['letter_grades'])}")
```

### مثال ۳: تولیدکننده رمز عبور

```python
import random
import string

def generate_password(length=12, use_upper=True, use_numbers=True, use_special=True):
    """
    تولید یک رمز عبور تصادفی.

    Args:
        length: طول رمز عبور
        use_upper: شامل حروف بزرگ
        use_numbers: شامل اعداد
        use_special: شامل کاراکترهای خاص

    Returns:
        رشته رمز عبور تولید شده
    """
    chars = string.ascii_lowercase

    if use_upper:
        chars += string.ascii_uppercase
    if use_numbers:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    return ''.join(random.choice(chars) for _ in range(length))

# استفاده
print(generate_password())                    # پیش‌فرض ۱۲ کاراکتر
print(generate_password(16, use_special=False))  # ۱۶ کاراکتر، بدون کاراکتر خاص
```

### مثال ۴: سیستم منو

```python
def show_menu(options):
    """
    نمایش یک منو و دریافت انتخاب کاربر.

    Args:
        options: دیکشنری {شماره_انتخاب: توضیحات}

    Returns:
        انتخاب کاربر به عنوان رشته
    """
    print("\n" + "="*30)
    for num, desc in options.items():
        print(f"{num}. {desc}")
    print("="*30)

    while True:
        choice = input("Enter your choice: ")
        if choice in options:
            return choice
        print("Invalid choice. Please try again.")

# استفاده
options = {
    "1": "View balance",
    "2": "Deposit money",
    "3": "Withdraw money",
    "4": "Exit"
}

# برای اجرا از حالت توضیح خارج کنید:
# choice = show_menu(options)
# print(f"You chose: {options[choice]}")
```

---

## اشتباهات رایج مبتدی‌ها

### اشتباه ۱: فراموش کردن فراخوانی تابع

```python
def say_hello():
    print("Hello!")

# غلط - فقط به تابع اشاره می‌کند، فراخوانی نمی‌کند
say_hello

# درست - واقعاً تابع را فراخوانی می‌کند
say_hello()
```

### اشتباه ۲: فراموش کردن `return`

```python
# غلط - نتیجه را برنمی‌گرداند
def add(a, b):
    result = a + b   # محاسبه می‌کند اما برنمی‌گرداند!

answer = add(2, 3)
print(answer)        # None

# درست
def add(a, b):
    return a + b

answer = add(2, 3)
print(answer)        # 5
```

### اشتباه ۳: تغییر سراسلی بدون اعلام

```python
counter = 0

# غلط
def increment():
    counter += 1     # UnboundLocalError!

# درست
def increment():
    global counter
    counter += 1

# بهتر - اجتناب از سراسری
def increment(current):
    return current + 1
```

### اشتباه ۴: تعداد اشتباه آرگومان‌ها

```python
def greet(first, last):
    print(f"Hello {first} {last}")

# غلط - آرگومان کم
greet("Alice")       # TypeError!

# غلط - آرگومان زیاد
greet("Alice", "Smith", "Extra")  # TypeError!

# درست
greet("Alice", "Smith")

# یا استفاده از آرگومان‌های کلیدی‌واژه‌ای
greet(last="Smith", first="Alice")
```

---

## تمرین‌های عملی

### تمرین ۱: مبدل دما

توابعی برای تبدیل بین سانتیگراد و فارنهایت ایجاد کنید.

```python
def celsius_to_fahrenheit(celsius):
    """تبدیل سانتیگراد به فارنهایت."""
    # کد شما اینجا
    pass

def fahrenheit_to_celsius(fahrenheit):
    """تبدیل فارنهایت به سانتیگراد."""
    # کد شما اینجا
    pass

# تست
print(celsius_to_fahrenheit(0))      # باید ۳۲.۰ باشد
print(celsius_to_fahrenheit(100))    # باید ۲۱۲.۰ باشد
print(fahrenheit_to_celsius(32))     # باید ۰.۰ باشد
print(fahrenheit_to_celsius(212))    # باید ۱۰۰.۰ باشد
```

### تمرین ۲: تحلیل‌گر اعداد

تابعی ایجاد کنید که آمار یک لیست اعداد را برمی‌گرداند.

```python
def analyze_numbers(numbers):
    """
    دیکشنری با تعداد، مجموع، میانگین، حداقل، حداکثر اعداد برمی‌گرداند.
    اگر لیست خالی است None برمی‌گرداند.
    """
    # کد شما اینجا
    pass

# تست
result = analyze_numbers([1, 2, 3, 4, 5])
# باید چیزی شبیه به: {'count': 5, 'sum': 15, 'average': 3.0, 'min': 1, 'max': 5} برمی‌گرداند
```

### تمرین ۳: ماشین‌حساب ساده

تابع ماشین‌حسابی ایجاد کنید که دو عدد و یک عملیات دریافت می‌کند.

```python
def calculator(a, b, operation):
    """
    انجام عملیات روی a و b.
    operation: 'add', 'subtract', 'multiply', 'divide'
    پیام خطا برای عملیات نامعتبر یا تقسیم بر صفر برمی‌گرداند.
    """
    # کد شما اینجا
    pass

# تست
print(calculator(10, 5, 'add'))       # 15
print(calculator(10, 5, 'divide'))    # 2.0
print(calculator(10, 0, 'divide'))    # پیام خطا
print(calculator(10, 5, 'unknown'))   # پیام خطا
```

### تمرین ۴: بررسی‌کننده کلمات متقارن

تابعی ایجاد کنید که بررسی می‌کند آیا یک کلمه متقارن است.

```python
def is_palindrome(word):
    """
    True برمی‌گرداند اگر کلمه متقارن باشد (از هر دو طرف یکسان خوانده می‌شود).
    حروف بزرگ و کاراکترهای غیرالفبایی را نادیده می‌گیرد.
    """
    # کد شما اینجا
    pass

# تست
print(is_palindrome("radar"))         # True
print(is_palindrome("A man a plan a canal Panama"))  # True (نادیده گرفتن فاصله‌ها)
print(is_palindrome("hello"))         # False
```

---

## نکات کلیدی

1. **توابع کد قابل استفاده مجدد را بسته‌بندی می‌کنند** - یک بار تعریف، بارها فراخوانی
2. **پارامترها ورودی را دریافت می‌کنند** - داده از طریق پارامترها وارد می‌شود
3. **return خروجی را برمی‌گرداند** - از `return` برای دادن نتایج به فراخوان استفاده کنید
4. **متغیرها به طور پیش‌فرض محلی هستند** - فضای نام سراسلی را آلوده نکنید
5. **توابع خود را مستند کنید** - از داک‌استرینگ‌ها برای توضیح استفاده کنید
6. **یک تابع = یک کار** - توابع را متمرکز و ساده نگه دارید

## کارت مرجع سریع

| کار | سینتکس | مثال |
|------|--------|---------|
| تعریف تابع | `def name():` | `def greet():` |
| با پارامترها | `def name(p1, p2):` | `def greet(name, age):` |
| با پیش‌فرض‌ها | `def name(p1="default"):` | `def greet(name, time="morning"):` |
| برگرداندن مقدار | `return value` | `return a + b` |
| فراخوانی تابع | `name()` | `greet()` |
| با آرگومان‌ها | `name(arg1, arg2)` | `greet("Alice", 25)` |
| با کلیدی‌واژه‌ها | `name(p1=val1)` | `greet(name="Alice")` |
| دسترسی به داک‌استرینگ | `function.__doc__` | `print(greet.__doc__)` |

---

## مطالعه بیشتر

- **درس بعدی**: پارامترهای تابع - مدیریت پیشرفته آرگومان‌ها
- **تمرین**: تمام تمرین‌های بالا را کامل کنید
- **چالش**: یک کتابخانه کوچک از توابع کمکی برای کارهای رایج ایجاد کنید
- **کاوش**: درباره توابع لامبدا یاد بگیرید (توابع ناشناس کوچک)
