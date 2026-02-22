# پردازش متن: تحلیل و دستکاری متن

## پردازش متن چیست؟

**پردازش متن** همه چیز درباره کار با رشته‌ها برای استخراج اطلاعات، تبدیل داده‌ها و تحلیل محتوا است. آن را مثل یک کارآگاه با متن در نظر بگیرید - جستجوی سرنخ، سازماندهی اطلاعات و یافتن الگوها.

### مثال‌های دنیای واقعی

- شمارش کلمات در یک انشا
- یافتن تمام آدرس ایمیل در یک سند
- تمیز کردن ورودی ناخوانا از کاربر
- تحلیل پست‌های شبکه‌های اجتماعی
- استخراج داده از فایل‌های CSV
- بررسی اینکه آیا رمز عبور شرایط لازم را دارد

---

## جستجو در رشته‌ها

### یافتن زیررشته‌ها

```python
text = "Python is a powerful programming language. Python is fun!"

# یافتن اولین رخداد (موقعیت یا -1 را برمی‌گرداند)
position = text.find("Python")      # 0 (از موقعیت 0 شروع می‌شود)
not_found = text.find("Java")        # -1 (در رشته نیست)

# یافتن از موقعیت 10 (پیدا کردن دومین "Python")
second = text.find("Python", 10)    # 45

# یافتن با rfind (جستجو از راست/انتها)
last = text.rfind("is")              # 47
```

**مهم**: `find()` اگر پیدا نشود -1 برمی‌گرداند، در حالی که `index()` خطا می‌دهد. وقتی مطمئن نیستید متن وجود دارد از `find()` استفاده کنید.

### بررسی عضویت (عملگر `in`)

```python
text = "Learning Python programming"

# بررسی اینکه آیا زیررشته وجود دارد (True یا False برمی‌گرداند)
"Python" in text      # True
"Java" in text        # False

# بررسی اینکه آیا در رشته نیست
"Java" not in text    # True
"Python" not in text  # False

# بررسی بدون حساسیت به بزرگی و کوچکی (ابتدا به یک حالته تبدیل کنید)
python_mentioned = "python" in text.lower()  # True
```

### شمارش رخدادها

```python
text = "The quick brown fox jumps over the lazy dog"

# شمارش چند بار یک زیررشته ظاهر می‌شود
t_count = text.count("t")           # 2 (t کوچک)
total_t = text.lower().count("t")   # 3 (شمارش همه tها)

# شمارش کلمات خاص
the_count = text.count("the")       # 2
```

### بررسی شروع و پایان

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
filename.endswith((".pdf", ".doc", ".txt"))  # True (هر کدام)
```

---

## تقسیم و پیوستن رشته‌ها

### تقسیم: شکستن متن

```python
# تقسیم بر فاصله (پیش‌فرض)
sentence = "Hello world how are you"
words = sentence.split()
# Result: ['Hello', 'world', 'how', 'are', 'you']

# تقسیم بر کاراکتر خاص
csv_line = "Alice,25,Engineer,New York"
fields = csv_line.split(",")
# Result: ['Alice', '25', 'Engineer', 'New York']

# تقسیم فقط اولین N رخداد
sentence = "one:two:three:four:five"
parts = sentence.split(":", 2)
# Result: ['one', 'two', 'three:four:five']

# تقسیم خطوط
multiline = "Line 1\nLine 2\nLine 3"
lines = multiline.split("\n")
# Result: ['Line 1', 'Line 2', 'Line 3']

# تقسیم خطوط (بهتر - پایان خطوط مختلف را مدیریت می‌کند)
lines = multiline.splitlines()
```

### پیوستن: کنار هم قرار دادن متن

```python
# پیوستن لیست به رشته
words = ['Hello', 'world']
sentence = ' '.join(words)
# Result: "Hello world"

# پیوستن با جداکننده‌های مختلف
path_parts = ['home', 'user', 'documents']
path = '/'.join(path_parts)
# Result: "home/user/documents"

# پیوستن اعداد (باید ابتدا به رشته تبدیل شوند!)
numbers = [1, 2, 3, 4, 5]
result = ', '.join(str(n) for n in numbers)
# Result: "1, 2, 3, 4, 5"

# ایجاد خط CSV
data = ["Alice", "25", "Engineer"]
csv = ','.join(data)
# Result: "Alice,25,Engineer"
```

---

## تبدیل و تمیز کردن متن

### تغییر بزرگی و کوچکی

```python
text = "Hello World"

upper = text.upper()          # "HELLO WORLD"
lower = text.lower()          # "hello world"
title = text.title()          # "Hello World"
capital = text.capitalize()   # "Hello world"
```

### حذف کاراکترهای ناخواسته

```python
text = "   Hello World   "

# حذف فاصله از انتهاها
clean = text.strip()          # "Hello World"
left = text.lstrip()          # "Hello World   "
right = text.rstrip()         # "   Hello World"

