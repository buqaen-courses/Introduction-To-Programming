# حلقه‌های while در پایتون

## آنچه خواهید آموخت
- چگونه تا وقتی شرطی برقرار است کد را تکرار کنید
- تفاوت بین while و for
- نحوه ایجاد حلقه‌های بی‌نهایت و کنترل آنها

---

## while چیست؟

**while** حلقه‌ای است که تا وقتی یک شرط `True` است، ادامه می‌یابد.

### تشبیه: چراغ قرمز

```
┌─────────────────────────────────┐
│        چراغ راهنمایی             │
├─────────────────────────────────┤
│  while چراغ قرمز است:           │
│      صبر کن                     │
│  حرکت کن                        │
└─────────────────────────────────┘
```

### تفاوت for و while

| for | while |
|-----|-------|
| وقتی می‌دانید چند بار | وقتی نمی‌دانید چند بار |
| روی مجموعه می‌چرخد | تا وقتی شرط برقرار است |
| مقداردهی اولیه خودکار | مقداردهی اولیه دستی |
| تعداد تکرار مشخص | ممکن است بی‌نهایت شود |

---

## نحو پایه

```python
while condition:
    # کدی که تا وقتی condition True است اجرا می‌شود
    # (با تورفتگی!)
```

### قوانین

۱. شرط اول بررسی می‌شود
۲. اگر `True`: کد اجرا می‌شود، برمی‌گردد به ۱
۳. اگر `False`: حلقه تمام می‌شود

### مثال ساده

```python
# شمارش ۱ تا ۵
count = 1
while count <= 5:
    print(count)
    count = count + 1

print("Done!")
# خروجی: 1, 2, 3, 4, 5, Done!
```

---

## مثال‌های پایه

### شمارش

```python
# شمارش معکوس
count = 10
while count > 0:
    print(count)
    count = count - 1

print("Blast off!")
```

### جمع کردن تا شرط

```python
# جمع اعداد تا وقتی مجموع از ۱۰۰ بیشتر نشود
total = 0
num = 1

while total < 100:
    total = total + num
    print(f"Added {num}, total = {total}")
    num = num + 1

print(f"Final total: {total}")
```

### حدس عدد

```python
import random

secret = random.randint(1, 10)
guess = 0

while guess != secret:
    guess = int(input("Guess a number (1-10): "))
    
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")

print("Congratulations! You got it!")
```

---

## while با else

مثل for، while هم می‌تواند else داشته باشد.

```python
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print("Loop completed normally")

# خروجی:
# 0
# 1
# 2
# 3
# 4
# Loop completed normally
```

### با break

```python
count = 0
while count < 10:
    print(count)
    if count == 5:
        print("Breaking early!")
        break
    count = count + 1
else:
    print("This won't print because of break")

# خروجی: 0, 1, 2, 3, 4, 5, Breaking early!
```

---

## حلقه‌های بی‌نهایت

### عمدی

```python
# حلقه بی‌نهایت با break
while True:
    user_input = input("Enter command (or 'quit'): ")
    
    if user_input == "quit":
        print("Goodbye!")
        break
    
    print(f"Executing: {user_input}")
```

### با شرط همیشه True

```python
running = True

while running:
    print("Running...")
    response = input("Continue? (yes/no): ")
    
    if response == "no":
        running = False

print("Stopped")
```

### ⚠️ خطای رایج: فراموش کردن بروزرسانی

```python
# ❌ حلقه بی‌نهایت!
count = 1
while count <= 5:
    print(count)
    # Forgot: count = count + 1!

# ✅ صحیح
count = 1
while count <= 5:
    print(count)
    count = count + 1  # Don't forget!
```

---

## کنترل حلقه while

### break

```python
# یافتن اولین عدد بخش‌پذیر بر ۷
num = 1
while num <= 100:
    if num % 7 == 0:
        print(f"Found: {num}")
        break
    num = num + 1
```

### continue

```python
# چاپ فقط اعداد فرد
count = 0
while count < 10:
    count = count + 1
    
    if count % 2 == 0:
        continue  # رد کردن اعداد زوج
    
    print(count)

# خروجی: 1, 3, 5, 7, 9
```

### مهم: مکان بروزرسانی

```python
# ⚠️ مراقب باشید - ممکن است بی‌نهایت شود
count = 0
while count < 10:
    if count % 2 == 0:
        continue  # ⬅️ count هرگز بروزرسانی نمی‌شود!
    print(count)
    count = count + 1

# ✅ بروزرسانی قبل از continue
count = 0
while count < 10:
    count = count + 1  # ⬅️ اول بروزرسانی کن
    
    if count % 2 == 0:
        continue
    
    print(count)
```

---

## کاربردهای عملی

### مثال ۱: اعتبارسنجی ورودی

```python
# تا وقتی ورودی معتبر ندهد، تکرار کن
while True:
    age_input = input("Enter your age: ")
    
    if age_input.isdigit():
        age = int(age_input)
        if 0 < age < 150:
            break
        else:
            print("Age must be between 1 and 149!")
    else:
        print("Please enter a valid number!")

print(f"Your age is {age}")
```

### مثال ۲: رمز عبور

```python
password = "secret123"
attempts = 3

while attempts > 0:
    user_input = input("Enter password: ")
    
    if user_input == password:
        print("Access granted!")
        break
    else:
        attempts = attempts - 1
        print(f"Wrong! {attempts} attempts remaining.")
else:
    print("Account locked!")
```

### مثال ۳: منو

