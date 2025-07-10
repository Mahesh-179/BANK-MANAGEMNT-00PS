from Bank_Manage import Bank, Person

def main():
    print("Welcome to the Bank Management System")
    person_name = input("Enter your name: ")
    user = Person(person_name)

    while True:
        print("\n===== MENU =====")
        print("1. Create New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Show All Accounts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            acc_no = input("Enter new account number: ")
            balance = float(input("Enter initial balance: "))
            user.create_account(acc_no, balance)

        elif choice == '2':
            acc_no = input("Enter account number: ")
            account = user.accounts.get(acc_no)
            if account:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            else:
                print("Account not found.")

        elif choice == '3':
            acc_no = input("Enter account number: ")
            account = user.accounts.get(acc_no)
            if account:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            else:
                print("Account not found.")

        elif choice == '4':
            print(f"\n{user.name}'s Accounts:")
            for acc in user.accounts.values():
                acc.display()

        elif choice == '5':
            print("Thank you for using our system.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
