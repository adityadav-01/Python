# Create a dictionary to store your name, age, and city. Then print each value.

adi={"Name" : "Aditya ", 'Age ': 20,'City ': 'Ballia'}
print(adi)


# User se input le rahe hain
user_input = input("Enter numbers separated by space: ")

# List bana rahe hain split karke
my_list = [int(x) for x in user_input.split()]

print("Your list:", my_list)
