

class BankAccount:    
    def __init__(self, account_number, owner_name):
        self.accunt_number = account_number
        self.owner_name = owner_name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False
        
    def get_balance(self):
        return self.balance
    

if __name__ == "__main__":
    account = BankAccount("123456", "John Doe")
    account.deposit(1000)
    print(account.get_balance())  # Should print 1000.0

    success = account.withdraw(500)
    print(str(success).lower())   # Should print true
    print(account.get_balance())  # Should print 500.0

    success = account.withdraw(1000)
    print(str(success).lower())   # Should print false