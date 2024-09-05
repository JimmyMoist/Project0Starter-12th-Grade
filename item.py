class Item:
    def __init__(self, name, price, desc):
        self.name = name
        self.price = price
        self.desc = desc

    def check(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Description: {self.desc}")

    def use(self, player):
        print(f"{player.name} looked at the {self.name}. It seems important.")
        self.check()

class Damage_Item(Item):
    def __init__(self, name, price, desc, damage):
        super().__init__(name, price, desc)
        self.damage = damage

    def attack(self, target):
        print(f"You attacked {target.name} with {self.name}.")
        print(f"You did {self.damage} damage.")
        target.hp -= self.damage
        target.check_health()

    def use(self, player):
        print(f"{player.name} looked at the {self.name}.")
        super().check()
        print(f"Damage: {self.damage}")

class Heal_Item(Item):
    def __init__(self, name, price, desc, health):
        super().__init__(name, price, desc)
        self.health = health

    def use(self, player):
        print(f"{player.name} used {self.name} and gained {self.health} HP.")
        player.hp += self.health
