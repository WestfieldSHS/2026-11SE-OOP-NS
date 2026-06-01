from datetime import date


class Teacher(Person):
    def __init__(self, name, age, date_of_birth, classes):
        super().__init__(name, age, date_of_birth)
        self.classes = classes

    def add_classes(self, class_name):
        print(f"{class_name} to be added to class list.")
        self.classes.append(class_name)
       
       # Driver code
       
    teacher1 = Teacher("Barbara", "O'Malley", date(1962, 1, 1), ["Math", "Computing Technology","Software Engineering"])
    print(teacher1.get_full_name())
    print(teacher1.get_age())
    print(teacher1.classes)
    teacher1.add_classes("STEM")