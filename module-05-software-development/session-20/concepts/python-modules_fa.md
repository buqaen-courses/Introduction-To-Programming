# ماژول‌های پایتون: سازماندهی کد در فایل‌ها

## مقدمه: چرا ماژول‌ها؟

با بزرگ شدن برنامه‌ها، گذاشتن همه کد در یک فایل شلوغ می‌شود. **ماژول‌ها** به شما اجازه می‌دهند:
- کد را در گروه‌های منطقی **سازماندهی** کنید
- توابع را در چند پروژه **استفاده مجدد** کنید
- با دیگران روی فایل‌های مختلف **همکاری** کنید
- کد را راحت‌تر **نگهداری** کنید (پیدا و رفع باگ سریع‌تر)

### استعاره ماژول

ماژول‌ها را مثل فصل‌های یک کتاب فکر کنید:
- فصل ۱: مقدمه
- فصل ۲: شخصیت‌ها
- فصل ۳: داستان

هر فصل روی یک موضوع تمرکز دارد. می‌توانید فصل‌ها را به ترتیب بخوانید یا مستقیم به فصل خاصی بروید.

### ماژول چیست؟

**ماژول** فقط یک فایل پایتون (`.py`) است که شامل کد است:
- توابع
- متغیرها
- کلاس‌ها (بعدا یاد می‌گیریم)

---

## بخش ۱: ساخت نخستین ماژول

### گام ۱: ساخت فایل ماژول

فایلی به نام `math_utils.py` بسازید:

```python
# math_utils.py
"""A collection of useful math functions."""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b (with error handling)."""
    if b == 0:
        return "Cannot divide by zero"
    return a / b

PI = 3.14159  # Module-level constant
```

### گام ۲: استفاده از ماژول

فایل دیگری در همان پوشه بسازید، `main.py`:

```python
# main.py
import math_utils  # Import the module

# Use functions from the module
result = math_utils.add(5, 3)
print(result)  # 8

result = math_utils.multiply(4, 7)
print(result)  # 28

# Use constants
print(math_utils.PI)  # 3.14159
```

**نکته کلیدی**: نام ماژول همان نام فایل بدون `.py` است

---

## بخش ۲: روش‌های مختلف import

### روش ۱: import کل ماژول

```python
import math_utils

result = math_utils.add(5, 3)
```

**مزایا**: مشخص است توابع از کجا آمده‌اند
**معایب**: تایپش طولانی‌تر است

### روش ۲: import آیتم‌های مشخص

```python
from math_utils import add, subtract, PI

result = add(5, 3)        # No need for math_utils.
result = subtract(10, 4)  # Direct access
print(PI)                 # 3.14159
```

**مزایا**: کد کوتاه‌تر
**معایب**: کمتر مشخص است چیزها از کجا آمده‌اند

### روش ۳: import با نام مستعار

```python
import math_utils as mu  # mu is the alias

result = mu.add(5, 3)
result = mu.multiply(4, 2)
```

**مفید وقتی**: نام ماژول‌ها بلند است

```python
import my_really_long_module_name as short
```

### روش ۴: import همه‌چیز (توصیه نمی‌شود!)

```python
from math_utils import *  # Import all functions

result = add(5, 3)
result = multiply(4, 2)
```

**⚠️ هشدار**: می‌تواند تداخل نام ایجاد کند! از این الگو پرهیز کنید.

---

## بخش ۳: مسیر جست‌وجوی ماژول

### پایتون کجا به دنبال ماژول‌ها می‌گردد؟

```python
import sys

# See where Python looks
print("Python looks in these folders:")
for path in sys.path:
    print(f"  {path}")
```

**ترتیب جست‌وجو:**
۱. پوشه جاری
۲. کتابخانه استاندارد پایتون
۳. پکیج‌های شخص ثالث (site-packages)

### افزودن مسیرهای سفارشی

```python
import sys

# Add your own folder
sys.path.append("/path/to/my/modules")

# Now you can import from there
import my_custom_module
```

---

## بخش ۴: الگوی `__name__ == "__main__"`

### مسئله