```python
while True:
    print("\n=== Menu ===")
    print("1. Say Hello")
    print("2. Calculate")
    print("3. Exit")
    
    choice = input("Select (1-3): ")
    
    if choice == "1":
        print("Hello, World!")
    elif choice == "2":
        num1 = float(input("Number 1: "))
        num2 = float(input("Number 2: "))
        print(f"Sum: {num1 + num2}")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
```

### مثال ۴: شبیه‌سازی

```python
# شبیه‌سازی رشد باکتری
population = 100
day = 0
target = 1000

while population < target:
    day = day + 1
    population = population * 2  # دو برابر شدن هر روز
    print(f"Day {day}: {population} bacteria")

print(f"Target reached on day {day}!")
```

---

## while vs for: چه زمانی از کدام استفاده کنیم؟

### از for استفاده کنید وقتی:

```python
# ✅ وقتی می‌دانید چند بار
for i in range(10):
    print(i)

# ✅ وقتی روی مجموعه می‌چرخید
for item in items:
    print(item)

# ✅ وقتی تعداد مشخص است
for char in "Hello":
    print(char)
```

### از while استفاده کنید وقتی:

```python
# ✅ وقتی نمی‌دانید چند بار
while user_input != "quit":
    user_input = input("Command: ")

# ✅ وقتی منتظر یک رویداد هستید
while not file_ready:
    wait_for_file()

# ✅ محاسبات تکراری تا شرط
while error > 0.001:
    error = improve_estimate()
```

---

## اشتباهات رایج

### اشتباه ۱: فراموش کردن مقداردهی اولیه

```python
# ❌ خطا - count تعریف نشده
while count < 5:
    print(count)
    count = count + 1

# ✅ صحیح
count = 0
while count < 5:
    print(count)
    count = count + 1
```

### اشتباه ۲: حلقه بی‌نهایت

```python
# ❌ هرگز تمام نمی‌شود
i = 0
while i < 5:
    print(i)
    # Forgot to increment!

# ✅ صحیح
i = 0
while i < 5:
    print(i)
    i = i + 1
```

### اشتباه ۳: شرط همیشه True

```python
# ❌ بی‌نهایت (مگر با break)
x = 5
while x > 0:
    print(x)
    x = x + 1  # x هرگز از ۵ کمتر نمی‌شود!

# ✅ صحیح
x = 5
while x > 0:
    print(x)
    x = x - 1
```

### اشتباه ۴: continue بدون بروزرسانی

```python
# ❌ بی‌نهایت
i = 0
while i < 10:
    if i % 2 == 0:
        continue  # i هرگز بروزرسانی نمی‌شود!
    print(i)
    i = i + 1

# ✅ صحیح
i = 0
while i < 10:
    i = i + 1
    if i % 2 == 0:
        continue
    print(i)
```

### اشتباه ۵: استفاده از while برای موارد for

```python
# ❌ overkill - from could do this
count = 0
while count < len(items):
    print(items[count])
    count = count + 1

# ✅ much cleaner
for item in items:
    print(item)
```

---

## خودتان امتحان کنید: تمرین‌ها

### تمرین ۱: شمارش معکوس

کدی بنویسید که:
۱. از ۱۰ تا ۱ بشمارد
۲. هر عدد را چاپ کند
۳. "Blast off!" در انتها چاپ کند

### تمرین ۲: محاسبه فاکتوریل

کدی بنویسید که فاکتوریل یک عدد را محاسبه کند:
- ۵! = ۵ × ۴ × ۳ × ۲ × ۱ = ۱۲۰
- از while استفاده کنید

### تمرین ۳: بازی حدس عدد پیشرفته

```python
import random

secret = random.randint(1, 100)
attempts = 0
max_attempts = 7

# کد را کامل کنید:
# - تا ۷ تلاش یا تا حدس صحیح
# - راهنمایی "Too high" یا "Too low"
# - شمارش تلاش‌ها
# - پیام پایان مناسب
```

### تمرین ۴: ماشین حساب با while

کدی بنویسید که:
۱. تا وقتی کاربر "quit" را نزده ادامه دهد
۲. هر بار دو عدد و یک عملگر بگیرد
۳. نتیجه را نمایش دهد
۴. اگر تقسیم بر صفر بود، خطا بدهد و ادامه دهد

### تمرین ۵: الگوی فیبوناچی

کدی بنویسید که اعداد فیبوناچی را تا وقتی از ۱۰۰۰ کمتر است چاپ کند:
- ۰, ۱, ۱, ۲, ۳, ۵, ۸, ۱۳, ۲۱, ۳۴, ...
- هر عدد مجموع دو عدد قبلی است

---

## مرجع سریع

### نحو while

```python
while condition:
    # code

while condition:
    # code
else:
    # if no break occurred

while True:
    # infinite loop (use break!)
```

### کنترل حلقه

```python
break       # exit immediately
continue    # skip to next iteration
else        # execute if no break
```

### الگوهای رایج

```python
# Count up
i = 0
while i < n:
    i += 1

# Count down
i = n
while i > 0:
    i -= 1

# Input validation
while True:
    if valid:
        break

# Wait for condition
while not condition:
    do_something()
```

---

## نکات کلیدی

۱. **while** تا وقتی شرط True است تکرار می‌شود
۲. **همیشه شرط را بروزرسانی کنید** - وگرنه بی‌نهایت می‌شود!
۳. **while True** + **break** برای ورودی معتبر عالی است
۴. **for** برای تعداد مشخص، **while** برای شرط محور
۵. **else** در while اگر break اجرا نشود

---

## گام بعدی چیست؟

حالا که با حلقه‌ها آشنا شدید، بیایید درباره کار با متن یاد بگیریم:
- **عملیات رشته** - کار با متن
