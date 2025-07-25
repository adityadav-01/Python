#  WAP to find the factorial of first n numbers. (using for)

# User se input le rahe hain — kitne numbers tak factorial chahiye
n = int(input("Enter a number (n): "))

# Outer loop: 1 se n tak har number ka factorial nikalenge
for i in range(1, n + 1):
    
    # har i ke liye fact ko 1 se initialize karna hoga
    fact = 1

    # Inner loop: 1 se i tak multiply karte jao (1 × 2 × ... × i)
    for j in range(1, i + 1):
        fact *= j  # fact = fact × j

    # har i ke baad uska factorial print kar do
    print(f"Factorial of {i} is {fact}")
