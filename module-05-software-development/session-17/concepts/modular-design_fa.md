# طراحی مدولار: ساخت نرم‌افزار قابل نگهداری

## مقدمه‌ای بر برنامه‌نویسی مدولار

طراحی مدولار شامل تقسیم برنامه‌های بزرگ به ماژول‌های کوچک‌تر و مستقل است که می‌توانند به طور جداگانه توسعه، تست و نگهداری شوند. این رویکرد منجر به کد قابل نگهداری‌تر، قابل استفاده مجدد و قابل فهم‌تر می‌شود.

## توابع به عنوان ماژول‌ها

### اصل مسئولیت واحد
```python
# بد - یک تابع که کارهای متعدد انجام می‌دهد
def process_user_data(data):
    """این تابع کارها زیادی انجام می‌دهد."""
    # اعتبار سنجی داده‌ها
    # پاک‌سازی داده‌ها
    # ذخیره در پایگاه داده
    # ارسال اعلان
    # ثبت فعالیت
    pass

# خوب - توابع جداگانه برای هر مسئولیت
def validate_user_data(data):
    """اعتبار سنجی داده‌های ورودی کاربر."""
    pass

def clean_user_data(data):
    """پاک‌سازی و استانداردسازی داده‌های کاربر."""
    pass

def save_user_to_database(user):
    """ذخیره کاربر در پایگاه داده."""
    pass

def send_welcome_email(user):
    """ارسال ایمیل خوش‌آمدگویی به کاربر."""
    pass

def log_user_registration(user):
    """ثبت فعالیت ثبت‌نام کاربر."""
    pass

def register_user(data):
    """ثبت‌نام کاربر جدید - هماهنگ‌کننده فرآیند."""
    clean_data = clean_user_data(data)
    user = validate_user_data(clean_data)

    save_user_to_database(user)
    send_welcome_email(user)
    log_user_registration(user)

    return user
```

### ترکیب توابع
```python
def get_text_from_file(filename):
    """خواندن متن از فایل."""
    with open(filename, 'r') as f:
        return f.read()

def clean_text(text):
    """پاک‌سازی و استانداردسازی متن."""
    return text.lower().strip()

def extract_words(text):
    """استخراج کلمات از متن."""
    import re
    return re.findall(r'\b\w+\b', text)

def count_word_frequency(words):
    """شمارش فراوانی کلمات."""
    from collections import Counter
    return Counter(words)

def get_top_words(filename, n=10):
    """دریافت کلمات رایج از فایل."""
    text = get_text_from_file(filename)
    cleaned = clean_text(text)
    words = extract_words(cleaned)
    frequencies = count_word_frequency(words)

    return frequencies.most_common(n)

# استفاده
top_words = get_top_words("sample.txt", 5)
print(top_words)
```

## اصول سازماندهی کد

### جداسازی نگرانی‌ها
```python
# data_processing.py - مدیریت داده‌ها
def load_data(filename):
    """بارگذاری داده‌ها از فایل."""
    pass

def validate_data(data):
    """اعتبار سنجی یکپارچگی داده‌ها."""
    pass

def clean_data(data):
    """پاک‌سازی و پیش‌پردازش داده‌ها."""
    pass

# database.py - عملیات پایگاه داده
def connect_to_database(config):
    """برقراری اتصال پایگاه داده."""
    pass

def save_record(record, connection):
    """ذخیره رکورد در پایگاه داده."""
    pass

def query_records(query, connection):
    """پرس‌وجوی رکوردهای پایگاه داده."""
    pass

# email_service.py - عملکرد ایمیل
def send_email(to, subject, body):
    """ارسال پیام ایمیل."""
    pass

def create_welcome_email(user):
    """ایجاد محتوای ایمیل خوش‌آمدگویی."""
    pass

# main.py - منطق اصلی برنامه
def process_new_user(user_data):
    """پردازش ثبت‌نام کاربر جدید."""
    # بارگذاری و اعتبار سنجی داده‌ها
    data = load_data(user_data)
    if not validate_data(data):
        raise ValueError("داده‌های نامعتبر")

    # پاک‌سازی داده‌ها
    clean_user_data = clean_data(data)

    # ذخیره در پایگاه داده
    conn = connect_to_database(db_config)
    save_record(clean_user_data, conn)

    # ارسال ایمیل خوش‌آمدگویی
    welcome_email = create_welcome_email(clean_user_data)
    send_email(clean_user_data['email'], welcome_email['subject'], welcome_email['body'])
```

