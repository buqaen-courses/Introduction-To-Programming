# تعریف تابع: ایجاد بلوک‌های کد قابل استفاده مجدد

## مقدمه‌ای بر توابع

توابع بلوک‌های قابل استفاده مجدد از کد هستند که وظایف خاصی را انجام می‌دهند. آنها به شما اجازه می‌دهند برنامه‌های پیچیده را به قطعات کوچک‌تر و قابل مدیریت تقسیم کنید و کد را سازمان‌دهی شده‌تر، قابل خواندن‌تر و قابل نگهداری‌تر کنید.

## تعریف تابع پایه

### نحو تابع
```python
def function_name():
    """مستندسازی اختیاری که توضیح می‌دهد تابع چه کاری انجام می‌دهد."""
    # بدنه تابع - کدی که اجرا می‌شود
    print("سلام از داخل تابع!")
    return  # دستور بازگشت اختیاری
```

### فراخوانی توابع
```python
# تعریف تابع
def greet_user():
    print("سلام، به برنامه ما خوش آمدید!")

# فراخوانی تابع
greet_user()  # خروجی: سلام، به برنامه ما خوش آمدید!
greet_user()  # می‌توان چندین بار فراخوانی کرد
```

## پارامترهای تابع

### پارامترهای موقعیتی
```python
def greet_person(name):
    """سلام کردن با یک شخص به نام."""
    print(f"سلام، {name}!")

# فراخوانی با آرگومان
greet_person("Alice")   # خروجی: سلام، Alice!
greet_person("Bob")     # خروجی: سلام، Bob!
```

### پارامترهای متعدد
```python
def introduce_person(name, age, city):
    """معرفی یک شخص با جزئیات او."""
    print(f"این {name} است که {age} سال دارد و در {city} زندگی می‌کند.")

introduce_person("Alice", 25, "New York")
introduce_person("Bob", 30, "London")
```

### مقادیر پیش‌فرض پارامترها
```python
def greet_with_time(name, time_of_day="morning"):
    """سلام کردن با زمان روز."""
    print(f"صبح بخیر {time_of_day}, {name}!")

greet_with_time("Alice")                    # صبح بخیر morning, Alice!
greet_with_time("Bob", "afternoon")         # صبح بخیر afternoon, Bob!
greet_with_time("Charlie", "evening")       # صبح بخیر evening, Charlie!
```

### آرگومان‌های کلیدی
```python
def create_profile(name, age, city, profession=None):
    """ایجاد پروفایل کاربر."""
    profile = {
        "name": name,
        "age": age,
        "city": city
    }
    if profession:
        profile["profession"] = profession
    return profile

# استفاده از آرگومان‌های موقعیتی
profile1 = create_profile("Alice", 25, "NYC", "Engineer")

# استفاده از آرگومان‌های کلیدی (قابل خواندن‌تر)
profile2 = create_profile(
    name="Bob",
    age=30,
    city="London",
    profession="Designer"
)

# ترکیب موقعیتی و کلیدی
profile3 = create_profile("Charlie", 35, city="Paris", profession="Artist")
```

## مقادیر بازگشتی

### بازگشت مقادیر تک
```python
def calculate_square(number):
    """بازگشت مربع یک عدد."""
    return number ** 2

result = calculate_square(5)  # result = 25
print(result)                 # خروجی: 25
```

### بازگشت مقادیر متعدد
```python
def get_user_info():
    """بازگشت چندین قطعه اطلاعات."""
    name = "Alice"
    age = 25
    city = "New York"
    return name, age, city

# باز کردن تاپل بازگشتی
user_name, user_age, user_city = get_user_info()
print(f"{user_name} {user_age} سال دارد و در {user_city} زندگی می‌کند")

# یا دریافت به عنوان یک تاپل واحد
info = get_user_info()
print(info)  # ('Alice', 25, 'New York')
```

### بازگشت‌های زودهنگام
```python
def divide_numbers(a, b):
    """تقسیم دو عدد با بررسی خطا."""
    if b == 0:
        return "خطا: نمی‌توان بر صفر تقسیم کرد"

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "خطا: هر دو آرگومان باید عدد باشند"

    return a / b

print(divide_numbers(10, 2))      # 5.0
print(divide_numbers(10, 0))      # خطا: نمی‌توان بر صفر تقسیم کرد
print(divide_numbers(10, "2"))    # خطا: هر دو آرگومان باید عدد باشند
```

## دامنه و متغیرهای تابع

### دامنه محلی در برابر جهانی
```python
# متغیر جهانی
global_counter = 0

def increment_counter():
    """افزایش شمارنده جهانی."""
    global global_counter  # اعلام اینکه از متغیر جهانی استفاده می‌کنیم
    global_counter += 1
    print(f"شمارنده اکنون: {global_counter}")

increment_counter()  # شمارنده اکنون: 1
increment_counter()  # شمارنده اکنون: 2

print(global_counter)  # 2 (قابل دسترسی به صورت جهانی)
```

