# مبانی کار با فایل: خواندن و نوشتن فایل‌های متنی

## مقدمه: چرا فایل‌ها مهم هستند

برنامه‌ها نیاز دارند چیزها را حتی بعد از بسته شدن به خاطر بسپارند. فایل‌ها به شما اجازه می‌دهند:
- **ذخیره داده** که بعد از پایان برنامه باقی بماند
- **خواندن داده** که توسط برنامه‌های دیگر ایجاد شده
- **اشتراک اطلاعات** بین اجراهای مختلف برنامه
- **پردازش مقادیر زیاد** داده که در حافظه جا نمی‌شوند

### استعاره فایل

فایل را مثل یک دفترچه در نظر بگیرید:
- آن را **باز** می‌کنید برای خواندن یا نوشتن
- آنچه قبلاً نوشته شده را **می‌خوانید**
- اطلاعات جدید را **می‌نویسید**
- وقتی تمام شد آن را **می‌بندید**

---

## بخش ۱: درک مسیرهای فایل

### مسیر فایل چیست؟

مسیر به پایتون می‌گوید فایل را کجا در کامپیوتر پیدا کند.

```
Windows: C:\Users\Alice\Documents\data.txt
Mac/Linux: /Users/Alice/Documents/data.txt
```

### انواع مسیر

```python
# مسیر مطلق - از ریشه شروع می‌شود
c:\Users\Alice\Documents\file.txt       # Windows
/home/alice/documents/file.txt            # Linux/Mac

# مسیر نسبی - از مکان فعلی شروع می‌شود
file.txt                                   # در پوشه فعلی
../data/file.txt                          # یک پوشه بالا برو، بعد وارد data شو
./file.txt                                # صریحاً پوشه فعلی
```

### کار با مسیرها در پایتون

```python
import os

# گرفتن پوشه کاری فعلی
print(os.getcwd())  # الان کجا هستم؟

# بررسی وجود فایل
if os.path.exists("data.txt"):
    print("File exists!")
else:
    print("File not found")

# اتصال امن مسیرها (\ و / را خودکار مدیریت می‌کند)
folder = "data"
filename = "results.txt"
full_path = os.path.join(folder, filename)
print(full_path)  # data/results.txt یا data\results.txt

# گرفتن اطلاعات فایل
if os.path.exists("data.txt"):
    size = os.path.getsize("data.txt")
    print(f"File size: {size} bytes")
```

---

## بخش ۲: خواندن فایل‌ها

### روش ۱: دستور `with` (بهترین روش)

```python
# خواندن کل فایل یک‌باره
with open("story.txt", "r") as file:
    content = file.read()
    print(content)

# فایل به‌صورت خودکار بسته می‌شود وقتی از بلاک 'with' خارج می‌شوید!
```

**چرا از `with` استفاده کنیم؟**
- به‌صورت خودکار فایل را می‌بندد (حتی اگر خطا رخ دهد)
- کد تمیزتر و ایمن‌تر
- برای همه عملیات فایل توصیه می‌شود

### روش ۲: خواندن خط به خط

```python
# پردازش فایل یک خط در هر بار (کارآمد در حافظه)
with open("story.txt", "r") as file:
    for line_number, line in enumerate(file, 1):
        print(f"Line {line_number}: {line.strip()}")
```

**چه موقع خط به خط استفاده کنیم:**
- فایل‌های بزرگ (همه چیز را در حافظه بارگذاری نمی‌کند)
- پردازش فایل‌ها به‌عنوان جریان
- تحلیل فایل‌های لاگ

### روش ۳: خواندن همه خطوط در یک لیست

```python
# گرفتن همه خطوط به‌عنوان یک لیست
with open("story.txt", "r") as file:
    lines = file.readlines()
    print(f"Total lines: {len(lines)}")
    print(f"First line: {lines[0]}")
```

### مقایسه روش‌های خواندن

| روش | بهترین برای | استفاده حافظه |
|-----|-------------|---------------|
| `read()` | فایل‌های کوچک، نیاز به کل محتوا | بارگذاری کل فایل |
| `readline()` | خواندن یک خط در هر بار | حداقل |
| `readlines()` | نیاز به لیست همه خطوط | بارگذاری کل فایل |
| `for line in file` | فایل‌های بزرگ، پردازش | حداقل |

