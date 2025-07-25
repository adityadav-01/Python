#  Task 1: Core Operations 
# Question: 
# Write a Python program to: 
# ● Take array input from user 
# ● Sort the array 
# ● Reverse it 
# ● Find max, min, average 
# ● Delete element by value 
# ● Insert a value at position 
# Tips: 
# ● Use arr.append(), arr.sort(), arr.reverse(), arr.remove() 
# ● Use sum(arr), max(arr), min(arr) 
#---------------------------------------------------------------------


# 1. User se input lena aur usko list of integers mein convert karna
arr = list(map(int, input("Enter array elements separated by space: ").split()))

# 2. Array ko sort karna
arr.sort()
print("Sorted array:", arr)

# 3. Array reverse
arr.reverse()
print("Reversed array:", arr)

# 4. Max, Min, Average
print("Maximum:", max(arr))
print("Minimum:", min(arr))
print("Average:", sum(arr) / len(arr))

# 5. Delete element by value
val_to_remove = int(input("Enter value to delete: "))
if val_to_remove in arr:
    arr.remove(val_to_remove)
    print("After deletion:", arr)
else:
    print("Value not found in array.")

# 6. Insert value at position
value = int(input("Enter value to insert: "))
position = int(input("Enter position (0-based index): "))

if 0 <= position <= len(arr):
    arr.insert(position, value)
    print("After insertion:", arr)
else:
    print("Invalid position")