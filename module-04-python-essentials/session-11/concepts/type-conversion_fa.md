# تبدیل انواع داده در پایتون

## آنچه خواهید آموخت
- چگونه یک نوع داده را به نوع دیگر تبدیل کنید
- چه زمانی تبدیل لازم است
- اشتباهات رایج و نحوه جلوگیری از آنها

---

## تبدیل انواع داده چیست؟

گاهی اوقات، شما یک داده با یک نوع دارید اما باید به نوع دیگری تبدیلش کنید. این مثل تبدیل یک مقدار از یک واحد به واحد دیگر است.

### تشبیه: تبدیل واحد

```
۱۰۰ سانتی‌متر → ۱ متر
۶۰ دقیقه → ۱ ساعت
"۱۰۰" (متن) → ۱۰۰ (عدد)
```

در برنامه‌نویسی، معمولاً این تبدیلها را انجام می‌دهیم:
- **رشته به عدد** - وقتی کاربر ورودی عددی می‌دهد
- **عدد به رشته** - وقتی می‌خواهیم عدد را نمایش دهیم
- **انواع مجموعه** - وقتی نیاز به تغییر قالب داریم

---

## توابع تبدیل اصلی

پایتون توابع داخلی برای تبدیل انواع داده دارد:

| تابع | چه تبدیلی انجام می‌دهد | مثال |
|--------|------------------|--------|
| `int()` | به عدد صحیح | `int("42")` → `42` |
| `float()` | به عدد اعشاری | `float("3.14")` → `3.14` |
| `str()` | به رشته | `str(42)` → `"42"` |
| `bool()` | به بولی | `bool(1)` → `True` |
| `list()` | به لیست | `list("abc")` → `['a','b','c']` |
| `tuple()` | به تاپل | `tuple([1,2,3])` → `(1,2,3)` |
| `set()` | به مجموعه | `set([1,1,2])` → `{1,2}` |
| `dict()` | به دیکشنری | `dict([("a",1)])` → `{"a":1}` |

---

## تبدیل عددی

### به عدد صحیح (int)

```python
# از رشته
number = int("42")
print(number)            # 42
print(type(number))      # <class 'int'>

# از اعشار (اعشار حذف می‌شود!)
whole = int(3.99)
print(whole)             # 3

# از بولی
flag = int(True)
print(flag)              # 1 (False می‌شود 0)
```

**هشدار:** `int()` همیشه به سمت صفر گرد می‌کند!

```python
print(int(3.9))          # 3 (نه 4!)
print(int(-3.9))         # -3 (نه -4!)
```

### به عدد اعشاری (float)

```python
# از رشته
decimal = float("3.14")
print(decimal)           # 3.14

# از عدد صحیح
pi = float(3)
print(pi)                # 3.0

# از بولی
flag = float(True)
print(flag)              # 1.0
```

---

## تبدیل رشته‌ای

### به رشته (str)

```python
# هر نوع داده‌ای می‌تواند به رشته تبدیل شود
text1 = str(42)          # "42"
text2 = str(3.14)        # "3.14"
text3 = str(True)        # "True"
text4 = str([1, 2, 3])   # "[1, 2, 3]"

print(text1, text2, text3, text4)
```

### استفاده معمول: پیوند رشته و عدد

```python
# ❌ این خطا می‌دهد
age = 25
message = "I am " + age + " years old"  # TypeError!

# ✅ تبدیل به رشته
message = "I am " + str(age) + " years old"
print(message)           # I am 25 years old

# ✅ یا از f-string استفاده کنید (بهتر!)
message = f"I am {age} years old"
print(message)
```

---

## تبدیل مجموعه

### به لیست (list)

```python
# از رشته (هر کاراکتر یک عنصر می‌شود)
chars = list("Hello")
print(chars)             # ['H', 'e', 'l', 'l', 'o']

# از تاپل
my_list = list((1, 2, 3))
print(my_list)           # [1, 2, 3]

# از مجموعه
my_list = list({1, 2, 3})
print(my_list)           # [1, 2, 3]

# از دیکشنری (فقط کلیدها)
keys = list({"a": 1, "b": 2})
print(keys)              # ['a', 'b']
```

