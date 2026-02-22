# کنترل حلقه‌ها در پایتون

## آنچه خواهید آموخت
- چگونه از حلقه زودتر خارج شوید
- چگونه یک تکرار را رد کنید
- نحوه استفاده از else در حلقه‌ها
- الگوهای پیشرفته کنترل جریان

---

## چرا کنترل حلقه؟

گاهی اوقات می‌خواهید:
- **زودتر از حلقه خارج شوید** (وقتی چیزی را پیدا کردید)
- **یک تکرار را رد کنید** (وقتی شرایط خاصی پیش آید)
- **کاری انجام دهید** اگر حلقه کامل اجرا شود

---

## break (خروج از حلقه)

**break** بلافاصله از حلقه خارج می‌شود.

### مثال ساده

```python
# پیدا کردن اولین عدد زوج
numbers = [1, 3, 5, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        print(f"Found even number: {num}")
        break  # خارج شدن

print("Done")
# خروجی: Found even number: 8
#         Done
```

### یافتن آیتم در لیست

```python
fruits = ["apple", "banana", "cherry", "date"]
target = "cherry"

for fruit in fruits:
    print(f"Checking: {fruit}")
    if fruit == target:
        print(f"Found {target}!")
        break

# خروجی:
# Checking: apple
# Checking: banana
# Checking: cherry
# Found cherry!
```

### بررسی وجود

```python
# بررسی اینکه آیا عدد اول وجود دارد
numbers = [4, 6, 8, 9, 10, 11, 12]
has_prime = False

for num in numbers:
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break  # خارج شدن از حلقه داخلی
        
        if is_prime:
            has_prime = True
            print(f"Found prime: {num}")
            break  # خارج شدن از حلقه بیرونی

if not has_prime:
    print("No prime numbers found")
```

### گرفتن ورودی تا شرط

```python
# تا وقتی کاربر "quit" را نزده
while True:
    command = input("Enter command (or 'quit'): ")
    if command == "quit":
        print("Goodbye!")
        break
    print(f"Executing: {command}")
```

---

## continue (رفتن به تکرار بعدی)

**continue** بقیه کد در آن تکرار را رد کرده و به تکرار بعدی می‌رود.

### مثال ساده

```python
# چاپ فقط اعداد فرد
for i in range(10):
    if i % 2 == 0:  # اگر زوج است
        continue    # رد کردن
    print(i)

# خروجی: 1, 3, 5, 7, 9
```

### پردازش لیست با فیلتر

```python
# پردازش فقط اعداد مثبت
numbers = [3, -1, 5, -2, 8, -4, 10]

for num in numbers:
    if num < 0:
        continue  # اعداد منفی را رد کن
    
    # فقط اعداد مثبت به اینجا می‌رسند
    square = num ** 2
    print(f"{num} squared = {square}")

# خروجی:
# 3 squared = 9
# 5 squared = 25
# 8 squared = 64
# 10 squared = 100
```

### پردازش رشته

```python
text = "Hello123World456"

for char in text:
    if char.isdigit():
        continue  # اعداد را رد کن
    print(char, end="")

# خروجی: HelloWorld
```

---

## else در حلقه

**else** در حلقه اجرا می‌شود اگر حلقه **کامل** اجرا شود (بدون break).

### مفهوم

```python
for item in sequence:
    if condition:
        break
else:
    # اگر break اجرا نشود، این اجرا می‌شود
```

### مثال: یافتن عدد اول

```python
# بررسی اینکه آیا یک عدد اول است
def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} is not prime (divisible by {i})")
            break
    else:
        # اگر break اجرا نشود، یعنی اول است
        print(f"{n} is prime!")
        return True
    
    return False

is_prime(17)   # 17 is prime!
is_prime(18)   # 18 is not prime (divisible by 2)
```

### جستجوی آیتم

```python
# بررسی اینکه آیا مقداری در لیست وجود دارد
fruits = ["apple", "banana", "cherry"]
target = "date"

for fruit in fruits:
    if fruit == target:
        print(f"Found {target}")
        break
else:
    # اگر break اجرا نشود
    print(f"{target} not found in the list")

# خروجی: date not found in the list
```

### مقایسه با پرچم