وقتی یک ماژول را import می‌کنید، پایتون همه کد داخل آن را اجرا می‌کند. اگر کد تست داشته باشید چه؟

```python
# math_utils.py
def add(a, b):
    return a + b

# This runs when file is imported!
print("Testing add function:")
print(add(2, 3))  # This executes during import!
```

### راه‌حل

```python
# math_utils.py
def add(a, b):
    return a + b

# This only runs when file is executed directly
if __name__ == "__main__":
    print("Testing add function:")
    print(add(2, 3))
    print("All tests passed!")
```

**چطور کار می‌کند:**
- وقتی فایل مستقیم اجرا می‌شود: `__name__` = `"__main__"`
- وقتی فایل import می‌شود: `__name__` = نام ماژول (مثلاً `"math_utils"`)

### مثال عملی

```python
# calculator.py
"""A simple calculator module."""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# Test code (only runs when file is executed directly)
if __name__ == "__main__":
    print("Running calculator tests...")
    assert add(2, 3) == 5
    assert subtract(10, 4) == 6
    assert multiply(3, 3) == 9
    assert divide(10, 2) == 5
    print("All tests passed!")
```

حالا می‌توانید:
```python
# Import and use
from calculator import add, subtract
result = add(5, 3)

# Or run directly to test
# python calculator.py
```

---

## بخش ۵: سازماندهی پروژه‌های چندفایلی

### نمونه ساختار پروژه

```
my_project/
├── main.py              # Entry point
├── config.py            # Settings and constants
├── utils/
│   ├── __init__.py      # Makes it a package
│   ├── file_utils.py    # File operations
│   └── math_utils.py    # Math functions
├── data/
│   ├── __init__.py
│   └── student_data.py  # Data handling
└── tests/
    └── test_calculator.py
```

### مثال: پروژه کارنامه

**config.py** - تنظیمات
```python
"""Configuration settings for the gradebook."""

DATA_FILE = "grades.txt"
REPORT_FILE = "report.txt"
PASSING_GRADE = 60
MAX_STUDENTS = 100
```

**utils/file_utils.py** - عملیات فایل
```python
"""File handling utilities."""

def read_lines(filename):
    """Read all lines from a file."""
    with open(filename, 'r') as f:
        return f.readlines()

def write_lines(filename, lines):
    """Write lines to a file."""
    with open(filename, 'w') as f:
        f.writelines(lines)
```

**utils/math_utils.py** - توابع ریاضی
```python
"""Math utility functions."""

def calculate_average(numbers):
    """Calculate average of a list."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def calculate_percentage(score, total):
    """Calculate percentage."""
    if total == 0:
        return 0
    return (score / total) * 100
```

**main.py** - نقطه ورود
```python
"""Main program entry point."""
from utils.file_utils import read_lines, write_lines
from utils.math_utils import calculate_average

def main():
    """Main program function."""
    print("Gradebook Program")
    print("=" * 30)

    # Read student data
    lines = read_lines("grades.txt")
    print(f"Loaded {len(lines)} records")

    # Process and report
    # ... your code here ...

if __name__ == "__main__":
    main()
```

---

## بخش ۶: ماژول‌های داخلی

### ماژول‌های پرکاربرد کتابخانه استاندارد

```python
# os - عملیات سیستم‌عامل
import os
print(os.getcwd())           # پوشه جاری
print(os.listdir("."))       # فهرست فایل‌ها

# sys - تنظیمات سیستم
import sys
print(sys.version)           # نسخه پایتون
print(sys.platform)           # سیستم‌عامل

# math - توابع ریاضی
import math
print(math.sqrt(16))         # 4.0
print(math.pi)               # 3.14159...

# random - اعداد تصادفی
import random
print(random.randint(1, 10)) # عدد تصادفی ۱ تا ۱۰

# datetime - تاریخ و زمان
from datetime import datetime
print(datetime.now())        # زمان فعلی

# json - کار با JSON
import json
data = {"name": "Alice", "age": 25}
json_string = json.dumps(data)
```

### ساخت پکیج سفارشی

