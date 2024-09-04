from player import Player
from character import Character
from item import *
from scene import Scene
from graphics import *
from time import sleep

# Introduction
print(title_text, end="")

print(credits_text)

print(intro_text)

# Items
commodore_64 = Item("Commodore 64", 100, "An old-ass computer")
sonic_memorabilia = Item("Sonic Memorabilia", 10, "A mini-figure of Sonic the Hedgehog")
unix_based_operating_system = Item("UNIX-based operating system", 10, "An operating system developed in the 1970s")

stick = Damage_Item("Stick", 5, "A regular stick from a regular tree", 10)
sword = Damage_Item("Sword", 10, "A super sharp sword", 10)
glock = Damage_Item("Glock", 100, "A gun... how did that get there?", 100)
grenade = Damage_Item("Grenade", 30, "A grenade", 50)

shasta = Heal_Item("Shasta", 10, "A can of Shasta", 10)
water_bottle = Heal_Item("Water Bottle", 10, "A water bottle", 10)
blood_of_christ = Heal_Item("Blood of Christ", 10, "A chalice filled with the blood of Jesus Christ himself", 100000000000)
coffee = Heal_Item("Coffee", 10, "A cup of coffee that's gone a bit stale", 10)
comic_book = Heal_Item("Comic Book", 10, "A comic book with some sticky pages", 10)

# Characters
terry_davis = Character("Terry Davis", "A man who is a bit of a nut", [commodore_64, coffee], 9999999999, 9999999999, "hi i'm terry davis i'm the guy who made templeos", "holy shit what are these stats", 9999999999)
chris_chan = Character("Chris Chan", "He may have done some outlandish things", [comic_book, sonic_memorabilia], 100, 10, "Hello, I’m Chris Chan! If you’re a fan of classic comics and Sonic memorabilia, then we’re already on the same page. My life’s a bit like a comic book—full of twists, turns, and the occasional super-powered hedgehog. So, pull up a chair and let’s dive into some nostalgic fun together!", "human", 10)
linus_torvalds = Character("Linus Torvalds", "Don't break userspace around him", [unix_based_operating_system, glock], 100, 10, "Greetings, I’m Linus Torvalds, the guy who thinks a Unix-based system can solve nearly anything, as long as you’ve got the right mindset. And yes, I’ve got a Glock for when things get intense. Don’t worry, it’s metaphorical—just a reminder that even in the tech world, you’ve got to be prepared for anything. Ready to dive into the power of Unix?", "human", 10)
merchant_of_death = Character("Merchant", "Got traded for Brittney Griner", [sword, grenade], 100, 10, "I am the Merchant of Death, and let’s just say I have a flair for the dramatic. Whether it's a sword or a grenade, I’ve got the tools to make a statement. Life’s short, so why not live it on the edge? If you’re looking for excitement, danger, and maybe a touch of chaos, you’ve come to the right place. Now, who’s up for a bit of mayhem?", "death", 20)

# Scenes
suburban_neighborhood = Scene("Suburban Neighborhood", "A quiet suburban neighborhood with neatly trimmed lawns and white picket fences.", [terry_davis], [shasta], sub_graphic)
forest = Scene("Forest", "A dense forest with towering trees and the sound of birds chirping.", [chris_chan], [stick, water_bottle], forest_graphic)
locked_gate = Scene("Locked Gate", "A large, imposing gate that stands between you and your goal.", [linus_torvalds], [coffee], gate_graphic)
merchant_scene = Scene("Merchant's Hideout", "A hidden hideout where the Merchant of Death resides.", [merchant_of_death], [blood_of_christ], merchant_graphic)

# Player Setup
while(True):
    print("_______   ________  ________  ________")
    print("_______   ________  ________  ________")
    print("_______   ________  ________  ________")
    player_name = input("\nWhat is your name, warrior? ")
    if len(player_name) > 26:
        print("Your name is too long! Please choose a shorter name.")
    elif len(player_name) <= 1:
        print("Your name is too short! Please choose a longer name.")
    else:
        print(knight_graphic)
        print(f"Good luck on your journey, {player_name.title()}!")
        #for i in range(3):
        #    sleep(1)
        #    print(".")
        sleep(1)
        break

