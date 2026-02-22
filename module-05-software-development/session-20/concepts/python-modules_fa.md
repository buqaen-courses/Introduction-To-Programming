# ماژول‌های پایتون: سازماندهی کد در فایل‌ها

## مقدمه: چرا ماژول‌ها؟

همانطور که برنامه‌ها بزرگ‌تر می‌شوند، قرار دادن تمام کد در یک فایل آشفته می‌شود. **ماژول‌ها** به شما اجازه می‌دهند:
- **سازماندهی** کد در گروه‌های منطقی
- **استفاده مجدد** از توابع در پروژه‌های مختلف
- **همکاری** با دیگران در فایل‌های مختلف
- **نگهداری** کد آسان‌تر (یافتن و رفع سریع‌تر باگ‌ها)

### استعاره ماژول

ماژول‌ها را مانند فصل‌های یک کتاب در نظر بگیرید:
- فصل ۱: مقدمه
- فصل ۲: شخصیت‌ها
- فصل ۳: طرح داستان

هر فصل روی یک موضوع تمرکز دارد. می‌توانید فصل‌ها را به ترتیب بخوانید یا به موارد خاص بپرید.

### ماژول چیست؟

یک **ماژول** به سادگی یک فایل پایتون (`.py`) است که حاوی کد است:
- توابع
- متغیرها
- کلاس‌ها (بعداً یاد می‌گیریم)

---

## بخش ۱: ایجاد اولین ماژول شما

### مرحله ۱: ایجاد فایل ماژول

یک فایل به نام `math_utils.py` ایجاد کنید:

```python
# math_utils.py
"""مجموعه‌ای از توابع ریاضی مفید."""

def add(a, b):
    """جمع دو عدد."""
    return a + b

def subtract(a, b):
    """تفریق b از a."""
    return a - b

def multiply(a, b):
    """ضرب دو عدد."""
    return a * b

def divide(a, b):
    """تقسیم a بر b (با مدیریت خطا)."""
    if b == 0:
        return "Cannot divide by zero"
    return a / b

PI = 3.14159  # ثابت سطح ماژول
```

### مرحله ۲: استفاده از ماژول

یک فایل دیگر در همان پوشه ایجاد کنید، `main.py`:

```python
# main.py
import math_utils  # ایمپورت ماژول

# استفاده از توابع ماژول
result = math_utils.add(5, 3)
print(result)  # 8

result = math_utils.multiply(4, 7)
print(result)  # 28

# استفاده از ثابت‌ها
print(math_utils.PI)  # 3.14159
```

**نکته کلیدی**: نام ماژول نام فایل بدون `.py` است

---

## بخش ۲: روش‌های مختلف ایمپورت

### روش ۱: ایمپورت کل ماژول

```python
import math_utils

result = math_utils.add(5, 3)
```

**مزایا**: مشخص است که توابع از کجا می‌آیند
**معایب**: طولانی‌تر برای تایپ

### روش ۲: ایمپورت موارد خاص

```python
from math_utils import add, subtract, PI

result = add(5, 3)        # نیازی به math_utils. نیست
result = subtract(10, 4)  # دسترسی مستقیم
print(PI)                 # 3.14159
```

**مزایا**: کد کوتاه‌تر
**معایب**: کمتر مشخص است که چیزها از کجا می‌آیند

### روش ۳: ایمپورت با نام مستعار

```python
import math_utils as mu  # mu نام مستعار است

result = mu.add(5, 3)
result = mu.multiply(4, 2)
```

**مفید وقتی**: نام‌های ماژول طولانی هستند

```python
import my_really_long_module_name as short
```

### روش ۴: ایمپورت همه (توصیه نمی‌شود!)

```python
from math_utils import *  # ایمپورت تمام توابع

result = add(5, 3)
result = multiply(4, 2)
```

**⚠️ هشدار**: می‌تواند باعث تداخل نام‌ها شود! از این الگو اجتناب کنید.

---

## بخش ۳: مسیر جستجوی ماژول

### پایتون کجا به دنبال ماژول‌ها می‌گردد؟

```python
import sys

# ببینید پایتون کجاها را می‌گردد
print("Python looks in these folders:")
for path in sys.path:
    print(f"  {path}")
```

**ترتیب جستجو:**
1. پوشه فعلی
2. کتابخانه استاندارد پایتون
3. بسته‌های شخص ثالث (site-packages)

### افزودن مسیرهای سفارشی

```python
import sys

# افزودن پوشه خود
sys.path.append("/path/to/my/modules")

# حالا می‌توانید از آنجا ایمپورت کنید
import my_custom_module
```

---

## بخش ۴: الگوی `__name__ == "__main__"`

### مشکل

وقتی یک ماژول را ایمپورت می‌کنید، پایتون تمام کد آن را اجرا می‌کند. اگر کد تست داشته باشید چطور؟

