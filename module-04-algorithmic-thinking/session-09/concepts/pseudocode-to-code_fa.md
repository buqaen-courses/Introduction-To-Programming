# شبه‌کد به کد: پیاده‌سازی الگوریتم‌ها

## فرآیند ترجمه

ترجمه شبه‌کد به کد برنامه‌نویسی واقعی شامل تبدیل منطق الگوریتمی به نحو زبان‌محور است و قصد و صحت اصلی را حفظ می‌کند.

## مراحل ترجمه گام به گام

### ۱. شبه‌کد را درک کنید
قبل از ترجمه، مطمئن شوید که کاملاً الگوریتم را درک کرده‌اید:

```pseudocode
ALGORITHM CalculateGrade
    READ score
    IF score >= 90 THEN
        grade ← "A"
    ELSE IF score >= 80 THEN
        grade ← "B"
    ELSE
        grade ← "D"
    END IF
    WRITE "Grade: " + grade
END ALGORITHM
```

### ۲. انواع داده مناسب انتخاب کنید

مفاهیم شبه‌کد را به انواع زبان نگاشت کنید:
- اعداد → `int`, `float`
- متن → `string`, `str`
- درست/غلط → `boolean`, `bool`
- مجموعه‌ها → arrays, lists, dictionaries

### ۳. ساختارهای کنترلی را ترجمه کنید

#### ترجمه توالی
```pseudocode
READ name
READ age
WRITE "Hello " + name
```

```python
name = input("نام را وارد کنید: ")
age = int(input("سن را وارد کنید: "))
print(f"سلام {name}")
```

#### ترجمه انتخاب
```pseudocode
IF score >= 90 THEN
    grade ← "A"
ELSE IF score >= 80 THEN
    grade ← "B"
ELSE
    grade ← "D"
END IF
```

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "D"
```

#### ترجمه تکرار
```pseudocode
FOR i FROM 1 TO 10 DO
    WRITE i
END FOR
```

```python
for i in range(1, 11):
    print(i)
```

## مثال‌های ترجمه زبان‌محور

### Python Translation

#### متغیرها و تخصیص
```pseudocode
DECLARE x, y AS INTEGER
x ← 5
y ← x + 3
```

```python
# متغیرها در Python پویا هستند
x = 5
y = x + 3
```

#### توابع
```pseudocode
FUNCTION AddNumbers(a, b)
    RETURN a + b
END FUNCTION
```

```python
def add_numbers(a, b):
    return a + b

# استفاده
result = add_numbers(3, 5)
```

#### آرایه‌ها/لیست‌ها
```pseudocode
DECLARE numbers AS ARRAY[5] OF INTEGER
numbers[0] ← 10
numbers[1] ← 20
```

```python
numbers = [0] * 5  # ایجاد لیست ۵ تا صفر
numbers[0] = 10
numbers[1] = 20

# یا ساده‌تر
numbers = [10, 20, 0, 0, 0]
```

### JavaScript Translation

#### متغیرها
```javascript
// JavaScript از let/const/var استفاده می‌کند
let x = 5;
const PI = 3.14159;
```

#### توابع
```javascript
function addNumbers(a, b) {
    return a + b;
}

// تابع پیکان
const addNumbers = (a, b) => a + b;
```

#### آرایه‌ها
```javascript
let numbers = new Array(5);
numbers[0] = 10;
numbers[1] = 20;

// یا نحو literal
let numbers = [10, 20, 0, 0, 0];
```

### Java Translation

#### متغیرها با نوع
```java
// Java نیاز به انواع صریح دارد
int x = 5;
double pi = 3.14159;
String name = "علی";
```

#### متدها
```java
public static int addNumbers(int a, int b) {
    return a + b;
}
```

#### آرایه‌ها
```java
int[] numbers = new int[5];
numbers[0] = 10;
numbers[1] = 20;

// یا مقداردهی اولیه
int[] numbers = {10, 20, 0, 0, 0};
```

## ترجمه الگوریتم پیچیده

### الگوریتم جستجوی خطی

**شبه‌کد:**
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

**پیاده‌سازی Python:**
```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# استفاده
numbers = [10, 20, 30, 40, 50]
index = linear_search(numbers, 30)
print(f"در شاخص یافت شد: {index}")  # ۲
```

**پیاده‌سازی JavaScript:**
```javascript
function linearSearch(arr, target) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === target) {
            return i;
        }
    }
    return -1;
}

// استفاده
const numbers = [10, 20, 30, 40, 50];
const index = linearSearch(numbers, 30);
console.log(`در شاخص یافت شد: ${index}`);  // ۲
```

### الگوریتم مرتب‌سازی (حبابی)

**شبه‌کد:**
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

**پیاده‌سازی Python:**
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # جابجایی عناصر
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# استفاده
numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numbers)
print(numbers)  # [11, 12, 22, 25, 34, 64, 90]
```

### الگوریتم بازگشتی (فاکتوریل)

**شبه‌کد:**
```
FUNCTION Factorial(n)
    IF n = 0 OR n = 1 THEN
        RETURN 1
    ELSE
        RETURN n × Factorial(n - 1)
    END IF
END FUNCTION
```

**پیاده‌سازی Python:**
```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# استفاده
print(factorial(5))  # ۱۲۰
```

## مدیریت تفاوت‌های زبان

### الحاق رشته
```pseudocode
result ← "Hello" + name
```

```python
result = "Hello" + name
# یا
result = f"Hello {name}"
```

```javascript
result = "Hello" + name;
// یا
result = `Hello ${name}`;
```

```java
result = "Hello" + name;
// برای کارایی StringBuilder
StringBuilder sb = new StringBuilder();
sb.append("Hello");
sb.append(name);
result = sb.toString();
```

