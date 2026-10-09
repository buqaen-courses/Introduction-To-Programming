# پارامترهای تابع: مدیریت پیشرفته آرگومان‌ها

## انواع پارامتر و مکانیسم‌های ارسال

توابع پایتون از انواع مختلف پارامتر و مکانیسم‌های ارسال آرگومان پشتیبانی می‌کنند که انعطاف‌پذیری را در نحوه فراخوانی و استفاده از توابع فراهم می‌کنند.

## آرگومان‌های موقعیتی در برابر کلیدی

### آرگومان‌های موقعیتی
```python
def create_user(username, email, age):
    """ایجاد کاربر با آرگومان‌های موقعیتی."""
    return {
        "username": username,
        "email": email,
        "age": age
    }

# باید به ترتیب دقیق فراخوانی شوند
user1 = create_user("alice123", "alice@email.com", 25)
user2 = create_user("bob456", "bob@email.com", 30)
```

### آرگومان‌های کلیدی
```python
# همان تابع، فراخوانی با آرگومان‌های کلیدی
user3 = create_user(
    username="charlie789",
    email="charlie@email.com",
    age=35
)

# ترتیب با آرگومان‌های کلیدی مهم نیست
user4 = create_user(
    age=28,
    username="diana101",
    email="diana@email.com"
)

# ترکیب موقعیتی و کلیدی (موقعیتی اول)
user5 = create_user("eve202", email="eve@email.com", age=32)
```

## مقادیر پیش‌فرض پارامترها

### مقادیر پیش‌فرض پایه
```python
def send_email(to, subject, body="", priority="normal"):
    """ارسال ایمیل با مقادیر پیش‌فرض."""
    email = {
        "to": to,
        "subject": subject,
        "body": body,
        "priority": priority
    }
    print(f"ارسال ایمیل: {email}")
    return True

# استفاده از پیش‌فرض‌ها
send_email("user@example.com", "Welcome!")

# بازنویسی برخی پیش‌فرض‌ها
send_email("user@example.com", "Alert", "System maintenance tonight", "high")

# بازنویسی همه
send_email("user@example.com", "Invoice", "Your bill is ready", "normal")
```

### ملاحظات مقدار پیش‌فرض
```python
# مشکل‌دار - آرگومان پیش‌فرض قابل تغییر
def add_item(item, shopping_list=[]):
    """افزودن آیتم به لیست خرید (نسخه مشکل‌دار)."""
    shopping_list.append(item)
    return shopping_list

# رفتار غیرمنتظره
list1 = add_item("apples")
print(list1)  # ['apples']

list2 = add_item("bananas")
print(list2)  # ['apples', 'bananas'] - لیست یکسان!

# نسخه اصلاح شده
def add_item_fixed(item, shopping_list=None):
    """افزودن آیتم به لیست خرید (نسخه صحیح)."""
    if shopping_list is None:
        shopping_list = []
    shopping_list.append(item)
    return shopping_list

list3 = add_item_fixed("apples")
list4 = add_item_fixed("bananas")
print(list3)  # ['apples']
print(list4)  # ['bananas']
```

### ارزیابی مقادیر پیش‌فرض
```python
import time

def log_message(message, timestamp=None):
    """ثبت پیام با timestamp."""
    if timestamp is None:
        timestamp = time.time()  # ارزیابی شده وقتی تابع فراخوانی می‌شود
    print(f"[{timestamp}] {message}")

# هر فراخوانی timestamp متفاوتی دریافت می‌کند
log_message("Starting process")
time.sleep(1)
log_message("Process complete")

# بد - فقط یک بار ارزیابی می‌شود وقتی تابع تعریف می‌شود
def log_message_bad(message, timestamp=time.time()):
    """این مشکل‌دار است."""
    print(f"[{timestamp}] {message}")

# هر دو فراخوانی از timestamp یکسان استفاده می‌کنند
log_message_bad("First message")
log_message_bad("Second message")
```

## آرگومان‌های طول متغیر

### *args - آرگومان‌های موقعیتی متغیر
```python
def sum_numbers(*numbers):
    """جمع هر تعداد آرگومان."""
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_numbers(1, 2, 3))           # 6
print(sum_numbers(10, 20, 30, 40))    # 100
print(sum_numbers())                  # 0

# باز کردن آرگومان‌ها
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = add(*numbers)  # معادل add(1, 2, 3)
print(result)  # 6
```

### **kwargs - آرگومان‌های کلیدی متغیر
```python
def create_config(**settings):
    """ایجاد تنظیمات از آرگومان‌های کلیدی."""
    config = {"debug": False, "timeout": 30}  # پیش‌فرض‌ها
    config.update(settings)  # بازنویسی با تنظیمات ارائه شده
    return config

config1 = create_config(host="localhost", port=8080)
config2 = create_config(debug=True, timeout=60, host="prod.example.com")

print(config1)  # {'debug': False, 'timeout': 30, 'host': 'localhost', 'port': 8080}
print(config2)  # {'debug': True, 'timeout': 60, 'host': 'prod.example.com'}
```

