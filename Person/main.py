try:
    from colorama import init, Fore, Style
except Exception:
    # Provide fallbacks if colorama is not available
    def init():
        return None

    class _Empty:
        RESET_ALL = ""
        BRIGHT = ""
        GREEN = ""
        BLUE = ""
        YELLOW = ""
        CYAN = ""

    Fore = _Empty()
    Style = _Empty()
from datetime import date
from person import Person
from student import Student
from teacher import Teacher

print(Fore.GREEN + Style.BRIGHT + "Welcome to the Person Information System!" + Style.RESET_ALL)
print(Fore.BLUE + "You can enter information about a student or a teacher." + Style.RESET_ALL)
print(Fore.YELLOW + "Let's get started!" + Style.RESET_ALL)
print(Fore.CYAN + "Please follow the prompts to enter the required information." + Style.RESET_ALL)


def main():
    person_type = input("Enter the type of person (student/teacher): ").upper()
    if person_type not in ["S", "T"]:
        raise ValueError("Invalid Input.")
    elif person_type == "S":
        student = get_student_info()
        print(student)
        print(f"Age: {student.get_age()}years")
    else:
        teacher = get_teacher_info()
        print(teacher)
        print(f"Age: {teacher.get_age()}years")

def get_basic_info():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    date_of_birth = input("Date of birth (YYYY-MM-DD): ")
    return first_name, last_name, date_of_birth

def get_student_info():
    first_name, last_name, date_of_birth = get_basic_info()
    finish_year = input("Finish year: ")
    return Student(first_name, last_name, date_of_birth, finish_year)

def get_teacher_info():
    first_name, last_name, date_of_birth = get_basic_info()
    classes_input = input("Subjects you teach. Place a comma after each subject: ").split(",")
    classes = [class_name.strip() for class_name in classes_input]
    return Teacher(first_name, last_name, date_of_birth, classes)

if __name__ == "__main__":
    init()
    main()