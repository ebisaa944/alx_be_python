shopping_list = []

def display_menu():
    """Displays the shopping list manager menu"""
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def add_item(item):
    """Adds an item to the shopping list"""
    shopping_list.append(item)
    print(f"Added '{item}' to the list")

def remove_item(item):
    """Removes an item from the shopping list"""
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
        for item in shopping_list:
            print(f"- {item}")

# Example usage
if __name__ == "__main__":
    display_menu()
    # Add more interactive logic here