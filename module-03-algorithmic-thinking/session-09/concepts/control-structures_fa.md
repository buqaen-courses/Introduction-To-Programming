# ساختارهای کنترل: هدایت جریان برنامه

## ساختارهای کنترل چیستند؟

ساختارهای کنترل ترتیب اجرای دستورات در یک برنامه را تعیین می‌کنند. آنها به برنامه‌ها اجازه می‌دهند تصمیم بگیرند، اقدامات را تکرار کنند، و به شرایط مختلف پاسخ دهند.

## سه ساختار کنترل بنیادی

### ۱. ترتیب (Sequence)
**تعریف**: اجرای دستورات به ترتیب، یکی پس از دیگری.

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
name = "Alice"
greeting = "Hello, " + name
print(greeting)

# JavaScript
let name = "Alice";
let greeting = "Hello, " + name;
console.log(greeting);

# Java
String name = "Alice";
String greeting = "Hello, " + name;
System.out.println(greeting);
```

### ۲. انتخاب (تصمیم‌گیری)
**تعریف**: انتخاب بین مسیرهای مختلف بر اساس شرایط.

**نماد فلوچارت**: لوزی

#### IF ساده
```
IF condition THEN
    statements
END IF
```

```python
# بررسی اگر عدد مثبت است
if number > 0:
    print("Number is positive")
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
# بررسی قبول/مردود
if score >= 60:
    print("Pass")
else:
    print("Fail")
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
# محاسبه‌گر نمره
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

#### دستورات IF تودرتو
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
        print("Can drive")
    else:
        print("Needs license")
else:
    print("Too young")
```

### ۳. تکرار (حلقه)
**تعریف**: تکرار دستورات چندین بار.

**نماد فلوچارت**: مستطیل با پایین منحنی

#### حلقه پیش‌آزمون (WHILE)
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

#### حلقه پس‌آزمون (DO-WHILE/REPEAT-UNTIL)
```
REPEAT
    statements
UNTIL condition
```

```python
# پیاده‌سازی Python (با استفاده از while True)
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break
    print(f"You entered: {user_input}")
```

#### حلقه شمارشی (FOR)
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
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

## ساختارهای کنترل پیشرفته

### دستورات کنترل حلقه

#### BREAK
خروج فوری از حلقه:
```python
# یافتن اولین عدد زوج
numbers = [1, 3, 5, 6, 8, 9]
for num in numbers:
    if num % 2 == 0:
        print(f"First even: {num}")
        break
```

#### CONTINUE
پرش به تکرار بعدی:
```python
# چاپ فقط اعداد فرد
for num in range(10):
    if num % 2 == 0:
        continue
    print(num)
```

#### ELSE در حلقه‌ها
اجرا وقتی حلقه به طور عادی تکمیل می‌شود:
```python
# جستجو با نشان دادن نتیجه
def find_item(items, target):
    for item in items:
        if item == target:
            print(f"Found {target}")
            break
    else:
        print(f"{target} not found")
```

### Switch/Case (در بعضی زبان‌ها)
انتخاب چندگانه بر اساس مقدار:
```javascript
// JavaScript
switch (grade) {
    case 'A':
        console.log("Excellent");
        break;
    case 'B':
        console.log("Good");
        break;
    case 'C':
        console.log("Average");
        break;
    default:
        console.log("Needs improvement");
}
```

## الگوهای ساختار کنترل

### حلقه اعتبارسنجی ورودی
```python
# تا دریافت ورودی معتبر ادامه بده
while True:
    try:
        age = int(input("Enter age: "))
        if age >= 0 and age <= 120:
            break
        else:
            print("Age must be between 0 and 120")
    except ValueError:
        print("Please enter a valid number")

print(f"Valid age: {age}")
```

### سیستم منو
```python
def show_menu():
    print("1. Add item")
    print("2. Remove item")
    print("3. List items")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose option: ")

    if choice == "1":
        # منطق افزودن آیتم
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
        print("Invalid choice")
```

### پردازش مجموعه‌ها
```python
# پردازش لیست با اقدامات مختلف
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    elif num % 3 == 0:
        print(f"{num} is divisible by 3")
    else:
        print(f"{num} is odd and not divisible by 3")
```

## جریان کنترل در زبان‌های مختلف

### ساختارهای کنترل Python
```python
# دستور IF
if condition:
    # code
elif another_condition:
    # code
else:
    # code

# حلقه FOR
for item in iterable:
    # code

# حلقه WHILE
while condition:
    # code
```

### ساختارهای کنترل JavaScript
```javascript
// دستور IF
if (condition) {
    // code
} else if (another_condition) {
    // code
} else {
    // code
}

// حلقه FOR
for (let i = 0; i < 10; i++) {
    // code
}

