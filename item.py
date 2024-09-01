class Item:
    def __init__(self, name, price, desc):
        self.name = name
        self.price = price
        self.desc = desc
    def check(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Description: {self.desc}")
    def use(self):
        print(f"You used {self.name}.")

class Damage_Item(Item):
    def __init__(self, name, price, desc, damage):
        super().__init__(name, price, desc)
        self.damage = damage
    def check_stats(self):
        self.check()
        print(f"Damage: {self.damage}")

class Heal_Item(Item):
    def __init__(self, name, price, desc, health):
        super().__init__(name, price, desc)
        self.health = health
    def check_stats(self):
        self.check()
        print(f"Health Gain: {self.health}")