### مدیریت خطوط جدید

```python
text = "Hello\nWorld\n"
print(f"Original: {repr(text)}")

# strip() فاصله‌ها از جمله خطوط جدید را حذف می‌کند
print(f"Stripped: {repr(text.strip())}")

# rstrip() فقط از انتها حذف می‌کند
print(f"Right stripped: {repr(text.rstrip())}")
```

---

## بخش ۳: نوشتن فایل‌ها

### نوشتن متن در فایل

```python
# 'w' mode = نوشتن (فایل جدید می‌سازد یا فایل موجود را بازنویسی می‌کند)
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is line 2\n")
    file.write("This is line 3\n")

print("File written successfully!")
```

**هشدار**: حالت `'w'` محتوای موجود را حذف می‌کند! با احتیاط استفاده کنید.

### افزودن به فایل

```python
# 'a' mode = افزودن (به انتهای فایل موجود اضافه می‌کند)
with open("output.txt", "a") as file:
    file.write("This line is appended!\n")

print("Content appended!")
```

### نوشتن چند خط یک‌باره

```python
lines = [
    "First line\n",
    "Second line\n",
    "Third line\n"
]

with open("output.txt", "w") as file:
    file.writelines(lines)

print("All lines written!")
```

### راهنمای حالت‌های فایل

| حالت | معنی | فایل وجود دارد | فایل وجود ندارد |
|------|------|----------------|-----------------|
| `'r'` | خواندن | باز می‌کند | خطا |
| `'w'` | نوشتن | بازنویسی می‌کند | جدید می‌سازد |
| `'a'` | افزودن | به انتها اضافه می‌کند | جدید می‌سازد |
| `'r+'` | خواندن + نوشتن | باز می‌کند | خطا |
| `'x'` | ایجاد انحصاری | خطا | جدید می‌سازد |

---

## بخش ۴: عملیات عملی فایل

### مثال ۱: شمارش کلمات در فایل

```python
def count_words_in_file(filename):
    """Count total words in a text file."""
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return 0

# Usage
count = count_words_in_file("story.txt")
print(f"Word count: {count}")
```

### مثال ۲: کپی کردن فایل

```python
def copy_file(source, destination):
    """Copy contents of one file to another."""
    try:
        with open(source, 'r') as src:
            content = src.read()

        with open(destination, 'w') as dst:
            dst.write(content)

        print(f"Copied {source} to {destination}")
        return True

    except FileNotFoundError:
        print(f"Error: Source file {source} not found")
        return False
    except PermissionError:
        print(f"Error: Permission denied writing to {destination}")
        return False

# Usage
copy_file("original.txt", "backup.txt")
```

### مثال ۳: پردازش داده CSV

```python
def process_student_grades(filename):
    """Read student grades from CSV-like file."""
    students = []

    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, 1):
                line = line.strip()
                if not line:  # Skip empty lines
                    continue

                parts = line.split(',')
                if len(parts) < 2:
                    print(f"Warning: Invalid data on line {line_number}")
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
                    print(f"Warning: Non-numeric score on line {line_number}")

    except FileNotFoundError:
        print(f"Error: File {filename} not found")

    return students

# Usage
students = process_student_grades("grades.txt")
for student in students:
    print(f"{student['name']}: {student['average']:.1f}")
```

### مثال ۴: نوشتن گزارش

```python
def generate_report(students, output_file):
    """Generate a formatted report file."""
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

        # Add summary
        if students:
            class_avg = sum(s['average'] for s in students) / len(students)
            file.write("-" * 50 + "\n")
            file.write(f"Class Average: {class_avg:.1f}\n")

    print(f"Report saved to {output_file}")

# Usage
students = process_student_grades("grades.txt")
generate_report(students, "report.txt")
```

---

## بخش ۵: مدیریت خطا

### خطاهای رایج فایل

