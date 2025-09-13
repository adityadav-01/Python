total = 0
items = ""
while True:
    print("\n1. Tea--------10 Rs")
    print("2. Milk-------20 Rs")
    print("3. coca cola--------40 Rs")
    print("4. Burger-------100 Rs")
    print("5. Pizza------ 100 Rs")
    print("6. For Exit ------press 0")
    
    ch = int(input("\nChoose Item number : "))
    if ch == 1:
        total += 10
        items += "Tea ,"
        print(f"You Orderd {items} and Total amount : {total}")
    elif ch == 2:
        total += 20
        items += "Milk ,"
        print(f"You Orderd {items} and Total amount : {total}")
    elif ch == 3:
        total += 40
        items += "coca cola ,"
        print(f"You Orderd {items} and Total amount : {total}")
    elif ch == 4:
        total += 100
        items += "Burger ,"
        print(f"You Orderd {items} and Total amount : {total}")
    elif ch == 5:
        total += 100
        items += "Pizza "
        print(f"You Orderd {items} and Total amount : {total}")
    elif ch == 0:
        print("\nThank You ")
        break
    else:
        print("Invalid Choice ")

print("\nBill")
print(f"Items : {items}")
print(f"Total Amount to Pay :{total}")
print(f"Number of Itmes {items.count}")