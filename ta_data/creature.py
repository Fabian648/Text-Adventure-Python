
# Attribute eines wesens
"""
Health
Strength
Inventory
Mana
Skills
"""

class Creature:

    def __init__(self, max_health, health=None, max_mana=0, mana=None, skills=[], inventory=[], strength=1):
        self.max_health = max_health
        self.max_mana = max_mana
        self.strength = strength
        self.inventory = inventory 
        self.skills = skills
        if health == None:
            self.health = max_health
        else:
            self.health = health
        if mana == None:
            self.mana = max_mana
        else:
            self.mana = mana
