# Use a lambda function to cube a number and apply it to a list using map().

y=int(input("Enter a number : "))
cube= lambda x : x**3
print(cube(y))

# for list

# Original list
numbers = [1, 2, 3, 4, 5]

# Lambda function inside map to cube each number
cubed_numbers = list(map(lambda x: x**3, numbers))

# Print result
print("Original list:", numbers)
print("Cubed list:", cubed_numbers)