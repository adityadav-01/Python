# Print the multiplication table of a number n.
# Print numbers from 100 to 1.

for i in range(10, 0, -1):       # Start from 10 |End just before 0 | Step: -1 (har baar 1 ghatao)
    print(i, end=' -> ')


n = int(input("\nEnter a number to print its multiplication table: "))
i = 1
print(f"\nMultiplication table of {n}:")

while i<=10:
    print(f"{i} X {n} = {i*n}")
    i+=1