### سطوح انتزاع
```python
# توابع سطح پایین - پیاده‌سازی جزئی
def read_csv_file(filename):
    """خواندن فایل CSV و بازگشت ردیف‌ها."""
    with open(filename, 'r') as f:
        lines = f.readlines()
        # تجزیه فرمت CSV
        rows = []
        for line in lines:
            # تقسیم بر اساس کاما، مدیریت نقل قول‌ها و غیره
            row = parse_csv_line(line)
            rows.append(row)
        return rows

def parse_csv_line(line):
    """تجزیه یک خط CSV."""
    # مدیریت فیلدهای نقل قول شده، کاماهای فرار شده و غیره
    pass

def save_to_database(records, table_name):
    """ذخیره رکوردها در جدول پایگاه داده."""
    conn = get_database_connection()
    for record in records:
        # اجرای دستور INSERT
        # مدیریت تراکنش‌ها، بازیابی خطا و غیره
        pass

# توابع سطح بالا - منطق کسب‌وکار
def import_customer_data(csv_filename):
    """وارد کردن داده‌های مشتری از CSV."""
    records = read_csv_file(csv_filename)
    validated_records = validate_customer_records(records)
    save_to_database(validated_records, "customers")
    send_import_notification(len(validated_records))

def validate_customer_records(records):
    """اعتبار سنجی داده‌های مشتری."""
    # اعتبار سنجی قوانین کسب‌وکار
    pass

def send_import_notification(count):
    """ارسال اعلان درباره تکمیل وارد کردن."""
    pass
```

## رابط‌های تابع و قراردادها

### قراردادهای تابع واضح
```python
def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    محاسبه شاخص توده بدنی.

    Args:
        weight_kg: وزن به کیلوگرم (باید > 0 باشد)
        height_m: قد به متر (باید > 0 باشد)

    Returns:
        مقدار BMI به عنوان float

    Raises:
        ValueError: اگر وزن یا قد مثبت نباشند
        TypeError: اگر ورودی‌ها عدد نباشند

    Example:
        >>> calculate_bmi(70, 1.75)
        22.857142857142858
    """
    if not isinstance(weight_kg, (int, float)) or not isinstance(height_m, (int, float)):
        raise TypeError("وزن و قد باید عدد باشند")

    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("وزن و قد باید مثبت باشند")

    return weight_kg / (height_m ** 2)
```

### مدیریت خطای سازگار
```python
class DataProcessingError(Exception):
    """استثنا سفارشی برای خطاهای پردازش داده‌ها."""
    pass

def process_financial_data(data):
    """پردازش داده‌های مالی با مدیریت خطای سازگار."""
    try:
        validated_data = validate_financial_data(data)
        processed_data = calculate_financial_metrics(validated_data)
        save_processed_data(processed_data)
        return processed_data
    except ValueError as e:
        raise DataProcessingError(f"داده‌های مالی نامعتبر: {e}")
    except ConnectionError as e:
        raise DataProcessingError(f"اتصال پایگاه داده ناموفق: {e}")
    except Exception as e:
        raise DataProcessingError(f"خطای غیرمنتظره: {e}")

def validate_financial_data(data):
    """اعتبار سنجی داده‌های مالی."""
    # منطق اعتبار سنجی
    pass

def calculate_financial_metrics(data):
    """محاسبه معیارهای مالی."""
    # منطق محاسبه
    pass

def save_processed_data(data):
    """ذخیره داده‌های پردازش شده."""
    # منطق ذخیره
    pass
```

## مدیریت وابستگی‌ها

### اتصال آزاد
```python
# اتصال محکم - سخت برای تست و نگهداری
class EmailService:
    def send_notification(self, user):
        # وابستگی مستقیم به پایگاه داده
        db = DatabaseConnection()
        user_data = db.get_user(user.id)
        email_content = self.create_email_content(user_data)

        # وابستگی مستقیم به سرویس ایمیل
        smtp = SMTPClient()
        smtp.send(user.email, email_content)

# اتصال آزاد - وابستگی‌ها تزریق می‌شوند
class NotificationService:
    def __init__(self, database, email_client):
        self.database = database
        self.email_client = email_client

    def send_notification(self, user_id):
        user_data = self.database.get_user(user_id)
        email_content = self.create_email_content(user_data)
        self.email_client.send(user_data['email'], email_content)
```

### تزریق وابستگی
```python
# تنظیمات و راه‌اندازی وابستگی‌ها
def create_app(config):
    """ایجاد برنامه با وابستگی‌ها."""
    database = DatabaseConnection(config['database_url'])
    email_client = SMTPClient(config['smtp_settings'])
    cache = RedisCache(config['redis_url'])

    # تزریق وابستگی‌ها
    user_service = UserService(database, email_client, cache)
    notification_service = NotificationService(database, email_client)

    return {
        'user_service': user_service,
        'notification_service': notification_service
    }

# استفاده در تست‌ها
def test_user_registration():
    # ایجاد وابستگی‌های mock
    mock_db = MockDatabase()
    mock_email = MockEmailClient()
    mock_cache = MockCache()

    # تزریق mockها برای تست
    user_service = UserService(mock_db, mock_email, mock_cache)

    # تست سرویس
    user = user_service.register_user(test_data)
    assert user.email == test_data['email']
```

