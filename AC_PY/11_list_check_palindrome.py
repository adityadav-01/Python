#  WAP to check if a list contains a palindrome of elements. Hint: use copy( ) method

og_list=[]
# Step 1: Take number of elements
num = int(input("Enter how many elements you want in the list: "))

# Step 2: Take input elements one by one
for i in range(num):
    lis=input(f"Enter element {i+1} : ")
    og_list.append(lis)
print(f"Your original list is : {og_list}")

rev=og_list.copy()
print(f"Your reverse list is : {rev}")

rev.reverse()
# Step 4: Check palindrome using list reverse
if og_list==rev:
    print("It is a palindrome list.")
else:
    print("It is NOT a palindrome list.")