```python
# ❌ بدون else (با پرچم)
found = False
for fruit in fruits:
    if fruit == target:
        found = True
        print(f"Found {target}")
        break

if not found:
    print(f"{target} not found")

# ✅ با else (تمیزتر)
for fruit in fruits:
    if fruit == target:
        print(f"Found {target}")
        break
else:
    print(f"{target} not found")
```

---

## pass (انجام ندادن کاری)

**pass** یک placeholder است - هیچ کاری انجام نمی‌دهد.

### استفاده‌ها

```python
# ۱. در حلقه‌ای که هنوز پیاده‌سازی نشده
for i in range(10):
    pass  # TODO: implement later

# ۲. در شرطی که هنوز پیاده‌سازی نشده
if condition:
    pass  # TODO: handle this case
else:
    print("Other case")

# ۳. در کلاس خالی
class MyClass:
    pass  # Will add methods later

# ۴. در تابع خالی
def placeholder():
    pass
```

---

## الگوهای پیشرفته

### یافتن چندین آیتم

```python
# پیدا کردن همه اعداد زوج
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

for num in numbers:
    if num % 2 != 0:
        continue
    even_numbers.append(num)

print(even_numbers)  # [2, 4, 6, 8, 10]
```

### اعتبارسنجی

```python
# بررسی اینکه آیا همه اعداد مثبت هستند
numbers = [3, 5, 8, -2, 10]

for num in numbers:
    if num < 0:
        print(f"Found negative number: {num}")
        print("List is not all positive!")
        break
else:
    print("All numbers are positive!")

# خروجی:
# Found negative number: -2
# List is not all positive!
```

### پردازش با محدودیت

```python
# پردازش حداکثر ۳ آیتم
items = ["a", "b", "c", "d", "e"]
processed = 0
max_items = 3

for item in items:
    if processed >= max_items:
        print("Reached maximum, stopping.")
        break
    
    print(f"Processing: {item}")
    processed = processed + 1

# خروجی:
# Processing: a
# Processing: b
# Processing: c
# Reached maximum, stopping.
```

---

## حلقه‌های تو در تو با کنترل

### break از حلقه داخلی

```python
# پیدا کردن جفت با مجموع خاص
numbers = [1, 2, 3, 4, 5]
target_sum = 7

for i in numbers:
    for j in numbers:
        if i + j == target_sum:
            print(f"Found: {i} + {j} = {target_sum}")
            break  # فقط از حلقه داخلی خارج می‌شود
    # حلقه بیرونی ادامه می‌یابد
```

### خروج از چندین حلقه

```python
# روش ۱: با پرچم
found = False
for i in range(5):
    for j in range(5):
        if i * j > 10:
            print(f"Found: {i} x {j} = {i*j}")
            found = True
            break
    if found:
        break

# روش ۲: تبدیل به تابع
def find_pair():
    for i in range(5):
        for j in range(5):
            if i * j > 10:
                return i, j  # return از همه حلقه‌ها خارج می‌شود
    return None

result = find_pair()
```

---

## کاربردهای عملی

### مثال ۱: گرفتن ورودی معتبر

```python
# تا وقتی عدد معتبر ندهد، ادامه بده
while True:
    user_input = input("Enter a number (or 'quit'): ")
    
    if user_input == "quit":
        print("Exiting...")
        break
    
    if not user_input.isdigit():
        print("Invalid input! Please enter a number.")
        continue
    
    number = int(user_input)
    print(f"You entered: {number}")
    print(f"Square: {number ** 2}")
```

### مثال ۲: پردازش فایل

```python
# پردازش خطوط تا رسیدن به خط خالی
lines = ["Line 1", "Line 2", "", "Line 4", "Line 5"]

for line in lines:
    if line == "":
        print("Empty line found, stopping.")
        break
    
    if line.startswith("#"):
        continue  # کامنت‌ها را رد کن
    
    print(f"Processing: {line}")

# خروجی:
# Processing: Line 1
# Processing: Line 2
# Empty line found, stopping.
```

### مثال ۳: جستجوی کاربر

