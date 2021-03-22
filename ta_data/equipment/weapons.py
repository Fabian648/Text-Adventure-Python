import sys
sys.path.append(".")

class Weapon:
    def __init__(self, damage, accuracy, durability=None, max_durability=100, price=0, name=None):
        self.damage = int(damage)
        self.accuracy = int(accuracy)
        self.max_durability = int(max_durability)
        self.price = int(price)
        self.name = name
        if durability == None:
            self.durability = int(max_durability)
        else:
            self.durability = int(durability)

class MeleeWeapon(Weapon):
    def __init__(self, damage=1, accuracy=1, durability=None, max_durability=100, price=0, name="Fist"):
        super().__init__(damage=damage, accuracy=accuracy, durability=durability, max_durability=max_durability, price=price, name=name)


class RangedWeapon(Weapon):
    def __init__(self, damage, accuracy, durability, max_durability, range=2, price=None, name="Pebel"):
        super().__init__(damage=damage, accuracy=accuracy, durability=durability, max_durability=max_durability, price=price, name=name)
        self.range = range
