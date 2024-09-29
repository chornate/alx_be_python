def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Initialize an empty list
    
    while True:
        display_menu()  # Display menu options
        choice = input("Enter your choice: ")

        if choice == '1':
            # Correct prompt for adding an item
            item = input("Enter the item to add: ")
            pass  # Logic for adding the item to the list
        
        elif choice == '2':
            # Logic for removing an item from the shopping list
            pass
        
        elif choice == '3':
            # Logic for displaying the shopping list
            pass
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
