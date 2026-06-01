from datetime import date

class Person:


 person1=Person()
print(person1)
class Person: 
    def __init__(self, name, age, date_of_birth):
        if not first_name:
           raise ValueError("First name cannot be empty")
        if not last_name:
              raise ValueError("Last name cannot be empty")
        if not dob:
              raise ValueError("Date of birth cannot be empty")
  
       
    # Set instance variables 
        self.name = name
        self.age = age
        self.dob = dob

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_age(self):
        today = date.today()
        age = today.year - self.dob.year
        print(type(age))
        return age
    



    def __str__(self):
        return(f"Name: {self.get_full_name()}\n"
               f"Date of Birth: {self.dob}\n")

    

    # Driver Code
    Person 1 = Person("Willa", "Johnston", date(2010,1 ,1))
    print(Person.first_name)
    

    class Student(Person):
        student1 = Student("Willa", "Johnston", date(2010,1 ,1))
        print(student1.get_full_name())
        print(student1.get_age())
        print(student1)                  
        print(student1.finish_year)

        def get_year(self):
            pass

    
    teacher1 = Teacher("Barbara", "O'Malley", date(1962, 1, 1), ["Math", "Computing Technology","Software Engineering"])
        print(teacher1.get_full_name())
        print(teacher1.get_age())
        print(teacher1.classes)
        print(teacher1.add_classes("STEM"))




