import sys
from bank_account import BankAccount

def main():
    # Create an instance of BankAccount with an example starting balance of 100
    account = BankAccount(100)

    # Check if the user provided a command via command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Split the command and amount (if provided)
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Perform the requested command
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