### به تاپل (tuple)

```python
# از لیست
my_tuple = tuple([1, 2, 3])
print(my_tuple)          # (1, 2, 3)

# از رشته
chars = tuple("abc")
print(chars)             # ('a', 'b', 'c')
```

### به مجموعه (set)

```python
# از لیست (تکرارها حذف می‌شوند)
unique = set([1, 2, 2, 3, 3, 3])
print(unique)            # {1, 2, 3}

# از رشته
chars = set("hello")
print(chars)             # {'h', 'e', 'l', 'o'}
```

### به دیکشنری (dict)

```python
# از لیست تاپل‌ها
pairs = [("name", "Alice"), ("age", 25)]
person = dict(pairs)
print(person)            # {'name': 'Alice', 'age': 25}

# از kwargs
person = dict(name="Bob", age=30)
print(person)            # {'name': 'Bob', 'age': 30}
```

---

## تبدیل بولی

### به بولی (bool)

```python
# اعداد: ۰ False، بقیه True
print(bool(0))           # False
print(bool(42))          # True
print(bool(-5))          # True
print(bool(0.0))         # False
print(bool(0.1))         # True

# رشته‌ها: خالی False، غیرخالی True
print(bool(""))          # False
print(bool("Hello"))     # True
print(bool(" "))         # True (حتی فاصله!)

# مجموعه‌ها: خالی False، غیرخالی True
print(bool([]))          # False
print(bool([1, 2, 3]))   # True
print(bool({}))          # False
print(bool({"a": 1}))    # True
```

**قاعده کلی:**
- **صفر/خالی** → `False`
- **غیرصفر/غیرخالی** → `True`

---

## تبدیل‌های رایج در عمل

### سینیario 1: ورودی کاربر

```python
# ورودی کاربر همیشه رشته است!
user_input = input("Enter your age: ")
print(type(user_input))  # <class 'str'>

# تبدیل به عدد
age = int(user_input)
print(f"Next year you'll be {age + 1}")
```

### سناریو ۲: خروجی فرمت‌شده

```python
# تبدیل برای نمایش
score = 95.5
message = "Your score is: " + str(score) + "%"
print(message)

# یا بهتر
print(f"Your score is: {score}%")
```

### سناریو ۳: کار با فایل

```python
# داده از فایل معمولاً رشته است
data = "42"
number = int(data)
```

---

## تبدیل‌های پیچیده‌تر

### تبدیل پایه اعداد

```python
# تبدیل به پایه‌های مختلف
print(bin(10))           # 0b1010 (باینری)
print(oct(10))           # 0o12 (اکتال)
print(hex(10))          # 0xa (هگزادسیمال)

# تبدیل از رشته با پایه خاص
print(int("1010", 2))    # 10 (از باینری)
print(int("12", 8))      # 10 (از اکتال)
print(int("a", 16))      # 10 (از هگزادسیمال)
```

### تبدیل نویسه‌ها

```python
# کد ASCII/یونیکد
print(ord('A'))          # 65
print(ord('a'))          # 97
print(chr(65))           # 'A'
print(chr(97))           # 'a'
```

---

## اشتباهات رایج

### اشتباه ۱: تبدیل رشته غیرعددی به عدد

```python
# ❌ اشتباه
number = int("Hello")    # ValueError!

# ✅ صحیح
number = int("42")       # کار می‌کند

# ✅ بررسی اول
user_input = "42"
if user_input.isdigit():
    number = int(user_input)
else:
    print("Please enter a valid number!")
```

### اشتباه ۲: فراموش کردن تبدیل ورودی

```python
# ❌ اشتباه
age = input("Enter age: ")
years_until_100 = 100 - age  # TypeError!

# ✅ صحیح
age = int(input("Enter age: "))
years_until_100 = 100 - age
```

### اشتباه ۳: تبدیل اعشار به صحیح بدون فکر

```python
# ❌ داده از دست می‌رود
price = 19.99
whole_price = int(price)
print(whole_price)       # 19 (قسمت اعشار از دست رفت!)

# ✅ نگه‌داشتن اعشار
price_float = float(price)
# یا رند کردن
rounded_price = round(price)  # 20
```

