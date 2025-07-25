#  Create a full example that uses all 5 types of inheritance: 
# ● Make a base class Person 
# ● Use: 
# ○ Single inheritance → Student inherits Person 
# ○ Multi-level → Intern → Student → Person 
# ○ Multiple → Intern also inherits from Employee 
# ○ Hierarchical → create Teacher, Student, Staff from Person 
# ○ Hybrid → show mix of above with Researcher 

# Base class
class Person:
    def show(self):
        print("I am a Person")

# Single Inheritance
class Student(Person):
    def show_student(self):
        print("I am a Student")

# Hierarchical Inheritance
class Teacher(Person):
    def show_teacher(self):
        print("I am a Teacher")

class Staff(Person):
    def show_staff(self):
        print("I am a Staff")

# Separate class for Multiple Inheritance
class Employee:
    def show_employee(self):
        print("I am an Employee")

# Multi-level + Multiple Inheritance
class Intern(Student, Employee):
    def show_intern(self):
        print("I am an Intern")

# Hybrid Inheritance (mix of Student + Employee)
class Researcher(Student, Employee):
    def show_researcher(self):
        print("I am a Researcher")


i = Intern()
i.show()              # From Person
i.show_student()      # From Student
i.show_employee()     # From Employee
i.show_intern()       # From Intern

r = Researcher()
r.show()              # From Person
r.show_student()      # From Student
r.show_employee()     # From Employee
r.show_researcher()   # From Researcher
