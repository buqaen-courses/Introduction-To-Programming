# عملیات رشته: دستکاری داده‌های متنی

## رشته‌ها به عنوان توالی‌ها

در برنامه‌نویسی، رشته‌ها توالی کاراکترها هستند. هر کاراکتر موقعیت (شاخص) خود را دارد و می‌تواند به طور جداگانه یا به عنوان گروه دستکاری شود.

## عملیات پایه رشته

### ایجاد رشته‌ها
```python
# گیومه تکی
text1 = 'سلام'

# گیومه جفت
text2 = "دنیا"

# رشته‌های چند خطی
poem = """رزها سرخ هستند
بنفشه‌ها آبی"""

# توالی‌های فرار
path = "C:\\Users\\file.txt"
quote = "او گفت \"سلام\""
```

### الحاق رشته‌ها
```python
# با استفاده از عملگر +
full_name = first_name + " " + last_name

# با استفاده از join() برای کارایی
words = ["سلام", "دنیای", "از", "Python"]
sentence = " ".join(words)  # "سلام دنیای از Python"

# ضرب رشته
divider = "=" * 50  # "=================================================="
```

## شاخص‌گذاری و برش رشته

### دسترسی به کاراکتر
```python
text = "Python"
print(text[0])    # 'P' (کاراکتر اول)
print(text[5])    # 'n' (کاراکتر آخر)
print(text[-1])   # 'n' (شاخص منفی)
```

### برش رشته
```python
text = "Hello World"

# برش پایه: string[start:end]
print(text[0:5])   # 'Hello'
print(text[6:])    # 'World'
print(text[:5])    # 'Hello'

# با گام: string[start:end:step]
print(text[::2])   # 'HloWrd' (هر کاراکتر دیگر)
print(text[::-1])  # 'dlroW olleH' (معکوس)
```

## متدهای رشته

### تبدیل حالت
```python
text = "Hello World"

text.upper()       # 'HELLO WORLD'
text.lower()       # 'hello world'
text.capitalize()  # 'Hello world'
text.title()       # 'Hello World'
text.swapcase()    # 'hELLO wORLD'
```

### جستجو و یافتن
```python
text = "برنامه‌نویسی Python جالب است"

text.find("برنامه")          # ۰ (شاخص جایی که یافت شد)
text.find("xyz")          # -۱ (یافت نشد)
text.index("برنامه")         # ۰ (اگر یافت نشد خطا ایجاد می‌کند)
text.count("ا")           # ۲ (شمارش رخدادها)
text.startswith("برنامه") # True
text.endswith("است")      # True
```

### متدهای تغییر
```python
text = "  سلام دنیا  "

text.strip()              # 'سلام دنیا' (حذف فضای خالی)
text.lstrip()             # 'سلام دنیا  ' (strip چپ)
text.rstrip()             # '  سلام دنیا' (strip راست)

text.replace("دنیا", "Python")  # '  سلام Python  '
text.split()              # ['سلام', 'دنیا'] (تقسیم بر اساس فاصله)
text.split("ا")           # ['  سل', 'م دنی', '  ']
```

### متدهای آزمون
```python
text = "Hello123"

text.isalpha()     # False (شامل عدد)
text.isdigit()     # False (شامل حرف)
text.isalnum()     # True (حرف و عدد)
text.islower()     # False (حالت مخلوط)
text.isupper()     # False (همه بزرگ نیستند)
text.isspace()     # False (همه فاصله نیستند)
```

## قالب‌بندی پیشرفته رشته

### F-Stringها (Python 3.6+)
```python
name = "علی"
age = 25
height = 1.68

# f-string پایه
message = f"سلام، {name}!"

# با عبارت‌ها
message = f"سال آینده {age + 1} ساله خواهید شد."

# با قالب‌بندی
message = f"قد: {height:.2f} متر"
message = f"سن: {age:03d}"  # با صفر پر شده
```

### متد format
```python
# قالب‌بندی موقعیتی
template = "{} {} ساله است".format(name, age)
# "علی ۲۵ ساله است"

# قالب‌بندی نام‌گذاری شده
template = "{name} {age} ساله است و {height:.1f} متر قد دارد".format(
    name=name, age=age, height=height)

# مشخصات قالب
f"مقدار: {42:04d}"    # 'مقدار: 0042'
f"شناور: {3.14159:.2f}"  # 'شناور: 3.14'
```

### قالب‌بندی قدیمی
```python
# قالب‌بندی % (قدیمی)
template = "%s %d ساله است" % (name, age)
# "علی ۲۵ ساله است"
```

## مقایسه رشته و مرتب‌سازی

### مقایسه لغوی
```python
"apple" < "banana"     # True (a < b)
"Apple" < "apple"      # True (A < a در ASCII)
"۱۰" < "۲"            # True (۱ < ۲، لغوی نه عددی)
```

### مقایسه بدون حساسیت به حالت
```python
text1 = "Hello"
text2 = "hello"

text1.lower() == text2.lower()  # True
text1.casefold() == text2.casefold()  # True (بهتر برای بین‌المللی‌سازی)
```

### مرتب‌سازی رشته‌ها
```python
words = ["zebra", "apple", "Banana", "cherry"]
sorted(words)  # ['Banana', 'apple', 'cherry', 'zebra'] (ترتیب ASCII)

# مرتب‌سازی بدون حساسیت به حالت
sorted(words, key=str.lower)  # ['apple', 'Banana', 'cherry', 'zebra']
```

