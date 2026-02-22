# ساختارهای کنترلی: هدایت جریان برنامه

## ساختارهای کنترلی چیستند؟

ساختارهای کنترلی تعیین می‌کنند که دستورالعمل‌ها در یک برنامه به چه ترتیبی اجرا شوند. این ساختارها به برنامه‌ها اجازه می‌دهند تصمیم‌گیری کنند، اقدامات را تکرار کنند و به شرایط مختلف پاسخ دهند.

## سه ساختار اساسی

### ۱. توالی
**تعریف**: دستورالعمل‌ها را به ترتیب اجرا کن، یکی پس از دیگری.

**نماد فلوچارت**: مستطیل

**شبه‌کد:**
```
statement1
statement2
statement3
```

**مثال‌های کد واقعی:**
```python
# Python
name = "علی"
greeting = "سلام، " + name
print(greeting)

# JavaScript
let name = "علی";
let greeting = "سلام، " + name;
console.log(greeting);

# Java
String name = "علی";
String greeting = "سلام، " + name;
System.out.println(greeting);
```

### ۲. انتخاب (تصمیم‌گیری)
**تعریف**: بر اساس شرایط، مسیرهای مختلف انتخاب کن.

**نماد فلوچارت**: لوزی

#### IF ساده
```
IF condition THEN
    statements
END IF
```

```python
# بررسی عدد مثبت بودن
if number > 0:
    print("عدد مثبت است")
```

#### IF-ELSE
```
IF condition THEN
    true_statements
ELSE
    false_statements
END IF
```

```python
# بررسی قبول/رد
if score >= 60:
    print("قبول")
else:
    print("رد")
```

#### انتخاب چندگانه (IF-ELSEIF)
```
IF condition1 THEN
    statements1
ELSE IF condition2 THEN
    statements2
ELSE
    default_statements
END IF
```

```python
# ماشین نمره‌دهی
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"
```

#### IFهای تودرتو
```
IF outer_condition THEN
    IF inner_condition THEN
        statements
    END IF
END IF
```

```python
# شرط پیچیده
if age >= 18:
    if has_license:
        print("می‌تواند رانندگی کند")
    else:
        print("نیاز به گواهینامه دارد")
else:
    print("سن کافی ندارد")
```

### ۳. تکرار (حلقه)
**تعریف**: دستورالعمل‌ها را چندین بار تکرار کن.

**نماد فلوچارت**: مستطیل با منحنی پایین

#### حلقه پیش‌تست (WHILE)
```
WHILE condition DO
    statements
END WHILE
```

```python
# شمارش تا ۵
count = 1
while count <= 5:
    print(count)
    count += 1
```

#### حلقه پس‌تست (DO-WHILE/REPEAT-UNTIL)
```
REPEAT
    statements
UNTIL condition
```

```python
# پیاده‌سازی Python (با استفاده از while True)
while True:
    user_input = input("برای خروج 'quit' تایپ کنید: ")
    if user_input == "quit":
        break
    print(f"شما تایپ کردید: {user_input}")
```

#### حلقه شمارش‌شده (FOR)
```
FOR counter FROM start TO end DO
    statements
END FOR
```

```python
# حلقه ۵ بار
for i in range(1, 6):
    print(i)

# حلقه روی مجموعه
fruits = ["سیب", "موز", "گیلاس"]
for fruit in fruits:
    print(fruit)
```

## ساختارهای کنترلی پیشرفته

### دستورات کنترل حلقه

#### BREAK
فوراً از حلقه خارج شود:
```python
# یافتن اولین عدد زوج
numbers = [1, 3, 5, 6, 8, 9]
for num in numbers:
    if num % 2 == 0:
        print(f"اولین عدد زوج: {num}")
        break
```

#### CONTINUE
به تکرار بعدی برود:
```python
# فقط اعداد فرد را چاپ کن
for num in range(10):
    if num % 2 == 0:
        continue
    print(num)
```

