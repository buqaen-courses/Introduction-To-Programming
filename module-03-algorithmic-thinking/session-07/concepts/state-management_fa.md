# مدیریت وضعیت: برنامه‌ها چگونه به خاطر می‌سپارند

## مقدمه: برنامه‌های دارای حافظه

یک اپلیکیشن ماشین حساب را در نظر بگیرید. وقتی فشار می‌دهید:
1. **۵** - نمایشگر "۵" را نشان می‌دهد
2. **+** - ماشین حساب به خاطر می‌سپارد که می‌خواهید جمع کنید
3. **۳** - نمایشگر "۳" را نشان می‌دهد
4. **=** - ماشین حساب "۸" را نشان می‌دهد (۵ + ۳)

ماشین حساب چگونه ۵ را به خاطر می‌سپارد در حالی که شما ۳ را وارد می‌کنید؟ از **وضعیت** استفاده می‌کند.

**وضعیت** اطلاعاتی است که یک برنامه بین اقدامات به خاطر می‌سپارد.

---

## وضعیت چیست؟

### تعریف

**وضعیت** = تمام داده‌هایی که یک برنامه در حال حاضر ردیابی و به خاطر سپاری می‌کند.

### تشبیه: آشپز در آشپزخانه

یک آشپز "وضعیت" را در حین پختن نگهداری می‌کند:
- **دمای فعلی** اجاق گاز
- **کدام مواد** اضافه شده‌اند
- **چه مدت** غذا در حال پختن است
- **در کدام مرحله** از دستور غذا قرار دارد

بدون به خاطر سپردن این موارد، آشپز نمی‌تواند به درستی آشپزی کند!

### وضعیت در یک برنامه

```python
# وضعیت سبد خرید
cart_state = {
    "items": ["apple", "banana"],
    "total": 3.50,
    "user_id": "user123",
    "logged_in": True
}
```

---

## انواع وضعیت

### ۱. وضعیت اپلیکیشن

**آنچه برنامه درباره خود می‌داند.**

```python
# وضعیت بازی
game_state = {
    "score": 1500,
    "level": 3,
    "lives": 2,
    "paused": False,
    "sound_on": True
}
```

### ۲. وضعیت کاربر

**اطلاعاتی درباره کاربر فعلی.**

```python
# وضعیت نشست کاربر
user_state = {
    "username": "alice",
    "logged_in": True,
    "last_activity": "2024-01-15 10:30:00",
    "permissions": ["read", "write"],
    "shopping_cart": ["item1", "item2"]
}
```

### ۳. وضعیت رابط کاربری

**آنچه رابط کاربری در حال حاضر نشان می‌دهد.**

```python
# وضعیت رابط کاربری
ui_state = {
    "current_page": "dashboard",
    "sidebar_open": True,
    "modal_visible": False,
    "selected_items": ["doc1", "doc2"],
    "sort_column": "date"
}
```

### ۴. وضعیت داده

**اطلاعات واقعی که روی آن کار می‌شود.**

```python
# وضعیت ویرایشگر سند
document_state = {
    "filename": "report.txt",
    "content": "This is my report...",
    "cursor_position": 45,
    "selection_start": None,
    "selection_end": None,
    "modified": True,
    "saved": False
}
```

---

## سیستم‌های Stateful در مقابل Stateless

### سیستم Stateful (چیزها را به خاطر می‌سپارد)

**مثال: سبد خرید آنلاین**
```
اقدام کاربر → پاسخ سیستم
─────────────────────────────────────
"Add apple" → سبد اکنون دارد: [apple]
"Add banana" → سبد اکنون دارد: [apple, banana]
"View cart" → نشان می‌دهد: [apple, banana], Total: $2.50
"Remove apple" → سبد اکنون دارد: [banana]
```

سیستم **محتویات** سبد را بین اقدامات به خاطر می‌سپارد.

### سیستم Stateless (همه چیز را فراموش می‌کند)

