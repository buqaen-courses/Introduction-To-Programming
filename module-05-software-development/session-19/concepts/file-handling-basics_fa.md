# اصول کار با فایل: خواندن و نوشتن فایل‌های متنی

## مقدمه: چرا فایل‌ها مهم هستند

برنامه‌ها نیاز دارند حتی پس از بسته شدن، اطلاعات را به خاطر بسپارند. فایل‌ها به شما اجازه می‌دهند:
- **ذخیره داده** که پس از پایان برنامه باقی بماند
- **خواندن داده** ایجاد شده توسط برنامه‌های دیگر
- **اشتراک اطلاعات** بین اجراهای مختلف برنامه
- **پردازش حجم زیادی** از داده که در حافظه جا نمی‌شود

### استعاره فایل

فایل را مانند یک دفترچه در نظر بگیرید:
- آن را **باز** می‌کنید برای خواندن یا نوشتن
- آنچه قبلاً نوشته شده را **می‌خوانید**
- اطلاعات جدید **می‌نویسید**
- پس از اتمام آن را **می‌بندید**

---

## بخش ۱: درک مسیرهای فایل

### مسیر فایل چیست؟

یک مسیر به پایتون می‌گوید فایل را در کامپیوتر کجا پیدا کند.

```
ویندوز: C:\Users\Alice\Documents\data.txt
مک/لینوکس: /Users/Alice/Documents/data.txt
```

### انواع مسیرها

```python
# مسیر مطلق - از ریشه شروع می‌شود
c:\Users\Alice\Documents\file.txt       # ویندوز
/home/alice/documents/file.txt            # لینوکس/مک

# مسیر نسبی - از محل فعلی شروع می‌شود
file.txt                                   # در پوشه فعلی
../data/file.txt                          # یک پوشه بالا برو، سپس وارد data شو
./file.txt                                # صریحاً پوشه فعلی
```

### کار با مسیرها در پایتون

```python
import os

# دریافت پوشه کاری فعلی
print(os.getcwd())  # الان کجا هستم؟

# بررسی وجود فایل
if os.path.exists("data.txt"):
    print("فایل وجود دارد!")
else:
    print("فایل یافت نشد")

# اتصال امن مسیرها (به صورت خودکار \ و / را مدیریت می‌کند)
folder = "data"
filename = "results.txt"
full_path = os.path.join(folder, filename)
print(full_path)  # data/results.txt یا data\results.txt

# دریافت اطلاعات فایل
if os.path.exists("data.txt"):
    size = os.path.getsize("data.txt")
    print(f"اندازه فایل: {size} بایت")
```

---

## بخش ۲: خواندن فایل‌ها

### روش ۱: دستور `with` (بهترین روش)

```python
# خواندن کل فایل یکجا
with open("story.txt", "r") as file:
    content = file.read()
    print(content)

# فایل به صورت خودکار پس از خروج از بلوک 'with' بسته می‌شود!
```

**چرا از `with` استفاده کنیم؟**
- به صورت خودکار فایل را می‌بندد (حتی اگر خطا رخ دهد)
- کد تمیزتر و ایمن‌تر
- برای تمام عملیات فایل توصیه می‌شود

### روش ۲: خواندن خط به خط

```python
# پردازش فایل خط به خط (کارآمد از نظر حافظه)
with open("story.txt", "r") as file:
    for line_number, line in enumerate(file, 1):
        print(f"خط {line_number}: {line.strip()}")
```

**چه زمانی از خط به خط استفاده کنیم:**
- فایل‌های بزرگ (همه چیز را در حافظه بارگذاری نمی‌کند)
- پردازش فایل‌ها به عنوان جریان
- تحلیل فایل‌های لاگ

### روش ۳: خواندن تمام خطوط در یک لیست

```python
# دریافت تمام خطوط به عنوان لیست
with open("story.txt", "r") as file:
    lines = file.readlines()
    print(f"تعداد خطوط: {len(lines)}")
    print(f"اولین خط: {lines[0]}")
```

