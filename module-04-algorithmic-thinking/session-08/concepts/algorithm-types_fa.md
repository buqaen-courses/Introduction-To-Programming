# انواع الگوریتم‌ها: دسته‌بندی جامع

## درک دسته‌بندی الگوریتم‌ها

الگوریتم‌ها می‌توانند به روش‌های مختلف بر اساس رویکرد، استراتژی یا نوع مسئله‌ای که حل می‌کنند دسته‌بندی شوند. درک این دسته‌ها در انتخاب الگوریتم مناسب برای مسائل خاص کمک می‌کند.

## دسته‌بندی بر اساس رویکرد

### ۱. الگوریتم‌های زورآزمایی

**استراتژی**: تمام راه حل‌های ممکن را امتحان کن تا راه حل صحیح را پیدا کنی.

**ویژگی‌ها:**
- ساده برای درک و پیاده‌سازی
- همیشه راه حلی پیدا می‌کند اگر وجود داشته باشد
- برای فضاهای مسئله بزرگ بسیار کند می‌تواند باشد

**مثال‌ها:**
```python
# شکستن رمز عبور (زورآزمایی)
def crack_password(target_hash, charset, max_length):
    for length in range(1, max_length + 1):
        for attempt in generate_combinations(charset, length):
            if hash(attempt) == target_hash:
                return attempt
    return None

# فروشنده دوره‌گرد - تمام مسیرها را امتحان کن
def tsp_brute_force(cities):
    min_distance = float('inf')
    best_route = None

    for route in permutations(cities):
        distance = calculate_route_distance(route)
        if distance < min_distance:
            min_distance = distance
            best_route = route

    return best_route, min_distance
```

**چه زمانی استفاده کن:** فضاهای مسئله کوچک، وقتی درستی مهم‌تر از سرعت است.

### ۲. الگوریتم‌های حریصانه

**استراتژی**: در هر مرحله انتخاب بهینه محلی انجام بده با امید یافتن بهینه جهانی.

**ویژگی‌ها:**
- سریع و کارآمد
- همیشه راه حل‌های بهینه تولید نمی‌کنند
- برای انواع خاصی از مسائل خوب کار می‌کنند

**مثال‌ها:**
```python
# مسئله تغییر سکه
def coin_change_greedy(amount, coins):
    coins.sort(reverse=True)  # بزرگ‌ترین اول
    result = []

    for coin in coins:
        while amount >= coin:
            result.append(coin)
            amount -= coin

    return result

# انتخاب فعالیت (حریصانه بر اساس زمان پایان)
def activity_selection(activities):
    # activities = [(start, finish), ...]
    activities.sort(key=lambda x: x[1])  # مرتب‌سازی بر اساس زمان پایان

    selected = [activities[0]]
    last_finish = activities[0][1]

    for activity in activities[1:]:
        if activity[0] >= last_finish:
            selected.append(activity)
            last_finish = activity[1]

    return selected
```

**چه زمانی استفاده کن:** مسائل بهینه‌سازی که انتخاب‌های محلی به بهینه جهانی منجر شوند.

### ۳. الگوریتم‌های تقسیم و حل

**استراتژی**: مسئله را به زیرمسئله‌های کوچکتر تقسیم کن، به صورت بازگشتی حل کن، سپس راه حل‌ها را ترکیب کن.

**ویژگی‌ها:**
- رویکرد بازگشتی
- مسئله‌ها باید قابل تقسیم باشند
- اغلب راه حل‌های بهینه
- خوب برای پردازش موازی

**مثال‌ها:**
```python
# مرتب‌سازی ادغام
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# جستجوی باینری
def binary_search(arr, target):
    if not arr:
        return -1

    mid = len(arr) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr[:mid], target)
    else:
        # نیاز به تنظیم شاخص برای نیمه راست
        result = binary_search(arr[mid+1:], target)
        return mid + 1 + result if result != -1 else -1
```

**چه زمانی استفاده کن:** مسائلی که به طور طبیعی به زیرمسئله‌های مستقل تقسیم می‌شوند.

### ۴. الگوریتم‌های برنامه‌ریزی پویا

**استراتژی**: مسئله را به زیرمسئله‌ها تقسیم کن، هر زیرمسئله را یک بار حل کن، راه حل‌ها را برای استفاده مجدد ذخیره کن.

**ویژگی‌ها:**
- ساختار بهینه زیرمسئله (راه حل بهینه از زیرراه حل‌های بهینه استفاده می‌کند)
- زیرمسئله‌های هم‌پوشانی
- فضای اضافی در برابر زمان معامله کن
- اغلب از memoization یا tabulation استفاده می‌کند

**مثال‌ها:**
```python
# فیبوناچی با memoization
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

# بلندترین زیر دنباله مشترک
def lcs(X, Y):
    m, n = len(X), len(Y)

    # ایجاد جدول DP
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # پر کردن جدول
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # بازسازی راه حل
    lcs_str = ""
    i, j = m, n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs_str = X[i-1] + lcs_str
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return len(lcs_str), lcs_str

# کوله‌پشتی ۰/۱
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w - weights[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]
```

**چه زمانی استفاده کن:** مسائلی با زیرمسئله‌های هم‌پوشانی و ساختار بهینه زیرمسئله.

### ۵. الگوریتم‌های پس‌گرد

**استراتژی**: راه حل‌های جزئی را امتحان کن، وقتی کار نمی‌کنند برگرد، انتخاب‌های متفاوتی امتحان کن.