**مثال: ماشین حساب (حالت ساده)**
```
اقدام کاربر → پاسخ سیستم
─────────────────────────────────────
"5" → نمایش: 5
"+ 3" → نمایش: 8 (۵ را پس از نشان دادن نتیجه فراموش می‌کند)
"+ 2" → نمایش: 2 (همه چیز را فراموش می‌کند!)
```

سیستم پس از هر محاسبه **همه چیز را فراموش** می‌کند.

### جدول مقایسه

| ویژگی | Stateful | Stateless |
|---------|----------|-----------|
| **حافظه** | داده را به خاطر می‌سپارد | هر بار تازه شروع می‌کند |
| **پیچیدگی** | پیچیده‌تر | ساده‌تر |
| **مثال‌ها** | سبد خرید، بازی‌ها | ماشین حساب‌های ساده، توابع ریاضی |
| **مقیاس‌پذیری** | مقیاس‌پذیری سخت‌تر | مقیاس‌پذیری آسان‌تر |
| **بازیابی** | می‌تواند وضعیت را بازیابی کند | باید دوباره شروع کند |

---

## مدیریت وضعیت در برنامه‌ها

### روش ۱: متغیرها

وضعیت ساده با استفاده از متغیرها:

```python
def simple_counter():
    count = 0  # متغیر وضعیت
    
    while True:
        action = input("Enter 'add', 'sub', or 'quit': ")
        
        if action == "add":
            count += 1  # به‌روزرسانی وضعیت
            print(f"Count: {count}")
        
        elif action == "sub":
            count -= 1  # به‌روزرسانی وضعیت
            print(f"Count: {count}")
        
        elif action == "quit":
            break
    
    return count
```

### روش ۲: دیکشنری‌ها

وضعیت سازمان‌یافته با استفاده از دیکشنری‌ها:

```python
def bank_account():
    account = {
        "balance": 1000.00,
        "transactions": [],
        "account_number": "ACC123"
    }
    
    while True:
        print(f"\nBalance: ${account['balance']:.2f}")
        action = input("Deposit, Withdraw, or History? ").lower()
        
        if action == "deposit":
            amount = float(input("Amount: $"))
            account["balance"] += amount
            account["transactions"].append(f"+${amount:.2f}")
            
        elif action == "withdraw":
            amount = float(input("Amount: $"))
            if amount <= account["balance"]:
                account["balance"] -= amount
                account["transactions"].append(f"-${amount:.2f}")
            else:
                print("Insufficient funds!")
                
        elif action == "history":
            print("\nTransaction History:")
            for trans in account["transactions"]:
                print(f"  {trans}")
                
        elif action == "quit":
            break
    
    return account
```

### روش ۳: کلاس‌ها (شی‌گرایی)

وضعیت پیشرفته با استفاده از کلاس‌ها:

```python
class TodoList:
    """لیست کارهایی که وضعیت را نگهداری می‌کند."""
    
    def __init__(self):
        self.tasks = []  # وضعیت: لیست کارها
        self.completed_count = 0  # وضعیت: ردیابی
    
    def add_task(self, task):
        """افزودن کار جدید."""
        self.tasks.append({
            "text": task,
            "done": False,
            "created": "now"
        })
    
    def complete_task(self, index):
        """علامت‌گذاری کار به عنوان انجام شده."""
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            self.completed_count += 1
    
    def get_stats(self):
        """برگرداندن آمار فعلی."""
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t["done"])
        pending = total - completed
        
        return {
            "total": total,
            "completed": completed,
            "pending": pending
        }

# استفاده
my_todos = TodoList()  # ایجاد با وضعیت خالی
my_todos.add_task("Buy groceries")
my_todos.add_task("Finish report")
my_todos.complete_task(0)

print(my_todos.get_stats())
# {'total': 2, 'completed': 1, 'pending': 1}
```

---

## انتقال‌های وضعیت

### انتقال وضعیت چیست؟

تغییر از یک وضعیت به وضعیت دیگر بر اساس یک رویداد یا اقدام.

### مثال: چراغ راهنمایی

