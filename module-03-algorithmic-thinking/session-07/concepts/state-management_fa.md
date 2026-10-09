# مدیریت وضعیت: پیگیری تغییر در برنامه‌ها

## وضعیت چیست؟

وضعیت وضعیت یا شرایط فعلی یک سیستم در هر لحظه است. در برنامه‌نویسی، وضعیت تمام اطلاعاتی را نشان می‌دهد که یک برنامه برای به یاد آوردن بین عملیات نیاز دارد.

## انواع وضعیت

### وضعیت برنامه
شرط کلی برنامه در حال اجرا:
- **متغیرها**: مقادیر فعلی ذخیره شده در حافظه
- **زمینه اجرا**: کدام تابع در حال اجرا است، کجا متوقف شده
- **منابع باز**: فایل‌ها، اتصالات شبکه، لینک‌های پایگاه داده
- **پیکربندی**: تنظیماتی که رفتار را تحت تأثیر قرار می‌دهند

### وضعیت برنامه
اطلاعات درباره کاری که برنامه انجام می‌دهد:
- **نشست کاربر**: وضعیت ورود، ترجیحات، سبد خرید
- **ناوبری**: صفحه/صفحه فعلی، مسیرهای breadcrumb
- **پیشرفت گردش کار**: تکمیل مرحله در فرآیندهای چند مرحله‌ای
- **داده‌های کش**: نتایج ذخیره شده برای جلوگیری از محاسبه مجدد

### وضعیت سیستم
شرط سیستم کامپیوتری:
- **سیستم فایل**: کدام فایل‌ها وجود دارند، محتوای آنها
- **اتصالات شبکه**: لینک‌های فعال و وضعیت آنها
- **وضعیت سخت‌افزار**: سطح باتری، فضای دیسک، دما
- **فرآیندهای در حال اجرا**: چه برنامه‌هایی فعال هستند

## وضعیت در الگوریتم‌ها

### الگوریتم‌های وضعیتی
الگوریتم‌هایی که اطلاعات را بین مراحل به یاد می‌آورند:

```python
def running_average():
    total = 0
    count = 0

    def add_number(number):
        nonlocal total, count  # دسترسی به متغیرهای بیرونی (وضعیت)
        total += number
        count += 1
        return total / count

    return add_number

# استفاده
avg_func = running_average()
print(avg_func(10))  # ۱۰.۰ (وضعیت: total=10, count=1)
print(avg_func(20))  # ۱۵.۰ (وضعیت: total=30, count=2)
print(avg_func(30))  # ۲۰.۰ (وضعیت: total=60, count=3)
```

### الگوریتم‌های بدون وضعیت
هر عملیات مستقل است، هیچ حافظه‌ای از فراخوانی‌های قبلی ندارد:

```python
def calculate_average(numbers):
    # بدون وضعیت - هر فراخوانی مستقل است
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# هر فراخوانی تازه شروع می‌شود
print(calculate_average([10, 20, 30]))  # ۲۰.۰
print(calculate_average([40, 50]))      # ۴۵.۰
print(calculate_average([10, 20, 30]))  # ۲۰.۰ (نتیجه یکسان)
```

## نمایش وضعیت

### متغیرها به عنوان ظروف وضعیت
وضعیت ساده با استفاده از متغیرها:
```python
# وضعیت شمارنده
counter = 0

def increment():
    global counter  # دسترسی به وضعیت جهانی
    counter += 1
    return counter

# استفاده
increment()  # ۱
increment()  # ۲
```

### اشیاء به عنوان ظروف وضعیت پیچیده
وضعیت پیچیده با استفاده از اشیاء:
```python
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance  # وضعیت حساب
        self.transactions = []          # وضعیت تاریخچه تراکنش‌ها

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"واریز: +{amount}")
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"برداشت: -{amount}")
            return True
        return False

    def get_balance(self):
        return self.balance

    def get_history(self):
        return self.transactions.copy()

# استفاده
account = BankAccount(1000)
account.deposit(500)    # وضعیت: balance=1500
account.withdraw(200)   # وضعیت: balance=1300
print(account.get_balance())     # 1300
print(account.get_history())     # ['واریز: +500', 'برداشت: -200']
```

### ماشین‌های وضعیت
نمایش رسمی گذارهای وضعیت:

```python
class TrafficLight:
    def __init__(self):
        self.state = "red"  # وضعیت اولیه

    def next(self):
        # گذارهای وضعیت
        if self.state == "red":
            self.state = "green"
        elif self.state == "green":
            self.state = "yellow"
        elif self.state == "yellow":
            self.state = "red"

        return self.state

    def get_color(self):
        return self.state

# استفاده
light = TrafficLight()
print(light.get_color())  # "red"
light.next()              # "green"
light.next()              # "yellow"
light.next()              # "red"
```

## پایداری وضعیت

### وضعیت موقت (RAM)
وضعیت فقط وقتی برنامه اجرا می‌شود وجود دارد:
```python
# وضعیت در حافظه
user_data = {"name": "علی", "score": 100}

# وضعیت در طول اجرای برنامه ادامه دارد
user_data["score"] += 50  # وضعیت تغییر می‌کند
print(user_data["score"]) # ۱۵۰
```

