# تکنیک‌های اشکال‌زدایی: یافتن و رفع خطاهای برنامه

## مقدمه‌ای بر اشکال‌زدایی

اشکال‌زدایی فرآیند یافتن و رفع خطاها (باگ‌ها) در برنامه‌های کامپیوتری است. اشکال‌زدایی مؤثر شامل بررسی سیستمی، تست فرضیه و تحلیل دقیق رفتار برنامه می‌شود.

## درک وضعیت برنامه

### اشکال‌زدایی با print
```python
def calculate_average(numbers):
    """محاسبه میانگین با printهای اشکال‌زدایی."""
    print(f"ورودی: {numbers}")
    print(f"طول: {len(numbers)}")

    if not numbers:
        print("لیست خالی، بازگرداندن 0")
        return 0

    total = 0
    for i, num in enumerate(numbers):
        print(f"افزودن عدد {i}: {num}")
        total += num
        print(f"مجموع جاری: {total}")

    average = total / len(numbers)
    print(f"میانگین نهایی: {average}")
    return average

# تست با اشکال‌زدایی
result = calculate_average([10, 20, 30])
print(f"نتیجه نهایی: {result}")
```

### استفاده از assertions
```python
def divide_and_round(a, b, decimals=2):
    """تقسیم a بر b و گرد کردن به اعشار مشخص."""
    assert b != 0, "نمی‌توان بر صفر تقسیم کرد"
    assert decimals >= 0, "اعشار باید غیرمنفی باشد"
    assert isinstance(a, (int, float)), "آرگومان اول باید عدد باشد"
    assert isinstance(b, (int, float)), "آرگومان دوم باید عدد باشد"

    result = a / b
    rounded = round(result, decimals)
    return rounded

# assertions کمک می‌کنند خطاها را زودتر بگیرند
try:
    result = divide_and_round(10, 3, 2)
    print(f"نتیجه: {result}")  # 3.33
except AssertionError as e:
    print(f"Assertion ناموفق: {e}")
```

### ثبت برای اشکال‌زدایی
```python
import logging

# تنظیم ثبت
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def process_data(data):
    """پردازش داده‌ها با ثبت جامع."""
    logging.info(f"شروع پردازش داده برای {len(data)} آیتم")

    try:
        # اعتبار سنجی ورودی
        if not data:
            logging.warning("داده خالی ارائه شد")
            return []

        # پردازش هر آیتم
        results = []
        for i, item in enumerate(data):
            logging.debug(f"پردازش آیتم {i}: {item}")

            processed = process_single_item(item)
            results.append(processed)

            if i % 10 == 0:  # ثبت پیشرفت برای مجموعه داده‌های بزرگ
                logging.info(f"{i+1}/{len(data)} آیتم پردازش شد")

        logging.info(f"با موفقیت {len(results)} آیتم پردازش شد")
        return results

    except Exception as e:
        logging.error(f"خطا در پردازش داده: {e}", exc_info=True)
        raise

def process_single_item(item):
    """پردازش آیتم واحد (placeholder)."""
    return item.upper() if isinstance(item, str) else item
```

## اشکال‌زدایی تعاملی

### اشکال‌زدای پایتون (pdb)
```python
import pdb

def complex_calculation(x, y, z):
    """محاسبه پیچیده با نقاط توقف اشکال‌زدایی."""
    # تنظیم نقطه توقف
    pdb.set_trace()

    step1 = x + y
    step2 = step1 * z
    step3 = step2 / (x + y)

    return step3

# اجرای با اشکال‌زدایی
result = complex_calculation(2, 3, 4)
print(result)

# در نقطه توقف، می‌توانید:
# n - خط بعدی
# s - ورود به تابع
# c - ادامه اجرا
# l - لیست کد
# p variable - چاپ مقدار متغیر
# q - خروج از اشکال‌زدای
```

### اشکال‌زدایی پس از مرگ
```python
import pdb
import traceback

def risky_function():
    """تابعی که ممکن است ناموفق باشد."""
    data = [1, 2, 3]
    return data[10]  # IndexError

try:
    risky_function()
except Exception:
    # شروع اشکال‌زدای در نقطه استثنا
    pdb.post_mortem()
```

