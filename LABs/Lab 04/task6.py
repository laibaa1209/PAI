class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful! New balance is: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawal successful! New balance is: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

# Example usage:
account = BankAccount("123456789", "laiba", "2024-01-01")
account.deposit(500)     
account.withdraw(200)    
account.check_balance()  
