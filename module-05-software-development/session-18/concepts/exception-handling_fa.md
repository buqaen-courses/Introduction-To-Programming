# مدیریت استثنا: مدیریت خطاها به طور优雅

## مقدمه‌ای بر استثناها

استثناها رویدادهایی هستند که در طول اجرای برنامه رخ می‌دهند و جریان عادی دستورات را مختل می‌کنند. پایتون از استثناها برای نشان دادن اینکه چیزی غیرمنتظره رخ داده استفاده می‌کند و به برنامه‌ها اجازه می‌دهد به طور مناسب پاسخ دهند به جای اینکه خراب شوند.

## مدیریت استثنا پایه

### بلوک try-except
```python
try:
    # کدی که ممکن است استثنا ایجاد کند
    result = 10 / 0
    print("این خط اجرا نخواهد شد")
except ZeroDivisionError:
    # کد برای مدیریت استثنا
    print("نمی‌توان بر صفر تقسیم کرد!")

print("برنامه پس از مدیریت استثنا ادامه می‌یابد")
```

### گرفتن استثناهای متعدد
```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "نمی‌توان بر صفر تقسیم کرد"
    except TypeError:
        return "هر دو آرگومان باید عدد باشند"
    except Exception as e:
        return f"خطای غیرمنتظره رخ داد: {e}"

print(safe_divide(10, 2))      # 5.0
print(safe_divide(10, 0))      # "نمی‌توان بر صفر تقسیم کرد"
print(safe_divide(10, "2"))    # "هر دو آرگومان باید عدد باشند"
```

### مدیریت استثنا عمومی
```python
try:
    # عملیات پرخطر
    with open("file.txt", "r") as f:
        data = f.read()
    result = int(data.strip())
except Exception as e:
    # گرفتن هر استثنایی
    print(f"خطایی رخ داد: {e}")
    result = None

print(f"نتیجه: {result}")
```

## سلسله مراتب استثنا

### انواع استثنای داخلی
```python
# استثناهای رایجی که با آنها مواجه خواهید شد:

# ValueError - مقدار نامعتبر برای عملیات
int("not_a_number")  # ValueError

# TypeError - عملیات بر روی انواع ناسازگار
"string" + 5         # TypeError

# KeyError - کلید دیکشنری یافت نشد
my_dict = {}
my_dict["missing"]   # KeyError

# IndexError - شاخص لیست خارج از محدوده
my_list = [1, 2, 3]
my_list[10]          # IndexError

# FileNotFoundError - فایل وجود ندارد
open("nonexistent.txt")  # FileNotFoundError

# ZeroDivisionError - تقسیم بر صفر
10 / 0               # ZeroDivisionError

# AttributeError - شی ویژگی ندارد
obj = "string"
obj.some_method()    # AttributeError
```

### استثناهای سفارشی
```python
class InsufficientFundsError(Exception):
    """وقتی حساب موجودی کافی ندارد ایجاد می‌شود."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"موجودی کافی نیست: موجودی ${balance}، نیاز ${amount}")

class InvalidAmountError(Exception):
    """وقتی مبلغ تراکنش نامعتبر است ایجاد می‌شود."""
    pass

def withdraw_money(account, amount):
    if amount <= 0:
        raise InvalidAmountError("مبلغ برداشت باید مثبت باشد")

    if amount > account.balance:
        raise InsufficientFundsError(account.balance, amount)

    account.balance -= amount
    return account.balance

# استفاده
account = type('Account', (), {'balance': 100})()

try:
    withdraw_money(account, 150)
except InsufficientFundsError as e:
    print(f"تراکنش ناموفق: {e}")
except InvalidAmountError as e:
    print(f"مبلغ نامعتبر: {e}")
```

## الگوهای مدیریت استثنا

