class Character:
    def __init__(self, name, desc, inv, hp, power, dialogue, race):
        self.name = name
        self.desc = desc
        self.inv = inv
        self.hp = hp
        self.power = power
        self.dialogue = dialogue
        self.race = race

    def section_box(self, section):
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print(section)
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

    def interact(self):
        section_content = (f'{self.name}: "{self.dialogue}"\n\n'
                           f'Description: {self.desc}\n'
                           f'Inventory: {self.inv}\n'
                           f'HP: {self.hp}\n'
                           f'Power: {self.power}\n'
                           f'Race: {self.race}')
        
        self.section_box(section_content)