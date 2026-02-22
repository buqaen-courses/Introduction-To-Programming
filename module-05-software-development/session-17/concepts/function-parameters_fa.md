# پارامترهای تابع: مدیریت انعطاف‌پذیر ورودی

## مقدمه: فراتر از پارامترهای پایه

ما یاد گرفتیم چگونه توابعی با پارامترهای ساده ایجاد کنیم. اکنون روش‌های انعطاف‌پذیرتری برای مدیریت ورودی‌های تابع بررسی می‌کنیم که توابع شما را قدرتمندتر و استفاده از آنها آسان‌تر می‌کند.

### آنچه خواهیم پوشش داد

- آرگومان‌های موقعیتی در مقابل کلیدی‌واژه‌ای
- مقادیر پیش‌فرض با نکات مهم برای اجتناب
- تعداد متغیر آرگومان‌ها
- باز کردن مجموعه‌ها به عنوان آرگومان‌ها

---

## آرگومان‌های موقعیتی در مقابل کلیدی‌واژه‌ای

### آرگومان‌های موقعیتی (ترتیب مهم است)

```python
def create_user(username, email, age):
    """ایجاد کاربر با آرگومان‌های موقعیتی."""
    return {
        "username": username,
        "email": email,
        "age": age
    }

# باید دقیقاً به ترتیب باشد
user1 = create_user("alice123", "alice@email.com", 25)
user2 = create_user("bob456", "bob@email.com", 30)
```

**نکته کلیدی**: با آرگومان‌های موقعیتی، ترتیب همه چیز است!

### آرگومان‌های کلیدی‌واژه‌ای (ترتیب مهم نیست)

```python
# همان تابع، با آرگومان‌های کلیدی‌واژه‌ای فراخوانی شده
user3 = create_user(
    username="charlie789",
    email="charlie@email.com",
    age=35
)

# با کلیدی‌واژه‌ای ترتیب مهم نیست
user4 = create_user(
    age=28,
    username="diana101",
    email="diana@email.com"
)

# ترکیب موقعیتی و کلیدی‌واژه‌ای (موقعیتی اول!)
user5 = create_user("eve202", email="eve@email.com", age=32)
```

### چرا از کلیدی‌واژه‌ها استفاده کنیم؟

```python
def send_email(to, subject, body, priority="normal"):
    """ارسال ایمیل."""
    print(f"To: {to}")
    print(f"Subject: {subject}")
    print(f"Priority: {priority}")
    print(f"Body: {body}")

# بدون کلیدی‌واژه‌ها - معنی هر مقدار چیست؟
send_email("boss@company.com", "Meeting", "Hi...", "high")
# تشخیص هر کدام سخت است!

# با کلیدی‌واژه‌ها - کاملاً واضح!
send_email(
    to="boss@company.com",
    subject="Meeting tomorrow",
    body="Hi, can we meet tomorrow at 2pm?",
    priority="high"
)
```

**بهترین تمرین**: از آرگومان‌های کلیدی‌واژه‌ای وقتی استفاده کنید که:
- تابع پارامترهای زیادی دارد
- برخی پارامترها اختیاری هستند
- می‌خواهید کد خودتوضیح‌گر باشد

---

## پارامترهای پیش‌فرض

### مقادیر پیش‌فرض پایه

```python
def greet(name, greeting="Hello", punctuation="!"):
    """سلام به کسی با پیام قابل تنظیم."""
    print(f"{greeting}, {name}{punctuation}")

# استفاده از همه پیش‌فرض‌ها
greet("Alice")                           # Hello, Alice!

# رونویسی برخی پیش‌فرض‌ها
greet("Bob", greeting="Hi")              # Hi, Bob!
greet("Charlie", punctuation=".")        # Hello, Charlie.

# رونویسی همه
greet("Dave", "Howdy", "...")            # Howdy, Dave...
```

### قوانین مهم پارامترهای پیش‌فرض

**قانون ۱: پیش‌فرض‌ها در انتها قرار می‌گیرند**

