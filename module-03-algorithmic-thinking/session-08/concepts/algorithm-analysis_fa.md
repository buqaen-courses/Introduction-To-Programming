# تحلیل الگوریتم: اندازه‌گیری عملکرد و کارایی

## چرا الگوریتم‌ها را تحلیل کنیم؟

الگوریتم‌های مختلف مسئله‌ای یکسان را با کارایی متفاوت حل می‌کنند. تحلیل الگوریتم به ما کمک می‌کند تا ویژگی‌های عملکردی را قبل از پیاده‌سازی درک و مقایسه کنیم.

## تحلیل پیچیدگی زمانی

### نمادگذاری Big O

**تعریف**: توصیف می‌کند عملکرد الگوریتم چگونه با افزایش اندازه ورودی رشد می‌کند.

**تمرکز**: رفتار漸سن در بدترین حالت (وقتی اندازه ورودی به بی‌نهایت نزدیک می‌شود).

**پیچیدگی‌های رایج:**

| پیچیدگی | نام | مثال | توضیح |
|----------|-----|-------|--------|
| O(1) | ثابت | دسترسی آرایه | زمان یکسان صرف نظر از اندازه ورودی |
| O(log n) | لگاریتمی | جستجوی باینری | زمان دو برابر می‌شود وقتی اندازه ورودی دو برابر می‌شود |
| O(n) | خطی | جستجوی خطی | زمان متناسب با اندازه ورودی |
| O(n log n) | لگاریتمی-خطی | مرتب‌سازی ادغام | n × log n عملیات |
| O(n²) | درجه دو | مرتب‌سازی حبابی | زمان متناسب با مربع اندازه ورودی |
| O(2ⁿ) | نمایی | تولید زیرمجموعه | زمان برای هر عنصر ورودی اضافی دو برابر می‌شود |
| O(n!) | فاکتوریل | فروشنده دوره‌گرد (زورآزمایی) | رشد بسیار کند |

### تحلیل عملیات پایه

```python
# O(1) - زمان ثابت
def access_array_element(arr, index):
    return arr[index]  # همیشه زمان یکسانی می‌برد

# O(n) - زمان خطی
def find_maximum(arr):
    max_val = arr[0]
    for num in arr:        # حلقه n بار اجرا می‌شود
        if num > max_val:
            max_val = num
    return max_val

# O(n²) - زمان درجه دو
def bubble_sort(arr):
    for i in range(len(arr)):      # n بار
        for j in range(len(arr)-1): # n بار
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```

### تحلیل فراخوانی توابع

```python
# O(n) - حلقه واحد
def linear_search(arr, target):
    for item in arr:  # O(n)
        if item == target:
            return True
    return False

# O(n²) - حلقه‌های تودرتو
def has_duplicates(arr):
    for i in range(len(arr)):      # O(n)
        for j in range(i+1, len(arr)):  # O(n)
            if arr[i] == arr[j]:
                return True
    return False

# O(log n) - تقسیم و حل
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:  # O(log n) تکرار
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### تحلیل بازگشتی

```python
# O(2ⁿ) - نمایی
def fibonacci_bad(n):
    if n <= 1:
        return n
    return fibonacci_bad(n-1) + fibonacci_bad(n-2)  # دو فراخوانی بازگشتی

# O(n) - خطی با memoization
def fibonacci_good(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_good(n-1, memo) + fibonacci_good(n-2, memo)
    return memo[n]
```

## تحلیل پیچیدگی فضایی

### تعریف پیچیدگی فضایی

**تعریف**: چقدر فضای اضافی یک الگوریتم نسبت به اندازه ورودی استفاده می‌کند.

### مثال‌ها

```python
# O(1) - فضای ثابت
def sum_array(arr):
    total = 0        # متغیرهای O(1)
    for num in arr:  # فضای اضافی O(1)
        total += num
    return total

# O(n) - فضای خطی
def copy_array(arr):
    copy = []         # فضای O(n) برای کپی
    for item in arr:
        copy.append(item)
    return copy

# O(n²) - فضای درجه دو
def create_matrix(n):
    matrix = []       # فضای O(n²)
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        matrix.append(row)
    return matrix
```

### الگوریتم‌های درجا

```python
# O(1) فضای اضافی - درجا
def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]  # جابجایی درجا
        left += 1
        right -= 1
    # فضای اضافی تخصیص داده نشده

