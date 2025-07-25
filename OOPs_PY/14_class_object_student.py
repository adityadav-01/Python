# Create a Student class with attributes name and roll, and a method display() to print 
# them. Create 2 student objects and call the method.

# Student class definition
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll}")

# Creating 2 student objects
student1 = Student("Aditya", 101)
student2 = Student("Sneha", 102)

# Calling display method for each
student1.display()
student2.display()