## تست کد مدولار

### تست واحد توابع
```python
import pytest
from my_module import calculate_bmi, process_financial_data

def test_calculate_bmi():
    """تست محاسبه BMI."""
    # موارد عادی
    assert calculate_bmi(70, 1.75) == pytest.approx(22.857, rel=1e-3)
    assert calculate_bmi(50, 1.60) == pytest.approx(19.531, rel=1e-3)

    # موارد مرزی
    assert calculate_bmi(1, 1) == 1.0

def test_calculate_bmi_errors():
    """تست مدیریت خطای محاسبه BMI."""
    with pytest.raises(ValueError):
        calculate_bmi(-70, 1.75)

    with pytest.raises(ValueError):
        calculate_bmi(70, -1.75)

    with pytest.raises(TypeError):
        calculate_bmi("70", 1.75)

def test_process_financial_data():
    """تست پردازش داده‌های مالی."""
    test_data = {
        'transactions': [100, 200, 300],
        'currency': 'USD'
    }

    result = process_financial_data(test_data)

    assert 'total' in result
    assert 'average' in result
    assert result['total'] == 600
    assert result['average'] == 200
```

### mocking وابستگی‌ها
```python
from unittest.mock import Mock, patch

def test_notification_service():
    """تست سرویس اعلان با وابستگی‌های mock."""
    # ایجاد mockها
    mock_db = Mock()
    mock_db.get_user.return_value = {'email': 'test@example.com', 'name': 'Test User'}

    mock_email = Mock()
    mock_email.send.return_value = True

    # ایجاد سرویس با mockها
    service = NotificationService(mock_db, mock_email)

    # تست متد
    result = service.send_notification(123)

    # تایید تعاملات
    mock_db.get_user.assert_called_once_with(123)
    mock_email.send.assert_called_once()

    assert result is True
```

## قابلیت استفاده مجدد کد و کتابخانه‌ها

### ایجاد توابع قابل استفاده مجدد
```python
def retry_operation(operation, max_attempts=3, delay=1):
    """امتحان مجدد عملیات با backoff نمایی."""
    import time

    for attempt in range(max_attempts):
        try:
            return operation()
        except Exception as e:
            if attempt == max_attempts - 1:
                raise e
            time.sleep(delay * (2 ** attempt))  # backoff نمایی

def safe_file_operation(filename, operation):
    """انجام عملیات فایل با مدیریت خطا."""
    try:
        with open(filename, 'r') as f:
            return operation(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"فایل یافت نشد: {filename}")
    except PermissionError:
        raise PermissionError(f"دسترسی رد شد: {filename}")
    except Exception as e:
        raise Exception(f"خطا در پردازش فایل {filename}: {e}")

# استفاده
def count_lines(file_obj):
    return len(file_obj.readlines())

line_count = safe_file_operation("data.txt", count_lines)
```

### کارخانه توابع
```python
def create_validator(rules):
    """ایجاد تابع اعتبار سنجی از قوانین."""
    def validator(data):
        errors = []
        for rule_name, rule_func in rules.items():
            if not rule_func(data):
                errors.append(f"شکست در {rule_name}")
        return errors if errors else None
    return validator

# تعریف قوانین اعتبار سنجی
user_rules = {
    'email_format': lambda d: '@' in d.get('email', ''),
    'age_range': lambda d: 13 <= d.get('age', 0) <= 120,
    'name_present': lambda d: bool(d.get('name', '').strip())
}

# ایجاد اعتبار سنجی
validate_user = create_validator(user_rules)

# استفاده از اعتبار سنجی
user_data = {'name': 'Alice', 'email': 'alice@example.com', 'age': 25}
errors = validate_user(user_data)
print(errors)  # None (بدون خطا)

invalid_data = {'name': '', 'email': 'invalid', 'age': 10}
errors = validate_user(invalid_data)
print(errors)  # ['Failed email_format', 'Failed age_range', 'Failed name_present']
```

## مستندسازی و کامنت‌های کد