# O(n) فضا - غیر درجا
def reverse_array_copy(arr):
    result = []                    # فضای اضافی O(n)
    for i in range(len(arr)-1, -1, -1):
        result.append(arr[i])
    return result
```

## تحلیل بهترین، متوسط و بدترین حالت

### درک حالات مختلف

```python
# جستجوی خطی - حالات مختلف
def linear_search(arr, target):
    for i, item in enumerate(arr):
        if item == target:
            return i
    return -1

# بهترین حالت: O(1) - هدف اولین عنصر است
# حالت متوسط: O(n) - هدف در وسط است
# بدترین حالت: O(n) - هدف پیدا نشد یا آخرین عنصر است
```

### حالات جستجوی باینری

```python
# جستجوی باینری همیشه O(log n) در همه حالات است
# بهترین حالت: O(1) - هدف عنصر وسط است
# حالت متوسط: O(log n)
# بدترین حالت: O(log n) - هدف پیدا نشد
```

### حالات الگوریتم‌های مرتب‌سازی

```python
# مرتب‌سازی حبابی
# بهترین حالت: O(n) - از قبل مرتب شده
# حالت متوسط: O(n²)
# بدترین حالت: O(n²) - معکوس مرتب شده

# مرتب‌سازی سریع
# بهترین حالت: O(n log n) - پارتیشن‌های متعادل
# حالت متوسط: O(n log n)
# بدترین حالت: O(n²) - از قبل مرتب شده یا معکوس مرتب شده
```

## تحلیل amortized

### تعریف

**تحلیل amortized**: عملکرد متوسط روی دنباله‌ای از عملیات، حتی اگر عملیات‌های فردی گران باشند.

### مثال: آرایه‌های پویا

```python
class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.arr = [None] * self.capacity

    def append(self, value):
        if self.size == self.capacity:
            # دو برابر کردن ظرفیت - عملیات O(n)
            self.capacity *= 2
            new_arr = [None] * self.capacity
            for i in range(self.size):
                new_arr[i] = self.arr[i]
            self.arr = new_arr

        self.arr[self.size] = value
        self.size += 1

# append فردی: O(1) amortized، O(n) بدترین حالت
# دنباله n append: O(n) زمان amortized کل
```

## اندازه‌گیری عملکرد عملی

### benchmarking

```python
import time

def benchmark_algorithm(algorithm, *args, runs=10):
    times = []
    for _ in range(runs):
        start = time.time()
        result = algorithm(*args)
        end = time.time()
        times.append(end - start)

    avg_time = sum(times) / len(times)
    return avg_time, result

# مقایسه الگوریتم‌ها
arr = list(range(1000))

linear_time, _ = benchmark_algorithm(linear_search, arr, 999)
binary_time, _ = benchmark_algorithm(binary_search, sorted(arr), 999)

print(f"جستجوی خطی: {linear_time:.6f} ثانیه")
print(f"جستجوی باینری: {binary_time:.6f} ثانیه")
```

### ابزارهای profiling

```python
import cProfile

def profile_function(func, *args):
    profiler = cProfile.Profile()
    profiler.enable()
    result = func(*args)
    profiler.disable()
    profiler.print_stats(sort='cumulative')
    return result

# profile یک تابع
result = profile_function(my_algorithm, data)
```

## مقایسه الگوریتم‌ها

### عملکرد نظری در برابر عملی

```python
# نظری: O(n²) در برابر O(n log n)
# برای n=1000:
# O(n²): ۱,۰۰۰,۰۰۰ عملیات
# O(n log n): حدود ۱۰,۰۰۰ عملیات

