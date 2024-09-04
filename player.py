death_text = r"""
   ▄██████▄     ▄████████    ▄▄▄▄███▄▄▄▄      ▄████████       ▄██████▄   ▄█    █▄     ▄████████    ▄████████ 
  ███    ███   ███    ███  ▄██▀▀▀███▀▀▀██▄   ███    ███      ███    ███ ███    ███   ███    ███   ███    ███ 
  ███    █▀    ███    ███  ███   ███   ███   ███    █▀       ███    ███ ███    ███   ███    █▀    ███    ███ 
 ▄███          ███    ███  ███   ███   ███  ▄███▄▄▄          ███    ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
▀▀███ ████▄  ▀███████████  ███   ███   ███ ▀▀███▀▀▀          ███    ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
  ███    ███   ███    ███  ███   ███   ███   ███    █▄       ███    ███ ███    ███   ███    █▄  ▀███████████ 
  ███    ███   ███    ███  ███   ███   ███   ███    ███      ███    ███ ███    ███   ███    ███   ███    ███ 
  ████████▀    ███    █▀    ▀█   ███   █▀    ██████████       ▀██████▀   ▀██████▀    ██████████   ███    ███ 
                                                                                                  ███    ███ 
"""

class Player:
    def __init__(self, name, hp, pwr, inv, currency=0):
        self.name = name
        self.hp = hp
        self.pwr = pwr
        self.inv = inv
        self.currency = currency

    def show_stats(self):
        print(f"--- {self.name.title()} Stats ---")
        print(f"HP: {self.hp}")
        print(f"Power: {self.pwr}")
        print(f"Inventory: {[item.name for item in self.inv]}")
        print(f"Currency: {self.currency}")

    # Death Screen
    def death_screen(self):
        print(death_text, end="")
        print("better luck next time lol")
        exit()

    def check_health(self):
        if self.hp <= 0:
            print(f"\n{self.name} has died.")
            self.death_screen()
        else:
            print(f"{self.name} has {self.hp} HP remaining.")
    
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

    def sell_item(self, item, buyer):
        if item in self.inv:
            sell_price = item.price
            self.currency += sell_price
            self.inv.remove(item)
            buyer.inv.append(item)
            buyer.currency -= sell_price
            print(f"Sold {item.name} for {sell_price} currency.")
        else:
            print("Item not found in inventory.")

    def use_item(self, item_name):
        for item in self.inv:
            if item.name.lower() == item_name.lower():
                item.use(self)
                return
        print("Item not found in inventory.")
