
from ta_data.src.TA_Errors import InvalidStats
from ta_data.src.modules import Logger
# Attribute eines wesens
"""
Health
Strength
Inventory
Mana
Skills
"""

class Creature:

    def __init__(self, max_health, health=None, max_mana=0, mana=None, skills={}, inventory={}, strength=1, money=0):
        self.max_health = int(max_health)
        self.max_mana = int(max_mana)
        self.strength = int(strength)
        self.inventory = inventory 
        self.skills = skills
        self.money = int(money)
        if health == None:
            self.health = int(max_health)
        else:
            self.health = int(health)
        if mana == None:
            self.mana = int(max_mana)
        else:
            self.mana = int(mana)
    
     