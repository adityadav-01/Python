# Take 2 numbers as input and divide them. Handle divide-by-zero and invalid input using try-except.
try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numbers.")

except Exception as e:
    print("Unexpected error:", e)
