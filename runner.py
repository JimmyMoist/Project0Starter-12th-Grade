from player import Player
from character import Character
from item import *
from scene import Scene

# Preliminary Functions

# Introduction
print(r"""
_______   ________  ________  ________  ________  ________  ________  ________  ________
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

intro = "\nWelcome to the game! You are a young adventurer who has just started their journey. You are on a quest to find the legendary binary tree of life.\nYou will encounter many challenges and obstacles on your journey, but with courage and determination, you will be able to overcome them all.\n"
print(intro.center(len(intro*2), "-"))

# Player
while(True):
    player_name = input("Now tell me, what is your name, warrior? ")
    if len(player_name) > 26:
        print("Your name is too long! Please choose a shorter name.")
    elif len(player_name) <= 1:
        print("Your name is too short! Please choose a longer name.")
    else:
        break
player = Player(player_name, 100, 10, [])

# Items
commodore_64 = Item("Commodore 64", 100, "An old-ass computer")
sonic_memorabilia = Item("Sonic Memorabilia", 10, "A mini-figure of Sonic the Hedgeehog")
unix_based_operating_system = Item("UNIX-based operating system", 10, "An operating system developed in the 1970s")

sword = Damage_Item("Sword", 10, "A super sharp sword", 10)
glock = Damage_Item("Glock", 100, "A gun... how did that get there?", 100)
grenade = Damage_Item("Grenade", 30, "A grenade", 50)

coffee = Heal_Item("Coffee", 10, "A cup of coffee that's gone a bit stale", 10)
comic_book = Heal_Item("Comic Book", 10, "A comic book with some sticky pages", 10)

# Characters
terry_davis = Character("Terry Davis", "A man who is a bit of a nut", [commodore_64, coffee], 9999999999, 9999999999, "hi i'm terry davis i'm the guy who made templeos", "human")
chris_chan = Character("Chris Chan", "A man with allegations", [comic_book, sonic_memorabilia], 100, 10, "Hello, I’m Chris Chan! If you’re a fan of classic comics and Sonic memorabilia, then we’re already on the same page. My life’s a bit like a comic book—full of twists, turns, and the occasional super-powered hedgehog. So, pull up a chair and let’s dive into some nostalgic fun together!", "human")
linus_torvalds = Character("Linus Torvalds", "A man who is a bit of a nut", [unix_based_operating_system, glock], 100, 10, "Greetings, I’m Linus Torvalds, the guy who thinks a Unix-based system can solve nearly anything, as long as you’ve got the right mindset. And yes, I’ve got a Glock for when things get intense. Don’t worry, it’s metaphorical—just a reminder that even in the tech world, you’ve got to be prepared for anything. Ready to dive into the power of Unix?", "human")
merchant_of_death = Character("Merchant of Death", "A man who is a bit of a nut", [sword, grenade], 100, 10, "I am the Merchant of Death, and let’s just say I have a flair for the dramatic. Whether it's a sword or a grenade, I’ve got the tools to make a statement. Life’s short, so why not live it on the edge? If you’re looking for excitement, danger, and maybe a touch of chaos, you’ve come to the right place. Now, who’s up for a bit of mayhem?", "death")

terry_davis.interact()
#chris_chan.interact()
#linus_torvalds.interact()
#merchant_of_death.interact()

# Scenes