```python
# غلط - SyntaxError!
def wrong(a="default", b):
    pass

# درست
def right(b, a="default"):
    pass
```

**قانون ۲: از پیش‌فرض‌های قابل تغییر استفاده نکنید!** (بسیار مهم!)

```python
# خطرناک - آرگومان پیش‌فرض قابل تغییر
def add_item_bad(item, shopping_list=[]):
    """این یک باگ پنهان دارد!"""
    shopping_list.append(item)
    return shopping_list

# فراخوانی اول
list1 = add_item_bad("apples")
print(list1)        # ['apples'] - خوب به نظر می‌رسد

# فراخوانی دوم
list2 = add_item_bad("bananas")
print(list2)        # ['apples', 'bananas'] - چه؟!

# list1 هم تغییر کرد!
print(list1)        # ['apples', 'bananas'] - غافلگیرکننده!
```

**مشکل**: لیست پیش‌فرض فقط یک بار هنگام تعریف تابع ایجاد می‌شود، نه در هر فراخوانی. بنابراین همه فراخوانی‌ها از یک لیست مشترک استفاده می‌کنند!

**راه‌حل**: از None به عنوان پیش‌فرض استفاده کنید

```python
# امن - استفاده از None به عنوان پیش‌فرض
def add_item_safe(item, shopping_list=None):
    """نسخه صحیح - بدون لیست مشترک."""
    if shopping_list is None:
        shopping_list = []    # هر بار لیست جدید ایجاد می‌شود
    shopping_list.append(item)
    return shopping_list

# هر فراخوانی لیست خودش را دارد
list1 = add_item_safe("apples")
print(list1)        # ['apples']

list2 = add_item_safe("bananas")
print(list2)        # ['bananas'] - لیست جداگانه!
```

**همیشه برای انواع قابل تغییر (لیست، دیکشنری، مجموعه) از None به عنوان پیش‌فرض استفاده کنید!**

---

## تعداد متغیر آرگومان‌ها

### *args - هر تعداد آرگومان موقعیتی

```python
def sum_all(*numbers):
    """جمع هر تعداد آرگومان."""
    total = 0
    for num in numbers:
        total += num
    return total

# فراخوانی با هر تعداد آرگومان
print(sum_all(1, 2, 3))              # 6
print(sum_all(10, 20, 30, 40))       # 100
print(sum_all())                     # 0 (بدون آرگومان)
print(sum_all(5))                    # 5 (یک آرگومان)

# داخل تابع، 'numbers' یک تاپل است
print(type(numbers))   # <class 'tuple'>
```

### **kwargs - هر تعداد آرگومان کلیدی‌واژه‌ای

```python
def create_profile(**info):
    """ایجاد پروفایل از هر آرگومان کلیدی‌واژه‌ای."""
    profile = {
        "created": True,
        "active": True
    }
    profile.update(info)  # افزودن تمام اطلاعات ارائه شده
    return profile

# فراخوانی با هر کلیدی‌واژه‌ای
user1 = create_profile(name="Alice", age=25, city="NYC")
user2 = create_profile(name="Bob", profession="Engineer")

print(user1)
# {'created': True, 'active': True, 'name': 'Alice', 'age': 25, 'city': 'NYC'}

print(user2)
# {'created': True, 'active': True, 'name': 'Bob', 'profession': 'Engineer'}
```

### ترکیب تمام انواع پارامترها

```python
def complex_function(required, *args, default="value", **kwargs):
    """
    تابع نمادین همه انواع پارامتر.

    required: باید ارائه شود
    *args: آرگومان‌های موقعیتی متغیر (تاپل)
    default: اختیاری با مقدار پیش‌فرض
    **kwargs: آرگومان‌های کلیدی‌واژه‌ای متغیر (دیکشنری)
    """
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Default: {default}")
    print(f"Kwargs: {kwargs}")

# نمونه‌های استفاده
complex_function("hello")
# Required: hello
# Args: ()
# Default: value
# Kwargs: {}

complex_function("hello", 1, 2, 3)
# Required: hello
# Args: (1, 2, 3)
# Default: value
# Kwargs: {}

complex_function("hello", 1, 2, 3, default="changed", extra="data")
# Required: hello
# Args: (1, 2, 3)
# Default: changed
# Kwargs: {'extra': 'data'}
```

