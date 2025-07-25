# Write a program to check whether a given string is a palindrome.

# Input from user
text = input("Enter a string: ")

# Remove spaces and convert to lowercase (optional step for general cases)
cleaned = text.replace(" ", "").lower()

# Check palindrome
if cleaned == cleaned[::-1]:
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")