### ترکیب *args و **kwargs
```python
def flexible_function(required_arg, *args, default_param="default", **kwargs):
    """تابعی با همه انواع پارامتر."""
    print(f"مورد نیاز: {required_arg}")
    print(f"Args: {args}")
    print(f"پیش‌فرض: {default_param}")
    print(f"Kwargs: {kwargs}")

# سبک‌های فراخوانی مختلف
flexible_function("hello")
flexible_function("hello", 1, 2, 3)
flexible_function("hello", 1, 2, 3, default_param="changed")
flexible_function("hello", 1, 2, 3, extra="data", more="info")
```

## باز کردن آرگومان‌ها

### باز کردن لیست/تاپل
```python
def calculate_area(length, width):
    return length * width

# فراخوانی مستقیم
area1 = calculate_area(5, 3)

# باز کردن از دنباله
dimensions = [5, 3]
area2 = calculate_area(*dimensions)  # همان calculate_area(5, 3)

# باز کردن با آرگومان‌های اضافی
base_dimensions = [5, 3]
area3 = calculate_area(*base_dimensions)  # هنوز کار می‌کند
```

### باز کردن دیکشنری
```python
def configure_server(host, port, ssl=True, debug=False):
    return {
        "host": host,
        "port": port,
        "ssl": ssl,
        "debug": debug
    }

# باز کردن دیکشنری
config = {"host": "localhost", "port": 8080, "ssl": False}
server_config = configure_server(**config)

print(server_config)
# {'host': 'localhost', 'port': 8080, 'ssl': False, 'debug': False}
```

## اعتبار سنجی پارامتر و بررسی نوع

### اعتبار سنجی دستی
```python
def divide(a, b):
    """تقسیم دو عدد با اعتبار سنجی."""
    if not isinstance(a, (int, float)):
        raise TypeError("اولین آرگومان باید عدد باشد")
    if not isinstance(b, (int, float)):
        raise TypeError("دومین آرگومان باید عدد باشد")
    if b == 0:
        raise ValueError("نمی‌توان بر صفر تقسیم کرد")

    return a / b

try:
    result = divide(10, 2)
    print(f"نتیجه: {result}")
except (TypeError, ValueError) as e:
    print(f"خطا: {e}")
```

### استفاده از نکات نوع و اعتبار سنجی
```python
from typing import Union, Optional

def calculate_tax(income: Union[int, float], tax_rate: float = 0.2) -> float:
    """محاسبه مالیات با نکات نوع."""
    if not isinstance(income, (int, float)):
        raise TypeError("درآمد باید عدد باشد")
    if not isinstance(tax_rate, float):
        raise TypeError("نرخ مالیات باید float باشد")
    if income < 0:
        raise ValueError("درآمد نمی‌تواند منفی باشد")
    if not 0 <= tax_rate <= 1:
        raise ValueError("نرخ مالیات باید بین 0 و 1 باشد")

    return income * tax_rate

try:
    tax = calculate_tax(50000, 0.25)
    print(f"مالیات: ${tax}")
except (TypeError, ValueError) as e:
    print(f"خطا: {e}")
```

## الگوهای اضافه بار تابع

### رفتار مبتنی بر پارامتر
```python
def process_data(data, operation="sum"):
    """پردازش داده‌ها بر اساس پارامتر عملیات."""
    if operation == "sum":
        return sum(data)
    elif operation == "average":
        return sum(data) / len(data)
    elif operation == "max":
        return max(data)
    elif operation == "min":
        return min(data)
    else:
        raise ValueError(f"عملیات نامشخص: {operation}")

numbers = [1, 2, 3, 4, 5]
print(process_data(numbers, "sum"))      # 15
print(process_data(numbers, "average"))  # 3.0
print(process_data(numbers, "max"))      # 5
```

### انواع union و پارامترهای اختیاری
```python
from typing import List, Union

def format_output(data: Union[str, List[str]], separator: str = ", ") -> str:
    """قالب‌بندی خروجی به عنوان رشته."""
    if isinstance(data, str):
        return data
    elif isinstance(data, list):
        return separator.join(data)
    else:
        raise TypeError("داده باید رشته یا لیست رشته‌ها باشد")

print(format_output("Hello World"))              # "Hello World"
print(format_output(["apple", "banana", "cherry"]))  # "apple, banana, cherry"
print(format_output(["a", "b", "c"], " | "))     # "a | b | c"
```

## الگوهای پیشرفته پارامتر

### callbacks و پارامترهای تابع
```python
def apply_operation(data: List[int], operation) -> List[int]:
    """اعمال عملیات بر هر عنصر."""
    return [operation(x) for x in data]

def double(x):
    return x * 2

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
doubled = apply_operation(numbers, double)
squared = apply_operation(numbers, square)

print(doubled)  # [2, 4, 6, 8, 10]
print(squared)  # [1, 4, 9, 16, 25]

# استفاده از توابع lambda
tripled = apply_operation(numbers, lambda x: x * 3)
print(tripled)  # [3, 6, 9, 12, 15]
```

### توابع factory
```python
def create_multiplier(factor):
    """ایجاد تابعی که بر ضریب خاصی ضرب می‌کند."""
    def multiplier(number):
        return number * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)
quadruple = create_multiplier(4)

print(double(5))     # 10
print(triple(5))     # 15
print(quadruple(5))  # 20
```

