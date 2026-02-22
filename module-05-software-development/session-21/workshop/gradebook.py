# Session 21 Workshop: Student Gradebook
# Complete implementation of the gradebook program

def read_grades(filename):
    """Read student data from file and return list of dictionaries"""
    students = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Parse each line: "Name,score1,score2,score3"
                parts = line.strip().split(',')
                if len(parts) >= 2:  # At least name and one score
                    name = parts[0]
                    scores = []
                    for score in parts[1:]:
                        try:
                            scores.append(float(score))
                        except ValueError:
                            print(f"Warning: Invalid score '{score}' for {name}, skipping")
                    if scores:  # Only add if we have valid scores
                        students.append({'name': name, 'scores': scores})
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
        return []
    return students

def calculate_average(scores):
    """Calculate average of a list of scores"""
    if not scores:
        return 0.0
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

def generate_report(students):
    """Generate and display grade report"""
    if not students:
        print("No student data available")
        return

    print("\n" + "="*60)
    print("STUDENT GRADE REPORT")
    print("="*60)
    print("<25")
    print("-" * 60)

    for student in students:
        avg = calculate_average(student['scores'])
        letter = get_letter_grade(avg)
        status = get_grade_status(avg)

        print("<25")

    # Calculate class statistics
    all_scores = [score for student in students for score in student['scores']]
    class_avg = calculate_average(all_scores) if all_scores else 0
    pass_count = sum(1 for s in students if calculate_average(s['scores']) >= 60)

    print("-" * 60)
    print("<25")
    print(".1f")
    print(f"Students Passing: {pass_count}/{len(students)} ({pass_count/len(students)*100:.1f}%)")

def show_statistics(students):
    """Show detailed class statistics"""
    if not students:
        print("No data available")
        return

    all_scores = [score for student in students for score in student['scores']]

    print("\nClass Statistics:")
    print(f"Total students: {len(students)}")
    print(f"Total scores recorded: {len(all_scores)}")
    print(".2f")
    print(".2f")
    print(f"Highest score: {max(all_scores)}")
    print(f"Lowest score: {min(all_scores)}")

    # Grade distribution
    grades = [get_letter_grade(calculate_average(s['scores'])) for s in students]
    print("\nGrade Distribution:")
    for grade in ['A', 'B', 'C', 'D', 'F']:
        count = grades.count(grade)
        print(f"{grade}: {count} students")

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
            show_statistics(students)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()