### مقایسه روش‌های خواندن

| روش | مناسب برای | مصرف حافظه |
|-----|----------|-----------|
| `read()` | فایل‌های کوچک، نیاز به تمام محتوا | بارگذاری کل فایل |
| `readline()` | خواندن یک خط در هر بار | حداقل |
| `readlines()` | نیاز به لیست تمام خطوط | بارگذاری کل فایل |
| `for line in file` | فایل‌های بزرگ، پردازش | حداقل |

### مدیریت کاراکترهای newline

```python
text = "Hello\nWorld\n"
print(f"اصلی: {repr(text)}")

# strip() فاصله‌ها و newline را حذف می‌کند
print(f"strip شده: {repr(text.strip())}")

# rstrip() فقط از انتها حذف می‌کند
print(f"rstrip شده: {repr(text.rstrip())}")
```

---

## بخش ۳: نوشتن فایل‌ها

### نوشتن متن در فایل

```python
# 'w' mode = نوشتن (فایل جدید ایجاد می‌کند یا فایل موجود را بازنویسی می‌کند)
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is line 2\n")
    file.write("This is line 3\n")

print("فایل با موفقیت نوشته شد!")
```

**هشدار**: حالت `'w'` محتوای موجود را حذف می‌کند! با احتیاط استفاده کنید.

### افزودن به فایل

```python
# 'a' mode = افزودن (به انتهای فایل موجود اضافه می‌کند)
with open("output.txt", "a") as file:
    file.write("This line is appended!\n")

print("محتوا افزوده شد!")
```

### نوشتن چند خط یکجا

```python
lines = [
    "First line\n",
    "Second line\n",
    "Third line\n"
]

with open("output.txt", "w") as file:
    file.writelines(lines)

print("تمام خطوط نوشته شد!")
```

### مرجع حالت‌های فایل

| حالت | معنی | فایل موجود | فایل وجود ندارد |
|------|------|-----------|----------------|
| `'r'` | خواندن | باز می‌کند | خطا |
| `'w'` | نوشتن | بازنویسی می‌کند | ایجاد جدید |
| `'a'` | افزودن | به انتها اضافه می‌کند | ایجاد جدید |
| `'r+'` | خواندن + نوشتن | باز می‌کند | خطا |
| `'x'` | ایجاد انحصاری | خطا | ایجاد جدید |

---

## بخش ۴: عملیات عملی فایل

### مثال ۱: شمارش کلمات در فایل

```python
def count_words_in_file(filename):
    """شمارش کل کلمات در یک فایل متنی."""
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print(f"خطا: {filename} یافت نشد")
        return 0

# استفاده
count = count_words_in_file("story.txt")
print(f"تعداد کلمات: {count}")
```

### مثال ۲: کپی کردن فایل

```python
def copy_file(source, destination):
    """کپی محتوای یک فایل به فایل دیگر."""
    try:
        with open(source, 'r') as src:
            content = src.read()

        with open(destination, 'w') as dst:
            dst.write(content)

        print(f"کپی شد {source} به {destination}")
        return True

    except FileNotFoundError:
        print(f"خطا: فایل مبدأ {source} یافت نشد")
        return False
    except PermissionError:
        print(f"خطا: عدم دسترسی برای نوشتن در {destination}")
        return False

# استفاده
copy_file("original.txt", "backup.txt")
```

### مثال ۳: پردازش داده CSV