### عملیات آرایه/لیست
```pseudocode
DECLARE numbers AS LIST OF INTEGER
ADD 10 TO numbers
REMOVE 5 FROM numbers
```

```python
numbers = []
numbers.append(10)
numbers.remove(5)
# یا
numbers = [10, 20, 30]
numbers.pop(1)  # حذف با شاخص
```

```javascript
let numbers = [];
numbers.push(10);
numbers.splice(numbers.indexOf(5), 1);
// یا
let numbers = [10, 20, 30];
numbers.splice(1, 1);  // حذف در شاخص ۱
```

## مدیریت خطا در ترجمه

### اعتبارسنجی ورودی
```pseudocode
READ age
IF age < 0 OR age > 120 THEN
    WRITE "Invalid age"
    RETURN
END IF
```

```python
try:
    age = int(input("سن را وارد کنید: "))
    if age < 0 or age > 120:
        print("سن نامعتبر")
        return
except ValueError:
    print("لطفاً عدد وارد کنید")
    return
```

### مدیریت استثنا
```pseudocode
TRY
    result ← risky_operation()
    WRITE "Success: " + result
CATCH error
    WRITE "Error: " + error
END TRY
```

```python
try:
    result = risky_operation()
    print(f"موفقیت: {result}")
except Exception as error:
    print(f"خطا: {error}")
```

## آزمایش و اشکال‌زدایی

### تست واحد در ترجمه
```pseudocode
// تست تابع AddNumbers
test_result1 ← AddNumbers(2, 3) = 5
test_result2 ← AddNumbers(-1, 1) = 0
```

```python
def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    print("همه تست‌ها گذرانده شدند")

test_add_numbers()
```

### تکنیک‌های اشکال‌زدایی
```python
# چاپ‌های اشکال‌زدایی اضافه کنید
def factorial(n):
    print(f"محاسبه فاکتوریل({n})")
    if n == 0 or n == 1:
        print("مورد پایه: بازگشت ۱")
        return 1
    else:
        result = n * factorial(n - 1)
        print(f"فاکتوریل({n}) = {n} × فاکتوریل({n-1}) = {result}")
        return result

factorial(3)
```

## ملاحظات عملکرد

### بهینه‌سازی الگوریتم
```pseudocode
// ناکارآمد O(n²)
FOR i FROM 0 TO n-1 DO
    FOR j FROM 0 TO n-1 DO
        // عملیاتی
    END FOR
END FOR
```

```python
# کارآمدتر
# از توابع داخلی استفاده کنید
total = sum(numbers)

# از list comprehensions استفاده کنید
squares = [x**2 for x in numbers]

# از ساختارهای داده مناسب استفاده کنید
# دیکشنری برای جستجوی O(1) به جای جستجوی O(n)
```

### مدیریت حافظه
```pseudocode
// پردازش داده بزرگ
FOR each item IN large_dataset DO
    // پردازش آیتم
    // استفاده از حافظه با اندازه مجموعه داده رشد می‌کند
END FOR
```

```python
# در تکه‌ها پردازش کنید تا حافظه مدیریت شود
def process_large_dataset(dataset, chunk_size=1000):
    for i in range(0, len(dataset), chunk_size):
        chunk = dataset[i:i + chunk_size]
        process_chunk(chunk)
        # تکه خارج از محدوده می‌رود، حافظه آزاد می‌شود
```

## کیفیت کد و روش‌های بهتر

### مستندسازی
```python
def calculate_average(numbers):
    """
    میانگین حسابی لیستی از اعداد را محاسبه می‌کند.

    Args:
        numbers (list): لیست مقادیر عددی

    Returns:
        float: مقدار میانگین، یا ۰ اگر لیست خالی باشد

    Raises:
        TypeError: اگر ورودی لیست نباشد یا شامل مقادیر غیرعددی باشد
    """
    if not numbers:
        return 0.0

    total = sum(numbers)
    return total / len(numbers)
```

### سبک کد
```python
# خوب: واضح، خوانا
def is_even(number):
    return number % 2 == 0

# بد: گیج‌کننده، سخت خواندن
def ie(n):
    return n%2==0
```

### مدیریت خطا
```python
def divide_numbers(a, b):
    """تقسیم دو عدد به طور امن."""
    if b == 0:
        raise ValueError("تقسیم بر صفر امکان‌پذیر نیست")
    return a / b

# استفاده
try:
    result = divide_numbers(10, 0)
except ValueError as e:
    print(f"خطا: {e}")
```

## نکات کلیدی

۱. **شبه‌کد مستقل از زبان است**: ابتدا روی منطق تمرکز کنید، سپس ترجمه کنید
۲. **سازگاری‌های مناسب انتخاب کنید**: هر زبان idioms و بهترین روش‌های خود را دارد
۳. **به طور کامل آزمایش کنید**: مطمئن شوید ترجمه صحت الگوریتم را حفظ می‌کند
۴. **عملکرد را در نظر بگیرید**: ویژگی‌های زبان و کتابخانه‌ها روی کارایی تأثیر می‌گذارند
۵. **کد قابل نگهداری بنویسید**: کد واضح، مستند شده برای تغییر آسان‌تر است

## مطالعه بیشتر
- چندین زبان برنامه‌نویسی را بیاموزید تا رویکردهای مختلف را درک کنید
- روش‌های بهتر و idioms زبان‌محور را مطالعه کنید
- چارچوب‌های تست و ابزارهای اشکال‌زدایی را کاوش کنید
- تمرین ترجمه الگوریتم‌ها بین زبان‌های مختلف