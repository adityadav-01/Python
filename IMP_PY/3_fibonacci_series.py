# 3. Fibonacci series 
def fib(n):
    a, b=0, 1
    for _ in range(n):
        print(a,end=" ")
        a,b= b , a+b

n=int(input("Enter the number : "))
fib(n)