```python
# math_utils.py
def add(a, b):
    return a + b

# این هنگام ایمپورت اجرا می‌شود!
print("Testing add function:")
print(add(2, 3))  # این هنگام ایمپورت اجرا می‌شود!
```

### راه‌حل

```python
# math_utils.py
def add(a, b):
    return a + b

# این فقط هنگام اجرای مستقیم فایل اجرا می‌شود
if __name__ == "__main__":
    print("Testing add function:")
    print(add(2, 3))
    print("All tests passed!")
```

**نحوه کار:**
- وقتی فایل مستقیماً اجرا می‌شود: `__name__` = `"__main__"`
- وقتی فایل ایمپورت می‌شود: `__name__` = نام ماژول (مثلاً `"math_utils"`)

### مثال عملی

```python
# calculator.py
"""یک ماژول ماشین حساب ساده."""

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

# کد تست (فقط هنگام اجرای مستقیم فایل اجرا می‌شود)
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
# ایمپورت و استفاده
from calculator import add, subtract
result = add(5, 3)

# یا مستقیماً برای تست اجرا کنید
# python calculator.py
```

---

## بخش ۵: سازماندهی پروژه‌های چند فایلی

### مثال ساختار پروژه

```
my_project/
├── main.py              # نقطه ورود
├── config.py            # تنظیمات و ثابت‌ها
├── utils/
│   ├── __init__.py      # آن را یک بسته می‌کند
│   ├── file_utils.py    # عملیات فایل
│   └── math_utils.py    # توابع ریاضی
├── data/
│   ├── __init__.py
│   └── student_data.py  # مدیریت داده
└── tests/
    └── test_calculator.py
```

### مثال: پروژه دفتر نمرات

**config.py** - تنظیمات
```python
"""تنظیمات پیکربندی برای دفتر نمرات."""

DATA_FILE = "grades.txt"
REPORT_FILE = "report.txt"
PASSING_GRADE = 60
MAX_STUDENTS = 100
```

**utils/file_utils.py** - عملیات فایل
```python
"""ابزارهای مدیریت فایل."""

def read_lines(filename):
    """خواندن تمام خطوط از فایل."""
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def write_lines(filename, lines):
    """نوشتن خطوط در فایل."""
    with open(filename, 'w') as file:
        file.writelines(lines)
```

**utils/grade_utils.py** - محاسبات نمره
```python
"""ابزارهای محاسبه نمره."""

def calculate_average(scores):
    """محاسبه میانگین نمرات."""
    if not scores:
        return 0
    return sum(scores) / len(scores)

def get_letter_grade(average):
    """تبدیل میانگین به نمره حرفی."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'
```

**main.py** - برنامه اصلی
```python
"""برنامه دفتر نمرات دانشجو."""

import config
from utils.file_utils import read_lines, write_lines
from utils.grade_utils import calculate_average, get_letter_grade

def process_grades():
    """تابع اصلی برای پردازش نمرات دانشجو."""
    lines = read_lines(config.DATA_FILE)

    students = []
    for line in lines:
        parts = line.strip().split(',')
        if len(parts) >= 2:
            name = parts[0]
            scores = [int(s) for s in parts[1:] if s.isdigit()]
            avg = calculate_average(scores)
            grade = get_letter_grade(avg)

            students.append({
                'name': name,
                'average': avg,
                'grade': grade
            })

    return students

def generate_report(students):
    """ایجاد و ذخیره گزارش."""
    lines = ["STUDENT GRADE REPORT\n", "="*50 + "\n\n"]

    for student in students:
        lines.append(f"{student['name']}: {student['average']:.1f} ({student['grade']})\n")

    write_lines(config.REPORT_FILE, lines)
    print(f"Report saved to {config.REPORT_FILE}")

if __name__ == "__main__":
    students = process_grades()
    for student in students:
        print(f"{student['name']}: {student['average']:.1f} ({student['grade']})")

    generate_report(students)
```

---

## بخش ۶: ماژول‌های داخلی

### ماژول‌های داخلی رایج

```python
# os - توابع سیستم عامل
import os

print(os.getcwd())              # پوشه فعلی
print(os.listdir('.'))          # لیست فایل‌ها
os.mkdir('new_folder')          # ایجاد پوشه
os.path.exists('file.txt')      # بررسی وجود

# sys - توابع سیستم
import sys

print(sys.argv)                 # آرگومان‌های خط فرمان
print(sys.path)                 # مسیر جستجوی ماژول
sys.exit()                      # خروج از برنامه

# datetime - تاریخ و زمان
from datetime import datetime

now = datetime.now()
print(now.strftime("%Y-%m-%d"))  # 2024-01-15

# random - اعداد تصادفی
import random

print(random.randint(1, 10))    # تصادفی ۱-۱۰
print(random.choice(['a', 'b', 'c']))  # انتخاب تصادفی

# json - داده JSON
import json

data = {'name': 'Alice', 'age': 25}
json_string = json.dumps(data, indent=2)
parsed = json.loads(json_string)

# math - توابع ریاضی
import math

print(math.sqrt(16))            # 4.0
print(math.pi)                  # 3.14159...
print(math.floor(4.7))          # 4
```

