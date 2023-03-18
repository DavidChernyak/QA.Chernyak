class BankAccount:
    def __init__(self, account_number, balance, owner_name):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name

    def deposit(self, amount):
        self.balance += amount
        return (self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        return (self.balance)

    def get_balance(self):
        return (self.balance)

    def transfer(self, to_account, amount):
        self.withdraw(amount)
        to_account.deposit(amount)