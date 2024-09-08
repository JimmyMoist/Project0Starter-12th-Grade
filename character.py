class Character:
    def __init__(self, name, desc, inv, hp, power, dialogue, race, currency):
        self.name = name
        self.desc = desc
        self.inv = inv
        self.hp = hp
        self.power = power
        self.dialogue = dialogue
        self.race = race
        self.currency = currency

    def interact(self):
        section_content = (f'{self.name}: "{self.dialogue}"\n'
                           f'Description: {self.desc}\n'
                           f'Inventory: {[item.name for item in self.inv]}\n'
                           f'Currency: {self.currency}\n'
                           f'HP: {self.hp}\n'
                           f'Power: {self.power}\n'
                           f'Race: {self.race}')
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print(section_content) # The CIA glow in the dark
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

    def check_health(self, current_scene):
        if self.hp <= 0:
            print(f"{self.name} has died.")
            # Assuming current_scene is defined somewhere, you can remove the character from the scene
            current_scene.characters.remove(self)
        else:
            print(f"{self.name} has {self.hp} HP remaining.")

    def equip_best_weapon(self):
        best_item = None  # Initialize best_item to None
        max_damage = 0    # Keep track of the highest damage found
        for item in self.inv:
            if hasattr(item, 'damage'):  # Check if item has a 'damage' attribute
                if item.damage > max_damage:
                    best_item = item      # Update the best_item
                    max_damage = item.damage  # Update the max_damage value
        if best_item:  # If a best_item was found
            self.power += best_item.damage
            print(f"{self.name} equipped their {best_item.name} that deals {best_item.damage} damage.")
        else:
            print(f"{self.name} has no weapons to equip.")

    def fight(self, enemy, current_scene):
        print(f"{enemy.name} is now fighting {self.name}.")
        enemy.equip_best_weapon()
        self.equip_best_weapon()
        while self.hp > 0 and enemy.hp > 0:
            # Character attacks the enemy (player)
            print(f"{self.name} attacks {enemy.name} for {self.power} damage.")
            enemy.hp -= self.power
            enemy.check_health()

            # Enemy (player) attacks the character
            print(f"{enemy.name} attacks {self.name} for {enemy.pwr} damage.")
            self.hp -= enemy.pwr
            self.check_health(current_scene)
            if self.hp <= 0:
                enemy.currency += self.currency
                print(f"{enemy.name} has gained {self.currency} currency.")
                for item in self.inv:
                    enemy.inv.append(item)
                    print(f"{enemy.name} has gained {item.name} from {self.name}.")
                return  # End the fight when the character dies
