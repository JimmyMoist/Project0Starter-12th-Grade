class Scene:
    def __init__(self, name, desc, characters, items, graphic):
        self.name = name
        self.desc = desc
        self.characters = characters
        self.items = items
        self.graphic = graphic

    def describe(self):
        print(f"\n--- {self.name} ---")
        print(self.graphic)
        print(self.desc)
        print(f"Characters: {[char.name for char in self.characters]}")
        print(f"Items: {[item.name for item in self.items]}")

    def get_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def interact_with_character(self, character_name):
        for character in self.characters:
            if character.name.lower() == character_name.lower():
                character.interact()
                return character
        print("Character not found.")
        return None
