class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance  # Private balance attribute

    def deposit(self, amount):
        """Adds the specified amount to the account balance."""
        self.__account_balance += amount

    def withdraw(self, amount):
        """Attempts to withdraw the specified amount.
        
        Returns True if successful, False if there are insufficient funds.
        """
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Prints the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.__account_balance:.2f}")

