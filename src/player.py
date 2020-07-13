# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.items = []
        # self.walk = walk
        # self.pickup = pickup
        # self.drop = drop
    
    def who(self):
        print(f"Your character's name is {self.name}")

    # def where_with(self):
    #     print(f"You are now in the {self.location}.\nHere, you find {room.item}")

    def walk(self, direction):
        new_room = getattr(self.location, f"{direction}_to")

        if new_room != None:
            self.location = new_room
            print(f"\nYou are now in the {self.location}.\n")
        else:
            print("\nYou hit a dead end. Go a different direction.")

    def pickup(self, this_item):
        if len(self.location.items) == 0:
            print(f"\nThe {self.location.name} is empty. There's nothing for you here.")
        else:
            for i in self.location.items:
                if i.name == this_item:
                    self.items.append(i)
                    self.location.items.remove(i)
                    print(f"You now have {this_item}!")
    
    def drop(self, this_item):
        if len(self.items) == 0:
            print("You can't drop what you don't have.")
        else:
            for i in self.items:
                if i.name == this_item:
                    self.items.remove(i)
                    self.location.append(i)
                    print(f"You've dropped your {i.name}.")