# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items
    
    def __str__(self):
        return f"You have entered the {self.name}\n{self.description}"

    def available_items(self):
        if len(self.items) == 0:
            print("There's nothing in this room.")
        else:
            print("In here, you find:\n")
            for i in self.items:
                print(f"{self.items}: {self.description}")