```python
def process_student_grades(filename):
    """خواندن نمرات دانشجویان از فایل CSV-like."""
    students = []

    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, 1):
                line = line.strip()
                if not line:  # رد کردن خطوط خالی
                    continue

                parts = line.split(',')
                if len(parts) < 2:
                    print(f"هشدار: داده نامعتبر در خط {line_number}")
                    continue

                name = parts[0]
                try:
                    scores = [int(score) for score in parts[1:]]
                    average = sum(scores) / len(scores)

                    students.append({
                        'name': name,
                        'scores': scores,
                        'average': average
                    })
                except ValueError:
                    print(f"هشدار: نمره غیرعددی در خط {line_number}")

    except FileNotFoundError:
        print(f"خطا: فایل {filename} یافت نشد")

    return students

# استفاده
students = process_student_grades("grades.txt")
for student in students:
    print(f"{student['name']}: {student['average']:.1f}")
```

### مثال ۴: نوشتن گزارش

```python
def generate_report(students, output_file):
    """ایجاد فایل گزارش فرمت‌بندی شده."""
    with open(output_file, 'w') as file:
        file.write("STUDENT GRADE REPORT\n")
        file.write("=" * 50 + "\n\n")

        for student in students:
            name = student['name']
            avg = student['average']
            status = "PASS" if avg >= 60 else "FAIL"

            file.write(f"Student: {name}\n")
            file.write(f"  Average: {avg:.1f}\n")
            file.write(f"  Status: {status}\n\n")

        # اضافه کردن خلاصه
        if students:
            class_avg = sum(s['average'] for s in students) / len(students)
            file.write("-" * 50 + "\n")
            file.write(f"Class Average: {class_avg:.1f}\n")

    print(f"گزارش در {output_file} ذخیره شد")

# استفاده
students = process_student_grades("grades.txt")
generate_report(students, "report.txt")
```

---

## بخش ۵: مدیریت خطا

### خطاهای رایج فایل

```python
def safe_file_operations(filename):
    """نمایش مدیریت خطاهای رایج فایل."""

    # خطای ۱: فایل وجود ندارد
    try:
        with open("nonexistent.txt", 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print("That file doesn't exist!")

    # خطای ۲: عدم دسترسی
    try:
        with open("/etc/passwd", 'w') as file:  # فایل سیستمی
            file.write("test")
    except PermissionError:
        print("You don't have permission to write there!")

    # خطای ۳: فایل یک دایرکتوری است
    try:
        with open(".", 'r') as file:  # دایرکتوری فعلی
            content = file.read()
    except IsADirectoryError:
        print("That's a directory, not a file!")

    # خطای ۴: دیسک پر (ندرت اما ممکن)
    try:
        with open("huge_file.txt", 'w') as file:
            file.write("x" * 100000000000)  # خیلی بزرگ!
    except OSError as e:
        print(f"OS Error: {e}")
```

### الگوی خواندن امن فایل

```python
def read_file_safely(filename):
    """خواندن فایل با مدیریت جامع خطا."""
    try:
        with open(filename, 'r') as file:
            return file.read(), None  # (content, error)

    except FileNotFoundError:
        return None, "File not found"
    except PermissionError:
        return None, "Permission denied"
    except UnicodeDecodeError:
        return None, "File is not text (might be binary)"
    except Exception as e:
        return None, f"Unexpected error: {e}"

# استفاده
content, error = read_file_safely("data.txt")
if error:
    print(f"Error: {error}")
else:
    print(f"Content: {content[:100]}...")
```

---

## بخش ۶: بهترین شیوه‌ها

### انجام دهید و ندهید

**✅ انجام دهید:**
```python
# از دستور with استفاده کنید (فایل را خودکار می‌بندد)
with open("file.txt", 'r') as file:
    data = file.read()

# قبل از خواندن بررسی کنید فایل وجود دارد
import os
if os.path.exists("file.txt"):
    with open("file.txt", 'r') as file:
        data = file.read()

# از مدیریت استثناء خاص استفاده کنید
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
```

**❌ انجام ندهید:**
```python
# فراموش نکنید فایل‌ها را ببندید
file = open("file.txt", 'r')
data = file.read()
# Missing: file.close()

# از بلوک‌های except خالی استفاده نکنید
except:  # خیلی گسترده!
    print("Error")

# خطاها را بی‌صدا نادیده نگیرید
try:
    os.remove("file.txt")
except:
    pass  # Error ignored!
```