### بلوک finally
```python
def read_file_with_cleanup(filename):
    file = None
    try:
        file = open(filename, "r")
        content = file.read()
        return content
    except FileNotFoundError:
        print(f"فایل {filename} یافت نشد")
        return None
    finally:
        # این همیشه اجرا می‌شود، حتی اگر استثنا رخ دهد
        if file:
            file.close()
            print("فایل بسته شد")

# رویکرد بهتر با استفاده از context manager
def read_file_context_manager(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"فایل {filename} یافت نشد")
        return None
    # فایل اینجا به طور خودکار بسته می‌شود
```

### بلوک else
```python
def process_data(data):
    try:
        # تلاش برای پردازش
        result = int(data)
    except ValueError:
        print("فرمت عدد نامعتبر")
        return None
    else:
        # فقط اگر استثنا رخ نداد اجرا می‌شود
        print(f"با موفقیت پردازش شد: {result}")
        return result * 2
    finally:
        # همیشه اجرا می‌شود
        print("پردازش کامل شد")

process_data("42")      # مسیر موفقیت
process_data("invalid") # مسیر خطا
```

### زنجیره کردن استثنا
```python
def process_user_data(raw_data):
    try:
        # تجزیه JSON
        import json
        data = json.loads(raw_data)

        # اعتبار سنجی فیلدهای مورد نیاز
        if "name" not in data:
            raise ValueError("فیلد مورد نیاز وجود ندارد: name")

        if "age" not in data:
            raise ValueError("فیلد مورد نیاز وجود ندارد: age")

        # اعتبار سنجی سن
        age = data["age"]
        if not isinstance(age, int) or age < 0:
            raise ValueError("سن باید عدد صحیح مثبت باشد")

        return data

    except json.JSONDecodeError as e:
        raise ValueError(f"فرمت JSON نامعتبر: {e}") from e
    except KeyError as e:
        raise ValueError(f"فیلد مورد نیاز وجود ندارد: {e}") from e
```

## مدیریت منابع و Context Managerها

### مدیریت منابع دستی
```python
def risky_file_operation(filename):
    file_handle = None
    try:
        file_handle = open(filename, "r")
        content = file_handle.read()
        # پردازش محتوا...
        return len(content)
    except FileNotFoundError:
        print(f"فایل {filename} یافت نشد")
        return 0
    except PermissionError:
        print(f"دسترسی برای {filename} رد شد")
        return 0
    finally:
        # اطمینان از بسته شدن فایل حتی اگر استثنا رخ دهد
        if file_handle:
            file_handle.close()
```

### الگوی Context Manager
```python
class DatabaseConnection:
    def __init__(self, config):
        self.config = config
        self.connection = None

    def __enter__(self):
        # راه‌اندازی - دریافت منبع
        self.connection = self._connect()
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        # پاک‌سازی - آزاد کردن منبع
        if self.connection:
            self.connection.close()

    def _connect(self):
        # شبیه‌سازی اتصال پایگاه داده
        print(f"اتصال به پایگاه داده: {self.config}")
        return "database_connection_object"

# استفاده
config = {"host": "localhost", "port": 5432}

try:
    with DatabaseConnection(config) as conn:
        # استفاده از اتصال
        print(f"استفاده از اتصال: {conn}")
        # انجام عملیات پایگاه داده...
except Exception as e:
    print(f"عملیات پایگاه داده ناموفق: {e}")
# اتصال اینجا به طور خودکار بسته می‌شود
```

### Context Managerهای داخلی
```python
# عملیات فایل
try:
    with open("data.txt", "r") as file:
        data = file.read()
        # پردازش داده‌ها...
except FileNotFoundError:
    print("فایل یافت نشد")

# منابع متعدد
try:
    with open("input.txt", "r") as input_file, \
         open("output.txt", "w") as output_file:

        for line in input_file:
            # پردازش خط
            processed = line.upper()
            output_file.write(processed)

except IOError as e:
    print(f"عملیات فایل ناموفق: {e}")
```

## بهترین روش‌های مدیریت استثنا

