
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
        self.max_health = max_health
        self.max_mana = max_mana
        self.strength = strength
        self.inventory = inventory 
        self.skills = skills
        self.money = money
        if health == None:
            self.health = max_health
        else:
            self.health = health
        if mana == None:
            self.mana = max_mana
        else:
            self.mana = mana

    
    def health_loss(self, amount):
        current_health = self.health
        if current_health - amount > 0:
            self.health -= amount
        elif current_health - amount <= 0:
            self.health = 0
        else:
            raise InvalidStats("health amount not valid " + Logger.lineno())
    
    def heath_increase(self, amount):
        current_health = self.health
        if current_health + amount >= self.max_health:
            self.health = self.max_health
        elif current_health + amount < self.max_health:
            self.health += amount
        else:
            raise InvalidStats("health amount not valid " + Logger.lineno())
    
     