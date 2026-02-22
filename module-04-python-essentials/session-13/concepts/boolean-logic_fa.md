# منطق بولی در پایتون

## آنچه خواهید آموخت
- چگونه کامپیوتر "درست" و "نادرست" را درک می‌کند
- نحوه ترکیب شرایط چندگانه
- چگونه تصمیمات پیچیده بگیرید

---

## منطق بولی چیست؟

**منطق بولی** سیستمی از استدلال است که فقط دو مقدار دارد:
- **True** (درست، بله، ۱)
- **False** (نادرست، خیر، ۰)

این سیستم به نام جورج بول، ریاضیدان قرن نوزدهم، نام‌گذاری شده است.

### چرا مهم است؟

کامپیوترها با **سوییچ‌های روشن/خاموش** کار می‌کنند. منطق بولی به ما اجازه می‌دهد:
- تصمیم بگیریم ("آیا کاربر وارد شده است؟")
- شرایط را ترکیب کنیم ("آیا سن بالای ۱۸ است و گواهینامه دارد؟")
- فیلتر کنیم ("آیا این محصول موجود و قیمت آن زیر ۵۰ است؟")

---

## مقادیر بولی در پایتون

### نوع داده bool

```python
# دو مقدار ممکن
is_active = True
is_closed = False

print(type(is_active))   # <class 'bool'>
print(is_active)         # True
print(is_closed)        # False
```

### تبدیل به بولی

```python
# اعداد: ۰ False، بقیه True
print(bool(0))           # False
print(bool(42))          # True
print(bool(-5))          # True
print(bool(0.0))         # False
print(bool(0.001))       # True

# رشته‌ها: خالی False، غیرخالی True
print(bool(""))          # False
print(bool("Hello"))     # True
print(bool(" "))          # True (حتی یک فاصله هم True است!)

# مجموعه‌ها: خالی False، غیرخالی True
print(bool([]))          # False
print(bool([1, 2, 3]))   # True
print(bool({}))          # False
print(bool({"a": 1}))    # True
print(bool(None))        # False
```

### قاعده کلی

**صفر، خالی، یا None** → `False`
**هر چیز دیگر** → `True`

---

## عملگرهای منطقی

### and (و)

هر دو باید True باشند تا نتیجه True شود.

| A | B | A and B |
|---|---|---------|
| True | True | **True** |
| True | False | False |
| False | True | False |
| False | False | False |

```python
# مثال‌های واقعی
has_ticket = True
is_adult = True
can_enter = has_ticket and is_adult
print(can_enter)         # True

# اگر یکی False باشد
has_ticket = True
is_adult = False
can_enter = has_ticket and is_adult
print(can_enter)         # False
```

### or (یا)

حداقل یکی باید True باشد تا نتیجه True شود.

| A | B | A or B |
|---|---|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | **False** |

```python
# مثال‌های واقعی
is_weekend = True
is_holiday = False
can_relax = is_weekend or is_holiday
print(can_relax)         # True

# اگر هر دو False باشند
is_weekend = False
is_holiday = False
can_relax = is_weekend or is_holiday
print(can_relax)         # False
```

### not (نقیض)

مقدار را معکوس می‌کند.

| A | not A |
|---|-------|
| True | **False** |
| False | **True** |

```python
# مثال‌های واقعی
is_raining = True
is_sunny = not is_raining
print(is_sunny)          # False

is_logged_in = False
is_guest = not is_logged_in
print(is_guest)          # True
```

---

## ترکیب عملگرهای منطقی

### ترتیب اولویت

1. `not` (اول)
2. `and` (دوم)
3. `or` (آخر)

```python
# بدون پرانتز
result = True or False and False
# ابتدا: False and False = False
# سپس: True or False = True
print(result)            # True

# با پرانتز برای وضوح
result = True or (False and False)  # معادل بالا

# اگر می‌خواستید ترتیب دیگری
result = (True or False) and False  # False
```

### مثال‌های پیچیده

