# خطاهای رایج: پیشگیری و مدیریت اشتباهات برنامه‌نویسی

## مقدمه‌ای بر خطاهای رایج برنامه‌نویسی

خطاهای برنامه‌نویسی اجتناب‌ناپذیر هستند، اما درک الگوهای رایج به توسعه‌دهندگان اجازه می‌دهد کد قوی‌تری بنویسند. این راهنما اشتباهات مکرر و استراتژی‌هایی برای پیشگیری و مدیریت را پوشش می‌دهد.

## خطاهای نحوی

### اشتباهات نحوی رایج
```python
# دو نقطه گم شده
if x > 5
    print("Big")  # SyntaxError: invalid syntax

# تورفتگی نادرست (پایتون سازگاری را نیاز دارد)
def function():
print("Hello")  # IndentationError: expected an indented block

# نقل قول‌های ناهمخوان
message = "Hello, world!  # SyntaxError: EOL while scanning string literal

# استفاده نادرست از عملگر
if x = 5:  # SyntaxError: invalid syntax (تخصیص به جای مقایسه)
    print("Equal")

# پرانتزهای گم شده در فراخوانی توابع
print "Hello"  # SyntaxError: Missing parentheses in call

# نحو دیکشنری نادرست
my_dict = {"key1": "value1" "key2": "value2"}  # SyntaxError: invalid syntax
```

### استراتژی‌های پیشگیری
```python
# از یک linter استفاده کنید (مانند flake8 یا pylint)
# pip install flake8
# flake8 your_file.py

# از IDE با برجسته‌سازی نحو استفاده کنید
# بیشتر ویرایشگرهای مدرن خطاهای نحوی را فوراً می‌گیرند

# کد را در تکه‌های کوچک بنویسید و به طور مکرر تست کنید
# این ایزوله کردن خطاهای نحوی را آسان‌تر می‌کند

def validate_syntax():
    """الگوهای اعتبار سنجی نحو پایه."""
    try:
        # تست کامپایل کد
        code = """
def test_function(x, y):
    if x > y:
        return x
    else:
        return y
"""
        compile(code, '<string>', 'exec')
        print("نحو معتبر است")
    except SyntaxError as e:
        print(f"خطای نحوی: {e}")
        print(f"خط {e.lineno}: {e.text}")
```

## خطاهای زمان اجرا

### خطاهای نوع
```python
# افزودن انواع ناسازگار
result = "Hello" + 5  # TypeError: can only concatenate str (not "int") to str

# فراخوانی متد بر نوع اشتباه
numbers = [1, 2, 3]
numbers.length()  # AttributeError: 'list' object has no attribute 'length'

# آرگومان‌های تابع نادرست
len(5)  # TypeError: object of type 'int' has no len()

# دسترسی به متغیر تعریف نشده
print(undefined_variable)  # NameError: name 'undefined_variable' is not defined
```

### خطاهای مقدار
```python
# تبدیل مقادیر نامعتبر
int("not_a_number")  # ValueError: invalid literal for int()

# دسترسی به شاخص‌های خارج از محدوده
my_list = [1, 2, 3]
my_list[10]  # IndexError: list index out of range

# خطاهای کلید دیکشنری
my_dict = {"a": 1}
my_dict["missing_key"]  # KeyError: 'missing_key'
```

### پیشگیری و مدیریت
```python
def safe_operations():
    """الگوهای عملیات امن را نمایش دهید."""

    # تبدیل نوع امن
    def safe_int(value, default=0):
        try:
            return int(value)
        except (ValueError, TypeError):
            return default

    # دسترسی امن لیست
    def safe_list_get(lst, index, default=None):
        try:
            return lst[index]
        except IndexError:
            return default

    # دسترسی امن دیکشنری
    def safe_dict_get(dct, key, default=None):
        return dct.get(key, default)

    # استفاده
    print(safe_int("42"))          # 42
    print(safe_int("not_number"))  # 0 (پیش‌فرض)
    print(safe_list_get([1,2,3], 5, "not found"))  # "not found"
    print(safe_dict_get({"a": 1}, "b", "missing"))  # "missing"
```

## خطاهای منطقی

