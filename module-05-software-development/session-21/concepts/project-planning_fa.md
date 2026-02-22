# برنامه‌ریزی پروژه: از ایده تا برنامه کارآمد

## مقدمه: ساختن برنامه‌های واقعی

تا کنون، اصول پایتون را یاد گرفته‌اید. اکنون زمان آن رسیده که همه چیز را در **برنامه‌های واقعی** که مشکلات واقعی را حل می‌کنند، ترکیب کنید. این راهنما به شما نشان می‌دهد چگونه یک پروژه برنامه‌نویسی را برنامه‌ریزی، بسازید و تکمیل کنید.

### فرآیند برنامه‌نویسی

```
۱. درک مسئله
   ↓
۲. برنامه‌ریزی راه‌حل
   ↓
۳. ساختن مرحله به مرحله
   ↓
۴. تست و رفع اشکال
   ↓
۵. بهبود و پرداخت
```

---

## بخش ۱: درک مسئله

### خواندن دقیق نیازمندی‌ها

**پروژه نمونه**: ساختن دفتر نمرات دانشجو

**تحلیل نیازمندی‌ها**:

```
چه کاری باید انجام دهد؟
├── ورودی
│   ├── خواندن نام و نمرات دانشجو از فایل
│   └── مدیریت خطاها (فایل گم شده، داده بد)
├── پردازش
│   ├── محاسبه میانگین برای هر دانشجو
│   ├── تخصیص نمرات حرفی
│   └── محاسبه آمار کلاس
├── خروجی
│   ├── نمایش گزارش فرمت‌بندی شده
│   └── ذخیره گزارش در فایل
└── رابط کاربری
    ├── سیستم منو برای انتخاب‌ها
    └── دستورالعمل‌های واضح
```

### پرسیدن سوالات

قبل از نوشتن کد، روشن کنید:
- فرمت داده ورودی چیست؟
- با خطاها چه باید کرد؟
- چه کسی از این برنامه استفاده خواهد کرد؟
- «موفقیت» چگونه به نظر می‌رسد؟

**بحث فرمت داده نمونه**:

```
فرمت grades.txt:
Alice Johnson,85,92,78
Bob Smith,76,88,91

سوالات:
- اگر خط خالی باشد چه؟ → رد کن
- اگر نمرات گم شده باشد چه؟ → پیام خطا
- اگر نام کاما داشته باشد چه؟ → از نقل‌قول یا جداکننده متفاوت استفاده کن
```

---

## بخش ۲: برنامه‌ریزی راه‌حل

### تقسیم به توابع

سعی نکنید کل برنامه را یکجا بنویسید. آن را به قطعات کوچک تقسیم کنید:

```python
# gradebook.py - طرح اولیه (هنوز کد ندارد!)

def read_student_data(filename):
    """خواندن داده از فایل و بازگرداندن لیست دانشجوها."""
    pass  # TODO: پیاده‌سازی

def calculate_average(scores):
    """محاسبه میانگین لیست نمرات."""
    pass  # TODO: پیاده‌سازی

def get_letter_grade(average):
    """تبدیل میانگین عددی به نمره حرفی."""
    pass  # TODO: پیاده‌سازی

def generate_report(students):
    """ایجاد گزارش فرمت‌بندی از داده دانشجو."""
    pass  # TODO: پیاده‌سازی

def save_report(report, filename):
    """ذخیره گزارش در فایل."""
    pass  # TODO: پیاده‌سازی

def show_menu():
    """نمایش منوی کاربر."""
    pass  # TODO: پیاده‌سازی

def main():
    """حلقه اصلی برنامه."""
    pass  # TODO: پیاده‌سازی
```

### ایجاد نمودار جریان

```
Start
  │
  ▼
Show Menu ◄─────────────────────────┐
  │                                  │
  ▼                                  │
Get User Choice                      │
  │                                  │
  ├── Choice 1: Load & Display ──► Process ──► Display ──┤
  │                                                        │
  ├── Choice 2: Statistics ───► Calculate ──► Display ────┤
  │                                                        │
  ├── Choice 3: Exit ────────► End                       │
  │                                                        │
  └── Invalid ───────────────► Error Message ─────────────┘
```

### برنامه‌ریزی ساختارهای داده

```python
# داده دانشجو چگونه به نظر می‌رسد؟
student = {
    'name': 'Alice Johnson',
    'scores': [85, 92, 78],
    'average': 85.0,
    'grade': 'B'
}

# چگونه چندین دانشجو را ذخیره کنیم؟
students = [
    {'name': 'Alice', 'scores': [85, 92, 78], ...},
    {'name': 'Bob', 'scores': [76, 88, 91], ...},
    ...
]
```

---

## بخش ۳: ساختن مرحله به مرحله

### مرحله ۱: شروع با ساده‌ترین نسخه

ابتدا یک قطعه کوچک را کار کنید:

