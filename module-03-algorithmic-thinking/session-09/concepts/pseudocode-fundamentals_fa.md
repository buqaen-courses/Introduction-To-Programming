# اصول شبه‌کد: پلی بین الگوریتم و کد

## شبه‌کد چیست؟

شبه‌کد توصیف دقیق و ساختاریافته یک الگوریتم با استفاده از ترکیبی از زبان طبیعی و ساختارهای شبیه برنامه‌نویسی است. طراحی شده برای خوانایی انسان در حالی که دقیق‌ترین برای ترجمه به هر زبان برنامه‌نویسی است.

## چرا از شبه‌کد استفاده کنیم؟

### مزایا
- **مستقل از زبان**: می‌تواند در هر زبان برنامه‌نویسی پیاده‌سازی شود
- **تمرکز روی منطق**: از حواس‌پرتی‌های نحوی اجتناب می‌کند
- **راحتی تغییر**: تغییر و اصلاح ساده
- **ابزار ارتباطی**: راه واضح برای اشتراک الگوریتم‌ها
- **ابزار برنامه‌ریزی**: قبل از کدنویسی منطق را بررسی کنید

### چه موقع از شبه‌کد استفاده کنیم
- طراحی الگوریتم‌ها قبل از پیاده‌سازی
- توضیح الگوریتم‌ها به دیگران
- برنامه‌ریزی برنامه‌های پیچیده
- آموزش مفاهیم برنامه‌نویسی
- مستندسازی راه‌حل‌های الگوریتمی

## ساختار شبه‌کد

### عناصر پایه

#### متغیرها و انتساب
```
SET variable_name TO value
variable_name ← value
```

#### ورودی/خروجی
```
READ variable_name
WRITE "message" OR variable_name
DISPLAY result
INPUT user_response
```

#### عملیات ریاضی
```
result ← a + b
product ← x × y
quotient ← dividend / divisor
remainder ← dividend MOD divisor
```

### ساختار برنامه

#### ساختار ترتیبی
```
Step 1: Do something
Step 2: Do next thing
Step 3: Do final thing
```

#### ساختار ماژولار
```
FUNCTION function_name(parameters)
    // Function body
    RETURN result
END FUNCTION

PROCEDURE procedure_name(parameters)
    // Procedure body
END PROCEDURE
```

## ساختارهای کنترل در شبه‌کد

### ترتیب
**تعریف**: اجرای دستورات به ترتیب، یکی پس از دیگری.

```
BEGIN
    READ number1
    READ number2
    sum ← number1 + number2
    WRITE "Sum is: " + sum
END
```

### انتخاب (تصمیم‌گیری)

#### IF ساده
```
IF condition THEN
    statement(s)
END IF
```

#### IF-ELSE
```
IF condition THEN
    statement(s) for true case
ELSE
    statement(s) for false case
END IF
```

#### IF تودرتو
```
IF condition1 THEN
    IF condition2 THEN
        statement(s)
    END IF
ELSE
    statement(s)
END IF
```

#### انتخاب چندگانه (IF-ELSEIF)
```
IF condition1 THEN
    statement(s) 1
ELSE IF condition2 THEN
    statement(s) 2
ELSE IF condition3 THEN
    statement(s) 3
ELSE
    default statement(s)
END IF
```

### تکرار (حلقه)

#### حلقه پیش‌آزمون (WHILE)
```
WHILE condition DO
    statement(s)
END WHILE
```

#### حلقه پس‌آزمون (REPEAT-UNTIL)
```
REPEAT
    statement(s)
UNTIL condition
```

#### حلقه شمارشی (FOR)
```
FOR counter FROM start TO end DO
    statement(s)
END FOR

FOR each item IN collection DO
    statement(s)
END FOR
```

#### کنترل حلقه
```
BREAK    // خروج فوری از حلقه
CONTINUE // پرش به تکرار بعدی
```

## مثال‌های شبه‌کد

### محاسبه ساده
```
الگوریتم CalculateAverage
    // محاسبه میانگین سه عدد

    DECLARE num1, num2, num3, average AS REAL

    WRITE "Enter three numbers:"
    READ num1
    READ num2
    READ num3

    average ← (num1 + num2 + num3) / 3

    WRITE "Average is: " + average
END الگوریتم
```

