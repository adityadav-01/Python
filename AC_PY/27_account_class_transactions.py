#  Create Account class with 2 attributes - balance & account no. 
# Create methods for debit, credit & printing the balance.


# Account class definition
class Account:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        print(f"₹{amount} credited to Account {self.account_no}")

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} debited from Account {self.account_no}")
        else:
            print("Insufficient balance!")

    def print_balance(self):
        print(f"Account {self.account_no} Balance: ₹{self.balance}")

# Test the class
acc1 = Account("SB123456", 5000)

acc1.print_balance()
acc1.credit(1000)
acc1.debit(3000)
acc1.debit(5000)  # should show warning
acc1.print_balance()
