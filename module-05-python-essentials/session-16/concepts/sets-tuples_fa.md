# مجموعه‌ها و تاپل‌ها: مجموعه‌های تخصصی

## مقدمه: چه موقع از چه چیزی استفاده کنیم

پایتون چند نوع مجموعه داخلی به ما می‌دهد. اینجا می‌بینید هرکدام را کِی به کار ببرید:

| نوع | چه وقتی استفاده کنید... | مثال |
|-----|------------------------|------|
| **فهرست** | ترتیب مهم است، تکراری اشکالی ندارد | فهرست خرید با چند سیب |
| **دیکشنری** | به جفت کلید-مقدار نیاز دارید | نمرات دانشجوها بر اساس نام |
| **تاپل** | داده نباید تغییر کند | مختصات (x و y) |
| **مجموعه** | فقط به آیتم‌های یکتا اهمیت می‌دهید، ترتیب مهم نیست | بازدیدکنندگان یکتای سایت |

---

## تاپل‌ها: دنباله‌های تغییرناپذیر

### تاپل چیست؟

**تاپل** مثل یک فهرست است که پس از ساخته شدن نمی‌توان تغییرش داد. مثل یک ظرف پلمب فکرش کنید: می‌توانید داخلش را ببینید، ولی نمی‌توانید محتوایش را تغییر دهید.

```python
# ساخت تاپل
coordinates = (10, 20)
person = ("Alice", 25, "Engineer")
```

### چرا از تاپل استفاده کنیم؟

۱. **محافظت**: داده‌ای که نباید به‌طور تصادفی تغییر کند
۲. **کارایی**: تاپل‌ها کمی از فهرست‌ها سریع‌ترند
۳. **کلید دیکشنری**: تاپل می‌تواند کلید دیکشنری باشد (فهرست نمی‌تواند!)
۴. **بازگشت چندمقداری از تابع**

### ساخت تاپل

```python
# تاپل خالی
empty = ()
empty = tuple()

# تاپل تک‌عنصری (به کاما نیاز دارد!)
single = (42,)   # ← به کاما دقت کنید!
not_a_tuple = (42)  # این فقط عدد ۴۲ در پرانتز است

# چند عنصر
point = (3, 4)
colors = ("red", "green", "blue")

# بدون پرانتز (tuple packing)
values = 1, 2, 3   # مثل (1, 2, 3)

# از اشیاء iterable دیگر
letters = tuple("hello")   # ('h', 'e', 'l', 'l', 'o')
numbers = tuple([1, 2, 3]) # (1, 2, 3)
```

### دسترسی به عناصر تاپل

```python
point = (3, 4, 5)

# مثل فهرست - از اندیس استفاده کنید
x = point[0]        # 3
y = point[1]        # 4
last = point[-1]    # 5

# برش هم کار می‌کند
first_two = point[:2]    # (3, 4)
```

### عملیات روی تاپل

```python
t1 = (1, 2, 3)
t2 = (4, 5, 6)

# الحاق (تاپل تازه می‌سازد)
combined = t1 + t2      # (1, 2, 3, 4, 5, 6)

# تکرار
repeated = t1 * 3       # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# طول
size = len(t1)          # 3

# حضور
two_in_t1 = 2 in t1     # True

# count و index (مثل فهرست)
count = t1.count(2)     # 1
position = t1.index(2)  # 1
```

### مهم: تاپل‌ها تغییرناپذیرند

```python
point = (3, 4)

# اشتباه - نمی‌توان تغییر داد!
point[0] = 5   # TypeError!

# درست - تاپل تازه بسازید
new_point = (5, point[1])   # (5, 4)
```

### باز کردن تاپل (Tuple Unpacking)

```python
# نسبت دادن مقادیر تاپل به چند متغیر
point = (10, 20)
x, y = point
print(x)    # 10
print(y)    # 20

# باز کردن گسترده
first, *middle, last = (1, 2, 3, 4, 5)
print(first)    # 1
print(middle)   # [2, 3, 4]
print(last)     # 5

# نادیده گرفتن مقادیر ناخواسته
name, _, age = ("Alice", "female", 25)
print(name, age)    # Alice 25

# جابه‌جایی مقادیر (پایتونی!)
a, b = 1, 2
a, b = b, a
print(a, b)    # 2 1
```

### بازگشت چندمقدادی

```python
def get_min_max(numbers):
    """Return both min and max."""
    return min(numbers), max(numbers)

# باز کردن تاپل بازگشتی
minimum, maximum = get_min_max([3, 1, 4, 1, 5])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 5

# یا گرفتنش به‌عنوان تاپل
result = get_min_max([3, 1, 4, 1, 5])
print(result)   # (1, 5)
```

