# ------ Exercise 1

class BankAccount:

    def __init__(self, balance , username, password, authenticated = False):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = authenticated

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("Authentication required.")
        if amount > 0:
            self.balance += amount
            raise Exception(f"Deposited {amount}. New balance: {self.balance}")
        else:
            raise Exception("Deposit amount must be positive.")
        
    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Authentication required.")
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            raise Exception(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            raise Exception("Invalid withdrawal amount.")       
        
    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
            raise Exception("Authentication successful.")
        else:
            raise Exception("Authentication failed.")

class MinimumBalanceAccount(BankAccount):

    def __init__(self, balance, minimum_balance):
        super().__init__(balance)
        self.minimum_balance = minimum_balance
    
    def withdraw(self, amount):
        if not self.authenticated:
            return "Authentication required."
        if amount > 0 and amount <= self.balance - self.minimum_balance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        else:
            return "Invalid withdrawal amount."
        
class ATM:
    
    def __init__(self, account_list, try_limit):
        if not all(isinstance(acc, (BankAccount, MinimumBalanceAccount)) for acc in account_list):
            raise TypeError("All items in account_list must be BankAccount or MinimumBalanceAccount instances.")
        
        if not isinstance(try_limit, int) or try_limit <= 0:
            raise ValueError("try_limit must be a positive integer.")

        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0

    

    def log_in(self, username, password):
        if self.current_tries >= self.try_limit:
            raise Exception("Maximum login attempts exceeded.")

        for account in self.account_list:
            if account.username == username and account.password == password:
                account.authenticated = True
                self.current_tries = 0
                print("Login successful.")

        self.current_tries += 1
        raise Exception("Login failed.")

    def show_main_menu(self, bank_account):
        if not bank_account.authenticated:
            raise Exception("User not authenticated.")

        print(f"Welcome {bank_account.username}! What would you like to do today?")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Logout")

        choice = input("Enter your choice: ")
        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            try:
                bank_account.deposit(amount)
            except Exception as e:
                print(e)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            try:
                bank_account.withdraw(amount)
            except Exception as e:
                print(e)
        elif choice == "3":
            bank_account.authenticated = False
            print("Logged out successfully.")
        else:
            print("Invalid choice.")