### مستندسازی ماژول
```python
"""
ماژول پردازش داده‌ها

این ماژول توابعی برای پردازش انواع مختلف داده‌ها
از جمله متن، اعداد و فرمت‌های داده‌های ساختار یافته فراهم می‌کند.

کلاس‌ها:
    DataProcessor: کلاس اصلی برای عملیات پردازش داده‌ها

توابع:
    clean_text: پاک‌سازی و استانداردسازی داده‌های متنی
    validate_data: اعتبار سنجی داده‌ها در برابر schema
    transform_data: اعمال تبدیل‌ها به داده‌ها

مثال‌ها:
    >>> processor = DataProcessor()
    >>> clean_data = processor.process(raw_data)
"""

class DataProcessor:
    """کلاس اصلی پردازش داده‌ها."""

    def __init__(self, config=None):
        """راه‌اندازی پردازنده با تنظیمات."""
        self.config = config or {}

    def process(self, data):
        """پردازش داده‌های ورودی."""
        cleaned = self.clean_data(data)
        validated = self.validate_data(cleaned)
        transformed = self.transform_data(validated)
        return transformed

    def clean_data(self, data):
        """پاک‌سازی داده‌های ورودی."""
        # پیاده‌سازی
        pass

    def validate_data(self, data):
        """اعتبار سنجی یکپارچگی داده‌ها."""
        # پیاده‌سازی
        pass

    def transform_data(self, data):
        """تبدیل داده‌ها طبق قوانین."""
        # پیاده‌سازی
        pass
```

### کامنت‌های درون خطی و مستندسازی
```python
def complex_calculation(data, parameters):
    """
    انجام محاسبه پیچیده بر روی داده‌ها.

    این تابع چندین تبدیل و محاسبه را بر اساس پارامترهای ارائه شده
    به داده‌های ورودی اعمال می‌کند.
    """
    # مرحله ۱: اعتبار سنجی داده‌های ورودی
    if not self.validate_input(data):
        raise ValueError("داده‌های ورودی نامعتبر")

    # مرحله ۲: اعمال تبدیل‌های پیش‌پردازش
    preprocessed = self.preprocess_data(data, parameters.get('preprocessing', {}))

    # مرحله ۳: انجام محاسبه اصلی
    # این الگوریتم اصلی است که داده‌ها را پردازش می‌کند
    result = self.perform_calculation(preprocessed, parameters)

    # مرحله ۴: اعمال پس‌پردازش اگر درخواست شده
    if parameters.get('post_processing', False):
        result = self.post_process_result(result, parameters)

    # مرحله ۵: اعتبار سنجی نتیجه نهایی
    self.validate_result(result)

    return result
```

## ملاحظات عملکرد

### سربار فراخوانی تابع
```python
# برای کد حیاتی عملکرد، در نظر گرفتن inline کردن توابع کوچک
def is_even(number):
    return number % 2 == 0

# در حلقه حیاتی عملکرد
even_numbers = []
for num in large_list:
    if num % 2 == 0:  # بررسی inline
        even_numbers.append(num)

# یا استفاده از list comprehension برای عملکرد بهتر
even_numbers = [num for num in large_list if num % 2 == 0]
```

### استفاده از حافظه در کد مدولار
```python
# اجتناب از ایجاد ساختارهای داده میانی بزرگ
def process_large_file(filename):
    """پردازش فایل بزرگ به طور کارآمد."""
    results = []

    with open(filename, 'r') as f:
        for line in f:
            # پردازش خط فوراً، انباشته کردن لیست‌های بزرگ نکن
            processed_line = process_single_line(line)
            if meets_criteria(processed_line):
                results.append(processed_line)

    return results

# بهتر - استفاده از generatorها برای کارآمد بودن حافظه
def process_large_file_generator(filename):
    """پردازش فایل بزرگ با generator."""
    with open(filename, 'r') as f:
        for line in f:
            processed_line = process_single_line(line)
            if meets_criteria(processed_line):
                yield processed_line
```

## نکات کلیدی

۱. **طراحی مدولار مشکلات پیچیده را** به قطعات قابل مدیریت تقسیم می‌کند
۲. **اصل مسئولیت واحد** توابع را متمرکز نگه می‌دارد
۳. **رابط‌ها و قراردادهای واضح** قابلیت نگهداری را بهبود می‌بخشند
۴. **تزریق وابستگی** امکان تست و انعطاف را فراهم می‌کند
۵. **تست جامع** قابلیت اطمینان ماژول را تضمین می‌کند
۶. **مستندسازی خوب** امکان استفاده مجدد و نگهداری کد را فراهم می‌کند

## مطالعه بیشتر
- اصول SOLID طراحی شی‌گرا
- الگوهای طراحی برای نرم‌افزار مدولار
- روش‌های توسعه تست‌محور
- تکنیک‌های refactoring برای کد قدیمی
- اصول معماری میکروسرویس‌ها