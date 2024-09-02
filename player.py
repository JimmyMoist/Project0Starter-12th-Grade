class Player:
    def __init__(self, name, hp, pwr, inv, currency=0):
        self.name = name
        self.hp = hp
        self.pwr = pwr
        self.inv = inv
        self.currency = currency

    def show_stats(self):
        print(f"--- {self.name.title()} Stats ---")
        print(f"Name: {self.name}")
        print(f"HP: {self.hp}")
        print(f"Power: {self.pwr}")
        print(f"Inventory: {[item.name for item in self.inv]}")
        print(f"Currency: {self.currency}")

    def add_item(self, item):
        self.inv.append(item)
        print(f"Added {item.name} to inventory.")

    def purchase_item(self, item):
        if self.currency >= item.price:
            self.currency -= item.price
            self.add_item(item)
            print(f"Purchased {item.name} for {item.price} currency.")
        else:
            print("Not enough currency to purchase this item.")

    def use_item(self, item_name):
        for item in self.inv:
            if item.name.lower() == item_name.lower():
                item.use()
                return
        print("Item not found in inventory.")
