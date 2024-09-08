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
            print(f"{self.name} has died.")
            self.death_screen()
        else:
            print(f"{self.name} has {self.hp} HP remaining.")
    
    def add_item(self, item):
        self.inv.append(item)
        print(f"Added {item.name} to inventory.")

    def purchase_item(self, item):
        if self.currency >= item.price:
            self.currency -= item.price
            print(f"Purchased {item.name} for {item.price} currency.")
            self.add_item(item)
        else:
            print("Not enough currency to purchase this item.")

    def sell_item(self, item, buyer):
        if item in self.inv:
            if buyer.currency >= item.price:
                sell_price = item.price
                self.currency += sell_price
                self.inv.remove(item)
                buyer.inv.append(item)
                buyer.currency -= sell_price
                print(f"Sold {item.name} for {sell_price} currency.")
            else:
                print("Buyer doesn't have enough currency.")
        else:
                print("Item not found in inventory.")

    def use_item(self, item_name):
        for item in self.inv:
            if item.name.lower() == item_name.lower():
                item.use(self)
                return
        print("Item not found in inventory.")

    def equip_best_weapon(self):
        best_item = None  # Initialize best_item to None
        max_damage = 0    # Keep track of the highest damage found
        for item in self.inv:
            if hasattr(item, 'damage'):  # Check if item has a 'damage' attribute
                if item.damage > max_damage:
                    best_item = item      # Update the best_item
                    max_damage = item.damage  # Update the max_damage value
        if best_item:  # If a best_item was found
            self.pwr += best_item.damage
            print(f"{self.name} equipped their {best_item.name} that deals {best_item.damage} damage.")
        else:
            print(f"{self.name} has no weapons to equip.")
