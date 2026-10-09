# پردازش متن: تحلیل و دستکاری متن

## پردازش متن چیست؟

**پردازش متن** یعنی کار با رشته‌ها برای استخراج اطلاعات، تبدیل داده و تحلیل محتوا. مثل کارآگاهی با متن فکر کنید: دنبال سرنخ بگردید، اطلاعات را سازماندهی کنید و الگوها را پیدا کنید.

### نمونه‌های واقعی

- شمردن کلمات یک مقاله
- پیدا کردن همه نشانی‌های ایمیل در یک سند
- پاک کردن ورودی شلوغ کاربر
- تحلیل پست‌های شبکه اجتماعی
- استخراج داده از فایل‌های CSV
- بررسی اینکه رمز عبور شرایط لازم را دارد یا نه

---

## جست‌وجو در رشته‌ها

### پیدا کردن زیررشته

```python
text = "Python is a powerful programming language. Python is fun!"

# پیدا کردن اولین مورد (موقعیت یا ۱- برمی‌گرداند)
position = text.find("Python")      # 0 (از موقعیت ۰ شروع می‌شود)
not_found = text.find("Java")        # -1 (در رشته نیست)

# پیدا کردن از موقعیت ۱۰ (دومین "Python" را پیدا می‌کند)
second = text.find("Python", 10)    # 45

# پیدا کردن با rfind (از راست، یعنی انتها جست‌وجو می‌کند)
last = text.rfind("is")              # 47
```

**مهم**: اگر پیدا نشود، `find()` مقدار `-1` برمی‌گرداند، ولی `index()` خطا می‌دهد. وقتی مطمئن نیستید متن وجود دارد یا نه، از `find()` استفاده کنید.

### بررسی حضور (عملگر `in`)

```python
text = "Learning Python programming"

# بررسی وجود زیررشته (True یا False برمی‌گرداند)
"Python" in text      # True
"Java" in text        # False

# بررسی نبودن در رشته
"Java" not in text    # True
"Python" not in text  # False

# بررسی بدون حساسیت به بزرگی و کوچکی حروف (اول هم‌حالتش کن)
python_mentioned = "python" in text.lower()  # True
```

### شمردن تکرارها

```python
text = "The quick brown fox jumps over the lazy dog"

# شمردن اینکه یک زیررشته چند بار آمده
t_count = text.count("t")           # 2 (حرف t کوچک)
total_t = text.lower().count("t")   # 3 (همه حرف‌های t شمرده می‌شوند)

# شمردن کلمات مشخص
the_count = text.count("the")       # 2
```

### بررسی ابتدا و انتها

```python
filename = "document.pdf"
url = "https://example.com"

# بررسی ابتدا
filename.startswith("doc")          # True
url.startswith("https://")          # True

# بررسی انتها
filename.endswith(".pdf")           # True
url.endswith(".com")                # True

# بررسی چند گزینه
filename.endswith((".pdf", ".doc", ".txt"))  # True (هرکدام کافی است)
```

---

## تقسیم و چسباندن رشته‌ها

### تقسیم: شکستن متن

```python
# تقسیم بر اساس فاصله (پیش‌فرض)
sentence = "Hello world how are you"
words = sentence.split()
# Result: ['Hello', 'world', 'how', 'are', 'you']

# تقسیم بر اساس نویسه مشخص
csv_line = "Alice,25,Engineer,New York"
fields = csv_line.split(",")
# Result: ['Alice', '25', 'Engineer', 'New York']

# تقسیم فقط N مورد اول
sentence = "one:two:three:four:five"
parts = sentence.split(":", 2)
# Result: ['one', 'two', 'three:four:five']

# تقسیم خطوط
multiline = "Line 1\nLine 2\nLine 3"
lines = multiline.split("\n")
# Result: ['Line 1', 'Line 2', 'Line 3']

# تقسیم خطوط (بهتر - با پایان خط‌های مختلف کار می‌کند)
lines = multiline.splitlines()
```

### چسباندن: کنار هم گذاشتن متن

