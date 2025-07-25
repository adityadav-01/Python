#  WAF to find the factorial of n. (n is the parameter)

# Function to find factorial
def find_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Calling the function
num = int(input("Enter a number: "))
print(f"Factorial of {num} is {find_factorial(num)}")
