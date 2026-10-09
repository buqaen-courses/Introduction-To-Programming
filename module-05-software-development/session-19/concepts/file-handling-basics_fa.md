# مبانی کار با فایل: خواندن و نوشتن فایل‌های متنی

## مقدمه: چرا فایل‌ها مهم‌اند

برنامه‌ها باید چیزها را حتی پس از بسته شدن به یاد بسپارند. فایل‌ها به شما اجازه می‌دهند:
- **داده ذخیره کنید** که بعد از پایان برنامه باقی می‌ماند
- **داده بخوانید** که برنامه دیگری ساخته است
- **اطلاعات به اشتراک بگذارید** بین اجراهای مختلف برنامه‌تان
- **حجم زیادی از داده را پردازش کنید** که در حافظه جا نمی‌شود

### استعاره فایل

فایل را مثل یک دفترچه فکر کنید:
- آن را **باز** می‌کنید تا بخوانید یا بنویسید
- آنچه از قبل هست را **می‌خوانید**
- اطلاعات تازه **می‌نویسید**
- وقتی کارتان تمام شد آن را **می‌بندید**

---

## بخش ۱: فهم مسیرهای فایل

### مسیر فایل چیست؟

مسیر به پایتون می‌گوید فایل را کجا روی کامپیوتر پیدا کند.

```
Windows: C:\Users\Alice\Documents\data.txt
Mac/Linux: /Users/Alice/Documents/data.txt
```

### انواع مسیر

```python
# مسیر مطلق - از ریشه شروع می‌شود
c:\\Users\\Alice\\Documents\\file.txt       # Windows
/home/alice/documents/file.txt            # Linux/Mac

# مسیر نسبی - از محل جاری شروع می‌شود
file.txt                                   # در پوشه جاری
../data/file.txt                          # یک پوشه بالا، بعد داخل data
./file.txt                                # صراحتاً پوشه جاری
```

### کار با مسیرها در پایتون

```python
import os

# گرفتن پوشه کاری جاری
print(os.getcwd())  # الان کجام؟

# بررسی وجود فایل
if os.path.exists("data.txt"):
    print("File exists!")
else:
    print("File not found")

# اتصال مسیرها به شکل ایمن (خودش به \ و / رسیدگی می‌کند)
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

### روش ۱: دستور `with` (بهترین راه)

```python
# خواندن کل فایل یکجا
with open("story.txt", "r") as file:
    content = file.read()
    print(content)

# فایل وقتی از بلوک 'with' خارج شوید خودکار بسته می‌شود!
```

**چرا از `with` استفاده کنیم؟**
- فایل را خودکار می‌بندد (حتی اگر خطا رخ دهد)
- کد تمیزتر و ایمن‌تر است
- برای همه عملیات فایل توصیه می‌شود

### روش ۲: خواندن خط‌به‌خط

```python
# پردازش فایل یک خط در هر بار (کم‌مصرف حافظه)
with open("story.txt", "r") as file:
    for line_number, line in enumerate(file, 1):
        print(f"Line {line_number}: {line.strip()}")
```

**چه موقع خط‌به‌خط؟**
- فایل‌های بزرگ (همه‌چیز در حافظه بارگذاری نمی‌شود)
- پردازش فایل به‌صورت جریان
- تحلیل فایل لاگ

### روش ۳: خواندن همه خطوط در یک فهرست

```python
# گرفتن همه خطوط به‌صورت فهرست
with open("story.txt", "r") as file:
    lines = file.readlines()
    print(f"Total lines: {len(lines)}")
    print(f"First line: {lines[0]}")
```

### مقایسه روش‌های خواندن

| روش | بهترین برای | مصرف حافظه |
|-----|-------------|------------|
| `read()` | فایل کوچک، نیاز به کل محتوا | کل فایل را بارگذاری می‌کند |
| `readline()` | خواندن یک خط در هر بار | کمینه |
| `readlines()` | نیاز به فهرست همه خطوط | کل فایل را بارگذاری می‌کند |
| `for line in file` | فایل بزرگ، پردازش | کمینه |

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

## بخش ۳: نوشتن فایل

### نوشتن متن در فایل

```python
# حالت 'w' = نوشتن (فایل تازه می‌سازد یا روی موجود می‌نویسد)
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is line 2\n")
    file.write("This is line 3\n")

print("File written successfully!")
```

**هشدار**: حالت `'w'` محتوای موجود را پاک می‌کند! با احتیاط استفاده کنید.

### افزودن به فایل

```python
# حالت 'a' = افزودن (به انتهای فایل موجود اضافه می‌کند)
with open("output.txt", "a") as file:
    file.write("This line is appended!\n")

print("Content appended!")
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