```python
# چسباندن فهرست به رشته
words = ['Hello', 'world']
sentence = ' '.join(words)
# Result: "Hello world"

# چسباندن با جداکننده متفاوت
path_parts = ['home', 'user', 'documents']
path = '/'.join(path_parts)
# Result: "home/user/documents"

# چسباندن اعداد (اول باید به رشته تبدیل شوند!)
numbers = [1, 2, 3, 4, 5]
result = ', '.join(str(n) for n in numbers)
# Result: "1, 2, 3, 4, 5"

# ساخت یک خط CSV
data = ["Alice", "25", "Engineer"]
csv = ','.join(data)
# Result: "Alice,25,Engineer"
```

---

## تبدیل و پاک‌سازی متن

### تغییر بزرگی و کوچکی حروف

```python
text = "Hello World"

upper = text.upper()          # "HELLO WORLD"
lower = text.lower()          # "hello world"
title = text.title()          # "Hello World"
capital = text.capitalize()   # "Hello world"
```

### حذف نویسه‌های ناخواسته

```python
text = "   Hello World   "

# حذف فاصله از دو طرف
clean = text.strip()          # "Hello World"
left = text.lstrip()          # "Hello World   "
right = text.rstrip()         # "   Hello World"

# حذف نویسه‌های مشخص
messy = "xxxHelloxxx"
clean = messy.strip('x')      # "Hello"

# حذف همه فاصله‌ها
no_spaces = text.replace(" ", "")
# Result: "HelloWorld"
```

### جایگزینی متن

```python
text = "I like Java programming"

# جایگزینی همه موارد
new_text = text.replace("Java", "Python")
# Result: "I like Python programming"

# جایگزینی N مورد اول
partial = text.replace("a", "@", 1)
# Result: "I like J@va programming" (فقط اولین a)

# حذف با جایگزینی با رشته خالی
text = "Hello, World!"
clean = text.replace(",", "").replace("!", "")
# Result: "Hello World"
```

---

## نمونه‌های کاربردی پردازش متن

### مثال ۱: شمارنده کلمات

```python
def count_words(text):
    """Count words in text."""
    # پاک کردن متن
    cleaned = text.lower()

    # حذف نقطه‌گذاری (روش ساده)
    for char in ".,!?;:'\"()-":
        cleaned = cleaned.replace(char, " ")

    # تقسیم به کلمات
    words = cleaned.split()

    return len(words)

# Usage
essay = "Python is amazing. Python is powerful and fun!"
print(f"Word count: {count_words(essay)}")  # Word count: 9
```

### مثال ۲: اعتبارسنج ساده ایمیل

```python
def is_valid_email(email):
    """Basic email validation."""
    # بررسی ساختار پایه
    if "@" not in email:
        return False

    # تقسیم به بخش‌ها
    parts = email.split("@")
    if len(parts) != 2:
        return False

    local, domain = parts

    # بررسی خالی نبودن هر دو بخش
    if not local or not domain:
        return False

    # بررسی وجود نقطه در دامنه
    if "." not in domain:
        return False

    return True

# Test
print(is_valid_email("user@example.com"))     # True
print(is_valid_email("invalid-email"))        # False
print(is_valid_email("@example.com"))          # False
```

### مثال ۳: پاک‌کننده متن

```python
def clean_text(text):
    """Clean and normalize text."""
    if not text:
        return ""

    # تبدیل به حروف کوچک
    text = text.lower()

    # حذف فاصله‌های اضافه
    text = ' '.join(text.split())

    # حذف نقطه‌گذاری رایج
    punctuation = ".,!?;:'\"()-"
    for char in punctuation:
        text = text.replace(char, "")

    return text

# Usage
messy = "  Hello, World!   HOW are you??  "
clean = clean_text(messy)
print(clean)  # "hello world how are you"
```

### مثال ۴: بررسی قدرت رمز عبور

```python
def check_password_strength(password):
    """Check if password is strong."""
    checks = {
        "length": len(password) >= 8,
        "has_upper": any(c.isupper() for c in password),
        "has_lower": any(c.islower() for c in password),
        "has_digit": any(c.isdigit() for c in password),
    }

    score = sum(checks.values())

    if score == 4:
        return "Strong"
    elif score >= 2:
        return "Medium"
    else:
        return "Weak"

# Test
print(check_password_strength("Hello123"))    # Strong
print(check_password_strength("hello"))       # Weak
print(check_password_strength("HELLO"))       # Weak
```