**ترتیب مهم است**: `def func(regular, *args, default="val", **kwargs)`

---

## باز کردن آرگومان‌ها

### باز کردن لیست/تاپل به عنوان آرگومان‌ها

```python
def greet(first, middle, last):
    """سلام با نام کامل."""
    print(f"Hello, {first} {middle} {last}!")

# فراخوانی مستقیم
greet("John", "Quincy", "Adams")

# باز کردن از تاپل
name_parts = ("John", "Quincy", "Adams")
greet(*name_parts)   # معادل greet("John", "Quincy", "Adams")

# باز کردن از لیست
name_list = ["Jane", "Marie", "Doe"]
greet(*name_list)    # معادل greet("Jane", "Marie", "Doe")
```

### باز کردن دیکشنری به عنوان آرگومان‌ها

```python
def create_user(name, email, age, city="Unknown"):
    """ایجاد کاربر با فیلدهای الزامی و اختیاری."""
    return {
        "name": name,
        "email": email,
        "age": age,
        "city": city
    }

# باز کردن دیکشنری
user_data = {
    "name": "Alice",
    "email": "alice@example.com",
    "age": 25,
    "city": "NYC"
}

user = create_user(**user_data)
# معادل: create_user(name="Alice", email="alice@example.com", age=25, city="NYC")
```

### استفاده عملی: ادغام پیکربندی سرور

```python
def configure_server(host, port, debug=False, ssl=True, timeout=30):
    """پیکربندی سرور با گزینه‌های مختلف."""
    return {
        "host": host,
        "port": port,
        "debug": debug,
        "ssl": ssl,
        "timeout": timeout
    }

# پیکربندی پایه
base_config = {
    "host": "localhost",
    "port": 8080,
    "debug": False
}

# محیط توسعه (رونویسی debug)
dev_config = {**base_config, "debug": True}
server1 = configure_server(**dev_config)

# محیط تولید (افزودن SSL)
prod_config = {**base_config, "ssl": True, "timeout": 60}
server2 = configure_server(**prod_config)
```

---

## مثال‌های کاربردی

### مثال ۱: ثبت‌کننده انعطاف‌پذیر

```python
def log(message, level="INFO", timestamp=None, **metadata):
    """
    تابع ثبت لاگ انعطاف‌پذیر.

    Args:
        message: پیام لاگ
        level: سطح لاگ (DEBUG, INFO, WARNING, ERROR)
        timestamp: زمان‌مهر اختیاری (پیش‌فرض: همین الان)
        **metadata: هر جفت کلید-مقدار اضافی
    """
    import datetime

    if timestamp is None:
        timestamp = datetime.datetime.now()

    # ساخت ورودی لاگ
    entry = f"[{timestamp:%Y-%m-%d %H:%M:%S}] {level}: {message}"

    # افزودن متادیتا اگر وجود دارد
    if metadata:
        meta_str = ", ".join(f"{k}={v}" for k, v in metadata.items())
        entry += f" | {meta_str}"

    print(entry)

# استفاده
log("Application started")
# [2024-01-15 10:30:00] INFO: Application started

log("Error occurred", level="ERROR", file="data.txt", line=42)
# [2024-01-15 10:30:00] ERROR: Error occurred | file=data.txt, line=42

log("User login", user="alice", ip="192.168.1.1")
# [2024-01-15 10:30:00] INFO: User login | user=alice, ip=192.168.1.1
```

### مثال ۲: سازنده تگ HTML