---

## بخش ۷: بهترین شیوه‌ها

### انجام دهید:

```python
# ۱. استفاده از نام‌های ماژول واضح
# good: student_grades.py
# bad: sg.py

# ۲. اضافه کردن docstrings
"""This module handles student grade calculations."""

# ۳. استفاده از __name__ == "__main__" برای کد تست
if __name__ == "__main__":
    # Test code here
    pass

# ۴. گروه‌بندی توابع مرتبط
# math_utils.py - فقط توابع ریاضی
# file_utils.py - فقط عملیات فایل

# ۵. ایمپورت در بالا
import os
import sys
from datetime import datetime
```

### انجام ندهید:

```python
# ۱. از 'import *' استفاده نکنید
from module import *  # Avoid this!

# ۲. تمام کد را در یک فایل نگذارید
# Split into logical modules

# ۳. ایمپورت‌های دایره‌ای ایجاد نکنید
# file_a.py imports file_b.py
# file_b.py imports file_a.py  # BAD!

# ۴. کد را در سطح ماژول اجرا نکنید
# (مگر اینکه ثابت‌ها یا راه‌اندازی ساده باشد)
print("This runs on import!")  # Avoid this
```

---

## تمرین‌های عملی

### تمرین ۱: ایجاد ماژول ابزارهای رشته‌ای

`string_utils.py` را با این توابع ایجاد کنید:
- `count_words(text)` - شمارش کلمات در متن
- `reverse_string(text)` - معکوس کردن رشته
- `is_palindrome(text)` - بررسی آیا palindrome است
- `capitalize_words(text)` - بزرگ کردن اول هر کلمه

سپس `main.py` ایجاد کنید که از این توابع استفاده می‌کند.

### تمرین ۲: ساخت ماشین حساب چند فایلی

یک پروژه ماشین حساب با این ساختار ایجاد کنید:
```
calculator/
├── main.py
├── operations.py    # +, -, *, /
├── validation.py    # بررسی ورودی
└── display.py       # فرمت‌بندی خروجی
```

### تمرین ۳: بازسازی یک برنامه نامرتب

این برنامه تک‌فایل را به ماژول‌ها تقسیم کنید:

```python
# messy_program.py (فعلی)
def read_data():
    pass

def validate_data():
    pass

def process_data():
    pass

def save_results():
    pass

def format_report():
    pass

def main():
    data = read_data()
    validate_data(data)
    process_data(data)
    save_results(data)
    format_report(data)

main()
```

تبدیل به:
- `data_io.py` - توابع خواندن/ذخیره
- `validation.py` - توابع اعتبارسنجی
- `processing.py` - توابع پردازش
- `reporting.py` - فرمت‌بندی گزارش
- `main.py` - برنامه اصلی

---

## نکات کلیدی

1. **ماژول‌ها فقط فایل‌های `.py` هستند** - با نوشتن کد پایتون ایجادشان کنید
2. **`import module_name`** تمام کد را وارد می‌کند
3. **`from module import function`** موارد خاص را وارد می‌کند
4. **`if __name__ == "__main__"`** کد ایمپورت را از کد اجرا جدا می‌کند
5. **بر اساس هدف سازماندهی کنید** - توابع مرتبط را با هم گروه‌بندی کنید
6. **از نام‌های واضح استفاده کنید** - نام‌های ماژول باید محتوا را توصیف کنند

## مرجع سریع

```python
# سبک‌های ایمپورت
import math_utils                    # math_utils.add(5, 3)
from math_utils import add           # add(5, 3)
import math_utils as mu              # mu.add(5, 3)

# الگوی __name__
if __name__ == "__main__":
    # کدی که هنگام اجرای فایل اجرا می‌شود
    pass

# ایجاد ماژول
# ۱. توابع را در یک فایل .py بنویسید
# ۲. آن را در فایل دیگر ایمپورت کنید
# ۳. از توابع استفاده کنید!
```

---

## مطالعه بیشتر

- **بعدی**: جلسه ۲۱ - پروژه کوچک (ترکیب تمام مفاهیم)
- **تمرین**: یکی از پروژه‌های قدیمی خود را به ماژول‌ها تقسیم کنید
- **چالش**: ایجاد کتابخانه ماژول قابل استفاده مجدد
- **کاوش**: آموختن درباره بسته‌های پایتون (پوشه‌ها با `__init__.py`)