```python
# مرحله ۱: فقط فایل را بخوان

def read_student_data(filename):
    """خواندن داده از فایل."""
    students = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(',')
                name = parts[0]
                scores = [int(s) for s in parts[1:]]

                students.append({
                    'name': name,
                    'scores': scores
                })

    except FileNotFoundError:
        print(f"Error: {filename} not found")

    return students

# فوراً تست کنید!
if __name__ == "__main__":
    students = read_student_data("grades.txt")
    print(f"Read {len(students)} students")
    for student in students:
        print(f"  {student['name']}: {student['scores']}")
```

### مرحله ۲: افزودن یک ویژگی در هر بار

```python
# مرحله ۲: افزودن محاسبات

def calculate_average(scores):
    """محاسبه میانگین نمرات."""
    if not scores:
        return 0
    return sum(scores) / len(scores)

def get_letter_grade(average):
    """تبدیل میانگین به نمره حرفی."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

# به‌روزرسانی تابع خواندن برای شامل کردن محاسبات
def read_student_data(filename):
    """خواندن داده از فایل با محاسبات."""
    students = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(',')
                name = parts[0]
                scores = [int(s) for s in parts[1:]]
                average = calculate_average(scores)
                grade = get_letter_grade(average)

                students.append({
                    'name': name,
                    'scores': scores,
                    'average': average,
                    'grade': grade
                })

    except FileNotFoundError:
        print(f"Error: {filename} not found")
    except ValueError:
        print("Error: Invalid score data in file")

    return students

# دوباره تست کنید
if __name__ == "__main__":
    students = read_student_data("grades.txt")
    for student in students:
        print(f"{student['name']}: {student['average']:.1f} ({student['grade']})")
```

### مرحله ۳: افزودن رابط کاربری

```python
# مرحله ۳: افزودن سیستم منو

def show_menu():
    """نمایش گزینه‌های منو."""
    print("\n" + "="*40)
    print("STUDENT GRADEBOOK")
    print("="*40)
    print("1. Load and Display Grades")
    print("2. Show Class Statistics")
    print("3. Save Report to File")
    print("4. Exit")
    print("="*40)

def get_choice():
    """دریافت انتخاب کاربر."""
    while True:
        choice = input("Enter choice (1-4): ").strip()
        if choice in ['1', '2', '3', '4']:
            return choice
        print("Invalid choice. Please enter 1-4.")

def main():
    """حلقه اصلی برنامه."""
    students = []

    while True:
        show_menu()
        choice = get_choice()

        if choice == '1':
            students = read_student_data("grades.txt")
            if students:
                display_grades(students)

        elif choice == '2':
            if students:
                show_statistics(students)
            else:
                print("No data loaded. Please load data first.")

        elif choice == '3':
            if students:
                save_report(students, "report.txt")
            else:
                print("No data loaded. Please load data first.")

        elif choice == '4':
            print("Goodbye!")
            break

# توابع کمکی
def display_grades(students):
    """نمایش نمرات دانشجو."""
    print("\nStudent Grades:")
    print("-" * 40)
    for student in students:
        print(f"{student['name']:<20} {student['average']:>6.1f} {student['grade']:>3}")

def show_statistics(students):
    """نمایش آمار کلاس."""
    if not students:
        print("No data available")
        return

    averages = [s['average'] for s in students]
    class_avg = sum(averages) / len(averages)
    passing = sum(1 for s in students if s['average'] >= 60)

    print(f"\nClass Statistics:")
    print(f"  Total Students: {len(students)}")
    print(f"  Class Average: {class_avg:.1f}")
    print(f"  Passing: {passing}/{len(students)} ({passing/len(students)*100:.0f}%)")

def save_report(students, filename):
    """ذخیره گزارش در فایل."""
    with open(filename, 'w') as file:
        file.write("STUDENT GRADE REPORT\n")
        file.write("="*50 + "\n\n")

        for student in students:
            file.write(f"{student['name']}: {student['average']:.1f} ({student['grade']})\n")

    print(f"Report saved to {filename}")

# اجرای برنامه
if __name__ == "__main__":
    main()
```

---

## بخش ۴: تست و رفع اشکال

### موارد تست برای در نظر گرفتن

```python
# تست ۱: عملیات عادی
def test_normal_operation():
    """تست با داده معتبر."""
    students = read_student_data("grades.txt")
    assert len(students) > 0
    assert all('name' in s for s in students)
    assert all('average' in s for s in students)
    print("✓ Normal operation test passed")

# تست ۲: فایل گم شده
def test_missing_file():
    """تست با فایل ناموجود."""
    students = read_student_data("nonexistent.txt")
    assert students == []
    print("✓ Missing file test passed")

# تست ۳: فایل خالی
def test_empty_file():
    """تست با فایل خالی."""
    # ایجاد فایل خالی
    open("empty.txt", 'w').close()
    students = read_student_data("empty.txt")
    assert students == []
    print("✓ Empty file test passed")

# تست ۴: داده نامعتبر
def test_invalid_data():
    """تست با داده نامعتبر."""
    # ایجاد فایل با داده بد
    with open("bad_data.txt", 'w') as f:
        f.write("Alice,abc,def\n")  # نمرات غیرعددی

    students = read_student_data("bad_data.txt")
    # باید به خوبی مدیریت شود
    print("✓ Invalid data test passed")

# اجرای تمام تست‌ها
if __name__ == "__main__":
    test_normal_operation()
    test_missing_file()
    test_empty_file()
    test_invalid_data()
    print("\nAll tests passed!")
```