### خطاهای یک-تا-کم یا یک-تا-زیاد
```python
# اشتباهات رایج حلقه
numbers = [1, 2, 3, 4, 5]

# اشتباه: شاخص 5 را شامل می‌شود که وجود ندارد
for i in range(len(numbers) + 1):  # range(6) -> 0,1,2,3,4,5
    print(numbers[i])  # IndexError در i=5

# اشتباه: عنصر آخر را حذف می‌کند
for i in range(len(numbers) - 1):  # range(4) -> 0,1,2,3
    print(numbers[i])  # عنصر در شاخص 4 را از دست می‌دهد

# درست
for i in range(len(numbers)):  # range(5) -> 0,1,2,3,4
    print(numbers[i])

# بهتر: از enumerate استفاده کنید یا مستقیماً پیمایش کنید
for number in numbers:
    print(number)
```

### خطاهای شرایط مرزی
```python
def is_valid_age(age):
    """بررسی اینکه آیا سن معتبر است (باید 0-120 باشد)."""
    if age > 0 and age < 120:  # اشتباه: 0 و 120 را حذف می‌کند
        return True
    return False

def is_valid_age_fixed(age):
    """اعتبار سنجی سن صحیح."""
    return 0 <= age <= 120

# تست موارد مرزی
print(is_valid_age(0))      # False (باید True باشد)
print(is_valid_age(120))    # False (باید True باشد)
print(is_valid_age_fixed(0))    # True
print(is_valid_age_fixed(120))  # True
```

### مسائل دقت اعداد اعشاری
```python
# مقایسه‌های خطرناک اعداد اعشاری
a = 0.1 + 0.2
b = 0.3

print(a == b)  # False! (0.30000000000000004 != 0.3)

# رویکردهای درست
def float_equal(a, b, tolerance=1e-9):
    """بررسی اینکه آیا دو float تقریباً برابر هستند."""
    return abs(a - b) < tolerance

print(float_equal(a, b))  # True

# یا از decimal برای محاسبات دقیق استفاده کنید
from decimal import Decimal, getcontext

getcontext().prec = 10  # تنظیم دقت
a = Decimal('0.1') + Decimal('0.2')
b = Decimal('0.3')
print(a == b)  # True
```

## خطاهای مدیریت منابع

### اشتباهات مدیریت فایل
```python
# خطرناک: فایل اگر استثنا رخ دهد به درستی بسته نمی‌شود
def read_file_dangerous(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()  # اگر استثنا در بالا رخ دهد هرگز اجرا نمی‌شود
    return content

# بهتر: از context manager استفاده کنید
def read_file_safe(filename):
    with open(filename, "r") as file:
        return file.read()

# یا پاک‌سازی دستی
def read_file_manual(filename):
    file = None
    try:
        file = open(filename, "r")
        return file.read()
    finally:
        if file:
            file.close()
```

### نشت حافظه
```python
# انباشتن مراجع
class MemoryLeak:
    def __init__(self):
        self.data = []

    def add_data(self, item):
        self.data.append(item)

# استفاده که مسائل حافظه ایجاد می‌کند
objects = []
for i in range(1000):
    obj = MemoryLeak()
    obj.add_data([i] * 1000)  # داده بزرگ در حافظه نگه داشته می‌شود
    objects.append(obj)

# راه‌حل: مراجع را پاک کنید وقتی کار تمام شد
del objects  # اجازه garbage collection بدهید
```

## مسائل همزمانی

### شرایط race (در کد چند رشته‌ای)
```python
import threading

counter = 0

def increment_counter():
    global counter
    for _ in range(100000):
        counter += 1  # اتمی نیست - شرایط race!

threads = []
for _ in range(10):
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(counter)  # به احتمال زیاد 1,000,000 نیست به دلیل شرایط race

# راه‌حل: از قفل‌ها استفاده کنید
counter = 0
lock = threading.Lock()

def increment_counter_safe():
    global counter
    for _ in range(100000):
        with lock:  # عملیات اتمی
            counter += 1

# یا از عملیات اتمی استفاده کنید (نمایش داده نشده - رویکرد متفاوتی نیاز دارد)
```

## خطاهای اعتبار سنجی داده‌ها