// حلقه WHILE
while (condition) {
    // code
}
```

### ساختارهای کنترل Java
```java
// دستور IF
if (condition) {
    // code
} else if (another_condition) {
    // code
} else {
    // code
}

// حلقه FOR
for (int i = 0; i < 10; i++) {
    // code
}

// حلقه WHILE
while (condition) {
    // code
}
```

## اشتباهات رایج ساختار کنترل

### خطاهای off-by-one
```python
# اشتباه: حلقه ۱۱ بار به جای ۱۰ بار اجرا می‌شود
for i in range(11):  # ۰ تا ۱۰ شامل
    print(i)

# درست: حلقه ۱۰ بار اجرا می‌شود
for i in range(10):  # ۰ تا ۹
    print(i)

# یا صریح‌تر
for i in range(1, 11):  # ۱ تا ۱۰
    print(i)
```

### حلقه‌های بی‌نهایت
```python
# حلقه بی‌نهایت - شرط هرگز false نمی‌شود
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break  # بدون این، حلقه هرگز تمام نمی‌شود

# حلقه بی‌نهایت دیگر
counter = 0
while counter < 10:
    print(counter)
    # فراموش کردن افزایش counter!
```

### مشکل ELSE معلق
```python
# ELSE متعلق به کدام IF است؟
if condition1:
    if condition2:
        statement1
else:  # متعلق به IF درونی است، نه بیرونی
    statement2

# با تورفتگی و آکولاد مناسب روشن کنید
if condition1:
    if condition2:
        statement1
    else:
        statement2
```

### محدوده متغیر حلقه
```python
# در بعضی زبان‌ها، متغیرهای حلقه در حلقه محدود می‌شوند
for (int i = 0; i < 10; i++) {
    // i فقط در این حلقه وجود دارد
}
// i اینجا قابل دسترسی نیست
```

## ساختارهای کنترل تودرتو

### حلقه‌های تودرتو
```python
# جدول ضرب
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i * j}")
    print()  # خط خالی پس از هر سطر
```

### حلقه با انتخاب
```python
# پردازش نمرات دانشجویان
grades = [85, 92, 78, 96, 88]
for grade in grades:
    if grade >= 90:
        print(f"{grade}: A")
    elif grade >= 80:
        print(f"{grade}: B")
    elif grade >= 70:
        print(f"{grade}: C")
    else:
        print(f"{grade}: F")
```

### انتخاب با حلقه‌ها
```python
# پردازش متفاوت بر اساس انتخاب کاربر
choice = input("Choose: (1) Sum (2) Product: ")

if choice == "1":
    total = 0
    for num in numbers:
        total += num
    print(f"Sum: {total}")
elif choice == "2":
    product = 1
    for num in numbers:
        product *= num
    print(f"Product: {product}")
```

## بهترین شیوه‌های ساختار کنترل

### خوانایی
- استفاده از نام‌های متغیر واضح و توصیفی
- افزودن توضیحات برای شرایط پیچیده
- تورفتگی مناسب
- اجتناب از ساختارهای عمیق تودرتو

### قابلیت نگهداری
- اصل تک مسئولیتی
- استخراج شرایط پیچیده به توابع
- استفاده از return زودهنگام برای کاهش تودرتویی
- محدود کردن عمق حلقه به ۲-۳ سطح

### عملکرد
- اجتناب از کار غیرضروری در حلقه‌ها
- استفاده از انواع حلقه مناسب
- در نظر گرفتن unrolling حلقه برای کد حساس به عملکرد
- BREAK زودهنگام وقتی ممکن است

### مدیریت خطا
- اعتبارسنجی ورودی‌ها قبل از پردازش
- مدیریت موارد خاص در شرایط
- استفاده از try-catch برای خطاهای غیرمنتظره
- ارائه پیام‌های خطای معنی‌دار

## نکات کلیدی

1. **سه ساختار بنیادی**: ترتیب، انتخاب، و تکرار همه نیازهای برنامه‌نویسی را پوشش می‌دهند
2. **انتخاب کنترل تصمیم‌ها**: ساختارهای IF-ELSE شرایط مختلف را مدیریت می‌کنند
3. **تکرار امکان تکرار را فراهم می‌کند**: حلقه‌ها مجموعه‌ها را پردازش و اقدامات را تکرار می‌کنند
4. **جریان کنترل اجرا را هدایت می‌کند**: برنامه‌ها می‌توانند به شرایط مختلف سازگار شوند
5. **ساختار مناسب برنامه را بهبود می‌بخشد**: برنامه‌های خوانا، قابل نگهداری، و صحیح

## مطالعه بیشتر
- مطالعه اصول برنامه‌نویسی ساختاریافته
- یادگیری درباره ساختارهای کنترل در زبان‌های مختلف
- بررسی الگوهای پیشرفته جریان کنترل
- درک نمودارهای جریان کنترل و تحلیل برنامه
