# تبدیل نوع: تغییر انواع داده در پایتون

## چرا تبدیل نوع؟

عملیات مختلف نیاز به انواع داده مختلف دارند. تبدیل نوع به شما اجازه می‌دهد مقدار را از یک نوع به نوع دیگر تغییر دهید و برنامه‌نویسی انعطاف‌پذیر را ممکن می‌سازد.

## تبدیل ضمنی در برابر صریح

### تبدیل ضمنی (خودکار)
پایتون به طور خودکار انواع را در موارد امن تبدیل می‌کند:
```python
# ارتقای عددی
result = 5 + 3.2  # 8.2 (int + float = float)

# زمینه‌های بولی
if []:           # لیست خالی → False
    print("هرگز اجرا نمی‌شود")

if [1, 2, 3]:    # لیست غیرخالی → True
    print("اجرا می‌شود")
```

### تبدیل صریح (دستی)
به طور صریح با استفاده از توابع داخلی تبدیل می‌کنید:
```python
# رشته به عدد
age = int("25")        # 25
price = float("19.99") # 19.99

# عدد به رشته
count = str(42)        # "42"

# تبدیل‌های مجموعه
numbers = list("123")  # ['1', '2', '3']
unique = set([1, 2, 2, 3])  # {1, 2, 3}
```

## تبدیل‌های عددی

### تبدیل‌های integer
```python
# از رشته
int("42")         # 42
int("1010", 2)    # 10 (رشته باینری)
int("2A", 16)     # 42 (رشته هگزادسیمال)
int("52", 8)      # 42 (رشته octal)

# از float
int(3.14)         # 3 (قطع می‌کند)
int(3.9)          # 3 (به سمت صفر قطع می‌کند)

# از boolean
int(True)         # 1
int(False)        # 0

# خطاها
# int("hello")   # ValueError
```

### تبدیل‌های float
```python
# از رشته
float("3.14")     # 3.14
float("42")       # 42.0
float("1e-3")     # 0.001 (نماد علمی)

# از integer
float(42)         # 42.0

# از boolean
float(True)       # 1.0
float(False)      # 0.0

# مقادیر ویژه
float("inf")      # inf
float("-inf")     # -inf
float("nan")      # nan
```

### تبدیل‌های complex
```python
# از اعداد
complex(2, 3)     # (2+3j)
complex(5)        # (5+0j)
complex(0, 1)     # 1j

# از رشته‌ها (محدود)
complex("2+3j")   # (2+3j)
# complex("2, 3") # کار نمی‌کند
```

## تبدیل‌های رشته

### از اعداد
```python
# integerها
str(42)           # "42"
str(-15)          # "-15"

# floatها
str(3.14)         # "3.14"
str(1e-6)         # "1e-06"

# booleanها
str(True)         # "True"
str(False)        # "False"
```

### از مجموعه‌ها
```python
# لیست‌ها
str([1, 2, 3])    # "[1, 2, 3]"

# تاپل‌ها
str((1, 2, 3))    # "(1, 2, 3)"

# دیکشنری‌ها
str({"a": 1, "b": 2})  # "{'a': 1, 'b': 2}"

# مجموعه‌ها
str({1, 2, 3})    # "{1, 2, 3}"
```

### قالب‌بندی رشته‌ها
```python
# f-stringها (پایتون ۳.۶+)
name = "Alice"
age = 25
message = f"نام من {name} است و {age} سال دارم."

# روش format()
message = "نام من {} است و {} سال دارم.".format(name, age)

# قالب‌بندی %
message = "نام من %s است و %d سال دارم." % (name, age)
```

## تبدیل‌های مجموعه

### تبدیل‌های لیست
```python
# از رشته
list("hello")     # ['h', 'e', 'l', 'l', 'o']

# از تاپل
list((1, 2, 3))   # [1, 2, 3]

# از مجموعه
list({1, 2, 3})   # [1, 2, 3] (ترتیب guarantee نیست)

# از range
list(range(5))    # [0, 1, 2, 3, 4]

# از دیکشنری
list({"a": 1, "b": 2})  # ['a', 'b'] (فقط کلیدها)
```