### اشتباه ۴: تبدیل لیست به تاپل به اشتباه

```python
# ❌ فراموش کردن که تاپل‌ها ثابت هستند
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
my_tuple[0] = 10         # TypeError! تاپل‌ها تغییرناپذیرند

# ✅ فقط وقتی تاپل نیاز دارید استفاده کنید
my_tuple = tuple(my_list)  # برای داده‌های ثابت
```

### اشتباه ۵: تبدیل دیکشنری به لیست

```python
# فقط کلیدها می‌آیند
data = {"a": 1, "b": 2}
keys = list(data)
print(keys)              # ['a', 'b']

# برای گرفتن مقادیر
values = list(data.values())
print(values)            # [1, 2]

# برای گرفتن جفت‌ها
items = list(data.items())
print(items)             # [('a', 1), ('b', 2)]
```

---

## خودتان امتحان کنید: تمرین‌ها

### تمرین ۱: تمرین‌های پایه

```python
# تبدیل اینها را انجام دهید
result1 = int("100")
result2 = float("3.14159")
result3 = str(2024)
result4 = bool(0)
result5 = list("Python")

print(result1, result2, result3, result4, result5)
```

### تمرین ۲: ماشین حساب ورودی

کدی بنویسید که:
۱. دو عدد از کاربر بگیرد
۲. آنها را جمع کند
۳. نتیجه را نمایش دهد

**راهنمایی:** ورودی را به int تبدیل کنید!

### تمرین ۳: تبدیل درجه حرارت

کدی بنویسید که:
۱. درجه حرارت فارنهایت را به عنوان رشته بگیرد
۲. آن را به float تبدیل کند
۳. به سلسیوس تبدیل کند: `(fahrenheit - 32) * 5/9`
۴. نتیجه را با دو رقم اعشار نمایش دهد

### تمرین ۴: لیست منحصر به فرد

کدی بنویسید که یک لیست با تکرارها بگیرد و لیست جدیدی با مقادیر منحصر به فرد برگرداند.

**راهنمایی:** از `set()` استفاده کنید!

---

## مرجع سریع

### توابع تبدیل

```python
# عددی
int(x)       # تبدیل به صحیح
float(x)     # تبدیل به اعشار

# رشته‌ای
str(x)       # تبدیل به رشته

# مجموعه
list(x)      # تبدیل به لیست
tuple(x)     # تبدیل به تاپل
set(x)       # تبدیل به مجموعه (منحصر به فرد)
dict(x)      # تبدیل به دیکشنری

# بولی
bool(x)      # تبدیل به True/False

# خاص
bin(x)       # باینری رشته‌ای
hex(x)       # هگزادسیمال رشته‌ای
ord(c)       # کد ASCII کاراکتر
chr(n)       # کاراکتر از کد ASCII
```

### نکات مهم

- ورودی `input()` همیشه **رشته** است - تبدیل کنید!
- `int()` اعشار را **حذف می‌کند**، رند نمی‌کند
- `set()` **تکرارها را حذف می‌کند**
- `bool()` صفر/خالی را `False` می‌کند، بقیه `True`

---

## نکات کلیدی

۱. **ورودی کاربر همیشه رشته است** - آن را قبل از استفاده عددی تبدیل کنید
۲. **از f-strings** برای جمع کردن متن و اعداد بدون تبدیل صریح استفاده کنید
۳. **`int()` به سمت صفر گرد می‌کند** - از `round()` برای گرد کردن استفاده کنید
۴. **`set()` برای حذف تکرارها** عالی است
۵. **`bool()`** صفر/خالی را `False` می‌کند

---

## گام بعدی چیست؟

حالا که می‌دانید چگونه انواع داده را تبدیل کنید، بیایید درباره عملیات‌های پیچیده‌تر یاد بگیریم:
- **عملگرها** - انجام محاسبات و مقایسه‌ها
- **ترتیب ارزیابی** - درک اینکه کدام عملیات اول انجام می‌شود