### تزریق وابستگی پارامتر
```python
def create_api_client(api_key: str, base_url: str = "https://api.example.com"):
    """ایجاد کلاینت API با تنظیمات."""

    def make_request(endpoint: str, method: str = "GET", data: dict = None):
        """ایجاد درخواست API."""
        url = f"{base_url}/{endpoint}"
        headers = {"Authorization": f"Bearer {api_key}"}

        # شبیه‌سازی فراخوانی API
        return {
            "url": url,
            "method": method,
            "headers": headers,
            "data": data or {}
        }

    return make_request

# ایجاد کلاینت تنظیم شده
api_client = create_api_client("my-secret-key")

# استفاده از کلاینت
response1 = api_client("users")
response2 = api_client("posts", "POST", {"title": "New Post"})

print(response1["url"])  # "https://api.example.com/users"
print(response2["method"])  # "POST"
```

## بهترین روش‌ها برای پارامترهای تابع

### نام‌های پارامتر واضح
```python
# خوب - نام‌های توصیفی
def calculate_payment(principal: float, annual_rate: float, months: int) -> float:
    pass

# بد - اختصارهای نامشخص
def calc_pmt(p: float, r: float, m: int) -> float:
    pass
```

### ترتیب پارامترهای سازگار
```python
# خوب - ترتیب سازگار در توابع مرتبط
def save_user(name: str, email: str, password: str):
    pass

def update_user(user_id: int, name: str = None, email: str = None):
    pass

# بد - ترتیب ناسازگار
def save_user(name, password, email):  # email آخر
    pass

def update_user(name, user_id, email):  # email اول بعد از name
    pass
```

### اجتناب از پارامترهای بیش از حد
```python
# خوب - استفاده از ساختار داده برای پارامترهای مرتبط متعدد
def create_report(config: dict):
    """ایجاد گزارش با تنظیمات."""
    title = config.get("title", "Report")
    date_range = config.get("date_range")
    filters = config.get("filters", {})
    # ...

# بد - پارامترهای بیش از حد
def create_report(title, start_date, end_date, filter_by_status,
                  filter_by_type, include_charts, export_format):
    pass

# به جای آن از شی تنظیمات استفاده کنید
```

### مستندسازی پارامتر
```python
def process_payment(amount: float, currency: str = "USD",
                   description: str = "", metadata: dict = None) -> dict:
    """
    پردازش پرداخت.

    Args:
        amount: مبلغ پرداخت (باید مثبت باشد)
        currency: کد ارز سه حرفی (مثلاً 'USD', 'EUR')
        description: توضیح اختیاری پرداخت
        metadata: داده‌های اضافی اختیاری به صورت جفت کلید-مقدار

    Returns:
        دیکشنری با جزئیات پرداخت و وضعیت

    Raises:
        ValueError: اگر مبلغ مثبت نباشد یا ارز نامعتبر باشد
    """
    # پیاده‌سازی...
    pass
```

## استراتژی‌های تست پارامتر

### کلاس‌های هم ارزی
```python
def test_calculate_tax():
    """تست calculate_tax با کلاس‌های ورودی مختلف."""

    # ورودی‌های معتبر
    assert calculate_tax(50000, 0.2) == 10000
    assert calculate_tax(0, 0.2) == 0

    # مقادیر مرزی
    assert calculate_tax(0.01, 0.2) == 0.002

    # ورودی‌های نامعتبر (باید استثنا ایجاد کنند)
    try:
        calculate_tax(-1000, 0.2)
        assert False, "باید ValueError برای درآمد منفی ایجاد کند"
    except ValueError:
        pass

def calculate_tax(income: float, rate: float) -> float:
    """محاسبه مالیات."""
    if income < 0:
        raise ValueError("درآمد نمی‌تواند منفی باشد")
    if not 0 <= rate <= 1:
        raise ValueError("نرخ باید بین 0 و 1 باشد")
    return income * rate

test_calculate_tax()
print("همه تست‌ها گذرانده شدند!")
```

## نکات کلیدی

۱. **انواع پارامتر انعطاف‌پذیری فراهم می‌کنند** در نحوه فراخوانی توابع
۲. **مقادیر پیش‌فرض پارامترها را اختیاری می‌کنند** اما نیاز به مدیریت دقیق دارند
۳. **آرگومان‌های طول متغیر** (*args, **kwargs) ورودی‌های دلخواه را مدیریت می‌کنند
۴. **باز کردن آرگومان** اجازه می‌دهد مجموعه‌ها به عنوان آرگومان‌های جداگانه ارسال شوند
۵. **اعتبار سنجی پارامتر** قابلیت اطمینان تابع را تضمین می‌کند
۶. **نام‌گذاری واضح و مستندسازی** قابلیت نگهداری کد را بهبود می‌بخشند

## مطالعه بیشتر
- مکانیسم‌های ارسال پارامتر پایتون
- بهترین روش‌های type hinting
- الگوهای ترکیب تابع
- استراتژی‌های تست برای توابع پارامتری