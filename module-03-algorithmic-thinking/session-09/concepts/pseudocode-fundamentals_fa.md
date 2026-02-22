# مبانی شبه‌کد: پل بین الگوریتم‌ها و کد

## شبه‌کد چیست؟

شبه‌کد توصیف دقیقی از یک الگوریتم است که از ترکیبی از زبان طبیعی و ساختارهای شبیه به برنامه‌نویسی استفاده می‌کند. برای خواندن توسط انسان‌ها طراحی شده اما به اندازه کافی دقیق است تا به هر زبان برنامه‌نویسی ترجمه شود.

## چرا از شبه‌کد استفاده کنیم؟

### مزایا
- **مستقل از زبان**: می‌تواند در هر زبان برنامه‌نویسی پیاده‌سازی شود
- **تمرکز روی منطق**: از حواس‌پرتی‌های نحوی اجتناب می‌کند
- **آسانی تغییر**: ساده برای اصلاح و بهبود
- **ابزار ارتباطی**: راه واضحی برای به اشتراک گذاشتن الگوریتم‌ها
- **ابزار برنامه‌ریزی**: قبل از کد نویسی فکر کنید

### چه زمانی از شبه‌کد استفاده کنیم
- طراحی الگوریتم‌ها قبل از پیاده‌سازی
- توضیح الگوریتم‌ها به دیگران
- برنامه‌ریزی برنامه‌های پیچیده
- آموزش مفاهیم برنامه‌نویسی
- مستندسازی راه‌حل‌های الگوریتمی

## ساختار شبه‌کد

### عناصر پایه

#### متغیرها و تخصیص
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

#### ساختار مدولار
```
FUNCTION function_name(parameters)
    // Function body
    RETURN result
END FUNCTION

PROCEDURE procedure_name(parameters)
    // Procedure body
END PROCEDURE
```

## ساختارهای کنترلی در شبه‌کد

### توالی
**تعریف**: عبارت‌ها را به ترتیب اجرا کن، یکی پس از دیگری.

**شبه‌کد:**
```
statement1
statement2
statement3
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
    true_statements
ELSE
    false_statements
END IF
```

#### IF تودرتو
```
IF outer_condition THEN
    IF inner_condition THEN
        statement(s)
    END IF
END IF
```

#### انتخاب چندگانه (IF-ELSEIF)
```
IF condition1 THEN
    statements1
ELSE IF condition2 THEN
    statements2
ELSE IF condition3 THEN
    statements3
ELSE
    default_statements
END IF
```

### تکرار (حلقه)

#### حلقه پیش‌تست (WHILE)
```
WHILE condition DO
    statement(s)
END WHILE
```

#### حلقه پس‌تست (REPEAT-UNTIL)
```
REPEAT
    statement(s)
UNTIL condition
```

#### حلقه شمارش‌شده (FOR)
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
BREAK    // فوراً از حلقه خارج شود
CONTINUE // به تکرار بعدی برود
```

## مثال‌های شبه‌کد

### محاسبه ساده
```
ALGORITHM CalculateAverage
    // محاسبه میانگین سه عدد

    DECLARE num1, num2, num3, average AS REAL

    WRITE "Enter three numbers:"
    READ num1
    READ num2
    READ num3

    average ← (num1 + num2 + num3) / 3

    WRITE "Average is: " + average
END ALGORITHM
```

### تصمیم‌گیری
```
ALGORITHM CheckGrade
    // تعیین نمره حرف از امتیاز

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
END ALGORITHM
```

### حلقه
```
ALGORITHM SumNumbers
    // مجموع اعداد از ۱ تا n

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
END ALGORITHM
```

### الگوریتم پیچیده
```
ALGORITHM FindMaximum
    // یافتن مقدار حداکثر در آرایه

    DECLARE array AS ARRAY OF INTEGER
    DECLARE max_value, i AS INTEGER
    DECLARE size AS INTEGER

    // Assume array is initialized
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
END ALGORITHM
```

## ساختارهای داده در شبه‌کد

### آرایه‌ها
```
DECLARE numbers AS ARRAY[10] OF INTEGER
numbers[0] ← 10
numbers[1] ← 20

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
student.name ← "علی"
student.age ← 20
student.grade ← 95.5
```

### لیست‌ها/مجموعه‌ها
```
DECLARE names AS LIST OF STRING
ADD "علی" TO names
ADD "رضا" TO names
REMOVE "علی" FROM names