### انواع استثنای خاص
```python
# بد - همه چیز را می‌گیرد
try:
    risky_operation()
except Exception:
    print("چیزی اشتباه شد")

# خوب - استثناهای خاص را می‌گیرد
try:
    risky_operation()
except ValueError:
    print("مقدار نامعتبر ارائه شد")
except ConnectionError:
    print("اتصال شبکه ناموفق")
except Exception as e:
    print(f"خطای غیرمنتظره: {e}")
```

### اجتناب از بندهای except خالی
```python
# بد - خروج سیستم و وقفه کیبورد را می‌گیرد
try:
    do_something()
except:
    print("خطایی رخ داد")

# بهتر - خاص باشید
try:
    do_something()
except ValueError:
    handle_value_error()
except (IOError, OSError):
    handle_io_error()

# اگر باید همه چیز را بگیرید، صریح باشید
try:
    do_something()
except Exception:
    handle_general_error()
```

### حفظ اطلاعات استثنا
```python
# بد - استثنا اصلی را از دست می‌دهد
try:
    risky_call()
except ValueError:
    raise RuntimeError("چیزی ناموفق بود")

# خوب - استثناها را زنجیره می‌کند
try:
    risky_call()
except ValueError as e:
    raise RuntimeError("چیزی ناموفق بود") from e

# حتی بهتر - با زمینه دوباره ایجاد می‌کند
try:
    risky_call()
except ValueError as e:
    raise RuntimeError(f"چیزی در حین پردازش ناموفق بود: {e}") from e
```

### مدیریت منابع
```python
# بد - نشت منبع ممکن است
file = open("data.txt", "r")
try:
    data = file.read()
finally:
    file.close()  # اگر استثنا در try رخ دهد ممکن است اجرا نشود

# خوب - از context manager استفاده کنید
with open("data.txt", "r") as file:
    data = file.read()  # به طور خودکار بسته می‌شود
```

## سناریوهای خطای رایج و راه‌حل‌ها

### عملیات شبکه
```python
import requests
from requests.exceptions import RequestException, Timeout, ConnectionError

def fetch_user_data(user_id):
    try:
        response = requests.get(f"https://api.example.com/users/{user_id}", timeout=5)
        response.raise_for_status()  # برای کدهای خطای HTTP ایجاد می‌کند
        return response.json()
    except Timeout:
        print("درخواست timeout شد")
        return None
    except ConnectionError:
        print("اتصال شبکه ناموفق")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"خطای HTTP: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"درخواست ناموفق: {e}")
        return None
```

### عملیات پایگاه داده
```python
import sqlite3

def get_user_balance(user_id):
    try:
        conn = sqlite3.connect("bank.db")
        cursor = conn.cursor()

        cursor.execute("SELECT balance FROM accounts WHERE id = ?", (user_id,))
        result = cursor.fetchone()

        if result is None:
            raise ValueError(f"کاربر {user_id} یافت نشد")

        return result[0]

    except sqlite3.OperationalError as e:
        print(f"عملیات پایگاه داده ناموفق: {e}")
        raise
    except sqlite3.IntegrityError as e:
        print(f"خطای یکپارچگی داده: {e}")
        raise
    finally:
        if 'conn' in locals():
            conn.close()
```

### عملیات ریاضی
```python
def safe_calculate(expression):
    """بی‌خطر ارزیابی عبارت ریاضی."""
    try:
        # فقط عملیات امن اجازه داده می‌شود
        allowed_names = {
            "abs": abs, "round": round, "min": min, "max": max,
            "__builtins__": {}  # برای امنیت built-ins غیرفعال می‌شود
        }

        result = eval(expression, allowed_names)
        return result

    except ZeroDivisionError:
        return "تقسیم بر صفر"
    except NameError:
        return "نام تابع یا متغیر نامعتبر"
    except (TypeError, SyntaxError):
        return "نحو عبارت نامعتبر"
    except Exception as e:
        return f"خطای محاسبه: {e}"

print(safe_calculate("10 / 2"))        # 5.0
print(safe_calculate("10 / 0"))        # "تقسیم بر صفر"
print(safe_calculate("import os"))     # "نام تابع یا متغیر نامعتبر"
print(safe_calculate("10 + 'text'"))   # "نحو عبارت نامعتبر"
```

