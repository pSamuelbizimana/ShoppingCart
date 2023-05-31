
class Item:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.cart_items = []

    def add(self, item: Item):
        self.cart_items.append(item)

    def total(self) -> int:
        return sum(item.price for item in self.cart_items)

    def __len__(self):
        return len(self.cart_items)

if __name__ == '__main__':
    # Example usage of the Item and ShoppingCart classes
    item1 = Item("Shirt", 20)
    item2 = Item("Pants", 30)
    item3 = Item('shoes',100)

    cart = ShoppingCart()
    cart.add(item1)
    cart.add(item2)
    cart.add(item3)

    total_price = cart.total()
    print("Total price:", total_price)

    num_items = len(cart)
    print("Number of items:", num_items)
