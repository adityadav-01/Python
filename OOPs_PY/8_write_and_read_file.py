# Write a program to create a file, write your name and age into it, then read and print the content.

# Step 1: Write to the file
with open("info.txt", "w") as file:
    file.write("Name: Aditya\n")
    file.write("Age: 20\n")

# Step 2: Read from the file
with open("info.txt", "r") as file:
    content = file.read()

# Step 3: Print the content
print("File Content:\n" + content)