```
وضعیت‌ها: [قرمز] → [قرمز-زرد] → [سبز] → [زرد] → [قرمز]

وضعیت فعلی    رویداد           وضعیت بعدی
────────────────────────────────────────────────
قرمز              زمان‌ساز تمام می‌شود   سبز
سبز               زمان‌ساز تمام می‌شود   زرد  
زرد               زمان‌ساز تمام می‌شود   قرمز
(هر)              اضطراری              چشمک‌زن
```

### مثال: ماشین وضعیت ورود کاربر

```
وضعیت‌ها: [خارج_شده] → [در_حال_ورود] → [وارد_شده] → [خارج_شده]

وضعیت فعلی     رویداد              وضعیت بعدی
────────────────────────────────────────────────────
خارج_شده        کلیک کاربر روی ورود  در_حال_ورود
در_حال_ورود     اعتبارنامه معتبر   وارد_شده
در_حال_ورود     رمز نامعتبر        خارج_شده (خطا)
وارد_شده        خروج کاربر         خارج_شده
وارد_شده        اتمام نشست         خارج_شده
```

### مثال کد: ماشین وضعیت

```python
class LoginSystem:
    def __init__(self):
        self.state = "LOGGED_OUT"
        self.username = None
    
    def login(self, username, password):
        if self.state != "LOGGED_OUT":
            return "Already logged in or processing"
        
        self.state = "LOGGING_IN"
        
        # بررسی اعتبارنامه‌ها
        if self._validate(username, password):
            self.state = "LOGGED_IN"
            self.username = username
            return f"Welcome, {username}!"
        else:
            self.state = "LOGGED_OUT"
            return "Invalid credentials"
    
    def logout(self):
        if self.state != "LOGGED_IN":
            return "Not logged in"
        
        self.state = "LOGGED_OUT"
        self.username = None
        return "Logged out successfully"
    
    def get_status(self):
        return {
            "state": self.state,
            "user": self.username
        }
    
    def _validate(self, username, password):
        # اعتبارسنجی ساده‌شده
        return username == "admin" and password == "secret"

# استفاده
system = LoginSystem()
print(system.get_status())  # {'state': 'LOGGED_OUT', 'user': None}

print(system.login("admin", "secret"))  # Welcome!
print(system.get_status())  # {'state': 'LOGGED_IN', 'user': 'admin'}

print(system.logout())  # Logged out
print(system.get_status())  # {'state': 'LOGGED_OUT', 'user': None}
```

---

## الگوهای رایج مدیریت وضعیت

### الگوی ۱: ذخیره‌سازی وضعیت فعلی

نگهداری "حالا کجا هستیم":

```python
def wizard_signup():
    current_step = 1  # وضعیت: مرحله فعلی
    user_data = {}    # وضعیت: داده جمع‌آوری شده
    
    while current_step <= 3:
        if current_step == 1:
            user_data["name"] = input("Enter name: ")
            current_step = 2  # انتقال وضعیت
            
        elif current_step == 2:
            user_data["email"] = input("Enter email: ")
            current_step = 3  # انتقال وضعیت
            
        elif current_step == 3:
            print(f"Confirm: {user_data}")
            confirm = input("Confirm? (yes/no): ")
            if confirm == "yes":
                save_user(user_data)
                current_step = 4  # تمام!
            else:
                current_step = 1  # شروع دوباره
    
    print("Signup complete!")
```

### الگوی ۲: تاریخچه/Undo

نگهداری تاریخچه برای اجازه undo:

```python
class TextEditor:
    def __init__(self):
        self.content = ""
        self.history = []  # وضعیت: تاریخچه
        self.history_index = -1  # وضعیت: موقعیت فعلی در تاریخچه
    
    def type_text(self, text):
        # ذخیره وضعیت فعلی در تاریخچه
        self.history = self.history[:self.history_index + 1]
        self.history.append(self.content)
        self.history_index += 1
        
        # به‌روزرسانی محتوا
        self.content += text
    
    def undo(self):
        if self.history_index >= 0:
            self.content = self.history[self.history_index]
            self.history_index -= 1
    
    def redo(self):
        if self.history_index < len(self.history) - 1:
            self.history_index += 1
            self.content = self.history[self.history_index]
```

