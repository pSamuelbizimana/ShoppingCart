

class VendingMachine:
    def __init__(self):
        self.inventory = {}
        self.balance = 0

    def add_item(self, item_name, price, quantity):
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] += quantity
        else:
            self.inventory[item_name] = {'price': price, 'quantity': quantity}

    def remove_item(self, item_name):
        if item_name in self.inventory:
            del self.inventory[item_name]
        else:
            print("Item not found in inventory.")

    def insert_coin(self, amount):
        self.balance += amount

    def buy_item(self, item_name):
        if item_name in self.inventory:
            item = self.inventory[item_name]
            if item['quantity'] > 0:
                if self.balance >= item['price']:
                    self.balance -= item['price']
                    item['quantity'] -= 1
                    print("Item purchased:", item_name)
                else:
                    print("Insufficient balance. Please insert more coins.")
            else:
                print("Item out of stock.")
        else:
            print("Item not found in inventory.")

    def get_balance(self):
        return self.balance

    def display_inventory(self):
        print("Current Inventory:")
        for item_name, item_info in self.inventory.items():
            print(f"Item: {item_name} | Price: {item_info['price']} | Quantity: {item_info['quantity']}")


# Example usage of the VendingMachine class
vending_machine = VendingMachine()

# Add items to the inventory
vending_machine.add_item("Soda", 1.5, 10)
vending_machine.add_item("Chips", 1.0, 5)

# Display current inventory
vending_machine.display_inventory()

# Insert coins into the vending machine
vending_machine.insert_coin(1.0)
vending_machine.insert_coin(0.5)

# Buy an item
vending_machine.buy_item("Chips")

# Display current balance
balance = vending_machine.get_balance()
print("Current balance:", balance)

# Remove an item from the inventory
vending_machine.remove_item("Soda")

# Display updated inventory
vending_machine.display_inventory()