### تبدیل‌های تاپل
```python
# از لیست
tuple([1, 2, 3])  # (1, 2, 3)

# از رشته
tuple("hello")    # ('h', 'e', 'l', 'l', 'o')

# از range
tuple(range(3))   # (0, 1, 2)
```

### تبدیل‌های مجموعه
```python
# از لیست (تکراری‌ها را حذف می‌کند)
set([1, 2, 2, 3]) # {1, 2, 3}

# از تاپل
set((1, 2, 3))    # {1, 2, 3}

# از رشته
set("hello")      # {'h', 'e', 'l', 'o'} (بدون تکراری)
```

### تبدیل‌های دیکشنری
```python
# از لیست جفت‌ها
dict([("a", 1), ("b", 2)])  # {'a': 1, 'b': 2}

# از آرگومان‌های کلیدواژه
dict(a=1, b=2, c=3)  # {'a': 1, 'b': 2, 'c': 3}

# از zip
keys = ["a", "b", "c"]
values = [1, 2, 3]
dict(zip(keys, values))  # {'a': 1, 'b': 2, 'c': 3}
```

## تبدیل‌های بولی

### مقادیر Truthy/Falsy
```python
# اعداد
bool(0)        # False
bool(1)        # True
bool(-1)       # True
bool(3.14)     # True

# رشته‌ها
bool("")       # False (رشته خالی)
bool("hello")  # True

# مجموعه‌ها
bool([])       # False (لیست خالی)
bool([1, 2])   # True
bool({})       # False (دیکشنری خالی)
bool({"a": 1}) # True
bool(set())    # False (مجموعه خالی)

# None
bool(None)     # False
```

## تکنیک‌های تبدیل امن

### Try-Except برای مدیریت خطا
```python
def safe_int_conversion(value):
    """به طور امن مقدار را به integer تبدیل می‌کند."""
    try:
        return int(value)
    except ValueError:
        print(f"نمی‌توان '{value}' را به integer تبدیل کرد")
        return None
    except TypeError:
        print(f"نوع نامعتبر برای تبدیل: {type(value)}")
        return None

# استفاده
print(safe_int_conversion("42"))     # 42
print(safe_int_conversion("hello"))  # None
print(safe_int_conversion([1, 2]))   # None
```

### مقادیر پیش‌فرض
```python
def get_port(config):
    """شماره پورت را با پیش‌فرض دریافت می‌کند."""
    port = config.get("port", "8080")
    try:
        return int(port)
    except ValueError:
        print(f"پورت نامعتبر '{port}'، از پیش‌فرض استفاده می‌شود")
        return 8080

config = {"port": "invalid"}
port = get_port(config)  # 8080
```

### توابع اعتبارسنجی
```python
def is_valid_number(text):
    """بررسی می‌کند آیا text عدد معتبر را نمایش می‌دهد."""
    try:
        float(text)
        return True
    except ValueError:
        return False

def parse_number(text, default=0):
    """text را به عدد parse می‌کند با fallback."""
    try:
        return float(text)
    except ValueError:
        print(f"از مقدار پیش‌فرض استفاده می‌شود: {default}")
        return default
```

## الگوهای تبدیل پیشرفته

### توابع تبدیل سفارشی
```python
def str_to_bool(text):
    """رشته را به boolean با فرمت‌های مختلف تبدیل می‌کند."""
    text = text.lower().strip()
    if text in ("true", "yes", "1", "on"):
        return True
    elif text in ("false", "no", "0", "off"):
        return False
    else:
        raise ValueError(f"نمی‌توان '{text}' را به boolean تبدیل کرد")

# استفاده
print(str_to_bool("yes"))    # True
print(str_to_bool("no"))     # False
print(str_to_bool("maybe"))  # ValueError
```