### متغیرهای محلی
```python
def calculate_area(length, width):
    """محاسبه مساحت مستطیل."""
    # متغیرهای محلی فقط داخل این تابع وجود دارند
    area = length * width
    perimeter = 2 * (length + width)

    print(f"مساحت: {area}")
    print(f"محیط: {perimeter}")

    return area

result = calculate_area(5, 3)
# داخل تابع: مساحت: 15، محیط: 16

# این متغیرها اینجا قابل دسترسی نیستند
# print(area)  # NameError: name 'area' is not defined
```

### توابع تو در تو و بسته‌ها
```python
def create_multiplier(factor):
    """ایجاد تابعی که بر یک ضریب خاص ضرب می‌کند."""
    def multiplier(number):
        return number * factor
    return multiplier

# ایجاد توابع ضرب‌کننده تخصصی
double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15

# متغیر ضریب "بسته شده" و به یاد سپرده می‌شود
print(double(10)) # 20
```

## پارامترهای پیشرفته تابع

### آرگومان‌های طول متغیر (*args)
```python
def sum_all(*numbers):
    """جمع هر تعداد آرگومان."""
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))        # 6
print(sum_all(10, 20, 30, 40)) # 100
print(sum_all())               # 0 (بدون آرگومان)
```

### آرگومان‌های کلیدی طول متغیر (**kwargs)
```python
def create_person(**info):
    """ایجاد دیکشنری شخص از آرگومان‌های کلیدی."""
    person = {}
    for key, value in info.items():
        person[key] = value
    return person

person1 = create_person(name="Alice", age=25, city="NYC")
person2 = create_person(name="Bob", profession="Engineer", salary=75000)

print(person1)  # {'name': 'Alice', 'age': 25, 'city': 'NYC'}
print(person2)  # {'name': 'Bob', 'profession': 'Engineer', 'salary': 75000}
```

### ترکیب همه انواع پارامترها
```python
def complex_function(required, *args, default="value", **kwargs):
    """تابعی با همه انواع پارامتر."""
    print(f"مورد نیاز: {required}")
    print(f"Args: {args}")
    print(f"پیش‌فرض: {default}")
    print(f"Kwargs: {kwargs}")

complex_function("hello", 1, 2, 3, default="changed", extra="data")
# مورد نیاز: hello
# Args: (1, 2, 3)
# پیش‌فرض: changed
# Kwargs: {'extra': 'data'}
```

## مستندسازی تابع

### رشته‌های مستندسازی
```python
def calculate_bmi(weight_kg, height_m):
    """
    محاسبه شاخص توده بدنی (BMI).

    Args:
        weight_kg (float): وزن به کیلوگرم
        height_m (float): قد به متر

    Returns:
        float: مقدار BMI

    Raises:
        ValueError: اگر وزن یا قد عدد مثبت نباشند

    Example:
        >>> calculate_bmi(70, 1.75)
        22.857142857142858
    """
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("وزن و قد باید اعداد مثبت باشند")

    return weight_kg / (height_m ** 2)

# دسترسی به رشته مستندسازی
print(calculate_bmi.__doc__)

# استفاده از تابع
bmi = calculate_bmi(70, 1.75)
print(f"BMI: {bmi:.1f}")
```

## حاشیه‌نویسی توابع (نکات نوع)

### نکات نوع پایه
```python
def greet_user(name: str, age: int) -> str:
    """سلام کردن با کاربر با نکات نوع."""
    return f"سلام {name}، شما {age} سال دارید!"

# تابع همچنان به طور عادی کار می‌کند
result = greet_user("Alice", 25)
print(result)  # "سلام Alice، شما 25 سال دارید!"
```

### نکات نوع پیشرفته
```python
from typing import List, Dict, Optional, Union

def process_data(data: List[Union[int, float]], config: Dict[str, any] = None) -> Optional[Dict[str, float]]:
    """
    پردازش لیستی از اعداد و بازگشت آمار.

    Args:
        data: لیستی از اعدادی که باید پردازش شوند
        config: دیکشنری تنظیمات اختیاری

    Returns:
        دیکشنری با آمار یا None اگر داده خالی باشد
    """
    if not data:
        return None

    return {
        "count": len(data),
        "sum": sum(data),
        "average": sum(data) / len(data),
        "min": min(data),
        "max": max(data)
    }

# استفاده
result = process_data([1, 2, 3, 4, 5])
print(result)
# {'count': 5, 'sum': 15, 'average': 3.0, 'min': 1, 'max': 5}
```

## بهترین روش‌های تابع