```python
def tag(name, *children, **attributes):
    """
    ساخت یک تگ HTML با محتوا و ویژگی‌ها.

    Args:
        name: نام تگ (div, span, p, و غیره)
        *children: عناصر فرزند یا متن
        **attributes: ویژگی‌های HTML (class, id, style, و غیره)
    """
    # ساخت رشته ویژگی‌ها
    attrs = " ".join(f'{k}="{v}"' for k, v in attributes.items())
    if attrs:
        attrs = " " + attrs

    # ساخت محتوا
    content = "".join(str(child) for child in children)

    # ساخت تگ
    return f"<{name}{attrs}>{content}</{name}>"

# استفاده
print(tag("p", "Hello, World!"))
# <p>Hello, World!</p>

print(tag("div", "Content", class_="container", id="main"))
# <div class="container" id="main">Content</div>

# نکته: 'class' کلمه رزرو شده است، به جای آن 'class_' استفاده کنید
print(tag("span", "Important", class_="highlight"))
# <span class="highlight">Important</span>
```

### مثال ۳: سازنده کوئری پایگاه داده

```python
def build_query(table, columns="*", where=None, order_by=None, limit=None):
    """
    ساخت کوئری SQL SELECT.

    Args:
        table: نام جدول
        columns: ستون‌های انتخابی (پیش‌فرض: همه)
        where: شرایط WHERE (دیکشنری)
        order_by: ستون ORDER BY
        limit: مقدار LIMIT

    Returns:
        رشته کوئری SQL
    """
    query = f"SELECT {columns} FROM {table}"

    if where:
        conditions = " AND ".join(f"{k}='{v}'" for k, v in where.items())
        query += f" WHERE {conditions}"

    if order_by:
        query += f" ORDER BY {order_by}"

    if limit:
        query += f" LIMIT {limit}"

    return query

# استفاده
print(build_query("users"))
# SELECT * FROM users

print(build_query("users", columns="name, email", where={"active": "true"}))
# SELECT name, email FROM users WHERE active='true'

print(build_query("products", where={"category": "electronics"}, order_by="price", limit=10))
# SELECT * FROM products WHERE category='electronics' ORDER BY price LIMIT 10
```

---

## اشتباهات رایج مبتدی‌ها

### اشتباه ۱: آرگومان‌های پیش‌فرض قابل تغییر (دوباره!)

```python
# خطرناک
def append_timestamp(timestamps=[]):
    import time
    timestamps.append(time.time())
    return timestamps

# امن
def append_timestamp(timestamps=None):
    if timestamps is None:
        timestamps = []
    import time
    timestamps.append(time.time())
    return timestamps
```

### اشتباه ۲: ترتیب اشتباه آرگومان‌ها

```python
def process_data(data, format="json", validate=True):
    pass

# غلط - کلیدی‌واژه قبل از موقعیتی
process_data(format="xml", my_data)  # SyntaxError!

# درست
process_data(my_data, format="xml")
```

### اشتباه ۳: فراموش کردن باز کردن

```python
def add_three(a, b, c):
    return a + b + c

numbers = [1, 2, 3]

# غلط - لیست را به عنوان آرگومان واحد منتقل می‌کند
result = add_three(numbers)  # TypeError!

# درست - باز کردن لیست
result = add_three(*numbers)  # برمی‌گرداند 6
```

### اشتباه ۴: اشتباه گرفتن * و **

```python
def func(*args, **kwargs):
    pass

# غلط
data = {"a": 1, "b": 2}
func(*data)     # کلیدها را باز می‌کند: func("a", "b")

# درست - استفاده از ** برای دیکشنری‌ها
func(**data)    # func(a=1, b=2)

# لیست‌ها از * استفاده می‌کنند
nums = [1, 2, 3]
func(*nums)     # func(1, 2, 3)
```

---

## تمرین‌های عملی

### تمرین ۱: محاسبه‌گر میانگین وزن‌دار

تابعی ایجاد کنید که میانگین را با وزن‌های اختیاری محاسبه می‌کند.

```python
def weighted_average(*values, weights=None):
    """
    محاسبه میانگین مقادیر.
    اگر وزن‌ها ارائه شده باشند، میانگین وزن‌دار محاسبه می‌کند.
    """
    # کد شما اینجا
    pass

# تست
print(weighted_average(10, 20, 30))                    # 20.0
print(weighted_average(10, 20, 30, weights=[1, 2, 3]))  # 23.33
```

