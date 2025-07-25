#  WAP to count the number of students with the “A” grade in the following tuple.
#  [”C”, “D”, “A”, “A”, “B”, “B”, “A”]

# Count number of students with "A" grade
grade = ("C", "D", "A", "A", "B", "B", "A")
print(f"The number of students who got 'A' Grade is: {grade.count('A')}")

# Store the above values in a list & sort them from “A” to “D”.
lis = list(grade)
print(f"List: {lis}")

# Sort the list (in-place)
lis.sort()
print(f"Sorted list (A to D): {lis}")