### تصمیم‌گیری
```
الگوریتم CheckGrade
    // تعیین نمره حرفی از نمره عددی

    DECLARE score AS INTEGER
    DECLARE grade AS STRING

    WRITE "Enter score (0-100):"
    READ score

    IF score >= 90 THEN
        grade ← "A"
    ELSE IF score >= 80 THEN
        grade ← "B"
    ELSE IF score >= 70 THEN
        grade ← "C"
    ELSE IF score >= 60 THEN
        grade ← "D"
    ELSE
        grade ← "F"
    END IF

    WRITE "Grade: " + grade
END الگوریتم
```

### حلقه
```
الگوریتم SumNumbers
    // جمع اعداد از ۱ تا n

    DECLARE n, sum, counter AS INTEGER

    WRITE "Enter n:"
    READ n

    sum ← 0
    counter ← 1

    WHILE counter <= n DO
        sum ← sum + counter
        counter ← counter + 1
    END WHILE

    WRITE "Sum is: " + sum
END الگوریتم
```

### الگوریتم پیچیده
```
الگوریتم FindMaximum
    // یافتن بزرگ‌ترین مقدار در آرایه

    DECLARE array AS ARRAY OF INTEGER
    DECLARE max_value, i AS INTEGER
    DECLARE size AS INTEGER

    // فرض کنید آرایه مقداردهی شده است
    size ← LENGTH(array)

    IF size = 0 THEN
        WRITE "Array is empty"
        RETURN
    END IF

    max_value ← array[0]

    FOR i FROM 1 TO size-1 DO
        IF array[i] > max_value THEN
            max_value ← array[i]
        END IF
    END FOR

    WRITE "Maximum value: " + max_value
END الگوریتم
```

## ساختارهای داده در شبه‌کد

### آرایه‌ها
```
DECLARE numbers AS ARRAY[10] OF INTEGER
numbers[0] ← 5
numbers[1] ← 10

FOR i FROM 0 TO 9 DO
    numbers[i] ← i * 2
END FOR
```

### رکوردها/ساختارها
```
TYPE Student RECORD
    name AS STRING
    age AS INTEGER
    grade AS REAL
END RECORD

DECLARE student AS Student
student.name ← "Alice"
student.age ← 20
student.grade ← 95.5
```

### لیست‌ها/مجموعه‌ها
```
DECLARE names AS LIST OF STRING
ADD "Alice" TO names
ADD "Bob" TO names
REMOVE "Alice" FROM names

FOR each name IN names DO
    WRITE name
END FOR
```

## توابع و روال‌ها

### تابع با مقدار برگشتی
```
FUNCTION CalculateArea(length, width)
    // محاسبه مساحت مستطیل
    RETURN length × width
END FUNCTION

// استفاده
area ← CalculateArea(5, 3)
WRITE "Area: " + area
```

### روال (بدون مقدار برگشتی)
```
PROCEDURE PrintGreeting(name)
    WRITE "Hello, " + name + "!"
    WRITE "Welcome to our program."
END PROCEDURE

// استفاده
PrintGreeting("Alice")
```

### تابع بازگشتی
```
FUNCTION Factorial(n)
    // محاسبه n!
    IF n = 0 OR n = 1 THEN
        RETURN 1
    ELSE
        RETURN n × Factorial(n - 1)
    END IF
END FUNCTION
```

## مدیریت خطا در شبه‌کد

### بررسی خطای پایه
```
FUNCTION SafeDivide(dividend, divisor)
    IF divisor = 0 THEN
        WRITE "Error: Division by zero"
        RETURN 0  // یا مقدار خطای دیگر
    ELSE
        RETURN dividend / divisor
    END IF
END FUNCTION
```

### اعتبارسنجی ورودی
```
PROCEDURE GetValidAge()
    DECLARE age AS INTEGER

    REPEAT
        WRITE "Enter age (0-120):"
        READ age

        IF age < 0 OR age > 120 THEN
            WRITE "Invalid age. Please try again."
        END IF
    UNTIL age >= 0 AND age <= 120

    RETURN age
END PROCEDURE
```

