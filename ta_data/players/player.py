import sys
sys.path.append(".")

from ta_data.creature import Creature
from ta_data.src.TA_Errors import InvalidStats, InventoryIntegretyError

class Player(Creature):

    def __init__(self, name, max_health, health=None, max_mana=0, mana=None, skills=[], max_inventory_slots=10, inventory=[], strength=1, money=0):
        super().__init__(max_health=max_health, health=health, max_mana=max_mana, mana=mana, inventory=inventory, skills=skills, strength=strength, money=money)
        self.name = name
        self.max_inventory_slots = max_inventory_slots
    
    def add_item_to_inventory(self, item):
        try:
            if len(self.inventory) + 1 > self.max_inventory_slots:
                raise InventoryIntegretyError
            else:
                self.inventory.append(item)
        except InventoryIntegretyError as e:
            print('Inventory full.')

    def list_inventory(self):
        for item in self.inventory:
            print('Item   ', item)