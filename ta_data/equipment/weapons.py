import sys
sys.path.append(".")

class Weapon:
    def __init__(self, id, damage, accuracy, durability=None, max_durability=100, price=0, name=None, range=0):
        self.id = int(id)
        self.damage = int(damage)
        self.accuracy = int(accuracy)
        self.max_durability = int(max_durability)
        self.price = int(price)
        self.name = name
        self.range = range
        if durability == None:
            self.durability = int(max_durability)
        else:
            self.durability = int(durability)

class MeleeWeapon(Weapon):
    def __init__(self, id=0, damage=1, accuracy=1, durability=None, max_durability=100, price=0, name="Fist", range=0):
        super().__init__(id=id, damage=damage, accuracy=accuracy, durability=durability, max_durability=max_durability, price=price, name=name, range=range)


class RangedWeapon(Weapon):
    def __init__(self, id, damage, accuracy, durability, max_durability, range=2, price=None, name="Pebel"):
        super().__init__(id=id, damage=damage, accuracy=accuracy, durability=durability, max_durability=max_durability, price=price, name=name, range=range)
        self.range = range

