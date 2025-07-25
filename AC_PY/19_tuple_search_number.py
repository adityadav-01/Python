#  Search for a number x in this tuple using loop:
#  [1, 4, 9, 16, 25, 36, 49, 64, 81,100] 

num=(1,4,99,16,25,36,49,64,81,100,)

x=int(input("Enter the number to search : "))
for i in num:
    if i==x:
        print("found")
        break
    else:
        print("not found ")
        break