---

## مجموعه‌ها: مجموعه‌ای از عناصر یکتا

### مجموعه چیست؟

**مجموعه** مجموعه‌ای بدون ترتیب از آیتم‌های یکتاست. مثل کیسه‌ای فکر کنید که نمی‌توانید تکراری داشته باشید و نمی‌توانید به ترتیبش اعتماد کنید.

```python
# ساخت مجموعه
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
```

### چرا از مجموعه استفاده کنیم؟

۱. **حذف خودکار تکراری‌ها**: مجموعه‌ها فقط آیتم‌های یکتا را نگه می‌دارند
۲. **تست سریع حضور**: بررسی وجود یک آیتم بسیار سریع است
۳. **عملیات ریاضی**: اجتماع، اشتراک، تفاضل
۴. **حذف تکراری‌ها از فهرست**: تبدیل آسان

### ساخت مجموعه

```python
# مجموعه خالی (نه {} - آن دیکشنری خالی است!)
empty = set()

# مجموعه با مقادیر
fruits = {"apple", "banana", "cherry"}

# از فهرست (تکراری‌ها را حذف می‌کند!)
numbers = set([1, 2, 2, 3, 3, 3, 4])
# Result: {1, 2, 3, 4}

# از رشته (کاراکترهای یکتا)
unique_chars = set("hello")
# Result: {'h', 'e', 'l', 'o'}
```

### مهم: مجموعه‌ها بدون ترتیب‌اند

```python
my_set = {3, 1, 4, 1, 5}
print(my_set)
# Might print: {1, 3, 4, 5} (ترتیب تضمین‌شده نیست!)

# نمی‌توان با اندیس دسترسی داشت
my_set[0]   # TypeError!
```

### عملیات مجموعه

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# اجتماع - عناصری که در یکی از دو مجموعه‌اند
union = set1 | set2              # {1, 2, 3, 4, 5, 6}
union = set1.union(set2)         # همان چیز

# اشتراک - عناصری که در هر دو مجموعه‌اند
intersection = set1 & set2       # {3, 4}
intersection = set1.intersection(set2)

# تفاضل - در set1 هست ولی در set2 نیست
diff = set1 - set2               # {1, 2}
diff = set1.difference(set2)

# تفاضل متقارن - در یکی هست ولی در هر دو نیست
sym_diff = set1 ^ set2           # {1, 2, 5, 6}
sym_diff = set1.symmetric_difference(set2)
```

### متدهای مجموعه

```python
fruits = {"apple", "banana"}

# افزودن یک عنصر
fruits.add("cherry")      # {"apple", "banana", "cherry"}

# افزودن چند عنصر
fruits.update(["date", "elderberry", "fig"])

# حذف (اگر پیدا نشود خطا می‌دهد)
fruits.remove("banana")

# حذف (اگر پیدا نشود خطا نمی‌دهد)
fruits.discard("grape")   # حتی اگر "grape" نباشد خطا نمی‌دهد

# حذف و بازگرداندن یک عنصر دلخواه
removed = fruits.pop()

# بررسی حضور
"apple" in fruits         # True

# خالی کردن همه
fruits.clear()            # set()
```

### Set Comprehension

```python
# مثل list comprehension ولی برای مجموعه
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# اعداد زوج
evens = {x for x in numbers if x % 2 == 0}
# Result: {2, 4, 6, 8, 10}

