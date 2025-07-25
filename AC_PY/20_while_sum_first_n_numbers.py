# WAP to find the sum of first n numbers. (using while)

# Input from user
n = int(input("Enter a number (n): "))

# Initialize
i = 1
total = 0

# while loop to find sum
while i <= n:
    total += i
    i += 1

# Output
print(f"Sum of first {n} natural numbers is: {total}")