#### ELSE در حلقه‌ها
وقتی حلقه به طور طبیعی تمام شود اجرا شود:
```python
# جستجو با نشان نتیجه
def find_item(items, target):
    for item in items:
        if item == target:
            print(f"یافت شد {target}")
            break
    else:
        print(f"{target} یافت نشد")
```

### Switch/Case (در برخی زبان‌ها)
انتخاب چندگانه بر اساس مقدار:
```javascript
// JavaScript
switch (grade) {
    case 'A':
        console.log("عالی");
        break;
    case 'B':
        console.log("خوب");
        break;
    case 'C':
        console.log("متوسط");
        break;
    default:
        console.log("نیاز به تلاش بیشتر");
}
```

## الگوهای ساختار کنترلی

### حلقه اعتبارسنجی ورودی
```python
# تا زمانی که ورودی معتبر وارد شود ادامه بده
while True:
    try:
        age = int(input("سن را وارد کنید: "))
        if age >= 0 and age <= 120:
            break
        else:
            print("سن باید بین ۰ تا ۱۲۰ باشد")
    except ValueError:
        print("لطفاً عدد وارد کنید")

print(f"سن معتبر: {age}")
```

### سیستم منو
```python
def show_menu():
    print("۱. اضافه کردن آیتم")
    print("۲. حذف آیتم")
    print("۳. لیست آیتم‌ها")
    print("۴. خروج")

while True:
    show_menu()
    choice = input("گزینه را انتخاب کنید: ")

    if choice == "1":
        # منطق اضافه کردن آیتم
        pass
    elif choice == "2":
        # منطق حذف آیتم
        pass
    elif choice == "3":
        # منطق لیست آیتم‌ها
        pass
    elif choice == "4":
        break
    else:
        print("گزینه نامعتبر")
```

### پردازش مجموعه‌ها
```python
# پردازش آرایه با اقدامات مختلف
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        print(f"{num} زوج است")
    elif num % 3 == 0:
        print(f"{num} بر ۳ بخش‌پذیر است")
    else:
        print(f"{num} فرد است و بر ۳ بخش‌پذیر نیست")
```

## ساختارهای کنترلی در زبان‌های مختلف

### ساختارهای کنترلی Python
```python
# IF statement
if condition:
    # code
elif another_condition:
    # code
else:
    # code

# FOR loop
for item in iterable:
    # code

# WHILE loop
while condition:
    # code
```

### ساختارهای کنترلی JavaScript
```javascript
// IF statement
if (condition) {
    // code
} else if (another_condition) {
    // code
} else {
    // code
}

// FOR loop
for (let i = 0; i < 10; i++) {
    // code
}

// WHILE loop
while (condition) {
    // code
}
```

### ساختارهای کنترلی Java
```java
// IF statement
if (condition) {
    // code
} else if (another_condition) {
    // code
} else {
    // code
}

// FOR loop
for (int i = 0; i < 10; i++) {
    // code
}

// WHILE loop
while (condition) {
    // code
}
```

## اشتباهات رایج ساختار کنترلی

### خطاهای خارج از محدوده
```python
# اشتباه: حلقه ۱۱ بار اجرا می‌شود به جای ۱۰
for i in range(11):  # ۰ تا ۱۰ شامل
    print(i)

# درست: حلقه ۱۰ بار اجرا می‌شود
for i in range(10):  # ۰ تا ۹
    print(i)

# یا به طور واضح‌تر
for i in range(1, 11):  # ۱ تا ۱۰
    print(i)
```

### حلقه‌های بی‌نهایت
```python
# حلقه بی‌نهایت - شرط هرگز false نمی‌شود
while True:
    user_input = input("برای خروج 'quit' تایپ کنید: ")
    if user_input == "quit":
        break  # بدون این، حلقه هرگز تمام نمی‌شود

# حلقه بی‌نهایت دیگر
counter = 0
while counter < 10:
    print(counter)
    # فراموش کردن افزایش counter!
```

