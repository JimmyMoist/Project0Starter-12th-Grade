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
        section_content = (f'\n{self.name}: "{self.dialogue}"\n'
                           f'Description: {self.desc}\n'
                           f'Inventory: {[item.name for item in self.inv]}\n'
                           f'HP: {self.hp}\n'
                           f'Power: {self.power}\n'
                           f'Race: {self.race}\n')
        print(section_content)

    def check_health(self):
        if self.hp <= 0:
            print(f"{self.name} has died.")
            # Assuming current_scene is defined somewhere, you can remove the character from the scene
            current_scene.characters.remove(self)
        else:
            print(f"{self.name} has {self.hp} HP remaining.")

    def fight(self, enemy):
        print(f"\n{enemy.name} is now fighting {self.name}.")
        while self.hp > 0 and enemy.hp > 0:
            # Character attacks the enemy (player)
            print(f"\n{self.name} attacks {enemy.name}.")
            enemy.hp -= self.power
            enemy.check_health()

            # Enemy (player) attacks the character
            print(f"\n{enemy.name} attacks {self.name}.")
            self.hp -= enemy.pwr
            self.check_health()
            if self.hp <= 0:
                print(f"{self.name} has been defeated.")
                return  # End the fight when the character dies
