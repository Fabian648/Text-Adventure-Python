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
            self.weapon = MeleeWeapon(damage=2, accuracy=50)
        else:
            self.weapon = weapon

class Ork(Creature):

    def __init__(self, name=None, max_health=275, health=None, max_mana=10, mana=None, skills=[{}], inventory=[{}], strength=4, money=6, weapon=None):
        super().__init__(max_health=max_health, health=health, max_mana=max_mana, mana=mana, inventory=inventory, skills=skills, strength=strength, money=money)
        if name == None:
            self.name = "Ork"
        else:
            self.name = name
        if weapon == None:
            self.weapon = MeleeWeapon(damage=8, accuracy=15)
        else:
            self.weapon = weapon

class Elf(Creature):

    def __init__(self, name=None, max_health=250, health=None, max_mana=10, mana=None, skills=[{}], inventory=[{}], strength=2, money=16, weapon=None):
        super().__init__(max_health=max_health, health=health, max_mana=max_mana, mana=mana, inventory=inventory, skills=skills, strength=strength, money=money)
        if name == None:
            self.name = "Ork"
        else:
            self.name = name
        if weapon == None:
            self.weapon = MeleeWeapon(damage=1, accuracy=75)
        else:
            self.weapon = weapon