# حذف کاراکترهای خاص
messy = "xxxHelloxxx"
clean = messy.strip('x')      # "Hello"

# حذف همه فاصله‌ها
no_spaces = text.replace(" ", "")
# Result: "HelloWorld"
```

### جایگزینی متن

```python
text = "I like Java programming"

# جایگزینی همه رخدادها
new_text = text.replace("Java", "Python")
# Result: "I like Python programming"

# جایگزینی اولین N رخداد
partial = text.replace("a", "@", 1)
# Result: "I like J@va programming" (فقط اولین 'a')

# حذف با جایگزینی با هیچ
text = "Hello, World!"
clean = text.replace(",", "").replace("!", "")
# Result: "Hello World"
```

---

## مثال‌های عملی پردازش متن

### مثال 1: شمارنده کلمات

```python
def count_words(text):
    """شمارش کلمات در متن."""
    # تمیز کردن متن
    cleaned = text.lower()

    # حذف نگارش (روش ساده)
    for char in ".,!?;:'\"()-":
        cleaned = cleaned.replace(char, " ")

    # تقسیم به کلمات
    words = cleaned.split()

    return len(words)

# Usage
essay = "Python is amazing. Python is powerful and fun!"
print(f"Word count: {count_words(essay)}")  # Word count: 9
```

### مثال 2: اعتبارسنجی ایمیل (ساده)

```python
def is_valid_email(email):
    """اعتبارسنجی پایه ایمیل."""
    # بررسی ساختار پایه
    if "@" not in email:
        return False

    # تقسیم به بخش‌ها
    parts = email.split("@")
    if len(parts) != 2:
        return False

    local, domain = parts

    # بررسی وجود هر دو بخش
    if not local or not domain:
        return False

    # بررسی دامنه دارای نقطه
    if "." not in domain:
        return False

    return True

# Test
print(is_valid_email("user@example.com"))     # True
print(is_valid_email("invalid-email"))        # False
print(is_valid_email("@example.com"))          # False
```

### مثال 3: تمیزکننده متن

```python
def clean_text(text):
    """تمیز کردن و نرمال‌سازی متن."""
    if not text:
        return ""

    # تبدیل به کوچک
    text = text.lower()

    # حذف فاصله اضافی
    text = ' '.join(text.split())

    # حذف نگارش رایج
    punctuation = ".,!?;:'\"()-"
    for char in punctuation:
        text = text.replace(char, "")

    return text

# Usage
messy = "  Hello, World!   HOW are you??  "
clean = clean_text(messy)
print(clean)  # "hello world how are you"
```

### مثال 4: بررسی قدرت رمز عبور

```python
def check_password_strength(password):
    """بررسی قوی بودن رمز عبور."""
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

### مثال 5: پارسر CSV ساده

```python
def parse_csv_line(line):
    """تجزیه یک خط CSV به فیلدها."""
    # حذف فاصله و تقسیم
    fields = [field.strip() for field in line.split(",")]
    return fields

def parse_csv_data(data_lines):
    """تجزیه چندین خط CSV."""
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

### یافتن پرتکرارترین کلمات

```python
def word_frequency(text):
    """شمارش چند بار هر کلمه ظاهر می‌شود."""
    # تمیز کردن و تقسیم
    cleaned = text.lower()
    for char in ".,!?;:'\"()-":
        cleaned = cleaned.replace(char, " ")

    words = cleaned.split()

    # شمارش فرکانس‌ها
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

# یافتن پرتکرارترین
most_common = max(freq.items(), key=lambda x: x[1])
print(f"Most common word: '{most_common[0]}' appears {most_common[1]} times")
```

### آمار متن

```python
def text_statistics(text):
    """محاسبه آمار مختلف متن."""
    # شمارش‌های پایه
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

## اشتباهات رایج مبتدی‌ها

### اشتباه 1: تغییر رشته حین تکرار

```python
# اشتباه - این می‌تواند آیتم‌ها را رد کند!
data = ["1", "2", "3", "a", "4", "b"]
for item in data:
    if not item.isdigit():
        data.remove(item)  # خطرناک!

# درست - ایجاد لیست جدید
data = ["1", "2", "3", "a", "4", "b"]
cleaned = [item for item in data if item.isdigit()]
# Result: ['1', '2', '3', '4']
```

### اشتباه 2: فراموش کردن تبدیل اعداد به رشته

```python
numbers = [1, 2, 3, 4, 5]

# اشتباه
result = ", ".join(numbers)   # خطا!

# درست
result = ", ".join(str(n) for n in numbers)
# Result: "1, 2, 3, 4, 5"
```

### اشتباه 3: مقایسه حساس به بزرگی و کوچکی

```python
text = "Python Programming"

# اشتباه - حساس به بزرگی و کوچکی
if "python" in text:   # False!
    print("Found!")

# درست - یکسان کردن حالت
if "python" in text.lower():   # True!
    print("Found!")
```

