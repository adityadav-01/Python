que= ["Capital of India\n 1. Delhi\n 2. B\n 3. C\n 4. D",
    "PM of india\n 1. A\n 2. MODI\n 3. C\n 4. D",
    "CM of UP\n 1. A\n 2. MODI\n 3. YOGI\n 4. D"]

ans = [1,2,3]
prizes = [500,20000,100000,]

print("Welcome to KBC")
total = 0
for i in range(len(que)):
    print(f"Q{i+1} : {que[i]}")
    
    an = int(input("Enter yout correct option number : "))
    
    if an == ans[i]:
        total = prizes[i]
        print(f"Correct You won {prizes[i]}")
    else:
        print("Wrong Answer. GAME OVER")
        break
print(f"You won {total}")