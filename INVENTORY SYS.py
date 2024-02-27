
def add_item(item_name, quantity):
  """Adds an item to the inventory or updates its quantity if it already exists.

  Args:
      item_name: The name of the item to add.
      quantity: The quantity of the item to add.
  """
  if item_name in inventory:
    inventory[item_name] += quantity
  else:
    inventory[item_name] = quantity

def get_item_info(item_name):
  """Retrieves information about a specific item in the inventory.

  Args:
      item_name: The name of the item to get information about.

  Returns:
      A string indicating the quantity of the item or a message if not found.
  """
  if item_name in inventory:
    return f"{item_name} has {inventory[item_name]} in stock."
  else:
    return f"Item '{item_name}' not found in inventory."

def total_quantity():
  """Calculates the total quantity of all items in the inventory.

  Returns:
      The total quantity of all items in the inventory.
  """
  total = 0
  for item, quantity in inventory.items():
    total += quantity
  return total

def main():
  """Runs the inventory management system."""
  while True:
    print("\nInventory Management System")
    print("1. Add item")
    print("2. Get item information")
    print("3. Total quantity")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
      item_name = input("Enter item name: ")
      quantity = int(input("Enter quantity: "))
      add_item(item_name, quantity)
      print(f"Item '{item_name}' added successfully.")
    elif choice == "2":
      item_name = input("Enter item name: ")
      print(get_item_info(item_name))
    elif choice == "3":
      total_qty = total_quantity()
      print(f"Total quantity of all items: {total_qty}")
    elif choice == "4":
      print("Exiting inventory system...")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