### مشکلات رایج و راه‌حل‌ها

| مشکل | راه‌حل |
|------|--------|
| فایل یافت نشد | بررسی نام و مسیر فایل |
| خطاهای فرمت داده | افزودن try-except برای تجزیه |
| تقسیم بر صفر | بررسی لیست نمرات خالی |
| حلقه منو برای همیشه اجرا می‌شود | اطمینان از کارکرد شرط خروج |
| نمایش نامرتب | استفاده از فرمت‌بندی رشته |

---

## بخش ۵: بهترین شیوه‌ها برای ساختن پروژه

### ۱. کوچک شروع کنید

```python
# همه چیز را یکجا نسازید

# بد: نوشتن ۲۰۰ خط، تست در انتها
# (باگ‌های زیاد، سخت برای یافتن)

# خوب: نوشتن ۱۰-۲۰ خط، فوراً تست
# (باگ‌ها را زود تشخیص دهید، در حالی که زمینه تازه است اصلاح کنید)
```

### ۲. استفاده از کنترل نسخه (اختیاری اما توصیه شده)

```bash
# ذخیره نقاط عطف هنگام ساخت:
git add gradebook.py
git commit -m "Step 1: File reading works"

git add gradebook.py
git commit -m "Step 2: Calculations added"

git add gradebook.py
git commit -m "Step 3: Menu system working"
```

### ۳. مستندسازی کد

```python
def calculate_average(scores):
    """
    Calculate the average of a list of scores.

    Args:
        scores: List of numeric scores

    Returns:
        Average as float, or 0 if list is empty

    Example:
        >>> calculate_average([80, 90, 100])
        90.0
    """
    if not scores:
        return 0
    return sum(scores) / len(scores)
```

### ۴. مدیریت موارد لبه

```python
def calculate_average(scores):
    """محاسبه میانگین با مدیریت موارد لبه."""

    # مورد لبه ۱: لیست خالی
    if not scores:
        return 0

    # مورد لبه ۲: حاوی مقادیر غیرعددی
    try:
        scores = [float(s) for s in scores]
    except ValueError:
        return None

    # مورد عادی
    return sum(scores) / len(scores)
```

### ۵. جداسازی مسئولیت‌ها

```python
# grade_reader.py - مدیریت عملیات فایل
def read_grades(filename):
    pass

# grade_calculator.py - مدیریت محاسبات
def calculate_averages(students):
    pass

# grade_display.py - مدیریت خروجی
def display_report(students):
    pass

# main.py - هماهنگی همه چیز
def main():
    students = read_grades("grades.txt")
    calculate_averages(students)
    display_report(students)
```

---

## بخش ۶: چک‌لیست پروژه

قبل از اعلام "تمام" پروژه:

- [ ] **عملکرد اصلی کار می‌کند**
  - می‌تواند داده ورودی را بخواند
  - می‌تواند درست پردازش کند
  - می‌تواند خروجی تولید کند

- [ ] **مدیریت خطا**
  - فایل‌های گم شده مدیریت شده‌اند
  - داده بد مدیریت شده است
  - ورودی نامعتبر کاربر مدیریت شده است

- [ ] **تجربه کاربر**
  - دستورالعمل‌های واضح
  - پیام‌های آموزنده
  - استفاده آسان

- [ ] **کیفیت کد**
  - توابع کوچک (<۲۰ خط)
  - نام‌های متغیر واضح
  - کامنت‌های لازم

- [ ] **تست**
  - موارد عادی کار می‌کنند
  - موارد لبه مدیریت شده‌اند
  - بدون crash

---

## نکات کلیدی

1. **قبل از کدنویسی برنامه‌ریزی کنید** - ابتدا مسئله را درک کنید
2. **کوچک شروع کنید** - یک قطعه را کار کنید، سپس بیشتر اضافه کنید
3. **مکرر تست کنید** - باگ‌ها را زود تشخیص دهید
4. **خطاها را مدیریت کنید** - برنامه خود را قوی کنید
5. **مسئولیت‌ها را جدا کنید** - به بخش‌های منطقی تقسیم کنید
6. **کد خود را مستند کنید** - به آینده خود (و دیگران) کمک کنید

---

## مطالعه بیشتر

- **بعدی**: جلسه ۲۲ - مرور و گام‌های بعدی
- **تمرین**: یک پروژه کامل را خودتان بسازید
- **چالش**: افزودن ویژگی‌هایی به دفتر نمرات (مرتب‌سازی، جستجو، نمودار)
- **کاوش**: آموختن الگوهای طراحی برای پروژه‌های بزرگ‌تر
