#  WAP to enter marks of 3 subjects from the user and store them in a dictionary. 
# Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

# Start with an empty dictionary
marks_dict = {}

num=int(input("Enter the number of subject : "))

# Loop 'num' times to take subject and marks
for i in range(num):
    subject = input(f"Enter name of subject {i+1}: ")
    marks = int(input(f"Enter marks for {subject}: "))
    marks_dict[subject] = marks

# Print the final dictionary
print("\nMarks Dictionary:")
print(marks_dict)
