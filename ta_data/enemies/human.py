import sys
sys.path.append(".")

from ta_data.creature import Creature
from ta_data.equipment.weapons import MeleeWeapon

class Human(Creature):

    def __init__(self, name=None, max_health=200, health=None, max_mana=10, mana=None, skills=[{}], inventory=[{}], strength=2, money=4, weapon=None):
        super().__init__(max_health=max_health, health=health, max_mana=max_mana, mana=mana, inventory=inventory, skills=skills, strength=strength, money=money)
        if name == None:
            self.name = "Human"
        else:
            self.name = name
        if weapon == None:
            self.weapon = MeleeWeapon()
        else:
            self.weapon = weapon