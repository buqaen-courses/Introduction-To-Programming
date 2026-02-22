# شرایط تودرتو در پایتون

## آنچه خواهید آموخت
- چگونه یک شرط داخل شرط دیگر قرار دهید
- چه زمانی از شرایط تودرتو استفاده کنید
- نحوه ساختاردهی کد برای خوانایی

---

## شرایط تودرتو چیست؟

**شرایط تودرتو** یعنی یک شرط داخل شرط دیگر. مثل جعبه‌های روسی: یک شرط درون شرط دیگر.

### تشبیه: تصمیمات تو در تو

تصور کنید می‌خواهید تصمیم بگیرید آیا می‌توانید رانندگی کنید:

```
آیا گواهینامه دارید؟
    └── بله → آیا سن شما بالای ۱۸ است؟
                └── بله → آیا مشروب نوشیده‌اید؟
                            └── خیر → می‌توانید رانندگی کنید! ✓
                            └── بله → نمی‌توانید! ✗
                └── خیر → نمی‌توانید! ✗
    └── خیر → نمی‌توانید! ✗
```

---

## ساختار پایه

### نحو

```python
if condition1:
    # کد
    if condition2:
        # کد درون شرط داخلی
    else:
        # کد
else:
    # کد
```

### مثال ساده

```python
age = 25
has_license = True

if has_license:
    if age >= 18:
        print("You can drive!")
    else:
        print("You're too young to drive.")
else:
    print("You need a license first.")
```

---

## مثال‌های عملی

### مثال ۱: ورود به سیستم

```python
username = input("Username: ")
password = input("Password: ")

if username == "admin":
    if password == "secret123":
        print("✓ Login successful!")
        print("Welcome, Administrator.")
    else:
        print("✗ Wrong password.")
        print("Please try again.")
else:
    print("✗ Username not found.")
    print("Please check your username.")
```

### مثال ۲: بررسی شایستگی وام

```python
income = 50000
credit_score = 720
has_debt = False

if income >= 40000:
    if credit_score >= 700:
        if not has_debt:
            print("✓ Loan approved!")
            print("Excellent credit profile.")
        else:
            print("⚠ Loan pending.")
            print("Debt review required.")
    else:
        print("⚠ Loan under review.")
        print("Credit score needs improvement.")
else:
    print("✗ Loan denied.")
    print("Income requirement not met.")
```

### مثال ۳: انتخاب رستوران

```python
is_hungry = True
has_money = True
is_vegetarian = False

if is_hungry:
    if has_money:
        if is_vegetarian:
            print("Go to: Green Garden (Vegetarian)")
        else:
            print("Go to: Burger Palace")
    else:
        print("Stay home and cook something.")
else:
    print("Maybe just have a drink somewhere.")
```

---

## تمیز کردن شرایط تودرتو

### روش ۱: استفاده از and

```python
# ❌ تودرتو
if has_license:
    if age >= 18:
        if is_sober:
            print("Can drive")

# ✅ صاف
if has_license and age >= 18 and is_sober:
    print("Can drive")
```

### روش ۲: استفاده از elif

```python
# ❌ تودرتو
if score >= 90:
    if attendance > 80:
        grade = "A+"
    else:
        grade = "A"
else:
    if score >= 80:
        grade = "B"

# ✅ بهتر
if score >= 90 and attendance > 80:
    grade = "A+"
elif score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
```

### روش ۳: توابع کمکی

```python
# ✅ تمیز با تابع

def can_drive(age, has_license, is_sober):
    if not has_license:
        return False, "No license"
    if age < 18:
        return False, "Too young"
    if not is_sober:
        return False, "Not sober"
    return True, "OK"

# استفاده
allowed, reason = can_drive(25, True, True)
if allowed:
    print("You can drive!")
else:
    print(f"Cannot drive: {reason}")
```

---

## ساختارهای پیچیده

### سطح‌های چندگانه

```python
# بررسی سلامت سیستم
is_online = True
has_updates = True
storage_ok = True

if is_online:
    print("System is online.")
    
    if has_updates:
        print("Updates available.")
        
        if storage_ok:
            print("Installing updates...")
            print("Updates installed successfully!")
        else:
            print("Not enough storage for updates.")
            print("Please free up space.")
    else:
        print("System is up to date.")
else:
    print("System is offline.")
    print("Please check connection.")
```

### if-elif درون if

```python
# مدیریت سفارش
is_member = True
order_total = 150

if is_member:
    print("Member detected.")
    
    if order_total > 200:
        discount = 0.25
        tier = "Gold"
    elif order_total > 100:
        discount = 0.15
        tier = "Silver"
    else:
        discount = 0.10
        tier = "Bronze"
    
    print(f"Tier: {tier}, Discount: {discount*100}%")
else:
    print("Guest checkout - no discount.")
```

---

## الگوهای رایج

### الگو ۱: اعتبارسنجی مرحله به مرحله

```python
# بررسی فرم ثبت‌نام
username = input("Username: ")
email = input("Email: ")
password = input("Password: ")

if len(username) >= 3:
    if "@" in email:
        if len(password) >= 8:
            print("✓ Registration successful!")
        else:
            print("✗ Password must be at least 8 characters.")
    else:
        print("✗ Invalid email address.")
else:
    print("✗ Username must be at least 3 characters.")
```

### الگو ۲: دسترسی مبتنی بر نقش

```python
is_logged_in = True
user_role = "admin"
resource = "financial_data"

if is_logged_in:
    if user_role == "admin":
        print("Full access granted.")
        print(f"Accessing: {resource}")
    elif user_role == "editor":
        if resource != "financial_data":
            print("Read-write access granted.")
        else:
            print("Read-only access for financial data.")
    else:
        print("Read-only access granted.")
else:
    print("Access denied. Please log in.")
```