### مشکلات اعتبار سنجی ورودی
```python
def process_user_age(age_str):
    """پردازش سن کاربر از ورودی رشته."""
    age = int(age_str)  # اگر age_str عددی نباشد چه؟

    if age < 0:
        raise ValueError("سن نمی‌تواند منفی باشد")

    return age

# اعتبار سنجی بهتر
def process_user_age_safe(age_input):
    """به طور امن سن کاربر را پردازش کنید."""
    try:
        age = int(age_input)
    except ValueError:
        raise ValueError(f"فرمت سن نامعتبر: {age_input}")

    if not 0 <= age <= 150:
        raise ValueError(f"سن باید بین 0 و 150 باشد، دریافت {age}")

    return age

# استفاده
try:
    age = process_user_age_safe("25")
    print(f"سن: {age}")
except ValueError as e:
    print(f"خطا: {e}")
```

### آسیب‌پذیری‌های SQL injection
```python
# خطرناک - SQL injection ممکن است
def get_user_bad(username):
    query = f"SELECT * FROM users WHERE username = '{username}'"
    # اگر username برابر "'; DROP TABLE users; --" باشد
    # این تبدیل می‌شود به: SELECT * FROM users WHERE username = ''; DROP TABLE users; --'
    return execute_query(query)

# امن - از پرس‌وجوهای پارامتری استفاده کنید
def get_user_safe(username):
    query = "SELECT * FROM users WHERE username = ?"
    return execute_query(query, (username,))  # پارامترها جدا از SQL
```

## خطاهای الگوریتم

### منطق حلقه نادرست
```python
# یافتن حداکثر - اشتباهات رایج
def find_max_broken(numbers):
    """پیاده‌سازی شکسته."""
    if not numbers:
        return None

    max_val = numbers[0]
    for num in numbers:  # عنصر اول را دوباره شامل می‌شود
        if num > max_val:
            max_val = num
    return max_val  # نتیجه درست، اما ناکارآمد

def find_max_correct(numbers):
    """پیاده‌سازی صحیح."""
    if not numbers:
        return None

    max_val = numbers[0]
    for num in numbers[1:]:  # عنصر اول را رد کنید
        if num > max_val:
            max_val = num
    return max_val
```

### حلقه‌های بی‌پایان
```python
# حلقه بی‌پایان تصادفی
def countdown_broken(n):
    while n > 0:
        print(n)
        # فراموش کرده n را کاهش دهید!

# رفع شده
def countdown_fixed(n):
    while n > 0:
        print(n)
        n -= 1

# اشتباه رایج دیگر
def process_list_broken(items):
    i = 0
    while i < len(items):
        if items[i] == "skip":
            continue  # i افزایش پیدا نمی‌کند!
        print(items[i])
        i += 1

# رفع شده
def process_list_fixed(items):
    i = 0
    while i < len(items):
        if items[i] == "skip":
            i += 1
            continue
        print(items[i])
        i += 1
```

## خطاهای import و ماژول

### مسائل import دایره‌ای
```python
# module_a.py
from module_b import function_b

def function_a():
    return function_b()

# module_b.py
from module_a import function_a  # import دایره‌ای!

def function_b():
    return function_a()

# راه‌حل: import داخل توابع یا بازسازی
# module_a.py
def function_a():
    from module_b import function_b
    return function_b()

# module_b.py
def function_b():
    from module_a import function_a
    return function_a()
```

### مشکلات برخورد نام
```python
# سایه انداختن بر توابع داخلی
list = [1, 2, 3]  # بر list() داخلی سایه می‌اندازد
my_list = list((4, 5, 6))  # TypeError: 'list' object is not callable

# رفع شده
my_list_data = [1, 2, 3]
my_tuple = (4, 5, 6)
my_list = list(my_tuple)  # از list داخلی استفاده کنید
```

## استراتژی‌های تست و اعتبار سنجی