## عبارات منظم

### تطبیق الگو
```python
import re

text = "ایمیل user@example.com و تلفن 555-1234 است"

# یافتن ایمیل
email = re.search(r'\w+@\w+\.\w+', text)
print(email.group())  # 'user@example.com'

# یافتن تلفن
phone = re.search(r'\d{3}-\d{4}', text)
print(phone.group())  # '555-1234'

# جایگزینی
cleaned = re.sub(r'\d{3}-\d{4}', '[تلفن]', text)
print(cleaned)  # 'ایمیل user@example.com و تلفن [تلفن] است'
```

### الگوهای رایج
```python
# ایمیل
r'[\w\.-]+@[\w\.-]+\.\w+'

# تلفن (ایالات متحده)
r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'

# URL
r'https?://(?:[-\w.])+(?:[:\d]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:#(?:\w*))?)?'

# تاریخ (MM/DD/YYYY)
r'\d{1,2}/\d{1,2}/\d{4}'
```

## الگوریتم‌های پردازش متن

### معکوس کردن رشته
```python
def reverse_string(text):
    return text[::-1]

# یا با استفاده از بازگشت
def reverse_recursive(text):
    if len(text) <= 1:
        return text
    return reverse_recursive(text[1:]) + text[0]
```

### بررسی palindrome
```python
def is_palindrome(text):
    clean_text = ''.join(c.lower() for c in text if c.isalnum())
    return clean_text == clean_text[::-1]

print(is_palindrome("یک مرد، یک برنامه، یک کانال: پاناما"))  # True
```

### شمارش فراوانی کلمه
```python
def word_frequency(text):
    words = text.lower().split()
    frequency = {}
    for word in words:
        # حذف علائم نگارشی
        word = ''.join(c for c in word if c.isalnum())
        if word:
            frequency[word] = frequency.get(word, 0) + 1
    return frequency
```

### فشرده‌سازی رشته
```python
def compress_string(text):
    if not text:
        return ""
    compressed = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count += 1
        else:
            compressed.append(text[i-1] + str(count))
            count = 1
    compressed.append(text[-1] + str(count))
    result = ''.join(compressed)
    return result if len(result) < len(text) else text

print(compress_string("aabcccccaaa"))  # "a2b1c5a3"
```

## یونیکد و متن بین‌المللی

### عملیات یونیکد
```python
# عادی‌سازی یونیکد
import unicodedata

text = "café"
normalized = unicodedata.normalize('NFC', text)

# دسته‌های یونیکد
for char in text:
    print(f"{char}: {unicodedata.category(char)}")
```

### مدیریت خط‌های مختلف
```python
# متن عربی (راست به چپ)
arabic = "مرحبا بالعالم"

# خطوط مخلوط
mixed = "Hello 世界 Привет"

# ملاحظات طول
len(mixed)  # ۱۵ (شمار کاراکتر)
len(mixed.encode('utf-8'))  # ۲۱ (شمار بایت)
```

## ملاحظات عملکرد

### تغییرناپذیری رشته
```python
# رشته‌ها تغییرناپذیر هستند - هر عملیات رشته جدیدی ایجاد می‌کند
text = "hello"
text = text.upper()  # رشته جدید ایجاد می‌کند
text = text + " world"  # رشته دیگری ایجاد می‌کند

# برای عملیات زیاد، از لیست‌ها استفاده کنید سپس join کنید
parts = []
for i in range(1000):
    parts.append(str(i))
result = ''.join(parts)  # کارآمد
```

### interning رشته
```python
# Python رشته‌های کوتاه را برای کارایی intern می‌کند
a = "hello"
b = "hello"
a is b  # True (شیء یکسان)

# اما نه برای رشته‌های بلندتر یا ایجاد شده به صورت پویا
a = "a" * 1000
b = "a" * 1000
a is b  # False (اشیاء مختلف)
```

## مشکلات رایج رشته

### مشکلات کدگذاری
```python
# کدگذاری اشتباه منجر به خطا می‌شود
text = "café"
try:
    text.encode('ascii')  # شکست خواهد خورد
except UnicodeEncodeError:
    print("نمی‌توان با ASCII کدگذاری کرد")
```

### خطاهای شاخص
```python
text = "hello"
# text[10]  # IndexError
# از برش به طور ایمن استفاده کنید
chunk = text[2:10]  # بدون خطا، فقط کوتاه می‌شود
```

### مشکلات حساسیت به حالت
```python
# به طور پیش‌فرض حساس به حالت
"Apple" == "apple"  # False

# از lower() برای غیر حساس به حالت استفاده کنید
"Apple".lower() == "apple".lower()  # True
```

## نکات کلیدی

۱. **رشته‌ها توالی هستند**: کاراکترها می‌توانند با شاخص دسترسی پیدا کنند
۲. **کتابخانه متد غنی**: ۴۰+ متد برای دستکاری متن
۳. **گزینه‌های قالب‌بندی**: f-stringها، format()، قالب‌بندی %
۴. **پشتیبانی یونیکد**: متن را در هر زبان مدیریت کنید
۵. **عملکرد مهم است**: تغییرناپذیری و interning را در نظر بگیرید

## مطالعه بیشتر
- الگوریتم‌های رشته (KMP، Boyer-Moore) را مطالعه کنید
- تکنیک‌های فشرده‌سازی متن را بیاموزید
- پردازش زبان طبیعی را کاوش کنید
- چینش و بین‌المللی‌سازی را درک کنید