## تست مدیریت استثنا

### تست واحد استثناها
```python
import pytest

def test_safe_divide():
    """تست تابع safe_divide."""
    from my_module import safe_divide

    # موارد عادی
    assert safe_divide(10, 2) == 5.0
    assert safe_divide(10, 5) == 2.0

    # موارد خطا
    assert safe_divide(10, 0) == "نمی‌توان بر صفر تقسیم کرد"
    assert safe_divide("10", 2) == "هر دو آرگومان باید عدد باشند"

def test_exceptions_with_pytest():
    """تست اینکه استثناها به درستی ایجاد می‌شوند."""

    def risky_function(value):
        if value < 0:
            raise ValueError("مقدار باید غیرمنفی باشد")
        return value * 2

    # تست عملیات عادی
    assert risky_function(5) == 10

    # تست اینکه استثنا ایجاد می‌شود
    with pytest.raises(ValueError, match="باید غیرمنفی باشد"):
        risky_function(-1)
```

### تست یکپارچه‌سازی
```python
def test_file_processing_integration():
    """تست پردازش فایل با شرایط خطای مختلف."""
    import tempfile
    import os

    # تست با فایل معتبر
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        f.write("test data")
        temp_filename = f.name

    try:
        result = process_file(temp_filename)
        assert result is not None
    finally:
        os.unlink(temp_filename)

    # تست با فایل گم شده
    result = process_file("nonexistent_file.txt")
    assert result is None or isinstance(result, str)  # باید优雅 مدیریت کند
```

## ملاحظات عملکرد

### سربار مدیریت استثنا
```python
# استثناها هزینه عملکرد دارند - فقط برای موارد استثنایی استفاده کنید
def find_item(items, target):
    """یافتن آیتم در لیست."""
    try:
        return items.index(target)
    except ValueError:
        return -1

# برای عملیات مکرر، به جای آن از بررسی‌های شرطی استفاده کنید
def find_item_efficient(items, target):
    """یافتن آیتم در لیست به طور کارآمد."""
    for i, item in enumerate(items):
        if item == target:
            return i
    return -1
```

### ثبت در برابر ایجاد استثنا
```python
import logging

def process_data(data):
    """پردازش داده‌ها با مدیریت خطای مناسب."""
    try:
        # تلاش برای پردازش
        result = risky_operation(data)
        return result
    except ValueError as e:
        # ثبت و ادامه برای خطاهای قابل بازیابی
        logging.warning(f"اعتبار سنجی داده ناموفق: {e}")
        return get_default_value()
    except Exception as e:
        # دوباره ایجاد برای خطاهای جدی
        logging.error(f"خطای حیاتی در پردازش داده: {e}")
        raise
```

## نکات کلیدی

۱. **استثناها رویدادهای غیرمنتظره را مدیریت می‌کنند** بدون خراب کردن برنامه‌ها
۲. **انواع استثنای خاص** مدیریت خطای بهتری نسبت به گرفتن عمومی فراهم می‌کنند
۳. **بلوک‌های finally** اطمینان می‌دهند کد پاک‌سازی همیشه اجرا می‌شود
۴. **Context managerها** به طور خودکار پاک‌سازی منابع را مدیریت می‌کنند
۵. **استثناهای سفارشی** پیام‌های خطای معنادار فراهم می‌کنند
۶. **تست مدیریت استثنا** بازیابی خطای قوی را تضمین می‌کند

## مطالعه بیشتر
- مستندات سلسله مراتب استثنای پایتون
- پروتکل context manager
- بهترین روش‌های ثبت
- الگوهای مدیریت خطا در پارادایم‌های برنامه‌نویسی مختلف
- تکنیک‌های برنامه‌نویسی دفاعی