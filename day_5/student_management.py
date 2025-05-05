class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def display_student(self):
        self.display_info()
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")


student1 = Student("Manoj", 21, "101", "Python")
student2 = Student("Kumar", 18, "102", "Java")
student3 = Student("Ramesh", 22, "103", "Python Full Stack")

student1.display_student()
student2.display_student()
student3.display_student()