### dispatcher نوع
```python
def convert_value(value, target_type):
    """مقدار را به نوع مشخص تبدیل می‌کند."""
    converters = {
        int: lambda x: int(float(x)) if isinstance(x, str) else int(x),
        float: float,
        str: str,
        bool: lambda x: bool(x) if not isinstance(x, str) else str_to_bool(x),
        list: lambda x: list(x) if hasattr(x, '__iter__') else [x],
    }

    converter = converters.get(target_type)
    if converter:
        return converter(value)
    else:
        raise ValueError(f"نوع پشتیبانی نشده: {target_type}")

# استفاده
print(convert_value("3.14", float))  # 3.14
print(convert_value("yes", bool))    # True
print(convert_value(42, str))        # "42"
```

### سریال‌سازی/د سریال‌سازی
```python
import json

# تبدیل اشیای پایتون به رشته‌های JSON
data = {"name": "Alice", "age": 25, "scores": [95, 87, 92]}
json_string = json.dumps(data)
# '{"name": "Alice", "age": 25, "scores": [95, 87, 92]}'

# تبدیل رشته‌های JSON به اشیای پایتون
parsed_data = json.loads(json_string)
# {'name': 'Alice', 'age': 25, 'scores': [95, 87, 92]}
```

## سناریوهای تبدیل رایج

### پردازش ورودی کاربر
```python
def get_user_info():
    """اطلاعات کاربر معتبر دریافت می‌کند."""
    name = input("Name: ").strip()
    if not name:
        raise ValueError("Name نمی‌تواند خالی باشد")

    try:
        age = int(input("Age: "))
        if age < 0 or age > 150:
            raise ValueError("Age باید بین 0 و 150 باشد")
    except ValueError as e:
        raise ValueError(f"Age نامعتبر: {e}")

    return {"name": name, "age": age}

user = get_user_info()
```

### پردازش فایل داده
```python
def parse_csv_line(line):
    """یک خط CSV را به انواع مناسب parse می‌کند."""
    parts = line.strip().split(',')
    try:
        name = parts[0].strip()
        age = int(parts[1].strip())
        score = float(parts[2].strip())
        active = parts[3].strip().lower() == 'true'
        return {"name": name, "age": age, "score": score, "active": active}
    except (IndexError, ValueError) as e:
        raise ValueError(f"خط CSV نامعتبر: {line}") from e

# استفاده
line = "Alice, 25, 95.5, true"
student = parse_csv_line(line)
```

### مدیریت داده API
```python
import requests

def fetch_user_data(user_id):
    """داده کاربر را از API دریافت می‌کند."""
    response = requests.get(f"https://api.example.com/users/{user_id}")
    data = response.json()

    # تبدیل رشته‌های API به انواع مناسب
    return {
        "id": int(data["id"]),
        "name": str(data["name"]),
        "age": int(data["age"]),
        "active": bool(data["active"]),
        "score": float(data["score"])
    }

user = fetch_user_data(123)
```

## نکات کلیدی

۱. **تبدیل نوع** کار با انواع داده مختلف را ممکن می‌سازد
۲. **تبدیل صریح** از توابع داخلی مانند `int()`، `str()`، `float()` استفاده می‌کند
۳. **تبدیل ضمنی** به طور خودکار در موارد امن اتفاق می‌افتد
۴. **مدیریت خطا** از خرابی‌های تبدیل‌های نامعتبر جلوگیری می‌کند
۵. **توابع تبدیل سفارشی** پردازش داده انعطاف‌پذیر فراهم می‌کنند

## مطالعه بیشتر
- مدل داده پایتون و سیستم نوع
- internationalization و تبدیل‌های خاص locale
- فرمت‌های سریال‌سازی پیشرفته (pickle، msgpack)
- نکات نوع و بررسی نوع static