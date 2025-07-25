# Task 2: Two Pointer - Find Pair With Target Sum
# Question:
#  Check if any two numbers in a sorted array add up to the target.
# Input: arr = [1, 2, 4, 7, 11], target = 15  
# Output: True (4 + 11)
# Tips:
# Start with two pointers: left = 0, right = n-1
# Move left/right based on arr[left] + arr[right]
#================================================================

def has_pair_with_sum(arr, target):
    left = 0                # Starting pointer
    right = len(arr) - 1    # Ending pointer

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            print(f"Pair found: {arr[left]} + {arr[right]} = {target}")
            return True     # Pair mil gaya

        elif current_sum < target:
            left += 1       # Sum chhota hai, bada karne ke liye left aage badhao

        else:
            right -= 1      # Sum zyada hai, kam karne ke liye right peeche lao

    return False            # Agar loop khatam ho gaya to pair nahi mila

# Sample Input
arr = [1, 2, 4, 7, 11]
target = 15

# Function call
result = has_pair_with_sum(arr, target)
print("Result:", result)


#=========================================================================

# 🔹 Two Pointer ka matlab:
# Ek pointer start se (left)
# Dusra pointer end se (right)
# 🔹 Jab tak left < right:
# current_sum = arr[left] + arr[right]
# Agar current_sum == target → ✅ Mil gaya
# Agar current_sum < target → sum badhaana padega → left += 1
# Agar current_sum > target → sum ghataana padega → right -= 1