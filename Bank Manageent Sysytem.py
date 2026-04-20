class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_no, name, balance):
        self.accounts[acc_no] = {"name": name, "balance": balance}
        print("Account created successfully.")

    def deposit(self, acc_no, amount):
        if acc_no in self.accounts:
            self.accounts[acc_no]["balance"] += amount
            print("Amount deposited.")
        else:
            print("Account not found.")

    def withdraw(self, acc_no, amount):
        if acc_no in self.accounts:
            if self.accounts[acc_no]["balance"] >= amount:
                self.accounts[acc_no]["balance"] -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient balance.")
        else:
            print("Account not found.")

    def check_balance(self, acc_no):
        if acc_no in self.accounts:
            print("Balance:", self.accounts[acc_no]["balance"])
        else:
            print("Account not found.")


# Menu-driven program
bank = Bank()

while True:
    print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        acc_no = input("Enter Account Number: ")
        name = input("Enter Name: ")
        balance = float(input("Enter Initial Balance: "))
        bank.create_account(acc_no, name, balance)

    elif choice == "2":
        acc_no = input("Enter Account Number: ")
        amount = float(input("Enter Amount: "))
        bank.deposit(acc_no, amount)

    elif choice == "3":
        acc_no = input("Enter Account Number: ")
        amount = float(input("Enter Amount: "))
        bank.withdraw(acc_no, amount)

    elif choice == "4":
        acc_no = input("Enter Account Number: ")
        bank.check_balance(acc_no)

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")