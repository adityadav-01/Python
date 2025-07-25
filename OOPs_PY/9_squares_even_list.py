# Use list comprehension to generate a list of squares of even numbers from 1 to 20.

num=[x for x in range(21) if x % 2==0]
ss=[x**2 for x in num ]
print(num, ss)


# in one line :
even=[x**2 for x in range(1,21) if x % 2 ==0]
print(even)
