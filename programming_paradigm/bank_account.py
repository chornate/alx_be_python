class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance  # private attribute

    def deposit(self, amount):
        self.__account_balance += amount

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance}")

account = BankAccount(100)
account.__account_balance = 1000  # This will not work as expected