### الگوی ۳: کش/حافظه‌سازی

به خاطر سپردن نتایج برای جلوگیری از محاسبه مجدد:

```python
# بدون کشینگ
def fibonacci_slow(n):
    if n <= 1:
        return n
    return fibonacci_slow(n-1) + fibonacci_slow(n-2)
    # بسیار کند برای n بزرگ!

# با کشینگ (مدیریت وضعیت)
def fibonacci_fast(n, cache={}):
    if n in cache:  # ابتدا بررسی وضعیت
        return cache[n]
    
    if n <= 1:
        result = n
    else:
        result = fibonacci_fast(n-1, cache) + fibonacci_fast(n-2, cache)
    
    cache[n] = result  # ذخیره در وضعیت
    return result
```

---

## پایداری وضعیت (ذخیره وضعیت)

### چرا وضعیت را پایدار کنیم؟

بدون پایداری، وضعیت هنگام پایان برنامه از دست می‌رود!

### روش ۱: ذخیره‌سازی فایل

```python
import json

def save_state(state, filename="state.json"):
    """ذخیره وضعیت در فایل."""
    with open(filename, "w") as f:
        json.dump(state, f)
    print(f"State saved to {filename}")

def load_state(filename="state.json"):
    """بارگذاری وضعیت از فایل."""
    try:
        with open(filename, "r") as f:
            state = json.load(f)
        print(f"State loaded from {filename}")
        return state
    except FileNotFoundError:
        print("No saved state found, starting fresh")
        return {}

# استفاده
app_state = {
    "user": "alice",
    "preferences": {"theme": "dark"},
    "last_opened": "document.txt"
}

save_state(app_state)
loaded_state = load_state()
print(loaded_state)
```

### روش ۲: ذخیره‌سازی پایگاه داده

```python
# مثال مفهومی با استفاده از SQLite
import sqlite3

def save_to_database(user_id, state):
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT OR REPLACE INTO user_states (user_id, data)
        VALUES (?, ?)
    ''', (user_id, json.dumps(state)))
    
    conn.commit()
    conn.close()

def load_from_database(user_id):
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT data FROM user_states WHERE user_id = ?
    ''', (user_id,))
    
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return json.loads(result[0])
    return None
```

---

## بهترین شیوه‌های مدیریت وضعیت

### ۱. حداقل نگهداری وضعیت

فقط آنچه نیاز دارید را ذخیره کنید:

```python
# خوب - وضعیت حداقلی
game_state = {
    "player_position": (10, 20),
    "health": 100,
    "inventory": ["sword", "potion"]
}

# بد - وضعیت زیادی اضافی
game_state = {
    "player_position": (10, 20),
    "health": 100,
    "max_health": 100,
    "health_percentage": 100.0,  # قابل محاسبه از health/max_health
    "inventory": ["sword", "potion"],
    "inventory_count": 2,  # قابل محاسبه از inventory
    "last_position": (10, 20),  # همان موقعیت فعلی!
}
```

### ۲. به‌روزرسانی‌های Immutable

وضعیت را مستقیماً تغییر ندهید - وضعیت جدید ایجاد کنید:

```python
# خوب - به‌روزرسانی immutable
def add_item(current_state, item):
    new_inventory = current_state["inventory"] + [item]
    return {
        **current_state,
        "inventory": new_inventory
    }

# بد - تغییر مستقیم وضعیت
def add_item_bad(current_state, item):
    current_state["inventory"].append(item)  # تغییر می‌دهد!
    return current_state
```

### ۳. منبع واحد حقیقت

وضعیت را تکرار نکنید:

```python
# بد - وضعیت تکراری
user_state = {
    "name": "Alice",
    "profile": {
        "name": "Alice"  # تکراری!
    }
}

# خوب - منبع واحد
user_state = {
    "name": "Alice",  # فقط اینجا
    "profile": {
        "bio": "Software developer",
        "location": "NYC"
    }
}
```

