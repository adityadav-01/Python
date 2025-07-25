# Create student class that takes name & marks of 3 subjects as arguments in constructor. 
# Then create a method to print the average.

class Stu:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg(self):
        avgg = sum(self.marks) / len(self.marks)
        print(f"Hi {self.name}, your avg marks is {avgg}")
        print(f"Your total score is {sum(self.marks)}")
        print(f"Your marks are: {self.marks}")

# Class ke baahar object banayein aur method call karein
s1 = Stu("Aditya", [45, 50, 48])
s1.avg()
     