```python
# بررسی وضعیت رانندگی
has_license = True
age = 25
is_sober = True

can_drive = has_license and (age >= 18) and is_sober
print(can_drive)         # True

# بررسی تخفیف
is_member = True
is_senior = False
is_student = True

gets_discount = is_member or is_senior or is_student
print(gets_discount)     # True

# بررسی پیچیده‌تر
has_ticket = True
is_vip = False
is_staff = True

can_enter = has_ticket and (is_vip or is_staff)
print(can_enter)         # True (چون is_staff True است)
```

---

## ارزیابی کوتاه

پایتون "ارزیابی کوتاه" می‌کند - به محض اینکه نتیجه مشخص شود، متوقف می‌شود.

### and با ارزیابی کوتاه

```python
# اگر اولین False باشد، دومی بررسی نمی‌شود
result = False and expensive_function()
# expensive_function() اصلاً صدا زده نمی‌شود!
print(result)            # False

# اگر اولین True باشد، دومی بررسی می‌شود
result = True and expensive_function()
# expensive_function() صدا زده می‌شود
```

### or با ارزیابی کوتاه

```python
# اگر اولین True باشد، دومی بررسی نمی‌شود
result = True or expensive_function()
# expensive_function() اصلاً صدا زده نمی‌شود!
print(result)            # True

# اگر اولین False باشد، دومی بررسی می‌شود
result = False or expensive_function()
# expensive_function() صدا زده می‌شود
```

---

## مقایسه‌ها و منطق بولی

### ترکیب مقایسه‌ها

```python
age = 25
score = 85

# سن بین ۱۸ و ۶۵ است
is_adult = 18 <= age <= 65
print(is_adult)          # True

# نمره عالی است
is_excellent = score >= 90
print(is_excellent)      # False

# هم بزرگسال و هم نمره خوب
is_qualified = is_adult and (score >= 80)
print(is_qualified)      # True
```

### زنجیره‌سازی مقایسه‌ها

```python
x = 10

# روش خوانا
if 5 < x < 15:
    print("x is between 5 and 15")

# معادل با and
if x > 5 and x < 15:
    print("x is between 5 and 15")
```

---

## کاربردهای عملی

### مثال ۱: صفحه ورود

```python
username = "alice"
password = "secret123"
is_active = True

# بررسی ورود
if username and password and is_active:
    print("Login successful!")
else:
    print("Login failed!")
```

### مثال ۲: بررسی سفارش

```python
has_items = True
is_paid = True
is_in_stock = True

# آیا سفارش قابل پردازش است؟
can_process = has_items and is_paid and is_in_stock
print(f"Can process: {can_process}")

# آیا نیاز به اطلاع‌رسانی است؟
needs_attention = not is_paid or not is_in_stock
print(f"Needs attention: {needs_attention}")
```

### مثال ۳: تخفیف فروشگاه

```python
is_member = True
total_purchase = 120

# تخفیف اگر عضو باشد و خرید بالای ۱۰۰ باشد
gets_discount = is_member and (total_purchase > 100)
print(f"Gets discount: {gets_discount}")

# یا اگر خرید بالای ۲۰۰ باشد (صرف‌نظر از عضویت)
gets_discount = (is_member and total_purchase > 100) or (total_purchase > 200)
print(f"Gets discount: {gets_discount}")
```

---

## اشتباهات رایج

### اشتباه ۱: استفاده از & و | به جای and و or

```python
# ❌ اشتباه - این عملگرهای بیتی هستند
result = True & False    # کار می‌کند اما اشتباه است
result = True | False    # کار می‌کند اما اشتباه است

# ✅ صحیح
result = True and False
result = True or False
```

### اشتباه ۲: مقایسه بولی‌ها

```python
# ❌ غیرضروری
if is_active == True:    # درست است اما اضافی

# ✅ صحیح
if is_active:            # خود is_active True یا False است

# ❌ برای False
if is_active == False:   # اضافی

# ✅ صحیح
if not is_active:
```

### اشتباه ۳: and/or اشتباهی در شرایط

```python
# ❌ اشتباه رایج
if age > 18 and < 65:    # SyntaxError!

# ✅ صحیح
if age > 18 and age < 65:

# ✅ حتی بهتر
if 18 < age < 65:
```

