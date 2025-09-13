students = []
averages = []
info = int(input("How many students data you want to enter: "))
print("Total number of students:", info)

for i in range(1, info + 1):
    print(f"\nEnter student details {i}:")
    name = input(f"Enter student name {i}: ")
    print("Enter marks :-")
    math = int(input("Enter maths marks: "))
    science = int(input("Enter science marks: "))
    english = int(input("Enter english marks: "))
    
    avg = (math + science + english) / 3
    averages.append(avg)
    
    a = [name, math, science, english, avg]
    students.append(a)

print("\nAll Student Data:")
print(students)

highmark = 0
topper = ""

for i in range(len(averages)):
    if averages[i] > highmark:
        highmark = averages[i]
        topper = students[i][0] 

print(f"\nTopper is {topper} with highest average {highmark}")