### مثال ۵: تجزیه‌گر ساده CSV

```python
def parse_csv_line(line):
    """Parse a CSV line into fields."""
    # حذف فاصله‌های اضافه و تقسیم
    fields = [field.strip() for field in line.split(",")]
    return fields

def parse_csv_data(data_lines):
    """Parse multiple CSV lines."""
    result = []
    for line in data_lines:
        if line.strip():  # رد کردن خطوط خالی
            result.append(parse_csv_line(line))
    return result

# Usage
csv_data = [
    "Alice,25,Engineer",
    "Bob,30,Designer",
    "Charlie,35,Manager"
]

parsed = parse_csv_data(csv_data)
for row in parsed:
    print(f"Name: {row[0]}, Age: {row[1]}, Job: {row[2]}")
```

---

## تحلیل متن

### پیدا کردن پرتکرارترین کلمات

```python
def word_frequency(text):
    """Count how often each word appears."""
    # پاک کردن و تقسیم
    cleaned = text.lower()
    for char in ".,!?;:'\"()-":
        cleaned = cleaned.replace(char, " ")

    words = cleaned.split()

    # شمردن فراوانی
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency

# Usage
text = "the quick brown fox jumps over the lazy dog"
freq = word_frequency(text)

# پیدا کردن پرتکرارترین
most_common = max(freq.items(), key=lambda x: x[1])
print(f"Most common word: '{most_common[0]}' appears {most_common[1]} times")
```

### آمار متن

```python
def text_statistics(text):
    """Calculate various text statistics."""
    # شمارش پایه
    char_count = len(text)
    char_count_no_spaces = len(text.replace(" ", ""))

    # شمارش کلمات
    words = text.split()
    word_count = len(words)

    # شمارش خطوط
    lines = text.splitlines()
    line_count = len(lines)

    # میانگین طول کلمه
    if words:
        avg_word_length = sum(len(word) for word in words) / len(words)
    else:
        avg_word_length = 0

    return {
        "characters": char_count,
        "characters_no_spaces": char_count_no_spaces,
        "words": word_count,
        "lines": line_count,
        "average_word_length": round(avg_word_length, 1)
    }

# Usage
text = """Hello world.
This is a test.
Python programming is fun!"""

stats = text_statistics(text)
for key, value in stats.items():
    print(f"{key}: {value}")
```

---

## اشتباهات رایج مبتدی

### اشتباه ۱: تغییر فهرست هنگام پیمایش روی آن

```python
# اشتباه - ممکن است آیتم‌ها جا بیفتند!
data = ["1", "2", "3", "a", "4", "b"]
for item in data:
    if not item.isdigit():
        data.remove(item)  # خطرناک!

# درست - یک فهرست تازه بسازید
data = ["1", "2", "3", "a", "4", "b"]
cleaned = [item for item in data if item.isdigit()]
# Result: ['1', '2', '3', '4']
```

### اشتباه ۲: فراموش کردن تبدیل اعداد به رشته

```python
numbers = [1, 2, 3, 4, 5]

# اشتباه
result = ", ".join(numbers)   # خطا!

# درست
result = ", ".join(str(n) for n in numbers)
# Result: "1, 2, 3, 4, 5"
```

### اشتباه ۳: مقایسه حساس به بزرگی و کوچکی حروف

```python
text = "Python Programming"

# اشتباه - حساس به بزرگی و کوچکی حروف
if "python" in text:   # False!
    print("Found!")

# درست - حروف را یکدست کنید
if "python" in text.lower():   # True!
    print("Found!")
```

### اشتباه ۴: مدیریت نکردن رشته خالی

```python
def get_first_char(text):
    # اشتباه - روی رشته خالی کرش می‌کند
    return text[0]

# درست - اول بررسی کنید
def get_first_char(text):
    if not text:
        return None
    return text[0]
```

---

## تمرین‌ها

### تمرین ۱: معکوس‌کننده جمله
تابعی بنویسید که ترتیب کلمات یک جمله را معکوس کند.