### اشتباه ۴: اولویت اشتباه

```python
# ❌ ممکن است غافلگیرکننده باشد
result = True or False and False
# این True است (چون and اول انجام می‌شود)

# ✅ با پرانتز واضح‌تر
result = True or (False and False)  # True
# یا
result = (True or False) and False  # False
```

### اشتباه ۵: فراموش کردن ارزیابی کوتاه

```python
# ⚠️ ممکن است غیرمنتظره باشد
x = 0
result = x and (10 / x)  # با x=0، تقسیم اجرا نمی‌شود!
# اما اگر x=5 باشد، 10/5 = 2.0

# ✅ بررسی صریح
if x != 0:
    result = 10 / x
```

---

## خودتان امتحان کنید: تمرین‌ها

### تمرین ۱: جدول درستی

جدول درستی این عبارات را بنویسید:

```python
A = True
B = False

# نتیجه هر کدام چیست؟
A and B
A or B
not A
not B
not (A and B)
not A or not B
A and not B
```

### تمرین ۲: شرایط واقعی

```python
# این شرایط را بنویسید:

# ۱. کاربر می‌تواند وارد شود اگر:
#    - نام کاربری و رمز داشته باشد
#    - حساب فعال باشد
#    - از ۳ تلاش بیشتر نشده باشد

# ۲. یک بازی باید تمام شود اگر:
#    - زمان تمام شده باشد
#    - یا امتیاز به حداکثر رسیده باشد
#    - یا بازیکن باخته باشد

# ۳. تخفیف اعمال می‌شود اگر:
#    - عضو باشد و بیش از ۵۰ خرید کرده باشد
#    - یا عضو VIP باشد
```

### تمرین ۳: تبدیل به کد

این شرایط را به عبارات بولی تبدیل کنید:

```
۱. "کاربر باید حداقل ۱۸ سال داشته باشد و گواهینامه معتبر داشته باشد"

۲. "فایل باید وجود داشته باشد و خواندنی باشد و خالی نباشد"

۳. "سیستم باید در حالت تعمیر نباشد یا کاربر ادمین باشد"

۴. "محصول باید موجود باشد و (قیمت زیر ۱۰۰ یا تخفیف داشته باشد)"
```

### تمرین ۴: اشکال‌زدایی

این کدها مشکل دارند - آنها را اصلاح کنید:

```python
# ۱
if age > 18 and < 65:
    print("Adult")

# ۲
if is_valid = True:        # اشتباه تایپی!
    print("Valid")

# ۳
result = True and False or True
# آیا نتیجه مورد نظر شماست؟ با پرانتز واضح‌تر کنید.
```

---

## مرجع سریع

### مقادیر بولی

```python
True    # مقدار درست
False   # مقدار نادرست
```

### عملگرهای منطقی

```python
A and B    # True فقط اگر هر دو True باشند
A or B     # True اگر حداقل یکی True باشد
not A      # معکوس A
```

### تبدیل به بولی

```python
bool(0)        # False
bool(42)       # True
bool("")       # False
bool("Hello")  # True
bool([])       # False
bool([1, 2])   # True
```

### الگوهای رایج

```python
# بررسی وجود
if name:                   # اگر name خالی نباشد

# بررسی فهرست
if items:                  # اگر items خالی نباشد

# بررسی None
if value is not None:

# بررسی مثبت
if count > 0:
```

---

## نکات کلیدی

۱. **منطق بولی** فقط دو مقدار دارد: `True` و `False`
۲. **and** هر دو باید True باشند، **or** حداقل یکی، **not** معکوس می‌کند
۳. **ترتیب:** not → and → or
۴. **ارزیابی کوتاه:** به محض مشخص شدن نتیجه، متوقف می‌شود
۵. **مقایسه زنجیره‌ای:** `18 <= age <= 65` خواناتر از `age >= 18 and age <= 65`

---

## گام بعدی چیست؟

حالا که با منطق بولی آشنا شدید، بیایید درباره جملات شرطی یاد بگیریم:
- **جملات شرطی** - اجرای کد بر اساس شرایط
