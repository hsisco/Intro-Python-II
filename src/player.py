# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def move_rooms(self, direction):
        room = self.location
        move = f"{direction}_to"
        if hasattr(room, move):
            self.location = getattr(room, move)
            return True
        else:
            print("You've hit a dead end. Try another direction.")
            return False