### اشتباه 4: عدم مدیریت رشته‌های خالی

```python
def get_first_char(text):
    # اشتباه - در رشته خالی crash می‌کند
    return text[0]

# درست - ابتدا بررسی کنید
def get_first_char(text):
    if not text:
        return None
    return text[0]
```

---

## تمرین‌های عملی

### تمرین 1: معکوس‌کننده جمله
تابعی بنویسید که ترتیب کلمات در یک جمله را معکوس کند.

```python
def reverse_words(sentence):
    # کد شما اینجا
    pass

# Test
print(reverse_words("Hello world"))   # باید چاپ کند: "world Hello"
print(reverse_words("The quick brown fox"))  # باید چاپ کند: "fox brown quick The"
```

### تمرین 2: بررسی palindrome
تابعی بنویسید که بررسی کند آیا یک کلمه/عبارت palindrome است (از دو طرف یکی خوانده می‌شود).

```python
def is_palindrome(text):
    # کد شما اینجا (فاصله و حالت را نادیده بگیرید)
    pass

# Test
print(is_palindrome("radar"))     # باید چاپ کند: True
print(is_palindrome("A man a plan a canal Panama"))  # باید چاپ کند: True
print(is_palindrome("hello"))     # باید چاپ کند: False
```

### تمرین 3: استخراج هشتگ‌ها
تابعی بنویسید که همه هشتگ‌ها را از یک پست شبکه اجتماعی استخراج کند.

```python
def extract_hashtags(text):
    # کد شما اینجا
    pass

# Test
post = "Learning #Python is fun! #coding #programming #learn"
print(extract_hashtags(post))
# باید چاپ کند: ['#Python', '#coding', '#programming', '#learn']
```

### تمرین 4: قالب‌بندی شماره تلفن
تابعی بنویسید که یک عدد 10رقمی را به شکل (XXX) XXX-XXXX قالب‌بندی کند.

```python
def format_phone(number):
    # کد شما اینجا
    pass

# Test
print(format_phone("5551234567"))   # باید چاپ کند: (555) 123-4567
print(format_phone("555-123-4567")) # باید چاپ کند: (555) 123-4567
```

---

## نکات کلیدی

1. **جستجو**: از `find()` برای جستجوی امن استفاده کنید (-1 برمی‌گرداند اگر پیدا نشود)، `in` برای بررسی‌های ساده True/False
2. **تقسیم/پیوستن**: `split()` رشته‌ها را از هم جدا می‌کند، `join()` آن‌ها را کنار هم قرار می‌دهد
3. **حالت مهم است**: به یاد داشته باشید "Python" و "python" متفاوت هستند - از `.lower()` برای کار بدون حساسیت به حالت استفاده کنید
4. **ابتدا داده را تمیز کنید**: همیشه قبل از پردازش ورودی کاربر، فاصله را حذف و حالت را نرمال کنید
5. **لیست در مقابل رشته**: به یاد داشته باشید `join()` روی لیست کار می‌کند اما رشته نیاز دارد، نه عدد
6. **رشته‌ها تغییرناپذیر هستند**: متدها رشته جدید برمی‌گردانند؛ اصلی تغییر نمی‌کند

---

## مرجع سریع

| کار | نحوه انجام | مثال |
|------|----------|--------|
| یافتن زیررشته | `text.find("sub")` | `"abc".find("b")` → 1 |
| بررسی وجود | `"sub" in text` | `"b" in "abc"` → True |
| شمارش رخدادها | `text.count("sub")` | `"aa".count("a")` → 2 |
| شروع می‌شود؟ | `text.startswith("pre")` | `"abc".startswith("a")` → True |
| پایان می‌یابد؟ | `text.endswith("suf")` | `"abc".endswith("c")` → True |
| تقسیم رشته | `text.split(sep)` | `"a,b".split(",")` → ['a','b'] |
| پیوستن رشته‌ها | `sep.join(list)` | `"-".join(['a','b'])` → 'a-b' |
| حذف فاصله | `text.strip()` | `" hi ".strip()` → 'hi' |
| جایگزینی | `text.replace(old, new)` | `"a,b".replace(",", "-")` → 'a-b' |
| بزرگ | `text.upper()` | `"hi".upper()` → 'HI' |
| کوچک | `text.lower()` | `"HI".lower()` → 'hi' |

---

## مطالعه بیشتر

- **درس بعدی**: لیست‌های پایتون - مجموعه‌های مرتب داده
- **تمرین**: تمام تمرین‌های بالا را کامل کنید
- **چالش**: یک بازی ماجراجویی متنی ساده بنویسید که دستورات کاربر را پردازش می‌کند
- **کاوش**: امتحان کنید خواندن و تحلیل یک فایل متنی واقعی
