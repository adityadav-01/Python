#  WAP to find the greatest of 3 numbers entered by the user.

# Step 1: Input three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Step 2: Compare using if-else
if num1 >= num2 and num1 >= num3:
    greatest = num1
elif num2 >= num1 and num2 >= num3:
    greatest = num2
else:
    greatest = num3

# Step 3: Print result
print("The greatest number is:", greatest)

# Program to find greatest among 3 numbers using map() and max()

a, b, c = map(int, input("Enter 3 numbers separated by space: ").split())

print("Greatest number among these 3 numbers is:", max(a, b, c))