### تست واحد برای پیشگیری از خطا
```python
import pytest

def add_numbers(a, b):
    """دو عدد را جمع کنید."""
    return a + b

def test_add_numbers():
    """تابع add_numbers را تست کنید."""
    # موارد عادی
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0.5, 0.5) == 1.0

    # موارد مرزی
    assert add_numbers(0, 0) == 0

def test_add_numbers_errors():
    """مدیریت خطا را تست کنید."""
    # این باید کار کند - تایپ پویا اجازه می‌دهد
    result = add_numbers("hello", "world")
    assert result == "helloworld"

# اجرای تست‌ها
if __name__ == "__main__":
    test_add_numbers()
    test_add_numbers_errors()
    print("همه تست‌ها گذرانده شدند!")
```

### برنامه‌نویسی دفاعی
```python
def robust_divide(dividend, divisor):
    """تقسیم با بررسی خطای جامع."""
    # بررسی نوع
    if not isinstance(dividend, (int, float)):
        raise TypeError("تقسیم شونده باید عدد باشد")
    if not isinstance(divisor, (int, float)):
        raise TypeError("تقسیم‌کننده باید عدد باشد")

    # بررسی مقدار
    if divisor == 0:
        raise ValueError("نمی‌توان بر صفر تقسیم کرد")

    # مدیریت موارد خاص
    if dividend == 0:
        return 0

    return dividend / divisor

def test_robust_divide():
    """robust_divide را با ورودی‌های مختلف تست کنید."""
    # موارد عادی
    assert robust_divide(10, 2) == 5.0

    # موارد خطا
    try:
        robust_divide(10, 0)
        assert False, "باید ValueError ایجاد کند"
    except ValueError:
        pass

    try:
        robust_divide("10", 2)
        assert False, "باید TypeError ایجاد کند"
    except TypeError:
        pass

test_robust_divide()
```

## الگوهای بازیابی خطا

### کاهش优雅
```python
def load_configuration(filename="config.json"):
    """پیکربندی را با گزینه‌های fallback بارگذاری کنید."""
    import json
    import os

    # فایل پیکربندی اصلی را امتحان کنید
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"خطا در بارگذاری {filename}: {e}")

    # fallback به متغیرهای محیطی
    config = {}
    config['database_url'] = os.getenv('DATABASE_URL', 'sqlite:///default.db')
    config['debug'] = os.getenv('DEBUG', 'False').lower() == 'true'

    print("از پیکربندی fallback استفاده می‌شود")
    return config
```

### مکانیسم‌های retry
```python
import time
import random

def unreliable_operation():
    """عملیاتی را شبیه‌سازی کنید که ممکن است ناموفق باشد."""
    if random.random() < 0.7:
        raise Exception("ناموفق بودن موقت")
    return "موفقیت"

def retry_operation(operation, max_attempts=3, delay=1):
    """عملیات را با backoff نمایی امتحان مجدد کنید."""
    for attempt in range(max_attempts):
        try:
            return operation()
        except Exception as e:
            if attempt == max_attempts - 1:
                raise e
            print(f"تلاش {attempt + 1} ناموفق: {e}")
            time.sleep(delay * (2 ** attempt))  # backoff نمایی

    raise Exception("همه تلاش‌های retry ناموفق بودند")

# استفاده
try:
    result = retry_operation(unreliable_operation)
    print(f"عملیات موفق: {result}")
except Exception as e:
    print(f"عملیات ناموفق: {e}")
```

## نکات کلیدی

۱. **خطاهای نحوی** توسط پارسر قبل از اجرا گرفته می‌شوند
۲. **خطاهای زمان اجرا** در طول اجرای برنامه رخ می‌دهند و نیاز به مدیریت دارند
۳. **خطاهای منطقی** نتایج نادرست تولید می‌کنند اما برنامه را خراب نمی‌کنند
۴. **برنامه‌نویسی دفاعی** خطاهای بالقوه را پیش‌بینی و مدیریت می‌کند
۵. **تست** کمک می‌کند خطاها را قبل از رسیدن به تولید بگیرند
۶. **مدیریت خطای优雅** تجربه کاربر را بهبود می‌بخشد

## مطالعه بیشتر
- سلسله مراتب استثنای پایتون
- بهترین روش‌های تست واحد
- تکنیک‌های برنامه‌نویسی دفاعی
- الگوهای مدیریت خطا در زبان‌های مختلف
- راهنماهای اشکال‌زدایی و عیب‌یابی