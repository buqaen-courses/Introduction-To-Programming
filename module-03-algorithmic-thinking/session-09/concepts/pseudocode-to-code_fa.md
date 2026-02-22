# از شبه‌کد به کد: پیاده‌سازی الگوریتم‌ها

## فرآیند ترجمه

ترجمه شبه‌کد به کد واقعی برنامه‌نویسی شامل تبدیل منطق الگوریتمی به نحو زبان‌خاص در حالی که قصد و صحت اصلی حفظ می‌شود.

## ترجمه گام‌به‌گام

### ۱. درک شبه‌کد
قبل از ترجمه، اطمینان حاصل کنید که کاملاً الگوریتم را درک می‌کنید:

```pseudocode
ALGORITHM CalculateGrade
    READ score
    IF score >= 90 THEN
        grade ← "A"
    ELSE IF score >= 80 THEN
        grade ← "B"
    ELSE IF score >= 70 THEN
        grade ← "C"
    ELSE
        grade ← "D"
    END IF
    WRITE "Grade: " + grade
END ALGORITHM
```

### ۲. انتخاب انواع داده مناسب

نگاشت مفاهیم شبه‌کد به انواع زبان:
- اعداد → `int`، `float`
- متن → `string`، `str`
- درست/نادرست → `boolean`، `bool`
- مجموعه‌ها → آرایه‌ها، لیست‌ها، دیکشنری‌ها

### ۳. ترجمه ساختارهای کنترل

#### ترجمه ترتیب
```pseudocode
READ name
READ age
WRITE "Hello " + name
```

```python
name = input("Enter name: ")
age = int(input("Enter age: "))
print(f"Hello {name}")
```

#### ترجمه انتخاب
```pseudocode
IF score >= 90 THEN
    grade ← "A"
ELSE IF score >= 80 THEN
    grade ← "B"
ELSE
    grade ← "F"
END IF
```

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "F"
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

## مثال‌های ترجمه زبان‌خاص

### ترجمه Python

#### متغیرها و انتساب
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
numbers = [0] * 5  # ایجاد لیست با ۵ صفر
numbers[0] = 10
numbers[1] = 20

# یا ساده‌تر
numbers = [10, 20, 0, 0, 0]
```

### ترجمه JavaScript

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

// Arrow function
const addNumbers = (a, b) => a + b;
```

#### آرایه‌ها
```javascript
let numbers = new Array(5);
numbers[0] = 10;
numbers[1] = 20;

// یا syntax literal
let numbers = [10, 20, 0, 0, 0];
```

### ترجمه Java

#### متغیرها با انواع
```java
// Java نیاز به انواع صریح دارد
int x = 5;
double pi = 3.14159;
String name = "Alice";
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
print(f"Found at index: {index}")  # 2
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
console.log(`Found at index: ${index}`);  // 2
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
print(factorial(5))  # 120
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
// StringBuilder برای کارایی
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

## ترجمه مدیریت خطا

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
    age = int(input("Enter age: "))
    if age < 0 or age > 120:
        print("Invalid age")
        return
except ValueError:
    print("Please enter a number")
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
    print(f"Success: {result}")
except Exception as error:
    print(f"Error: {error}")
```

## آزمایش و اشکال‌زدایی

### آزمایش واحد ترجمه
```pseudocode
// تابع AddNumbers را آزمایش کنید
test_result1 ← AddNumbers(2, 3) = 5
test_result2 ← AddNumbers(-1, 1) = 0
```

```python
def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    print("All tests passed")

test_add_numbers()
```

### تکنیک‌های اشکال‌زدایی
```python
# افزودن printهای اشکال‌زدایی
def factorial(n):
    print(f"Computing factorial({n})")
    if n == 0 or n == 1:
        print(f"Base case: returning 1")
        return 1
    else:
        result = n * factorial(n - 1)
        print(f"factorial({n}) = {n} * factorial({n-1}) = {result}")
        return result

factorial(3)
```

## ملاحظات کارایی

### بهینه‌سازی الگوریتم
```pseudocode
// ناکارآمد O(n²)
FOR i FROM 0 TO n-1 DO
    FOR j FROM 0 TO n-1 DO
        // Some operation
    END FOR
END FOR
```

```python
# رویکردهای کارآمدتر
# استفاده از توابع داخلی
total = sum(numbers)

# استفاده از list comprehensions
squares = [x**2 for x in numbers]

# استفاده از ساختارهای داده مناسب
# دیکشنری برای جستجوهای O(1) به جای جستجوهای O(n)
```

### مدیریت حافظه
```pseudocode
// پردازش داده بزرگ
FOR each item IN large_dataset DO
    // Process item
    // Memory usage grows with dataset size
END FOR
```

```python
# پردازش به قطعات برای مدیریت حافظه
def process_large_dataset(dataset, chunk_size=1000):
    for i in range(0, len(dataset), chunk_size):
        chunk = dataset[i:i + chunk_size]
        process_chunk(chunk)
        # Chunk از scope خارج می‌شود، حافظه آزاد می‌شود
```

## کیفیت کد و بهترین شیوه‌ها

### مستندسازی
```python
def calculate_average(numbers):
    """
    Calculate the arithmetic mean of a list of numbers.

    Args:
        numbers (list): List of numeric values

    Returns:
        float: Average value, or 0 if list is empty

    Raises:
        TypeError: If input is not a list or contains non-numeric values
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

# اجتناب: گیج‌کننده، خواندن سخت
def ie(n):
    return n%2==0
```

### مدیریت خطا
```python
def divide_numbers(a, b):
    """Divide two numbers safely."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# استفاده
try:
    result = divide_numbers(10, 0)
except ValueError as e:
    print(f"Error: {e}")
```

## نکات کلیدی

1. **شبه‌کد مستقل از زبان است**: ابتدا روی منطق تمرکز کنید، سپس ترجمه کنید
2. **ساختارهای مناسب انتخاب کنید**: هر زبان ایدیوم‌ها و بهترین شیوه‌های خود را دارد
3. **آزمایش کامل**: اطمینان حاصل کنید که ترجمه صحت الگوریتم را حفظ می‌کند
4. **کارایی را در نظر بگیرید**: ویژگی‌ها و کتابخانه‌های زبان بر کارایی تأثیر می‌گذارند
5. **کد قابل نگهداری بنویسید**: کد واضح و مستند شده اصلاح آن را آسان‌تر می‌کند

## مطالعه بیشتر
- مطالعه زبان‌های برنامه‌نویسی متعدد برای درک رویکردهای مختلف
- یادگیری درباره ایدیوم‌ها و بهترین شیوه‌های زبان‌خاص
- بررسی چارچوب‌های آزمایش و ابزارهای اشکال‌زدایی
- تمرین ترجمه الگوریتم‌ها بین زبان‌های مختلف
