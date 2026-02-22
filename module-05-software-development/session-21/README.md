# Session 21: Mini-Project 1 – Data Processing Script

## Session Overview

Congratulations! After 20 weeks of learning, today you get to apply everything you've learned to build your first complete Python program. We'll plan, design, implement, and test a data processing script that integrates variables, input/output, conditionals, loops, functions, file handling, and error management. This capstone project demonstrates how all the pieces fit together to solve real problems.

## Key Terms

- **Requirements gathering**: Understanding what the program needs to do
- **Incremental development**: Building features step by step
- **Integration testing**: Making sure all parts work together
- **User experience (UX)**: How easy and intuitive the program is to use
- **Edge cases**: Unusual inputs or situations the program must handle
- **Refactoring**: Improving code structure while keeping functionality

## Project Overview

You'll build a **Student Gradebook** program that:
- Reads student data from a file
- Calculates grades and statistics
- Handles various data formats
- Provides a simple text-based interface
- Includes proper error handling

## Planning Phase

### Requirements Breakdown
1. **Input**: Read student names and scores from a text file
2. **Processing**: Calculate averages, letter grades, pass/fail status
3. **Output**: Display results in a formatted report
4. **Error Handling**: Handle missing files, invalid data, etc.
5. **User Interface**: Simple menu system for different operations

### Data Format
Input file (`grades.txt`):
```
Alice Johnson,85,92,78
Bob Smith,76,88,91
Charlie Brown,95,87,93
Diana Prince,82,79,85
```

## Implementation Strategy

### Step 1: Basic File Reading
Start with the foundation - reading data from a file:

```python
def read_grades(filename):
    """Read student data from file and return list of dictionaries"""
    students = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Parse each line
                parts = line.strip().split(',')
                name = parts[0]
                scores = [int(score) for score in parts[1:]]
                students.append({'name': name, 'scores': scores})
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
        return []
    except ValueError:
        print("Error: Invalid score data in file")
        return []
    return students
```

### Step 2: Grade Calculations
Add functions to process the data:

```python
def calculate_average(scores):
    """Calculate average of a list of scores"""
    if not scores:
        return 0
    return sum(scores) / len(scores)

def get_letter_grade(average):
    """Convert numeric average to letter grade"""
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

def get_grade_status(average):
    """Return pass/fail status"""
    return "Pass" if average >= 60 else "Fail"
```

### Step 3: Report Generation
Create output formatting:

```python
def generate_report(students):
    """Generate and display grade report"""
    if not students:
        print("No student data available")
        return

    print("\n" + "="*50)
    print("STUDENT GRADE REPORT")
    print("="*50)
    print("<25")
    print("-" * 50)

    for student in students:
        avg = calculate_average(student['scores'])
        letter = get_letter_grade(avg)
        status = get_grade_status(avg)

        print("<25")

    # Calculate class statistics
    all_scores = [score for student in students for score in student['scores']]
    class_avg = calculate_average(all_scores)
    pass_count = sum(1 for s in students if calculate_average(s['scores']) >= 60)

    print("-" * 50)
    print("<25")
    print(f"Students Passing: {pass_count}/{len(students)} ({pass_count/len(students)*100:.1f}%)")
```

### Step 4: Main Program Loop
Add user interface:

```python
def main():
    """Main program function"""
    filename = "grades.txt"

    while True:
        print("\nGradebook Menu:")
        print("1. Load and display grades")
        print("2. Show class statistics")
        print("3. Exit")

        choice = input("Enter choice (1-3): ").strip()

        if choice == '1':
            students = read_grades(filename)
            generate_report(students)
        elif choice == '2':
            students = read_grades(filename)
            if students:
                show_statistics(students)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

## Testing and Debugging

### Test Cases
1. **Normal operation**: Valid file with good data
2. **Missing file**: What happens when grades.txt doesn't exist?
3. **Invalid data**: Non-numeric scores, empty lines
4. **Empty file**: What if the file exists but is empty?
5. **Edge cases**: Students with no scores, very high/low grades

### Common Issues
- File path problems
- Type conversion errors
- Division by zero (empty score lists)
- String formatting issues

## Enhancement Ideas

Once the basic version works, consider adding:
- Save reports to file
- Sort students by grade
- Individual student lookup
- Grade distribution charts
- Input validation for menu choices

## Development Process

1. **Start small**: Get file reading working first
2. **Test frequently**: Run your code after each change
3. **Add features incrementally**: Don't try to build everything at once
4. **Handle errors gracefully**: Use try/except blocks
5. **Improve formatting**: Make output readable and professional

## Summary and Checklist

### What We Covered Today
- ✅ Planning a complete program from requirements
- ✅ Integrating multiple programming concepts
- ✅ File handling, functions, loops, and conditionals
- ✅ Error handling and user input validation
- ✅ Testing and debugging strategies

### Key Skills Demonstrated
- Breaking down complex problems
- Using functions to organize code
- Handling files and data
- Creating user-friendly interfaces
- Testing for edge cases

### Key Takeaway
Programming is about solving problems by combining simple concepts into powerful solutions. You've now built a complete, useful program that could actually be used in a classroom!

## Next Steps

Our final session will review everything we've learned and give you a chance to work on a personal project. You'll also get guidance on continuing your programming journey beyond this course.

## Connection to Future Learning

This project demonstrates the skills you'll need for:
- **Web development**: Handling user data and generating reports
- **Data analysis**: Processing and analyzing datasets
- **Automation**: Writing scripts to solve real-world problems
- **Software development**: Planning, implementing, and testing larger programs

## Further Reading (Optional)

- "Python Crash Course" by Eric Matthes (Project chapters)
- Automate the Boring Stuff with Python (Chapters 8-12 on files and data)
- Real Python tutorials on file handling and data processing