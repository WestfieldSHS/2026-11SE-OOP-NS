from datetime import date

class Person:
    def __init__(self, first_name, last_name, dob):
        if not first_name:
            raise ValueError("First name cannot be empty")
        if not last_name:
            raise ValueError("Last name cannot be empty")
        if not dob:
            raise ValueError("Date of birth cannot be empty")

        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_age(self):
        today = date.today()
        return today.year - self.dob.year

    def __str__(self):
        return (f"Name: {self.get_full_name()}\n"
                f"Date of Birth: {self.dob}\n")


class Student(Person):
    def __init__(self, first_name, last_name, dob, finish_year=None):
        super().__init__(first_name, last_name, dob)
        self.finish_year = finish_year

    def get_year(self):
        return self.finish_year


class Teacher(Person):
    def __init__(self, first_name, last_name, dob, classes=None):
        super().__init__(first_name, last_name, dob)
        self.classes = classes or []

    def add_classes(self, cls):
        self.classes.append(cls)
        return self.classes


if __name__ == "__main__":
    p = Person("Willa", "Johnston", date(2010, 1, 1))
    print(p.get_full_name())
    print(p.get_age())

    student1 = Student("Willa", "Johnston", date(2010, 1, 1), finish_year=2028)
    print(student1.get_full_name())
    print(student1.get_age())
    print(student1.finish_year)

    teacher1 = Teacher("Barbara", "O'Malley", date(1962, 1, 1), ["Math", "Computing Technology", "Software Engineering"])
    print(teacher1.get_full_name())
    print(teacher1.get_age())
    print(teacher1.classes)
    print(teacher1.add_classes("STEM"))




