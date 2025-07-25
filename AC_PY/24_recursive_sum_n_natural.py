#  Write a recursive function to calculate the sum of first n natural numbers. 

# Recursive function to find sum of first n natural numbers
def sum_natural(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural(n - 1)

# Calling the function
num = int(input("Enter a number: "))
print(f"Sum of first {num} natural numbers is: {sum_natural(num)}")  # call the function you can do only - print(sum_natural(num))
