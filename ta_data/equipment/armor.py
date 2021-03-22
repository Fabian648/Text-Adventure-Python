import sys
sys.path.append(".")


class Armor:
    def __init__(self, defence, durability=None, max_durability=100):
        self.defence = defence
        self.max_durability = max_durability
        if durability == None:
            self.durability = durability
        else:
            self.durability = durability