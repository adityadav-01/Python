num = int(input("Enter number of visitor : "))
tic = 0

for i in range(1,num + 1):
    age = int(input(f"Enter age of visitor {i} : "))
    
    if 0<= age <5:
        fee = 0
        cat = "New Born"
    elif 5<= age <12:
        fee = 20
        cat = "Child"
    elif 12 <= age <60:
        fee = 50
        cat = "Adult"
    else:
        fee = 30
        cat = "Senior Citizens"
    
    print(f"Visitor {i} : Age {age} - {cat} , Ticket Rs. {fee}")
    tic+=fee
print(f"\nTotal Amount collected today : Rs. {tic} ")