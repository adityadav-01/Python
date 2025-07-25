# Write a recursive function to print all elements in a list.
#  Hint : use list & index as parameters.

# Recursive function to print all elements in a list
def print_list_elements(lst, index):
    if index == len(lst):
        return  # base case: agar index list se bahar chala gaya to stop
    print(lst[index])
    print_list_elements(lst, index + 1)  # recursion: next element

# Sample list
my_list = ["apple", "banana", "cherry", "date"]

# Function call with list and starting index 0
print_list_elements(my_list, 0)