### نقاط توقف شرطی
```python
def find_duplicates(items):
    """یافتن آیتم‌های تکراری در لیست."""
    seen = set()
    duplicates = []

    for item in items:
        if item in seen:
            duplicates.append(item)
            # نقطه توقف شرطی
            if len(duplicates) >= 3:
                breakpoint()  # اشکال‌زدای داخلی پایتون 3.7+
        else:
            seen.add(item)

    return duplicates
```

## فرآیند اشکال‌زدایی سیستمی

### ۱. بازتولید مشکل
```python
def test_function_with_bug():
    """تابع با یک باگ ظریف."""
    data = [1, 2, 3, 4, 5]

    # باگ: تغییر لیست در حین پیمایش
    for item in data:
        if item % 2 == 0:
            data.remove(item)  # این باعث رد شدن آیتم‌ها می‌شود!

    return data

# بازتولید مسئله
print("انتظار: [1, 3, 5]")
print(f"واقعی: {test_function_with_bug()}")  # [1, 3, 5] - درست به نظر می‌رسد؟
print("صبر کنید، بیایید با داده‌های مختلف بررسی کنیم...")

# باگ با داده‌های مختلف آشکار می‌شود
print(f"با [1,2,3,4,5,6]: {test_function_with_bug()}")  # برخی زوج‌ها رد می‌شوند
```

### ۲. ایزوله کردن مشکل
```python
def test_isolation():
    """ایزوله کردن کد مشکل‌دار."""

    # تست اجزای فردی
    data = [1, 2, 3, 4, 5]
    print("داده اصلی:", data)

    # تست منطق حلقه به صورت دستی
    seen_items = []
    for i, item in enumerate(data):
        print(f"تکرار {i}: item={item}, data={data}")
        if item % 2 == 0:
            print(f"  حذف عدد زوج: {item}")
            data.remove(item)
            print(f"  داده پس از حذف: {data}")
        seen_items.append(item)

    print("آیتم‌های دیده شده در تکرار:", seen_items)
    print("داده نهایی:", data)

test_isolation()
```

### ۳. شناسایی علت اصلی
```python
def correct_function(items):
    """پیاده‌سازی صحیح که لیست را در حین پیمایش تغییر نمی‌دهد."""

    # روش ۱: ایجاد لیست جدید
    odds = []
    for item in items:
        if item % 2 != 0:
            odds.append(item)
    return odds

    # روش ۲: comprehension لیست
    # return [item for item in items if item % 2 != 0]

    # روش ۳: تابع filter
    # return list(filter(lambda x: x % 2 != 0, items))

def test_fix():
    """تست تابع اصلاح شده."""
    test_cases = [
        [1, 2, 3, 4, 5],
        [2, 4, 6, 8, 10],
        [1, 3, 5, 7, 9],
        []
    ]

    for case in test_cases:
        result = correct_function(case)
        print(f"ورودی: {case} -> خروجی: {result}")

test_fix()
```

### ۴. پیاده‌سازی و تست رفع
```python
def comprehensive_test():
    """تست رفع با موارد مرزی."""
    test_cases = [
        ([], []),
        ([1], [1]),
        ([2], []),
        ([1, 2], [1]),
        ([1, 2, 3, 4, 5], [1, 3, 5]),
        ([2, 4, 6], []),
        (list(range(1, 11)), list(range(1, 11, 2))),  # 1,3,5,7,9
    ]

    for input_data, expected in test_cases:
        result = correct_function(input_data)
        status = "✓" if result == expected else "✗"
        print(f"{status} {input_data} -> {result} (انتظار {expected})")

        if result != expected:
            print(f"  خطا: انتظار {expected}، دریافت {result}")

comprehensive_test()
```

## ابزارهای اشکال‌زدایی رایج

### اشکال‌زداهای IDE
```python
# بیشتر IDEها (PyCharm, VS Code و غیره) فراهم می‌کنند:
# - اجرای مرحله به مرحله
# - بازرسی متغیرها
# - مشاهده پشته فراخوانی
# - مدیریت نقاط توقف
# - عبارات نظارت

def function_to_debug(a, b, c):
    """تابع برای نمایش اشکال‌زدایی IDE."""
    x = a + b
    y = x * c
    z = y / (a + b)

    # نقطه توقف را اینجا در IDE تنظیم کنید
    return z  # متغیرها را در این نقطه بازرسی کنید
```