### کار با انواع مختلف فایل

```python
# فایل‌های JSON (داده ساختاریافته)
import json

# خواندن JSON
with open("data.json", 'r') as file:
    data = json.load(file)

# نوشتن JSON
with open("output.json", 'w') as file:
    json.dump(data, file, indent=2)

# فایل‌های CSV (داده جدولی)
import csv

# خواندن CSV
with open("data.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

---

## تمرین‌های عملی

### تمرین ۱: تحلیلگر فایل

یک تابع ایجاد کنید که یک فایل متنی را تحلیل و آمار بازگرداند:
- تعداد خطوط
- تعداد کلمات
- تعداد کاراکترها
- میانگین کلمات در هر خط

```python
def analyze_file(filename):
    """تحلیل یک فایل متنی و بازگرداندن آمار."""
    # کد شما اینجا
    pass

# تست
stats = analyze_file("story.txt")
print(f"Lines: {stats['lines']}")
print(f"Words: {stats['words']}")
print(f"Characters: {stats['chars']}")
```

### تمرین ۲: جستجو در فایل

یک تابع ایجاد کنید که یک کلمه را در فایل جستجو و تمام خطوط حاوی آن را بازگرداند:

```python
def search_in_file(filename, search_word):
    """یافتن تمام خطوط حاوی search_word."""
    # کد شما اینجا
    pass

# تست
results = search_in_file("story.txt", "python")
for line_num, line in results:
    print(f"Line {line_num}: {line}")
```

### تمرین ۳: تبدیل‌کننده داده

یک فرمت داده ساده را به فرمت دیگر تبدیل کنید:

```python
def convert_data(input_file, output_file):
    """
    خواندن input.txt با فرمت:
        Alice,25
        Bob,30
    نوشتن output.txt با فرمت:
        Name: Alice, Age: 25
        Name: Bob, Age: 30
    """
    # کد شما اینجا
    pass
```

---

## نکات کلیدی

1. **همیشه از `with` استفاده کنید** - به صورت خودکار فایل‌ها را می‌بندد
2. **خطاها را مدیریت کنید** - فایل‌ها ممکن است وجود نداشته باشند یا قابل دسترس نباشند
3. **حالت مناسب را انتخاب کنید** - 'r' برای خواندن، 'w' برای نوشتن (با احتیاط!)، 'a' برای افزودن
4. **از مسیرهای نسبی استفاده کنید** - کد را قابل حمل‌تر می‌کند
5. **فایل‌های بزرگ را خط به خط پردازش کنید** - حافظه را ذخیره می‌کند
6. **بررسی وجود فایل** - قبل از تلاش برای باز کردن

## مرجع سریع

```python
# خواندن
with open("file.txt", 'r') as f:
    content = f.read()        # تمام محتوا
    lines = f.readlines()     # لیست خطوط
    for line in f:            # خط به خط
        process(line)

# نوشتن
with open("file.txt", 'w') as f:  # بازنویسی می‌کند!
    f.write("text\n")
    f.writelines(["line1\n", "line2\n"])

with open("file.txt", 'a') as f:  # افزودن
    f.write("more text\n")

# بررسی
import os
os.path.exists("file.txt")   # فایل وجود دارد؟
os.path.getsize("file.txt")  # اندازه فایل
os.path.join("folder", "file.txt")  # اتصال امن مسیر
```

---

## مطالعه بیشتر

- **بعدی**: جلسه ۲۰ - ماژول‌ها و سازماندهی کد
- **تمرین**: ایجاد برنامه‌ای که یک پوشه از فایل‌های متنی را پردازش می‌کند
- **چالش**: ساخت موتور جستجوی متن ساده
- **کاوش**: آموختن درباره مدیریت فایل‌های باینری