# مربع‌ها
squares = {x ** 2 for x in range(1, 6)}
# Result: {1, 4, 9, 16, 25}
```

---

## مثال‌های کاربردی

### مثال ۱: حذف تکراری‌ها از فهرست

```python
def remove_duplicates(items):
    """Remove duplicates while preserving order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Usage
original = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = remove_duplicates(original)
print(unique)   # [1, 2, 3, 4]

# راه سریع (ترتیب را از دست می‌دهد)
unique_fast = list(set(original))
```

### مثال ۲: پیدا کردن دوستان مشترک

```python
def find_common_friends(user1_friends, user2_friends):
    """Find friends that both users have."""
    set1 = set(user1_friends)
    set2 = set(user2_friends)
    return set1 & set2

# Usage
alice_friends = ["Bob", "Charlie", "Diana", "Eve"]
bob_friends = ["Alice", "Charlie", "Eve", "Frank"]

common = find_common_friends(alice_friends, bob_friends)
print(f"Common friends: {common}")  # {'Charlie', 'Eve'}

# پیدا کردن آنچه فقط مال یکی است
alice_only = set(alice_friends) - set(bob_friends)
bob_only = set(bob_friends) - set(alice_friends)
```

### مثال ۳: اعتبارسنجی ورودی کاربر

```python
def validate_selection(user_selection, valid_options):
    """Check if user selected valid options."""
    user_set = set(user_selection)
    valid_set = set(valid_options)

    # پیدا کردن گزینه‌های نامعتبر
    invalid = user_set - valid_set

    # پیدا کردن موارد الزامی جاافتاده
    missing = valid_set - user_set

    return {
        "valid": not invalid,
        "invalid": invalid,
        "all_selected": not missing,
        "missing": missing
    }

# Usage
valid_colors = ["red", "green", "blue", "yellow"]
user_picked = ["red", "purple", "green"]

result = validate_selection(user_picked, valid_colors)
print(f"Invalid colors: {result['invalid']}")  # {'purple'}
```

### مثال ۴: تنظیمات به‌صورت تاپل

```python
# برای تنظیماتی که نباید تغییر کنند از تاپل استفاده کنید
DATABASE_CONFIG = (
    "localhost",  # host
    5432,         # port
    "myapp",      # database
    "user",       # username
    "password"    # password
)

# برای استفاده باز کنید
host, port, dbname, user, password = DATABASE_CONFIG

# نمی‌توان به‌طور تصادفی تغییرش داد
# DATABASE_CONFIG[0] = "other"  # TypeError!
```

### مثال ۵: تحلیل واژگان

```python
def analyze_vocab(text1, text2):
    """Compare vocabulary between two texts."""
    # استخراج کلمات (ساده‌شده)
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())

    # حذف نقطه‌گذاری (ساده)
    punctuation = ".,!?;:'\""
    for p in punctuation:
        words1 = {w.replace(p, "") for w in words1}
        words2 = {w.replace(p, "") for w in words2}

    # حذف رشته‌های خالی
    words1 = {w for w in words1 if w}
    words2 = {w for w in words2 if w}

    return {
        "unique_to_text1": words1 - words2,
        "unique_to_text2": words2 - words1,
        "common": words1 & words2,
        "total_unique": words1 | words2
    }

# Usage
text_a = "Python is great for data science"
text_b = "Python is also great for web development"

analysis = analyze_vocab(text_a, text_b)
print(f"Common words: {analysis['common']}")
print(f"Unique to text A: {analysis['unique_to_text1']}")
```

---

## اشتباهات رایج مبتدی

### اشتباه ۱: ساخت مجموعه خالی به شکل غلط

```python
# اشتباه - این دیکشنری خالی می‌سازد!
empty = {}
type(empty)   # <class 'dict'>

# درست
empty = set()
type(empty)   # <class 'set'>
```

### اشتباه ۲: فراموش کردن کامای تاپل

```python
# اشتباه - این تاپل نیست!
single = (5)
type(single)   # <class 'int'>

# درست
single = (5,)
type(single)   # <class 'tuple'>
```

### اشتباه ۳: تلاش برای دسترسی به مجموعه با اندیس

```python
my_set = {1, 2, 3}

# اشتباه
first = my_set[0]   # TypeError!

# درست - به فهرست تبدیل یا پیمایش کنید
first = list(my_set)[0]   # کار می‌کند ولی ترتیب تضمین‌شده نیست
# یا بهتر:
for item in my_set:
    print(item)
    break
```

### اشتباه ۴: تغییر عناصر تاپل

```python
point = (3, 4)

# اشتباه
point[0] = 5   # TypeError!

# درست - تاپل تازه بسازید
new_point = (5, point[1])
# یا به فهرست تبدیل و برگردانید
temp = list(point)
temp[0] = 5
new_point = tuple(temp)
```

---

## مقایسه انواع مجموعه

### هرکدام را کِی به کار برید

```python
# فهرست - مرتب، تغییرپذیر، تکراری مجاز
shopping = ["milk", "eggs", "milk"]  # می‌تواند دو شیر داشته باشد
shopping.append("bread")              # می‌تواند آیتم اضافه کند

# تاپل - مرتب، تغییرناپذیر، تکراری مجاز
coordinates = (40.7128, -74.0060)    # مختصات ثابت
color_rgb = (255, 128, 0)             # رنگ ثابت

# مجموعه - بدون ترتیب، تغییرپذیر، فقط یکتا
unique_visitors = {"alice", "bob", "alice"}  # فقط یک "alice"
unique_visitors.add("charlie")              # می‌تواند اضافه کند

# دیکشنری - جفت کلید-مقدار، مرتب، تغییرپذیر
student = {"name": "Alice", "grade": "A"}
student["age"] = 20                  # می‌تواند کلید تازه اضافه کند
```

### مقایسه کارایی

```python
# تست حضور (بررسی وجود یک آیتم)
large_list = list(range(10000))
large_set = set(range(10000))

# مجموعه برای بررسی وجود آیتم بسیار سریع‌تر است
9999 in large_list   # کند - آیتم‌ها را یکی‌یکی بررسی می‌کند
9999 in large_set    # سریع - از جدول هش استفاده می‌کند

# ولی فهرست برای دسترسی مرتب بهتر است
large_list[5000]     # سریع - دسترسی مستقیم با اندیس
# large_set[5000]    # خطا! مجموعه از اندیس پشتیبانی نمی‌کند
```

---

## تمرین‌ها

### تمرین ۱: پیدا کردن اعداد جاافتاده
پیدا کنید کدام اعداد از ۱ تا N در یک فهرست نیستند.

```python
def find_missing(numbers, n):
    """Return set of missing numbers from 1 to n."""
    # کد شما اینجا
    pass

# Test
print(find_missing([1, 2, 4, 6], 6))
# Should return: {3, 5}
```

### تمرین ۲: بررسی آناگرام
بررسی کنید آیا دو کلمه آناگرامند (حروف یکسانی دارند).

```python
def is_anagram(word1, word2):
    """Return True if word1 and word2 are anagrams."""
    # کد شما اینجا
    pass

# Test
print(is_anagram("listen", "silent"))   # True
print(is_anagram("hello", "world"))      # False
```

### تمرین ۳: سبد سهام
خریدهای سهام را پیگیری کنید و میانگین قیمت را حساب کنید.

```python
def add_purchase(portfolio, stock, price, shares):
    """Add stock purchase to portfolio."""
    # کد شما اینجا
    pass

def get_average_cost(portfolio, stock):
    """Calculate average cost per share for a stock."""
    # کد شما اینجا
    pass

# Test
portfolio = {}
add_purchase(portfolio, "AAPL", 150.00, 10)
add_purchase(portfolio, "AAPL", 155.00, 5)
add_purchase(portfolio, "GOOGL", 2800.00, 2)

print(get_average_cost(portfolio, "AAPL"))   # Should be ~151.67
```

### تمرین ۴: مرتب‌سازی تاپل
فهرستی از تاپل‌ها را بر اساس عنصر دوم مرتب کنید.

```python
def sort_by_second(items):
    """Sort list of tuples by second element."""
    # کد شما اینجا
    pass

# Test
data = [(1, 5), (2, 3), (3, 8), (4, 1)]
result = sort_by_second(data)
# Should return: [(4, 1), (2, 3), (1, 5), (3, 8)]
```

---

## نکات کلیدی

۱. **تاپل‌ها تغییرناپذیرند**: وقتی داده نباید تغییر کند به کارشان ببرید
۲. **مجموعه‌ها برای آیتم‌های یکتاست**: تکراری‌ها را خودکار حذف می‌کنند
۳. **مجموعه‌ها بدون ترتیب‌اند**: نمی‌توانید روی موقعیت یا ترتیب حساب کنید
۴. **مجموعه‌ها سریع‌اند**: تست حضور O(1) در برابر O(n) برای فهرست
۵. **از `set()` استفاده کنید نه `{}`**: پرانتز خالی دیکشنری می‌سازد!
۶. **کامای تاپل مهم است**: `(x,)` تاپل است، `(x)` نیست

## کارت مرجع سریع

| عملیات | تاپل | مجموعه |
|--------|------|--------|
| ساخت | `(1, 2, 3)` یا `tuple()` | `{1, 2, 3}` یا `set()` |
| خالی | `()` | `set()` (نه `{}`) |
| دسترسی | `t[0]` | با اندیس نمی‌توان |
| بررسی حضور | `x in t` | `x in s` (سریع‌تر!) |
| افزودن عنصر | نمی‌توان (تغییرناپذیر) | `s.add(x)` |
| حذف | نمی‌توان | `s.remove(x)` یا `s.discard(x)` |
| طول | `len(t)` | `len(s)` |
| عناصر یکتا | مربوط نیست (تکراری دارد) | خودکار |
| اجتماع | مربوط نیست | `s1 \| s2` یا `s1.union(s2)` |
| اشتراک | مربوط نیست | `s1 & s2` یا `s1.intersection(s2)` |
| تفاضل | مربوط نیست | `s1 - s2` یا `s1.difference(s2)` |

---

## مطالعه بیشتر

- **درس بعدی**: تعریف تابع، ساخت بلوک‌های قابل استفاده مجدد کد
- **تمرین**: همه تمرین‌های بالا را کامل کنید
- **چالش**: با یک مجموعه از کلمات معتبر یک املاشناس ساده بسازید
- **کاوش کنید**: `frozenset` را امتحان کنید، نسخه تغییرناپذیر مجموعه که می‌تواند کلید دیکشنری باشد