FOR each name IN names DO
    WRITE name
END FOR
```

## توابع و رویه‌ها

### تابع با مقدار بازگشتی
```
FUNCTION CalculateArea(length, width)
    // Calculate rectangle area
    RETURN length × width
END FUNCTION

// Usage
area ← CalculateArea(5, 3)
WRITE "Area: " + area
```

### رویه (بدون مقدار بازگشتی)
```
PROCEDURE PrintGreeting(name)
    WRITE "Hello, " + name + "!"
    WRITE "Welcome to our program."
END PROCEDURE

// Usage
PrintGreeting("علی")
```

### تابع بازگشتی
```
FUNCTION Factorial(n)
    // Calculate n!
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
        RETURN 0  // Or some error value
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

## کامنت‌ها و مستندسازی

### کامنت‌های درون خطی
```
total ← 0  // Initialize sum variable
count ← 0  // Initialize counter
```

### کامنت‌های بلوکی
```
/*
 * This function calculates the average of an array
 * Input: array of numbers
 * Output: average value
 */
FUNCTION CalculateAverage(numbers)
    // Implementation here
END FUNCTION
```

## روش‌های بهتر برای شبه‌کد

### وضوح
- از نام‌های متغیر معنادار استفاده کنید
- در مورد عملیات‌ها خاص باشید
- کامنت‌هایی برای منطق پیچیده اضافه کنید

### سازگاری
- از تورفتگی سازگار استفاده کنید
- از کنوانسیون‌های نام‌گذاری سازگار پیروی کنید
- از فرمت‌های ساختار کنترلی استاندارد استفاده کنید

### کامل بودن
- تمام موارد ممکن را مدیریت کنید
- شرایط خطا را شامل شود
- الزامات ورودی/خروجی را مشخص کنید

### استقلال از زبان
- از نحو زبان برنامه‌نویسی خاص استفاده نکنید
- از سازه‌های عمومی استفاده کنید
- روی منطق الگوریتمی تمرکز کنید

## الگوهای شبه‌کد رایج

### جستجوی خطی
```
FUNCTION LinearSearch(array, target)
    FOR i FROM 0 TO LENGTH(array) - 1 DO
        IF array[i] = target THEN
            RETURN i
        END IF
    END FOR
    RETURN -1
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

### جستجوی باینری
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

    RETURN -1  // Not found
END FUNCTION
```

## نکات کلیدی

۱. **شبه‌کد مستندسازی الگوریتم است**: به اندازه کافی دقیق برای پیاده‌سازی، به اندازه کافی خوانا برای انسان‌ها
۲. **ساختارهای کنترلی اساسی هستند**: توالی، انتخاب و تکرار تمام نیازهای برنامه‌نویسی را پوشش می‌دهند
۳. **طراحی مستقل از زبان**: روی منطق تمرکز کن، نه نحو
۴. **آسانی اصلاح و بهبود**: ساده برای بهبود الگوریتم‌ها قبل از کد نویسی
۵. **پل بین تفکر و کد نویسی**: ایده‌ها را به شکل ساخت‌یافته تبدیل می‌کند

## مطالعه بیشتر
- اصول برنامه‌نویسی ساخت‌یافته را مطالعه کنید
- تکنیک‌های طراحی الگوریتم را بیاموزید
- کنوانسیون‌های مختلف شبه‌کد را کاوش کنید
- تمرین ترجمه شبه‌کد به زبان‌های برنامه‌نویسی مختلف