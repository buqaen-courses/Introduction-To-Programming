# Project Planning: From Idea to Working Program

## Introduction: Building Real Programs

So far, you've learned Python basics. Now it's time to combine everything into **real programs** that solve real problems. This guide shows you how to plan, build, and complete a programming project.

### The Programming Process

```
1. Understand the Problem
   ↓
2. Plan the Solution
   ↓
3. Build Step by Step
   ↓
4. Test and Debug
   ↓
5. Improve and Polish
```

---

## Part 1: Understanding the Problem

### Read the Requirements Carefully

**Example Project**: Build a Student Gradebook

**Requirements Analysis**:

```
What does it need to do?
├── Input
│   ├── Read student names and scores from a file
│   └── Handle errors (missing file, bad data)
├── Processing
│   ├── Calculate averages for each student
│   ├── Assign letter grades
│   └── Calculate class statistics
├── Output
│   ├── Display formatted report
│   └── Save report to file
└── User Interface
    ├── Menu system for choices
    └── Clear instructions
```

### Ask Questions

Before writing code, clarify:
- What format is the input data?
- What should happen with errors?
- Who will use this program?
- What does "success" look like?

**Example Data Format Discussion**:

```
grades.txt format:
Alice Johnson,85,92,78
Bob Smith,76,88,91

Questions:
- What if a line is blank? → Skip it
- What if scores are missing? → Error message
- What if name has commas? → Use quotes or different delimiter
```

---

## Part 2: Planning the Solution

### Break Down into Functions

Don't try to write the whole program at once. Break it into small pieces:

```python
# gradebook.py - Initial plan (no code yet!)

def read_student_data(filename):
    """Read data from file and return list of students."""
    pass  # TODO: implement

def calculate_average(scores):
    """Calculate average of a list of scores."""
    pass  # TODO: implement

def get_letter_grade(average):
    """Convert numeric average to letter grade."""
    pass  # TODO: implement

def generate_report(students):
    """Create formatted report from student data."""
    pass  # TODO: implement

def save_report(report, filename):
    """Save report to file."""
    pass  # TODO: implement

def show_menu():
    """Display user menu."""
    pass  # TODO: implement

def main():
    """Main program loop."""
    pass  # TODO: implement
```

### Create a Flow Diagram

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

### Plan Your Data Structures

```python
# What does student data look like?
student = {
    'name': 'Alice Johnson',
    'scores': [85, 92, 78],
    'average': 85.0,
    'grade': 'B'
}

# How do we store multiple students?
students = [
    {'name': 'Alice', 'scores': [85, 92, 78], ...},
    {'name': 'Bob', 'scores': [76, 88, 91], ...},
    ...
]
```

---

## Part 3: Building Step by Step

### Step 1: Start with the Simplest Version

Get one small piece working first:

```python
# Step 1: Just read the file

def read_student_data(filename):
    """Read data from file."""
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

# Test it immediately!
if __name__ == "__main__":
    students = read_student_data("grades.txt")
    print(f"Read {len(students)} students")
    for student in students:
        print(f"  {student['name']}: {student['scores']}")
```

### Step 2: Add One Feature at a Time

```python
# Step 2: Add calculations

def calculate_average(scores):
    """Calculate average of scores."""
    if not scores:
        return 0
    return sum(scores) / len(scores)

def get_letter_grade(average):
    """Convert average to letter grade."""
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

# Update read function to include calculations
def read_student_data(filename):
    """Read data from file with calculations."""
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

# Test again
if __name__ == "__main__":
    students = read_student_data("grades.txt")
    for student in students:
        print(f"{student['name']}: {student['average']:.1f} ({student['grade']})")
```

### Step 3: Add User Interface

```python
# Step 3: Add menu system

def show_menu():
    """Display menu options."""
    print("\n" + "="*40)
    print("STUDENT GRADEBOOK")
    print("="*40)
    print("1. Load and Display Grades")
    print("2. Show Class Statistics")
    print("3. Save Report to File")
    print("4. Exit")
    print("="*40)

def get_choice():
    """Get user choice."""
    while True:
        choice = input("Enter choice (1-4): ").strip()
        if choice in ['1', '2', '3', '4']:
            return choice
        print("Invalid choice. Please enter 1-4.")

def main():
    """Main program loop."""
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

# Helper functions
def display_grades(students):
    """Display student grades."""
    print("\nStudent Grades:")
    print("-" * 40)
    for student in students:
        print(f"{student['name']:<20} {student['average']:>6.1f} {student['grade']:>3}")

def show_statistics(students):
    """Show class statistics."""
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
    """Save report to file."""
    with open(filename, 'w') as file:
        file.write("STUDENT GRADE REPORT\n")
        file.write("="*50 + "\n\n")

        for student in students:
            file.write(f"{student['name']}: {student['average']:.1f} ({student['grade']})\n")

    print(f"Report saved to {filename}")

# Run the program
if __name__ == "__main__":
    main()
```