### الگو ۳: تصمیمات بازی

```python
has_key = True
has_weapon = False
door_locked = True

if has_key:
    if door_locked:
        print("You unlock the door with your key.")
        door_locked = False
    
    if not door_locked:
        print("You enter the room.")
        
        if has_weapon:
            print("You defeat the monster!")
            print("✓ You win!")
        else:
            print("A monster attacks!")
            print("✗ Game over - you need a weapon.")
else:
    print("The door is locked.")
    print("✗ You need a key.")
```

---

## نکات خوانایی

### محدود کردن عمق

```python
# ❌ خیلی عمیق (3+ سطح)
if a:
    if b:
        if c:
            if d:
                print("Too deep!")

# ✅ صاف‌تر
if not a:
    return
if not b:
    return
if not c:
    return
if d:
    print("Better!")
```

### استفاده از پرانتز برای وضوح

```python
# ✅ با پرانتز واضح
if (has_ticket and is_adult) or is_vip:
    print("Entry granted")

# ✅ همچنین واضح
if has_ticket:
    if is_adult or is_vip:
        print("Entry granted")
```

### کامنت‌گذاری شرایط پیچیده

```python
# بررسی می‌کند آیا کاربر می‌تواند فایل را ویرایش کند
# نیازمندی‌ها: مالک باشد یا دسترسی نوشتن داشته باشد
# و همچنین فایل قفل نباشد

if (is_owner or has_write_permission) and not is_locked:
    print("Can edit file")
```

---

## اشتباهات رایج

### اشتباه ۱: else اشتباهی

```python
# ❌ else به if اشتباهی متصل شده
if condition1:
    if condition2:
        print("Both true")
    else:           # این else برای condition2 است
        print("Only 1 true")
        
# ✅ صحیح با پرانتز یا بازسازی
if condition1:
    if condition2:
        print("Both true")
else:               # این else برای condition1 است
    print("1 false")
```

### اشتباه ۲: منطق اشتباه

```python
# ❌ منطق اشتباه
if age >= 18:
    if age < 18:        # هرگز True نمی‌شود!
        print("Impossible!")

# ✅ صحیح
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

### اشتباه ۳: تورفتگی اشتباه

```python
# ❌ اشتباه
if x > 0:
    if y > 0:
    print("Both positive")  # IndentationError!

# ✅ صحیح
if x > 0:
    if y > 0:
        print("Both positive")
```

### اشتباه ۴: فراموش کردن یک حالت

```python
# ⚠️ ممکن است چیزی را از دست بدهد
if user_type == "admin":
    if logged_in:
        show_admin_panel()
    # else ندارد!
elif user_type == "user":
    show_user_panel()
# اگر user_type چیز دیگری باشد چه؟
```

---

## خودتان امتحان کنید: تمرین‌ها

### تمرین ۱: سیستم نمره‌دهی

کدی بنویسید که:
۱. نمره امتحان (۰-۱۰۰) را بگیرد
۲. نمره تکالیف (۰-۱۰۰) را بگیرد
۳. اگر هر دو بالای ۶۰ باشند: "Pass"
۴. اگر یکی بالای ۶۰ باشد: "Conditional Pass"
۵. اگر هیچ‌کدام بالای ۶۰ نباشند: "Fail"

### تمرین ۲: سیستم منو

```python
# کد منوی رستوران را کامل کنید:
print("1. Pizza ($10)")
print("2. Burger ($8)")
print("3. Salad ($6)")

choice = input("Select item (1-3): ")
is_member = input("Member? (yes/no): ") == "yes"

# اگر عضو باشد ۱۰٪ تخفیف
# اگر بیش از ۲ آیتم سفارش دهد ۵٪ تخفیف اضافی
# قیمت نهایی را محاسبه و نمایش دهید
```

### تمرین ۳: بازی حدس کلمه

```python
secret_word = "python"
guess = input("Guess the word: ").lower()
attempts = 1

# اگر حدس درست بود: "Correct in X attempts!"
# اگر نزدیک بود (طول یکی): "Close! Try again."
# اگر خیلی دور بود: "Not even close! Try again."
# تا ۳ تلاش اجازه بدهید
```

### تمرین ۴: بررسی تاریخ

```python
day = int(input("Day (1-31): "))
month = int(input("Month (1-12): "))
year = int(input("Year: "))

# بررسی کنید:
# - ماه باید ۱-۱۲ باشد
# - روز باید معتبر برای آن ماه باشد
# - سال کبیسه را برای فوریه در نظر بگیرید
# پیام مناسب نمایش دهید
```

---

## مرجع سریع

### ساختار تودرتو

```python
if condition1:
    # کد
    if condition2:
        # کد داخلی
        if condition3:
            # کد عمیق‌تر
```

### تبدیل به شرایط صاف

```python
# قبل
if a:
    if b:
        print("OK")

# بعد
if a and b:
    print("OK")
```

### روش early return

```python
# تمیزتر با return
if not condition1:
    return
if not condition2:
    return
print("All conditions met")
```

---

## نکات کلیدی

۱. **شرایط تودرتو** یک شرط داخل شرط دیگر است
۲. **بیش از ۳ سطح تودرتو** معمولاً نشانه نیاز به refactoring است
۳. **and و or** می‌توانند به صاف کردن شرایط کمک کنند
۴. **تابعات کمکی** کد پیچیده را به بخش‌های کوچکتر تقسیم می‌کنند
۵. **تورفتگی صحیح** برای خوانایی بسیار مهم است

---

## گام بعدی چیست؟

حالا که با شرایط تودرتو آشنا شدید، بیایید درباره تکرار یاد بگیریم:
- **حلقه‌ها** - انجام کارها بارها و بارها
