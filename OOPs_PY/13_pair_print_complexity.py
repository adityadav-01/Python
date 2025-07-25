# Write a program that prints all pairs from a list (nested loop) and mention its time complexity in a comment.

# Program to print all pairs from a list
# Time Complexity: O(n^2)

numbers = [1, 2, 3, 4]

for i in range(len(numbers)):
    for j in range(len(numbers)):
        print(f"{numbers[i]}, {numbers[j]}")


# Outer loop runs n times.
# Inner loop runs n times for each outer loop.
# So total iterations = n * n = O(n²)

