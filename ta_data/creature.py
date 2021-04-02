
from ta_data.equipment.weapons import MeleeWeapon
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

    def __init__(self, name, max_health, health, max_mana, mana, strength, money, weapon):
        self.name = name
        self.max_health = max_health
        self.max_mana = max_mana
        self.strength = strength
        self.money = money
        self.health = health
        self.mana = mana
        self.weapon = weapon
    
     