# عملی: ثابت‌ها مهم هستند
# O(n²) با ثابت کوچک ممکن است O(n log n) با ثابت بزرگ را شکست دهد
# برای n کوچک
```

### انتخاب الگوریتم مناسب

**عوامل مورد توجه:**
- اندازه ورودی و محدودیت‌ها
- محدودیت‌های زمانی مورد نیاز
- حافظه موجود
- سهولت پیاده‌سازی
- قابلیت نگهداری کد

### راهنمای انتخاب الگوریتم

| نوع مسئله | ورودی کوچک (n<100) | ورودی متوسط (n<10,000) | ورودی بزرگ (n>10,000) |
|-----------|---------------------|-----------------------|----------------------|
| جستجو | جستجوی خطی | جستجوی باینری | جدول هش |
| مرتب‌سازی | مرتب‌سازی درج | مرتب‌سازی ادغام/سریع | مرتب‌سازی خارجی |
| کوتاه‌ترین مسیر | Floyd-Warshall | Dijkstra | A* با هیوریستیک |
| تطبیق | زورآزمایی | برنامه‌ریزی پویا | تقریب |

## کلاس‌های پیچیدگی رایج

### P (زمان چندجمله‌ای)
مسائلی که در زمان چندجمله‌ای حل می‌شوند: O(n^k) برای برخی ثابت k.

**مثال‌ها:** مرتب‌سازی، جستجو، کوتاه‌ترین مسیرها در گراف‌ها.

### NP (چندجمله‌ای غیرقطعی)
مسائلی که راه حل‌ها را می‌توان در زمان چندجمله‌ای تأیید کرد.

**مثال‌ها:** فروشنده دوره‌گرد، کوله‌پشتی، satisfiability بولی.

### NP-Complete
سخت‌ترین مسائل در NP - اگر هر کدام بتوانند در زمان چندجمله‌ای حل شوند، همه می‌توانند.

### NP-Hard
حداقل به اندازه NP-complete سخت هستند، ممکن است در NP نباشند.

## قضیه اصلی برای تقسیم و حل

### فرمول
برای بازگشت: T(n) = aT(n/b) + f(n)

**حالات:**
۱. اگر f(n) = O(n^(log_b a - ε))، پس T(n) = Θ(n^log_b a)
۲. اگر f(n) = Θ(n^log_b a)، پس T(n) = Θ(n^log_b a log n)
۳. اگر f(n) = Ω(n^(log_b a + ε))، پس T(n) = Θ(f(n))

### مثال‌ها

```python
# مرتب‌سازی ادغام: T(n) = 2T(n/2) + O(n)
# a=2, b=2, f(n)=n
# log_b a = log_2 2 = 1
# f(n) = Θ(n^1) = Θ(n^log_b a)
# حالت ۲: T(n) = Θ(n log n)

# درخت جستجوی باینری: T(n) = T(n/2) + O(1)
# a=1, b=2, f(n)=1
# log_b a = log_2 1 = 0
# f(n) = Ω(n^0) = Ω(1)
# حالت ۳: T(n) = Θ(1)
```

## تکنیک‌های بهینه‌سازی عملکرد

### بهینه‌سازی‌های سطح الگوریتم
- ساختارهای داده بهتر انتخاب کن
- از الگوریتم‌های کارآمدتر استفاده کن
- بهبودهای الگوریتمی اعمال کن (memoization، pruning)

### بهینه‌سازی‌های سطح کد
- عوامل ثابت را کاهش بده
- تخصیص حافظه را به حداقل برسان
- از عملیات برداری استفاده کن
- بهینه‌سازی کامپایلر را به کار بگیر

### بهینه‌سازی‌های سطح سیستم
- پردازش موازی
- محاسبات توزیع‌شده
- شتاب سخت‌افزار (GPU، FPGA)
- بهینه‌سازی کش و سلسله مراتب حافظه

## نکات کلیدی

۱. **Big O نرخ رشد را توصیف می‌کند**: تمرکز روی چگونگی مقیاس عملکرد با اندازه ورودی
۲. **بدترین حالت معمولاً مهم است**: برای سناریوهای سخت‌ترین طراحی کن
۳. **معامله فضای-زمان**: گاهی از حافظه بیشتری برای صرفه‌جویی در زمان استفاده کن
۴. **ثابت‌ها می‌توانند مهم باشند**: تحلیل نظری جزئیات پیاده‌سازی را ثبت نمی‌کند
۵. **benchmarking نظریه را تأیید می‌کند**: عملکرد واقعی ممکن است با تحلیل asymptotic متفاوت باشد

## مطالعه بیشتر
- کتاب "طراحی الگوریتم" نوشته Kleinberg و Tardos را مطالعه کنید
- تکنیک‌های تحلیل پیشرفته را بیاموزید (تحلیل smoothed، پیچیدگی parameterized)
- برنامه‌نویسی رقابتی و بهینه‌سازی عملکرد را بررسی کنید
- تأثیر رفتار کش و سلسله مراتب حافظه را درک کنید