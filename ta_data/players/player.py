import sys
sys.path.append(".")

from rich import print
from ta_data.creature import Creature
from ta_data.src.TA_Errors import InvalidStats, InventoryIntegretyError




class Player(Creature):

    def __init__(self, name, max_health, health=None, max_mana=0, mana=None, skills=[], max_inventory_slots=10, inventory=[], strength=1, money=0):
        super().__init__(max_health=max_health, health=health, max_mana=max_mana, mana=mana, inventory=inventory, skills=skills, strength=strength, money=money)
        self.name = name
        self.max_inventory_slots = max_inventory_slots


def add_item_to_inventory(player, item):
    try:
        if len(player.inventory) + 1 > player.max_inventory_slots:
            raise InventoryIntegretyError
        else:
            player.inventory.append(item)
    except InventoryIntegretyError as e:
        print('Inventory full.')

def list_inventory(player):
    for item in player.inventory:
        print(f'[#8B4513]Item  %25s '% (item))

def list_player_stats(player):
    print("listing player stats:")
    print(f"%-25s [bold purple]%25s" % ("player name", player.name))
    print(f"%-25s [bold red]%25s" % ("player health", player.health))
    print(f"%-25s [bold blue]%25s" % ("player mana", player.mana))
    print(f"%-25s [bold green]%25s" % ("player strength", player.strength))
    print(f"%-25s [bold #FFD700]%25s" % ("player money", player.money))

    print(f"%-25s [bold red]%25s" % ("player max health", player.max_health))
    print(f"%-25s [bold blue]%25s" % ("player max mana", player.max_mana))
    print(f"%-25s [bold #8B4513]%25s" % ("player inventory size", player.max_inventory_slots))