```python
def safe_file_operations(filename):
    """Demonstrate handling common file errors."""

    # Error 1: فایل وجود ندارد
    try:
        with open("nonexistent.txt", 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print("That file doesn't exist!")

    # Error 2: عدم دسترسی
    try:
        with open("/etc/passwd", 'w') as file:  # فایل سیستمی
            file.write("test")
    except PermissionError:
        print("You don't have permission to write there!")

    # Error 3: فایل یک پوشه است
    try:
        with open(".", 'r') as file:  # پوشه فعلی
            content = file.read()
    except IsADirectoryError:
        print("That's a directory, not a file!")

    # Error 4: دیسک پر (نادر اما ممکن)
    try:
        with open("huge_file.txt", 'w') as file:
            file.write("x" * 100000000000)  # خیلی بزرگ!
    except OSError as e:
        print(f"OS Error: {e}")
```

### الگوی خواندن ایمن فایل

```python
def read_file_safely(filename):
    """Read file with comprehensive error handling."""
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

# Usage
content, error = read_file_safely("data.txt")
if error:
    print(f"Error: {error}")
else:
    print(f"Content: {content[:100]}...")
```

---

## بخش ۶: بهترین شیوه‌ها

### کارها و کارهای نکن

**✅ انجام بدهید:**
```python
# استفاده از دستور 'with' (بستن خودکار فایل)
with open("file.txt", 'r') as file:
    data = file.read()

# بررسی وجود فایل قبل از خواندن
import os
if os.path.exists("file.txt"):
    with open("file.txt", 'r') as file:
        data = file.read()

# استفاده از مدیریت خطای خاص
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

# از except خالی استفاده نکنید
except:  # خیلی گسترده!
    print("Error")

# خطاها را بی‌صدا رد نکنید
try:
    os.remove("file.txt")
except:
    pass  # خطا نادیده گرفته شد!
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

### تمرین ۱: تحلیل‌گر فایل

یک تابع بسازید که یک فایل متنی را تحلیل کرده و آمار برمی‌گرداند:
- تعداد خطوط
- تعداد کلمات
- تعداد کاراکترها
- میانگین کلمات در هر خط

```python
def analyze_file(filename):
    """Analyze a text file and return statistics."""
    # Your code here
    pass

# Test
stats = analyze_file("story.txt")
print(f"Lines: {stats['lines']}")
print(f"Words: {stats['words']}")
print(f"Characters: {stats['chars']}")
```

### تمرین ۲: جستجو در فایل

یک تابع بسازید که یک کلمه را در فایل جستجو کرده و همه خطوط حاوی آن را برمی‌گرداند:

```python
def search_in_file(filename, search_word):
    """Find all lines containing search_word."""
    # Your code here
    pass

# Test
results = search_in_file("story.txt", "python")
for line_num, line in results:
    print(f"Line {line_num}: {line}")
```

### تمرین ۳: مبدل داده

یک فرمت داده ساده را به فرمت دیگر تبدیل کنید:

```python
def convert_data(input_file, output_file):
    """
    Read input.txt with format:
        Alice,25
        Bob,30
    Write output.txt with format:
        Name: Alice, Age: 25
        Name: Bob, Age: 30
    """
    # Your code here
    pass
```

---

## نکات کلیدی

1. **همیشه از `with` استفاده کنید** - به‌صورت خودکار فایل‌ها را می‌بندد
2. **خطاها را مدیریت کنید** - فایل‌ها ممکن است وجود نداشته باشند یا قابل دسترسی نباشند
3. **حالت مناسب را انتخاب کنید** - 'r' برای خواندن، 'w' برای نوشتن (با احتیاط!)، 'a' برای افزودن
4. **از مسیرهای نسبی استفاده کنید** - کد را قابل حمل‌تر می‌کند
5. **فایل‌های بزرگ را خط به خط پردازش کنید** - حافظه را ذخیره می‌کند
6. **وجود فایل را بررسی کنید** - قبل از تلاش برای باز کردن

## راهنمای سریع

```python
# خواندن
with open("file.txt", 'r') as f:
    content = f.read()        # کل محتوا
    lines = f.readlines()     # لیست خطوط
    for line in f:            # خط به خط
        process(line)

# نوشتن
with open("file.txt", 'w') as f:  # بازنویسی می‌کند!
    f.write("text\n")
    f.writelines(["line1\n", "line2\n"])

with open("file.txt", 'a') as f:  # اضافه می‌کند
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
- **تمرین**: یک برنامه بسازید که یک پوشه از فایل‌های متنی را پردازش کند
- **چالش**: یک موتور جستجوی متن ساده بسازید
- **کاوش**: درباره مدیریت فایل‌های باینری یاد بگیرید
