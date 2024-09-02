#TODO: make random items in each scene, make an ending for the game, make a combat system, make a selling system

from player import Player
from character import Character
from item import *
from scene import Scene

# Introduction
print(r"""_______   ________  ________  ________  ________  ________  ________  ________  ________
 _________  ___  ___  _______           ________  ________  _____ ______   _______      
|\___   ___\\  \|\  \|\  ___ \         |\   ____\|\   __  \|\   _ \  _   \|\  ___ \     
\|___ \  \_\ \  \\\  \ \   __/|        \ \  \___|\ \  \|\  \ \  \\\__\ \  \ \   __/|    
     \ \  \ \ \   __  \ \  \_|/__       \ \  \  __\ \   __  \ \  \\|__| \  \ \  \_|/__  
      \ \  \ \ \  \ \  \ \  \_|\ \       \ \  \|\  \ \  \ \  \ \  \    \ \  \ \  \_|\ \ 
       \ \__\ \ \__\ \__\ \_______\       \ \_______\ \__\ \__\ \__\    \ \__\ \_______\
        \|__|  \|__|\|__|\|_______|        \|_______|\|__|\|__|\|__|     \|__|\|_______|
_______   ________  ________  ________  ________  ________  ________  ________  ________
""", end="")

print(r"""
   ___           _         _  __        __    __                     __  ___   
  / _ )  __ __  (_)       / |/ / ___ _ / /_  / /  ___ _  ___        /  |/  /   
 / _  | / // / _         /    / / _ `// __/ / _ \/ _ `/ / _ \      / /|_/ /  _ 
/____/  \_, / (_)       /_/|_/  \_,_/ \__/ /_//_/\_,_/ /_//_/     /_/  /_/  (_)
       /___/                                                                   
""")

print("*************************************************************************************************************************************************")
print("Welcome to The Game! You are a young adventurer who has just started their journey. You are on a quest to find the legendary binary tree of life.\nYou will encounter many challenges and obstacles on your journey, but with courage and determination, you will be able to overcome them all.")
print("*************************************************************************************************************************************************")

# Items
commodore_64 = Item("Commodore 64", 100, "An old-ass computer")
sonic_memorabilia = Item("Sonic Memorabilia", 10, "A mini-figure of Sonic the Hedgehog")
unix_based_operating_system = Item("UNIX-based operating system", 10, "An operating system developed in the 1970s")

sword = Damage_Item("Sword", 10, "A super sharp sword", 10)
glock = Damage_Item("Glock", 100, "A gun... how did that get there?", 100)
grenade = Damage_Item("Grenade", 30, "A grenade", 50)

coffee = Heal_Item("Coffee", 10, "A cup of coffee that's gone a bit stale", 10)
comic_book = Heal_Item("Comic Book", 10, "A comic book with some sticky pages", 10)

# Characters
terry_davis = Character("Terry Davis", "A man who is a bit of a nut", [commodore_64, coffee], 9999999999, 9999999999, "hi i'm terry davis i'm the guy who made templeos", "holy shit what the fuck are these stats")
chris_chan = Character("Chris Chan", "He may or may not have done some outlandish shit", [comic_book, sonic_memorabilia], 100, 10, "Hello, I’m Chris Chan! If you’re a fan of classic comics and Sonic memorabilia, then we’re already on the same page. My life’s a bit like a comic book—full of twists, turns, and the occasional super-powered hedgehog. So, pull up a chair and let’s dive into some nostalgic fun together!", "human")
linus_torvalds = Character("Linus Torvalds", "Don't break userspace around him", [unix_based_operating_system, glock], 100, 10, "Greetings, I’m Linus Torvalds, the guy who thinks a Unix-based system can solve nearly anything, as long as you’ve got the right mindset. And yes, I’ve got a Glock for when things get intense. Don’t worry, it’s metaphorical—just a reminder that even in the tech world, you’ve got to be prepared for anything. Ready to dive into the power of Unix?", "human")
merchant_of_death = Character("Merchant", "Got traded for Brittney Griner", [sword, grenade], 100, 10, "I am the Merchant of Death, and let’s just say I have a flair for the dramatic. Whether it's a sword or a grenade, I’ve got the tools to make a statement. Life’s short, so why not live it on the edge? If you’re looking for excitement, danger, and maybe a touch of chaos, you’ve come to the right place. Now, who’s up for a bit of mayhem?", "death")

