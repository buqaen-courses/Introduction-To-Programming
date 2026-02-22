# پردازش متن در پایتون

## آنچه خواهید آموخت
- چگونه متن را تحلیل و دستکاری کنید
- اعتبارسنجی و پاکسازی داده‌ها
- الگوهای رایج پردازش متن
- مثال‌های کاربردی

---

## تحلیل متن

### شمارش کلمات

```python
def count_words(text):
    words = text.split()
    return len(words)

text = "Python is a powerful programming language"
print(f"Word count: {count_words(text)}")  # 6
```

### شمارش کاراکترها

```python
text = "Hello World"

# همه کاراکترها
print(f"Characters: {len(text)}")  # 11

# بدون فاصله
no_spaces = text.replace(" ", "")
print(f"Without spaces: {len(no_spaces)}")  # 10

# فقط حروف
letters_only = "".join(c for c in text if c.isalpha())
print(f"Letters only: {len(letters_only)}")  # 10
```

---

## پاکسازی و نرمال‌سازی

### حذف کاراکترهای اضافی

```python
def clean_text(text):
    # حذف فاصله‌های اضافی
    text = text.strip()
    
    # تبدیل به حروف کوچک
    text = text.lower()
    
    # حذف کاراکترهای خاص
    allowed = set("abcdefghijklmnopqrstuvwxyz0123456789 ")
    text = "".join(c for c in text if c in allowed)
    
    # حذف فاصله‌های متعدد
    words = text.split()
    text = " ".join(words)
    
    return text

# آزمایش
dirty = "  Hello!!! World...  "
print(clean_text(dirty))  # hello world
```

---

## اعتبارسنجی

### اعتبارسنجی ایمیل (ساده)

```python
def is_valid_email(email):
    # بررسی پایه
    if "@" not in email:
        return False
    
    if "." not in email:
        return False
    
    # نباید با @ شروع یا تمام شود
    if email.startswith("@") or email.endswith("@"):
        return False
    
    # نباید با . شروع یا تمام شود
    if email.startswith(".") or email.endswith("."):
        return False
    
    return True

# آزمایش
emails = ["test@example.com", "invalid", "@test.com", "test@.com"]
for email in emails:
    print(f"{email}: {is_valid_email(email)}")
```

### اعتبارسنجی شماره تلفن

```python
def clean_phone(phone):
    # حذف همه به جز اعداد
    digits = "".join(c for c in phone if c.isdigit())
    return digits

def is_valid_phone(phone):
    digits = clean_phone(phone)
    return len(digits) == 10

# آزمایش
phones = ["(123) 456-7890", "123-456-7890", "123456789", "123-456-78901"]
for phone in phones:
    print(f"{phone}: {is_valid_phone(phone)}")
```

---

## تبدیل و تغییر شکل

### CamelCase به snake_case

```python
def camel_to_snake(name):
    result = []
    for i, char in enumerate(name):
        if char.isupper() and i > 0:
            result.append("_")
        result.append(char.lower())
    return "".join(result)

# آزمایش
print(camel_to_snake("helloWorld"))      # hello_world
print(camel_to_snake("myVariableName")) # my_variable_name
```

### snake_case به CamelCase

```python
def snake_to_camel(name):
    words = name.split("_")
    return words[0] + "".join(word.title() for word in words[1:])

# آزمایش
print(snake_to_camel("hello_world"))      # helloWorld
print(snake_to_camel("my_variable_name")) # myVariableName
```

---

## استخراج اطلاعات

### یافتن اعداد در متن

```python
def extract_numbers(text):
    numbers = []
    current = ""
    
    for char in text:
        if char.isdigit():
            current += char
        elif current:
            numbers.append(int(current))
            current = ""
    
    if current:
        numbers.append(int(current))
    
    return numbers

# آزمایش
text = "I have 5 apples and 3 oranges, total 8 fruits"
print(extract_numbers(text))  # [5, 3, 8]
```

### استخراج URL

```python
def extract_urls(text):
    words = text.split()
    urls = []
    
    for word in words:
        if word.startswith("http://") or word.startswith("https://"):
            urls.append(word)
    
    return urls

# آزمایش
text = "Visit https://example.com or http://test.org for more info"
print(extract_urls(text))  # ['https://example.com', 'http://test.org']
```