player = Player(player_name, 100, 10, [commodore_64, sonic_memorabilia, unix_based_operating_system, glock])

# Game Loop
current_scene = suburban_neighborhood

def move_to_scene(scene):
    global current_scene
    current_scene = scene
    current_scene.describe()

def check_for_win(player):
    if all(item in [i.name.lower() for i in player.inv] for item in ['commodore 64', 'sonic memorabilia', 'unix-based operating system']):
        print("You have collected all the necessary items!")
        print(binary_tree_graphic, end="")
        print("The gate opens, revealing the legendary Binary Tree of Life. You have won the game!")
        exit()

def game_loop():
    global current_scene
    current_scene.describe()
    while True:
        action = input("What would you like to do? (move/interact/pickup/use/stats): ").lower()

        if action == "move":
            print(f"You are currently in the {current_scene.name}.")
            destination = input("Where would you like to go? (forest/gate/neighborhood/hideout): ").lower()
            if destination == "forest":
                move_to_scene(forest)
            elif destination == "gate":
                check_for_win(player)
                move_to_scene(locked_gate)
                print("The gate is locked. You need all key items to proceed.")
            elif destination == "neighborhood":
                move_to_scene(suburban_neighborhood)
            elif destination == "hideout":
                move_to_scene(merchant_scene)
            else:
                print("Invalid destination.")

        elif action == "interact":
            if not current_scene.characters:
                print("No characters in current scene.")
            else:
                print(f"Characters in scene: {[char.name for char in current_scene.characters]}")
                character_name = input("Who would you like to interact with? ").lower()
                character = current_scene.interact_with_character(character_name)
                if character:
                    action = input(f"What would you like to do with {character.name}? (purchase/sell/fight/leave): ").lower()
                    if action == "purchase":
                        print("Character Inventory:")
                        for idx, item in enumerate(character.inv, start=1):
                            print(f"{idx}. {item.name} - {item.price} currency")
                        print("\n")
                        item_choice = int(input("Enter the !!!NUMBER!!! of the item you'd like to purchase: "))
                        if 1 <= item_choice <= len(character.inv):
                            player.purchase_item(character.inv[item_choice - 1])
                        else:
                            print("Invalid choice.")
                    elif action == "sell":
                        print("Player Inventory:")
                        for idx, item in enumerate(player.inv, start=1):
                            print(f"{idx}. {item.name} - {item.price} currency")
                        print("\n")
                        print(f"Character Currency: {character.currency}")
                        item_choice = int(input("Enter the !!!NUMBER!!! of the item you'd like to sell: "))
                        if 1 <= item_choice <= len(player.inv):
                            player.sell_item(player.inv[item_choice - 1], character)
                        else:
                            print("Invalid choice.")
                    elif action == "fight":
                        character.fight(player, current_scene)
                    elif action == "leave":
                        print(f"You left {character.name}.")
                    else:
                        print("Invalid action.")

        elif action == "pickup":
            if not current_scene.items:
                print("No items in current scene.")
            else:
                print(f"Items in scene: {[item.name for item in current_scene.items]}")
                item_name = input("Enter the name of the item you want to pick up: ").lower()
                item = current_scene.get_item(item_name)
                if item:
                    player.add_item(item)
                    current_scene.items.remove(item)
                else:
                    print("Item not found.")
        
        elif action == "use":
            print(f"Your inventory: {[item.name for item in player.inv]}")
            item_name = input("Enter the name of the item you want to use: ").lower()
            player.use_item(item_name)

        elif action == "stats":
            player.show_stats()

        elif action == "die":
            death_screen()

        else:
            print("Invalid action.")

# Start the game
game_loop()