### تمرین ۲: تابع فرمت‌دهی

یک فرمت‌کننده رشته انعطاف‌پذیر ایجاد کنید.

```python
def format_line(template, *values, separator=" | ", align="left"):
    """
    قالب‌بندی مقادیر بر اساس الگو.
    separator: رشته بین مقادیر
    align: "left", "right", یا "center"
    """
    # کد شما اینجا
    pass

# تست
print(format_line("Name: {}, Age: {}", "Alice", 25))
print(format_line("{} - {}", "Item", "$10.00", separator=" | "))
```

### تمرین ۳: سازنده کادر متن

تابعی ایجاد کنید که تزیینات چاپی می‌سازد.

```python
def make_box(*texts, padding=1, char="*"):
    """
    ایجاد کادر متن با فاصله.
    مثال: make_box("Title", "Subtitle", padding=2, char="#")
    """
    # کد شما اینجا
    pass

# تست
print(make_box("Welcome", padding=1, char="*"))
# باید چیزی شبیه به این چاپ کند:
# ***********
# *         *
# * Welcome *
# *         *
# ***********
```

### تمرین ۴: ترکیب‌کننده توابع

تابعی ایجاد کنید که توابع دیگر را با آرگومان‌ها فراخوانی می‌کند.

```python
def apply_functions(value, *functions):
    """
    اعمال هر تابع به مقدار به ترتیب.
    نتیجه نهایی را برمی‌گرداند.
    """
    # کد شما اینجا
    pass

# تست
def double(x): return x * 2
def add_one(x): return x + 1
def square(x): return x ** 2

result = apply_functions(3, double, add_one, square)
# باید باشد: ((3 * 2) + 1) ** 2 = 49
```

---

## نکات کلیدی

1. **آرگومان‌های کلیدی‌واژه‌ای وضوح را بهبود می‌بخشند** - از آنها مخصوصاً با پارامترهای زیاد استفاده کنید
2. **از پیش‌فرض‌های قابل تغییر اجتناب کنید** - از `None` استفاده کنید و داخل تابع بررسی کنید
3. **`*args` آرگومان‌های موقعیتی اضافی را می‌گیرد** - یک تاپل می‌شود
4. **`**kwargs` آرگومان‌های کلیدی‌واژه‌ای اضافی را می‌گیرد** - یک دیکشنری می‌شود
5. **باز کردن با `*`** - از `func(*list)` برای منتقل کردن اعضای لیست به عنوان آرگومان‌های جداگانه استفاده کنید
6. **باز کردن با `**`** - از `func(**dict)` برای منتقل کردن اعضای دیکشنری به عنوان آرگومان‌های کلیدی‌واژه‌ای استفاده کنید

## کارت مرجع سریع

| ویژگی | سینتکس | داخل تابع |
|---------|--------|----------------|
| پارامتر معمولی | `def f(a, b)` | متغیرهای عادی |
| مقدار پیش‌فرض | `def f(a, b=1)` | b برابر ۱ اگر ارائه نشود |
| پیش‌فرض قابل تغییر | `def f(a, b=None)` | بررسی `if b is None` |
| موقعیتی متغیر | `def f(*args)` | `args` یک تاپل است |
| کلیدی‌واژه‌ای متغیر | `def f(**kwargs)` | `kwargs` یک دیکشنری است |
| باز کردن لیست | `f(*my_list)` | به عنوان آرگومان‌های جداگانه منتقل می‌کند |
| باز کردن دیکشنری | `f(**my_dict)` | به عنوان آرگومان‌های کلیدی‌واژه‌ای منتقل می‌کند |

---

## مطالعه بیشتر

- **درس بعدی**: طراحی ماژولار - سازماندهی توابع در گروه‌های منطقی
- **تمرین**: تمام تمرین‌های بالا را کامل کنید
- **چالش**: یک چارچوب کوچک برای ساخت رابط‌های خط فرمان ایجاد کنید
- **کاوش**: درباره دکوراتورهای تابع یاد بگیرید (`@decorator`)