### اصل مسئولیت واحد
```python
# خوب - یک هدف واضح
def validate_email(email: str) -> bool:
    """بررسی اینکه آیا آدرس ایمیل معتبر است."""
    # منطق اعتبار سنجی ایمیل
    pass

def send_welcome_email(email: str) -> bool:
    """ارسال ایمیل خوش‌آمدگویی به کاربر."""
    # منطق ارسال ایمیل
    pass

def register_user(email: str, password: str) -> bool:
    """ثبت‌نام کاربر جدید."""
    if not validate_email(email):
        return False

    # منطق ثبت‌نام
    # ...

    send_welcome_email(email)
    return True

# بد - مسئولیت‌های متعدد
def register_user_bad(email, password):
    """این تابع کارها زیادی انجام می‌دهد."""
    # اعتبار سنجی ایمیل
    # هش کردن رمز عبور
    # ذخیره در پایگاه داده
    # ارسال ایمیل
    # ثبت فعالیت
    pass
```

### نام‌های معنادار و پارامترها
```python
# خوب - واضح و توصیفی
def calculate_monthly_payment(principal: float, annual_rate: float, years: int) -> float:
    """محاسبه پرداخت ماهانه وام مسکن."""

# بد - نامشخص
def calc(x, y, z):
    """این چه چیزی را محاسبه می‌کند؟"""
```

### مدیریت خطا
```python
def safe_divide(dividend: float, divisor: float) -> Union[float, str]:
    """تقسیم امن دو عدد."""
    try:
        if divisor == 0:
            raise ZeroDivisionError("نمی‌توان بر صفر تقسیم کرد")
        return dividend / divisor
    except ZeroDivisionError as e:
        return f"خطا: {e}"
    except TypeError:
        return "خطا: هر دو آرگومان باید عدد باشند"

print(safe_divide(10, 2))     # 5.0
print(safe_divide(10, 0))     # خطا: نمی‌توان بر صفر تقسیم کرد
print(safe_divide(10, "2"))   # خطا: هر دو آرگومان باید عدد باشند
```

## تست و اشکال‌زدایی توابع

### تست واحد توابع
```python
def is_even(number: int) -> bool:
    """بررسی اینکه آیا عدد زوج است."""
    return number % 2 == 0

def test_is_even():
    """تست تابع is_even."""
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True
    assert is_even(-2) == True
    print("همه تست‌ها گذرانده شدند!")

test_is_even()
```

### اشکال‌زدایی توابع
```python
def factorial(n: int) -> int:
    """محاسبه فاکتوریل با اشکال‌زدایی."""
    print(f"محاسبه فاکتوریل {n}")

    if n < 0:
        raise ValueError("فاکتوریل برای اعداد منفی تعریف نشده است")

    result = 1
    for i in range(1, n + 1):
        print(f"  ضرب در {i}: {result} * {i} = {result * i}")
        result *= i

    print(f"نتیجه نهایی: {result}")
    return result

# factorial(5)
```

## ترکیب توابع

### زنجیره کردن توابع
```python
def clean_text(text: str) -> str:
    """پاک‌سازی و استانداردسازی متن."""
    return text.lower().strip()

def extract_words(text: str) -> List[str]:
    """استخراج کلمات از متن."""
    import re
    return re.findall(r'\b\w+\b', text)

def remove_stop_words(words: List[str]) -> List[str]:
    """حذف کلمات ایست متداول."""
    stop_words = {"the", "a", "an", "and", "or", "but", "in", "on", "at"}
    return [word for word in words if word not in stop_words]

# ترکیب توابع
def process_text(text: str) -> List[str]:
    """پردازش متن از طریق چندین تبدیل."""
    cleaned = clean_text(text)
    words = extract_words(cleaned)
    filtered = remove_stop_words(words)
    return filtered

text = "The quick brown fox jumps over the lazy dog"
result = process_text(text)
print(result)  # ['quick', 'brown', 'fox', 'jumps', 'lazy', 'dog']
```

## نکات کلیدی

۱. **توابع بلوک‌های کد قابل استفاده مجدد هستند** که وظایف خاصی را انجام می‌دهند
۲. **پارامترها به توابع اجازه می‌دهند ورودی بپذیرند** در اشکال مختلف
۳. **مقادیر بازگشتی خروجی تابع را فراهم می‌کنند** برای کد فراخوان
۴. **دامنه دسترسی متغیرها را کنترل می‌کند** داخل و خارج توابع
۵. **مستندسازی و نکات نوع** خوانایی و قابلیت نگهداری کد را بهبود می‌بخشند
۶. **اصل مسئولیت واحد** توابع را متمرکز و قابل تست نگه می‌دارد

## مطالعه بیشتر
- مستندات توابع پایتون
- مفاهیم برنامه‌نویسی تابعی
- الگوهای پارامتر پیشرفته
- استراتژی‌های تست توابع
- تکنیک‌های بهینه‌سازی عملکرد