---

## الگوهای رایج

### پیدا کردن و جایگزینی چندگانه

```python
def multi_replace(text, replacements):
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

# آزمایش
replacements = {
    " Mr. ": " Mister ",
    " Dr. ": " Doctor ",
    " e.g. ": " for example ",
    " i.e. ": " that is "
}

text = "Mr. Smith, Dr. Jones, e.g. this, i.e. that"
print(multi_replace(text, replacements))
```

### حذف کلمات توقف (Stop Words)

```python
STOP_WORDS = {"the", "a", "an", "in", "on", "at", "to", "for", "of", "and"}

def remove_stop_words(text):
    words = text.lower().split()
    filtered = [w for w in words if w not in STOP_WORDS]
    return " ".join(filtered)

# آزمایش
text = "The quick brown fox jumps over the lazy dog"
print(remove_stop_words(text))
# quick brown fox jumps over lazy dog
```

---

## خودتان امتحان کنید: تمرین‌ها

### تمرین 1: تحلیل متن

تابعی بنویسید که تحلیل متن ارائه دهد:
- تعداد کلمات
- تعداد جملات
- متوسط طول کلمه
- کلمات منحصر به فرد

<details>
<summary>برای دیدن پاسخ کلیک کنید</summary>

```python
def analyze_text(text):
    # کلمات
    words = text.split()
    word_count = len(words)
    
    # جملات (ساده - بر اساس نقطه، علامت سوال، تعجب)
    sentences = text.count(".") + text.count("?") + text.count("!")
    if sentences == 0:
        sentences = 1
    
    # متوسط طول کلمه
    word_lengths = [len(w.strip(".,!?;:")) for w in words]
    avg_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0
    
    # کلمات منحصر به فرد
    unique_words = set(w.lower().strip(".,!?;:") for w in words)
    
    return {
        "word_count": word_count,
        "sentence_count": sentences,
        "avg_word_length": round(avg_length, 2),
        "unique_words": len(unique_words)
    }

# آزمایش
text = "Python is great. Python is easy. I love Python!"
result = analyze_text(text)
for key, value in result.items():
    print(f"{key}: {value}")
```

</details>

### تمرین 2: ماسک کردن اطلاعات حساس

تابعی بنویسید که:
- شماره کارت اعتباری را ماسک کند (فقط 4 رقم آخر را نشان دهد)
- ایمیل را ماسک کند (قبل از @ را مخفی کند)

<details>
<summary>برای دیدن پاسخ کلیک کنید</summary>

```python
def mask_credit_card(card):
    # حذف همه به جز اعداد
    digits = "".join(c for c in card if c.isdigit())
    if len(digits) != 16:
        return "Invalid card"
    return "****-****-****-" + digits[-4:]

def mask_email(email):
    if "@" not in email:
        return "Invalid email"
    
    parts = email.split("@")
    name = parts[0]
    domain = parts[1]
    
    # مخفی کردن همه به جز اول و آخر
    if len(name) <= 2:
        masked_name = "*" * len(name)
    else:
        masked_name = name[0] + "*" * (len(name) - 2) + name[-1]
    
    return masked_name + "@" + domain

# آزمایش
print(mask_credit_card("1234-5678-9012-3456"))  # ****-****-****-3456
print(mask_email("john.doe@example.com"))       # j*******e@example.com
```

</details>

---

## نکات کلیدی

1. **split() و join() قدرتمندند** - برای تجزیه و ترکیب
2. **لیست‌تفسیری برای فیلتر کردن** - `[x for x in items if condition]`
3. **isX() برای بررسی نوع** - `isdigit()`, `isalpha()`, `isalnum()`
4. **re برای عبارات باقاعده** - برای الگوهای پیچیده (در بخش پیشرفته)
5. **همیشه پاکسازی کنید** - قبل از پردازش، داده را پاک کنید

---

## قدم بعدی چیست؟

اکنون می‌توانید متن را پردازش کنید! بعدی، ما یاد می‌گیریم:
- لیست‌ها در پایتون
- ذخیره و دستکاری مجموعه‌ها
- ساختارهای داده پیشرفته