### وضعیت پایدار (ذخیره‌سازی)
وضعیت از ری‌استارت برنامه جان سالم به در می‌برد:
```python
import json

def save_game_state(player_data):
    with open("game_save.json", "w") as file:
        json.dump(player_data, file)

def load_game_state():
    try:
        with open("game_save.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"level": 1, "score": 0, "items": []}

# استفاده
player = load_game_state()  # بازیابی وضعیت
player["score"] += 100      # به‌روزرسانی وضعیت
save_game_state(player)     # پایدارسازی وضعیت
```

## چالش‌های مدیریت وضعیت

### شرایط رقابتی
چند فرآیند همزمان به وضعیت دسترسی دارند:
```python
# وضعیت اشتراکی مشکل‌ساز
counter = 0

def increment_counter():
    global counter
    current = counter      # خواندن
    # فرآیند دیگری ممکن است counter را اینجا تغییر دهد
    counter = current + 1  # نوشتن

# راه حل: عملیات اتمی یا قفل‌ها
import threading
lock = threading.Lock()

def safe_increment():
    with lock:
        global counter
        counter += 1
```

### ناسازگاری وضعیت
ترکیب‌های وضعیت نامعتبر:
```python
class User:
    def __init__(self):
        self.logged_in = False
        self.session_token = None

    def login(self, token):
        self.logged_in = True
        self.session_token = token

    def logout(self):
        self.logged_in = False
        self.session_token = None  # پاکسازی وضعیت

    # وضعیت ناسازگار ممکن است:
    # logged_in = True, session_token = None
```

### انفجار وضعیت
تعداد زیادی ترکیب وضعیت ممکن:
```python
# وضعیت پیچیده - در صورت امکان اجتناب کنید
class GameCharacter:
    def __init__(self):
        self.health = 100
        self.mana = 50
        self.position = (0, 0)
        self.inventory = []
        self.quests = []
        self.achievements = []
        self.friends = []
        # ... فیلدهای بسیار زیادی

# بهتر: گروه‌بندی وضعیت مرتبط
class GameCharacter:
    def __init__(self):
        self.stats = {"health": 100, "mana": 50}
        self.location = Location(0, 0)
        self.inventory = Inventory()
        self.progress = Progress()
```

## الگوهای طراحی وضعیت

### الگوی Singleton
نمونه وضعیت جهانی واحد:
```python
class Configuration:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.settings = {}
            self.initialized = True

# استفاده
config1 = Configuration()
config2 = Configuration()
config1.settings["theme"] = "dark"
print(config2.settings["theme"])  # "dark" (نمونه یکسان)
```

### الگوی Observer
تغییرات وضعیت به طرف‌های علاقه‌مند اطلاع می‌دهد:
```python
class Subject:
    def __init__(self):
        self._observers = []
        self._state = None

    def attach(self, observer):
        self._observers.append(observer)

    def set_state(self, state):
        self._state = state
        self._notify_observers()

    def _notify_observers(self):
        for observer in self._observers:
            observer.update(self._state)

class Observer:
    def update(self, state):
        print(f"وضعیت به: {state} تغییر کرد")

# استفاده
subject = Subject()
observer = Observer()
subject.attach(observer)

subject.set_state("active")   # Observer اطلاع داده می‌شود
subject.set_state("inactive") # Observer اطلاع داده می‌شود
```

## وضعیت در پارادایم‌های برنامه‌نویسی مختلف

### برنامه‌نویسی امرات
مدیریت وضعیت صریح:
```python
# تغییرات وضعیت صریح هستند
balance = 1000
balance = balance - 100  # تغییر وضعیت صریح
balance = balance + 200  # تغییر وضعیت دیگری
```

### برنامه‌نویسی تابعی
به حداقل رساندن یا اجتناب از وضعیت قابل تغییر:
```python
# توابع خالص، بدون تغییرات وضعیت
def withdraw(balance, amount):
    return balance - amount  # مقدار جدیدی برمی‌گرداند، تغییر نمی‌دهد

def deposit(balance, amount):
    return balance + amount

# استفاده
balance = 1000
balance = withdraw(balance, 100)  # ۹۰۰
balance = deposit(balance, 200)   # ۱۱۰۰
```

### برنامه‌نویسی شی‌گرا
وضعیت در اشیاء محصور شده است:
```python
class Account:
    def __init__(self, balance):
        self._balance = balance  # وضعیت خصوصی

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False

    def get_balance(self):
        return self._balance
```

## نکات کلیدی

۱. **وضعیت حافظه رویدادهای گذشته است**: آنچه سیستم در هر لحظه می‌داند
۲. **مدیریت وضعیت بسیار مهم است**: مدیریت وضعیت ضعیف منجر به باگ می‌شود
۳. **انواع وضعیت مختلف**: برنامه، برنامه، و وضعیت سیستم
۴. **پایداری اهمیت دارد**: برخی وضعیت‌ها از ری‌استارت برنامه جان سالم به در می‌برند
۵. **الگوهای طراحی کمک می‌کنند**: الگوهای مناسب وضعیت پیچیده را مدیریت می‌کنند

## مطالعه بیشتر
- نظریه ماشین‌های وضعیت و اتوماتا را مطالعه کنید
- درباره Redux و مدیریت وضعیت در برنامه‌های وب بیاموزید
- مدیریت وضعیت پایگاه داده و تراکنش‌ها را کاوش کنید
- یکسانی نهایی و سیستم‌های توزیع شده را درک کنید