---

## Part 4: Testing and Debugging

### Test Cases to Consider

```python
# Test 1: Normal operation
def test_normal_operation():
    """Test with valid data."""
    students = read_student_data("grades.txt")
    assert len(students) > 0
    assert all('name' in s for s in students)
    assert all('average' in s for s in students)
    print("✓ Normal operation test passed")

# Test 2: Missing file
def test_missing_file():
    """Test with non-existent file."""
    students = read_student_data("nonexistent.txt")
    assert students == []
    print("✓ Missing file test passed")

# Test 3: Empty file
def test_empty_file():
    """Test with empty file."""
    # Create empty file
    open("empty.txt", 'w').close()
    students = read_student_data("empty.txt")
    assert students == []
    print("✓ Empty file test passed")

# Test 4: Invalid data
def test_invalid_data():
    """Test with invalid data."""
    # Create file with bad data
    with open("bad_data.txt", 'w') as f:
        f.write("Alice,abc,def\n")  # Non-numeric scores

    students = read_student_data("bad_data.txt")
    # Should handle gracefully
    print("✓ Invalid data test passed")

# Run all tests
if __name__ == "__main__":
    test_normal_operation()
    test_missing_file()
    test_empty_file()
    test_invalid_data()
    print("\nAll tests passed!")
```

### Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| File not found | Check filename and path |
| Data format errors | Add try-except for parsing |
| Division by zero | Check for empty score lists |
| Menu loops forever | Ensure exit condition works |
| Display looks messy | Use string formatting |

---

## Part 5: Best Practices for Project Building

### 1. Start Small

```python
# Don't try to build everything at once

# BAD: Write 200 lines, test at the end
# (Will have many bugs, hard to find)

# GOOD: Write 10-20 lines, test immediately
# (Catch bugs early, fix while context is fresh)
```

### 2. Use Version Control (Optional but Recommended)

```bash
# Save checkpoints as you build:
git add gradebook.py
git commit -m "Step 1: File reading works"

git add gradebook.py
git commit -m "Step 2: Calculations added"

git add gradebook.py
git commit -m "Step 3: Menu system working"
```

### 3. Document Your Code

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

### 4. Handle Edge Cases

```python
def calculate_average(scores):
    """Calculate average with edge case handling."""

    # Edge case 1: Empty list
    if not scores:
        return 0

    # Edge case 2: Contains non-numeric values
    try:
        scores = [float(s) for s in scores]
    except ValueError:
        return None

    # Normal case
    return sum(scores) / len(scores)
```

### 5. Separate Concerns

```python
# grade_reader.py - Handles file operations
def read_grades(filename):
    pass

# grade_calculator.py - Handles calculations
def calculate_averages(students):
    pass

# grade_display.py - Handles output
def display_report(students):
    pass

# main.py - Orchestrates everything
def main():
    students = read_grades("grades.txt")
    calculate_averages(students)
    display_report(students)
```

---

## Part 6: Project Checklist

Before declaring your project "done":

- [ ] **Core functionality works**
  - Can read input data
  - Can process correctly
  - Can produce output

- [ ] **Error handling**
  - Missing files handled
  - Bad data handled
  - Invalid user input handled

- [ ] **User experience**
  - Clear instructions
  - Informative messages
  - Easy to use

- [ ] **Code quality**
  - Functions are small (<20 lines)
  - Clear variable names
  - Comments where needed

- [ ] **Testing**
  - Normal cases work
  - Edge cases handled
  - No crashes

---

## Key Takeaways

1. **Plan before coding** - Understand the problem first
2. **Start small** - Get one piece working, then add more
3. **Test frequently** - Catch bugs early
4. **Handle errors** - Make your program robust
5. **Separate concerns** - Split into logical parts
6. **Document your code** - Help future you (and others)

---

## Further Reading

- **Next**: Session 22 - Review and next steps
- **Practice**: Build one complete project on your own
- **Challenge**: Add features to your gradebook (sorting, searching, charts)
- **Explore**: Learn about design patterns for larger projects