```
my_package/
├── __init__.py          # فایل الزامی - پوشه را پکیج می‌کند
├── module1.py           # ماژول اول
├── module2.py           # ماژول دوم
└── subpackage/
    ├── __init__.py
    └── module3.py
```

```python
# استفاده از پکیج
from my_package import module1
from my_package.subpackage import module3
```

---

## اشتباهات رایج مبتدی

### اشتباه ۱: فراموش کردن `__init__.py`

```
my_package/
├── __init__.py      # ← این فایل لازم است!
├── module1.py
└── module2.py
```

بدون `__init__.py` پایتون پوشه را پکیج نمی‌شناسد.

### اشتباه ۲: تداخل نام‌ها

```python
# اشتباه - هر دو تابع add دارند
from math_utils import add
from string_utils import add  # این قبلی را بازنویسی می‌کند!

# درست - از نام مستعار استفاده کنید
from math_utils import add as math_add
from string_utils import add as str_add
```

### اشتباه ۳: import چرخه‌ای

```python
# module_a.py
from module_b import something  # خطا اگر module_b هم import module_a کند!

# درست - کد مشترک را در فایل سوم بگذارید
# common.py
def shared_function():
    pass
```

### اشتباه ۴: اجرای کد در سطح بالا

```python
# اشتباه - این کد هنگام import اجرا می‌شود!
def helper():
    pass

helper()  # این هنگام import اجرا می‌شود!

# درست - داخل if __name__ == "__main__" بگذارید
def helper():
    pass

if __name__ == "__main__":
    helper()
```

---

## تمرین‌ها

### تمرین ۱: ماژول ابزارهای ریاضی
ماژولی به نام `math_tools.py` بسازید با توابع زیر:
- `add(a, b)` - جمع
- `subtract(a, b)` - تفریق
- `multiply(a, b)` - ضرب
- `divide(a, b)` - تقسیم (با مدیریت تقسیم بر صفر)
- `power(a, b)` - توان
- `factorial(n)` - فاکتوریل

```python
# math_tools.py
# کد شما اینجا
```

### تمرین ۲: برنامه چندفایلی
برنامه‌ای بسازید که از ۳ فایل تشکیل شده:
- `main.py` - نقطه ورود
- `data.py` - توابع مدیریت داده
- `display.py` - توابع نمایش خروجی

### تمرین ۳: پکیج سفارشی
پکیجی به نام `my_utils` بسازید با دو ماژول:
- `my_utils/text.py` - توابع کار با متن
- `my_utils/numbers.py` - توابع کار با اعداد

---

## نکات کلیدی

۱. **ماژول فقط یک فایل `.py` است** - نحو خاصی ندارد
۲. **از `import module` استفاده کنید** - واضح‌تر و امن‌تر
۳. **از `from x import *` پرهیز کنید** - تداخل نام ایجاد می‌کند
۴. **از `if __name__ == "__main__":` استفاده کنید** - کد تست را هنگام import اجرا نمی‌کند
۵. **وابستگی‌ها یک‌طرفه باشند** - چرخه باعث خطا می‌شود
۶. **کتابخانه استاندارد را بررسی کنید** - قبل از نوشتن یک تابع

## مرجع سریع

| عملیات | نحو | مثال |
|--------|-----|------|
| import کل ماژول | `import module` | `import math_utils` |
| import مشخص | `from module import name` | `from math_utils import add` |
| import با نام مستعار | `import module as alias` | `import math_utils as mu` |
| import همه (توصیه نمی‌شود) | `from module import *` | `from math_utils import *` |
| اجرای مستقیم | `if __name__ == "__main__":` | کد تست |
| مسیر ماژول‌ها | `sys.path` | `sys.path.append("/path")` |

---

## مطالعه بیشتر

- **بعدی**: جلسه ۲۱، پروژه کوچک ۱
- **تمرین**: همه تمرین‌های بالا را کامل کنید
- **چالش**: پکیجی با ۳ ماژول بسازید و در پروژه دیگری استفاده کنید
- **کاوش کنید**: ماژول `collections` و `itertools` را بررسی کنید