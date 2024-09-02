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
    def check_damage(self):
        print(f"Damage: {self.damage}")
    def check_stats(self):
        self.check()
        self.check_damage()
    def use(self):
        print(f"You used {self.name}.")
        print(f"You did {self.damage} damage.")

class Heal_Item(Item):
    def __init__(self, name, price, desc, health):
        super().__init__(name, price, desc)
        self.health = health
    def check_health(self):
        print(f"Health: {self.health}")
    def check_stats(self):
        self.check()
        self.check_health()
    def use(self):
            print(f"You used {self.name}.")
            print(f"You healed {self.health} HP.")