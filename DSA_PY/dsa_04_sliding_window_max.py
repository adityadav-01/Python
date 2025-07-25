# dsa_04_sliding_window_max.py
# Find maximum sum of any subarray of size k. 
# Input: arr = [1, 4, 2, 10, 23, 6], k = 3   
# Output: 39 (subarray [10,23,6]) 
# Tips: 
# ● Keep window sum, slide forward by subtracting arr[i - k] and adding arr[i]

def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        print("Array size is smaller than k")
        return None

    # Step 1: Pehle k elements ka sum nikal lo
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Step 2: Loop chalao k se n tak
    for i in range(k, n):
        # window ko slide karo:
        # pehla element minus + naya element add
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Input
arr = [1, 4, 2, 10, 23, 6]
k = 3

# Function call
result = max_sum_subarray(arr, k)
print(f"Maximum sum of subarray of size {k} is: {result}")
