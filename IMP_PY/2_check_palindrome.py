# 2. Check for palindrome 

s =input("Enter a string :")

# Remove spaces and convert to lowercase (optional step for general cases)
a = s.replace(" ","").lower()

if a==a[::-1]:
    print("It's Palindrome ")
else:
    print("NO its not a palidrome")