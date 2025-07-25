# Task 3: Prefix Sum Array 
# Question: 
# Given array → return prefix sum array 
# Input: [2, 4, 6]   
# Output: [2, 6, 12] 
# Tips: 
# ● Keep sum_so_far variable 
# ● Loop and build a new list using it 
#-------------------------------------------

def pref(arr):
    new = []
    su = 0

    for num in arr:
        su += num
        new.append(su)

    return new

arr = [10, 20, 30, 50, 40]
result = pref(arr)
print(f"new array with prefix is : {result} ")