#  You are given a list of subjects for students. Assume one classroom is required for 1 subject.
#  How many classrooms are needed by all students.
#  ”python”, “java”, “C++”, “python”, “javascript”,
#  “java”, “python”, “java”, “C++”, “C”

sub=['python', 'java', 'C++', 'python', 'javascript','java', 'python', 'java', 'C++', 'C']

uni_sub=set(sub)

print(f"total unique subject are : {uni_sub}")
print(f"nummber of class needed :{len(uni_sub)}")