## توضیحات و مستندسازی

### توضیحات درون‌خطی
```
total ← 0  // مقداردهی اولیه متغیر sum
count ← 0  // مقداردهی اولیه شمارنده
```

### توضیحات بلوکی
```
/*
 * این تابع میانگین یک آرایه را محاسبه می‌کند
 * ورودی: آرایه اعداد
 * خروجی: مقدار میانگین
 */
FUNCTION CalculateAverage(numbers)
    // پیاده‌سازی اینجا
END FUNCTION
```

## بهترین شیوه‌ها برای شبه‌کد

### وضوح
- استفاده از نام‌های متغیر معنی‌دار
- مشخص بودن درباره عملیات
- افزودن توضیحات برای منطق پیچیده

### ثبات
- استفاده از تورفتگی مناسب
- پیروی از قراردادهای نام‌گذاری مداوم
- استفاده از فرمت‌های استاندارد ساختار کنترل

### کامل بودن
- مدیریت همه موارد ممکن
- شامل کردن شرایط خطا
- مشخص کردن نیازمندی‌های ورودی/خروجی

### مستقل از زبان
- اجتناب از نحو خاص زبان برنامه‌نویسی
- استفاده از ساختارهای عمومی
- تمرکز روی منطق الگوریتمی

## ترجمه شبه‌کد به کد

### پیاده‌سازی Python
```
# شبه‌کد
IF score >= 90 THEN
    grade ← "A"
ELSE IF score >= 80 THEN
    grade ← "B"
END IF

# Python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
```

### پیاده‌سازی JavaScript
```
# شبه‌کد
FOR i FROM 0 TO 9 DO
    WRITE i
END FOR

// JavaScript
for (let i = 0; i < 10; i++) {
    console.log(i);
}
```

## الگوهای رایج شبه‌کد

### جستجوی خطی
```
FUNCTION LinearSearch(array, target)
    FOR i FROM 0 TO LENGTH(array) - 1 DO
        IF array[i] = target THEN
            RETURN i
        END IF
    END FOR
    RETURN -1  // پیدا نشد
END FUNCTION
```

### مرتب‌سازی حبابی
```
PROCEDURE BubbleSort(array)
    DECLARE n AS INTEGER
    n ← LENGTH(array)

    FOR i FROM 0 TO n-2 DO
        FOR j FROM 0 TO n-i-2 DO
            IF array[j] > array[j+1] THEN
                SWAP array[j] AND array[j+1]
            END IF
        END FOR
    END FOR
END PROCEDURE
```

### جستجوی دودویی
```
FUNCTION BinarySearch(array, target)
    DECLARE left, right, mid AS INTEGER
    left ← 0
    right ← LENGTH(array) - 1

    WHILE left <= right DO
        mid ← (left + right) / 2

        IF array[mid] = target THEN
            RETURN mid
        ELSE IF array[mid] < target THEN
            left ← mid + 1
        ELSE
            right ← mid - 1
        END IF
    END WHILE

    RETURN -1  // پیدا نشد
END FUNCTION
```

## نکات کلیدی

1. **شبه‌کد مستندسازی الگوریتم است**: دقیق‌ترین برای پیاده‌سازی، خواناترین برای انسان
2. **ساختارهای کنترل بنیادی**: ترتیب، انتخاب، و تکرار همه نیازهای برنامه‌نویسی را پوشش می‌دهند
3. **طراحی مستقل از زبان**: تمرکز روی منطق، نه نحو
4. **راحتی اصلاح و بهبود**: ساده برای بهبود الگوریتم‌ها قبل از کدنویسی
5. **پل بین فکر و کد**: تبدیل ایده‌ها به شکل ساختاریافته

## مطالعه بیشتر
- مطالعه اصول برنامه‌نویسی ساختاریافته
- یادگیری درباره تکنیک‌های طراحی الگوریتم
- بررسی قراردونده‌های مختلف شبه‌کد
- تمرین ترجمه شبه‌کد به زبان‌های برنامه‌نویسی مختلف
