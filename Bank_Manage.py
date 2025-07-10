class Bank:
    def __init__(self, name, account_no, balance=0):
        self.name = name
        self.account_no = account_no
        self.balance = balance

    def display(self):
        print("Name:", self.name)
        print("Account No:", self.account_no)
        print("Balance:", self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited NPR {amount} in your account.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount < 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Successfully withdrew NPR {amount} from your account.")


class Person:
    def __init__(self, name):
        self.name = name
        self.accounts = {}  # Dictionary to store account_no: Bank object

    def create_account(self, account_no, initial_balance=0):
        if account_no in self.accounts:
            print(f"Account {account_no} already exists.\n")
        else:
            new_account = Bank(self.name, account_no, initial_balance)
            self.accounts[account_no] = new_account
            print(f"Account {account_no} successfully created!\n")
