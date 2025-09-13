card_number = "123"
pin = "1234"
balance = 10000


user_card = input("Please enter your card number: ")

if user_card == card_number:
    user_pin = input("Enter your 4-digit PIN: ")

    if user_pin == pin:
        while True:
            print("\n--- ATM MENU ---")
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Print Statement")
            print("4. Change PIN")
            print("5. Exit")


            choice = input("Enter your choice: ")

            if choice == "1":
                print(f"Your account balance is {balance}")

            elif choice == "2":
                amount = int(input("Enter amount to withdraw: "))
                if amount <= balance:
                    balance -= amount
                    print(f"{amount} withdrawn. New balance: {balance}")
                else:
                    print("Insufficient balance.")

            elif choice == "3":
                print("\n--- Account Statement ---")
                print("Mr. Aditya Kuamr Yadav")
                print("HDFC BANK")
                print("card number : ",user_card)
                print(f"Account Balance: {balance}")
                print("Thank you for banking with us!")

            elif choice == "4":
                new_pin = input("Enter new 4-digit PIN: ")
                if len(new_pin) == 4 and new_pin.isdigit():
                    pin = new_pin
                    print("PIN changed successfully.")
                else:
                    print("Invalid PIN. Must be 4 digits.")

            elif choice == "5":
                print("Thank you! Visit again.")
                break

            else:
                print("Invalid option . Try again")
        else:
            print("Inavlid pin ")
else:
    print("Card not reconized")
