class Character:
    def __init__(self, name, desc, inv, hp, power, dialogue, race):
        self.name = name
        self.desc = desc
        self.inv = inv
        self.hp = hp
        self.power = power
        self.dialogue = dialogue
        self.race = race

    def interact(self):
        print(self.dialogue + "\n")
