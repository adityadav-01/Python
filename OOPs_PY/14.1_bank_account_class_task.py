# Create a class BankAccount with: 
# ● Attributes: acc_no, holder_name, balance 
# ● Methods: 
# ○ deposit(amount) → adds money 
# ○ withdraw(amount) → subtracts (if enough balance) 
# ○ display() → prints details 
# Add: 
# ● Class variable: bank_name = "SBI" 
# ● Private variable: __balance 
# ● In withdraw(), check if sufficient balance. Else, show warning. 
#  Try using 2 objects and test different deposits and withdrawals.


class BankAccount:
    bank = "SBI"  # Class variable

    def __init__(self, acc_no, holder_name, balance):
        self.acc_no = acc_no
        self.holder_name = holder_name
        self.__balance = balance  # Encapsulated → private we can acess it through only method

    def deposit(self, amount):
        self.__balance += amount
        print(f"Dear {self.holder_name}, in your bank {BankAccount.bank}, Rs {amount} has been credited.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Dear {self.holder_name}, in your bank {BankAccount.bank}, Rs {amount} has been debited.")
        else:
            print(f"Insufficient balance for {self.holder_name}. Cannot withdraw Rs {amount}.")

    def display(self):
        print(f"\nAccount Details for {self.holder_name}:")
        print(f"Bank: {BankAccount.bank}")
        print(f"Account No: {self.acc_no}")
        print(f"Current Balance: Rs {self.__balance}")


# Creating 2 objects
s1 = BankAccount("SBI8181", "Aditya Yadav", 100)
s2 = BankAccount("CBN7570", "Rohan Yadav", 500)

# Testing deposits and withdrawals
s1.deposit(300)    # Aditya: Rs 100 + 300 = 400
s2.withdraw(400)   # Rohan: Rs 500 - 400 = 100

# Displaying details
s1.display()
s2.display()