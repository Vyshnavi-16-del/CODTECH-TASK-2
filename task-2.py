def calculate_letter_grade(average):
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

def calculate_gpa(average):
    if average >= 90:
        return 4.0
    elif average >= 80:
        return 3.0
    elif average >= 70:
        return 2.0
    elif average >= 60:
        return 1.0
    else:
        return 0.0

def main():
    print("Welcome to the Student Grade Tracker!")
    
    grades = []
    
    while True:
        subject = input("Enter the subject name (or type 'done' to finish): ")
        if subject.lower() == 'done':
            break
        try:
            grade = float(input(f"Enter the grade for {subject}: "))
            grades.append(grade)
        except ValueError:
            print("Invalid input. Please enter a numeric value for the grade.")
            continue

    if not grades:
        print("No grades entered.")
        return
    
    average_grade = sum(grades) / len(grades)
    letter_grade = calculate_letter_grade(average_grade)
    gpa = calculate_gpa(average_grade)
    
    print("\nGrade Summary:")
    print(f"Average Grade: {average_grade:.2f}")
    print(f"Letter Grade: {letter_grade}")
    print(f"GPA: {gpa:.1f}")

# Run the grade tracker
main()