### profiling برای مسائل عملکرد
```python
import cProfile
import pstats

def slow_function():
    """تابعی با مسائل عملکرد."""
    result = []
    for i in range(10000):
        result.append(i ** 2)  # الحاق ناکارآمد
    return result

# profile تابع
profiler = cProfile.Profile()
profiler.enable()
result = slow_function()
profiler.disable()

# چاپ آمار
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(10)  # ۱۰ تابع برتر
```

### اشکال‌زدایی حافظه
```python
import tracemalloc

def memory_intensive_function():
    """تابعی که از حافظه زیادی استفاده می‌کند."""
    data = []
    for i in range(100000):
        data.append([i] * 1000)  # لیست‌های تو در تو بزرگ ایجاد می‌کند

    return len(data)

# ردیابی استفاده از حافظه
tracemalloc.start()

print(f"حافظه قبل: {tracemalloc.get_traced_memory()[0] / 1024 / 1024:.2f} MB")

result = memory_intensive_function()

print(f"حافظه بعد: {tracemalloc.get_traced_memory()[0] / 1024 / 1024:.2f} MB")

# دریافت کاربران برتر حافظه
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("کاربران برتر حافظه:")
for stat in top_stats[:5]:
    print(stat)
```

## تکنیک‌های پیشرفته اشکال‌زدایی

### اشکال‌زدایی جستجوی باینری
```python
def binary_search_debug(code_lines):
    """استفاده از جستجوی باینری برای ایزوله کردن کد مشکل‌دار."""

    # نیمی از کد را کامنت کنید
    mid = len(code_lines) // 2

    print("تست نیمه اول...")
    # نیمه اول را اجرا کنید
    try:
        exec('\n'.join(code_lines[:mid]))
        print("نیمه اول کار می‌کند - باگ در نیمه دوم")
        # نیمه دوم را اشکال‌زدایی کنید
        binary_search_debug(code_lines[mid:])
    except Exception as e:
        print(f"نیمه اول ناموفق: {e} - باگ در نیمه اول")
        # نیمه اول را اشکال‌زدایی کنید
        binary_search_debug(code_lines[:mid])

# مثال استفاده (مفاهیم)
problematic_code = [
    "x = 1",
    "y = 2",
    "z = x / y",  # اگر y=0 ناموفق خواهد شد
    "print(z)"
]

# در عمل، کد را تغییر می‌دهید تا بخش‌ها را کامنت/آن‌کامنت کنید
```

### monkey patching برای تست
```python
import random

def unreliable_function():
    """تابعی که گاهی ناموفق می‌شود."""
    if random.random() < 0.7:
        raise Exception("ناموفق بودن تصادفی")
    return "موفقیت"

def test_with_monkey_patch():
    """تست با کنترل رفتار تصادفی."""

    # تابع اصلی را ذخیره کنید
    original_random = random.random

    # تست مورد موفقیت
    random.random = lambda: 0.8  # همیشه > 0.7 بازگرداند
    try:
        result = unreliable_function()
        assert result == "موفقیت"
        print("مورد موفقیت: ✓")
    except Exception as e:
        print(f"مورد موفقیت ناموفق: {e}")

    # تست مورد ناموفق
    random.random = lambda: 0.5  # همیشه < 0.7 بازگرداند
    try:
        result = unreliable_function()
        print(f"مورد ناموفق باید استثنا ایجاد کند: {result}")
    except Exception:
        print("مورد ناموفق: ✓")

    # اصلی را بازیابی کنید
    random.random = original_random

test_with_monkey_patch()
```