**ویژگی‌ها:**
- جستجوی سیستماتیک فضای راه حل
- ساخت راه حل به طور تدریجی
- حذف راه حل‌هایی که کار نمی‌کنند
- می‌تواند همه راه حل‌ها یا فقط یکی را پیدا کند

**مثال‌ها:**
```python
# مسئله N-ملکه
def solve_n_queens(n):
    def is_safe(board, row, col):
        # بررسی این ستون
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # بررسی قطر بالایی
        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if board[i][j] == 'Q':
                return False

        # بررسی قطر پایینی
        for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
            if board[i][j] == 'Q':
                return False

        return True

    def solve(board, row):
        if row == n:
            solutions.append([''.join(row) for row in board])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                solve(board, row + 1)
                board[row][col] = '.'  # پس‌گرد

    solutions = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    solve(board, 0)
    return solutions

# حل‌کننده سودوکو
def solve_sudoku(board):
    def is_valid(num, pos):
        # بررسی ردیف
        for j in range(9):
            if board[pos[0]][j] == num and j != pos[1]:
                return False

        # بررسی ستون
        for i in range(9):
            if board[i][pos[1]] == num and i != pos[0]:
                return False

        # بررسی جعبه ۳×۳
        box_x = pos[0] // 3
        box_y = pos[1] // 3
        for i in range(box_x*3, box_x*3 + 3):
            for j in range(box_y*3, box_y*3 + 3):
                if board[i][j] == num and (i,j) != pos:
                    return False

        return True

    def find_empty():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None

    def solve():
        empty = find_empty()
        if not empty:
            return True

        row, col = empty
        for num in range(1, 10):
            if is_valid(num, (row, col)):
                board[row][col] = num
                if solve():
                    return True
                board[row][col] = 0  # پس‌گرد

        return False

    solve()
    return board
```

**چه زمانی استفاده کن:** مسائل رضایت محدودیت، معماها، بهینه‌سازی ترکیبی.

## دسته‌بندی بر اساس نوع مسئله

### الگوریتم‌های مرتب‌سازی

#### بر پایه مقایسه
```python
# مرتب‌سازی سریع (تقسیم و حل)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# مرتب‌سازی heap
def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr
```

#### غیر مقایسه‌ای
```python
# مرتب‌سازی شمارش
def counting_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    min_val = min(arr)
    range_size = max_val - min_val + 1

    count = [0] * range_size
    output = [0] * len(arr)

    # شمارش رخدادها
    for num in arr:
        count[num - min_val] += 1

    # شمارش تجمعی
    for i in range(1, len(count)):
        count[i] += count[i-1]

    # ساخت خروجی
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output

# مرتب‌سازی پایه
def radix_sort(arr):
    max_digits = len(str(max(arr)))

    for digit in range(max_digits):
        buckets = [[] for _ in range(10)]

        for num in arr:
            digit_value = (num // (10 ** digit)) % 10
            buckets[digit_value].append(num)

        arr = []
        for bucket in buckets:
            arr.extend(bucket)

    return arr
```

### الگوریتم‌های جستجو

#### جستجوی خطی
```python
def linear_search(arr, target):
    for i, item in enumerate(arr):
        if item == target:
            return i
    return -1
```

#### جستجوی باینری
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

#### جستجوی مبتنی بر هش
```python
class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None
```

## الگوریتم‌های تصادفی

**استراتژی**: از انتخاب‌های تصادفی برای ساده‌سازی یا سرعت بخشیدن به الگوریتم‌ها استفاده کن.

```python
# مرتب‌سازی سریع با pivot تصادفی
import random

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Pivot تصادفی
    pivot_idx = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_idx]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

# الگوریتم مونت کارلو برای تست اول بودن
import random

def is_prime_monte_carlo(n, k=10):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # n-1 را به صورت 2^r * d بنویس
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    # حلقه شاهد
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True
```

## الگوریتم‌های تقریب

**استراتژی**: راه حل‌های نزدیک به بهینه را پیدا کن وقتی راه حل‌های دقیق خیلی گران هستند.

```python
# تقریب فروشنده دوره‌گرد (همسایه نزدیک‌ترین)
def tsp_nearest_neighbor(cities):
    if not cities:
        return [], 0

    unvisited = set(cities)
    current = cities[0]
    unvisited.remove(current)
    route = [current]
    total_distance = 0

    while unvisited:
        # نزدیک‌ترین شهر بازدید نشده را پیدا کن
        closest = min(unvisited, key=lambda city: distance(current, city))
        total_distance += distance(current, closest)
        route.append(closest)
        current = closest
        unvisited.remove(closest)

    # به شروع برگرد
    total_distance += distance(route[-1], route[0])
    route.append(route[0])

    return route, total_distance
```

## نکات کلیدی

۱. **استراتژی‌های مختلف**: زورآزمایی، حریصانه، تقسیم و حل، برنامه‌ریزی پویا، پس‌گرد
۲. **مشخص مسئله**: الگوریتم را بر اساس ویژگی‌های مسئله انتخاب کن
۳. **معامله‌ها**: زمان در برابر فضا، راه حل‌های دقیق در برابر تقریب
۴. **ترکیب‌ها کار می‌کنند**: بسیاری از مسائل از رویکردهای ترکیبی بهره‌مند می‌شوند
۵. **تمرین مهم است**: درک زمان اعمال تکنیک‌های مختلف

## مطالعه بیشتر
- کتاب‌های راهنمای طراحی الگوریتم را مطالعه کنید
- روی پلتفرم‌های برنامه‌نویسی رقابتی تمرین کنید
- ساختارهای داده پیشرفته را بیاموزید
- الگوریتم‌های موازی و توزیع‌شده را بررسی کنید