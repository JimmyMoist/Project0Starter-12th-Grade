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
        print(section_content)
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

    def check_health(self, current_scene):
        if self.hp <= 0:
            print(f"{self.name} has died.")
            # Assuming current_scene is defined somewhere, you can remove the character from the scene
            current_scene.characters.remove(self)
        else:
            print(f"{self.name} has {self.hp} HP remaining.")

    def fight(self, enemy, current_scene):
        print(f"{enemy.name} is now fighting {self.name}.")
        enemy.equip_best_weapon()
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
                print(f"{self.name} has been defeated.")
                enemy.currency += self.currency
                return  # End the fight when the character dies
