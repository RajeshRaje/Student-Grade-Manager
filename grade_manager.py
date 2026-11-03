students = []


def get_grade(mark):
    """Return the grade for a mark from 0 to 100."""
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


def add_student():
    """Ask for a student's name and mark, validate them, and store the student."""
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty. Student was not added.")
        return

    mark_text = input("Enter mark (0-100): ").strip()

    try:
        mark = float(mark_text)
    except ValueError:
        print("Invalid mark. Please enter a number between 0 and 100.")
        return

    if not 0 <= mark <= 100:
        print("Mark must be between 0 and 100. Student was not added.")
        return

    # A list of dictionaries allows students with the same name.
    students.append({"name": name, "mark": mark, "grade": get_grade(mark)})
    print(f"{name} was added successfully.")


def show_results():
    """Display all student results and class statistics."""
    if not students:
        print("\nNo student records yet. Add a student first.")
        return

    print("\n{:<20} {:>8} {:>8}".format("Name", "Mark", "Grade"))
    print("-" * 38)

    for student in students:
        print(
            "{:<20} {:>8.1f} {:>8}".format(
                student["name"], student["mark"], student["grade"]
            )
        )

    marks = [student["mark"] for student in students]
    average = sum(marks) / len(marks)

    print("-" * 38)
    print(
        f"Average: {average:.1f}    "
        f"Highest: {max(marks):.1f}    "
        f"Lowest: {min(marks):.1f}"
    )


def main():
    """Run the menu until the user chooses to quit."""
    while True:
        print("\n===== Student Grade Manager =====")
        print("1. Add Student")
        print("2. Show Results")
        print("3. Quit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            show_results()
        elif choice == "3":
            print("Thank you for using Student Grade Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram stopped safely. Goodbye!")