### مشکل else آویزان
```python
# else متعلق به کدام if است؟
if condition1:
    if condition2:
        statement1
else:  # متعلق به if داخلی است، نه بیرونی
    statement2

# با تورفتگی و آکولاد مناسب توضیح دهید
if condition1:
    if condition2:
        statement1
    else:
        statement2
```

### محدوده متغیر حلقه
```python
# در برخی زبان‌ها، متغیرهای حلقه به حلقه محدود می‌شوند
for (int i = 0; i < 10; i++) {
    // i فقط در این حلقه وجود دارد
}
// i اینجا در دسترس نیست
```

## ساختارهای کنترلی تودرتو

### حلقه‌های تودرتو
```python
# جدول ضرب
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i * j}")
    print()  # خط خالی پس از هر ردیف
```

### حلقه با انتخاب
```python
# پردازش نمرات دانش‌آموزان
grades = [85, 92, 78, 96, 88]
for grade in grades:
    if grade >= 90:
        print(f"{grade}: A")
    elif grade >= 80:
        print(f"{grade}: B")
    elif grade >= 70:
        print(f"{grade}: C")
    else:
        print(f"{grade}: D")
```

### انتخاب با حلقه‌ها
```python
# پردازش مختلف بر اساس انتخاب کاربر
choice = input("انتخاب کنید: (۱) مجموع (۲) حاصل‌ضرب: ")

if choice == "1":
    total = 0
    for num in numbers:
        total += num
    print(f"مجموع: {total}")
elif choice == "2":
    product = 1
    for num in numbers:
        product *= num
    print(f"حاصل‌ضرب: {product}")
```

## روش‌های بهتر ساختار کنترلی

### قابلیت خواندن
- از نام‌های متغیر توصیفی و واضح استفاده کنید
- برای شرایط پیچیده کامنت اضافه کنید
- تورفتگی سازگار
- از ساختارهای تودرتو عمیق اجتناب کنید

### قابلیت نگهداری
- اصل مسئولیت واحد
- شرایط پیچیده را به توابع استخراج کنید
- از بازگشت‌های زودهنگام برای کاهش تودرتو استفاده کنید
- عمق حلقه را به ۲-۳ سطح محدود کنید

### عملکرد
- از کار غیرضروری در حلقه‌ها اجتناب کنید
- از انواع حلقه مناسب استفاده کنید
- برای کد حیاتی عملکرد، از باز کردن حلقه در نظر بگیرید
- در صورت امکان زود بشکنید

### مدیریت خطا
- ورودی‌ها را قبل از پردازش اعتبارسنجی کنید
- موارد لبه را در شرایط مدیریت کنید
- از try-catch برای خطاهای غیرمنتظره استفاده کنید
- پیام‌های خطای معنادار ارائه دهید

## نکات کلیدی

۱. **سه ساختار اساسی تمام نیازهای برنامه‌نویسی را پوشش می‌دهند**: توالی، انتخاب و تکرار
۲. **انتخاب جریان را از طریق تصمیم‌ها کنترل می‌کند**: ساختارهای IF-ELSE شرایط مختلف را مدیریت می‌کنند
۳. **تکرار امکان تکرار را فراهم می‌کند**: حلقه‌ها مجموعه‌ها را پردازش می‌کنند و اقدامات را تکرار می‌کنند
۴. **کنترل جریان اجرای برنامه را هدایت می‌کند**: برنامه‌ها می‌توانند به شرایط مختلف پاسخ دهند
۵. **ساختار مناسب کد را بهبود می‌بخشد**: خوانا، قابل نگهداری و صحیح

## مطالعه بیشتر
- اصول برنامه‌نویسی ساخت‌یافته را مطالعه کنید
- ساختارهای کنترلی در زبان‌های مختلف را بیاموزید
- الگوهای جریان کنترلی پیشرفته را کاوش کنید
- نمودارهای جریان و تحلیل برنامه را درک کنید