print("All lines written!")
```

### مرجع حالت‌های فایل

| حالت | معنا | فایل موجود | فایل ناموجود |
|------|------|------------|--------------|
| `'r'` | خواندن | بازش می‌کند | خطا |
| `'w'` | نوشتن | بازنویسی می‌کند | تازه می‌سازد |
| `'a'` | افزودن | به انتها اضافه می‌کند | تازه می‌سازد |
| `'r+'` | خواندن + نوشتن | بازش می‌کند | خطا |
| `'x'` | ساخت انحصاری | خطا | تازه می‌سازد |

---

## بخش ۴: عملیات کاربردی فایل

### مثال ۱: شمردن کلمات یک فایل

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
                if not line:  # رد کردن خطوط خالی
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

        # افزودن خلاصه
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

    # خطای ۱: فایل وجود ندارد
    try:
        with open("nonexistent.txt", 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print("That file doesn't exist!")

    # خطای ۲: دسترسی رد می‌شود
    try:
        with open("/etc/passwd", 'w') as file:  # فایل سیستم
            file.write("test")
    except PermissionError:
        print("You don't have permission to write there!")

    # خطای ۳: فایل در واقع پوشه است
    try:
        with open(".", 'r') as file:  # پوشه جاری
            content = file.read()
    except IsADirectoryError:
        print("That's a directory, not a file!")

    # خطای ۴: دیسک پر (نادر ولی ممکن است)
    try:
        with open("huge_file.txt", 'w') as file:
            file.write("x" * 100000000000)  # خیلی بزرگ!
    except OSError as e:
        print(f"OS Error: {e}")
```

### الگوی ایمن خواندن فایل

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

## بخش ۶: بهترین روش‌ها

### چیزهایی که باید و نباید کرد

**✅ باید:**
```python
# از دستور 'with' استفاده کنید (فایل خودکار بسته می‌شود)
with open("file.txt", 'r') as file:
    data = file.read()

# پیش از خواندن وجود فایل را بررسی کنید
import os
if os.path.exists("file.txt"):
    with open("file.txt", 'r') as file:
        data = file.read()

# مدیریت استثنای مشخص
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
```

**❌ نباید:**
```python
# فایل را نباید بدون بستن رها کنید
file = open("file.txt", 'r')
data = file.read()
# Missing: file.close()

# از except خالی استفاده نکنید
except:  # خیلی گسترده!
    print("Error")

# خطاها را بی‌صدا نادیده نگیرید
try:
    os.remove("file.txt")
except:
    pass  # خطا نادیده گرفته شد!
```

### کار با انواع مختلف فایل

```python
# فایل JSON (داده ساخت‌یافته)
import json

# خواندن JSON
with open("data.json", 'r') as file:
    data = json.load(file)

# نوشتن JSON
with open("output.json", 'w') as file:
    json.dump(data, file, indent=2)

# فایل CSV (داده جدولی)
import csv

# خواندن CSV
with open("data.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

---

## تمرین‌ها

### تمرین ۱: تحلیلگر فایل
تابعی بسازید که یک فایل متنی را تحلیل کند و آمارش را برگرداند:
- تعداد کل خطوط
- تعداد کل کلمات
- تعداد کل کاراکترها
- میانگین کلمات در هر خط

```python
def analyze_file(filename):
    """Analyze a text file and return statistics."""
    # کد شما اینجا
    pass

# Test
stats = analyze_file("story.txt")
print(f"Lines: {stats['lines']}")
print(f"Words: {stats['words']}")
print(f"Characters: {stats['chars']}")
```

### تمرین ۲: جست‌وجو در فایل
تابعی بسازید که یک کلمه را در فایل بگردد و همه خطوطی را که آن را دارند برگرداند:

```python
def search_in_file(filename, search_word):
    """Find all lines containing search_word."""
    # کد شما اینجا
    pass

# Test
results = search_in_file("story.txt", "python")
for line_num, line in results:
    print(f"Line {line_num}: {line}")
```

###exercício ۳: مبدل داده
یک قالب داده ساده را به قالب دیگر تبدیل کنید:

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
    # کد شما اینجا
    pass
```

---

## نکات کلیدی

۱. **همیشه از `with` استفاده کنید**: فایل را خودکار می‌بندد
۲. **خطاها را مدیریت کنید**: ممکن است فایل وجود نداشته باشد یا قابل دسترسی نباشد
۳. **حالت درست را انتخاب کنید**: 'r' برای خواندن، 'w' برای نوشتن (با احتیاط!)، 'a' برای افزودن
۴. **از مسیر نسبی استفاده کنید**: کد قابل حمل می‌شود
۵. **فایل بزرگ را خط‌به‌خط پردازش کنید**: حافظه сох می‌کند
۶. **وجود فایل را بررسی کنید**: پیش از تلاش برای باز کردنش

## مرجع سریع

```python
# خواندن
with open("file.txt", 'r') as f:
    content = f.read()        # کل محتوا
    lines = f.readlines()     # فهرست خطوط
    for line in f:            # خط به خط
        process(line)

# نوشتن
with open("file.txt", 'w') as f:  # بازنویسی می‌کند!
    f.write("text\n")
    f.writelines(["line1\n", "line2\n"])

with open("file.txt", 'a') as f:  # افزودن می‌کند
    f.write("more text\n")

# بررسی
import os
os.path.exists("file.txt")   # فایل وجود دارد؟
os.path.getsize("file.txt")  # حجم فایل
os.path.join("folder", "file.txt")  # اتصال ایمن مسیر
```

---

## مطالعه بیشتر

- **بعدی**: جلسه ۲۰، ماژول‌ها و سازماندهی کد
- **تمرین**: برنامه‌ای بسازید که یک پوشه از فایل‌های متنی را پردازش کند
- **چالش**: یک موتور جست‌وجوی متنی ساده بسازید
- **کاوش کنید**: درباره کار با فایل باینری یاد بگیرید