# Scenes
suburban_neighborhood = Scene("Suburban Neighborhood", "A quiet suburban neighborhood with neatly trimmed lawns and white picket fences.", [terry_davis], [])
forest = Scene("Forest", "A dense forest with towering trees and the sound of birds chirping.", [chris_chan], [])
locked_gate = Scene("Locked Gate", "A large, imposing gate that stands between you and your goal.", [linus_torvalds], [])
merchant_scene = Scene("Merchant's Hideout", "A hidden hideout where the Merchant of Death resides.", [merchant_of_death], [])

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
        break
player = Player(player_name, 100, 10, [])

# Death Screen
def death_screen():
    print("""
   ▄██████▄     ▄████████    ▄▄▄▄███▄▄▄▄      ▄████████       ▄██████▄   ▄█    █▄     ▄████████    ▄████████ 
  ███    ███   ███    ███  ▄██▀▀▀███▀▀▀██▄   ███    ███      ███    ███ ███    ███   ███    ███   ███    ███ 
  ███    █▀    ███    ███  ███   ███   ███   ███    █▀       ███    ███ ███    ███   ███    █▀    ███    ███ 
 ▄███          ███    ███  ███   ███   ███  ▄███▄▄▄          ███    ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
▀▀███ ████▄  ▀███████████  ███   ███   ███ ▀▀███▀▀▀          ███    ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
  ███    ███   ███    ███  ███   ███   ███   ███    █▄       ███    ███ ███    ███   ███    █▄  ▀███████████ 
  ███    ███   ███    ███  ███   ███   ███   ███    ███      ███    ███ ███    ███   ███    ███   ███    ███ 
  ████████▀    ███    █▀    ▀█   ███   █▀    ██████████       ▀██████▀   ▀██████▀    ██████████   ███    ███ 
                                                                                                  ███    ███ 
""", end="")
    exit()

# Game Loop
current_scene = suburban_neighborhood

def move_to_scene(scene):
    global current_scene
    current_scene = scene
    current_scene.describe()

def game_loop():
    global current_scene
    current_scene.describe()
    while True:
        action = input("\nWhat would you like to do? (move/interact/pickup/use/stats/scene): ").lower()
        
        if action == "move":
            destination = input("Where would you like to go? (forest/locked gate/suburban neighborhood/merchant): ").lower()
            if destination == "forest":
                move_to_scene(forest)
            elif destination == "locked gate":
                move_to_scene(locked_gate)
            elif destination == "suburban neighborhood":
                move_to_scene(suburban_neighborhood)
            elif destination == "merchant":
                move_to_scene(merchant_scene)
            else:
                print("Invalid destination.")
        
        elif action == "interact":
            print(f"Characters in scene: {[char.name for char in current_scene.characters]}")
            character_name = input("Who would you like to interact with? ").lower()
            character = current_scene.interact_with_character(character_name)
            if character and character.inv:
                purchase_choice = input(f"Would you like to purchase an item from {character.name}? (yes/no): ").lower()
                if purchase_choice == "yes":
                    for idx, item in enumerate(character.inv, start=1):
                        print(f"{idx}. {item.name} - {item.price} currency")
                    item_choice = int(input("Enter the number of the item you'd like to purchase: "))
                    if 1 <= item_choice <= len(character.inv):
                        player.purchase_item(character.inv[item_choice - 1])
                    else:
                        print("Invalid choice.")
        
        elif action == "pickup":
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
        
        elif action == "scene":
            print(f"You are currently in the {current_scene.name}.")

        elif action == "die":
            death_screen()

        else:
            print("Invalid action.")

game_loop()