```python
users = [
    {"name": "Alice", "active": True},
    {"name": "Bob", "active": False},
    {"name": "Charlie", "active": True}
]

# پیدا کردن اولین کاربر فعال
for user in users:
    if not user["active"]:
        continue  # کاربران غیرفعال را رد کن
    
    print(f"Found active user: {user['name']}")
    break
else:
    print("No active users found")

# خروجی: Found active user: Alice
```

---

## اشتباهات رایج

### اشتباه ۱: break در حلقه اشتباه

```python
# ⚠️ فقط از حلقه داخلی خارج می‌شود
for i in range(3):
    for j in range(3):
        if i * j > 2:
            break  # فقط از حلقه j خارج می‌شود
    print(f"i = {i}")  # این هنوز اجرا می‌شود
```

### اشتباه ۲: continue در حلقه اشتباه

```python
# ⚠️ فقط به تکرار بعدی در حلقه فعلی می‌رود
for i in range(3):
    for j in range(3):
        if j == 1:
            continue  # به j بعدی می‌رود، نه i
        print(f"i={i}, j={j}")
```

### اشتباه ۳: فراموش کردن else

```python
# ⚠️ این else مربوط به if است، نه for!
for i in range(5):
    if i == 3:
        break
else:  # این مربوط به for است، نه if!
    print("Loop completed")
```

### اشتباه ۴: else بدون break

```python
# ❌ else هیچ‌وقت اجرا نمی‌شود چون همیشه break می‌شود
for i in range(5):
    print(i)
    break
else:
    print("This will never print")
```

---

## خودتان امتحان کنید: تمرین‌ها

### تمرین ۱: شمارش معکوس

کدی بنویسید که از ۱۰ تا ۱ بشمارد، اما:
- اگر به ۵ رسید، "Halfway there!" چاپ کند و ادامه دهد
- اگر به ۳ رسید، بشمارد "Almost done!" و خارج شود

### تمرین ۲: اعتبارسنجی رمز

کدی بنویسید که:
۱. تا ۳ تلاش برای گرفتن رمز صحیح اجازه دهد
۲. اگر رمز صحیح بود، "Access granted!" و خارج شود
۳. اگر ۳ تلاش اشتباه بود، "Account locked!"

### تمرین ۳: پردازش لیست

کدی بنویسید که یک لیست اعداد را پردازش کند:
- اعداد منفی را رد کند
- اعداد زوج را چاپ کند
- اگر به عدد ۰ رسید، "Zero found, stopping!" و خارج شود
- اگر حلقه کامل اجرا شود، "Processing complete!" چاپ کند

### تمرین ۴: بازی حدس عدد

```python
import random

secret = random.randint(1, 100)
attempts = 0
max_attempts = 7

# کد را کامل کنید:
# - تا ۷ تلاش اجازه بدهید
# - راهنمایی "Too high" یا "Too low" بدهید
# - اگر حدس درست بود، "Congratulations!" و تعداد تلاش‌ها
# - اگر تمام تلاش‌ها اشتباه بود، "Game over! The number was X"
```

---

## مرجع سریع

### دستورات کنترل

```python
break       # خروج فوری از حلقه
continue    # رفتن به تکرار بعدی
else        # اگر حلقه کامل شود (بدون break)
pass        # هیچ کاری نکن
```

### استفاده else

```python
for item in items:
    if condition:
        break
else:
    # اگر break اجرا نشود
    print("No break occurred")
```

### حلقه‌های تو در تو

```python
# فقط از حلقه داخلی خارج می‌شود
for i in range(5):
    for j in range(5):
        if condition:
            break  # فقط از j خارج می‌شود

# خروج از همه حلقه‌ها
for i in range(5):
    for j in range(5):
        if condition:
            return  # از تابع خارج می‌شود
```

---

## نکات کلیدی

۱. **break** - فوری از حلقه خارج می‌شود
۲. **continue** - به تکرار بعدی می‌رود
۳. **else** - اگر حلقه کامل شود (بدون break)
۴. **pass** - placeholder، هیچ کاری نمی‌کند
۵. **break فقط حلقه فعلی** را می‌شکند، نه همه را

---

## گام بعدی چیست؟

حالا که با کنترل حلقه‌ها آشنا شدید، بیایید درباره حلقه while یاد بگیریم:
- **حلقه while** - تکرار تا وقتی شرط برقرار است
