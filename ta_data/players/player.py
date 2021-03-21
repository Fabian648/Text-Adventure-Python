import sys
sys.path.append(".")

from ta_data.creature import Creature
from ta_data.src.TA_Errors import InvalidStats

class Player(Creature):

    def __init__(self, name, max_health, health=None, max_mana=0, mana=None, skills=[], inventory=[], strength=1, money=0):
        super().__init__(max_health=max_health, health=health, max_mana=max_mana, mana=mana, inventory=inventory, skills=skills, strength=strength, money=money)
        self.name = name
   