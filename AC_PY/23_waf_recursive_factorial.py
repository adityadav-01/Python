# Function to find factorial using recursion
def find_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * find_factorial(n - 1)

# Calling the function
num = int(input("Enter a number: "))
print(f"Factorial of {num} is {find_factorial(num)}")