### ۴. انتقال‌های وضعیت واضح

واضح کنید که وضعیت چگونه تغییر می‌کند:

```python
# خوب - انتقال‌های صریح
def process_order(order_state, action):
    if action == "submit":
        return {**order_state, "status": "PENDING"}
    elif action == "pay":
        return {**order_state, "status": "PAID"}
    elif action == "ship":
        return {**order_state, "status": "SHIPPED"}
    else:
        return order_state  # بدون تغییر
```

---

## تمرین‌های عملی

### تمرین ۱: شناسایی وضعیت

برای هر اپلیکیشن، ۳-۵ مورد از وضعیت را لیست کنید:

1. اپلیکیشن پخش موسیقی
2. سبد خرید فروشگاه اینترنتی
3. بازی ویدیویی
4. اپلیکیشن چت

### تمرین ۲: طراحی مدیریت وضعیت

مدیریت وضعیت را برای یک **بازی ساده** طراحی کنید:

```python
game_state = {
    # چه وضعیتی نیاز دارید؟
    
}

def initialize_game():
    # راه‌اندازی وضعیت اولیه
    pass

def update_game(state, action):
    # به‌روزرسانی وضعیت بر اساس اقدام
    pass
```

### تمرین ۳: ماشین وضعیت

یک ماشین وضعیت برای یک **چراغ راهنمایی** ایجاد کنید:

- وضعیت‌ها: قرمز، سبز، زرد
- رویدادها: TIMER_EXPIRED، EMERGENCY_VEHICLE
- انتقال‌ها: تعریف کنید برای هر رویداد در هر وضعیت چه اتفاقی می‌افتد

### تمرین ۴: عملکرد Undo

عملکرد undo را برای یک ویرایشگر متن ساده پیاده‌سازی کنید:

```python
class SimpleEditor:
    def __init__(self):
        self.content = ""
        # اضافه کردن وضعیت تاریخچه اینجا
    
    def type_text(self, text):
        # افزودن متن و ذخیره در تاریخچه
        pass
    
    def undo(self):
        # بازیابی وضعیت قبلی
        pass
```

---

## نکات کلیدی

1. **وضعیت داده به خاطر سپرده شده است**: آنچه برنامه الآن می‌داند
2. **Stateful در مقابل Stateless**: سیستم‌هایی که به خاطر می‌سپارند در مقابل سیستم‌هایی که فراموش می‌کنند
3. **انتقال‌های وضعیت**: چگونه وضعیت در طول زمان تغییر می‌کند
4. **الگوهای مدیریت وضعیت**: متغیرها، دیکشنری‌ها، کلاس‌ها
5. **پایداری**: ذخیره وضعیت تا از دست نرود

## به خاطر بسپارید

```
┌─────────────────────────────────────────┐
│         مدیریت وضعیت                │
├─────────────────────────────────────────┤
│                                         │
│  ورودی → [به‌روزرسانی وضعیت] → خروجی       │
│              ↑                          │
│         [به خاطر سپردن برای           │
│          دفعه بعد]                      │
│                                         │
└─────────────────────────────────────────┘
```

### سوالات کلیدی برای طراحی وضعیت

1. **چه چیزی باید به خاطر سپرده شود؟** (شناسایی وضعیت)
2. **چه موقع تغییر می‌کند؟** (شناسایی انتقال‌ها)
3. **چه کسی می‌تواند آن را تغییر دهد؟** (کنترل دسترسی)
4. **آیا باید پایدار شود؟** (ذخیره روی دیسک/پایگاه داده؟)

---

## گام‌های بعدی

- درباره وضعیت global در مقابل local بیاموزید
- معماری Redux/Flux را مطالعه کنید (برای وب اپلیکیشن‌ها)
- طراحی پایگاه داده برای پایداری وضعیت را بررسی کنید
- دسترسی همزمان به وضعیت (threading) را درک کنید
