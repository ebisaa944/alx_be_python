shopping_list = []

def display_menu():
    """Displays the shopping list manager menu"""
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def add_item():
    """Adds an item to the shopping list"""
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"Added '{item}' to the list")

def remove_item():
    """Removes an item from the shopping list"""
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Removed '{item}' from the list")
    else:
        print(f"'{item}' not found in the list")

def view_list():
    """Displays all items in the shopping list"""
    if not shopping_list:
        print("Your shopping list is empty")
    else:
        print("Your Shopping List:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                add_item()
            elif choice == 2:
                remove_item()
            elif choice == 3:
                view_list()
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1-4.")
        except ValueError:
            print("Please enter a number between 1 and 4")

if __name__ == "__main__":
    main()