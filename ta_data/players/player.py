import sys
sys.path.append(".")

from ta_data.creature import Creature
from ta_data.src.TA_Errors import InvalidStats

class Player(Creature):

    def __init__(self, name, max_health, health=None, max_mana=0, mana=None, skills=[], inventory=[], strength=1):
        super().__init__(max_health, health, max_mana, mana, inventory, skills, strength)
        self.name = name

    def health_loss(self, amount):
        current_health = self.health
        if current_health - amount > 0:
            self.health -= amount
        elif current_health - amount <= 0:
            self.health = 0
        else:
            raise InvalidStats("health amount not valid " + str(current_health - amount))
    
    def heath_increase(self, amount):
        current_health = self.health
        if current_health + amount >= self.max_health:
            self.health = self.max_health
        elif current_health + amount < self.max_health:
            self.health += amount
        else:
            raise InvalidStats("health amount not valid " + str(current_health + amount))
    
        