### decoratorهای ثبت
```python
import functools
import time

def debug_log(func):
    """دکوراتوری که فراخوانی توابع و نتایج را ثبت می‌کند."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__

        # ثبت فراخوانی تابع
        arg_str = ', '.join([repr(arg) for arg in args] +
                          [f"{k}={v!r}" for k, v in kwargs.items()])
        print(f"فراخوانی {func_name}({arg_str})")

        start_time = time.time()

        try:
            result = func(*args, **kwargs)
            end_time = time.time()

            print(f"{func_name} بازگشت {result!r} در {end_time - start_time:.3f}s")
            return result

        except Exception as e:
            end_time = time.time()
            print(f"{func_name} ایجاد {type(e).__name__}: {e} پس از {end_time - start_time:.3f}s")
            raise

    return wrapper

@debug_log
def calculate_fibonacci(n):
    """محاسبه عدد فیبوناچی nام."""
    if n <= 1:
        return n
    return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

# تست با اشکال‌زدایی
result = calculate_fibonacci(5)
```

## بهترین روش‌های اشکال‌زدایی

### اشکال‌زدایی rubber duck
```python
def explain_to_rubber_duck():
    """
    کد خود را خط به خط به یک شی غیرمتحرک توضیح دهید.
    این اغلب خطاهای منطقی در تفکر شما را آشکار می‌کند.
    """
    print("خوب rubber duck، اجازه بده کد را توضیح دهم...")

    # از طریق کد مشکل‌دار قدم بردارید
    data = [1, 2, 3, 4, 5]
    print(f"با داده شروع می‌کنیم: {data}")

    # هر مرحله را توضیح دهید
    for i, item in enumerate(data):
        print(f"به شاخص {i}، آیتم {item} نگاه می‌کنیم")
        print(f"آیا {item} زوج است؟ {item % 2 == 0}")

        if item % 2 == 0:
            print(f"بله، حذف {item}")
            data.remove(item)
            print(f"داده اکنون: {data}")

    print("نتیجه نهایی:", data)
    print("صبر کنید، این درست به نظر نمی‌رسد...")

explain_to_rubber_duck()
```

### کنترل نسخه برای اشکال‌زدایی
```python
# از git bisect برای یافتن زمان معرفی باگ استفاده کنید
"""
git bisect start
git bisect bad     # نسخه فعلی باگ دارد
git bisect good v1.0  # نسخه 1.0 کار می‌کرد
# git یک نسخه میانی را checkout می‌کند
# تست کنید آیا باگ وجود دارد
git bisect bad     # یا git bisect good
# تکرار کنید تا git commit مشکل‌دار را پیدا کند
git bisect reset   # بازگشت به وضعیت اصلی
"""
```

### ایجاد موارد تست مینیمال
```python
def create_minimal_reproduction():
    """کوچک‌ترین کد ممکن که باگ را بازتولید می‌کند ایجاد کنید."""

    # با کد مشکل‌دار کامل شروع کنید
    # قسمت‌هایی که به باگ مربوط نیستند را حذف کنید
    # نام متغیرها و مقادیر را ساده کنید
    # به حذف ادامه دهید تا مورد مینیمال را داشته باشید

    # مثال: بازتولید مینیمال باگ تغییر لیست
    data = [1, 2]  # داده مینیمال که مشکل را نشان می‌دهد

    print("قبل:", data)
    for item in data:
        if item % 2 == 0:
            data.remove(item)  # این باگ را ایجاد می‌کند
    print("بعد:", data)  # [1] - 2 رد شد!

    # اکنون می‌توانید مسئله را واضح ببینید و رفع کنید
```

## نکات کلیدی

۱. **اشکال‌زدایی سیستمی** شامل بازتولید، ایزوله، شناسایی و رفع می‌شود
۲. **دستورات print و ثبت** دید به اجرای برنامه فراهم می‌کنند
۳. **اشکال‌زداها** اجازه اجرای مرحله به مرحله و بازرسی وضعیت می‌دهند
۴. **assertions** خطاها را زود در توسعه می‌گیرند
۵. **تست** با موارد تست جامع از regressions جلوگیری می‌کند
۶. **اشکال‌زدایی rubber duck** خطاهای منطقی را شناسایی می‌کند

## مطالعه بیشتر
- مستندات اشکال‌زدای پایتون
- بهترین روش‌های ثبت
- چارچوب‌های تست واحد (pytest, unittest)
- ابزارهای profiling و تحلیل عملکرد
- تکنیک‌های اشکال‌زدایی در پارادایم‌های برنامه‌نویسی مختلف