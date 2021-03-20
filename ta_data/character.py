
# Attribute eines wesens
"""
Health
Strength
Inventory
Mana
Skills
"""

class Character:

    def __init__(self, entity):
        self.health = self.health(entity)
        self.strength = self.strength(entity)
        self.inventory = self.inventory(entity)
        self.mana = self.mana(entity)
        self.skills = self.skills(entity)

    def health(self):
        
        pass

    def strength(self):
        pass

    def inventory(self):
        pass

    def mana(self):
        pass

    def skills(self):
        pass