```python
def reverse_words(sentence):
    # کد شما اینجا
    pass

# Test
print(reverse_words("Hello world"))   # Should print: "world Hello"
print(reverse_words("The quick brown fox"))  # Should print: "fox brown quick The"
```

### تمرین ۲: بررسی palindrome
تابعی بنویسید که بررسی کند آیا یک کلمه یا عبارت palindrome است (از جلو و عقب یکی خوانده می‌شود).

```python
def is_palindrome(text):
    # کد شما اینجا (فاصله‌ها و بزرگی و کوچکی حروف را نادیده بگیرید)
    pass

# Test
print(is_palindrome("radar"))     # Should print: True
print(is_palindrome("A man a plan a canal Panama"))  # Should print: True
print(is_palindrome("hello"))     # Should print: False
```

### تمرین ۳: استخراج هشتگ‌ها
تابعی بنویسید که همه هشتگ‌های یک پست شبکه اجتماعی را استخراج کند.

```python
def extract_hashtags(text):
    # کد شما اینجا
    pass

# Test
post = "Learning #Python is fun! #coding #programming #learn"
print(extract_hashtags(post))
# Should print: ['#Python', '#coding', '#programming', '#learn']
```

### تمرین ۴: قالب‌بند شماره تلفن
تابعی بنویسید که یک شماره ۱۰ رقمی را به شکل (XXX) XXX-XXXX قالب‌بندی کند.

```python
def format_phone(number):
    # کد شما اینجا
    pass

# Test
print(format_phone("5551234567"))   # Should print: (555) 123-4567
print(format_phone("555-123-4567")) # Should print: (555) 123-4567
```

---

## نکات کلیدی

1. **جست‌وجو**: برای جست‌وجوی امن از `find()` استفاده کنید (اگر پیدا نشود `-1` می‌دهد)، برای بررسی ساده True/False از `in`
2. **تقسیم و چسباندن**: `split()` رشته را می‌شکند، `join()` دوباره کنار هم می‌گذارد
3. **حروف بزرگ و کوچک مهم است**: به یاد داشته باشید «Python» و «python» فرق دارند، برای کار بدون حساسیت از `.lower()` استفاده کنید
4. **اول داده را پاک کنید**: پیش از پردازش ورودی کاربر، همیشه فاصله‌ها را حذف و حروف را یکدست کنید
5. **فهرست در برابر رشته**: یادتان باشد `join()` روی فهرست کار می‌کند ولی رشته می‌خواهد، نه عدد
6. **رشته تغییرناپذیر است**: متدها رشته تازه برمی‌گردانند، رشته اصلی تغییر نمی‌کند

## مرجع سریع

| کار | چگونه | مثال |
|-----|-------|------|
| پیدا کردن زیررشته | `text.find("sub")` | `"abc".find("b")` → 1 |
| بررسی حضور | `"sub" in text` | `"b" in "abc"` → True |
| شمردن تکرار | `text.count("sub")` | `"aa".count("a")` → 2 |
| شروع با؟ | `text.startswith("pre")` | `"abc".startswith("a")` → True |
| پایان با؟ | `text.endswith("suf")` | `"abc".endswith("c")` → True |
| تقسیم رشته | `text.split(sep)` | `"a,b".split(",")` → ['a','b'] |
| چسباندن رشته‌ها | `sep.join(list)` | `"-".join(['a','b'])` → 'a-b' |
| حذف فاصله‌ها | `text.strip()` | `" hi ".strip()` → 'hi' |
| جایگزینی | `text.replace(old, new)` | `"a,b".replace(",", "-")` → 'a-b' |
| حروف بزرگ | `text.upper()` | `"hi".upper()` → 'HI' |
| حروف کوچک | `text.lower()` | `"HI".lower()` → 'hi' |

---

## مطالعه بیشتر

- **درس بعدی**: فهرست‌های پایتون، مجموعه‌های مرتب داده
- **تمرین**: همه تمرین‌های بالا را کامل کنید
- **چالش**: یک بازی ماجراجویی متنی ساده بنویسید که فرمان‌های کاربر را پردازش کند
- **کاوش کنید**: یک فایل متنی واقعی را بخوانید و تحلیل کنید