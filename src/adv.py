from room import Room
from player import Player

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance", """North of you, the cave mount beckons"""),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),
    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
welcome = "\nWE'RE GOING ON A TREASURE HUNT!\n💰🔱👑💍✨🏆💎🤩\n\nNavigate through the house using your compass 🧭\nEnter N, S, E or W.\n\nEnter Q to quit.\n"
print(welcome)

# Make a new player object that is currently in the 'outside' room.
player = Player(input("What is your name? : "), room['outside'], None, None, None)

# Write a loop that:
#
# * Waits for user input and decides what to do.

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
if len(player.name) == 1:
    playing = True

print(f"Where do you want to go? : " + {action})

def move(player, direction):
    new_room = None
    if direction == "n":
        new_room = player.location.n_to
    elif direction == "s":
        new_room = player.location.s_to
    elif direction == "e":
        new_room = player.location.e_to
    elif direction == "w":
        new_room = player.location.w_to
    # if new_room == None:
    #     print("You hit a dead end. Go a different direction")
    else:
        player.location = new_room

while playing = True:
    if action == "n" or "N" or "North" or "north":
        move(player, "n")
    elif action == "s" or "S" or "South" or "south":
        move(player, "s")
    elif action == "e" or "E" or "East" or "east":
        move(player, "e")
    elif action == "w" or "W" or "West" or "west":
        move(player, "w")
    elif action == "q" or "Q" or "Quit" or "quit":
        playing = False
    else:
        print(f"Where do you want to go? : " + {action})

