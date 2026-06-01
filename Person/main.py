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
    return Teacher(first_name, last_name, dob classes)

if__name__ == "__main__":
    main()